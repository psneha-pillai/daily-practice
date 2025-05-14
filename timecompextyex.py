#def get_first_element(lst):
#return lst[0]  # Always takes the same time
'''def print_elements(lst):
    for item in lst:
        print(item)
lst=list(map(int,input("enter").split()))
print_elements(lst)
print(print_elements)'''

def print_pairs(lst):
    for i in lst:
        for j in lst:
            print(i, j)
lst=list(map(int,input("enter").split()))
print_pairs(lst)
print(print_pairs)