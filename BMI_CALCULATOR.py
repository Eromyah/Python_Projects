print("This is a BMI Calculator")
print("For the most accurate results enter your height in meters, and your weight in kilograms")


while True:
     query = input('Do you need me to convert inches to meters and pounds into kilograms?')
     Fl = query[0].lower()
     if query == '' or not Fl in ['y','n']:
        print('Please answer with yes or no!')
     else:
        break
if Fl == 'y':
    print("How tall are you in inches?")
    height_inches = float(input())
    inches_converted = height_inches * 0.0254
    print(format(float(height_inches)), "inches", " = ", format(float(inches_converted)), "meters")
    print("How much do you weigh in pounds?")
    weight_pounds = float(input())
    pounds_converted = weight_pounds * .45
    print(format(float(weight_pounds)), " = ", format(float(pounds_converted)), "kilograms")
    

print("How tall are you?")
height = float(input())

print("How much do you weigh")
weight = float(input())

def bmi_calculator(height, weight):
    bmi = weight / (height ** 2)
    print("Here is your BMI:")
    print(bmi)
    if bmi > 25:
        return "You are at a healthy weight."
    else:
        return "You are overweight."
 

print(bmi_calculator(height, weight))