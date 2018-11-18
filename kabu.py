import pandas as pd
import numpy as np
from IPython.core.display import display

import pandas_datareader.data as web
import datetime

class Kabu():
    '''
    @brief : 株価を取得するクラス
    '''
    dfAllBrands = ""
    
    def __init__(self):
        print("")
        
    def init_kabutan(self):
        '''
        @brief : 株探サイトから株価一覧を取得（2018.11.18 全銘柄のデータ取得は不可）
        '''
        pd.set_option("display.max_rows", 10)
        
        baseUrl = 'https://kabutan.jp/tansaku/?mode=1_funda_06&market=0&stc=&stm=0&page='
        pageNum = 1
        self.dfAllBrands = pd.DataFrame()
        while True:
            url = baseUrl + str(pageNum)
            # 7つ目に作られるDataFrameが銘柄情報
            # 1行目(index=0)にヘッダが重複して取得されるため2行目から使用
            dfBrandsInPage = pd.read_html(url, header=0)[6].iloc[1:,:]
            if len(dfBrandsInPage) == 0:
                #display('break')
                break
            self.dfAllBrands = self.dfAllBrands.append(dfBrandsInPage)
            pageNum += 1
        
        # ヘッダ部とデータ部のズレを引き起こしている不要な列を除外してDataFrameを再構成
        header = self.dfAllBrands.columns.values
        header = np.r_[header[0:3],header[4:5],header[6:12]] 
        data = [np.r_[row[0:3],row[5:6],row[7:]] for row in self.dfAllBrands.values]
        self.dfAllBrands = pd.DataFrame(data, columns=header)
        #display(self.dfAllBrands)
        
    def display_kabutan(self):
        display(self.dfAllBrands)
        
    def get_last_by_stooq(self, ticker_code):
        '''
        @brief : 指定した銘柄コードの最新株価を取得
        '''
        code = str(ticker_code) + '.JP'
        #print(code)
        end = datetime.date.today()
        start = end - datetime.timedelta(days=10)
        
        df = web.DataReader(code, 'stooq', start, end)
        return df
        
# For Debug
#kabu = Kabu()
#print(kabu.get_last_by_stooq(6503))