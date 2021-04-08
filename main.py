from pprint import pprint

cookbook = {
    # Название блюда: [кол-во ингридиентов в блюде{
    #    'ingredient_name': 'имя',
    #    'quantity': число,
    #    'measure': 'единицы_измерения'
    # }]
    # пустая строка
}


def blanker():
    pass


with open('recipes.txt') as f:
    dish_name = f.readline().strip()
    count = int(f.readline())
    ing_list = list()
    for some in range(count):
        ingr = f.readline().strip()
        splited = ingr.split('|')
        # print(splited)
        ing_dict = {'ingredient_name': splited[0], 'quantity': splited[1], 'measure': splited[2]}
        ing_list.append(ing_dict)
    f.readline()
    cookbook[dish_name] = ing_list

# print(type(dish_name))
# print(type(cookbook))
# print(ing_dict)
print(cookbook)
