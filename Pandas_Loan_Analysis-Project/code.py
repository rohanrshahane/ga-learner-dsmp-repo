# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here

bank = pd.read_csv(path,sep=",",delimiter=None,header='infer',names=None, index_col=None, usecols=None)
categorical_var = bank.select_dtypes(include='object')
print(categorical_var)
numerical_var = bank.select_dtypes(include='number')
print(numerical_var)





# code ends here


# --------------
# code starts here

banks = bank.drop(columns='Loan_ID')
#banks=bank
print(bank.isnull().sum())

bank_mode = banks.mode().iloc[0]
banks.fillna(bank_mode, inplace=True)
print(banks.isnull().sum())

#code ends here


# --------------
# Code starts here

avg_loan_amount = pd.pivot_table(banks, index=['Gender', 'Married', 'Self_Employed'], values='LoanAmount',aggfunc='mean')
print(avg_loan_amount)


# code ends here



# --------------
# code starts here

loan_approved_se = banks[(banks['Loan_Status'] == "Y") & (banks['Self_Employed'] == "Yes")]
loan_approved_se = loan_approved_se['Gender'].count()
print(loan_approved_se)
loan_approved_nse = banks[(banks['Loan_Status'] == "Y") & (banks['Self_Employed'] == "No")]
loan_approved_nse = loan_approved_nse['Gender'].count()

percentage_se = round((100 * loan_approved_se/614),2)
percentage_nse = round((100 * loan_approved_nse/614),2)

# code ends here


# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)

big_loan_term = loan_term[(loan_term >= 25)].count()



# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby(by='Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()
print(mean_values)



# code ends here


