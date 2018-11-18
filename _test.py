import sys
import pprint

#print(sys.path)

import pandas_datareader.data as web
import datetime

end = datetime.date.today()
start = end - datetime.timedelta(days=10)

df = web.DataReader('8411.JP', 'stooq', start, end)
print(df[:1])