
balance = int(input("What is your balance:"))

if (balance >= 0):
 if (balance > 10):
  print("Positive significant")
 else:
   print ("Positive insignificant")
else:
  if (balance < -10):
    print ("Negative significant")
  else:
    print ("Negative insignificant")