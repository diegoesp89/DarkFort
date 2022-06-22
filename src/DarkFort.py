import random as rng
import pygame as pg
import os

room_quantity = 6
rooms = []
names_all = []
tries = 0
debugflag = True

# # initialize pygame
# pg.init()

# # Initializing surface
# screen = pg.display.set_mode((800,600))

# # Initialing Color
# color = (255,0,0)

def clear_console():
    pass
    # os.system('cls' if os.name == 'nt' else 'clear')


def dice(d = 1, q = 1) -> int:
    total = 0
    for _ in range(q):
        result = rng.randrange(1, d+1)
        total += result
    return total

#the list of weapons of the game with an id starting with 1 a name a damage and a plus to hit
#the 1 is a warhammer with 5 damage and a plus of 0
#the 2 is a dagger with 4 damage and a plus to hit of 1
#the 3 is a sword with 6 damage with a plus to hit of 1
#the 4 is a flail with 6 damage+1 and a plus to hit of 0
class Weapon(object):
    def __init__(self, id, name, damage, plus):
        self.id = id
        self.name = name
        self.damage = damage
        self.plus = plus

weapons = [Weapon(1, "Warhammer", 5, 0), Weapon(2, "Dagger", 4, 1), Weapon(3, "Sword", 6, 1), Weapon(4, "Flail", 6, 0)]

#the class Item has an id name, a description, a uses and a effect
class Item(object):
    def __init__(self, id, name, description, uses, effect):
        self.id = id
        self.name = name
        self.description = description
        self.uses = uses
        self.effect = effect

#the list of items of the game, first with a list called B and after that a list of 6 items
#the first item is an armor with the effect of -4 damage
#the second item is a potion with the effect of +6 hp
#the third item is a scroll with the effect of Summon weak daemon
#the fourth item is a scroll of invisibility with the effect of make you invisible
items_list_B = [Item(5, "Armor", "This armor is made of steel and has a -d4 damage", 0, 4), Item(6, "Potion", "This potion is made of a green liquid and has a +d6 hp bonus", 1, 6), Item(7, "Scroll of Daemon Summon", "This scroll is made of a white paper and has a Summon weak daemon effect", rng.randrange(1,4), "Summon weak daemon"), Item(8, "Cloak of invisibility", "This cloak is made of a white paper and has a make you invisible effect", rng.randrange(1,4), "Invisible")]

#items of scrolls its a list of items
#the first is a Summon weak daemon, d4 effect, d4 damage as description
#the second is Open the southern gate, d6+1 effect, 1 in 4 uses as description
#the third is Aegis of sorrow, -d4 damage effect, 1 in 4 uses uses as description
#the fourth is False Omen, its effect is "Reroll room"
items_of_scrolls = [Item(9, "Scroll of Daemon Summon", "This scroll is made of a white paper and has a Summon weak daemon effect", rng.randrange(1,4), "Summon weak daemon"), Item(10, "Open the southern gate", "1 in 4 uses", rng.randrange(1,4), "d6+1"), Item(11, "Aegis of sorrow", "1 in 4 uses", rng.randrange(1,4), "-d4"), Item(12, "False Omen", "Reroll room", 1, "Reroll room")]

final_items = [Item(13, "Rope", "This rope is made of a soft string and has a +1 on trap rolls", 0, 1)]

#this is the general items
def get_item():
    d = dice(6,1)
    if d == 1:
        return items_list_A[rng.randrange(0, len(items_list_A))]
    elif d == 2:
        return items_list_B[1]
    elif d == 3:
        return final_items[0]
    elif d == 4:
        #return a random scroll from the items of scrolls list
        return items_of_scrolls[rng.randrange(0, len(items_of_scrolls))]
    elif d == 5:
        #return armor from items list B
        return items_list_B[0]
    elif d == 6:
        return items_list_B[3]





def starting_pack():
    #the variable a has an item from weapons list
    a = weapons[rng.randrange(0, len(weapons))]
    #the varaible b has an item from items B list
    b = items_list_B[rng.randrange(0, len(items_list_B))]
    return [a, b]

def room_shape():
    s = dice(6, 2)
    #2 irregular cave, 3 oval, 4 cross-shaped, 5 corridor, 6-8 square, 9 round, 10 rectangular, 11 triangular, 12 skull-shaped
    if s == 2:
        return "irregular cave"
    elif s == 3:
        return "oval"
    elif s == 4:
        return "cross-shaped"
    elif s == 5:
        return "corridor"
    elif s in [6, 7, 8]:
        return "square"
    elif s == 9:
        return "round"
    elif s == 10:
        return "rectangular"
    elif s == 11:
        return "triangular"
    elif s == 12:
        return "skull-shaped"


class Player:
    def __init__(self, name = "Kargunt", tries = 1):
        self.items = []
        self.name = name
        self.hp = 15
        self.maximum_hp = 15
        self.silver = 15 + dice(6, 1)
        self.level = 1
        self.explored_rooms = 0
        self.xp = 0
        self.location = 0
        self.tries = tries
        self.defense = 0
        self.cloak_uses = 0
        self.daemon_uses = 0
        it = starting_pack()
        self.items.extend(iter(it))

    #the function to take damage and check if the player is dead yet, show the final player stats and exit the game
    def take_damage(self, damage):
        print("You took {0} damage".format(damage))
        self.hp -= damage
        if self.hp <= 0:
            print("You died!")
            print(f"You had {self.silver} silver")
            print(f"You had {self.xp} xp")
            print(f"You had {self.explored_rooms} explored rooms")
            print(f"You had {self.level} levels")

            print("Thanks for playing!")
            exit()

    #the function to show the stats
    def show_stats(self):
        clear_console()
        print(f"{self.name} has {self.hp} hp of {self.maximum_hp} hp")
        print(f"{self.name} has {self.silver} silver")
        print(f"{self.name} has {self.xp} xp")
        print(f"{self.name} has {self.explored_rooms} explored rooms")
        print(f"{self.name} has {self.level} levels")
        print(f"{self.name} has {self.defense} defense")
        print(f"{self.name} has {self.daemon_uses} uses of the daemon")
        input("Press enter to continue")

    #the function to show the inventory
    def show_inventory(self):
        clear_console()
        print(f"{self.name}'s inventory:")
        #show all the items from player and if there is no item, show that there is no item, also if the item has an effect show it
        if len(self.items) == 0:
            print("You have no items")
        else:
            for item in self.items:
                #print name damage and plus of the item if the item.id is between 1 and 4
                if item.id in range(1, 5):
                    print(f"{item.name} has {item.damage} damage and {item.plus} plus")
                else:
                    print(f"{item.name} \"{item.description}\" with {item.effect} effect and {item.uses} uses")

        #if item has substring in name "armor", "cloak", "potion", "daemon" list as option to select one use
        defense_armor = 0
        cloak_uses = 0
        daemon_uses = 0
        for item in self.items:
            index = 0
            if "armor" in item.name or "Armor" in item.name and self.defense == 0:
                print(f"A. Equip armor (defense -d{item.effect} damage)")
                defense_armor = item.effect
                index += 1
            elif "cloak" in item.name or "Cloak" in item.name:
                print(f"C. Equip cloak (avoid {item.uses} battles)")
                cloak_uses = item.uses
                index += 1
            elif "potion" in item.name or "Potion" in item.name:
                print("P. Drink potion (Heal +d6 HP)")
                index += 1
            elif "daemon" in item.name or "Daemon" in item.name:
                print("D. Summon daemon")
                daemon_uses = item.uses
                index += 1
        #user input to select one of the options
        if index > 0:
            choice = input("Select an option: ")
        else:
            choice = 0
        #if user input is A, equip armor
        if choice == "A" or choice == "a":
            self.equip_armor(defense_armor)
        #if user input is C, equip cloak
        elif choice == "C" or choice == "c":
            self.equip_cloak(cloak_uses)
            for i in self.items:
                if "Cloak" in i.name or "cloak" in i.name:
                    self.items.remove(i)
        #if user input is P, drink potion
        elif choice == "P" or choice == "p":
            self.drink_potion()
            #remove an item potion from the player's inventory
            for i in self.items:
                if "potion" in i.name or "Potion" in i.name:
                    self.items.remove(i)
        #if user input is D, use daemon
        elif choice == "D" or choice == "d":
            self.summon_daemon(daemon_uses)
            #removes the item from the player's inventory
            for i in self.items:
                if "daemon" in i.name or "Daemon" in i.name:
                    self.items.remove(i)


        #wait for user input to continue
        input("Press enter to continue")

    #the function to equip armor
    def equip_armor(self, defense_armor):
        self.defense = defense_armor
        print(f"You equipped armor with {self.defense} defense")

    #the function to equip cloak
    def equip_cloak(self, cloak_uses):
        self.cloak_uses = cloak_uses
        print(f"You have {self.cloak_uses} uses of the invisibility cloak left")
    
    #the function to drink potion
    def drink_potion(self):
        #the potion heals between 1 and 6 hp to player and removes the potion from the inventory also shows how much HP has recovered
        heal = dice(6, 1)
        self.hp += heal
        #if the player has more than 15 hp, set the player hp to 15
        if self.hp > 15:
            self.hp = 15
        print(f"You healed {heal} hp")

    #the function to summon daemon
    def summon_daemon(self, daemon_uses):
        self.daemon_uses = daemon_uses
        print(f"You have {self.daemon_uses} uses of the daemon left")

    #the function to attack a monster
    def attack(self, monster):
        attack_loop = True
        while attack_loop:
            clear_console()

            #if the player has a cloak, the player can avoid the monster's attack
            if self.cloak_uses > 0:
                print(f"{self.name} has a cloak and has avoided the monster!")
                self.cloak_uses -= 1
                #kill the monster and end the attack loop
                monster.hp = 0
                attack_loop = False
                #get the monster points as xp
                self.xp += monster.points
                print(f"You got {monster.points} XP points")
            #let the player choose a weapon or a spell
            print("What do you want to use?")
            #print the list of weapons and spells in items of the player to choose with the id and name for the player to choose
            for item in self.items:
                print(f"{item.id} - {item.name}")
            #if the user has Daemon uses left, list the option of using the daemon
            if self.daemon_uses > 0:
                print("D. Use daemon")
    
            #get the id of the weapon or spell the player wants to use
            choice = input("Enter the id of the item you want to use: ")
            #if the player wants to use a weapon from id 1 to 4
            if choice in ["1", "2", "3", "4"]:
                for i in self.items:
                    if i.id == int(choice):
                        ret = monster.take_damage(i.damage, i.plus, None, self.defense)
                #if the reward is not None, the player gets the reward if is it 0 just continue, if it is not 0, the player gets the reward
                if ret[0] != None and isinstance(ret[0], int) and ret[0] != 0:
                    self.xp += ret[0]
                    #set the current room explored to True
                    rooms[self.location].explored = True
                    attack_loop = False
                #check if ret[1] is a number, then if is greater than 0, if it is, take damage and continue to the next cycle
                if isinstance(ret[1], int) and ret[1] > 0:
                    self.take_damage(ret[1])
                    attack_loop = False
                    continue
                
                #if back_damage is string and it has scroll, the player get the scroll
                if isinstance(ret[1], str) and ret[1] == "scroll":
                    scroll = items_of_scrolls[rng.randrange(0, len(items_of_scrolls))]
                    self.items.append(scroll)
                    #print the scroll the player got
                    print(f"You got {scroll.name} Scroll!")
                #if back_damage is string and it has dagger the player get the dagger that is the weapon of id 2
                if isinstance(ret[1], str) and ret[1] == "dagger":
                    self.items.append(weapons[1])
                    #print the dagger the player got
                    print(f"You got {weapons[1].name}!")
                #if back_damage is string and it has rope the player get the rope that is the item of id 13
                if isinstance(ret[1], str) and ret[1] == "rope":
                    self.items.append(final_items[0])
                    #print the rope the player got
                    print(f"You got {final_items[0].name}!")

            elif choice == "5":
                #the player equip the armor
                defense_armor = 0
                for i in self.items:
                    if i.name == "Armor" or i.name == "armor":
                        defense_armor = i.effect
                self.equip_armor(defense_armor)
            elif choice == "6":
                #the player drinks a potion
                self.drink_potion()
                #remove the potion from the inventory
                for i in self.items:
                    if "potion" in i.name or "Potion" in i.name:
                        self.items.remove(i)
                
            elif choice == "D" or choice == "d":
                #if the player has Daemon uses left, use the daemon and continue to the next cycle
                if self.daemon_uses > 0:
                    self.daemon_uses -= 1
                    ret = monster.take_damage(4, 0, "daemon")
                    if self.daemon_uses == 0:
                        print("The daemon its gone")
            else:
                print("Invalid selection, choose again")

        #wait for user input to continue
        input("Press enter to continue")



            

class Monster:
    def __init__(self, name = "Default", points = 1, damage = 10, secondary_damage = 0 , hp = 10, item = None):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.points = points
        self.item = item
        self.secondary_damage = secondary_damage

    #the function to take damage and check if the monster is dead yet, show the final monster stats and exit the game
    def take_damage(self, damage, secondary_damage, summon = None, defense = 0):
        #if secondary_damage is more than 0 sum it to d
        d = dice(6, 1)
        print("You rolled a {0}".format(d))
        if summon is None:
            print("The weapon has a plus of {0}".format(secondary_damage))
        else:
            print(f"The {summon} has a {d} of bonus to hit")
        if secondary_damage > 0:
            d += secondary_damage
        if d >= self.points:
            return self.subdamage(damage)
        if summon is None:
            print(f"You missed {self.name}!")

        else:
            print(f"{summon} has missed the attack")
        if summon is None:
            damage = dice(1, self.damage)
            #the final damage is calculated as damage minus a number between 1 and the defense of the player
            defe =  rng.randrange(1, defense)
            damage -= defe
            print(f"{self.name} hit you for {damage} damage! (the armor absorved {defe} damage)")
        else:
            damage = 0

        input("Press enter to continue")
        return None, damage

    def subdamage(self, damage):
        #damage is a number between 1 and damage
        damage = dice(1, damage)
        print(f"You hit {self.name} for {damage} damage!")
        self.hp -= damage
        print(f"{self.name} has {self.hp} hp now")
        #wait for user input to continue
        input("Press enter to continue")

        if self.hp > 0:
            return 0, 0
        print(f"{self.name} died!")


        #the player gets the item if there is one in the monster item list
        if self.item != None:
            print(f"{self.name} dropped {self.item}")
        #the player gets xp points based on points of the monster
        print(f"You got {self.points} XP points")
        #return the item and xp points to the player
        item = self.item
        if item is None:
            return [self.points, 0]
        return [self.points, item]


def roll_weak_monster():
    d = dice(4, 1)
    #this is a blood-drenched skeleton with 3 points, 4 damage and 6 hp, with a chance of 2/6 to have a dagger
    if d == 1:
        if(dice(6, 1) > 1):
            return Monster("Skeleton", 3, 4, 0, 6, "dagger")
        return Monster("Blood-Drenched Skeleton", 3, 4, 6)
    #this is a catacomb cultist with 3 points, 4 damage and 6 hp with a random scroll
    elif d == 2:
        return Monster("Catacomb Cultist", 3, 4, 0, 6, "scroll")
    #this is a goblin with 3 points, 4 damage and 5 hp with a chance of 2/6 to have a rope
    elif d == 3:
        if(dice(6, 1) > 1):
            return Monster("Goblin", 3, 4, 0, 5, "rope")
        return Monster("Goblin", 3, 4, 0, 5)
    #this is an undead hound with 4 points, 4 damage and 6 hp
    elif d == 4:
        return Monster("Undead Hound", 4, 4, 0, 6)



def roll_strong_monster():
    d = dice(4, 1)
    #this is a Necro-Sorcerer with 4 points, 4 damage and 6 secondary damage, and 8 hp, with dice(6,3) silver as item
    if d == 1:
        return Monster("Necro-Sorcerer", 4, 4, 6, 8, dice(6,3))
    #this is a Small Stone Troll with 3 points, 4 damage, 6 hp, with a chance of 2/6 to have a scroll
    if d == 2:
        if(dice(6, 1) > 1):
            return Monster("Small Stone Troll", 3, 4, 0, 6, "scroll")
        else:
            return Monster("Small Stone Troll", 3, 4, 0, 6)

        


    

class Room:
    def __init__(self, room_id, exits):
        name_gen = "Entrance" if (room_id == 0) else name_generator()
        self.id = room_id
        self.name = name_gen
        self.exits = exits
        self.item = 0
        self.weak_monster = 0
        self.strong_monster = 0
        self.pit_trap = 0
        self.riddle = 0
        self.peddler = 0
        self.shape = room_shape()
        self.explored = False
        self.rooms_connected = []
        self.room_roll = 0
        self.x = 0
        self.y = 0

        room_r = dice(6, 1)
        self.room_roll = room_r
        if self.room_roll == 1:
            self.explored = True
        elif self.room_roll == 2:
            self.pit_trap = 1
        elif self.room_roll == 3:
            self.riddle = 1
        elif self.room_roll == 4:
            self.weak_monster = roll_weak_monster()
        elif self.room_roll == 5:
            self.strong_monster = roll_strong_monster()
        elif self.room_roll == 6:
            self.peddler = 1

        #if there is a debug flag, the room with id 0 will start with a weak monster
        if debugflag:
            if self.id == 0:
                self.weak_monster = roll_weak_monster()


def name_generator() -> str:
    ar1 = open("C:\\Users\\strif\\Downloads\\DarkFortCopilot\\DarkFort\\src\\firstname.txt")
    ar2 = open("C:\\Users\\strif\\Downloads\\DarkFortCopilot\\DarkFort\\src\\secondname.txt")
    ar3 = open("C:\\Users\\strif\\Downloads\\DarkFortCopilot\\DarkFort\\src\\connector.txt")
    ar4 = open("C:\\Users\\strif\\Downloads\\DarkFortCopilot\\DarkFort\\src\\adjective.txt")

    names = file_get(ar1)
    surnames = file_get(ar2)
    connector = file_get(ar3)
    adjective = file_get(ar4)
    name = "The {0} {1} {2} {3}".format(rng.choice(adjective), rng.choice(names), rng.choice(
        connector), rng.choice(surnames))
    for n in names_all:
        if n == name:
            name = "The {0} {1} {2} {3}".format(rng.choice(adjective), rng.choice(names), rng.choice(
                connector), rng.choice(surnames))
    names_all.append(name)
    return name


def file_get(file) -> list:
    result = file.read()
    result = result.split("\n")
    file.close()

    return result


def exits_generate(actual_id) -> int:
    exits = 0
    if actual_id == 0:
        exits = dice(4, 1)
    else:
        result = dice(4, 1)
        if result == 1:
            exits = 0
        elif result == 2:
            exits = 1
        elif result in [3, 4]:
            exits = 2
    return exits

#connection between the rooms using the number of exits randomized
def connect_rooms(room_id, exits):
    for _ in range(exits):
        room_connect = rng.randrange(1, room_quantity)
        while room_connect == room_id:
            room_connect = rng.randrange(1, room_quantity)
        if room_connect not in rooms[room_id].rooms_connected:
            rooms[room_id].rooms_connected.append(room_connect)
            rooms[room_connect].rooms_connected.append(room_id)
    

#draw the rooms in the screen with pygame
def draw_maze():
    #draw a square for each room
    #draw the exits for each room
    #draw the items for each room
    #draw the monsters for each room
    #draw the traps for each room
    #draw the riddles for each room
    #draw the peddlers for each room
    #draw the shapes for each room
    for room in rooms:    
        x = rng.randrange(100, 700)
        y = rng.randrange(100, 500)    
        room.x = x
        room.y = y
        #check if the room is overlapping another room
        for room_check in rooms:
            if room_check.x == room.x and room_check.y == room.y:
                x = rng.randrange(100, 700)
                y = rng.randrange(100, 500)
                room.x = x
                room.y = y
            if not room.explored:
                color = (255,0,0)
            else:
                color = (0,255,0)
                #randomize the position of the room

                #draw the room with its shape
                if room.shape == "irregular cave":
                    pg.draw.rect(screen, color, (room.x, room.y, 100, 100))
                elif room.shape == "oval":
                    pg.draw.ellipse(screen, color, (room.x, room.y, 100, 100))
                elif room.shape == "cross-shaped":
                    pg.draw.ellipse(screen, color, (room.x, room.y, 100, 100))
                elif room.shape == "corridor":
                    pg.draw.rect(screen, color, (room.x, room.y, 100, 100))
                elif room.shape == "square":
                    pg.draw.rect(screen, color, (room.x, room.y, 100, 100))
                elif room.shape == "round":
                    pg.draw.circle(screen, color, (room.x + 50, room.y + 50), 50)
                elif room.shape == "rectangular":
                    pg.draw.rect(screen, color, (room.x, room.y, 100, 100))
                elif room.shape == "triangular":
                    pg.draw.polygon(screen, color, [(room.x, room.y), (room.x + 100, room.y), (room.x + 50, room.y + 100)])
                elif room.shape == "skull-shaped":
                    pg.draw.polygon(screen, color, [(room.x, room.y), (room.x + 100, room.y), (room.x + 50, room.y + 100)])

    #draw the connections between the rooms
    for room in rooms:
        for room_connected in room.rooms_connected:
            color = (0,0,255)
            pg.draw.line(screen, color, (rooms[room.id].x, rooms[room.id].y), (rooms[room_connected].x, rooms[room_connected].y))

#menu for the terminal game
def menu(player):
    clear_console()
    print("Welcome to the Dark Fort")
    print("1. New Game")
    # print("2. Load Game")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        new_game()
        run(player)
    # elif choice == "2":
    if choice == "3":
        exit()

def new_game():
    rooms.clear()
    for i in range(room_quantity):
        rooms.append(Room(i, exits_generate(i)))
    for r in rooms:
        connect_rooms(r.id, r.exits)

def run(player):
    while True:
        clear_console()
        #show the name of the room where is the player
        print("You are in {0}".format(rooms[player.location].name))
        #show if the room is already explored or not
        if rooms[player.location].explored:
            print("This room is already explored")
        #show what is in the room
        print("You see:")
        #show the items, monsters, traps, riddles, peddlers, shapes if there is any in the current room

        if rooms[player.location].item:
            print("Item:")
            print(rooms[player.location].item)
        if rooms[player.location].pit_trap:
            print("Pit Trap")
        if rooms[player.location].riddle:
            print("Riddle")
        if rooms[player.location].weak_monster:
            #prints the weak monster name and its hp in a single line if the monster has more than 0 hp
            if rooms[player.location].weak_monster.hp > 0:
                print(f"Weak Monster | Name: {rooms[player.location].weak_monster.name} | HP: {rooms[player.location].weak_monster.hp}")
        if rooms[player.location].strong_monster:
            #prints the name of the monster and its hp in a single line if the monster has more than 0 hp
            if rooms[player.location].strong_monster.hp > 0:
                print(f"Strong Monster | Name: {rooms[player.location].strong_monster.name} | HP: {rooms[player.location].strong_monster.hp}")
        if rooms[player.location].peddler:
            print("Peddler")
        
        #show the exits if there is any in the current room
        if rooms[player.location].rooms_connected:
            print("Exits:")
            for room in rooms[player.location].rooms_connected:
                print(rooms[room].name)
        #ask the player what he wants to do}
        print("")
        print("What do you want to do?")
        #if the player is in the entrance, another opcion is exit to start a new game
        if player.location == 0:
            print("S. Start a new run")


        #let the player choise what to do, if there is a weak monster or a strong monster in the room, the player has to attack the monster, else the player can go to another room
        #also the run option must be only visible if the monster in the room have more than 0 hp and the room is not explored
        if rooms[player.location].weak_monster or rooms[player.location].strong_monster and rooms[player.location].weak_monster.hp > 0 or rooms[player.location].strong_monster.hp > 0:
            if not rooms[player.location].explored:
                print("A. Attack")
                print("R. Run")   
        else:
            print("G. Go to another room")

        #print an option for the player to check its inventory and another option to check its stats
        print("I. Check inventory")
        print("P. Check stats")
        
        #let the player choose between the options
        choice = input("Enter your choice: ")
        clear_console()
        if choice == "A" or choice == "a":
            if rooms[player.location].weak_monster:
                player.attack(rooms[player.location].weak_monster)
            elif rooms[player.location].strong_monster:
                player.attack(rooms[player.location].strong_monster)
        if choice == "G" or choice == "g" or choice == "R" or choice == "r":
            #let the player choose which room to go to, listing all rooms connected with an autogenerated temporal id
            if choice == "G" or choice == "g":
                print("Which room do you want to go to?")
            if choice == "R" or choice == "r":
               
                player.hp -= dice(4, 1)
                rooms[player.location].explored = False
                #show the player the damage taken, the room is going to enter and wait for input to continue

                damage = dice(4, 1)
                #take the damage
                player.take_damage(damage)
                input("Press enter to continue")
                print("Which room do you want to go run to?")
                
            #r_conn is the quantity of rooms connected with the current room
            r_conn = len(rooms[player.location].rooms_connected)
            for i in range(r_conn):
                print("{0}. {1}".format(i, rooms[rooms[player.location].rooms_connected[i]].name))
            #let the player choose which room to go to
            while True:
                choice = input("Enter your choice: ")
                clear_console()
                #check if the player choose a valid room
                if int(choice) < r_conn:
                    player.location = rooms[player.location].rooms_connected[int(choice)]
                   
                    break
                else:
                    print("Invalid choice")
        #if the player choose to check its stats it shows the player's stats
        if choice == "P" or choice == "p":
            player.show_stats()
        #if the player choose to check its inventory it shows the player's inventory
        if choice == "I" or choice == "i":
            player.show_inventory()
        if choice == "S" or choice == "S" and player.location == 0:
            #restart all the application
            new_game()
            main()

            





  

            


def main():
    #clear the console

    player = Player()
        # printDebug(r)
    # draw_maze()
    # pg.display.update()
    # while True:
    #     continue
    # print(f"Location:{player.location}")
    # print(f"Items:{player.items}")
    menu(player)


def printDebug(room):
    pass
    # print(f"ID:{room.id}")
    # print(f"Name:{room.name}")
    # print(f"Exits:{room.exits}")
    # print(f"Connected:{room.rooms_connected}")
    # print(f"RoomR:{room.room_roll}")
    # print("")


if __name__ == "__main__":
    main()
