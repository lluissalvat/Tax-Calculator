# Tax-Calculator
This script takes annual income and monthly expenses as inputs and outputs tax payments and a variety of personal finance metrics.

This script focuses on England and Wales personal taxes, and relies on a series of assumptions: 
1) The taxpayer only pays Income Tax and National Insurance Contributions.
2) The taxpayer took Plan 2 Undergraduate Student Loans from the SLC and makes the minimum payments.
3) The taxpayer isn't claiming tax reliefs of any kind.
4) The taxpayer doesn't have any additional sources of income other than a stardard permanent employment contract.

The script requires two outputs from the user (the taxpayer):
1) The user's annual gross salary.
2) The user's monthly expenses.

The script outputs the following values:
1) Income Tax Payment
2) National Insurance Payment
3) Student Loan Payment
4) Total Tax Payment
5) Effective Tax Rate
6) Net Income
7) Annual Savings
8) Monthly Savings
9) Net Savings Rate

This script accounts for the loss of the personal allowance once the income exceeds £100,000.

This is an example output of the script for the following input variables (Annual Gross Pay: £50000, Monthly Expenses: £2000): 

Income Tax Payment: £7,486.0,
National Insurance Payment: £4,852.32,
Student Loan Payment: £2,043.45.

Total Tax Payment: £14,381.77,
Effective Tax Rate: 28.76%,
Net Income: £35,618.23.

Annual Savings: £11,618.23,
Monthly Savings: £968.19,
Net Savings Rate: 32.62%.

Disclaimer: This material has been prepared for informational purposes only, and is not intended to provide, and should not be relied on for, tax, legal or accounting advice. You should consult your own tax, legal and accounting advisors before engaging in any transaction.
