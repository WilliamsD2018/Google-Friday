##The meaning of this program is for a person to have a better understanding of himself healthwise.
##It will tell him factors about its body and things hr should work on.


height = float(input("Input your height in meters: "))
weight = float(input("Input your weight in kilogram: "))
BMI = round(weight / (height * height),2)
print("Your body mass index is: ", BMI)
## round(weight / (height * height),2))

if BMI >= 40:
	print("Your obesity is at extreme levels, you are morbidly obese,  you should eat healthier and see a doctor to help yourself. I would not expect you to live past 10 more years. Morbid obesity is ssociated with a multitude of health problems, many of wich significantly increse the risk of death")
elif BMI <= 39.9 and BMI > 35:
	print("Your obesity level is at a point were you will strugle to recover, you are severly obese, it would be hard for you to lose weight but you might make it. You should start an exercise program as soon as you can and find a doctor")
elif BMI <= 34.9 and BMI > 30:
	print("Start doing exsercise and get a better diet, it is terrible that you are not taking care of yourself, you should find a diet that suits you, of course it must be low in fat. See a nutriologist")
elif BMI <= 29.9 and BMI > 25:
	print("You are standing at an obese state. It is important for your health and people that love you that you begin to lose weight. It might not seem right now that you need to, but soon everything can change")
elif BMI <= 24.9 and BMI > 18.5:
	print("You are as healthy as you can get, great job maintaining your fat down. It must of been a hard task for some of you, but pretty easy for others. Keep doing exercise and a healthy diet.")
elif BMI <= 18.4:
	print("You are under weight, get some fat on your body. At this point you still have to mae sure you dont have to much sugar. Exercise is vital for weight gaining. See a doctor if you have had this problem for a long time.")
else: 
	print("Testing..................................................................")
	














	print("I       AM        SURE        SOMETHING        IS      WRONG")
