from pprint import pprint

cook_book = {}
with open('recipies.txt', 'r', encoding='utf-8') as file:
    while True:
        key = (file.readline().strip())
        if not key:
            break
        cook_book[key] = []
        number_of_ingridients = int(file.readline().strip())
        for line in range(number_of_ingridients):
            ingridient = file.readline().strip().split('|')
            cook_book[key] += [{'ingredient_name': ingridient[0].strip(),'quantity': ingridient[1].strip(), 'measure':
            ingridient[2].strip()}]
        file.readline()


shop_list = {}
def get_shop_list_by_dishes(dishes: list, person_count: int):
    '''
    функция, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить

    '''
    for dish in dishes:
        if dish not in cook_book.keys():
            return (f'Блюдо {dish} отсутствует')
        else:
            print(cook_book[dish])
            for ingredient in cook_book[dish]:
                shop_list[ingredient['ingredient_name']] = {'quantity': 0, 'measure': ingredient['measure']}
                shop_list[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity'])* person_count

    return shop_list


pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))

