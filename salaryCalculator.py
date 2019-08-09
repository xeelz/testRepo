



while True:

        weeklyHours = int(input("Enter Number:"))


        #weeklyHours = 40
        hourlyPayRate = 15

        weeklyPayPeriod = weeklyHours * hourlyPayRate
        biWeeklyPayPeriod = weeklyPayPeriod * 2
        monthlyPayPeriod = weeklyPayPeriod * 4
        yearlyPayPeriod = weeklyPayPeriod * 52
        extraTearDownPay = 300

        monthlyPayPeriodWITHbonus = (monthlyPayPeriod + (extraTearDownPay / 2))


        weeklyPayLabel = "Weekly:"
        biWeeklyLabel = "Paycheck:"
        monthlyPayLabel = "Monthly:"
        monthlyPlusBONUSPayLabel = "Monthly pay PLUS bonus:"
        yearlyPayLabel = "Yearly:"


        print(weeklyPayLabel + str(weeklyPayPeriod))
        print(biWeeklyLabel + str(biWeeklyPayPeriod))
        print(monthlyPayLabel + str(monthlyPayPeriod))
        print(yearlyPayLabel + str(yearlyPayPeriod))
