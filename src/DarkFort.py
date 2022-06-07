import random as rng

rooms = []
room_quantity = 6
names_all = []
generation = 1


def dice(d = 1, q = 1) -> int:
    total = 0
    for _ in range(q):
        result = rng.randrange(1, d+1)
        total += result
    return total


def starting_pack():
    a = dice(4, 1)
    b = dice(4, 1)
    return a, b


class Player:
    def __init__(self, name = "Kargunt", generation = 1):
        self.items = []
        self.name = name
        self.hp = 15
        self.silver = 15 + dice(6, 1)
        self.level = 1
        self.explored_rooms = 0
        self.xp = 0
        self.location = 0
        self.generation = generation
        self.items.append(starting_pack())


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
        self.shape = 0
        self.explored = False
        self.room_roll = 0

        room_r = dice(6, 1)
        self.room_roll = room_r
        if self.room_roll == 1:
            self.explored = True
        elif self.room_roll == 2:
            self.pit_trap = 1
        elif self.room_roll == 3:
            self.riddle = 1
        elif self.room_roll == 4:
            self.weak_monster = 1
        elif self.room_roll == 5:
            self.strong_monster = 1
        elif self.room_roll == 6:
            self.peddler = 1


def name_generator() -> str:
    ar1 = open("C:\\Users\\strif\\Downloads\\DarkFort\\src\\firstname.txt")
    ar2 = open("C:\\Users\\strif\\Downloads\\DarkFort\\src\\secondname.txt")
    ar3 = open("C:\\Users\\strif\\Downloads\\DarkFort\\src\\connector.txt")
    ar4 = open("C:\\Users\\strif\\Downloads\\DarkFort\\src\\adjective.txt")

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


def main():
    player = Player()
    for i in range(room_quantity):
        rooms.append(Room(i, exits_generate(i)))
    for r in rooms:
        printDebug(r)
    print(f"Location:{player.location}")
    print(f"Items:{player.items}")


def printDebug(room):
    print(f"ID:{room.id}")
    print(f"Name:{room.name}")
    print(f"Exits:{room.exits}")
    print(f"RoomR:{room.room_roll}")
    print("")


if __name__ == "__main__":
    main()
