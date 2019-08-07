


weeklyHours = 48
hourlyPayRate = 15

weeklyPayPeriod = weeklyHours * hourlyPayRate
biWeeklyPayPeriod = weeklyPayPeriod * 2
monthlyPayPeriod = weeklyPayPeriod* 4

extraTearDownPay = 300


monthlyPayPeriodWITHbonus = (monthlyPayPeriod + (extraTearDownPay / 2))

your = "Your"
weeklyPayLabel = "weekly pay is:"
biWeeklyLabel = "paycheck every 2 weeks is:"
monthlyPayLabel = "monthly pay is:"
monthlyPlusBONUSPayLabel = "monthly pay PLUS bonus is:"


print(your) + " " + (weeklyPayLabel)
print(weeklyPayPeriod)

print(your) + " " + (biWeeklyLabel)
print(biWeeklyPayPeriod)

print(your) + " " + (monthlyPayLabel)
print(monthlyPayPeriod)

print(your) + " " + (monthlyPlusBONUSPayLabel)
print(monthlyPayPeriodWITHbonus)
