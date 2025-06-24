totalhour=10.50
rate=12.35
pay= totalhour*rate
print("total hour=%.2f. Hpurly rate=%.2f,salary=$%.2f"%(totalhour,rate,pay))
print(f"total hour={totalhour:.2f},hourly rate={rate:.2f},salary=${pay:.2f}")

totalhour2=float(int(input("total working hours:")))
rate2=float(int(input("hourly rate:")))
pay2=totalhour2*rate2
print(f"monthly salary is ${pay2:.2f}")

numS=2 #number of small room
numB=3 #number of big room 
sTables=int(input('Enter number of tables in the small room'))
bTables=int(input('Enter number of tables in the big room'))


totalSmall,totalBig=numS*sTables,numB*bTables
totalTable = totalSmall+totalBig
print(f"Total tables={totalTable}")
