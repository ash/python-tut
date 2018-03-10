amount = int(input('Amount, €: '))
years = int(input('Years: '))
rate = float(input('Interest rate, %: '))

p = rate / 100.0
monthly = (amount * p * ((1 + p) ** years)) / (12 * (((1 + p) ** years) - 1))
print('Monthly payment = %.02f' % monthly)

total = monthly * 12 * years
print('Total amount to be paid %.02f ' % total)
