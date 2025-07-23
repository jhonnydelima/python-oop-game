class Character:
  def __init__(self, name, life, level) -> None:
    self.__name = name
    self.__life = life
    self.__level = level
  
  def get_name(self):
    return self.__name
  
  def get_life(self):
    return self.__life
  
  def get_level(self):
    return self.__level
  
  def show_info(self):
    return f"Name: {self.get_name()}\nLife: {self.get_life()}\nLevel: {self.get_level()}"
  
  def attack(self, target):
    if self.get_life() > 0:
      damage = self.get_level() * 2
      target.take_damage(damage)
      print(f"\n{self.get_name()} attacks {target.get_name()} and causes {damage} of damage!")
    else:
      print(f"\n{self.get_name()} cannot attack because they have no life left.")
  
  def take_damage(self, damage):
    self.__life -= damage
    if self.__life < 0:
      self.__life = 0

class Hero(Character):
  def __init__(self, name, life, level, skill) -> None:
    super().__init__(name, life, level)
    self.__skill = skill
  
  def get_skill(self):
    return self.__skill
  
  def show_info(self):
    return f"{super().show_info()}\nSkill: {self.get_skill()}\n"
  
  def use_skill(self, target):
    damage = self.get_level() * 5
    target.take_damage(damage)
    print(f"\n{self.get_name()} uses skill '{self.get_skill()}' on {target.get_name()} and causes {damage} of damage!")

class Enemy(Character):
  def __init__(self, name, life, level, type) -> None:
    super().__init__(name, life, level)
    self.__type = type
  
  def get_type(self):
    return self.__type
  
  def show_info(self):
    return f"{super().show_info()}\nType: {self.get_type()}\n"

class Game:
  def __init__(self) -> None:
    self.hero = Hero("HeroName", 100, 5, "Super Strength")
    self.enemy = Enemy("EnemyName", 80, 3, "Flying")
  
  def start(self):
    print("Game Started!")
    while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
      print("\nCharacters info:")
      print(self.hero.show_info())
      print(self.enemy.show_info())

      input("Press Enter to continue...")
      attack_choice = input("Press 1 to normal attack, or 2 to use skill: ")

      if attack_choice == '1':
        self.hero.attack(self.enemy)
      elif attack_choice == '2':
        self.hero.use_skill(self.enemy)
      else:
        print("\nInvalid choice. Please try again.")

      if self.enemy.get_life() > 0:
        self.enemy.attack(self.hero)
    
    if self.hero.get_life() > 0:
      print(f"\n{self.hero.get_name()} wins!")
    else:
      print(f"\n{self.enemy.get_name()} wins!")

game = Game()
game.start()