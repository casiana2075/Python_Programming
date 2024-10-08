#ex1
#
# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)
#
# n = int(input("Enter the desired number of elements to do gcd with them: "))
#
# num1 = int(input("Enter number: "))
# n = n - 1
# while n != 0:
#     num2 = int(input("Enter number: "))
#     gcrCommDiv = gcd(num1, num2)
#     num1 = gcrCommDiv
#     n = n - 1 
# print(f"The greatest common divisor is : {gcrCommDiv}")


#ex2
#
# phrase = input("Enter a string: ")
# numberOfVowels = (phrase.count('a') + phrase.count('e') + phrase.count('i') + 
#                   phrase.count('o') + phrase.count('u') + phrase.count('A') + 
#                   phrase.count('E') + phrase.count('I') + phrase.count('O') + 
#                   phrase.count('U'))
# print(f"The number of vowels in the string is: {numberOfVowels}")


#ex3
#
# stringToBeSearched = input("Enter a string to be searched: ")
# stringToSearchIn = input("Enter a string to search in: ")
#
# if stringToSearchIn.find(stringToBeSearched) == -1:
#     print("The string was not found")
# else:
#     numberOfOccurences = stringToSearchIn.count(stringToBeSearched)
#     print(f"The string was found {numberOfOccurences} times")


#ex4
#
# upperCamelCaseString = input("Enter an upperCamelCase string: ")
# lowerSnakeCase = ""
#
# if upperCamelCaseString[0].isupper():
#     lowerSnakeCase += upperCamelCaseString[0].lower()
#
# for character in upperCamelCaseString[1:]:
#     if character.isupper():
#         lowerSnakeCase += f"_{character.lower()}"
#     else:
#         lowerSnakeCase += character
#
# print(f"The new string is: {lowerSnakeCase}")


#ex5
#
# def isPalindrome(number):
#     originalNum = number
#     reversedNum = 0
#     while number > 0:
#         digit = number % 10
#         reversedNum = reversedNum * 10 + digit
#         number = number // 10 
#     if reversedNum == originalNum:
#         return True
#     else: 
#         return False
#   
# value = 12021
# print(isPalindrome(value))



#ex6 - extract a number from a string function
#
# def extractNumbersFromString(inputString):
#     found = False
#     extractedNum = ""
#     for character in inputString:
#         if character.isdigit():
#             extractedNum += character
#             found = True
#         elif character.isdigit() == False and found == True:
#             break
#     print(f"Extracted numbers are: {extractedNum}")
#
# inputString = "Casiana are 120 lei si Ana are 110$"
# extractNumbersFromString(inputString)


#ex7
#
# def numberOfOneBits(number):
#     counter = 0
#     for character in bin(number):
#         if character == "1":
#             counter += 1
#     print(f"Number of bits with value 1: {counter}")
#
# numberOfOneBits(2472)

#ex8
#
# def countNumOfWords(text):
#     words = text.split(" ")
#     return len(words)
#
# text = "I have Python exam"
# print(f"The text \"{text}\" has {countNumOfWords(text)} words.")
