import statistics 
def calculate_bmi():
 height = float(input(("Enter your height in meters: ")))
 weight = float(input(("Enter your weight in kg: ")))
 bmi = (weight/(height * height))
 print("BMI = " + str(round(bmi, 2)))
 if (bmi <= 18):
  print("Underweight")
  return -1
 elif (bmi >= 25):
  print("Overweight")
  return 1
 else:
  print("Healthy Weight")
  return 0
calculate_bmi()


#def display_main_menu():
 #print("Enter some numbers seperated by commas")
#display_main_menu()

#def user_input():
 #number = input()
 #numbersplit = number.split(",")
 #list = [numbersplit]
 #print (list)
 #return list
#number_list = user_input()


