import json
extract = lambda x: [i['content'] for i in x]
page_number = 2
file_name = "table_data.pdf"
file = file_name.strip('.pdf')
with open(f'artifacts/{file}_page{page_number}.json') as f:
    data = json.load(f)
table_data = data['tables']

_table = []
for i,table in enumerate(table_data):        
    data = table_data[i]
    _row=[]       
    for _ in range(0,len(table['cells']), table['columnCount']):
        _row.append(extract(table['cells'][_ : _+table['columnCount']]))
    _table.append(_row)

import pandas as pd
_dfs = []
for _t in _table:
    df = pd.DataFrame(_t[1:], columns=_t[0])
    _dfs.append(df)

for i, _df in enumerate(_dfs):
    _df.to_csv(f'artifacts/{file}_page{page_number}_table{i}.csv', index=False)
