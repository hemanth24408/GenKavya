
from chanda import analyze_text

verse = """को न्वस्मिन् साम्प्रतं लोके
गुणवान् कश्च वीर्यवान्
धर्मज्ञश्च कृतज्ञश्च
सत्यवाक्यो दृढव्रतः"""

results = analyze_text(verse, verse_mode=True, fuzzy=False)

for i, line_result in enumerate(results.result.line, start=1):
    result = line_result.result

    # Remove empty markers returned by the library
    pattern = [mark for mark in result.lg if mark in ("ल", "ग")]

    print(f"\nPada {i}: {result.line}")
    print("Reported syllable count:", result.length)
    print("Usable Laghu-Guru markers:", pattern)
    print("Number of markers:", len(pattern))

    if len(pattern) == 8:
        print("Positions 5–7:", pattern[4:7])
    else:
        print("Cannot safely check positions 5–7.")
