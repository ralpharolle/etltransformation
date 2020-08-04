# [ESSILOR] Python Exam for Basic ETL Transformation
# Author/Applicant: Rolle, Ralph Michael A.
# Date: 20200804 2259

import pandas as pd

# Read the CSV file and store it to variable df as DataFrame
df = pd.read_csv('example-file.csv')

# Converts column header to UPPERCASE
df.columns = df.columns.str.upper()

# Filter the given CSV file with CHLOE records and save it to CHLOE.csv
df[df.SUB_ENTITY=="CHLOE"].to_csv('CHLOE.csv', index = False)

# Filter the given CSV file with Antony-PF records and save it to Antony-PF.csv
df[df.SUB_ENTITY=="Antony-PF"].to_csv('Antony-PF.csv', index = False)
