#shal we go through the lenght function

name="prajwal c"
print(len(name))                 #finding the lenght of a string 
print(name.endswith("jwal c"))
print(name.startswith("praj")) #it was an case sensitive both ends and starts function in python 
print(name.capitalize()) #capitalize means capital the first letter of name as it has
print(name.lower())
print(name.upper())
#its an overview string function and so many methods 

'''
1. len()

👉 Finds length of the string

s = "Python"
print(len(s))   # 6

2. lower()

👉 Converts string to lowercase

s = "HELLO"
print(s.lower())   # hello

3. upper()

👉 Converts string to uppercase

s = "hello"
print(s.upper())   # HELLO

4. capitalize()

👉 First letter capital

s = "python"
print(s.capitalize())   # Python

5. title()

👉 Capitalizes first letter of each word

s = "python programming"
print(s.title())   # Python Programming

6. strip()

👉 Removes spaces from start & end

s = "  hello  "
print(s.strip())   # hello

7. replace()

👉 Replaces one word/letter with another

s = "I like Java"
print(s.replace("Java", "Python"))
# I like Python

8. split()

👉 Splits string into list

s = "apple banana mango"
print(s.split())
# ['apple', 'banana', 'mango']

9. join()

👉 Joins list into string

words = ["Python", "is", "easy"]
print(" ".join(words))
# Python is easy

10. find()

👉 Finds position of character/word
(Returns -1 if not found)

s = "Python"
print(s.find("t"))   # 2

11. startswith()

👉 Checks starting word

s = "Python"
print(s.startswith("Py"))  # True

12. endswith()

👉 Checks ending word

print(s.endswith("on"))  # True

13. isdigit()

👉 Checks only digits or not

s = "123"
print(s.isdigit())  # True

14. isalpha()

👉 Checks only alphabets

s = "Hello"
print(s.isalpha())  # True

15. isalnum()

👉 Alphabets + Numbers

s = "Hello123"
print(s.isalnum())  # True

'''