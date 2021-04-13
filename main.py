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
# print()
# for dish in cookbook:
#     # print(dish, cookbook[dish])
#     for ingrid in cookbook[dish]:
#         print(ingrid['ingredient_name'])

# get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)

for dish in cookbook:
    if dish in ['Омлет', 'Фахитос']:
        # print('dish:', dish)
        # print('cookbook[dish]:', cookbook[dish])
        name_dict = {}
        name_set = set()
        name_list = list()
        quant_list = list()
        measure_list = list()
        for ingrid in cookbook[dish]:
            if ingrid['ingredient_name'] in name_set:
                print('yes!')
            else:
                name_list.append(ingrid['ingredient_name'])
                quant_list.append(int(ingrid['quantity']))
                # print(name_list, quant_list)
                # inn = set(name_list)
            # print("ingrid['ingredient_name']:", name_list, quant_list)


        print('set', name_set)


# words = ['hello', 'daddy', 'hello', 'mum']
# a = set(words)
#
# words2 = ['hello', 'hello', 'bye', 'mum']
# b = set(words2)
# if 'mum' in b:
#     print('yes')
# else:
#     b.update('mum')
# print(b)