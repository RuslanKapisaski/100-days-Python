# import random
# import maths
#
# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(a=1, b=3)
#         new_item = maths.sum(new_item, item)
#     b_list.append(new_item)
#     print(b_list)
#
# mutate([1, 2, 3, 5, 8, 13])

# Fix the bug
import random

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in range(len(a_list)):
        new_item = item * 2
        new_item += random.randint(a=1, b=3)
        new_item = new_item + item
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])