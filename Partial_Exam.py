#Partial exam

"""
vibraton machine cost 2000.00
10% discount
Robot name Juan
All of it will have to be asked before
"""
#Easy
def Juan():
  print("I am Juan, I will do the calculation of the cost of the machines")
  print("First, tell me the cost of the vibration machine [without money sign, $]")
  V_M_cost = input()
  print("tell me the discount you want tp know [Without percentage sign, %]")
  Discount = input()
  print("processing")
  V_W_Discount = float(V_M_cost) * float(Discount) / 100
  Result_1 = float(V_M_cost) - float(V_W_Discount)
  print("This is the money you should pay with the discount Applied $",Result_1)

Juan()
#Normal
def Juan_2():
  print("So now you want me to calculate 3 machines with and without the discount -_-")
  print("Well tell me the cost off the first one [remember no $ sign]")
  vibration_M2 = input()
  print("Tell me the second one [remmber no $ sign]")
  Temp_M = input()
  print("And the last one [remember no $ sign]")
  Thermal_M = input()
  print("And the last one tell me the discount it will be applied, it will be applied to all of them")
  discount2 = input()
  Total = float(vibration_M2) + float(Temp_M) + float(Thermal_M)
  Value_O_D2 = float(Total) * float(discount2) / 100
  Total_W_D = float(Total) - float(Value_O_D2)
  print("This is the total amount $",float(Total), "and this is the total amount with the discount $",Total_W_D)

Juan_2()

#Hard
"""
This one was not finished
"""
def Jaun_3():
  print("So now you want me to make the conversion to other currnecy, -_-, I should start to chraging you up my services -_-")
  print("Put the name of the currency we are currently are")
  Name_1 = input()
  print("Put the name of the second currency you want to know")
  Name_2 = input()
  print("How much currency ")
  
