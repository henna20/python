def initials(name: str):
    names = name.split()
    initials = '.'.join(letter[0].upper() for letter in names)
    return (initials)


n = input("Enter your fullname:")
answer = initials(n)
print("The initials :", answer)
