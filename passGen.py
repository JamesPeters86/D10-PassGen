#!/usr/bin/python3

with open("tokenList") as fptr:
    lines = fptr.readlines()

# We want an even probablity distribution. 
# Rolling the dice 4 times will give 3 numbers that can select each token.
# For example, the vales: 0, count, and 2 * count will select the first token in the file.
# The vales: 1, count + 1, and 2 * count + 1  will select the second token in the file.
# If we don't throw out rolls that are higher than 3 * count, the first several tokens will
# have 4 numbers that select them. Thus they will have a 33% higher probablity of being picked. 
cnt = len(lines)
maxRoll = cnt * 3 - 1

print("There are " + str(cnt) + " different tokens")
if cnt > 3333:
    print("Only the first 3333 tokens will be used.")
    cnt = 3333
print("For each token, roll a d10 4 times. For 10 enter 0.")
print("If your number is greater than", maxRoll, "start over from the first roll")
print("Enter q when done");
print("Total Digits\t", "Token")

# print the tokens along with a running count of the digits
digitCount = 0
while True:
    line = input("Number: ").strip()
    if "q" == line:
        break

    number = int(line);
    if number > maxRoll:
        print("Too big, retry!")
        continue

    # use modulo to wrap back around the list
    number = (number % cnt)
    token = lines[number].strip()
    digitCount += len(token)
    print(digitCount, "\t\t", token)
