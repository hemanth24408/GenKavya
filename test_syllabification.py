
import sanskrit_text as skt

words = ["रामः", "कर्म", "भक्ति", "गुरुः"]

for word in words:
    syllables = skt.get_syllables(word)

    print("Word:", word)
    print("Syllables:", syllables)
    print()
