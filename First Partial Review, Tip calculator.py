#Tip Calculator
#Write a program that calculates the tip for a meal. The user should input the cost of the meal and the percentage of tip they want to give. The program should display the total amount to pay, the tip amount, and the original cost of the meal.
"""
1. Ask the user the cost of the meal
2. Make that an integer
3. Ask the user the the value of tip he wants to give
4. Make that into an integer
5. Make a function that take the value given in the cost meal and multiplies it by the value given in the percentage he want to give and then divides by 100 
6. Give the user the answer
"""


def Tip_Calculator():
  print("How much does the meal cost?")
  meal_cost = input()
  print("And how much percentaje do you want to give as a tip? (write it without the %)")
  tip = input()
  result = int(meal_cost) * int(tip) / 100
  print("The amount you give as a tip will be", int(result))


Tip_Calculator()
