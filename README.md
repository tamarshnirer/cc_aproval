# cc_aproval

## Introduction

Credit score cards are a common risk control method in the financial industry. It uses personal information and data submitted by credit card applicants to predict the probability of future defaults and credit card borrowings. The bank is able to decide whether to issue a credit card to the applicant. Credit scores can objectively quantify the magnitude of risk.
 
Generally speaking, credit score cards are based on historical data. Once encountering large economic fluctuations. Past models may lose their original predictive power. Logistic model is a common method for credit scoring. Because Logistic is suitable for binary classification tasks and can calculate the coefficients of each feature. In order to facilitate understanding and operation, the score card will multiply the logistic regression coefficient by a certain value (such as 100) and round it.
 
At present, with the development of machine learning algorithms. More predictive methods such as Boosting, Random Forest, and Support Vector Machines have been introduced into credit card scoring. However, these methods often do not have good transparency. It may be difficult to provide customers and regulators with a reason for rejection or acceptance.

The project data was taken from https://www.kaggle.com/rikdifos/credit-card-approval-prediction 

## Goal

My goal is to predict to predict what would be current month's loan status, given certain soical econoical and credit history of a client.

## Data Dictionary

application_record.csv		

ID	Client = number	<br />
CODE_GENDER	= Gender	<br />
FLAG_OWN_CAR	= Is there a car	<br />
FLAG_OWN_REALTY	= Is there a property	<br />
CNT_CHILDREN	= Number of children	<br />
AMT_INCOME_TOTAL	= Annual income	<br />
NAME_INCOME_TYPE	= Income category	<br />
NAME_EDUCATION_TYPE	= Education level	<br />
NAME_FAMILY_STATUS	= Marital status	<br />
NAME_HOUSING_TYPE	= Way of living	<br />
DAYS_BIRTH	= Birthday	(Count backwards from current day (0), -1 means yesterday)<br />
DAYS_EMPLOYED	= Start date of employment	(Count backwards from current day(0). If positive, it means the person currently unemployed.)<br />
FLAG_MOBIL	= Is there a mobile phone	<br />
FLAG_WORK_PHONE	= Is there a work phone	<br />
FLAG_PHONE	= Is there a phone	<br />
FLAG_EMAIL	= Is there an email	<br />
OCCUPATION_TYPE	= Occupation	<br />
CNT_FAM_MEMBERS	= Family size	<br />

credit_record.csv		

ID	Client = number	<br />
MONTHS_BALANCE	= Record month	The month of the extracted data is the starting point, backwards, (0 is the current month, -1 is the previous month, and so on)<br />
STATUS	= Status	(0: 1-29 days past due 1: 30-59 days past due 2: 60-89 days overdue 3: 90-119 days overdue 4: 120-149 days overdue 5: Overdue or bad debts, write-offs for more than 150 days C: paid off that month X: No loan for the month)
