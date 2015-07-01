# -*- coding: utf-8 -*-
#Write a program to calculate the credit card balance after one year if a person only 
#pays the minimum monthly payment required by the credit card company each month.

#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal
#monthlyPaymentRate - minimum monthly payment rate as a decimal

#For each month:
#Compute the monthly payment, based on the previous month’s balance.
#Update the outstanding balance by removing the payment, then charging interest on the result.
#Output the month, the minimum monthly payment and the remaining balance.
#Keep track of the total amount of paid over all the past months so far.
#Print out the result statement with the total amount paid and the remaining balance.
#Use these ideas to guide the creation of your code.

def pay(balance, annualInterestRate, monthlyPaymentRate):
    """
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal
    monthlyPaymentRate - minimum monthly payment rate as a decimal
    """
    month = 1
    total = 0
    while month<13:
        monthrate=annualInterestRate/12
        monthlyPayment = balance * monthlyPaymentRate
        roundmonthlyPayment = round(monthlyPayment,2)
        balance = balance - monthlyPayment
        balance = balance + (balance*monthrate)
        roundbalance = round(balance,2)
        print 'Month: ' + str(month)
        print 'Minimum monthly payment: ' + str(roundmonthlyPayment)
        print 'Remaining balance: ' + str(roundbalance)
        total = total + monthlyPayment
        roundtotal = round(total,2)
        month = month + 1
    print 'Total paid: ' + str(roundtotal)
    print 'Remaining balance: ' + str(roundbalance)
        
#code to see what fixed monthly payment will pay off the balance in 12 months
#defined variables
#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal

#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)


balance = 4773
annualInterestRate = 0.2
	      
monthlyPayment = 10
monthrate=annualInterestRate/12
def pay(monthp,bal): 
    """
    given a monthly payment and start balance will calculate balance at the end of 12 months
    """
    month=1
    while month<13:
        bal = bal - monthp
        bal = bal + (bal*monthrate)
        month = month + 1   
    return bal
balance2=balance
while balance2 > 0:
    balance2 = pay(monthlyPayment,balance)
    monthlyPayment = monthlyPayment + 10
print "Lowest Payment: " + str(monthlyPayment-10)

#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly payment lower bound = Balance / 12
#Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

balance = 999999
annualInterestRate = 0.18

monthrate=annualInterestRate/12
def pay(monthp,bal): 
    """
    given a monthly payment and start balance will calculate balance at the end of 12 months
    """
    month=1
    while month<13:
        bal = bal - monthp
        bal = bal + (bal*monthrate)
        month = month + 1   
    return bal

monthlow = balance/12
monthhigh = (balance*(1+monthrate)*12)/12.0
ans = (monthlow + monthhigh)/2
ans2 = 0
#print "ans is " + str(ans) + " and ans2 is " + str(ans2) + " and monthlow is " + str(monthlow) + " and monthhigh is " + str(monthhigh) + " and balance is " + str(balance)
while abs(ans2-ans)>0.01:
    balance2=pay(ans,balance)
    if balance2>0:
        monthlow=ans
        ans2=ans
        ans=(monthlow + monthhigh)/2
#        print "ans is " + str(ans) + " and ans2 is " + str(ans2) + " and monthlow is " + str(monthlow) + " and monthhigh is " + str(monthhigh) + " and balance is " + str(balance2)
    elif balance2<0:
        monthhigh=ans
        ans2=ans
        ans=(monthlow + monthhigh)/2
#        print "ans is " + str(ans) + " and ans2 is " + str(ans2) + " and monthlow is " + str(monthlow) + " and monthhigh is " + str(monthhigh) + " and balance is " + str(balance2)
    else:
        break
    
ans=round(ans,2)
print "Lowest Payment: " + str(ans)