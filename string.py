# stringone= 'shehab nasser "ahned"'

# stringtwo="shehab nasser 'ahmed'"

# print(stringone)
# print(stringtwo)
# # stringthree= """ shehab 
# 'nasser' 
#  "ahmed" 
# mostafa"""

# # print(stringthree)

# -------------------------------
# Strings Indexing & Slicing
# [1] All Data in Python is Object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing ( Index Start From Zero )
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists

# indexing
eng="shehab nasser"
# print(eng[1])
# nagative
# print(eng[-1])
# slicing
print(eng[0:11])  #shehab nass

print(eng[-1::1])
# string method 
s= "        shehab nasser      "

# strip() بتشيل المسافات من البدايه والنهايه 
print(s.strip())

# rstrip()  بتشيل المسافات من النهايه 
print(s.rstrip())
#  lstrip()  بتشيل المسافات من البدايه 

print(s.lstrip())

m="#@##shehabnasser###"

print(m.strip("#"))
print(m.rstrip("#"))
print(m.lstrip("#"))

# title هيحول اي نص مكتوب الي title

d= "I LOve mohmmed Nasser 3n 4w"

print(d.title())

# capitalize اول حرف من الجمله هيكون capital 

print(d.capitalize())

# zfill  Pad a numeric string with zeros on the left, to fill a field of the given width.The string is never truncated.

z="11"  

print(z.zfill(4))

# upper بتخلي كل index on object is captal

print(d.upper())

# lower  index on object is small 

print(d.lower())





