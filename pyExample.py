
#print('Fuck the Lakers')

# l = ['a', 'b', 'c']
# l.pop(2)
#
# if 'c' in l:
# 	 print("heads")
#
# else:
# 	 print("tails")

hours = 48
rate = 15
breakdownPay = 300
payPeriod = 2
month = payPeriod * 2

biMonthlyPay = ((hours * rate) * payPeriod)

monthlyPay = biMonthlyPay * 2
monthlyPayPlusBreakdown = monthlyPay + breakdownPay
yearlyPay = monthlyPay * 12

# _biMonthlyPay = "Bi-Monthly Pay:"
# _MonthlyPay = "Monthly Pay:"
# _monthlyPayPlusBreakdown = "Monthly Pay w/ Breakdown:"
# _yearlyPay = "Yearly Pay:"

# biMonthlyPay_ = _biMonthlyPay + monthlyPay

print(biMonthlyPay)
print(monthlyPay)
print(monthlyPayPlusBreakdown)
print(yearlyPay)
