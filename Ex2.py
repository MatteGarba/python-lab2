import sys

tasks = []

f = open(sys.argv[1], "r")
for line in f:
    tasks.append(line)
f.close()

menu="""
1. Add a task;
2. Remove a task;
3. Show all tasks sorted in alphabetic order;
4. Close the program;
"""

print("Insert a number corresponding to an action of the menu: ")
print(menu)

i = input()

while int(i)!= 4 :

    if int(i) == 1 :
        print("Insert task to add:")
        new = input()
        tasks.append(new + "\n")

    if int(i) == 2 :
        print("Insert task to delete:")
        rem = input()
        if tasks.__contains__(rem + "\n") :
            tasks.remove(rem + "\n")
        else :
            print("Element was not present")

    if int(i) == 3 :
        print(end="\n")
        for x in sorted(tasks):
            print(x,end='')
        print(end="\n")

    print("Insert a new command:")
    i = input()

f = open(sys.argv[1], "w")
for line in tasks:
    f.write(line)
f.close()