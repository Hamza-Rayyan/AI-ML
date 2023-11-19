Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\omer\Desktop\Internship for ML\Internship Short\Loan Predict\Loan Prediction.py
Libraries updated
pandas version  2.1.3
Number of columns in the dataframe: 13
Number of rows in the dataframe: 614

['Loan_ID', 'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'Loan_Status']
Loan_Status
Y    422
N    192
Name: count, dtype: int64 

    Loan_ID Gender Married  ...  Credit_History Property_Area Loan_Status
0  LP001002   Male      No  ...            1.00         Urban           Y
1  LP001003   Male     Yes  ...            1.00         Rural           N
2  LP001005   Male     Yes  ...            1.00         Urban           Y
3  LP001006   Male     Yes  ...            1.00         Urban           Y
4  LP001008   Male      No  ...            1.00         Urban           Y

[5 rows x 13 columns] 

       Dependents  ApplicantIncome  ...  Loan_Amount_Term  Credit_History
count      599.00           614.00  ...            600.00          564.00
mean         0.76          5403.46  ...            342.00            0.84
std          1.02          6109.04  ...             65.12            0.36
min          0.00           150.00  ...             12.00            0.00
25%          0.00          2877.50  ...            360.00            1.00
50%          0.00          3812.50  ...            360.00            1.00
75%          2.00          5795.00  ...            360.00            1.00
max          3.00         81000.00  ...            480.00            1.00

[8 rows x 6 columns] 

Loan_ID               0
Gender               13
Married               3
Dependents           15
Education             0
Self_Employed        32
ApplicantIncome       0
CoapplicantIncome     0
LoanAmount           22
Loan_Amount_Term     14
Credit_History       50
Property_Area         0
Loan_Status           0
dtype: int64 

Loan_ID               0
Gender               13
Married               3
Dependents           15
Education             0
Self_Employed        32
ApplicantIncome       0
CoapplicantIncome     0
LoanAmount            0
Loan_Amount_Term     14
Credit_History        0
Property_Area         0
Loan_Status           0
dtype: int64 

Number of columns in the dataframe: 13
Number of rows in the dataframe: 614

Loan_ID              0
Gender               0
Married              0
Dependents           0
Education            0
Self_Employed        0
ApplicantIncome      0
CoapplicantIncome    0
LoanAmount           0
Loan_Amount_Term     0
Credit_History       0
Property_Area        0
Loan_Status          0
dtype: int64 

Number of columns in the dataframe: 13
Number of rows in the dataframe: 542

Preprocessing Stage, Visualization Level 1 Done
Loan_Status    N    Y
Gender               
Female        33   65
Male         133  311
Married   No  Yes
Gender           
Female    69   29
Male     118  326
Self_Employed   No  Yes
Gender                 
Female          83   15
Male           384   60
Property_Area  Rural  Semiurban  Urban
Gender                                
Female            23         49     26
Male             136        160    148
Loan_Status
Y    376
N    166
Name: count, dtype: int64 

Loan_Status
1    376
0    166
Name: count, dtype: int64 

Gender
Male      444
Female     98
Name: count, dtype: int64 

Gender
1    444
0     98
Name: count, dtype: int64 

Married
Yes    355
No     187
Name: count, dtype: int64 

Married
1    355
0    187
Name: count, dtype: int64 

Education
Graduate        425
Not Graduate    117
Name: count, dtype: int64 

Education
1    425
0    117
Name: count, dtype: int64 

Self_Employed
No     467
Yes     75
Name: count, dtype: int64 

Self_Employed
0    467
1     75
Name: count, dtype: int64 

Property_Area
Semiurban    209
Urban        174
Rural        159
Name: count, dtype: int64 

Property_Area
1    209
2    174
0    159
Name: count, dtype: int64 

    Loan_ID  Gender  Married  ...  Credit_History  Property_Area  Loan_Status
0  LP001002       1        0  ...            1.00              2            1
1  LP001003       1        1  ...            1.00              0            0
2  LP001005       1        1  ...            1.00              2            1
3  LP001006       1        1  ...            1.00              2            1
4  LP001008       1        0  ...            1.00              2            1

[5 rows x 13 columns] 

Preprocessing Stage, Visualization Level 2 Done

 train_X = 
      Gender  Married  ...  Credit_History  Property_Area
205       0        0  ...            1.00              1
122       0        0  ...            0.00              1
458       1        0  ...            1.00              0
308       1        0  ...            1.00              0
339       0        0  ...            1.00              1
..      ...      ...  ...             ...            ...
81        1        1  ...            1.00              1
124       1        1  ...            1.00              0
306       0        0  ...            1.00              0
495       0        1  ...            1.00              1
119       0        0  ...            1.00              2

[487 rows x 11 columns]

 test_X = 
 

 train_y = 
 205    1
122    1
458    1
308    0
339    1
      ..
81     1
124    1
306    1
495    1
119    1
Name: Loan_Status, Length: 487, dtype: int64

 test_y = 
 

 final_test = 
      Gender  Married  ...  Credit_History  Property_Area
409       1        1  ...            0.00              0
83        1        1  ...            1.00              1
402       1        0  ...            1.00              1
97        1        1  ...            1.00              1
270       0        0  ...            1.00              2
87        1        1  ...            1.00              1
235       1        1  ...            1.00              0
568       0        0  ...            1.00              2
607       1        1  ...            1.00              0
585       1        1  ...            1.00              0

[10 rows x 11 columns]

 Machine Learning Model Build 

accuracy_score 0.7454545454545455 

Output Prediction =  [0 1 1 1 1 1 1 1 1 1] 


 409    0
83     0
402    1
97     1
270    1
87     1
235    1
568    0
607    1
585    0
Name: Loan_Status, dtype: int64
Project End
