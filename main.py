def palindrome_check(word) :
    if len(word) <= 1 :
        return True
    if word[0] == word[len(word) - 1]:
        return palindrome_check(word[1:len(word) - 1])
    else:
        return False

input = ["madam", "stats", "rafal", "tacocat", "noon", "ufotofu"]

for term in input:
   ans = palindrome_check(term)
   if ans == 1:
    print( "The " + term + " is a palindrome.")
   else:
    print("Unfortunately, " + term + " is not a palindrome :(.")