import random
import time

class Main:
    def __init__(self):
        print("Welcome to PyRogue\n")
        time.sleep(1)
        
    def start_game(self):
        self.dungeon = Dungeon()
        self.dungeon.traverse_dungeon()

class Player(Main):
    def __init__(self):
        self.name = input("Enter your name: ")
        self.maxhp = 10
        self.hp = self.maxhp
        self.atk = 2
        self.dodge = 40
        self.gold = 0

    def show_stats(self):
        print(f"{self.name}'s HP: {self.hp}")
        print(f"{self.name}'s ATK: {self.atk}")
        print(f"{self.name}'s Probability of dodge: {self.dodge}%\n")
        time.sleep(2)

    def earn_gold(self):
        fight_gold = random.randrange(5, 16) 
        print(f"You received {fight_gold} golds")
        self.gold += fight_gold
        print(f"You have {self.gold} golds in total.\n")

    def buy_items(self):
        print("Do you want to buy an upgrade?\n")
        print("1)ATK Potion: 10 golds. Raise your ATK +1")
        print("2)DGD Potion: Raise your dodge to +5%.")
        print("3)Big Potion: 5 golds. Raise 2 HP.")
        print("4)Exit.\n")
        while True:
            item_option = input("Select your option: ")
            if item_option == "1":
                if self.gold < 10:
                    print("You don't have enough gold")
                else:
                    self.atk += 1
                    self.gold -=10
                    break
            elif item_option == "2":
                if self.gold < 10:
                    print("You don't have enough gold")
                else:
                    self.dodge += 5
                    self.gold -= 10
                    break
            elif item_option == "3":
                if self.gold < 5:
                    print("You don't have enough gold")
                else:
                    self.maxhp += 2
                    self.gold -= 5
                    print(f"Your Max HP is now {self.maxhp}")
                    break
            elif item_option == "4":
                    break
            else:
                print("Select a valid option")
                continue
        print(f"Total golds: {self.gold}\n")
        self.show_stats()

    def fight(self, enemy):
        enemy.show_stats()
        while True:
            print("Player's turn.\n")
            time.sleep(1)
            self.show_stats()
            time.sleep(2)
            while True:
                print("What do you want to do?")
                print("1) Attack.")
                print("2) Take a small potion. Recover 4` HP.")
                option = input("Select your option: ")
                print("")
                if option == "1":
                    enemy_dodge_calc = random.randrange(0,101) #Dodge calculation
                    if enemy_dodge_calc >= enemy.dodge:
                        enemy.hp -= self.atk
                        print(f"You hit the enemy with {self.atk} points!")
                        if enemy.hp > 0:
                            print(f"Remaining enemy's HP: {enemy.hp} points\n")
                            time.sleep(1)
                            break
                        else:
                            print(f"Remaining enemy's HP: 0 points")
                            print("You defeated the enemy\n")
                            self.earn_gold()
                            time.sleep(1)
                            return
                    else:
                        print("The enemy dodges your hit!\n")
                        time.sleep(1)
                        break
                elif option == "2":
                    if self.hp <= self.maxhp - 4:
                        self.hp += 4
                        print("You recover 4 HP.\n")
                        print(f"{self.name}'s HP: {self.hp}\n")
                        time.sleep(1)
                    else:
                        self.hp = self.maxhp
                        print("You recover 4 HP.\n")
                        print(f"{self.name}'s HP: {self.hp}")
                        time.sleep(1)
                    break
                else:
                    print("Select a valid option.")
                    continue

            print("Enemy's turn.\n")
            enemy.show_stats()
            time.sleep(2)
            player_dodge_calc = random.randrange(0,101)
            if player_dodge_calc >= self.dodge:
                self.hp -= enemy.atk
                print(f"The enemy hits you with {enemy.atk} points!")
                if self.hp > 0:
                    print(f"{self.name}'s HP: {self.hp}\n")
                    time.sleep(1)
                else:
                    print(f"{self.name}'s HP:0 points")
                    time.sleep(1)
                    break
            else:
                print("You dodge the enemy's hit!\n")
                time.sleep(1)

class Enemies(Main):
    def __init__(self):
        self.hp = random.randrange(4,7) #Random enemies stats
        self.atk = random.randrange(2,4)
        self.dodge = random.randrange(15,26)

    def show_stats(self):
        print(f"Enemy's HP: {self.hp}")
        print(f"Enemy's ATK: {self.atk}")
        print(f"Enemy's Probability of dodge: {self.dodge}%\n")
        time.sleep(2)

class Dungeon(Main):
    def __init__(self):
        pass

    def traverse_dungeon(self):
        player = Player()
        print("\nYou enter to the dungeon.\n")
        time.sleep(1)
        floor = 1
        while True:
            print(f"Floor {floor}\n")
            time.sleep(1)
            enemy = Enemies()
            fight_prob = random.randrange(0,101)
            if fight_prob <= 70:
                print("You found an enemy!\n")
                time.sleep(1)
                player.fight(enemy)
                if player.hp <= 0:
                    print("Game Over\n")
                    break
                elif enemy.hp <= 0:
                    print("Let's go to the next floor!\n")
                    floor += 1
                    time.sleep(1)
                    continue    
            else:
                print("There is no enemy on this floor.\n")
                time.sleep(1)
                if player.gold <= 5:
                    print("You don't have enough gold to buy an item.\n")
                    time.sleep(1)
                else:
                    player.buy_items()
                floor += 1
game = Main()
game.start_game()