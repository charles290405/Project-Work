
import random



ladder = {27: 8, 34: 7, 29: 3, 69: 31, 72: 36, 77: 46, 80: 41, 96: 48, 98: 79,} 
snake  =  {4: 16, 6: 25, 12: 49, 20: 40, 38: 88, 58: 62, 71: 93, 78: 84, 86: 95,}  

pos1=0
pos2=0 
pos3=0
pos4=0 

def move(pos):
        dice=random.randint(1,6)
        print(f"Dice:{dice}")
        pos = pos + dice
        if pos in snake:
            print("bitten by snake")
            pos = snake[pos]
            print(f"position:{pos}")
        elif pos in ladder:
            print("climbed ladder")
            pos = snake[pos]
            print(f"position:{pos}")
        else:
             print(f"position:{pos}")
        print("\n")
        return pos

while True:
        A = input("player 1 enter \"A\" to throw dice:")
        pos1 = move(pos1)
        if pos1 >= 100:
           print("game over!!!\nPlayer 1 wins.")
           break
        B= input("player 2 enter \"B\" to throw dice:")
        pos2 = move(pos2)
        if pos2 >= 100:
           print("game over!!!\nPlayer 2 wins.")
           break
        C  = input("player 3 enter \"C\" to throw dice:")
        pos3 = move(pos3)
        if pos3 >= 100:
           print("game over!!!\nPlayer 3 wins.")
           break
        D= input("player 4 enter \"D\" to throw dice:")
        pos4 = move(pos4)
        if pos4 >= 100:
           print("game over!!!\nPlayer 4 wins.")
           break