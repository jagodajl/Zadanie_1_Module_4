import logging

logging.basicConfig(level=logging.INFO)


def palindrome_check(word):
    if not word.isalnum():
        logging.info("Provided input: %s contains non-alphanumeric characters. Skipping non-alphanumeric characters",
                     word)

    prepared_input = ""
    for character in range(len(word)):
        if word[character].isalnum():
            prepared_input += word[character]

    return prepared_input == prepared_input[::-1]


input = ["madam", "kobyla ma maly bok", "bugi to maly szop", "A to kawony sama da Ada? Ma synowa kota."]

for word in input:
    is_true = palindrome_check(word)
    if is_true:
        logging.info("The " + word + " is a palindrome.")
    else:
        logging.warning("Unfortunately, " + word + " is not a palindrome :(.")