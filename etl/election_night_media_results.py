import pandas as pd


dir_path = r'C:\Users\mayer\Desktop\Development\gaston-election2020\data\election_night_media_results'
data_path = dir_path + r'\results_pct_20201103.txt'

# tab-delimited .txt file
data = pd.read_csv(data_path, sep="\t")

# narrow it down to just Gaston County
df = data[data['County'] == 'GASTON']

# sort by Precint, then Contest, then Total Votes descending
df = df.sort_values(by=['Precinct', 'Contest Group ID', 'Total Votes'], ascending=[True, True, False])

# save results to Excel file
df.to_excel(dir_path + r'\election_night_media_results.xlsx', index=False)