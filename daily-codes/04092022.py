def tip(orders, tip=0.1):
    total = sum(orders)
    tip = total * tip
    return round(tip)

ordered = [10, 11, 8]

print('Tip amount comes to:',tip(orders=ordered))