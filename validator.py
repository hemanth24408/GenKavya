
from chanda import analyze_text


def validate_anustubh(verse):
    # Split the verse into four pādas (one per line)
    padas = [line.strip() for line in verse.strip().splitlines()
             if line.strip()]

    # Check that there are exactly four pādas
    if len(padas) != 4:
        return {
            "valid": False,
            "message": f"Expected 4 padas, but received {len(padas)}."
        }

    # Analyze the complete verse using chanda
    try:
        results = analyze_text(
            "\n".join(padas),
            verse_mode=True,
            fuzzy=False
        )
    except Exception as error:
        return {
            "valid": False,
            "message": f"Analysis failed: {error}"
        }

    analysis = results.result

    if len(analysis.line) != 4:
        return {
            "valid": False,
            "message": (
                f"The library analyzed {len(analysis.line)} padas; "
                "expected 4."
            )
        }
    # Check each pada's syllable count and common pathya pattern
    expected_positions = [
        ["ल", "ग", "ग"],  # Pada 1: positions 5–7
        ["ल", "ग", "ल"],  # Pada 2: positions 5–7
        ["ल", "ग", "ग"],  # Pada 3: positions 5–7
        ["ल", "ग", "ल"],  # Pada 4: positions 5–7
    ]

    for i, line_result in enumerate(analysis.line, start=1):
        result = line_result.result
        count = result.length

        if count != 8:
            return {
                "valid": False,
                "message": f"Pada {i} has {count} syllables; expected 8."
            }

        # Keep only the Laghu (ल) and Guru (ग) markers
        pattern = [mark for mark in result.lg if mark in ("ल", "ग")]

        if len(pattern) != 8:
            return {
                "valid": False,
                "message": (
                    f"Pada {i}: could not reliably determine "
                    "all 8 Laghu-Guru positions."
                )
            }

        expected = expected_positions[i - 1]

        if pattern[4:7] != expected:
            return {
                "valid": False,
                "message": (
                    f"Pada {i} fails the common pathya pattern "
                    "at positions 5–7."
                )
            }

    # Check whether a complete verse analysis was produced
    if not analysis.verse:
        return {
            "valid": False,
            "message": "The library did not identify a complete verse."
        }

    verse_result = analysis.verse[0]

    if verse_result.is_partial:
        return {
            "valid": False,
            "message": "The metre analysis is incomplete."
        }

    # Check whether Anushtubh was identified

    if not verse_result.chanda or not verse_result.chanda[0]:
        return {
            "valid": False,
            "message": "No matching metre was found."
        }

    metre_names = verse_result.chanda[0]

    if "अनुष्टुभ्" in metre_names:
        return {
            "valid": True,
            "message": (
                "Anushtubh identified; all four padas have 8 syllables "
                "and pass the checked pathya pattern."
            )
        }

    return {
        "valid": False,
        "message": "The verse was not identified as Anushtubh."
    }
