import string

text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world. Many tourists
visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""

def word_frequency(text):
    text = text.lower()

    for mark in string.punctuation:
        text = text.replace(mark, "")

    words = text.split()

    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    top_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:3]

    return top_words

result = word_frequency(text)

print("Top 3 words:")
for word, count in result:
    print(f"{word} — {count} times")