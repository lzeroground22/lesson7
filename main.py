cookbook = {
    # Название блюда: [{
    #    'ingredient_name': 'имя',
    #    'quantity': число,
    #    'measure': 'единицы_измерения'
    # }]
    # пустая строка
}
#


# def get_shop_list_by_dishes(dishes, person_count):
#     for dish in cookbook:
#         if dish in dishes:
#             print(dish)
#             for ingrid in cookbook[dish]:
#                 # print(ingrid['ingredient_name'])
#                 ingr_dict = {'measure': ingrid['measure'], 'quantity': int(ingrid['quantity'])}
#             print(ingrid['ingredient_name'], ingr_dict)


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

# print(cookbook)

# get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
for dish in cookbook:
    name_list = list()
    # quant_list = list()
    measure_list = list()
    person = 2
    name_dict = {
        # ingrid['ingredient_name'] : inn_dict
    }
    inn_dict = {
        # {'measure' : ingrid['measure'], 'quantity': int(ingrid['quantity']}
    }
    if dish in ['Омлет', 'Фахитос']:
        for ingrid in cookbook[dish]:
            if ingrid['ingredient_name'] not in name_dict:
                inn_dict = {'measure': ingrid['measure'], 'quantity': int(ingrid['quantity'])}

            else:
                print('yes!', 'опять ', ingrid['ingredient_name'])
                inn_dict = {'measure': ingrid['measure'], 'quantity': int(ingrid['quantity']) * person}
            name_dict[ingrid['ingredient_name']] = inn_dict
        # print(inn_dict)
        print(name_dict)

        # name_dict[ingrid['ingredient_name']] = inn_dict
