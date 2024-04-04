import random

class Player:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
        
    def roll_dice(self):
        return random.randint(1,6)
    
def main():
    print("Welcome to Dice Battle!")
    print("------RULES------")
    print("(1)Two Players take turns rolling a six standing die.")
    print("(2)If one roll is lower than the other,the player will lose some hit points.")
    print("(3)If both rolls has the same number, they will have a chance to heal.")
    print("(4)The game continues until one of the players reaches 0 hit points or below, and that player loses.")
    
    player1 = Player(input("Enter Player 1's name:  "), 20)
    player2 = Player(input("Enter Player 2's name:  "), 20)
    
    players=[player1, player2]
    current_player_index =0
    
    while True:
        current_player=players[current_player_index]
        opponent=players[(current_player_index + 1) % 2]
        print(f"\n{current_player.name}'s turn.")
        input("Press Enter to roll the dice...")
        
        roll1=current_player.roll_dice()
        roll2=opponent.roll_dice()
        print(f"{current_player.name} rolled: {roll1}")
        print(f"{opponent.name} rolled: {roll2}")
        
        if roll1<roll2:
            hp_loss=roll2-roll1
            print(f"You lose {hp_loss} HP.")
            current_player.hp-=hp_loss
            
        elif roll1>roll2:
           print(f"{current_player.name} wins this round. No HP lost")
            
        else:
            print("It's a Tie! Both players have the opportunity to heal")
            current_player.hp+=1
            opponent.hp+=1
            print(f"{current_player.name} and {opponent.name} gained 1 HP")
            
        print(f"{current_player.name}'s HP: {current_player.hp}")
        print(f"{opponent.name}'s HP: {opponent.hp}")
        
        if current_player.hp <= 0:
            print(f"{current_player.name} has lost!")
            break
        
        current_player_index=(current_player_index +1) %2
        
if __name__ == "__main__":
    main()

        
