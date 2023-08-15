# Boolean Value (True/False)
print('10 > 9 --> ' + str(10 > 9))
print(10 == 9)
print(10 < 9)
print('not True = ' +str(not True))     # print(not True)
print( 2 != 3 )    # [KQ ra True, "!=": KO BẰNG]

x = "Hello"
y = 15
print('"Hello" --> ' + str(bool(x)))      # print(bool("Hello"))
print( '15 --> ' + str(bool(y)))          # print(bool(15))

True == 7
print(True)       # [KQ ra True]
# False == 5.6
# print(str(True + (False / True)))       # [dù có phần trên hay ko thì KQ đều ra 1.0]      ???

def print_and_return(x):
    print(f"I am returning {x}")
    return x
True and print_and_return(True)    
True and print_and_return(False)
# False and print_and_return(True)    # [F-T hay F-F đều ko hiển thị KQ vì là F]

lines = """
He took his vorpal sword in hand;
      Long time the manxome foe he sought—
So rested he by the Tumtum tree
      And stood awhile in thought.
"""
line_list = lines.splitlines()
print(' "the" in line_list[0] --> ' + str(bool("the" in line_list[0])))
print(' "the" in line_list[1] --> ' + str(bool("the" in line_list[1])))
print('0 + False + True = ' + str(0 + False + True))   # [Equivalent to 0 + 0 + 1]
# print(bool(["the" in line for line in line_list]))   # [Phải ra: <False, True, True, False> nma chạy chỉ ra <True>]    ???
print('False + True + True + False = ' + str(False + True + True + False))

# Binary Boolean Operators
print(('4<5 and 5<6 --> ')+ str(4<5 and 5<6))     # [True and True : True]
print(('4<5 and 6<5 --> ')+ str(4<5 and 6<5))         # True and False : F
print(('5<4 and 5<6 --> ')+ str(5<4 and 5<6))         # False and True : F
print(('5<4 and 6<5 --> ')+ str(5<4 and 6<5))         # False and False : F                 # [Not-->And-->Or]

print(('4<5 or 5<6 --> ')+ str(4<5 or 5<6))         # True or True : T
print(('4<5 or 6<5 --> ')+ str(4<5 or 6<5))         # True or False : T
print(('5<4 or 5<6 --> ')+ str(5<4 or 5<6))         # False or True : T
print(('5<4 or 6<5 --> ')+ str(5<4 or 6<5))     # [False or False : False]

not True #False
not not not not True #FTFT-->True
print(2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2)      #True [2+2=4, & KO PHAI 2+2=5, & 2*2=2+2 --> TTT--> True]


# Blocks of Code (khối mã: bắt đầu khi có khoảng trống đầu dòng)
name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print('Hello, Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')

# [KQ ra: Hello, stranger]
if name == 'Alice':
    print('Hi, Alice.')
else:
    print('Hello, stranger.')

# [KQ chỉ ra: Unlike you... thôi, vì name!=Alice + age 3000>2000]
name2 = 'Carol'
age = 3000
if name2 == 'Alice':
    print('Hi, Alice.')
elif age < 12:            
    print('You are not Alice, kiddo.')      
elif age > 2000:        # [== You are neither Alice nor a little kid.]
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
pass

# Account & Password, Tối Đa Sai 3 lần (đến L3 dừng chạy C.Trình)
name3 = input()
if name3 == 'Mary':              # Nếu acc đúng
    print('Hello, Mary')
    password = input()
    if password == 'swordfish':             # if Sai pass L1
        print('Access granted.')
    else:
        print('Wrong password.')
        password = input()
        if password == 'swordfish':         # if Sai pass L2
            print('Access granted.')
        else:
            print('Wrong password.')
            password = input()
            if password == 'swordfish':     # if Sai pass L3
                print('Access granted.')
            else:
                print('Wrong password.')      
        pass    # [dừng CT]
else:                            # Ngoài ra, nếu acc sai
    print('Wrong name.')
    name3 = input()
    if name3 == 'Mary':           # Nếu acc đúng
        print('Hello, Mary')
    else:
        print('Wrong name.')
        name3 = input()
        if name3 == 'Mary':                      # if Sai acc L1
            print('Hello, Mary')
        else:
            print('Wrong name.')
            name3 = input()
            if name3 == 'Mary':                  # if Sai acc L2
                print('Hello, Mary')
            else:
                print('Wrong name.')
        pass    # [dừng CT]

# While
name = ''
while name != 'Ngoc':                   # [CT sẽ ghi Please... mãi đến khi Đúng tên]
    print('Please type your name.')
    name = input()
print('Thank you!')

spam = 0
while spam < 5:                  # [CT sẽ chạy 5 lần, vì chạy 6 lần là: 0+1+1+1+1+1=5, ko <5 nên CT dừng vì sai]
    print('Hello, world.')
    spam = spam + 1

print('My name is')
i = 1
while i < 5:                    # [CT sẽ chạy 4 lần]
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1

# Break
while True:         # [ĐK True là luôn đúng nên đây là 1 vòng lặp vô hạn - thậm chí còn ko gán đc g.trị cho name ở đầu - LỖI]
    print('Please type "your name".')
    name = input()
    if name == 'your name':     # [Dùng Break để CT dừng khi If đúng]
        break
print('Thank you!')

# # sys.exit() Function (hàm kết thúc CT sớm)
# import sys
# while True:
#     print('Type exit to exit.')
#     response = input()
#     if response == 'exit':          # Ghi e
#         sys.exit()
#     print('You typed ' + response + '.')


# Continue
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue        # [hiện câu hỏi + KC để mình trả lời đến khi đúng cái IF mới chuyển lệnh]
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break           # [sai MK phát là quay lại từ đầu luôn]
print('Access granted.')    

# “TRUTHY” & “FALSEY”       
name = ''
while not name:         # Mặc định: {not name} == {not name != '' } == ko phải {name}
    print('Enter your name:')
    name = input()
print('How many guests will you have?')     # Ý là, gán name == rỗng (dấu cách != rỗng).
numOfGuests = int(input())                  # Nếu điền tên != rỗng thì mới dừng bước hỏi tên + chuyển bước !=
if numOfGuests:         # Mặc định:  {numOfGuests} == {numOfGuests != 0 } == {numOfGuests khác 0} <dạng int: số nguyên>
    print('Be sure to have enough room for all your guests.')
    print('Done')

# FOR loops & the RANGE() function      # Vòng lặp FOR & hàm PHẠM VI
print('My name is')
for i in range(5):      # [hiện 5 lần, i tính từ 0-4]
    print('AI (' + str(i) + ')')    # ko muốn sau AI có số thì để:  print('AI ') 

total = 0
for num in range(101):
    total = total + num     # [cộng các số từ 0-100 --> 101 số]
print(total) 

# The STARTING, STOPPING, & STEPPING arguments to range()       # Các đối số BẮT ĐẦU, DỪNG & BƯỚC cho phạm vi ()
for i in range(12, 16):
    print(i)                # Print số nguyên từ 12 đến 15
for i in range(0, 10, 2):
    print(i)                # Print các số từ 0 đến 8, KC là 2
for i in range(5, -1, -1):
    print(i)                # Print các số từ 5 đến 0, KC là -1 (đếm lùi từ 5 đến 0)


# The RANDOM module
import random
for i in range(5):          # Print ngẫu nhiên 5 số từ 1 đến 10
    print(random.randint(1, 10))

# A Short Program: GUESS THE NUMBER!
print ('This is a guess the number game.')
import random
secretNumber = random.randint(1, 20)

print('I am thinking of a number between 1 and 20.')
print ('You can guess guess 6 times.')
for guessesTaken in range(1, 7):      # đc đoán 7 - 1 = 6 lần
    print('Take a guess.')            # ghi kiểu (5, 11) tức là 11 - 5 = 6 cũng ok
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))


# A Short Program: ROCK, PAPER, SCISSORS!
import random, sys
print('ROCK, PAPER, SCISSORS!')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q.')

    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1