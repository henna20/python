def print_int_list():
    n = []
    global a, b
    n = input("Enter two numbers: ")
    a, b = n.split()
    print("You Entered:", a, b)
def swap(a, b):
    temp = a
    a = b
    b = temp
    print("Your entries swapped:", a, b)

print_int_list()
swap(a, b)
