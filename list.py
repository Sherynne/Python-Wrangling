
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [i for i in numbers if i <= 0]


list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_numbers = [num for sublist in list_of_lists for num in sublist]


exponent_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
formatted_countries = [[c.upper(), c[:3].upper(), city.upper()] for sub in countries for c, city in sub]


country_dicts = [{'country': c.upper(), 'city': city.upper()} for sub in countries for c, city in sub]


names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{first} {last}" for sub in names for first, last in sub]

#  Output Results
print("Filtered:", negative_and_zero)
print("Flattened:", flattened_numbers)
print("Exponents Sample:", exponent_list[:3]) # Showing first 3 for brevity
print("Country List:", formatted_countries)
print("Country Dicts:", country_dicts)
print("Full Names:", full_names)