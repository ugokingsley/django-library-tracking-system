import random
# rand_list =

import random 

numbers = [random.randint(1,20) for _ in range(10)]
# list_comprehension_below_10 =
below_10_list_com = [num for num in numbers if num < 10]
# list_comprehension_below_10 =
below_10_filter = list(filter(lambda num: num < 10, numbers))
