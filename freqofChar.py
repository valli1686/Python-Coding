n = input("Enter a string: ")
char = input("Enter a character: ")

count = 0
for c in n:
    if c == char:
        count += 1

print("Frequency:", count)