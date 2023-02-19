"""
Challenge 1 - How much does a booklet weigh?
90 – 120 GSM paper: The average weight of regular office paper or copy paper. 
130 – 250 GSM paper: The weight most commonly used for promotional posters. 

Your program should accept inputs from the user and output the weight of their booklet. 
"""
# - Version 2 - 
def GetInput(prompt, MinParam = 0, MaxParam = 100000):
  """
  Asks and validates an integer input.
  :param prompt: what is displayed to to ask for the integer
  :param LowParam: the minimum value accepted
  :param MaxParam: the maximum value accepeted
  :return: the validated integer input by the user
  """
  
  # Asks for integer and returns the value until validates
  while True:
    try:
      answer = int(input(prompt))
      if answer > MinParam and answer < MaxParam:
        return answer
      else:
        print("Please input a integer between {} and {}.".format(MinParam, MaxParam))
    except:
      print("Please print a valid integer")
      
# Input the measurements
print("Challenge 1 - How much does a booklet weigh?\n")
weight = GetInput("Weight (gsm): ", 90, 250)
width = GetInput("Width (mm): ", 0, 1000)
height = GetInput("Height (mm): ", 0, 1500)
pages = GetInput("Total Pages: ")

# Calculates the weight of the booklet
result = round((weight * width * height * round(pages / 2)) / 1000000, 2)

# Display the result on the screen
print("Total:", result, "grams")


# - Version 1 -
print("Challenge 1 - How much does a booklet weigh?")
weight = float(input("Weight (Grams per Square Meter): "))
width = float(input("Width (Metres): "))
height = float(input("Height (Metres): "))
pages = int(input("Total Pages: "))
additional = float(input("Additional Weight such as the cover (Grams): "))

result = round(weight * width * height * round(pages / 2) + additional, 2)
print(result, "grams")
