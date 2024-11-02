def main():
    book_name = "books/frankenstein.txt"
    with open(book_name) as f:
        file_contents = f.read()

        print(f"--- Begin report of {book_name} ---")

        # Print number of words in the file
        words = file_contents.split()

        print(f"{len(words)} words found in the document \n")

        book_char_count = count_characters(file_contents)
        book_filtered_char_count = filter_dict(book_char_count)
        book_sorted_char_count = sort_dict_to_list(book_filtered_char_count)

        #print(book_sorted_char_count)
        for dict in book_sorted_char_count:
            # print(dict["char"])
            print(f"The \'{dict['char']}\' character was found {dict['num']} times")

        print("--- End report ---")



def count_characters(text):
    lowered_text = text.lower()
    result = {}

    for char in lowered_text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def filter_dict(dict):
    filtered_dict = {}
    for elem, val in dict.items():
        if elem.isalpha():
            filtered_dict[elem] = val

    return filtered_dict

def sort_on(dict):
    return dict["num"]

def sort_dict_to_list(dict):
    dict_list = []

    for elem, val in dict.items():
        dict_list.append({ "char": elem, "num": val  })
    dict_list.sort(reverse=True, key=sort_on)

    return dict_list

main()
