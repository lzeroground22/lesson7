cookbook = {
    # Название блюда: [{
    #    'ingredient_name': 'имя',
    #    'quantity': число,
    #    'measure': 'единицы_измерения'
    # }]
    # пустая строка
}

with open('recipes.txt') as f:
    for lin in f:
        dish_name = lin.strip()
        count = int(f.readline())
        ing_list = list()
        for some in range(count):
            ingr = f.readline().strip()
            splited = ingr.split('|')
            ing_dict = {'ingredient_name': splited[0], 'quantity': splited[1], 'measure': splited[2]}
            ing_list.append(ing_dict)
        f.readline()
cookbook[dish_name] = ing_list
print(cookbook)
