#----------------------------------------------------------------------------------------------
# Name: Siddhi Agrawal
# Date: October 23, 2025
# Project Title: Daily Calorie Tracker
#----------------------------------------------------------------------------------------------
# Task 1 : Setup & Introduction
import datetime


print("-------------------------------------------")
print("   Welcome to the Daily Calorie Tracker!   ")
print("-------------------------------------------")
print("This tool helps you record what you eat and how many calories you take in.")
print("It also checks if you stay within your daily calorie limit.\n")

# Task 2 : Input & Data Collection
meals = []
calories = []
try:
    num_meals= int(input(" Enter the number of meals: "))
except ValueError:
    print(" Invalid Number! ")
    exit()

print("\n Meals & Calories")
for i in range(num_meals):
    meal_name = input(f"\nEnter the name of meal {i+1}: ")
    calorie_amount = int(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(calorie_amount)
print("\n All values are added !")    

# Task 3: Calorie Calculations
total_calories = sum(calories)
if num_meals > 0:
    average_calories= total_calories / len(calories)
else:
    average_calories = 0

daily_limit = int(input(" Whats your daily calorie limit:   "))

# Task 4: Exceed Limit Warning System
print("\n -------- Your Calorie Analysis -------- ")
print(f"Total Calories Consumed: {total_calories}")
print(f"Average Calories per Meal: {average_calories:.2f}")

if total_calories > daily_limit:
    print(" Warning: You have exceeded your daily calorie limit! ")
    print(f"{total_calories - daily_limit} calories over the limit!")
else:
    print(" Congratulations! you are within your daily calorie limit. ")
    calories_left = daily_limit - total_calories
    print(f"You can take {calories_left} calories more.")

# Task 5: Neatly Formatted Output
print(" \n ------------------------------------- ")
print(" Daily Calorie Summary")
print(" ------------------------------------- ")
print(f"{'Meal Name':<20}{'Calories':>10}")

for i in range(len(meals)):
    print(f"{meals[i]:<20}{calories[i]:>10.2f}")

print("--------------------------------------")
print(f"{'Total:':<20} {total_calories}")
print(f"{'Average:':<20} {average_calories:.2f}")
print("--------------------------------------")

# Task 6 : Save Session Log to File
save = input("Would you like to save this session to a file? (yes/no): ").lower()

if save == "yes":
    filename = "calorie_log.txt"
    with open(filename, "a") as file:
        file.write("\n-------------------------------------\n")
        file.write("        Daily Calorie Summary        \n")
        file.write("-------------------------------------\n")
        file.write(f"{'Meal Name':<20}{'Calories':>10}\n")
        file.write("-------------------------------------\n")
        for i in range(len(meals)):
            file.write(f"{meals[i]:<20}{calories[i]:>10.2f}\n")
        file.write("-------------------------------------\n")
        file.write(f"{'Total:':<20}{total_calories:>10.2f}\n")
        file.write(f"{'Average:':<20}{average_calories:>10.2f}\n")
        file.write("-------------------------------------\n")
        file.write(f"Session Date/Time: {datetime.datetime.now()}\n")
        file.write("-------------------------------------\n")
    print(f" Session saved successfully in '{filename}'.")
else:
    print("Session not saved.")



