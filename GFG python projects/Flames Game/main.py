print("Welcome to FLAMES...")

name1  = input("Enter your first name: ").lower()
name2 = input("Enter your second name: ").lower()

def common_characters_removal(name1, name2):
    for i in name1:
        if i in name2:
            name1 = name1.replace(i, "", 1) #it will just replace the first instance of the string 
            name2 = name2.replace(i, "", 1)
        
    return (name1, name2)

flames = ["F", "L", "A", "M", "E", "S"]

# load the removed characters
a, b = common_characters_removal(name1, name2)
# lenght of the remaining string combined
length = len(a) + len(b)

# F L A M E S
# 0 1 2 3 4 5
n = len(flames)
start = 0

while n != 1:
    i = (start + length-1) % n
    del flames[i]
    n -= 1

    if n > 0:
        start = i % n
    else:
        start = 0

i = flames.pop(0)

match i:

    case "F":
        print("They are Friends")
    case "L":
        print("They are in Loooove")
    case "A":
        print("They have Affection for each other")
    case "M":
        print("They will Marry someday")
    case "E":
        print("They become archenemies")
    case "S":
        print("They are brother/sister from another mother")

    case _:
        print("Invalid Input!!, Please try again")



