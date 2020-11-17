#Author: ALJ (AMDG) 11/18/20

first_word = input(("Please type a word: "))
second_word = input(("Please type a second word: "))

a = first_word.lower()
b = second_word.lower()

word1 = list(a)
word2 = list(b)

word1.sort()
word2.sort()

if word1 == word2:
    print(first_word + ' and ' + second_word + ' are anagrams!')
else:
    print(first_word + ' and ' + second_word + ' are not anagrams!')