#beansandleaves.py

#Author: Alejandra Aguilar
#CIS129 Module 3: Coffee shop receipt program

#assigning values to constants of prices and tax rates

PRICE_PER_COFFEE = 5.00
PRICE_PER_MUFFIN = 4.00
PRICE_PER_TEA = 3.00
PRICE_PER_SCONE = 4.00
TAX_RATE = 0.06

#print greeting

print('***************************************\n\n\
Beans and Leaves Eatery\n')

# get number of items purchased

numCoffee = int(input('Number of coffees bought?\n'))

numMuffin = int(input('Number of muffins bought?\n'))

#updated to include tea and scones as items for purchase

numTea = int(input('Number of teas bought?\n'))

numScone = int(input('Number of scones bought?\n'))

# calculate total cost for each item type purchased

cost_Coffees = numCoffee * PRICE_PER_COFFEE

cost_Muffins = numMuffin * PRICE_PER_MUFFIN

cost_Teas = numTea * PRICE_PER_TEA

cost_Scones = numScone * PRICE_PER_SCONE

# calculate subtotal and tax

subTotal = cost_Coffees + cost_Muffins + cost_Teas + cost_Scones

tax = subTotal * TAX_RATE

#calculate total

total_Cost = subTotal + tax

#print receipt

print('\n***************************************\n\n\n\
***************************************\n\n\
Beans and Leaves Eatery Receipt\n')

#show number of items at cost for total per item

print(numCoffee, 'Coffee at $', PRICE_PER_COFFEE, 'each: $', cost_Coffees,'\n')

print(numMuffin, 'Muffins at $', PRICE_PER_MUFFIN, 'each: $', cost_Muffins,'\n')

print(numTea, 'Coffee at $', PRICE_PER_TEA, 'each: $', cost_Teas,'\n')

print(numScone, 'Coffee at $', PRICE_PER_SCONE, 'each: $', cost_Scones,'\n')

print('6% tax: $', tax,'\n')

print('---------\n')

print('Total: $', total_Cost,'\n')

print('***************************************\n\n\
Thank you for visiting Beans and Leaves. We hope you\'ll visit again!')
