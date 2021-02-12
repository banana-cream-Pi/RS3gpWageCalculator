import time as t
import math
wage = input("Input hourly wage:")
wage = wage.strip('$')
wage = float(wage)
bondGP = 26653078#change this to market price of bond, I don't feel like quering the server
wagePs = wage/60/60
totalMoney = 0
bond = 6.99
print("GP per hour",round(wage/bond*bondGP))
while True: 
    t.sleep(1)
    lastMoney = round(totalMoney,2)
    totalMoney+=wagePs
    bonds = round(totalMoney,2) / bond
    keys = bonds * 15
    if lastMoney == round(totalMoney,2):
        continue
    else:
        print("+=====================+\nUSD:","{:.2f}".format(totalMoney),"\nGP:",math.floor(bondGP*bonds),"\nKeys:",math.floor(keys),"\nBonds:",math.floor(bonds),"\nRuneCoins:",math.floor(bonds*195),"\nDays of Membership:",math.floor(bonds*14),"\n+=====================+")
    
    
