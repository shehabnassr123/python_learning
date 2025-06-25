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

#  split, rsplit(separator , maxsplit) بيقسم النص من اليمين واليسار علي حسب البراميتر اللي محطوط 
f = "shehab nasser ahmed"

print(f.split(" ",1))
print(f.rsplit(" "))

# center (width,fillchar )  بيوسطن النص من اليمين واليسار وبيحط من اليمين واليسار حروف او علامه انا بحددها 

j="shehab nasser"

print(j.center(12,"*"))

# count() تحسب عدد مرات ظهور جزء معيّن (حرف أو كلمة) داخل النص.



print(j.count("s",1,10))

# swapcase()  بتعكس الحروف الحرف الكبير تخليه صغير والعكس

print(j.swapcase())

# stratswith(prefix , start,end) and endswith بتخليك تتشك علي الكلامات بداية الجمله 

print(j.startswith("she",0,4))

print(j.startswith("s",0,1))

#  index (substring ,strat ,end )دا بيحددلك رقم ال index داخل string
print(j.index("s"))

#  find  (substring ,strat ,end )دا بيحددلك رقم ال index داخل string   بتدور بامان 

print(j.find("h"))

# ljust and rjust <<< center  الفرق بينهم واضح ي لفت 

k = "amany"
print(k.center(10,"#"))
print(k.ljust(10,"!"))
print(k.rjust(10,"'"))

# splitlines  بتقسم لما بتلاقي اي escape وبيطلعهم في شكل list

g= "shehab\nnasser\nahmed\thedve"

print(g.splitlines())
#  expandtabs بتخليك تحدد عدد المسافات في استرنج مستخدم \t

print(g.expandtabs(10))

one ="I Love You Mohammed 3S"

print(one.istitle())
print(one.isspace())
print(one.islower())
print(one.isupper())

two = "shehab112"

print(two.isidentifier())
print(two.isalpha())
print(two.isalnum())


sh = """ shehab \nnasser ahmed\tmostafa"""

print(sh.istitle())
print(sh.isalpha())
print(sh.isspace())
print(sh.isalnum())
print(sh.isidentifier())
print(sh.islower())
print(sh.isupper())
# =============================
sentence = "This is bad, really bad, very bad"

print(sentence.replace("bad","good",1))

# +++++++++++++++++++++++
words = ["I", "love", "Python"]
print("#".join(words))



















