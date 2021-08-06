"""
Here I am interested in string and list operators

"""
s = "routing_3_v6"

# I want to treat the number 3 as a block and v6 as a version

# First, split the string using underscore (_) as a delimiter
s1 = s.split("_")  # This produces a list from the above string
print(s1)

# Return the block and the version as in above

block_and_version = {'block': s1[1], 'version': s1[2]}
print("The block and version is:\n", block_and_version)

"""
List comprehension

Creating a list based on another list

I will use a list of heights and weights to populate a list of bmi. 

I will then define the bmi if they are underweight, overweight or normal wight. 
"""

students_first_name = ['Mesy', 'Rony', 'Van', 'Wein', 'Mari']
students_weight = [45, 54, 62, 51, 55]
students_height = [1.5, 1.4, 0.9, 1.16, 1.71]
bmi = [weight / (height ** 2) for weight, height in zip(students_weight, students_height)]
print(bmi)

"""
I will use these categories

def get_category(bmi):
    if bmi < 15:
        return 'very severely underweight'
    elif bmi <= 16 :
        return 'severely underweight'
    elif bmi <= 18.5:
        return 'underweight'
    elif bmi <= 25:
        return 'Normal(healthy weight)'
    elif bmi <= 30:
        return 'overweight'
    elif bmi <= 35:
        return 'moderately obese'
    elif bmi <= 40:
        return 'severely obese'
    else:
        return 'very severely obese'
"""

weight_condition = \
    [
        'very severely underweight' if body_mass_index < 15
        else 'severely underweight' if body_mass_index <= 16
        else 'underweight' if body_mass_index <= 18.5
        else 'Normal(healthy weight)' if body_mass_index <= 25
        else 'overweight' if body_mass_index <= 30
        else 'moderately obese' if body_mass_index <= 35
        else 'severely obese' if body_mass_index <= 40
        else 'very severely obese'
        for body_mass_index in bmi
    ]
print("The weight categories of each student is \n", weight_condition)

"""
Match each student with their weight categories

"""
weight_category = dict(zip(students_first_name, weight_condition))
print("These are the weights of the students \n", weight_category)

"""
Creation of dictionaries
"""

# Using braces
lunch = {'starch': 'ugali', 'vitamins': 'terere', 'proteins': 'nyam chom'}

# Using the keyword 'dict'
breko = dict(stimulant='chai', carbs='mahindi boil', protein='mayai')

# using a list of tuples
dinar = dict([('drink', 'red wine'), ('main dish', 'mashed potatoes'), ('stew', 'chicken soup')])

print({'Breakfast': breko, 'Lunch': lunch, 'Supper': dinar})

"""
Using Nested Loops to create a multiplication table

"""
print("\nThis is the multiplication table")
for number in range(11, 20):  # The range is from 11 to 19
    # The above is the outer loop
    for second_number in range(11, number+1):
        """
        # This is the inner loop (second number ranges from 11 to 19)
        # Lets format the string for the output
        """

        print("%dX%d=%-2d" % (second_number, number, second_number * number), end=" ")
    print()
