from random import randint

#Fix the bug
# dice_images= ["1","2","3","4","5","6"]
# dice_num = randint(1,6)
# print(dice_images[dice_num])


dice_images= ["1","2","3","4","5","6"]
dice_num = randint(0,5)
print(dice_images[dice_num])
# We cannot use 6 because index out of range exception occurs
