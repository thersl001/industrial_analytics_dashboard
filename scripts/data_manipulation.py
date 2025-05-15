"""
This script processes the raw ASI (Annual Survey of Industries) data file by cleaning, transforming, and encoding it for further analysis. 

Key Opeations Performed:

- Removal of irrelevant and empty columns to streamline the dataset.
- Replacement of missing unit values with a standard label.
- Mapping of categorical variables ("State" and "Indicator") to numeric IDs to create primary keys.
- Renaming and reordering columns for consistency and clarity.
- Exporting the cleaned and encoded dataset to a new CSV file for use in data modelling.

"""

import pandas as pd

# Imported the ASI Data File
d1 = pd.read_csv(r"C:\Users\Rushikesh\Desktop\ASI Data.csv") 

# Removed the unwanted and empty columns from table
d1.drop(["Unnamed: 10", "Unnamed: 11", "Unnamed: 12", "Unnamed: 13", "Unnamed: 14", "Unnamed: 15", "NIC type", 
         "Sector", "NIC Description", "NIC Classification"], axis=1, inplace=True) 

# Replaced "-" with "Units" 
d1["Unit"] = d1["Unit"].mask(d1["Unit"] == "-", "Units")                           

# Coded the "State" column with Numbers to create Foreign Keys 
state_mapping = {                                                                  
    "All India": 0,
    "Dadra & N Haveli & Daman & Diu": 1,
    "Ladakh": 2,
    "Telangana": 3,
    "A & N. Island": 4,
    "Puducherry": 5,
    "Tamil Nadu": 6,
    "Kerala": 7,
    "Goa": 8,
    "Karnataka": 9,
    "Andhra Pradesh": 10,
    "Maharashtra": 11,
    "Gujarat": 12,
    "Madhya Pradesh": 13,
    "Chattisgarh": 14,
    "Odisha": 15,
    "Jharkhand": 16,
    "West Bengal": 17,
    "Assam": 18,
    "Meghalaya": 19,
    "Tripura": 20,
    "Mizoram": 21,
    "Manipur": 22,
    "Nagaland": 23,
    "Arunachal Pradesh": 24,
    "Sikkim": 25,
    "Bihar": 26,
    "Uttar Pradesh": 27,
    "Rajasthan": 28,
    "Delhi": 29,
    "Haryana": 30,
    "Uttarakhand": 31,
    "Chandigarh": 32,
    "Punjab": 33,
    "Himachal Pradesh": 34,
    "Jammu & Kashmir": 35,
    "Dadra & N Haveli": 36,
    "Daman & Diu": 37
}

# Coded the "Indicator" column with Numbers to create Foreign Keys
indicator_mapping = {                                                             
    "Number of Factories": 1,
    "Factories in Operation": 2,
    "Fixed Capital": 3,
    "Physical Working Capital": 4,
    "Working Capital": 5,
    "Invested Capital": 6,
    "Gross Value of Addition to Fixed Capital": 7,
    "Rent Paid for Fixed Assets": 8,
    "Outstanding Loan": 9,
    "Interest Paid": 10,
    "Rent Received for Fixed Asset": 11,
    "Interest Received": 12,
    "Gross Value of Plant & Machinery": 13,
    "Value of Product and By-Product": 14,
    "Total Output": 15,
    "Fuels Consumed": 16,
    "Materials Consumed": 17,
    "Total Inputs": 18,
    "Gross Value Added": 19,
    "Depreciation": 20,
    "Net Value Added": 21,
    "Net Fixed Capital Formation": 22,
    "Gross Fixed Capital Formation": 23,
    "Addition in Stock of Materials, Fuels, Semi Finished Goods, Finshed Goods etc.": 24,
    "Addition in Stock of Materials, Fuels etc.": 25,
    "Addition in Stock of Semi Finished Goods": 26,
    "Addition in Stock of Finished Goods": 27,
    "Gross Capital Formation": 28,
    "Net Income": 29,
    "Net Profit": 30,
    "Total Number of Persons Engaged": 31,
    "Total Number of Workers": 32,
    "No. of Directly Employed  Workers": 33,
    "No. of Directly Employed Male Workers": 34,
    "No. of Directly Employed Female Workers": 35,
    "No. of Workers employed Through Contractors": 36,
    "No. of Employees Other Than Workers": 37,
    "No. of Employees Other Than Workers -Supervisory and Managerial": 38,
    "No. of Employees Other Than Workers -Other Employees": 39,
    "Unpaid family members-proprietor etc": 40,
    "Total Mandays Employed": 41,
    "Wages and Salaries Including Employer's Contribution": 42,
    "Wages and Salaries Including Bonus": 43,
    "Wages and Salaries": 44,
    "Wages and Salary of Workers": 45,
    "Wages and Salary of Supervisory & Managerial Employees": 46,
    "Wages and Salary of  Other Employees": 47,
    "Bonus to All Staff": 48,
    "Employers' Contribution": 49,
    "Quantity of Coal Consumed": 50,
    "Value of Coal Consumed": 51,
    "Quantity of Electricity Purchased and Consumed": 52,
    "Value of Electricity Purchased  and Consumed": 53,
    "Value of Petroleum Products Consumed": 54,
    "Value of Other Fuels Consumed": 55,
    "Total Value of Fuel Consumed": 56
}

# Created a new column named "State_ID" with respective coded numbers
d1['State_ID'] = d1["State"].map(state_mapping)     

# Created a new column named "Indicator_ID" with respective coded numbers
d1['Indicator_ID'] = d1["Indicator"].map(indicator_mapping)       

# Renamed "NIC Code" into "Nic_Code" to maintain consistency in variable naming
d1["NIC_Code"] = d1["NIC Code"]                                                   

# Removed "State", "Indicator", "NIC Code" columns to keep only their coded columns in dataset for Data Modelling
d1.drop(["State", "Indicator", "NIC Code"], axis=1, inplace=True)                  

# Reordered dataset 
d1 = d1[["Year", "State_ID", "Indicator_ID", "NIC_Code", "Value", "Unit"]] 

# Exported new dataset named "Value_table" after all transformations
d1.to_csv("C:/Users/Rushikesh/Desktop/Value_table.csv", index=False)               
