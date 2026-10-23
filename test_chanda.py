
from chanda import analyze_text

verse = """को न्वस्मिन् साम्प्रतं लोके
गुणवान् कश्च वीर्यवान्
धर्मज्ञश्च कृतज्ञश्च
सत्यवाक्यो दृढव्रतः"""

results = analyze_text(verse, verse_mode=True, fuzzy=True)
analysis = results.result

print("Number of lines:", len(analysis.line))

for i, line_result in enumerate(analysis.line, start=1):
    result = line_result.result
    print(f"\nPada {i}: {result.line}")
    print("Syllable count:", result.length)
    print("Metre found:", result.found)
    print("Matched metres:", result.chanda)

for verse_result in analysis.verse:
    print("\nVerse metre:", verse_result.chanda)
    print("Partial:", verse_result.is_partial)
    print("Match coverage:", [
        score.match_extent for score in verse_result.scores
    ])
