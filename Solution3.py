#1.Write a function that receives as parameters two lists a and b and 
#returns a list of sets containing: (a intersected with b, a reunited
#with b, a - b, b - a)
def calculate(list1, list2):
    intersection = [number for number in list1 if number in list2]        
    reunion = []
    reunion = list1 + list2
    for i in intersection:
        reunion.remove(i)
    minusB = [number for number in list1 if number not in list2]
    minusA = [number for number in list2 if number not in list1]

    mySet = { intersection, reunion, minusB, minusA }
    print("The set is: ", mySet)
    
#calculate([1,3,4],[2,3,5])

#2.Write a function that receives a string as a parameter and returns a 
#dictionary in which the keys are the characters in the character string
#and the values are the number of occurrences of that character in the given text.
def dictionary(text):
    dict = {}
    for i in text:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

#print (dictionary("Hello World"))

#3.Compare two dictionaries without using the operator "==" returning True or
#False. (Attention, dictionaries must be recursively covered because they can
#contain other containers, such as dictionaries, lists, sets, etc.) 
def compareDictionaries(dic1, dic2):
    if dic1.keys() != dic2.keys(): #not the same keys
        return False
    for key in dic1: #parse keys from dic1
        if isinstance(dic1[key], dict) and isinstance(dic2[key], dict):
            if not compareDictionaries(dic1[key], dic2[key]): #recursive call 
                return False
        elif isinstance(dic1[key], list) and isinstance(dic2[key], list):
            if len(dic1[key]) != len(dic2[key]):
                return False
            for item1, item2 in zip(dic1[key], dic2[key]):
                if isinstance(item1, dict) and isinstance(item2, dict):
                    if not compareDictionaries(item1, item2):
                        return False
                elif item1 != item2:
                    return False
        elif isinstance(dic1[key], set) and isinstance(dic2[key], set):
            if dic1[key] != dic2[key]:
                return False
        else:
            if dic1[key] != dic2[key]:
                return False
    return True

dict1 = {
    "A": 1,
    "fistic": {"Cocos": 2, "D": [1, 1, 2]},
    "Casiana": {1, 6, "max"}
}
dict2 = {
    "A": 1,
    "fistic": {"Cocos": 2, "D": [1, 1, 2]},
    "Casiana": {1, 6, "mix"}
}
#print(compareDictionaries(dict1, dict2))


#4.The build_xml_element function receives the following parameters: tag, 
#content, and key-value elements given as name-parameters. Build and return a
#string that represents the corresponding XML element.
#Example: build_xml_element ("a", "Hello there", href =" http://python.org "
#_class =" my-link ", id= " someid ") returns the string = 
#"<a href="http://python.org "_class = " my-link " id = " someid "> Hello there </a>"
def build_xml_element(tag, content, **key_value):
    xml = "<" + tag
    for key, value in key_value.items():
        xml += " " + key + "=\"" + value + "\""
    xml += ">" + content + "</" + tag + ">"    
    return xml

#print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))


#5.The validate_dict function that receives as a parameter a set of tuples ( that 
#represents validation rules for a dictionary that has strings as keys and
#values) and a dictionary. A rule is defined as follows: (key, "prefix",
#"middle", "suffix"). A value is considered valid if it starts with "prefix",
#"middle" is inside the value (not at the beginning or end) and ends with "suffix".
#The function will return True if the given dictionary matches all the rules, False
#otherwise. Example: the rules s={("key1", "", "inside", ""), ("key2",
#"start", "middle", "winter")} and d= {"key1": "come inside, it's too cold
#out", "key3": "this is not valid"} => False because although the rules are 
#respected for "key1" and "key2" "key3" that does not appear in the rules.

def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key not in dictionary:
            return False
        if not dictionary[key].startswith(prefix) or not dictionary[key].endswith(suffix):
            return False
        if middle not in dictionary[key]:
            return False
    return True

rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
dictionary = {"key1": "come inside, it's too cold out",
              "key2": "start this middle winter"}
#print(validate_dict(rules, dictionary))


#6.Write a function that receives as a parameter a list and returns a tuple 
#(a, b), a representing the number of unique elements in the list, and b 
#representing the number of duplicate elements in the list (use sets to achieve this objective).
def count_elements(lst):
    uniqueCnt = len(set(lst))
    duplicateCnt = len(lst) - uniqueCnt
    return (uniqueCnt, duplicateCnt)

#print(count_elements(list("Hello World")))


#7.Write a function that receives a variable number of sets and returns a
#dictionary with the following operations from all sets two by two: reunion,
#intersection, a-b, b-a. The key will have the following form: "a op b",
#where a and b are two sets, and op is the applied operator: |, &, -.
def operations(*sets):
    result = {}
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            result[str(sets[i]) + " | " + str(sets[j])] = sets[i] | sets[j]
            result[str(sets[i]) + " & " + str(sets[j])] = sets[i] & sets[j]
            result[str(sets[i]) + " - " + str(sets[j])] = sets[i] - sets[j]
            result[str(sets[j]) + " - " + str(sets[i])] = sets[j] - sets[i]
    return result

#print(operations({1,2},{2,3}))

#8.Write a function that receives a single dict parameter named mapping.
#This dictionary always contains a string key "start". Starting with the 
#value of this key you must obtain a list of objects by iterating over mapping
#in the following way: the value of the current key is the key for the next 
#value, until you find a loop (a key that was visited before). The function 
#must return the list of objects obtained as previously described.
def loop(mapping):
    result = []
    key = "start"
    value = mapping[key]
    while key != value:
        result.append(value)
        key = value
        value = mapping[key]
    return result

#print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))


#9.Write a function that receives a variable number of positional arguments 
#and a variable number of keyword arguments and will return the number of 
#positional arguments whose values can be found among keyword arguments values. 
def my_function(*posArgs, **kwArgs):
    return len([posArgs for posArgs in posArgs if posArgs in kwArgs.values()])

#print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))