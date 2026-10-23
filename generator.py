
import json
import os

from dotenv import load_dotenv
from google import genai
from prompt import build_prompt
from validator import validate_anustubh

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=API_KEY)


def generate_once(story, number_of_candidates):
    """Generate candidates once and validate them."""

    prompt = build_prompt(story, number_of_candidates)

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    if not response.text:
        raise ValueError("The model returned an empty response.")

    try:
        result = json.loads(response.text)
    except json.JSONDecodeError as error:
        raise ValueError(
            "The model did not return valid JSON."
        ) from error

    candidates = result.get("candidates")
    print("Candidates received from Gemini:", len(candidates) if isinstance(candidates, list) else "Not a list")

    if not isinstance(candidates, list):
        raise ValueError("The candidates field is missing.")

    valid_candidates = []
    invalid_candidates = []

    for candidate in candidates:
        if not isinstance(candidate, dict):
            continue

        padas = candidate.get("padas")

        if not (
            isinstance(padas, list)
            and len(padas) == 4
            and all(
                isinstance(pada, str) and pada.strip()
                for pada in padas
            )
        ):
            continue

        verse = "\n".join(padas)
        validation = validate_anustubh(verse)

        candidate["validation"] = validation

        if validation["valid"]:
            valid_candidates.append(candidate)
        else:
            invalid_candidates.append(candidate)
    print("Valid candidates:", len(valid_candidates))
    print("Invalid candidates:", len(invalid_candidates))
    result["candidates"] = valid_candidates
    result["invalid_candidates"] = invalid_candidates
    result["valid_count"] = len(valid_candidates)
    result["invalid_count"] = len(invalid_candidates)

    return result


def generate_verses(story, number_of_candidates=5):
    """Generate candidates, retrying only when none pass validation."""

    if not story or not story.strip():
        raise ValueError("Please enter an English story.")

    max_attempts = 3
    last_result = None

    for attempt in range(1, max_attempts + 1):
        print(f"Generation attempt {attempt}/{max_attempts}...")

        result = generate_once(story, number_of_candidates)
        last_result = result

        if result["valid_count"] > 0:
            result["attempts_used"] = attempt
            return result

        print("No candidates passed validation.")

    last_result["attempts_used"] = max_attempts
    last_result["message"] = (
        "No candidates passed metre validation after "
        f"{max_attempts} attempts."
    )

    return last_result
