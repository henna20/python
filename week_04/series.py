s = input("Enter the numbers:")
numbers = list(map(int, s.split()))

positives = [i for i in numbers if i >= 0]
print("Positive numbers in the list: ", *positives)
print("Sum of positive integers: ", sum(positives))

negatives = [i for i in numbers if i < 0]
print("Negative numbers in the list: ", *negatives)
print("Sum of negative integers:", sum(negatives))


