# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types

mylist = [1,2,3,"shehab","eslam"]


# print(mylist[1])


#  الإضافة add 
mylist.append("ahmed")  # add items in last list

print(mylist)

mylist.insert(3,"said") # بتضيف في المكان اللي انا عايزه وبحددله كمان القيمه اللي هضيفها 
print(mylist)

#  extend () بتضيف العناصر في اخر list

mylist.extend([1,2])

print(mylist)

# الخذف 
#  بيحذف القيمه اللي بنحددهاله 

mylist.remove(1)
print(mylist)

# بيحذف اخر عنصر في الليست 

mylist.pop()
print(mylist)
# بيحذف  عنصر اللي الاندكس بتاعه كذا في الليست 

mylist.pop(0)

print(mylist)

# بيحذف الليست كلهات 
mylist.clear()
print(mylist)

mylist.append("shehab")
print(mylist)
mylist.extend([1,"nasser"])
print(mylist)
mylist.insert(0,10)
print(mylist)
mylist.remove(1)
print(mylist)
mylist.pop()
print(mylist)
mylist.pop(1)
print(mylist)
print(mylist.clear())
# 
# البحث والفحص

# my_list.index(4)          # يرجّع index لأول قيمة 4
# 4 in my_list              # هل 4 موجود؟ True or False
# my_list.count(2)          # عدد مرات تكرار الرقم 2

mylist.extend([10,"shehab","nasser"])
print(mylist.index("shehab"))

print(10 in mylist )
print(mylist.count("shehab"))

#  عكس القيمه من البدايه الي النهايه 

mylist1 = [1,2,4,5,6]
mylist1.sort(reverse=True)

print(mylist1)

mylist1.sort(reverse=False)
print(mylist1)
mylist1.reverse()
print(mylist1)

elzoz = mylist1.copy()
print(elzoz)

elzoz.append(["said",1,3])
print(elzoz)
print(elzoz[5][0])
print(elzoz[5][1])
print(elzoz[5][2])

print(elzoz)
print(mylist)
mylist.append(3)
print(mylist)
mylist.extend(["shehab",1999])
print(mylist)
mylist.insert(0,"zyead")
print(mylist)

mylist[0] = "zyead hamdy"
print(mylist)
print(mylist.index("shehab"))
w = mylist.count("shehab")
print(f"{w:.2f}")

print(len(mylist))

mylist = [1,2,3,4,5,6,7]
print(mylist)
mylist.sort(reverse=True)
print(mylist)
mylist.reverse()
print(mylist)
# remove يرب ما اكون غبي 
mylist.remove(1)
print(mylist)
mylist.pop()
print(mylist)
mylist.pop(1)
print(mylist)
mylist.pop()
print(mylist)

