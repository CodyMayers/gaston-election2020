import pandas as pd

# Show all columns when printing
pd.set_option('display.max_columns', None)

dir_path = r'C:\Users\mayer\Desktop\Development\gaston-election2020\data\voter_statistics'
data_path = dir_path + r'\voter_stats_20201103.txt'

# tab-delimited .txt file
data = pd.read_csv(data_path, sep="\t")

# narrow it down to just Gaston County
df = data[data['county_desc'] == 'GASTON']

# sort by Precint, then Contest, then Total Votes descending
df = df.sort_values(by=['precinct_abbrv', 'party_cd', 'total_voters'], ascending=[True, True, False])

# save results to Excel file
df.to_excel(dir_path + r'\voter_statistics.xlsx', index=False)