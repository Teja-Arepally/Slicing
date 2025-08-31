#1.	Write a Python program to store "manoj" in one variable and "parlapalli" in another, then print them together as "manoj parlapalli".
a="Teja"
b="Arepally"
print(f'My name is {a} {b}')

#2. How would you slice characters from a string "manoj" without using loops? Give 3 different slice examples.
name="Teja Arepally"
print(name[0:2])
print(name[4:9])
print(name[0:13:2])

#3.Write a program to reverse the string "manoj".
name="Teja Arepally"
print(name[::-1])

#4.	Print the first and last character of the string "manoj". Expected output: mj.
name="Teja Arepally"
print(f"{name[0]}{name[-1]}")

#5.Print the first two and last two characters of "manoj".
name="Teja Arepally"
print(f"{name[0:2]}{name[-2:]}")

#6.	If the input is "manoj", how do you display only the first and last letter while replacing middle letters with *?
#Example: "manoj" → "m***j".
name="Arepally"
print(f"{name[0:1]}{"*"*(len(name)-2) }{name[-1:]}")

#7.	Extend the above: Show the first two and last two characters and cover the remaining characters with *.
#Example: "manoj" → "ma*oj".
name="Arepally"
print(f'{name[0:2]}{"*"*(len(name)-4)}{name[-2:]}')

#8.	Write a program to extract the first half of the string "parlapalli".
name="Arepally"
print(f'{name[0:4]}')

#9.	Write a program to extract the last half of the string "parlapalli".
name="Arepally"
print(f'{name[4:8]}')

#10.	Take two variables: one storing a name and another storing a number. Print the name repeated number times.
#Example: name = "manoj", number = 3 → Output: "manoj manoj manoj".
name="Teja"
number=3
print(" ".join([name]*number))