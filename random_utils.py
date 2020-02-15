from enum import Enum
import random

def get_random_bool():
    return bool(random.getrandbits(1))

def get_random_enum_value(_enum: Enum):
    return random.choice(list(_enum))

def get_random_list_value(_list: list):
    return random.choice(_list)

def bag_pull(items: [list, Enum]):
    is_list = type(items) == list
    last_index = None
    while True:
        # get a new order for the items in the bag
        order = list(range(len(items)))
        random.shuffle(order)
        # prevent duplicates at shuffles
        if order[0] == last_index:
            order.append(order.pop())
        # step through order
        for index in order:
            if is_list:
                yield items[index]
            else:
                yield items(index)
        last_index = order[-1]
            