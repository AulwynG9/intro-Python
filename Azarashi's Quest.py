#Hello Player to the new open world experience game called Azarashi’s Quest. This game is about a poor village boy named Azarashi who lives with his mother in a small village. One day Azarashi’s town gets attacked by monsters and he is the only one to survive. Due  to this Azarashi finds the house of one of the elder masters. This elder masters name is Tengen. Tengen is very powerful but his body is decaying due to him being alive for 1000 years.Tengen offers his power to Azarashi saying that he has lived his life and feels as if Azarashi should be the one with Tengen’s power. Azarashi accepts this blessing and obtains the power.Shortly after Tengen dies and Azarashi burys him in the front yard of his house.


#After burying Tengen Azarashi returns to his village and slays all the monsters with his new power. Of course Azarashi wins the battle against most of the monsters in the forest. He goes to walk out of the forest covered in blood from the many monsters he slayed to avenge his village and mother. He collapes on the ground and wakes up hours later on the grass. He then swears from were he is laying his despise for monsters and swears to Slay them all.


#Azarashi is now traveling to achieve his dream of slaying all the monsters in the world. He rests for the day after saving a couple from goblins. While resting he has a dream about his mothers final words to him while she died in his arms. She told to always stay the way you are and to not let his heart decay. Azarashi wakes up with a fuss and cries while while still swearing to slay the monsters that took his mother away from him. Azarashi unable to sleep after the dream travels and fights throughout the night and happens to come upon a village. He is tired is slightly injured from the fighting. He collapeses and is caught by none other then the village chief himself who sends him to the first aid center with mages there to heal him. After being healed and getting some well deserved rest Azarashi rises and sees the village chief sitting in the chair next to his bed cutting apples. He asks the village chief what he is doing here. The village chief says that he found him collapsed in front of the village injured and exhuasted so he healed him and let him rest. The village chief also mentions that he saved Azarashi so he needs payment. Azarashi says he has no money to pay but offers to do anything else. The village chief says he can slay the goblins that attacks the village every night. Azarashi accepts. FIND OUT THE REST BY BUYING OUR GAME!!!!


import random

class Player:
    def __init__(self, name, health=100, attack=10):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

def battle(player, monster):
    print(f"You encounter a {monster.name}!")
    
    while player.is_alive() and monster.is_alive():
        player_damage = random.randint(1, player.attack)
        monster_damage = random.randint(1, monster.attack)

        print(f"{player.name} attacks the {monster.name} for {player_damage} damage.")
        monster.take_damage(player_damage)
        
        if not monster.is_alive():
            print(f"{player.name} has defeated the {monster.name}!")
            break

        print(f"The {monster.name} attacks {player.name} for {monster_damage} damage.")
        player.take_damage(monster_damage)

        if not player.is_alive():
            print(f"{player.name} has been defeated by the {monster.name}.")
            break

player = Player("Azarashi")
monsters = [
    Monster("Goblin", 20, 5),
    Monster("Skeleton", 15, 8),
    Monster("Orc", 25, 10)
]

for monster in monsters:
    battle(player, monster)

print("Azarashi has slain all the monsters in the village of Taj and vows to continue his journey to rid the world of all monsters.")


#This is a simple Python script that simulates battles between Azarashi and different monsters.The players health and attack values are
#set at the beginning and each monster has its own health and attack values as well. The player and monsters take turns hitting each other
#until one of them is defeated.After defeating all the monsters in the village of Taj Azarashi swears to his mother and himself 
#to slay every last monster on the earth.