conversion_factor = 12
def showExpenses(loanPayment, insurance, gas, oil, tires, maintenance):
    monthTotal = totalMonthly(loanPayment, insurance, gas, oil, tires, maintenance)
    print(monthTotal, 'dollars per month.', totalAnnual(monthTotal), 'dollars per year.')
def totalMonthly(loanPayment, insurance, gas, oil, tires, maintenance): 
    return loanPayment + insurance + gas + oil + tires + maintenance
def totalAnnual(monthTotal):
    return monthTotal * conversion_factor
def main():
    loanPayment = float(input('Enter the amount spent on loan payment:'))
    insurance = float(input('Enter the amount spent on insurance:'))
    gas = float(input('Enter the amount spent on gas:'))
    oil = float(input('Enter the amount spent on oil:'))
    tires = float(input('Enter the amount spent on tires:'))
    maintenance = float(input('Enter the amount spent on maintenence'))
    showExpenses(loanPayment, insurance, gas, oil, tires, maintenance)
main()