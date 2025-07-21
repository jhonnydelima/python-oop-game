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

class Hero(Character):
  def __init__(self, name, life, level, skill) -> None:
    super().__init__(name, life, level)
    self.__skill = skill
  
  def get_skill(self):
    return self.__skill
  
  def show_info(self):
    return f"{super().show_info()}\nSkill: {self.get_skill()}\n"

class Enemy(Character):
  def __init__(self, name, life, level, type) -> None:
    super().__init__(name, life, level)
    self.__type = type
  
  def get_type(self):
    return self.__type
  
  def show_info(self):
    return f"{super().show_info()}\nType: {self.get_type()}\n"
