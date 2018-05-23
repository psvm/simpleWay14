#Find the set of English characters into the text
def find_english_characters(text):
    english_characters = set()
    for i in text:
        if (65 <= ord(i) and ord(i) <= 90) or (97 <= ord(i) and ord(i) <= 122):
            english_characters.add(i)

    return english_characters
print(find_english_characters("AAAAAAAAAAAAAAAAAAAAAddsefwerhgykjuk"))