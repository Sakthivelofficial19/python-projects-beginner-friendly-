import random # ●
def generator(board):
    n1,n2=random.sample(range(1,len(board)),2)
    return n1,n2
target_ships=2
print('''It's a battle ship game:
-------------------''')
board=[
[" ","A","B","C","D"],
["1","-","-","-","-"],
["2","-","-","-","-"],
["3","-","-","-","-"],
["4","-","-","-","-"]]
sample=[
[" ","A","B","C","D"],
["1","-","-","-","-"],
["2","-","-","-","-"],
["3","-","-","-","-"],
["4","-","-","-","-"]]

row1,row2=generator(board)
clm1,clm2=generator(board)
print("The hidden board :")
def display(x):
    for i in range(len(x)):
        for j in x[i]:
            print(j,end=" ")
        print()
display(board)        
board[row1][clm1],board[row2][clm2]="$","$"
lives=6
found=0
while True:
    print(f"\nyour lives: {lives*"●"}")
    choice=input("Enter your choice : ")
    choice=choice.replace(" ","")
    column=ord(choice[0])-64
    row=int(choice[1])
    if board[row][column]=="$":
        sample[row][column]="$"
        display(sample)
        found+=1
        if found==target_ships:
            print("Hurray! you won!")
            break
    else:
        lives-=1
        sample[row][column]=="x"
        display(sample)
        if lives==0:
            print("your lives over!")
            print("Better luck next time")
            break
