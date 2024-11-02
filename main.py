def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        # Print number of words in the file
        words = file_contents.split()

        print(len(words))

main()
