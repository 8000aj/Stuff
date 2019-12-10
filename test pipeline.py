# SPY
#     SPY

# SP500
#     [509]
#         Price_Action
#                 TIME TIME TIME
#             High   #    #    #
#             Open   #    #    #
#             Low    #    #    #
#             Close  #    #    #

#         Income_Statement
#                 TIME TIME TIME
#             #   #    #    #
#             #   #    #    #
#         Cash_Flow_Statement
#                 TIME TIME TIME
#             #   #    #    #
#             #   #    #    #
#         Balance_Sheet
#                  TIME TIME TIME
#             #   #    #    #
#             #   #    #    #

# TABLE CREATION

# TABLE ADDITION

###

# INDEX INDEX INDEX
# schema creation
# table creation
# column cell title population
# row cell title population


# SCHEMA CREATION // TESTED, FUNCTION REQUIRES STRING
# def create_schema(schema_title):
#     with con.cursor() as cursor:
#         create_schema_command = "CREATE SCHEMA `" + schema_title + "` ;"
#         cursor.execute(create_schema_command)
# create_schema('schema_20191128')
# END OF SCHEMA CREATION

# TABLE CREATION //  // TESTED, FUNCTION REQUIRES TWO STRINGS
# def create_table(live_schema, table_title):
#     con = pymysql.connect(host="localhost",
#                           user="jefferson",
#                           passwd="1234",
#                           db=live_schema)
#     with con.cursor() as cursor:
#         create_table_command = "CREATE TABLE " + table_title + "(id INT       AUTO_INCREMENT PRIMARY KEY)"
#         cursor.execute(create_table_command)
# create_table('testdb', 'tabletable')
# END OF TABLE CREATION

# VALUE INSERTION INTO TABLE // UNABSTRACTED
#   COLUMN TITLE CREATION
# def new_col(live_schema, live_table, new_column):
#     con = pymysql.connect(host="localhost",
#                           user="jefferson",
#                           passwd="1234",
#                           db=live_schema)
#     with con.cursor() as cursor:
#         # create new columns
#         new_col_command = "ALTER TABLE " + live_table + " ADD " + new_column + " VARCHAR(100)"
#         cursor.execute(new_col_command)
# new_col('testdb', 'tabletable', 'new_col')
#   END OF COLUMN CREATION

#   ROW TITLE ADDITION
# def new_row(live_schema, live_table, live_column, title_row):
#     # def new_row(title_row):
#     con = pymysql.connect(host="localhost",
#                           user="jefferson",
#                           passwd="1234",
#                           db=live_schema)
#     with con.cursor() as cursor:
#         # create new rows
#         # ini = []
#         val = title_row
#         new_row_command = "INSERT INTO `" + live_table + "` (`" + live_column + "`) VALUES  (%s)"
#         # new_row_command_ini = "INSERT INTO `" + live_table + "` (`" + live_column + "`) VALUES (%s);"
#         # ini.append(new_row_command_ini)
#         # print(ini[0])
#         # new_row_command = "INSERT INTO `tabletable` (`Statement`)VALUES(%s)"
#         # test = "INSERT INTO `spy20190828` (`daydate`, `daytime`, `open_price`, `high_price`, `low_price`, `close_price`, `volume`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#         cursor.execute(new_row_command, val)
#         con.commit()


# new_row('testdb', 'tabletable', 'Statement', '555')
# END OF ROW CELL TITLE INSERTION
# END OF VALUE INSERTION INTO TABLE

# PLAN
# lOCALIZE THE PROGRAM WITH FILES
# CREATE LISTS OF ALL FILEPATHS
# ITERATE THROUGH THE LIST
# INTEGRATE ERROR CATCH FOR FILE NOT FOUND
# INTEGRATE PROGRESS VISUALIZATION
# SCAN FILE
# ISOLATE VALUES
# ENTER INTO MYSQL

# CREATE LISTS OF ALL FILEPATHS
# SYMBOLS
# symbols = ["AAPL","MSFT","AMZN","FB","XOM","JNJ","BRKB","JPM","GOOGL","GOOG","GE","WFC","BAC","T","PG","CVX","PFE","HD","VZ","CMCSA","INTC","MRK","V","PM","CSCO","KO","C","UNH","DIS","PEP","MO","IBM","ORCL","AMGN","MMM","MCD","MDT","WMT","MA","ABBV","BA","HON","SLB","CELG","PCLN","BMY","UNP","AVGO","UTX","SBUX","GILD","GS","USB","CVS","AGN","QCOM","TXN","COST","LLY","TWX","ABT","ACN","LOW","UPS","WBA","NKE","CHTR","DOW","MDLZ","DD","LMT","NFLX","ADBE","TMO","CB","CL","MS","NEE","NVDA","AXP","PNC","CAT","BIIB","COP","DUK","AIG","MET","CRM","GD","PYPL","AMT","RAI","KHC","SPG","EOG","TJX","MON","DHR","BK","SCHW","SO","D","CSX","ANTM","BLK","PRU","FDX","AET","OXY","RTN","GM","KMB","AMAT","ADP","F","ITW","NOC","BLKFDS","YHOO","SYK","CI","CME","COF","HAL","BDX","JCI","KMI","EMR","MMC","ESRX","CTSH","ATVI","BSX","ICE","LUV","PX","BBT","DAL","PSX","SPGI","ETN","NSC","PCG","TRV","CCI","EBAY","HUM","AEP","ECL","EQIX","GIS","DE","TGT","HPQ","AON","EXC","APD","ISRG","REGN","ALL","HPE","PSA","MAR","INTU","FOXA","STT","STZ","AFL","VRTX","WM","MCK","ALXN","VLO","EA","APC","MU","PXD","STI","PLD","PPG","SRE","ADI","ILMN","ZTS","FIS","BAX","KR","SHW","MPC","LYB","GLW","TEL","SYY","CCL","AVB","PPL","WDC","EIX","ROST","FISV","WMB","HCN","BHI","WY","CMI","MTB","LRCX","ED","ZBH","HCA","PCAR","DFS","CBS","ADM","EQR","DLPH","PGR","EW","IR","YUM","CAH","ORLY","XEL","SYF","AAL","VTR","PEG","BCR","ROP","APH","DXC","NWL","IP","PH","UAL","SWK","INCY","EL","KEY","DVN","AMP","AZO","ROK","MCO","SYMC","NTRS","OMC","DLTR","CXO","NUE","BXP","WEC","FTV","CERN","CFG","DG","SWKS","ES","DTE","PAYX","APA","FITB","HIG","RCL","ADSK","A","MNST","TSN","DLR","VFC","LVLT","PFG","NEM","TROW","K","WLTW","RF","MYL","ULTA","VMC","COL","CLX","EXPE","TAP","DPS","EFX","ESS","MCHP","MJN","VNO","FCX","O","KLAC","CAG","XLNX","RHT","MLM","HSY","LNC","DGX","BEN","SJM","XRAY","FTI","MHK","HCP","RSG","HBAN","LH","ADS","MSI","IDXX","CTL","BBY","AWK","USD","HSIC","ETR","WHR","WAT","VIAB","FOX","NBL","HRS","CMG","DISH","AME","NLSN","GPC","CTXS","ABC","WRK","HST","MTD","GGP","BLL","FAST","LLL","AEE","IVZ","L","CNC","NOV","FE","CMA","CMS","LB","HES","TXT","MRO","CHD","HOLX","STX","GPN","TDG","ALB","DOV","CNP","ARNC","COH","VRSK","MAS","COG","JNPR","EMN","WFM","XEC","MKC","HAS","SNPS","XL","MAA","OKE","DHI","UHS","IFF","CPB","KMX","DRI","NTAP","PNR","ALK","UNM","CBG","CINF","SLG","CTAS","AAP","CHRW","PRGO","GWW","DVA","CA","EQT","IT","LEN","FL","ARE","ETFC","WYN","COO","WYNN","UDR","TIF","RJF","LKQ","EXPD","HOG","AJG","FBHS","SNA","FRT","FMC","TSS","KSU","TSO","IPG","PNW","HRL","SCG","AKAM","REG","WU","EXR","URI","XYL","LNT","GT","AMG","M","SEE","QRVO","KIM","VAR","COTY","IRM","BFB","TMK","LUK","MOS","BWA","FFIV","TSCO","ZION","AMD","VRSN","NDAQ","PVH","JBHT","HBI","NI","AYI","AVY","CBOE","MAC","ALLE","AES","MAT","SRCL","FLR","LEG","NFX","KSS","EVHC","AIV","JEC","HP","FLS","PKI","SNI","PHM","SPLS","XRX","KORS","PBCT","CF","RHI","GRMN","AIZ","JWN","GPS","DISCK","BBBY","TGNA","PWR","HRB","TRIP","FLIR","RRC","NWSA","NRG","MNK","SIG","RL","NAVI","CHK","CSRA","RIG","MUR","DISCA","TDC","UAA","PDCO","R","UA","AN","UBFUT","NWS","ESM"]
import pymysql.cursors
from bs4 import BeautifulSoup

# con = pymysql.connect(host="localhost",
#                       user="jefferson",
#                       passwd="1234",
#                       db="testdb")


# BUILD LIST OF FILES
# list_income_statement = []
# list_balance_sheet_statement = []
# list_cash_flow_statement = []
# for n in range(1, ((len(symbols)) + 1), 1):
#     for m in range(1, 16, 1):
#     income_statement = (symbols[n]) + "_income_statement_" + (str(m))

#     balance_sheet_statement = (symbols[n]) + "_balance_sheet_statement_" + (str(m))

#     cash_flow_statement = (symbols[n]) + "_cash_flow_statement_" + (str(m))

#     list_income_statement.append(income_statement)
#     list_balance_sheet_statement.append(balance_sheet_statement)
#     list_cash_flow_statement(cash_flow_statement)


# NOTES: WRAP THE SQL COMMANDS IN A FUNCTION. ITERATE THE FILE PATHS

# TRANSMUTION
#     HOW DO I SOLVE THE ISSUE OF MULTIPLE TITLE INSERTION?
#     HOW DO I STACK THE DATA CORRECTLY?
#         IF CHRONO AND NUMERICAL SYNC:
#             IF TITLE HAS ONE, TITLE STATEMENT TRANSMUTE

# MUST TEST ISOLATION..
# SOLUTION TO STITCH:
# read all related files individually
# create stiched file


# CREATE SCHEMA

# def create_schema(schema_title):
#     with con.cursor() as cursor:
#         create_schema_command = "CREATE SCHEMA `" + schema_title + "` ;"
#         cursor.execute(create_schema_command)
# create_schema(**********************************)

# CREATE TABLES OF SYMBOL
#     INCOME STATEMENT
#     BALANCE SHEET STATEMENT
#     CASH FLOW STATEMENT

# READ FILE
# SCAN FILE
# ISOLATE DATA
# TRANSMUTE INTO MYSQL

# ARE THE NUMERICAL TITLES CHRONOLOGICAL?
# NO, INVERTED. _1 = PRESENT _2 = PAST

# FLOAT

# AAPL_CFS1 = 'AAPL_cash_flow_statement_1.html'
# AAPL_CFS2 = 'AAPL_cash_flow_statement_2.html'
# AAPL_IS1 = 'AAPL_income_statement_1.html'
# AAPL_IS2 = 'AAPL_income_statement_2.html'
# AAPL_BS1 = 'AAPL_balance_sheet_1.html'
# AAPL_BS2 = 'AAPL_balance_sheet_2.html'
# with open(AAPL_CFS2, 'r') as f:

#     # whole html file
#     whole_html = f.read()
#     soup = BeautifulSoup(whole_html, 'lxml')  # type: bs
#     soupp = soup.prettify()  # type: string
#     # print(soupp)

#     # ISOLATION; left to right, future to past
#     # this pulls the whole table; need to isolate further
#     table = soup.find('table', attrs={'id': 'report'})
#     data = []

#     rows = table.findAll('tr')
#     for row in rows:
#         cols = row.findAll('td')
#         cols = [ele.text.strip() for ele in cols]
#         data.append([ele for ele in cols if ele])  # gets rid of empty values

#     # print(table.td.next_sibling.next_sibling.next_sibling.next_sibling.text)
#     print('AAPL CFS2')
#     for x in data:
#         print(x)

MSFT_CFS1 = 'MSFT_cash_flow_statement_1.html'
MSFT_CFS2 = 'MSFT_cash_flow_statement_2.html'
MSFT_CFS12 = 'MSFT_cash_flow_statement_12.html'
MSFT_CFS13 = 'MSFT_cash_flow_statement_13.html'

MSFT_IS1 = 'MSFT_income_statement_1.html'
MSFT_IS2 = 'MSFT_income_statement_2.html'
MSFT_BS1 = 'MSFT_balance_sheet_1.html'
MSFT_BS2 = 'MSFT_balance_sheet_2.html'


try:

    # should it be so brute? is there a better way? cycle the data, appending to master?
    f1 = open(MSFT_CFS12)
    f2 = open(MSFT_CFS13)
    # f2 = open(MSFT_CFS1)
    # f4 = open(MSFT_CFS1)
    # f5 = open(MSFT_CFS1)
    # f6 = open(MSFT_CFS1)
    # f7 = open(MSFT_CFS1)
    # f8 = open(MSFT_CFS1)
    # f9 = open(MSFT_CFS1)
    # f10 = open(MSFT_CFS1)
    # f11 = open(MSFT_CFS1)
    # f12 = open(MSFT_CFS1)
    # f13 = open(MSFT_CFS1)
    # f14 = open(MSFT_CFS1)

    # whole html file
    whole_html1 = f1.read()
    soup1 = BeautifulSoup(whole_html1, 'lxml')  # type: bs
    # soupp = soup.prettify()  # type: string
    # print(soupp)

    # ISOLATION; left to right, future to past
    # this pulls the whole table; need to isolate further
    table = soup1.find('table', attrs={'id': 'report'})
    data1 = []
    rows = table.findAll('tr')
    for row in rows:
        cols = row.findAll('td')
        cols = [ele.text.strip() for ele in cols]
        data1.append([ele for ele in cols if ele])  # gets rid of empty values

    # whole html file
    whole_html2 = f2.read()
    soup2 = BeautifulSoup(whole_html2, 'lxml')  # type: bs
    # soupp = soup.prettify()  # type: string
    # print(soupp)

    # ISOLATION; left to right, future to past
    # this pulls the whole table; need to isolate further
    table = soup2.find('table', attrs={'id': 'report'})
    data2 = []
    rows = table.findAll('tr')
    for row in rows:
        cols = row.findAll('td')
        cols = [ele.text.strip() for ele in cols]
        data2.append([ele for ele in cols if ele])  # gets rid of empty values

    # print('MSFT CFS1')
    # for x in data1:
    #     print(x)

    # NOW BUILD STICHED FILE
    # IMPORT FILE ONE ~
    # IMPORT FILE TWO ~
    # ERROR EXCEPTION HANDLING ~
    # MASTER LIST CREATION
    # INITIAL APPENDAGE
    # SEQUENTIAL APPENDAGE

    # msft_cfs_master = [[]]
    # msft_cfs_master.append(data1)
    # msft_cfs_master.append(data2[0][1])
    # # running into an issue of sequential stacking

    # for x in msft_cfs_master:
    #     print(x)

    # cfs1
    # append to master
    # 00 01 02 03 04 05 06 07 08 09 010
    # then
    # cfs2
    # append to master
    # 01 02 03 04 05 06 07 08 09 010
    # .. so on so forth how to make dynamic?

    #####

    list contains url paths(or a function of the paths)
    feed list into function
    fx looks at length(nb of items)
    fx allocates titled memory channels according to(nb of items)
    fx isolates the tabled data from .html file(html to list obj)
    data is now allocated into its proper memory channel
    every memory channel gets compared(statements, dates)
    print analysis(identical or non - identical)
    if identical print identical
        proceed with stitching
    else print non - identical
        break

    def master_mk1(list_mk1):
        len_list = len(list_mk1)
        listOfLists = [[] for i in range(len_list)]


except FileNotFoundError:
    print('Not found')

    # print('data[3][1]')
    # print(data[3][1])
    # out of range error exception handling
    # https://stackoverflow.com/questions/11902458/i-want-to-exception-handle-list-index-out-of-range/11902480
    # TESTING ISOLATION:
    # [0][0] # dataset title
    # [0][1 + n] # dates, inverted. higher n equals further in the past
    # [1][0] # net income title
    # [1][1 + n] # values of net income, associated with dates

    # could flip the tables after import. for left to right, chronological

    # print('type(data[3][0])')
    # print(type(data[3][0])) # STR

    # print('type(data[3]')
    # print(type(data[3])) # LIST

    # print('type(data)')
    # print(type(data)) # LIST


# ALTER TABLE `sp500_options`.`aapl c 06dec 19 270.00`
# ADD COLUMN `info` VARCHAR(45) NULL AFTER `id`,
# ADD COLUMN `25oct 19` VARCHAR(45) NULL AFTER `info`,
# ADD COLUMN `28oct 19` VARCHAR(45) NULL AFTER `25oct 19`,
# ADD COLUMN `29oct 19` VARCHAR(45) NULL AFTER `28oct 19`,
# ADD COLUMN `30oct 19` VARCHAR(45) NULL AFTER `29oct 19`,
# ADD COLUMN `31oct 19` VARCHAR(45) NULL AFTER `30oct 19`,
# ADD COLUMN `01nov 19` VARCHAR(45) NULL AFTER `31oct 19`,
# ADD COLUMN `04nov 19` VARCHAR(45) NULL AFTER `01nov 19`,
# ADD COLUMN `05nov 19` VARCHAR(45) NULL AFTER `04nov 19`,
# ADD COLUMN `06nov 19` VARCHAR(45) NULL AFTER `05nov 19`,
# ADD COLUMN `07nov 19` VARCHAR(45) NULL AFTER `06nov 19`,
# ADD COLUMN `08nov 19` VARCHAR(45) NULL AFTER `07nov 19`,
# ADD COLUMN `11nov 19` VARCHAR(45) NULL AFTER `08nov 19`,
# ADD COLUMN `12nov 19` VARCHAR(45) NULL AFTER `11nov 19`,
# ADD COLUMN `13nov 19` VARCHAR(45) NULL AFTER `12nov 19`,
# ADD COLUMN `14nov 19` VARCHAR(45) NULL AFTER `13nov 19`,
# ADD COLUMN `15nov 19` VARCHAR(45) NULL AFTER `14nov 19`,
# ADD COLUMN `18nov 19` VARCHAR(45) NULL AFTER `15nov 19`,
# ADD COLUMN `19nov 19` VARCHAR(45) NULL AFTER `18nov 19`,
# ADD COLUMN `20nov 19` VARCHAR(45) NULL AFTER `19nov 19`,
# ADD COLUMN `21nov 19` VARCHAR(45) NULL AFTER `20nov 19`,
# ADD COLUMN `22nov 19` VARCHAR(45) NULL AFTER `21nov 19`,
# ADD COLUMN `25nov 19` VARCHAR(45) NULL AFTER `22nov 19`,
# ADD COLUMN `26nov 19` VARCHAR(45) NULL AFTER `25nov 19`,
# ADD COLUMN `27nov 19` VARCHAR(45) NULL AFTER `26nov 19`,
# ADD COLUMN `29nov 19` VARCHAR(45) NULL AFTER `27nov 19`,
# ADD COLUMN `02dec 19` VARCHAR(45) NULL AFTER `29nov 19`,
# ADD COLUMN `03dec 19` VARCHAR(45) NULL AFTER `02dec 19`,
# ADD COLUMN `04dec 19` VARCHAR(45) NULL AFTER `03dec 19`,
# ADD COLUMN `05dec 19` VARCHAR(45) NULL AFTER `04dec 19`,
# ADD COLUMN `06dec 19` VARCHAR(45) NULL AFTER `05dec 19`;


# INSERT INTO `sp500_options`.`aapl c 06dec 19 270.00` (`info`, `25oct 19`, `28oct 19`, `29oct 19`, `30oct 19`, `31oct 19`, `01nov 19`, `04nov 19`, `05nov 19`, `06nov 19`, `07nov 19`, `08nov 19`, `11nov 19`, `12nov 19`, `13nov 19`, `14nov 19`, `15nov 19`, `18nov 19`, `19nov 19`, `20nov 19`, `21nov 19`, `22nov 19`, `25nov 19`, `26nov 19`, `27nov 19`, `29nov 19`, `02dec 19`, `03dec 19`, `04dec 19`, `05dec 19`, `06dec 19`) VALUES ('open', '0.69', '1.1', '1.39', '1.02', '0.75', '0.84', '1.85', '1.47', '1.24', '1.48', '1.31', '1.23', '1.85', '1.65', '2.46', '2.45', '2.47', '3.2', '2.35', '1.98', '1.73', '1.22', '1.9', '1.18', '1.03', '1.37', '0.08', '0.15', '0.09', '0.01');
# INSERT INTO `sp500_options`.`aapl c 06dec 19 270.00` (`info`, `25oct 19`, `28oct 19`, `29oct 19`, `30oct 19`, `31oct 19`, `01nov 19`, `04nov 19`, `05nov 19`, `06nov 19`, `07nov 19`, `08nov 19`, `11nov 19`, `12nov 19`, `13nov 19`, `14nov 19`, `15nov 19`, `18nov 19`, `19nov 19`, `20nov 19`, `21nov 19`, `22nov 19`, `25nov 19`, `26nov 19`, `27nov 19`, `29nov 19`, `02dec 19`, `03dec 19`, `04dec 19`, `05dec 19`, `06dec 19`) VALUES ('high', '0.9', '1.28', '1.39', '1.28', '0.75', '1.49', '1.85', '1.7', '1.25', '1.75', '1.53', '2.07', '1.94', '2.76', '2.79', '2.65', '3.18', '3.2', '2.57', '2.08', '1.75', '1.78', '1.95', '1.79', '1.75', '1.65', '0.2', '0.15', '0.17', '1.27');
# INSERT INTO `sp500_options`.`aapl c 06dec 19 270.00` (`info`, `25oct 19`, `28oct 19`, `29oct 19`, `30oct 19`, `31oct 19`, `01nov 19`, `04nov 19`, `05nov 19`, `06nov 19`, `07nov 19`, `08nov 19`, `11nov 19`, `12nov 19`, `13nov 19`, `14nov 19`, `15nov 19`, `18nov 19`, `19nov 19`, `20nov 19`, `21nov 19`, `22nov 19`, `25nov 19`, `26nov 19`, `27nov 19`, `29nov 19`, `02dec 19`, `03dec 19`, `04dec 19`, `05dec 19`, `06dec 19`) VALUES ('low', '0.69', '1.1', '0.7', '0.88', '0.52', '0.84', '1.4', '1.47', '0.95', '1.29', '1.05', '1.17', '1.63', '1.65', '1.87', '2.07', '2.25', '2.53', '1.35', '1.49', '0.96', '1.15', '1', '1.1', '1.03', '0.54', '0.08', '0.07', '0.05', '0.01');
# INSERT INTO `sp500_options`.`aapl c 06dec 19 270.00` (`info`, `25oct 19`, `28oct 19`, `29oct 19`, `30oct 19`, `31oct 19`, `01nov 19`, `04nov 19`, `05nov 19`, `06nov 19`, `07nov 19`, `08nov 19`, `11nov 19`, `12nov 19`, `13nov 19`, `14nov 19`, `15nov 19`, `18nov 19`, `19nov 19`, `20nov 19`, `21nov 19`, `22nov 19`, `25nov 19`, `26nov 19`, `27nov 19`, `29nov 19`, `02dec 19`, `03dec 19`, `04dec 19`, `05dec 19`, `06dec 19`) VALUES ('close', '0.88', '1.28', '0.99', '1.14', '0.59', '1.49', '1.68', '1.48', '1.04', '1.29', '1.52', '1.91', '1.75', '2.68', '1.96', '2.65', '3', '2.7', '1.8', '1.61', '1.15', '1.76', '1', '1.79', '1.53', '0.54', '0.11', '0.07', '0.08', '0.67');
# INSERT INTO `sp500_options`.`aapl c 06dec 19 270.00` (`info`, `25oct 19`, `28oct 19`, `29oct 19`, `30oct 19`, `31oct 19`, `01nov 19`, `04nov 19`, `05nov 19`, `06nov 19`, `07nov 19`, `08nov 19`, `11nov 19`, `12nov 19`, `13nov 19`, `14nov 19`, `15nov 19`, `18nov 19`, `19nov 19`, `20nov 19`, `21nov 19`, `22nov 19`, `25nov 19`, `26nov 19`, `27nov 19`, `29nov 19`, `02dec 19`, `03dec 19`, `04dec 19`, `05dec 19`, `06dec 19`) VALUES ('volume', '71', '52', '287', '99', '65', '195', '147', '134', '99', '149', '141', '347', '260', '909', '382', '1264', '1471', '1801', '1837', '1391', '1299', '5061', '4759', '6680', '9291', '21652', '15387', '5351', '14631', '80000');
