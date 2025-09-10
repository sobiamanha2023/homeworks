weight = float(input("Enter the weight in kg: "))
height = float(input("Enter the weight in meter: "))

bmi = weight/height ** 2

print(f"Your bmi is: {bmi:0.2f}")

if bmi <18.5:
    print("You are underweight")

elif 18.5 <= bmi <=24.9:
    print("You are normal in weight")

elif 25<= bmi <=29.9:
    print("You are overwight")

elif 30<= bmi <=34.9:
    print("You are obese")

else:
    print("You are extreamly obese")