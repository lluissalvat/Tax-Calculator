income = input('Annual Gross Pay: £')
spend = input('Monthly Expenses: £')

yearly_income = int(income)
expenses = int(spend) * 12

ug_thres = 27295 # Plan2: 9%

natins_thres1 = 9564 #12%
natins_thres2 = 50268 #2%

inctax_thres1 = 12570 #20%
inctax_thres2 = 50270 #40%
inctax_thres3 = 150000 #45%
nopersallow_thres = 100000

def studentLoanPayment (yearly_income):
  if yearly_income < ug_thres:
    student_loan_payment = 0
  else:
    student_loan_payment = (yearly_income - ug_thres) * 0.09
  return student_loan_payment

def incomeTaxPayment (yearly_income):
  if yearly_income < inctax_thres1: #Less than 12570
    income_tax_payment = 0
  elif yearly_income >= inctax_thres1 and yearly_income < inctax_thres2: #12570-50270
    income_tax_payment = (yearly_income - inctax_thres1) * 0.2
  elif yearly_income >= inctax_thres2 and yearly_income < nopersallow_thres: #50270-100000
    income_tax_payment = (inctax_thres2 - inctax_thres1) * 0.2 + (yearly_income - inctax_thres2) * 0.4
  elif yearly_income >= nopersallow_thres and yearly_income < nopersallow_thres+2*inctax_thres1: #100000-125570
    income_tax_payment = (inctax_thres2 - inctax_thres1 - (yearly_income - nopersallow_thres) / 2) * 0.2 + (yearly_income - inctax_thres2) * 0.4
  elif yearly_income >= nopersallow_thres+2*inctax_thres1 and yearly_income < inctax_thres3: #125140-150000
    income_tax_payment = inctax_thres2 * 0.2 + (yearly_income - inctax_thres2) * 0.4
  elif yearly_income >= inctax_thres3 : #More than 150000
    income_tax_payment = inctax_thres2 * 0.2 + (inctax_thres3 - inctax_thres2) * 0.4 + (yearly_income - inctax_thres3) * 0.45
  return income_tax_payment

def nationalInsurancePayment (yearly_income):
  if yearly_income < natins_thres1:
    nat_ins_payment = 0
  elif yearly_income >= natins_thres1 and yearly_income < natins_thres2:
    nat_ins_payment = (yearly_income - natins_thres1) * 0.12
  elif yearly_income >= natins_thres2:
    nat_ins_payment = (natins_thres2 - natins_thres1) * 0.12 + (yearly_income - natins_thres2) * 0.02
  return nat_ins_payment

def totalTaxPayment (yearly_income):
  total_tax_payment = incomeTaxPayment(yearly_income) + nationalInsurancePayment(yearly_income) + studentLoanPayment(yearly_income)
  return total_tax_payment

def effectiveTaxRate (yearly_income):
  tax_rate = totalTaxPayment(yearly_income) / yearly_income *100
  return tax_rate

def netIncome (yearly_income):
  net_income = yearly_income - totalTaxPayment(yearly_income)
  return net_income

def annualSavings (yearly_income):
  annual_savings = netIncome(yearly_income) - expenses
  return annual_savings

def monthlySavings (yearly_income):
  monthly_savings = annualSavings(yearly_income) / 12
  return monthly_savings

def netSavingsRate (yearly_income):
  net_savings_rate = annualSavings(yearly_income) / netIncome(yearly_income) *100
  return net_savings_rate

print('')
print('Income Tax Payment: £' + str("{:,}".format(round(incomeTaxPayment(yearly_income),2))))
print('National Insurance Payment: £' + str("{:,}".format(round(nationalInsurancePayment(yearly_income),2))))
print('Student Loan Payment: £' + str("{:,}".format(round(studentLoanPayment(yearly_income),2))))
print('')
print('Total Tax Payment: £' + str("{:,}".format(round(totalTaxPayment(yearly_income),2))))
print('Effective Tax Rate: ' + str(round(effectiveTaxRate(yearly_income),2)) + '%')
print('Net Income: £' + str("{:,}".format(round(netIncome(yearly_income),2))))
print('')
print('Annual Savings: £' + str("{:,}".format(round(annualSavings(yearly_income),2))))
print('Monthly Savings: £' + str("{:,}".format(round(monthlySavings(yearly_income),2))))
print('Net Savings Rate: ' + str(round(netSavingsRate(yearly_income),2)) + '%')
