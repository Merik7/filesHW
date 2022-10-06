from pprint import pprint


COOK_BOOK = {}
with open('recipes.txt', 'rt', encoding='utf8') as file:
    for l in file:
        dish_name = l.strip()
        dishes = []
        ingredient_count = int(file.readline())
        for _ in range(ingredient_count):
            dish_ingredients = file.readline()
            ingredient_name, quantity, measure = dish_ingredients.strip().split(' | ')
            dishes.append({'ingredient_name': ingredient_name,
                                      'quantity': quantity,
                                      'measure': measure})
        blank_line = file.readline()
        COOK_BOOK[dish_name] = dishes
print(COOK_BOOK)


def get_shop_list_by_dishes(dishes, person_count):
    final_shop_list = {}
    for dish, ings in COOK_BOOK.items():
        if dish in dishes:
            for ing in ings:
                final_shop_list[ing['ingredient_name']] = {'measure': ing['measure'],
                                                           'quantity': int(ing['quantity']) * person_count}
    return final_shop_list
print()


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))