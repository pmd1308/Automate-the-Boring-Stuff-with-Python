#if example
name = "Alice"
if name == "Alice":
    print("Hi Alice")
print("Done")

#if else example
pw = "Sel"
if pw == "Sel":
    print("Welcome")
else:
    print("Wrong password")
print("Done")

#if else example 2
print("Enter your name: ")
name = input()
if name != "":
    print("You have a beautiful name, "+ name)
else:
    print("I want know your name...")

#elif example
print("Enter your name")
name = input()
print("Enter your age:")
age = input()
print("Hi "+ name)
if age < 12:
    print("Are you kid?")
elif age < 20:
    print("You are adult!")
elif age > 1000:
    print("THERE CAN BE ONLY ONE!!")