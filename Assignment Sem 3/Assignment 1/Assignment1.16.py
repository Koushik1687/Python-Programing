# WAP: Add two  dictionaries using update() function
def add_dict_update(d1, d2):
    d1.update(d2)
    return d1

d1 = {'name': "Koushik", 'roll': 30}
d2 = {'course': "MCA", 'year': 2025-26}

print(add_dict_update(d1, d2))
