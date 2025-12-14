#24331A05E2
#CALCULATION OF compound INTEREST
principle=float(input("Enter principle amount: "))
rate=float(input("Enter rate of interest: "))
time=int(input("Enter time in years: "))
amount=principle*(1+rate/100)**time
compound_interest=amount-principle
print("Compound Interest is:", compound_interest)