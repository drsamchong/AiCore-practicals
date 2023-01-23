# %%

items = ["tomato", "sugar", "sponges", "juice", "foil"]
prices = [0.87, 1.09, 0.29, 1.89, 1.29]

items_and_prices = zip(items, prices)

#print(list(items_and_prices)) 
#  weird, having this here means list_i_p ends up as an empty list
# apparently using list() on the zip function changes it somehow (see the loops notebook)
# Answer: zip returns a iterator or something similar which once iterated through is consumed
# Remember there was something about this in DataCamp Python Data Science Toolbox pt 2


print(list(zip(items, prices)))

#print(list(items_and_prices))

list_i_p = list(items_and_prices)
print(*list_i_p)


# %%

# %%
x = 0
while x < 50:
    print(x+1)
    x += 1
# %%
for x in range(1, 51):
    print(x)
# %%
x = 1
while x <= 50:
    if x%2 == 0:
        print(x)
    x += 1
# %%
for x in range(1, 51, 2):
    print(x+1)
# %%
total = 0
for x in range(0, 101, 2):
    print(x)
    total += x
print(total)

# %%
odd_total = 0
for x in range(1, 101, 2):
    print(x)
    odd_total += x
print(odd_total)

# %%
for x in range(1, 101):
    if (x % 3 == 0):  
        if (x % 5 == 0):
            print("FizzBuzz")
        else:
            print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)



# %%
num_player_one_wins = 0
num_player_two_wins = 0

def ask_for_input():
    move = (input("Choose rock, paper or scissors").lower())
    if move in ["rock", "paper", "scissors"]:
        return move
    else:
        print("Invalid input")
        ask_for_input()


while (num_player_one_wins) < 3 and (num_player_two_wins < 3):
    player_one_move = ask_for_input()
    player_two_move = ask_for_input()

    if player_one_move == "rock":
        if player_two_move == "paper":
            print("Player 2 wins")
            num_player_two_wins += 1
        elif player_two_move == "scissors":
            print("Player 1 wins")
            num_player_one_wins += 1
        else:
            print("It's a tie")

# %%
my_list = [1, 5, 8, 6, 21]

lc = [x**2 if x%2 == 0 else (x+1)**2 for x in my_list]
print(lc)
# %%
dict_1 = {"name": "sam", "skills": ["sleeping", "eating"]}
dict_2 = {"name": "darryl", "skills": ["cycle", "swim"]}

my_list = [dict_1, dict_2]
letter = my_list[1]["skills"][0][-1]
print(letter)

list_2 = [len(thing["name"]) for thing in my_list]
print(sum(list_2))


# %%
shop_dict = {"tom": 0.87, "sug": 1.09, "ws": 0.29, "cc": 1.89, "ccz": 1.29}

names_dict = {"tom": "Tomatoes", "sug": "Sugar", "ws": "Washing Sponges", "cc": "Coca-Cola", "ccz": "Coca-Cola Zero"}

expensive_items = [names_dict[name] for name, price in shop_dict.items() if price > 1.00]

expensive_items
# %%
n = 5

for i in range(1, n+1):
    for j in range(i):
        print('?', end=" ")
    print()
for i in range(n-1, 0, -1):
    for j in range(i):
        print('?', end=" ")
    print()


# %%
for num in range(10, 51):
    for n in range(2,num):
        if num % n == 0:
            print(f"{num} is not a prime. It has a factor of {n}")
            break
    else:
       print(f"{num} is a prime number")

# %%
num = 0
while num < 51:
    for n in range(2, num):
        if num % n == 0:
            print(f"{num} is not a prime. It has a factor of {n}")
            break
    else:
        print(f"{num} is a prime number")
    num += 1

# %%
