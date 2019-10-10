import random
target = random.randint(0, 100)
min = 0
max = 99
print("Guess a number", min, "-", max, ": ", end="")
guess = int(input())
count = 1
while guess != target:
    if not (guess<=max and guess>=min):
        print('Not in the range!')
        print("Guess a number", min, "-", max, ": ", end="")
        guess = int(input())
        count+=1
        continue
    if target<guess:
        max=guess
    else:
        min=guess
    print("Guess a number", min, "-", max, ": ", end="")
    guess = int(input())
    count+=1
print('Correct after',count,'trial!')
