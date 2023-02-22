#write a program that calculates 16% tax
#ranging btwn 100k - 150k

#19% tax income is btwn 150k - 300k
#30% tax income is above 300k
#15% if income is below 100k
#200 nssf
#800 nhif
#print gross income ,net income 
gross_income = int(input("enter your income:"))
tax_group_a = (gross_income *0.05)
tax_group_b = (gross_income *0.16)
tax_group_c = (gross_income *0.19)
tax_group_d = (gross_income *0.3)

if gross_income <= 100000:
    print("gross_income:",gross_income)
    print("net_income:",gross_income - tax_group_a )
elif (gross_income >= 100001) & (gross_income < 150000):
    print("gross_income:",gross_income)
    print("net_income:",gross_income -tax_group_b)
elif (gross_income >= 150001) & (gross_income < 300000):
     print("gross_income:",gross_income) 
     print("net_income:",gross_income -tax_group_c)
else:
    print("gross_income:",gross_income)
    print("net_income:",gross_income -tax_group_d)







  




