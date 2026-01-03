import pandas as pd
import glob

folder_path = "C:\Exercise\dataegfrfilter2025"

excel_files = glob.glob(folder_path + "/*.xlsx")

df_list = []

for file in excel_files:
    df = pd.read_excel(file)
    df_list.append(df)

lt_all = pd.concat(df_list, ignore_index=True)

jumlah_pasien_egfr = lt_all['Test Name'].notna().sum()

print(jumlah_pasien_egfr)