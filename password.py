import random
import string
print("PASSWORD GENERATOR")
caps=string.ascii_lowercase
low=string.ascii_uppercase
nums=string.digits
spl_char=string.punctuation
size=int(input("Enter the length of the password:"))
print("1.STRONG")
print("2.NORMAL")
print("3.WEAK")
sensitivity=int(input("please enter the type of password / sensitivity:"))
if sensitivity==1:
    strings=caps+low+nums+spl_char
    pwd=random.sample(strings,size)
    password="".join(pwd)
    print(password)
elif sensitivity==2:
    strings=caps+low+nums
    pwd=random.sample(strings,size)
    password="".join(pwd)
    print(password)
else:
    strings=caps+low
    pwd=random.sample(strings,size)
    password="".join(pwd)
    print(password)
