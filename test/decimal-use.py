from decimal import Decimal

a = 0.1
b = 0.2
c = a + b
print(c) # 0.30000000000000004

a = Decimal('0.1') 
b = Decimal('0.2')
c = a + b
print(c) # 0.3
