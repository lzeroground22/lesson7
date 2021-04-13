def cooking(recipes):
    cookbook = {
        # Название блюда: [{
        #    'ingredient_name': 'имя',
        #    'quantity': число,
        #    'measure': 'единицы_измерения'
        # }]
        # пустая строка
    }
    with open(recipes) as f:
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
    return cookbook


def get_shop_list_by_dishes(dishes, person_count):
    cookbook2 = cooking('recipes.txt')
    for dish in cookbook2:
        name_dict = {
            # ingrid['ingredient_name'] : inn_dict
        }
        inn_dict = {
            # {'measure' : ingrid['measure'], 'quantity': int(ingrid['quantity']}
        }
        if dish in dishes:
            for ingrid in cookbook2[dish]:
                if ingrid['ingredient_name'] not in name_dict:
                    inn_dict = {'measure': ingrid['measure'], 'quantity': int(ingrid['quantity'])}

                else:
                    print('yes!', 'опять ', ingrid['ingredient_name'])
                    inn_dict = {'measure': ingrid['measure'], 'quantity': int(ingrid['quantity']) * person_count}
                name_dict[ingrid['ingredient_name']] = inn_dict
            # print(inn_dict)
            # print(name_dict)
    return name_dict


if __name__ == '__main__':
    # print(cooking('recipes.txt'))
    print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))
