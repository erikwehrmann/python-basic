bill = float(input("Bill total: "))
tip = bill * (float(input("Tip percentage: ")) / 100)
numOfPeople = float(input("Number of people: "))
print("Each person should pay:")
print((bill + tip) / numOfPeople)