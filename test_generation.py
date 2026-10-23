
from generator import generate_verses

story = """
A poor woodcutter lived near a forest. One day, while cutting a tree beside a river, his axe slipped from his hand and fell into the water. He sat on the riverbank and cried because he could not afford another axe. A kind divine being appeared and showed him a golden axe, but the woodcutter said it was not his. The being then showed him a silver axe, which he also refused. Finally, the being showed him his iron axe, and the woodcutter happily accepted it. Impressed by his honesty, the being rewarded him with all three axes.
"""

try:
    result = generate_verses(story, number_of_candidates=5)

    print("Story summary:")
    print(result.get("story_summary", "No summary returned"))

    print("\nVALID CANDIDATES")
    print("================")

    if result["candidates"]:
        for candidate in result["candidates"]:
            print(f"\nCandidate {candidate.get('id', '?')}")

            for i, pada in enumerate(candidate["padas"], start=1):
                print(f"Pada {i}: {pada}")

            print("Meaning:", candidate.get("meaning", "Not provided"))
            print("Validation:", candidate["validation"]["message"])
    else:
        print("No candidates passed validation.")

    print("\nINVALID CANDIDATES")
    print("==================")

    if result["invalid_candidates"]:
        for candidate in result["invalid_candidates"]:
            print(f"\nCandidate {candidate.get('id', '?')}")

            for i, pada in enumerate(candidate["padas"], start=1):
                print(f"Pada {i}: {pada}")

            print("Reason:", candidate["validation"]["message"])
    else:
        print("No invalid candidates.")

    print("\nSUMMARY")
    print("=======")
    print("Valid:", result["valid_count"])
    print("Invalid:", result["invalid_count"])

except Exception as error:
    print("Generation failed:", error)
print("Attempts used:", result["attempts_used"])

if result["valid_count"] == 0:
    print(result["message"])