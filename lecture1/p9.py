d=int(input("Enter the number of days:"))
years=d//365
months=(d-years*365)//30
days=(d-years*365-months*30)
print("years:",years)
print("months:",months)
print("days:",days)