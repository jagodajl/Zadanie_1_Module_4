import logging

logging.basicConfig(level=logging.INFO)


def palindrome_check(word):
    input_without_spaces = word.lower().replace(" ", "")
    if not input_without_spaces.isalnum():
        logging.info("Provided input: %s contains non-alphanumeric characters. Skipping non-alphanumeric characters",
                     word)

    prepared_input = ""
    for character in range(len(input_without_spaces)):
        if input_without_spaces[character].isalnum():
            prepared_input += input_without_spaces[character]

    return prepared_input == prepared_input[::-1]


input = ["madam", "kobyla ma maly bok", "bugi to maly szop", "A to kawony sama da Ada? Ma synowa kota."]

for word in input:
    is_true = palindrome_check(word)
    if is_true:
        logging.info("The " + word + " is a palindrome.")
    else:
        logging.warning("Unfortunately, " + word + " is not a palindrome :(.")