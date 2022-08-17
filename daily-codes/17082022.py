import numpy as np

income = float(input("What is your income (£)? "))
expenses = float(input("What are your expenses (£)? "))
rent = float(input("What is your monthly rental amount (£)? "))

def dti(income, expenses):
    dti = round(expenses / income, 2)
    return dti

def mortgage(i, n, p):
    mortgage = p * (1 + i)**n
    return round(mortgage)

print('--------------------------------------------------------------------------')
print(f"Your debt to income ratio is: {dti(income=income, expenses=expenses)}")
print('--------------------------------------------------------------------------')
print(f"You can get a mortgage with interest 2% over 30 years for: £{mortgage(i=0.02, n=360, p=rent)}")
print('--------------------------------------------------------------------------')