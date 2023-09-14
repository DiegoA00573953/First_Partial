  #First Partial Review, Temperature Converter.

#Temperature Converter:
#Create a program that converts a temperature in degrees Celsius to Fahrenheit. The user should input the temperature in Celsius, and the program will display the equivalent temperature in Fahrenheit and Kelvin.
"""1. Ask the user the temperature in Celsius 
   2. Escpecify that I will give it in Fahrenheit and Kelvin
   3. Take all the values as decimal
   4. Do two separate functions, one for Fahrenheit, and the other for Kelvin
   5. First Fahrenheit: The value of celsius multiplied by 9/5 and then add 32
   6. Tell him the answer
   7. Second Kelvin: the value of celsius add 273.15
   8. Tell him the answer"""

def Tempereture_Converter():
  print ("Tell me the temperature in Celsius degrees so I can tell you the equivalent in Kelvin and Fahrenheit")
  Celsius = input()
  result_F = float(Celsius) * 9/5 + 32
  print("This is the answer in fahrenheit  ",float(result_F))
  result_K = float(Celsius) + 273.15
  print("This is the result in Kelvin",float(result_K))
Tempereture_Converter()
