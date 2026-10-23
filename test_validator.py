
from validator import validate_anustubh

valid_verse = """को न्वस्मिन् साम्प्रतं लोके
गुणवान् कश्च वीर्यवान्
धर्मज्ञश्च कृतज्ञश्च
सत्यवाक्यो दृढव्रतः"""

# Test 1: Valid verse
print("TEST 1: Valid verse")
print(validate_anustubh(valid_verse))
print()

# Test 2: Only three padas
print("TEST 2: Missing pada")
three_padas = """को न्वस्मिन् साम्प्रतं लोके
गुणवान् कश्च वीर्यवान्
धर्मज्ञश्च कृतज्ञश्च"""
print(validate_anustubh(three_padas))
print()

# Test 3: One pada is too short
print("TEST 3: Wrong syllable count")
wrong_count = """रामः
गुणवान् कश्च वीर्यवान्
धर्मज्ञश्च कृतज्ञश्च
सत्यवाक्यो दृढव्रतः"""
print(validate_anustubh(wrong_count))

# Test 4: Four padas with eight short-vowel syllables each
print("TEST 4: Incorrect rhythmic pattern")

wrong_pattern = """लललललललल
लललललललल
लललललललल
लललललललल"""

print(validate_anustubh(wrong_pattern))

# Test 5: Eight syllables per pada, but an unsuitable rhythm
print("TEST 5: Rhythmic pattern check")

wrong_rhythm = """रामो रामो रामो रामो
रामो रामो रामो रामो
रामो रामो रामो रामो
रामो रामो रामो रामो"""

result = validate_anustubh(wrong_rhythm)

print(result)
# Test 6: Correct syllable count, but wrong pattern at positions 5–7
print("TEST 6: Violates the pathya pattern")

wrong_pathya = """लललललललल
लललललललल
लललललललल
लललललललल"""

print(validate_anustubh(wrong_pathya))