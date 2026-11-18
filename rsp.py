import random
choose = ['rock', 'scissor', 'paper']
n = int(input('how many want to play? '))
def choice() :
    computer = 0
    user = 0
    for i in range(n) :
        print (f'\n___ROUND {i+1} ___')
        rand =random.choice(choose)
        print (rand)
        cin = input('Enter (rock or scissor or paper) =').lower()
        if rand == cin :
            print ('tie')
        elif (rand == 'rock' and cin == 'scissor') or (rand == 'paper' and cin == 'rock') or (rand == 'scissor' and cin == 'paper'):
            computer += 1
            print (f'you are lose : computer = {computer} | you = {user}')
        else :
            user += 1
            print (f'you are win : computer = {computer} | you = {user}')
        print ('\n___FINAL RESULT___')
    if user > computer :
        print ('\nfinally you are win!!!')
    else :
        print ('\nfinaly the computer defeated you :)')
        
choice()