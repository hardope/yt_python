def print_all(mylist):

    for i in mylist:
        print('{:d}'.format(i))

def get_index(mylist, index):

    if index < 0 or index >= len(mylist):

        return None

    return mylist[index]

def replace_index(mylist, index, value):

    if index < 0 or index >= len(mylist):

        return None
    
    mylist[index] = value

def print_reverse(mylist):

    mylist.reverse()
    for i in mylist:
        print("{:d}".format(i))

"""
new_list = [2, 9, 4, 7]

replace_index(new_list, 2, 10)
print_reverse(new_list)
"""

new_tuple = (1, 2)
print(new_tuple[0])
