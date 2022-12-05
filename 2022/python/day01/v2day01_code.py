import os
import sys

filename = "adventofcode2022_day01_input.txt"

fh = open(os.path.join(os.getcwd(), filename), "r")
calories_input = fh.read().splitlines()
fh.close()

elf_count = 0
elf = ()
elves = {}
calories_input.append("")
for calories in calories_input:
    if calories.isnumeric():
        icalories = int(calories)
        if elf:
            elf[0] = elf[0]+1
            elf[1] += icalories
            elf[2].append(icalories)
        else:
            elf = [1, icalories, [icalories]]
    else:
        elf_count += 1
        elves[elf_count] = elf
        # print("New elf %d = %s" % (elf_count, elf))
        elf = ()
        
list_of_calories  = [calories for (num, calories, items) in elves.values()]
list_of_calories.sort()

print("method 1: The most calories carried = %d" % max(calories for (num, calories, items) in elves.values()))
print("method 2: The most calories carried = %d" % list_of_calories[-1])

print("Sum of calories held by the 3 elves with the most calories (%s) = %s" % (list_of_calories[-3:], sum(list_of_calories[-3:])))

print("---------------------")

def readfile(filename, path=os.getcwd()):
    fh = open(os.path.join(path, filename), "r")
    file_data = fh.read()
    fh.close()    
    return file_data

class Food:
    def __init__(self, calories):
        self.calories = calories

class Elf:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_food(self, calories):
        self.inventory.append(Food(calories))
        
    def inventory_carried(self):
        return self.inventory
        
    def food_carried(self):
        return [i for i in self.inventory if i.__class__.__name__ == "Food"]       

    def calories_carried(self):
        # Calculate this for the moment, but considering storing a value for performance
        return sum([food.calories for food in self.food_carried()])

class Expedition:
    def __init__(self):
        self.elves = {}
        
    def add_elf(self, elf_name, elf):
        self.elves[elf_name] = elf

    def find_elf_with_x_most_calories(self, x):
        elves_calories_sorted = [elf.calories_carried() for elf in self.elves.values()]
        elves_calories_sorted.sort()
        elves_calories_sorted.reverse()
        
        return elves_calories_sorted[x-1]      

expedition = Expedition()

def read_elves_inventory(filename):
    calories_input = readfile(filename).splitlines()
    
    elf_name = 0
    elf = None
    calories_input.append("")
    for calories in calories_input:
        if calories.isnumeric():
            icalories = int(calories)
            if not elf:
                elf_name = elf_name + 1
                elf_name_str = str(elf_name)
                elf = Elf(elf_name_str)
            elf.add_food(icalories)
        else:
            expedition.add_elf(elf_name_str, elf)
            elf = None

    
read_elves_inventory("adventofcode2022_day01_input.txt")
print("method 3: The most calories carried = %d" % expedition.find_elf_with_x_most_calories(1))

list_of_calories = [expedition.find_elf_with_x_most_calories(1), expedition.find_elf_with_x_most_calories(2), expedition.find_elf_with_x_most_calories(3)]
print("method 2: Sum of calories held by the 3 elves with the most calories (%s) = %s" % (list_of_calories, sum(list_of_calories)))
    

