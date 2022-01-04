import random


game=['r','p','s']

compScore=0
playerScore=0



      
    



while True:
    if compScore >=5:
        print(f'Compter win {compScore}')
        break

    elif playerScore>=5:
         print(f'User win {playerScore}')
         break


    else:
     b=random.choice([0,1,2])
     compVar=game[b]
     userVar =input('For Rock click r, for Paper click p, for Scissers click s ')


    
    if userVar.isdigit():
        print('--------------------------')

        print(f'Input text must be a string not a number {userVar} ')
        break
   
    elif userVar=='r' and compVar=='r':
        print('--------------------------')
    
        print('It is a draw')
        print(f'User score : {playerScore}')
        print(f'Computer score : {compScore}')
        print('')
    elif userVar =='p' and compVar=='p':
        print('--------------------------')
        print('It is a draw')
        print(f'User score : {playerScore}')
        print(f'Computer score : {compScore}')
        print('')

    elif userVar =='s' and compVar=='s':
        print('--------------------------')
        print('It is a draw')

        print(f'User score : {playerScore}')
        print(f'Computer score : {compScore}')
        print('')
    elif userVar =='r' and compVar=='p':
        print('--------------------------')
        print('Computer wins')
   
       
        compScore+=1
        print(f'User score : {playerScore}')
        print(f'Computer score : {compScore}')
        print('')
    elif userVar =='r' and compVar=='s':
        print('--------------------------')
        print('User wins')
        
        playerScore+=1
        print(f'User score : {playerScore}')
        print(f'Computer score : {compScore}')
        print('')
    elif userVar =='p' and compVar=='r':
        print('--------------------------')
        print('User wins')
        
        playerScore+=1
        print(f'User score : {playerScore}')
        print(f'Computer score : {compScore}')
        print('')
    elif userVar =='p' and compVar=='s':
        print('--------------------------')
        print('Computer wins')
        
        compScore+=1
        print(f'User score : {playerScore}')
        print(f'Computer score : {compScore}')
        print('')
    elif userVar =='s' and compVar=='r':
        print('--------------------------')
        print('Computer wins')
        
        compScore+=1
        print(f'User score : {playerScore}')
        print(f'Computer score : {compScore}')
        print('')
    elif userVar =='s' and compVar=='p':
        print('--------------------------')
        print('User wins')
        playerScore+=1
        print(f'User score : {playerScore}')
        print(f'Computer score : {compScore}')
        print('')
    
  





 

