import random

class Robot(object):
    robot_list = []

    @staticmethod
    def contenders():
        robots = len(Robot.robot_list)
        print("There are", robots, "robots.\n")
        if robots:
            print("Here is a list of them:")
            for robot in Robot.robot_list:
                print(robot)

    @staticmethod
    def weapon_check():
        weapons = {}

        for robot in Robot.robot_list:
            if robot.weapon in weapons:
                weapons[robot.weapon].append(robot.name)
            else:
                weapons[robot.weapon] = [robot.name]

        for weapon in weapons.keys():
            print("The robots using the", weapon, "weapon are: ", end = '')

            print(", ".join(weapons[weapon]))

    @staticmethod
    def random_tournament():
        functional = Robot.robot_list.copy()

        round_num = 1

        while len(functional) > 1:
            functional.sort()
            print("\nRandom Tournament, Round", round_num, "!")

            for i in range(0, len(functional), 2):
                if i+1 <= len(functional) - 1:
                    robot1 = functional[i]
                    robot2 = functional[i+1]
                    robot1.fight(robot2)
                else:
                    print(functional[i].name, "gets a bye this round!")

            new_functional = []
            for robot in functional:
                if robot.online:
                    new_functional.append(robot)
            functional = new_functional

            round_num += 1

        print("\nThe ultimate winner is:", functional[0].name)

    def __init__(self, name, weapon, strength):
        print("Robot created!", name, "\n")
        self.name = name
        self.weapon = weapon
        self.strength = strength
        self.online = True
        Robot.robot_list.append(self)

    def __str__(self):
        reply = "-" * 20 + "\n"
        reply += "Fighting Robot\n"
        reply += "Name: " + self.name + "\n"
        reply += "Weapon: " + self.weapon + "\n"
        reply += "Strength: " + str(self.strength) + "\n"
        if self.online:
            reply += "Status: ONLINE\n"
        else:
            reply += "Status: OFFLINE\n"
        reply += "-" * 20 + "\n"
        return reply

    def __lt__(self, other):
        if self.strength < other.strength:
            return True
        else:
            return False

    def fight(self, opponent):
        print(self.name, "challenges", opponent.name)            
        
        if not self.online:
            print(self.name, "cannot fight - it is offline.")
        elif not opponent.online:
            print(opponent.name, "cannot fight - it is offline.")
        else:
            if self.strength > opponent.strength:
                winner = self
            elif self.strength < opponent.strength:
                winner = opponent
            else:
                print("Close match!!!")
                winner = random.choice([self, opponent])
                                
            if winner == self:
                print(self.name, "wins, using its", self.weapon)
                opponent.online = False
            else:
                print(opponent.name, "wins, using its", opponent.weapon)
                self.online = False

            #print(self)
            #print(opponent)

    
#main
r2d2 = Robot("R2D2", "Beeps", 2)
c3p0 = Robot("C3P0", "Conversation", 2)
bb8 = Robot("BB-8", "Beeps", 1)
j = Robot("Robot J", "Conversation", 2)
optimus = Robot("Optimus", "Fists", 10)
voltron = Robot("Voltron", "Sword", 10)
gipsy = Robot("Gipsy Danger", "Sword", 9)
Robot.random_tournament()
