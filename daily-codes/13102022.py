def DTI(income, expenses):
    dti = round(expenses/income,2)
    if dti < 0.3:
        print(f'Your DTI is {dti} which is acceptable.')
    else:
        print(f'Your DTI is {dti} which is high.')
    return dti

DTI(income=1000, expenses=100)