################ex1################
def Fibbo(number):
    list = []
    if number == 1:
        return [0]  
    elif number == 2:
        return [0,1]
    list = [0,1]
    for index in range(2,number):
        list.append(list[index-1] + list[index-2])
    return list
  
# print(Fibbo(5))


################ex2################
def is_prime(number):
    if number == 1:
        return False
    for index in range(2,number):
        if number % index == 0:
            return False
    return True

def filter_prime(list):
    return [number for number in list if is_prime(number)]

# print(filter_prime([1,2,3,4,5,6,7,8,9,10]))


################ex3################
def calculate(list1, list2):
    intersection = [number for number in list1 if number in list2]        
    reunion = []
    reunion = list1 + list2
    for i in intersection:
        reunion.remove(i)
    minusB = [number for number in list1 if number not in list2]
    minusA = [number for number in list2 if number not in list1]

    print("The intersection between list1 and list2 is: ", intersection)
    print("The reunion: ", reunion)
    print("List1 - list2 = ", minusB)
    print("List2 - list1 = ", minusA)
    
# calculate([1,3,4],[2,3,5])


##############ex4##############
def composeSong(musicalNotes, moves, startPosition):
    composedSong = []
    currentPosition = startPosition
    composedSong.append(musicalNotes[currentPosition])
    
    for move in moves:
        currentPosition = (currentPosition + move) % len(musicalNotes)
        composedSong.append(musicalNotes[currentPosition])
    
    return composedSong
    
# composeSong(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) 


##############ex5##############
def replaceWithZero(matrix):
    return [ [0 if x > y else matrix[x][y] for y in range(len(matrix[0]))] for x in range(len(matrix))]

# print(replaceWithZero([[1,2,3],[4,5,6],[7,8,9]]))
# print(replaceWithZero([(1,2,3),(4,5,6),(7,8,9)]))

##############ex6##############
def listOfExaclyXAparitions(*multipleLists, x ):
    element_count = {}
    
    for lst in multipleLists:
        for element in lst:
            if element in element_count:
                element_count[element] += 1
            else:
                element_count[element] = 1
    
    result = [element for element, count in element_count.items() if count == x]
    
    return result

# print(listOfExaclyXAparitions([1,2,3], [2,3,4],[4,5,6], [4,1,"test"], x = 2))


##############ex7##############
def is_palindrome(number):
    return str(number) == str(number)[::-1] 

def filter_palindromes(list):
    maxPalindrome = 0
    counterPalindrome = 0
    for number in list:   
        if is_palindrome(number):
            if number > maxPalindrome:
                maxPalindrome = number
            counterPalindrome +=1
    return (counterPalindrome, maxPalindrome)

#print(filter_palindromes([121, 123, 1221, 12321, 12345, 123321]))
 


##############ex8##############
def filterAsciiDivisibility(x=1, strings=[], flag=True):
    result = []
    for string in strings:
        filtered_chars = []
        for char in string:
            if flag:
                if ord(char) % x == 0:
                    filtered_chars.append(char)
            else:
                if ord(char) % x != 0:
                    filtered_chars.append(char)
        result.append(filtered_chars)
    return result

#print(filterAsciiDivisibility(2, ["test", "hello", "lab002"], False))         




##############ex9##############
def findBlockedSeats(matrix):
    blockedSeats = []
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            for row_ in range(0, row):
                if matrix[row][col] <= matrix[row_][col]:
                    blockedSeats.append((row, col))
                    break
    return blockedSeats


matrix = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]
#print(findBlockedSeats(matrix))



##############ex10##############
def combineLists(*lists):
    max_length = max(len(lst) for lst in lists)
    result = []
    
    for i in range(max_length):
        tuple_element = tuple(lst[i] if i < len(lst) else None for lst in lists)
        result.append(tuple_element)
    
    return result

#print(combineLists([1, 2, 3, 4], [5, 6, 7], ["a", "b", "c"]))



##############ex11##############
def sortByThirdChar(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1][2]) #2nd element & 3rd character

sorted_list = sortByThirdChar([('abc', 'bcd'), ('abc', 'zza')])
#print(sorted_list)


##############ex12##############
def groupByRhyme(words):
    rhyme_dict = {}
    
    for word in words:
        if len(word) < 2:
            rhyme = word
        else:
            rhyme = word[-2:]
        
        if rhyme in rhyme_dict:
            rhyme_dict[rhyme].append(word)
        else:
            rhyme_dict[rhyme] = [word]
    
    return list(rhyme_dict.values())

#print(groupByRhyme(['ana', 'banana', 'carte', 'arme', 'parte']))