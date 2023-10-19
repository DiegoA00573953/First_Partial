https://replit.com/join/pyyqepokiw-diego-adieladie 

#Healthy Diet
"""
1.Ask the patient to insert the :
  Age: #Done
  Weight: (Kilogram) #done
  Phyasical activity: #done
  Height: #done
2.Complete the criteria one:
  if age <=  18, print "We recommend a high carbohydrate diet" #Done
  if age > 18 and age <= 35 print "We recomend a high protein and ower carbohydrate diet" #Done
  if age > 35 print "we recommend a low sugar diet" #Done
3. Complete cirteria two:
  if age >= 18 and age <= 35 and physically activity is sedentary or moderated, print "you need aerobic excersises" #Done
4. Create BMI: weight / Height ** 2   #Done
5. Complete criteria 3
  If BMI < 18 and physical activity = sedentary, print "You need to cosult a nutrionisst and increase your physical activity"   #Done
  If BMI >= 18 and BMI <= 25 physical activity moderated or active, print "Youare ina a good position" #done
  If BMI > 25 and physical activity is sedentary print "You need to consult a nutrionist, increase physical activity and reduce your weight"    #done
"""


age = float(input("Tell me the age of the patient"))
weight = float(input("Now the weight (in kilograms)"))
physical_activity = input("The physicall activity (sedentary, moderated, active)")
height = float(input("his height (in meters)"))
if age <=  18: 
  print ("We recommend a high carbohydrate diet")
if age > 18 and age <= 35:
  print("We recomend a high protein and ower carbohydrate diet")
if age > 35:
  print("we recommend a low sugar diet")


if age >= 18 and age <= 35 and physical_activity == "sedentary" or physical_activity == "moderated":
  print ("you need aerobic excersises")


BMI = weight / height ** 2
if BMI < 18 and physical_activity == "sedentary":
  print ("You need to cosult a nutrionisst and increase your physical activity")
if BMI >= 18 and BMI <= 25 and physical_activity == "moderated" or physical_activity == "active":
  print("You are in a good position")
if BMI > 25 and physical_activity == "sedentary":
  print("You need to consult a nutrionist, increase physical activity and reduce your weight")
