# write your code here
import random

print("Enter the number of friends joining (including you):")
count = int(input())

if count < 1:
    print("No one is joining for the party")
    exit()

print("Enter the name of every friend (including you), each on a new line:")

friends = {}
for _ in range(count):
    friends.update({input(): 0})

print("Enter the total bill value:")
bill = int(input())
split = round(bill / count, 2)

print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
if input() == "Yes":
    lucky = random.choice(list(friends.keys()))
    print(lucky, "is the lucky one!")
    split = round(bill / (count - 1), 2)
else:
    lucky = None
    print("No one is going to be lucky")

for friend in friends:
    if lucky != friend:
        friends[friend] = split

print(friends)
