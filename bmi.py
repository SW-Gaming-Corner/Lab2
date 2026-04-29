def calculate_bmi(height, weight):
 print("Height = " + str(height))
 print("Weight = " + str(weight))
 bmi = (weight/(height * height))
 print("BMI = " + str(bmi))
 if (bmi <= 18):
  print("Underweight")
 elif (bmi >= 25):
  print("Overweight")
 else:
  print("Healthy Weight")
calculate_bmi(height = 1.65, weight= 52)

