thedict = {
    "List1": ["Bob","Comes","After","You"],
    "List2": [100,"Hello"]
}

theList = [ "first", "second" ]

# function takes a dict, a list name and the element
def add_to_list_in_dict(thedict, listname, element):
    try:
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))
    except KeyError:
        print("The dict don't have a following key %s" % (listname))
    except:
        print("Something went wrong")

def get_from_list(theList, index):
    try:
        print(theList[index])
    except IndexError:
        print("Out of index.")
    except:
        print("Something went wrong")

def name_error():
    try:
        raise NameError
    except NameError:
        print("Name error raised")

add_to_list_in_dict(thedict, "List1", "Hellou")
add_to_list_in_dict(thedict, "Book", "Page1")


get_from_list(theList, 1)
get_from_list(theList, 2)

name_error()