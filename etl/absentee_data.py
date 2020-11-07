import pandas as pd

# Show all columns when printing
pd.set_option('display.max_columns', None)

dir_path = r'C:\Users\mayer\Desktop\Development\gaston-election2020\data\absentee_data'
data_path = dir_path + r'\absentee_20201103.csv'

# if you don't specify the encoding here you get a UnicodeDecodeError
data = pd.read_csv(data_path, encoding="ISO-8859-1")

# narrow it down to just Gaston County
df = data[data['county_desc'] == 'GASTON']

# save results to Excel file
df.to_excel(dir_path + r'\absentee_data.xlsx', index=False)