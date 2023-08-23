# Calculating the BMI

print("BMI CALCULATOR")

print("Please Input Your Weight")
weight = input("Weight(lbs): ")

print("Please Input Your Height")
height = input("Height(in): ")

kilograms = float(weight) * 0.453592

height_meters = float(height) * 0.0254

height_squared = float(height_meters) ** 2

bmi = kilograms / height_squared
print(bmi)

if bmi <= 18.4:
    print("Underweight BMI")

elif bmi >= 18.5 and bmi <= 24.9:
    print("Healthy BMI")

elif bmi >= 25:
    print("Overweight BMI")



def gain_lose():

    # Gaining Weight Calorie Requirement
    question_gain_lose = input("Would You Like To Gain or Lose Weight: ")

    if question_gain_lose == "gain":
        pounds_gain = input("How Many Pounds (lbs) Would You Like To Gain Each Week: ")

        calories_gain = int(pounds_gain) * 500

        total_BMR_gain = calories_gain + float(BMR)

        print("In Order To Gain " + pounds_gain + " You Need To Consume " + str(total_BMR_gain) + " Calories Each Day")

        # Losing Weight Calorie Requirement

    elif question_gain_lose == "lose":
        pounds_lose = input("How Many Pounds (lbs) Would You Like To Lose Each Week: ")

        calories_lose = int(pounds_lose) * 500

        total_BMR_lose = float(BMR) - calories_lose
        if total_BMR_lose > 1000:
            print("In Order To Lose " + pounds_lose + "You Need To Consume " + str(total_BMR_lose) + "Calories Each Day")
        while total_BMR_lose < 1000:
            print("The Amount Of Calorie Intake Is Under 1000KCal, This Is Unhealthy For Your Body")

            print("Try Another Number")

            # Asking Question Again Until Correct Amount
            question_gain_lose == "lose"

            pounds_lose = input("How Many Pounds (lbs) Would You Like To Lose Each Week: ")

            calories_lose = int(pounds_lose) * 500

            total_BMR_lose = float(BMR) - calories_lose
            if total_BMR_lose > 1000:
                print("In Order To Lose " + pounds_lose + "lbs You Need To Consume " + str(total_BMR_lose) + " Calories Each Day")           
            
    else:
        print("Invalid Response")

# Figuring out calorie requirements
question_calorie_req = input("Would You Like To Figure Out on Daily How Much Calories You Should Consume?: ")

if question_calorie_req == "yes":


    gender = input(("Enter Your Gender: "))

    age = input("What is Your Age: ")

    # Normal Calorie Requirements

    if gender == "male" or "man" or "boy":
        print(age)
        BMR = 66 + (6.23 * int(weight)) + (12.7 * int(height)) - (6.8 * int(age))
        print("You Should Consume " + str(BMR) + " a Day")
        gain_lose()

    elif gender == "female" or "woman" or "girl":
        BMR = 655 + (4.35 * int(weight)) + (4.7 * int(height)) - (4.7 * int(age))
        print("You Should Consume " + str(BMR) + " a Day")
        gain_lose()
    else:
        print("Invalid Response")
elif question_calorie_req == "no":
    gain_lose()

else:
    print("Invalid Response")


# Calorie Requirement Based On Activity    
    





