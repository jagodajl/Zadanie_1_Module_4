import logging

logging.basicConfig(level=logging.INFO)


def palindrome_check(word):
    input_adjusted = word.lower().replace(" ", "")
    return input_adjusted[::1] == input_adjusted[::-1]

input = ["madam", "kobyla ma maly bok", "bugi to maly szop"]

for word in input:
    is_true = palindrome_check(word)
    if is_true:
        logging.info("The " + word + " is a palindrome.")
    else:
        logging.warning("Unfortunately, " + word + " is not a palindrome :(.")
