"""
条件控制语句：
1、每个条件后面使用冒号(:),表示接下来是满足条件后要执行的语句块
2、使用所进来划分语句块，相同缩进数的语句在一起组成一个语句块
3、在Python中没有switch -case语句
"""

age = int(input("Age of th dog:"))
print()
if age < 0:
    print("This can hardly be true")
elif age == 1:
    print("about 14 human years")
elif age == 2:
    print("about 22 human years")
elif age > 2:
    human = 22 + (age-2)*5
    print("human years:",human)


number = 7
guess = -1
print("Guess the number")
while guess != number:
    guess = int(input("Is it ...."))
    if guess == number:
        print("Hooray,you guessed it right")
    elif guess < number:
        print("It's bigger...")
    elif guess > number:
        print("It's not so big")


