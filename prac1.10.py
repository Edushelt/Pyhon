# Body Mass Index calculator for adult.
name = input("What is your name: ")
age = float(input("How old are you (yrs): "))
gender = input("Please enter 'M' for male and 'F' for female: ")
weight = float(input("Please enter your weight here (Kgs): "))
height = float(input("Please enter your height here (meters): "))

if gender == "M":
    gender_1 = "Male"
elif gender == "F":
    gender_1 = "Female"


if gender == "M":
    gender_2 = "Sir"
    print(f"Here you go {gender_2}:")
elif gender == "F":
    gender_2 = "Madam"
    print(f"Here you go {gender_2}:")
else:
    print("Warning! go back and enter 'M' for male and 'F' for female.\nUse CAPS for this is case sensitive")

bmi = weight / (height * height)


if bmi < 18.5:
    print(f"""
          Name: {name}
          Age: {age} years 0ld
          Gender: {gender_1}
          Weight: {weight}Kgs
          Height: {height}m
          BMI: {round(bmi,2)}
          Visual fat: Extremely Slim
          Dignosis: Your results show you are underweight. {gender_2}
          you need to eat properly
          """)
    
elif 18.5 <= bmi < 25.0:
    print(f"""
          Name: {name}
          Age: {age} years 0ld
          Gender: {gender_1}
          Weight: {weight}Kgs
          Height: {height}m
          BMI: {round(bmi,2)}
          Visual fat: Normal
          Dignosis: Your results show you
          have a healty weight. Cheer up! {gender_2}.
          """)

elif 25.0 <= bmi < 30.0:
    print(f"""
          Name: {name}
          Age: {age} years 0ld
          Gender: {gender_1}
          Weight: {weight}Kgs
          Height: {height}m
          BMI: {round(bmi,2)}
          Visual fat: Getting fat
          Dignosis: Your results show you are overweight. {gender_2},
          I recommend you to avoid sleeping
          right after eating.
          """)

elif 30.0 <= bmi < 40.0:
    print(f"""
          Name: {name}
          Age: {age} years 0ld
          Gender: {gender_1}
          Weight: {weight}Kgs
          Height: {height}m
          BMI: {round(bmi,2)}
          Visual fat: Fat
          Dignosis: Your results show you are obese. {gender_2}, I
          recommend execising the body regularly.
          """)

elif bmi >= 40:
    print(f"""
          Name: {name}
          Age: {age} years 0ld
          Gender: {gender_1}
          Weight: {weight}Kgs
          Height: {height}m
          BMI: {round(bmi,2)}
          Visual fat: Too much fat
          Dignosis: Your results show you are at the critical 
          stage of obesity. Which is dangerous to your
          health. {gender_2}, I suggest you see a dietician
          and gym coach for advice.
          """)
