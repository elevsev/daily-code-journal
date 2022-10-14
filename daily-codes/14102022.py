def ECL(PD, EAD, LGD):
    ECL = round(PD * EAD * LGD,2)
    return ECL

print(f"ECL = {ECL(PD=0.03, EAD=100, LGD=0.1)}")