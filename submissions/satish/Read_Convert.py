import pandas as pd
import glob
json_files = glob.glob('C:\\Users\\MsK_PC\\Desktop\\data\\*.json')
df = pd.concat([pd.read_json(file , encoding='UTF-8', lines= True) for file in json_files], ignore_index = True)
df.to_excel('output.xlsx', index = False)