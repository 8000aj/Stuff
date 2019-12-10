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

con = pymysql.connect(host="localhost",
                      user="jefferson",
                      passwd="1234",
                      db="testdb")


# BUILD LIST OF FILES
list_income_statement = []
list_balance_sheet_statement = []
list_cash_flow_statement = []
for n in range(1, ((len(symbols)) + 1), 1):
    for m in range(1, 16, 1):
    income_statement = (symbols[n]) + "_income_statement_" + (str(m))

    balance_sheet_statement = (symbols[n]) + "_balance_sheet_statement_" + (str(m))

    cash_flow_statement = (symbols[n]) + "_cash_flow_statement_" + (str(m))

    list_income_statement.append(income_statement)
    list_balance_sheet_statement.append(balance_sheet_statement)
    list_cash_flow_statement(cash_flow_statement)


# NOTES: WRAP THE SQL COMMANDS IN A FUNCTION. ITERATE THE FILE PATHS

TRANSMUTION
    HOW DO I SOLVE THE ISSUE OF MULTIPLE TITLE INSERTION?
    HOW DO I STACK THE DATA CORRECTLY?
        IF CHRONO AND NUMERICAL SYNC:
            IF TITLE HAS ONE, TITLE STATEMENT TRANSMUTE

MUST TEST ISOLATION..


CREATE SCHEMA

# def create_schema(schema_title):
#     with con.cursor() as cursor:
#         create_schema_command = "CREATE SCHEMA `" + schema_title + "` ;"
#         cursor.execute(create_schema_command)
# create_schema(**********************************)

CREATE TABLES OF SYMBOL
    INCOME STATEMENT
    BALANCE SHEET STATEMENT
    CASH FLOW STATEMENT

READ FILE
SCAN FILE
ISOLATE DATA
TRANSMUTE INTO MYSQL

ARE THE NUMERICAL TITLES CHRONOLOGICAL?


# filename =
# with open(filename) as f:
