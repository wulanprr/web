def categorize_number(num):
    if isinstance(num, float):
        return "float"
    elif isinstance(num, int):
        return "int"
    else:
        return "string"

def map_to_units(num):
    return {
        'ratusan': num // 100,
        'puluhan': (num % 100) // 10,
        'satuan': num % 10
    }

# List containing a mix of numbers and strings
random_list = [3.1, 105, 'hello', 2.7, 5.5, 'python', 'world', 737, 'AI', 412]

# Separate float, int, and string values
float_values = list(filter(lambda x: isinstance(x, float), random_list))
int_values = list(filter(lambda x: isinstance(x, int), random_list))
string_values = list(filter(lambda x: isinstance(x, str), random_list))

# Convert int values to integers before categorizing
int_values = [int(x) for x in int_values]
categorized_int_values = list(map(categorize_number, int_values))
mapped_int_values = list(map(map_to_units, int_values))

# Output the results
print("Data float:", float_values)
print("Data int:", int_values)
print("Mapped int values:", mapped_int_values)
print("Data string:", string_values)