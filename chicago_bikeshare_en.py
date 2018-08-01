
# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    data_list = [{k: v for k, v in row.items()}
                    for row in csv.DictReader(file_read, skipinitialspace=True)]
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))
print(data_list[0]['Gender'])
# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])

print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
# Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")
for i in range(20):
    print("Row {} : {}".format(i+1, data_list[i]))

# We can access the features through name
# E.g. sample['Gender'] to print gender

input("Press Enter to continue...")
# TASK 2
# Print the `gender` of the first 20 rows
print("\nTASK 2: Printing the genders of the first 20 samples")
for i in range(20):
    print("Row {} : {}".format(i+1, data_list[i]['Gender']))

# Cool! We can get the rows(samples) iterating with a for and the columns(features) by name.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")
# TASK 3
# Create a function to add the columns(features) of a list in another list in the same order
def column_to_list(data, index):
    """
    Creates a list with all values from a collumn
    Args:
        data: The whole csv file with the data.
        index: The collumn index in the csv.
    Returns:
        List of all values in a collumn
    """
    key_name = list(data[0].keys())[index]
    column_list = [line[key_name] for line in data]
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    return column_list


# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# Count each gender. You should not use a function to do that.
gender_list = column_to_list(data_list, -2)
male = sum(1 for gender in gender_list if gender == 'Male')
female = sum(1 for gender in gender_list if gender == 'Female')


# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
def count_gender(data_list):
    """
    Counts how many of each gender exists in the csv
    Args:
        data_list: A list with all gender values.
    Returns:
        The count of male and female
    """
    male = sum(1 for row in data_list if row['Gender'] == 'Male')
    female = sum(1 for row in data_list if row['Gender'] == 'Female')
    return [male, female]


print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.
def most_popular_gender(data_list):
    """
    Retuns which gender is most popular in the data_list
    Args:
        data_list: A list with all gender values.
    Returns:
        A string with the most popular gender(Male or Female); if they are equals returns Equal
    """
    male_count, female_count = count_gender(data_list)
    
    if (male_count == female_count):
        return "Equal"

    return  "Male" if male_count > female_count else "Female"


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 7
# Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!")
def count_usertype(data_list):
    """
    Counts how many of each user type exists in the csv
    Args:
        data_list: A list with all user type values.
    Returns:
        A list with the count of each user type
    """
    customer = sum(1 for row in data_list if row['User Type'] == 'Customer')
    subscriber = sum(1 for row in data_list if row['User Type'] == 'Subscriber')
    dependent = sum(1 for row in data_list if row['User Type'] == 'Dependent')
    return [customer, subscriber, dependent]

types = ["Customer", "Subscriber", 'Dependent']

quantity = count_usertype(data_list)
y_pos = list(range(len(types)))

plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('User Type')
plt.xticks(y_pos, types)
plt.title('Quantity by User Type')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 8
# Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Some rows do not have information about gender."
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
trip_duration_list = sorted([int(i) for i in column_to_list(data_list, 2)])
trip_list_len = len(trip_duration_list)

min_trip = trip_duration_list[0]
max_trip = trip_duration_list[-1]
mean_trip = sum(trip_duration_list) / trip_list_len
if trip_list_len  % 2 == 0:
    median_trip = sum(trip_duration_list[trip_list_len//2-1:trip_list_len//2+1]) / 2
else:
    median_trip = trip_duration_list[trip_list_len//2]


print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# Check types how many start_stations do we have using set()
user_types = set(column_to_list(data_list, 3))

print("\nTASK 10: Printing start stations:")
print(len(user_types))
print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# # def new_function(param1: int, param2: str) -> list:
#        """
#        Example function with annotations.
#        Args:
#            param1: The first parameter.
#            param2: The second parameter.
#        Returns:
#            List of X values

#        """

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "yes"

def count_items(column_list):
    """
    Counts a the unique values from a column and how many itens it have
    Args:
        column_list: A list with all values from a column.
    Returns:
        Returns the unique values from a column and how many itens it have
    """
    item_types = set(column_list)
    count_items = list(1 for i in column_list)
    return item_types, count_items


if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------