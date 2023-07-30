
# Help Suzuki count his vegetables
# link = https://www.codewars.com/kata/56ff1667cc08cacf4b00171b/solutions/python
'''
VEGETABLES = ("cabbage", "carrot", "celery", "cucumber", "mushroom", "onion", "pepper", "potato", "tofu", "turnip")


def count_vegetables(string):
    result = []
    vegetables = [i for i in string.split() if i in VEGETABLES]
    veg_set = set(vegetables)
    for veg in veg_set:
        result.append((vegetables.count(veg), veg))

    return sorted(result, reverse=True)
'''
