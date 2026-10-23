
from generator import generate_verses


story = """
A boy finds a thirsty bird near a tree.
He gives the bird some water.
The bird becomes happy and flies away.
"""

try:
    result = generate_verses(story, number_of_candidates=5)

    print("\nSTORY SUMMARY")
    print(result.get("story_summary", ""))

    print("\nGENERATED CANDIDATES")

    for candidate in result["candidates"]:
        print(f"\nCandidate {candidate.get('id', '?')}")

        for i, pada in enumerate(candidate["padas"], start=1):
            print(f"Pada {i}: {pada}")

        print("Meaning:", candidate.get("meaning", ""))

except Exception as error:
    print("Error:", error)
