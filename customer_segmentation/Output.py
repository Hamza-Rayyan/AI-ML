Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\omer\Desktop\Internship for ML\ML-Customer Segmentation\Customer Segment L2.py
Libraries updated
pandas version  2.1.3
Number of columns in the dataframe: 11
Number of rows in the dataframe: 8068

['ID', 'Gender', 'Ever_Married', 'Age', 'Graduated', 'Profession', 'Work_Experience', 'Spending_Score', 'Family_Size', 'Var_1', 'Segmentation']
Segmentation
D    2268
A    1972
C    1970
B    1858
Name: count, dtype: int64 

       ID  Gender Ever_Married  ...  Family_Size  Var_1 Segmentation
0  462809    Male           No  ...         4.00  Cat_4            D
1  462643  Female          Yes  ...         3.00  Cat_4            A
2  466315  Female          Yes  ...         1.00  Cat_6            B
3  461735    Male          Yes  ...         2.00  Cat_6            B
4  462669  Female          Yes  ...         6.00  Cat_6            A

[5 rows x 11 columns] 

             ID     Age  Work_Experience  Family_Size
count   8068.00 8068.00          7239.00      7733.00
mean  463479.21   43.47             2.64         2.85
std     2595.38   16.71             3.41         1.53
min   458982.00   18.00             0.00         1.00
25%   461240.75   30.00             0.00         2.00
50%   463472.50   40.00             1.00         3.00
75%   465744.25   53.00             4.00         4.00
max   467974.00   89.00            14.00         9.00 

Number of columns in the dataframe: 9
Number of rows in the dataframe: 8068

Gender               0
Ever_Married       140
Age                  0
Graduated           78
Profession         124
Work_Experience    829
Spending_Score       0
Family_Size        335
Segmentation         0
dtype: int64
Gender             0
Ever_Married       0
Age                0
Graduated          0
Profession         0
Work_Experience    0
Spending_Score     0
Family_Size        0
Segmentation       0
dtype: int64 

Number of columns in the dataframe: 9
Number of rows in the dataframe: 6718

Segmentation
D    1772
C    1735
A    1628
B    1583
Name: count, dtype: int64 

Preprocessing Stage, Visualization Level 1 Done
Ever_Married    No   Yes
Gender                  
Female        1420  1596
Male          1323  2379
Profession  Artist  Doctor  Engineer  ...  Homemaker  Lawyer  Marketing
Gender                                ...                              
Female        1069     258       470  ...        147     256        128
Male          1142     336       116  ...         31     247        105

[2 rows x 9 columns]
Spending_Score  Average  High   Low
Gender                             
Female              700   398  1918
Male                977   614  2111
Profession  Artist  Doctor  Engineer  ...  Homemaker  Lawyer  Marketing
Graduated                             ...                              
No             245     247       316  ...         77     177        142
Yes           1966     347       270  ...        101     326         91

[2 rows x 9 columns]
Profession
Artist           2211
Healthcare       1089
Entertainment     815
Doctor            594
Engineer          586
Executive         509
Lawyer            503
Marketing         233
Homemaker         178
Name: count, dtype: int64 

(4329, 8)
Gender
Male      2529
Female    1800
Name: count, dtype: int64 

Gender
1    2529
0    1800
Name: count, dtype: int64 

Ever_Married
Yes    2292
No     2037
Name: count, dtype: int64 

Ever_Married
1    2292
0    2037
Name: count, dtype: int64 

Profession
Healthcare       1089
Entertainment     815
Doctor            594
Engineer          586
Executive         509
Lawyer            503
Marketing         233
Name: count, dtype: int64 

Profession
6    1089
4     815
2     594
3     586
5     509
8     503
9     233
Name: count, dtype: int64 

Spending_Score
Low        2808
High        780
Average     741
Name: count, dtype: int64 

Spending_Score
0    2808
2     780
1     741
Name: count, dtype: int64 

Segmentation
D    1593
A    1106
B     871
C     759
Name: count, dtype: int64 

Segmentation
4    1593
1    1106
2     871
3     759
Name: count, dtype: int64 

Preprocessing Stage, Visualization Level 2 Done

 train_X = 
       Ever_Married  Age  Profession  ...  Spending_Score  Family_Size  Segmentation
3723             0   20           6  ...               0         4.00             4
2053             1   27           4  ...               1         2.00             2
7158             0   47           4  ...               0         1.00             1
2440             0   21           6  ...               0         4.00             4
3438             0   20           6  ...               0         4.00             4
...            ...  ...         ...  ...             ...          ...           ...
8031             1   43           4  ...               1         2.00             1
4695             0   23           6  ...               0         4.00             4
1006             1   62           8  ...               0         2.00             3
2222             0   41           4  ...               0         1.00             4
7961             0   36           9  ...               0         2.00             4

[3679 rows x 7 columns]

 test_X = 
       Ever_Married  Age  Profession  ...  Spending_Score  Family_Size  Segmentation
5666             1   71           8  ...               1         2.00             3
2934             1   38           4  ...               0         3.00             1
3203             1   43           2  ...               0         1.00             2
3646             1   26           2  ...               1         3.00             4
5404             1   36           4  ...               1         4.00             1
...            ...  ...         ...  ...             ...          ...           ...
4893             1   61           5  ...               2         2.00             3
2381             1   69           5  ...               1         4.00             2
5755             1   87           8  ...               2         2.00             1
1560             1   38           9  ...               2         4.00             2
368              0   18           6  ...               0         5.00             4

[650 rows x 7 columns]

 train_y = 
 3723    4
2053    2
7158    1
2440    4
3438    4
       ..
8031    1
4695    4
1006    3
2222    4
7961    4
Name: Segmentation, Length: 3679, dtype: int64

 test_y = 
 5666    3
2934    1
3203    2
3646    4
5404    1
       ..
4893    3
2381    2
5755    1
1560    2
368     4
Name: Segmentation, Length: 650, dtype: int64

 final_test = 
       Ever_Married  Age  Profession  ...  Spending_Score  Family_Size  Segmentation
5666             1   71           8  ...               1         2.00             3
2934             1   38           4  ...               0         3.00             1
3203             1   43           2  ...               0         1.00             2
3646             1   26           2  ...               1         3.00             4
5404             1   36           4  ...               1         4.00             1
1214             1   38           4  ...               0         1.00             2
3525             0   39           4  ...               0         2.00             1
1228             0   25           3  ...               0         2.00             1
1596             1   48           5  ...               2         2.00             1
7956             0   50           9  ...               0         4.00             4

[10 rows x 7 columns]

 Machine Learning Model Build 


 5666    3
2934    1
3203    2
3646    4
5404    1
1214    2
3525    1
1228    1
1596    1
7956    4
Name: Segmentation, dtype: int64 

LR Alg Accuracy 1.0 

Output Prediction =  [3 1 2 4 1 2 1 1 1 4] 

SVM Alg Accuracy 70 Percent
Output Prediction SVM =  [2 1 1 4 1 1 1 1 1 4] 

KNN Alg Accuracy 78 Percent
Output Prediction KNN =  [3 1 1 4 1 2 1 1 2 4] 

Project End
