paragraph = input("Enter a paragraph: ")

def clean_text(text):

    text = text.lower()
    punctuation = ".,!?;:'\"()[]{}-_/\\@#$%^&*+=<>`~"

    cleaned = ""

    for ch in text:
        if ch not in punctuation:
            cleaned += ch

    return cleaned

if not paragraph.strip():

    print("Please enter a non-empty paragraph!")
else:

    cleaned_text = clean_text(paragraph)
    words = cleaned_text.split()

    if not words:
        print("No valid words found!")

    else:
        frequency = {}

        for word in words:
            frequency[word] = frequency.get(word, 0) + 1

        print("\n1. Word Frequencies:")
        print(frequency)

        n = int(input("\nEnter N for top words: "))
        if n < 0:
            print("N cannot be negative!")

        else:
            sorted_words = sorted(
                frequency.items(),
                key=lambda item: (-item[1], item[0])
            )

            print("\n2. Top", n, "Words:")

            for word, count in sorted_words[:n]:
                print(word, "->", count)


        single_words = [
            word
            for word, count in frequency.items()
            if count == 1
        ]

        print("\n3. Words Appearing Exactly Once:")
        print(sorted(single_words))

        inverted = {}

        for word, count in frequency.items():
            inverted.setdefault(count, []).append(word)

        for count in inverted:
            inverted[count].sort()

        print("\n4. Inverted Dictionary:")
        print(inverted)

        length_groups = {}

        for word in frequency:

            length = len(word)

            length_groups.setdefault(length, []).append(word)

        for length in length_groups:
            length_groups[length].sort()

        print("\n5. Words Grouped by Length:")
        print(length_groups)

        search_word = input("\nEnter a word to search: ")

        search_word = clean_text(search_word).strip()

        if search_word in frequency:
            print(
                search_word,
                "appears",
                frequency[search_word],
                "time(s)."
            )
        else:
            print("Word not found!")
