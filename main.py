def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        # Print number of words in the file
        words = file_contents.split()

        print(len(words))
        count_characters(file_contents)


def count_characters(text):
    lowered_text = text.lower()
    ## print(lowered_text)

    result = {}

    for char in lowered_text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    
    print(result)

main()
