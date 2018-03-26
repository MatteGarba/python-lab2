tasks = []
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
        tasks.append(new)
    if int(i) == 2 :
        print("Insert task to delete:")
        rem = input()
        if tasks.__contains__(rem) :
            tasks.remove(rem)
        else :
            print("Element was not present")


    if int(i) == 3 :
        for x in sorted(tasks):
            print(x)


    print("Insert a new command:")
    i = input()
