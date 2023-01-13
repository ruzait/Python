import random
r = (random.randint(0, 9))
secret_num = r
guess_count = 0
guess_limit = 10
while guess_count < guess_limit:
    guess = int(input("Your guess:"))
    guess_count += 1
    if guess == secret_num:
        print("You won")
        print("num is:" + str(r))
        break
else:
    print("you are out of guesses")
    print("num is:"+str(r))'''

'''import random
class Dice:
    def roll(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        return x, y
round1 = Dice()
print(round1.roll())'''

'''import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#print(len(upper))
number = "0123456789"
symbol = "$#"
all = lower + upper + number + symbol
length = 16
password = "".join(random.sample(all, length))
print(password)