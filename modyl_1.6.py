my_dict={'Vera' : 1995, 'Vitalii' : 1994, 'Gosha' : 2007}
print(my_dict)
print(my_dict.get('Vera'))
print(my_dict.get('Polina'))
my_dict.update({'Vitek': 2020, 'Lyoha': 2021})
print(my_dict)
a= my_dict.pop('Gosha')
print(my_dict)
print(a)
print(my_dict)
#
my_set= {20, 3.14, 'Vera', 3, 20, 'Vera'}
print(my_set)
my_set.update([5, 'Fox'])
print(my_set)
my_set.discard(3.14)
print(my_set)