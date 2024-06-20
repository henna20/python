def get_initials(fullname):
    xs = fullname
    name_list = xs.split()

    first = name_list[0][0]
    second = name_list[1][0]

    return first.upper() + second.upper()


n = input("Enter your fullname:")
answer = get_initials(n)
print("The initials :", answer)
