import os

FILE_DIR = 'files'
FILE_NAME = 'recipes.txt'

file_path = os.path.join(os.getcwd(), FILE_DIR, FILE_NAME)

cook_book = {}
with open(file_path, encoding='utf-8') as file:
    for line in file:
        filtered_line = line.strip(' \n')
        if filtered_line:
            dish = filtered_line
            ingredients = []
            for _ in range(int(file.readline().strip(' \n'))):
                ingredient = file.readline().strip(' \n').split(' | ')
                ingredient_dict = {'ingredient_name': ingredient[0],
                                   'quantity': float(ingredient[1]),
                                   'measure': ingredient[2]}
                ingredients.append(ingredient_dict)
            cook_book[dish] = ingredients

print(cook_book)
