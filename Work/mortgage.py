# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra = 1000
extra_month = 12

while principal > 0:
    principal = principal * (1 + rate / 12) - payment

    if extra_month > 0:
        total_paid = total_paid + payment + 1000
    else:
        total_paid = total_paid + payment

    extra_month -= 1

print('Total paid', total_paid)
