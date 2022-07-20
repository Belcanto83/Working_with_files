import os

FILE_DIR = 'files'
FILE_NAME = 'recipes.txt'
absolute_file_path = os.path.join(os.getcwd(), FILE_DIR, FILE_NAME)


class Ingredient(dict):
    def __init__(self, ingredient_name: str, quantity: float, measure: str):
        self.ingredient_name = ingredient_name
        self.quantity = quantity
        self.measure = measure
        super().__init__({
            'ingredient_name': self.ingredient_name,
            'quantity': self.quantity,
            'measure': self.measure
        })

    def __add__(self, other):
        if isinstance(other, Ingredient) and self.ingredient_name == other.ingredient_name and \
                self.measure == other.measure:
            return Ingredient(self.ingredient_name, self.quantity + other.quantity, self.measure)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Ingredient(self.ingredient_name, other * self.quantity, self.measure)
        return self


def get_shop_list_by_dishes(dishes, person_count=1):
    uniq_ingredients = set()
    for dish in dishes:
        uniq_ingredients.update(cook_book[dish])
    return uniq_ingredients


cook_book = {}
with open(absolute_file_path, encoding='utf-8') as file:
    for line in file:
        filtered_line = line.strip(' \n')
        if filtered_line:
            item = filtered_line
            ingredients = []
            for _ in range(int(file.readline().strip(' \n'))):
                ingredient = file.readline().strip(' \n').split(' | ')
                # ingredient_dict = {'ingredient_name': ingredient[0],
                #                    'quantity': float(ingredient[1]),
                #                    'measure': ingredient[2]}
                ingredient_dict = Ingredient(ingredient[0], float(ingredient[1]), ingredient[2])
                ingredients.append(ingredient_dict)
            cook_book[item] = ingredients

print(cook_book)
# print(type(cook_book['Омлет'][2]))
# print(type(cook_book['Омлет'][2] + cook_book['Фахитос'][4]))
# print(type(cook_book['Омлет'][2] * 3))
#
# print(cook_book['Омлет'][2] + cook_book['Фахитос'][4])
# print(cook_book['Омлет'][2] * 4)

shop_list = get_shop_list_by_dishes(['Омлет', 'Фахитос'])
print(shop_list)
print(type(shop_list))

for item in shop_list:
    print(item)
    print(type(item))
