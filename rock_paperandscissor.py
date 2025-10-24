import random

Tie = 0
User_win = 0
Computer_win = 0
print("There will be total 5 rounds \n and results will be counter accordingly")
for i in range(5):
    secret = random.choice(['r', 'p', 's'])  
    print("Computer chose:", secret)
    
    user = input("Choose (R)ock, (P)aper or (S)cissor: ").lower()
    
    if user == secret:
        print("Tie")
        Tie += 1
    elif (user == 'r' and secret == 's') or (user == 'p' and secret == 'r') or (user == 's' and secret == 'p'):
        print("User Wins")
        User_win += 1
    elif (user == 's' and secret == 'r') or  (user == 'r' and secret == 'p') or (user == 'p' and secret == 's'):
        print("Computer Wins")
        Computer_win += 1
    else:
        print("Invalid input, please choose R, P, or S properly.")

print("\nFinal Score:")
print("Ties:", Tie)
print("User Wins:", User_win)
print("Computer Wins:", Computer_win)
   






