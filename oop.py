class Superhero:
    def __init__(self, name, power, secret_identity):
        self.name = name
        self.power = power
        self.__secret_identity = secret_identity  # Encapsulated

    def use_power(self):
        print(f"{self.name} uses {self.power}! ⚡")

    def reveal_identity(self):
        print(f"My real name is {self.__secret_identity}.")

# Inheritance
class Avenger(Superhero):
    def team_up(self):
        print(f"{self.name} assembles with the Avengers! 🛡️")

# Usage
hero = Avenger("Thor", "lightning", "Thor Odinson")
hero.use_power()           # Output: "Thor uses lightning! ⚡"
hero.reveal_identity()     # Output: "My real name is Thor Odinson."
hero.team_up()             # Output: "Thor assembles with the Avengers! 🛡️"