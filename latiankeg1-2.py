def calculate_total_minutes(weeks, days, hours, minutes):
    total_minutes = ((weeks * 7 + days) * 24 + hours) * 60 + minutes
    return total_minutes

def create_minutes_adder(total_minutes):
    def add_minutes(extra_minutes=0):
        return total_minutes + extra_minutes

    return add_minutes

# Contoh penggunaan dengan data berupa daftar
data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit"]

# Process data and create a list of functions using explicit steps
time_data_list = [item.split() for item in data]
time_objects = [create_minutes_adder(calculate_total_minutes(int(item[0]), int(item[2]), int(item[4]), int(item[6]))) for item in time_data_list]
outputDataExplicit = [time_object() for time_object in time_objects]

print("Output Data = ", outputDataExplicit)

# Add the code below the existing code
extracted_integers = [[int(val) for val in item if val.isdigit()] for item in time_data_list]

print("\nInteger values extracted from data:")
for extracted_values in extracted_integers:
    print(extracted_values)