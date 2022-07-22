import os

FILE_DIR = 'files'
FILE_NAME = 'recipes.txt'
absolute_file_path = os.path.join(os.getcwd(), FILE_DIR, FILE_NAME)
CHUNK_SIZE = 8192


# Задачи № 1 - 2
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
            return Ingredient(self.ingredient_name, self.quantity * other, self.measure)
        return self

    def __str__(self):
        return f'{self.ingredient_name} | {str(round(self.quantity, 2))} | {self.measure}'

    # def __hash__(self):
    #     return hash(str(self))

    def __eq__(self, other):
        if isinstance(other, Ingredient):
            return self.ingredient_name == other.ingredient_name
        return False


def get_shop_list_by_dishes(dishes, person_count=1):
    def shop_list_to_dict(ingred_list):
        d = {ingred.ingredient_name: {'measure': ingred.measure, 'quantity': ingred.quantity} for ingred in ingred_list}
        return d

    shop_list = []
    for dish in dishes:
        ingredient_list = cook_book.get(dish)
        if ingredient_list:
            for ingredient_item in ingredient_list:
                if ingredient_item in shop_list:
                    shop_list[shop_list.index(ingredient_item)] += ingredient_item * person_count
                else:
                    shop_list.append(ingredient_item * person_count)

    return shop_list_to_dict(shop_list)


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
# print(cook_book['Омлет'][2] == cook_book['Фахитос'][4])

# print(cook_book['Омлет'][2] + cook_book['Фахитос'][4])
# print(cook_book['Омлет'][2] * 4)

shopping_list = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)
print(shopping_list)

for k, v in shopping_list.items():
    print(k, ': ', v)

######################################################################################################################

# Задача № 3

ABS_FILES_DIR_PATH = os.path.join(os.getcwd(), FILE_DIR)

files = [f for f in os.listdir(ABS_FILES_DIR_PATH)
         if os.path.isfile(os.path.join(ABS_FILES_DIR_PATH, f))]
# text_files = [os.path.join(ABS_FILES_DIR, f) for f in files if f[-4:] == '.txt']
text_files_names = [f for f in files if f[-4:] == '.txt']
# print(text_files_names)


def define_number_of_rows_in_text_files(file_list, chunk_size=8192):
    res = []
    for f in file_list:
        with open(os.path.join(ABS_FILES_DIR_PATH, f), encoding='utf-8') as file_ob:
            s = sum(chunk_.count('\n') for chunk_ in iter(lambda: file_ob.read(chunk_size), ''))
        res.append(s)
    return res


number_of_rows = define_number_of_rows_in_text_files(text_files_names)
# print(number_of_rows)
# print(list(zip(text_files_names, number_of_rows)))
print(sorted(zip(text_files_names, number_of_rows), key=lambda itm: itm[1]))

with open(os.path.join(ABS_FILES_DIR_PATH, 'result.txt'), 'a', encoding='utf-8') as target_file:
    for f, rows_count in sorted(zip(text_files_names, number_of_rows), key=lambda itm: itm[1]):
        with open(os.path.join(ABS_FILES_DIR_PATH, f), encoding='utf-8') as file_obj:
            target_file.write(f + '\n')
            target_file.write(str(rows_count) + '\n')
            # target_file.write(file_obj.read() + '\n')
            for chunk in iter(lambda: file_obj.read(CHUNK_SIZE), ''):
                target_file.write(chunk)
            target_file.write('\n')
