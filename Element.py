# -*- coding: utf-8 -*-
# Source emoji: https://unicode.org/emoji/charts/full-emoji-list.html
import random as rd

class Element: 
    def __init__(self, char_repr):
        '''Initializes the element with a unicode representation.'''
        self.__char_repr = char_repr

    def __repr__(self):
        '''Represents the element in the terminal.'''
        return self.__char_repr

    def __eq__(self, other):
        '''Returns if the element and another are equivalent.'''
        return type(self) == type(other) and self.__char_repr == other.__repr__() 




#############################
######  Turmite class  ######
#############################



class Turmite(Element):
    '''Defines the Turmite element, with its color.'''
    def __init__(self):
        Element.__init__(self, 'tur')
        self.__color = 'red'
        
    def get_color(self):
        '''Returns Turmite's color.'''
        return self.__color




####################################
######  Snake and food class  ######
####################################



WIDTH = 500
HEIGHT = 500
SPEED = 200
SPACE_SIZE = 20
BODY_SIZE = 2
SNAKE = "#00FF00"
FOOD = "#FFFFFF"
BACKGROUND = "#000000"

class Snake(Element):
    def __init__(self):
        '''Initializes the snake, base of the game, coordinates and size.'''
        Element.__init__(self, 'Snk')
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_SIZE):
            self.coordinates.append([0, 0])

    def create_snake(self, canvas):
        '''Defines the snake as itself, as moving squares in the canvas.'''
        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                fill=SNAKE, tag="snake")
            self.squares.append(square)

class Food(Element):
    def __init__(self):
        '''Function defining the random location of the food.'''
        Element.__init__(self, 'food')
        x = rd.randint(0, (WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = rd.randint(0, (HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]

    def create_food(self, canvas):
        '''Creates the food representation on the canvas.'''
        x, y = self.coordinates
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD, tag="food")



###########################
######  Human class  ######
###########################



# Redefinition of the Human class
class Human(Element):
    def __init__(self):
        Element.__init__(self, '\U0001F468')

        
        
################################        
######  Animal class def  ######
################################



class Animal(Element):
    def __init__(self, char_repr, life_max):
        '''Defines an Element as an Animal, with its unicode representation, age, gender, life, and direction.'''
        Element.__init__(self, char_repr)
        self.__age = 0
        self.__gender = rd.randint(0,1)
        self.__bar_life = [life_max, life_max]
        self.__current_direction = [rd.randint(-1,1),rd.randint(-1,1)] != [0,0]

    def get_age(self):
        '''Returns Animal's age.'''
        return self.__age

    def ageing(self):
        '''Adds one unit to the Animal's age.'''
        self.__age += 1

    def get_gender(self):
        '''Returns Animal's gender.'''
        return self.__gender

    def get_life_max(self):
        '''Returns the maximum health points the Animal has.'''
        return self.__bar_life[-1]

    def get_life(self):
        '''Returns Animal's current health points.'''
        return self.__bar_life[0]

    def is_alive(self):
        '''Returns True if the Animal has at least one HP, False otherwise.'''
        if self.__bar_life > 0:
            return True
        return False

    def is_dead(self):
        '''Returns True if the Animal has 0 HP or less, False otherwise.'''
        if self.__bar_life[0] == 0:
            return True
        return False

    def recovering_life(self, value):
        '''Restores Animal's life bar.'''
        if self.__bar_life[0] + value >= self.__bar_life[-1]:
            self.__bar_life[0] += (self.__bar_life[0] + value) - self.__bar_life[-1]
            
        else:
            self.__bar_life[0] += value

    def losing_life(self, value):
        '''Makes the Animal lose a certain amount of life.'''
        if self.__bar_life[0] - value <= 0:
            self.__bar_life[0] = 0
        else:
            self.__bar_life[0] -= value

    def get_current_direction(self):
        '''Returns Animal's current direction.'''
        return self.__current_direction

    def set_current_direction(self, line_direction, columns_direction):
        '''Sets the Animal's current direction as desired.'''
        self.__current_direction = [line_direction, columns_direction]



#######################
######  Animals  ######
#######################



class Dragon(Animal):
    def __init__(self):
        '''Defines the Dragon as an Animal.'''
        Animal.__init__(self, '\U0001F426', 50)

class Cow(Animal):
    def __init__(self):
        '''Defines the Cow as an Animal.'''
        Animal.__init__(self, '\U0001F42E', 1000)

class Lion(Animal):
    def __init__(self):
        '''Defines the Lion as an Animal.'''
        Animal.__init__(self, '\U0001F431', 30)
        
class Mouse(Animal):
    def __init__(self):
        '''Defines the Mouse as an Animal.'''
        Animal.__init__(self, '\U0001F42D', 10)



##################################
######  Resource class def  ######
##################################



class Ressource(Element):
    def __init__(self, char_repr, value):
        '''Used to define all resources findable on the Planet.'''
        Element.__init__(self,char_repr)
        self.__value = value

    def get_value(self):
        '''Returns Resource's value.'''
        return self.__value



#########################
######  Resources  ######
#########################



class Herb(Ressource):
    def __init__(self):
        '''Defines the Herb as a Resource.'''
        Ressource.__init__(self, 'He', 5)

class Water(Ressource):
    def __init__(self):
        '''Defines the Water as a Resource.'''
        Ressource.__init__(self, '\U0001F41F', 10)



######################
######  Others  ######
######################



class Ground(Element):
    def __init__(self):
        '''Defines the Ground as an Element.'''
        Element.__init__(self, '\u2B1C')
        
class Sand(Element):
    '''Defines the Sand element, with its color.'''
    def __init__(self):
        Element.__init__(self, '\u2B1C')
        self.__color = 'yellow'
                
    def get_color(self):
        '''Returns Sand's color.'''
        return self.__color