from bs4 import BeautifulSoup
import pymysql.cursors
import re
tmaster = ["aapl"]
#"AMZN", "BAC", "C", "CMCSA", "CSCO", "CVX", "FB", "GE", "GOOG", "GOOGL", "HD", "INTC", "JNJ", "JPM", 'KO', 'MRK', 'MSFT', 'PFE', 'PG', 'PM', 'T', 'V', 'VZ', 'WFC', 'XOM', 'BRK.B', 'UNH', 'DIS', 'PEP', 'MO', 'IBM', 'ORCL', 'AMGN', 'MMM', 'MCD', 'MDT', 'WMT', 'MA', 'ABBV', 'BA', 'HON', 'SLB', 'CELG', 'PCLN', 'BMY', 'UNP', 'AVGO', 'UTX', 'SBUX', 'GILD', 'GS', 'USB', 'CVS', 'AGN', 'QCOM', 'TXN', 'COST', 'LLY', 'TWX', 'ABT', 'ACN', 'LOW', 'UPS', 'WBA', 'NKE', 'CHTR', 'DOW', 'MDLZ', 'DD', 'LMT', 'NFLX', 'ADBE', 'TMO', 'CB', 'CL', 'MS', 'NEE', 'NVDA', 'AXP', 'PNC', 'CAT', 'BIIB', 'COP', 'DUK', 'AIG', 'MET', 'CRM', 'GD', 'PYPL', 'AMT', 'KHC', "SPG","EOG","TJX","MON","DHR","BK","SCHW","SO","D","CSX","ANTM","BLK","PRU","FDX","AET","OXY","RTN","GM","KMB","AMAT","ADP","F","ITW","NOC","BLKFDS","YHOO","SYK","CI","CME","COF", "HAL","BDX","JCI","KMI","EMR","MMC","ESRX","CTSH","ATVI","BSX","ICE","LUV","PX","BBT","DAL","PSX","SPGI","ETN","NSC","PCG","TRV","CCI","EBAY","HUM","AEP","ECL","EQIX","GIS", "DE","TGT","HPQ","AON","EXC","APD","ISRG","REGN","ALL","HPE","PSA","MAR","INTU","FOXA","STT","STZ","AFL","VRTX","WM","MCK","ALXN","VLO","EA","MU","PXD", "STI","PLD","PPG","SRE","ADI","ILMN","ZTS","FIS","BAX","KR","SHW","MPC","LYB","GLW","TEL","SYY","CCL","AVB","PPL","WDC","EIX","ROST","FISV","WMB", "WY","CMI","MTB","LRCX","ED","ZBH","HCA","PCAR","DFS","CBS","ADM","EQR","DLPH","PGR","EW","IR","YUM","CAH","ORLY","XEL","SYF","AAL", "VTR","PEG","ROP","APH","DXC","NWL","IP","PH","UAL","SWK","INCY","EL","KEY","DVN","AMP","AZO","ROK","MCO", "NTRS","OMC","DLTR","CXO","NUE","BXP","WEC","FTV","CERN","CFG","DG","SWKS","ES","DTE","PAYX","APA","FITB", "HIG","RCL","ADSK","A","MNST","TSN","DLR","VFC","PFG","NEM","TROW","K","WLTW","RF","MYL","ULTA", "VMC","CLX","EXPE","TAP","EFX","ESS","MCHP","VNO","FCX","O","KLAC","CAG", "XLNX","MLM","HSY","LNC","DGX","BEN","SJM","XRAY","FTI","MHK", "RSG","HBAN","LH","ADS","MSI","IDXX","CTL","BBY","AWK","USD","HSIC","ETR","WHR","WAT", "VIAB","FOX","NBL","HRS","CMG","DISH","AME","NLSN","GPC","CTXS","ABC","WRK","HST","MTD","BLL","FAST","AEE","IVZ","L","CNC","NOV","FE","CMA", "CMS","LB","HES","TXT","MRO","CHD","HOLX","STX","GPN","TDG","ALB", "DOV","CNP","ARNC","VRSK","MAS","COG","JNPR","EMN","XEC","MKC","HAS","SNPS","MAA","OKE","DHI","UHS","IFF","CPB","KMX","DRI","NTAP","PNR","ALK","UNM","CINF", "SLG","CTAS","AAP","CHRW","PRGO","GWW","DVA", "EQT", "IT","LEN","FL","ARE","ETFC","COO", "WYNN","UDR","TIF","RJF","LKQ","EXPD","HOG", "AJG","FBHS","SNA","FRT","FMC","KSU", "IPG","PNW","HRL","AKAM","REG","WU","EXR","URI","XYL","LNT","GT","AMG","M","SEE","QRVO","KIM","VAR", "COTY", "IRM", "MOS","BWA","FFIV","TSCO","ZION","AMD","VRSN","NDAQ","PVH","JBHT","HBI","NI","AYI","AVY","CBOE","MAC","ALLE","AES","MAT","SRCL","FLR","LEG","KSS","AIV","JEC","HP","FLS","PKI","PHM","XRX","PBCT","CF","RHI","GRMN","AIZ","JWN","GPS","DISCK","BBBY","TGNA","PWR","HRB","TRIP","FLIR","RRC","NWSA","NRG","MNK","SIG","RL","NAVI","CHK","RIG","MUR","DISCA","TDC","UAA","PDCO","R","UA","AN","NWS"]

statement_rotation = ["_income_statement_", "_balance_sheet_statement_", "_cash_flow_statement_"]

# TABLE CREATION //  // TESTED, FUNCTION REQUIRES TWO STRINGS


def create_table(live_schema, table_title):
    con1 = pymysql.connect(host="localhost",
                           user="jefferson",
                           passwd="1234",
                           db=live_schema)
    with con1.cursor() as cursor1:
        create_table_command = "CREATE TABLE " + table_title + "(id INT       AUTO_INCREMENT PRIMARY KEY)"
        cursor1.execute(create_table_command)
# create_table('testdb', 'tabletable')
# END OF TABLE CREATION

#   COLUMN TITLE CREATION


def new_col(live_schema, live_table, new_column):
    con2 = pymysql.connect(host="localhost",
                           user="jefferson",
                           passwd="1234",
                           db=live_schema)
    with con2.cursor() as cursor2:
        # create new columns
        new_col_command = "ALTER TABLE " + live_table + " ADD " + new_column + " TEXT(100);"
        print(new_col_command)
        cursor2.execute(new_col_command)
# new_col('sp500', t, master_statement[0][0])
# new_col('testdb', 'tabletable', 'new_col')
#   END OF COLUMN CREATION

#   ROW TITLE ADDITION


def new_row(live_schema, live_table, live_column, title_row):
    # def new_row(title_row):
    con3 = pymysql.connect(host="localhost",
                           user="jefferson",
                           passwd="1234",
                           db=live_schema)
    with con3.cursor() as cursor3:
        # create new rows
        # ini = []
        val = title_row
        new_row_command = "INSERT INTO `" + live_table + "` (`" + live_column + "`) VALUES  (%s)"
        # new_row_command_ini = "INSERT INTO `" + live_table + "` (`" + live_column + "`) VALUES (%s);"
        # ini.append(new_row_command_ini)
        # print(ini[0])
        # new_row_command = "INSERT INTO `tabletable` (`Statement`)VALUES(%s)"
        # test = "INSERT INTO `spy20190828` (`daydate`, `daytime`, `open_price`, `high_price`, `low_price`, `close_price`, `volume`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor3.execute(new_row_command, val)
        con3.commit()
# new_row('testdb', 'tabletable', 'Statement', '555')
# END OF ROW CELL TITLE INSERTION


# iterating over sp500 symbols
for symbol in tmaster:

    for a in range(0, 2, 1):
        # paths; refreshing every loop
        temp_list = []
        for b in range(1, 16, 1):
            temp = symbol + statement_rotation[a] + (str(b)) + ".html"
            # print(temp)
            temp_list.append(temp)

        # open 15 channels
        try:
            # delivery of 15 files
            f1 = open(temp_list[0])
            f2 = open(temp_list[1])
            f3 = open(temp_list[2])
            f4 = open(temp_list[3])
            f5 = open(temp_list[4])
            f6 = open(temp_list[5])
            f7 = open(temp_list[6])
            f8 = open(temp_list[7])
            f9 = open(temp_list[8])
            f10 = open(temp_list[9])
            f11 = open(temp_list[10])
            f12 = open(temp_list[11])
            f13 = open(temp_list[12])
            f14 = open(temp_list[13])
            f15 = open(temp_list[14])

            # isolation of 15 tables
            whole_html1 = f1.read()
            soup1 = BeautifulSoup(whole_html1, 'lxml')
            table1 = soup1.find('table', attrs={'id': 'report'})
            data1 = []
            rows1 = table1.findAll('tr')
            for row in rows1:
                cols = row.findAll('td')
                cols = [ele.text.strip() for ele in cols]
                data1.append([ele for ele in cols if ele])

            whole_html2 = f2.read()
            soup2 = BeautifulSoup(whole_html2, 'lxml')
            table2 = soup2.find('table', attrs={'id': 'report'})
            data2 = []
            rows2 = table2.findAll('tr')
            for row in rows2:
                cols = row.findAll('td')
                cols = [ele.text.strip() for ele in cols]
                data2.append([ele for ele in cols if ele])

            whole_html3 = f3.read()
            soup3 = BeautifulSoup(whole_html3, 'lxml')
            table3 = soup3.find('table', attrs={'id': 'report'})
            data3 = []
            rows3 = table3.findAll('tr')
            for row in rows3:
                cols = row.findAll('td')
                cols = [ele.text.strip() for ele in cols]
                data3.append([ele for ele in cols if ele])

            whole_html4 = f4.read()
            soup4 = BeautifulSoup(whole_html4, 'lxml')
            table4 = soup4.find('table', attrs={'id': 'report'})
            data4 = []
            rows4 = table4.findAll('tr')
            for row in rows4:
                cols = row.findAll('td')
                cols = [ele.text.strip() for ele in cols]
                data4.append([ele for ele in cols if ele])

            whole_html5 = f5.read()
            soup5 = BeautifulSoup(whole_html5, 'lxml')
            table5 = soup5.find('table', attrs={'id': 'report'})
            data5 = []
            rows5 = table5.findAll('tr')
            for row in rows5:
                cols = row.findAll('td')
                cols = [ele.text.strip() for ele in cols]
                data5.append([ele for ele in cols if ele])

            whole_html6 = f6.read()
            soup6 = BeautifulSoup(whole_html6, 'lxml')
            table6 = soup6.find('table', attrs={'id': 'report'})
            data6 = []
            rows6 = table6.findAll('tr')
            for row in rows6:
                cols = row.findAll('td')
                cols = [ele.text.strip() for ele in cols]
                data6.append([ele for ele in cols if ele])

            whole_html7 = f7.read()
            soup7 = BeautifulSoup(whole_html7, 'lxml')
            table7 = soup7.find('table', attrs={'id': 'report'})
            data7 = []
            rows7 = table7.findAll('tr')
            for row in rows7:
                cols = row.findAll('td')
                cols = [ele.text.strip() for ele in cols]
                data7.append([ele for ele in cols if ele])

            whole_html8 = f8.read()
            soup8 = BeautifulSoup(whole_html8, 'lxml')
            table8 = soup8.find('table', attrs={'id': 'report'})
            data8 = []
            rows8 = table8.findAll('tr')
            for row in rows8:
                cols = row.findAll('td')
                cols = [ele.text.strip() for ele in cols]
                data8.append([ele for ele in cols if ele])

            whole_html9 = f9.read()
            soup9 = BeautifulSoup(whole_html9, 'lxml')
            table9 = soup9.find('table', attrs={'id': 'report'})
            data9 = []
            rows9 = table9.findAll('tr')
            for row in rows9:
                cols = row.findAll('td')
                cols = [ele.text.strip() for ele in cols]
                data9.append([ele for ele in cols if ele])

            whole_html10 = f10.read()
            soup10 = BeautifulSoup(whole_html10, 'lxml')
            table10 = soup10.find('table', attrs={'id': 'report'})
            data10 = []
            rows10 = table10.findAll('tr')
            for row in rows10:
                cols = row.findAll('td')
                cols = [ele.text.strip() for ele in cols]
                data10.append([ele for ele in cols if ele])

            whole_html11 = f11.read()
            soup11 = BeautifulSoup(whole_html11, 'lxml')
            table11 = soup11.find('table', attrs={'id': 'report'})
            data11 = []
            rows11 = table11.findAll('tr')
            for row in rows11:
                cols = row.findAll('td')
                cols = [ele.text.strip() for ele in cols]
                data11.append([ele for ele in cols if ele])

            whole_html12 = f12.read()
            soup12 = BeautifulSoup(whole_html12, 'lxml')
            table12 = soup12.find('table', attrs={'id': 'report'})
            data12 = []
            rows12 = table12.findAll('tr')
            for row in rows12:
                cols = row.findAll('td')
                cols = [ele.text.strip() for ele in cols]
                data12.append([ele for ele in cols if ele])

            whole_html13 = f13.read()
            soup13 = BeautifulSoup(whole_html13, 'lxml')
            table13 = soup13.find('table', attrs={'id': 'report'})
            data13 = []
            rows13 = table13.findAll('tr')
            for row in rows13:
                cols = row.findAll('td')
                cols = [ele.text.strip() for ele in cols]
                data13.append([ele for ele in cols if ele])

            whole_html14 = f14.read()
            soup14 = BeautifulSoup(whole_html14, 'lxml')
            table14 = soup14.find('table', attrs={'id': 'report'})
            data14 = []
            rows14 = table14.findAll('tr')
            for row in rows14:
                cols = row.findAll('td')
                cols = [ele.text.strip() for ele in cols]
                data14.append([ele for ele in cols if ele])

            whole_html15 = f15.read()
            soup15 = BeautifulSoup(whole_html15, 'lxml')
            table15 = soup15.find('table', attrs={'id': 'report'})
            data15 = []
            rows15 = table15.findAll('tr')
            for row in rows15:
                cols = row.findAll('td')
                cols = [ele.text.strip() for ele in cols]
                data15.append([ele for ele in cols if ele])

            d = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15]
            # initial stitch
            master_statement = data1
            # sequential stitch

            # z over 1 - 15 (15 channels)
            for z in range(0, 15, 1):

                # x over length of data1 (nb of statements)
                for x in range(0, len(d[z]), 1):

                    # y over length of data1[x] (nb of obj in statement)
                    for y in range(0, (len((d[z])[x])), 1):

                        if y == 0:
                            pass
                        else:
                            master_statement[x].append((d[z])[x][y])

            # for x in range(0, len(master_statement), 1):
            #     for x in range

            # for statement in master_statement:
            #     for s in statement:
            #         for ss in s:
            #             ss.strip("()")
            # print("stripped")

            # print(master_statement)
            # code sql migration
            # the creation of the table, title, base template
            # for g in master_statement:
            #     print(g)

            t = symbol + statement_rotation[a] + "master"
            create_table('sp500', t)
            # print("created: " + t)
            # # addition of data
            # # c = str(master_statement[0][0])
            # # print(type(master_statement[0][0]))
            new_col('sp500', t, 'time')

            for c in range(1, (len(master_statement[0])), 1):
                new_row('sp500', t, 'time', master_statement[0][c])

            # print('done')

            # s = re.sub(' ', '', master_statement[1][0])
            # print(s)
            # new_col('sp500', t, s)
            # new_col('testdb', 'tabletable', 'new_col')

            # testing...

            # unlock the rest of the symbols
            # run at max

        except FileNotFoundError:
            print('Not found')
            # pass
