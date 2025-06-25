#   traing 
#  1. Print your full name in a decorative box using * and \n.
print("******************\n*shehab nasser*\n******************")

#  2. Print this shape using one print and escape characters:
#    *
#   ***
#  *****
# *******

print("   *\n  ***\n *****\n*******")

# 3. Print your name with a tab space between each character.
s="s\th\te\th\ta\tb\t"
print("s\th\te\th\ta\tb\t")

print(s.replace("\t",""))

# 4. Print three sentences on three lines using one print function.

print("shehab\nnasser\nahmed")

# 5. Print a menu of 3 items using tabs and newlines.

print("tea\t20p\ncoffe\t30\nmango\t50")

# 6. Store your name, age, and country in variables, then print them.

name = "shehab"
age = 20
country = "cairo"
money = 1690750
print("my name is %s and my age is %d and my country is %s"%(name,age,country))
print("my name is %s and my age is %.2f and my country is %s"%(name,age,country))

print("my name is {0:.2s} and my age is {1:d} and my country is {2:s} and money is {3:,d}".format(name,age,country,money))
print(f"my name is {name:.4s} and my age is {age:d} and my country is{country:s} and my money is {money:,d}")

# 7. Use type() to print the data type of 4 variables.

list = [1,3,4,5]
tuple= (1,3,"asdvh")
string = "shehab"
interger= 22

print(type(list))
print(type(tuple))
print(type(string))
print(type(interger))

# 9. Convert an integer to string and print its length.

interger="21321321"
print(str(interger))
print(len(str(interger)))

# 11. Concatenate your first and last name into one variable.
firstname ="shehab"
lastname="nasser"

fullname = firstname +" "+lastname

print(fullname)

print(f"{firstname} {lastname}")

# 12. Count how many characters your name has using len().

print(len(fullname))

# 13. Join 3 words with "-" between them and print the result.

s= "I love python"

print(s.rsplit(" ",1))

print("-".join(s.split()))

# 15. Get user's input for hobby and print a sentence with it.

# hoppy =input(" enter your hoppies please")

# print(f"my hoopy is {hoppy}")

# 16. Store a sentence and replace one word with another.

s = "shehab nasser"
x= s.split()
print(x)
v = x[-1:-3:-1]
print(v)

print(" ".join(v))

# 17. Print the first and last character of your name.
name ="shehab"
last = "nasser"

print(name[1])
print(last[1])
# 19. Reverse a string using slicing.

print(name[-1::-1])
# 20. Extract and print a substring from character 2 to 5.
print(name[2:5])
# 21. Given a word, print the middle character.

test = "conactenaction"
lenght =len(test)
print(lenght)
middle = lenght //2 
print(middle)
if lenght % 2 == 0:
    print(test[middle-1])
    print(test[middle])

# 22. Make a string uppercase and lowercase.
word = "     shehab nasser ahmed   "
print(word.upper())
print(word.lower())
# 23. Strip spaces from start and end of a string.


print(word.strip(" "))
print(word.lstrip(" "))
print(word.rstrip(" "))
# 24. Count how many times "a" appears in a sentence.
print(word.count("a"))

# 25. Check if a string starts with "Hello".
print(word.startswith("hello"))
print(word.startswith("sh",5,7))
print(word.endswith("sh",5,10))

# 26. Replace "ahmed" with "mostafa" in a sentence.

print(word.replace("ahmed","mostafa"))

# 27. Find the index of "e" in a word.
print(word.index("a"))
print(word.find("a"))
# 28. Split a sentence into words and print the list.
words = word.strip(" ")
print(words.split(" "))
print("@".join(words.split(" ")))

# 30. Print: Hello Ali, your score is 98.5% using:
#    - % formatting
#    - .format()
#    - f-string
name = "ali"
score = 98.5

print("hello %s your score is %f " %(name,score))
print("hello {:s} your score is {:.4f} %".format(name,score))

print(f"hello {name:s} your score is {score: .3f} %")

# 
# 33. Use f-string to align text in a table style.

print(f" {'name':<10} | {'age':<3} | {'country':<10}")

print(f" {'shehab':<10} | {'26':<3} | {'beni_suef':<10}")

# 41. Build a receipt that shows 3 items, prices, and total.

banna = 20 
tea = 5
cola =15 
total = cola + tea + banna

print(f"tea is price {tea}\nbanna is price {banna}\ncola is price {cola}\ntotal is {total} ")













