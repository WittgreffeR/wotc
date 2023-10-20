import os

#Where the MAIN script is located (not this one)
my_location = os.path.dirname(os.path.dirname(__file__)) #1 directory above Functions (where this script is)

def read_from_file(relative_location): 
    with open(os.path.join(my_location,relative_location), "r") as read_file:
        export = read_file.read().split("\n")
    return export

def file_to_list(relative_location, dlist, start, stop):
    importlist = read_from_file(relative_location)
    for x in range (0,len(importlist)):
        join = list(importlist[x].split(","))
        for i in range (start,stop):
            join[i] = int(join[i])
        dlist.append(join)