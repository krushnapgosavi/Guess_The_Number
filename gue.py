import random
print("This is a game .GUESS THE NUMBER.")
ch = 1
choice = 1
def game():
    print('Easy : 1\nNormal : 2\nMedium : 3\nDifficult : 4')
    diff = int(input('Choose Difficulty : '))
    lst = []
    che = []
    li = []
    
    if diff == 1:
        ra = random.randrange(100,999)
        diff_num = 3
        dif_name = 'Easy'
    elif diff == 2:
        ra = random.randrange(1000,9999)
        diff_num = 4
        dif_name = 'Normal'
    elif diff == 3:
        ra = random.randrange(10000,99999)
        diff_num = 5
        dif_name = 'Medium'
    elif diff == 4:
        ra = random.randrange(100000,999999)
        diff_num = 6
        dif_name = 'Difficult'
    else:
        print('Please Enter the Valid Difficulty level !!')
        
    ra = str(ra)
    cou = 0
    c = 0
    print('\nDifficulty : %s'%(dif_name))
    print('\nGuess the %s digit Number\n'%(diff_num)) 
    while cou < diff_num:
        c = c+1
        lst = []
        che = []
        cor = []
        for i in range(0,diff_num):
            li.append(ra[i])
        choice = (input("GUESS the Number : "))
        for j in range(0,len(choice)):
            lst.append(choice[j])
        try:
            for k in range(0,diff_num):
                if lst[k] == li[k]:
                    che.append("Correct")
                else:
                    che.append("Wrong")
        except IndexError:
            print("Please enter the %s digit numbers"%(diff_num))
        cou = che.count("Correct")
            
        print(str(cou)+" number(s) are Guessed correct")
    print("You took "+str(c)+" chances")

        
while ch == 1:
    game()
    ch = int(input("Do you want to play again(Yes(1),No(0)): "))
