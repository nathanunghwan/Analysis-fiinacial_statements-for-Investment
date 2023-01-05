import requests
import pandas as pd
import pymysql
import datetime
from dateutil.relativedelta import relativedelta

def connect_db():
    return pymysql.connect(host='localhost', user='root', password='******', db='USASTOCK', charset='utf8')
'''
conn = connect_db()
curs = conn.cursor()
sql = "SELECT DISTINCT STOCK_CODE FROM USA_STOCK_INFO"
curs.execute(sql)
stock_list = [item[0] for item in curs.fetchall()]

conn.commit()
conn.close()
len(stock_list)
print(stock_list)
'''
import csv
stock_list =  ["A", "AA", "AAC", "AACG", "AACI", "AADI", "AAIC", "AAL", "AAME", "AAN", "AAOI", "AAON", "AAP", "AAPL", "AAQC",
              "AAT", "AATC", "AAU", "AAWW", "AB", "ABB", "ABBV", "ABC", "ABCB", "ABCL", "ABCM", "ABEO", "ABEV", "ABG", "ABGI",
              "ABIO", "ABM", "ABMD", "ABNB", "ABOS", "ABR", "ABSI", "ABST", "ABT", "ABTX", "ABUS", "ABVC", "AC", "ACA", "ACAD",
              "ACAH", "ACB", "ACBI", "ACC", "ACCD", "ACCO", "ACEL", "ACER", "ACET", "ACEV", "ACGL", "ACH", "ACHC", "ACHL",
              "ACHR", "ACHV", "ACI", "ACII", "ACIU", "ACIW", "ACLS", "ACM", "ACMR", "ACN", "ACNB", "ACOR", "ACQR", "ACR",
              "ACRE", "ACRO", "ACRS", "ACRX", "ACST", "ACT", "ACTD", "ACTG", "ACU", "ACVA", "ACXP", "ACY", "ADAG", "ADAP",
              "ADBE", "ADC", "ADCT", "ADER", "ADES", "ADEX", "ADF", "ADGI", "ADI", "ADIL", "ADM", "ADMA", "ADMP",
              "ADN", "ADNT", "ADOC", "ADP", "ADPT", "ADRA", "ADS", "ADSK", "ADT", "ADTN", "ADTX", "ADUS", "ADV",
              "ADVM", "ADXN", "ADXS", "AE", "AEAC", "AEE", "AEG", "AEHA", "AEHL", "AEHR", "AEI", "AEIS", "AEL", "AEM", "AEMD",
              "AENZ", "AEO", "AEP", "AER", "AERC", "AERI", "AES", "AESE", "AEVA", "AEY", "AEYE", "AEZS", "AFAQ", "AFBI", "AFCG",
              "AFG", "AFI", "AFIB", "AFIN", "AFL", "AFMD", "AFRM", "AFTR", "AFYA", "AG", "AGAC", "AGBA", "AGCB", "AGCO", "AGE",
              "AGEN", "AGFS", "AGFY", "AGGR", "AGI", "AGIL", "AGIO", "AGL", "AGLE", "AGM", "AGMH", "AGNC", "AGO", "AGR", "AGRI",
              "AGRO", "AGRX", "AGS", "AGTC", "AGTI", "AGX", "AGYS", "AHCO", "AHH", "AHI", "AHPA", "AHPI", "AHT", "AI", "AIG", "AIH",
              "AIHS", "AIKI", "AIM", "AIMC", "AIN", "AINC", "AINV", "AIP", "AIR", "AIRC", "AIRG","AIRI", "AIRS", "AIRT", "AIT", "AIV",
              "AIZ", "AJG", "AJRD", "AJX", "AKA", "AKAM", "AKBA", "AKIC", "AKO-A", "AKR", "AKRO", "AKTS", "AKTX", "AKU", "AKUS",
              "AKYA", "AL", "ALAC", "ALB", "ALBO", "ALC", "ALCC", "ALCO", "ALDX", "ALE", "ALEC", "ALEX", "ALF", "ALG", "ALGM",
              "ALGN", "ALGS", "ALGT", "ALHC", "ALIM", "ALIT", "ALJJ", "ALK", "ALKS", "ALKT", "ALL", "ALLE", "ALLK", "ALLO", "ALLT",
              "ALLY", "ALNA", "ALNY", "ALOT", "ALPA", "ALPN", "ALPP", "ALRM", "ALRN", "ALRS", "ALSN", "ALT", "ALTG", "ALTM", "ALTO",
              "ALTR", "ALTU", "ALV", "ALVR", "ALX", "ALXO", "ALYA", "ALZN", "AM", "AMAL", "AMAM", "AMAO", "AMAT", "AMBA", "AMBC",
              "AMBO", "AMBP", "AMC", "AMCI", "AMCR", "AMCX", "AMD", "AME", "AMED", "AMEH", "AMG", "AMGN", "AMH", "AMK", "AMKR",
              "AMN", "AMNB", "AMOT", "AMOV", "AMP", "AMPE", "AMPG", "AMPH", "AMPI", "AMPL", "AMPY", "AMR", "AMRC", "AMRK", "AMRN",
              "AMRS", "AMRX", "AMS", "AMSC", "AMSF", "AMST", "AMSWA", "AMT", "AMTB", "AMTI", "AMTX", "AMWD", "AMWL", "AMX", "AMYT",
              "AMZN", "AN", "ANAB", "ANAC", "ANAT", "ANDE", "ANEB", "ANET", "ANF", "ANGI", "ANGN", "ANGO", "ANIK", "ANIP", "ANIX",
              "ANNX", "ANPC", "ANSS", "ANTE", "ANTM", "ANVS", "ANY", "ANZU", "AOMR", "AON", "AOS", "AOSL", "AOUT", "AP", "APA", "APAC",
              "APAM", "APD", "APDN", "APEI", "APEN", "APG", "APGB", "APH", "API", "APLE", "APLS", "APLT", "APM", "APMI", "APO", "APOG",
              "APP", "APPF", "APPH", "APPN", "APPS", "APR", "APRE", "APRN", "APSG", "APT", "APTM", "APTO", "APTV", "APTX", "APVO", "APWC",
              "APYX", "AQB", "AQMS", "AQN", "AQST", "AQUA", "AR", "ARAV", "ARAY", "ARBE", "ARBG", "ARBK", "ARC", "ARCB", "ARCC", "ARCE",
              "ARCH", "ARCO", "ARCT", "ARDS", "ARDX", "ARE", "AREC", "ARES", "ARGO", "ARGU", "ARGX", "ARHS", "ARI", "ARIS", "ARKO",
              "ARKR", "ARL", "ARLO", "ARLP", "ARMK", "ARMP", "ARNA", "ARNC", "AROC", "AROW", "ARQQ", "ARQT", "ARR", "ARRW", "ARRY",
              "ARTA", "ARTE", "ARTL", "ARTNA", "ARTW", "ARVL", "ARVN", "ARW", "ARWR", "ARYD", "ARYE", "ASA", "ASAI", "ASAN", "ASAQ",
              "ASAX", "ASB", "ASC", "ASGN", "ASH", "ASIX", "ASLE", "ASLN", "ASM", "ASMB", "ASML", "ASND", "ASO", "ASPA", "ASPC", "ASPN",
              "ASPS", "ASPU", "ASR", "ASRT", "ASRV", "ASTC", "ASTE", "ASTL", "ASTR", "ASTS", "ASUR", "ASX", "ASXC", "ASYS", "ASZ", "ATA",
              "ATAI", "ATAQ", "ATAX", "ATC", "ATCO", "ATCX", "ATEC", "ATEN", "ATER", "ATEX", "ATGE", "ATH", "ATHA", "ATHE", "ATHM", "ATHN",
              "ATHX", "ATI", "ATIF", "ATIP", "ATKR", "ATLC", "ATLO", "ATMR", "ATNF", "ATNI", "ATNM", "ATNX", "ATO", "ATOM", "ATOS", "ATR",
              "ATRA", "ATRC", "ATRI", "ATRO", "ATRS", "ATSG", "ATTO", "ATUS", "ATVC", "ATVI", "ATXI", "ATXS", "ATY", "AU", "AUB", "AUBN",
              "AUD", "AUDC", "AUGX", "AUID", "AUMN", "AUPH", "AUR", "AURA", "AURC", "AUS", "AUTL", "AUTO", "AUUD", "AUVI", "AUY", "AVA", "AVAH",
              "AVAN", "AVAV", "AVB", "AVCO", "AVCT", "AVD", "AVDL", "AVDX", "AVEO", "AVGO", "AVGR", "AVHI", "AVID", "AVIR", "AVLR", "AVNS",
              "AVNT", "AVNW", "AVO", "AVPT", "AVRO", "AVT", "AVTE", "AVTR", "AVTX", "AVXL", "AVY", "AVYA", "AWH", "AWI", "AWK", "AWR", "AWRE",
              "AWX", "AX", "AXDX", "AXGN", "AXL", "AXLA", "AXNX", "AXON", "AXP", "AXR", "AXS", "AXSM", "AXTA", "AXTI", "AXU", "AY", "AYI", "AYLA",
              "AYRO", "AYTU", "AYX","AZEK", "AZN", "AZO", "AZPN", "AZRE", "AZTA", "AZYO", "AZZ", "B", "BA", "BABA", "BAC", "BACA", "BAFN",
              "BAH", "BAK", "BALY", "BAM", "BAMR", "BANC", "BAND", "BANF", "BANR", "BANX", "BAOS", "BAP", "BARK", "BASE", "BATL", "BATRA",
              "BATRK", "BAX", "BB", "BBAR", "BBBY", "BBCP", "BBD", "BBDC", "BBDO", "BBGI", "BBI", "BBIG", "BBIO", "BBL", "BBLG", "BBLN",
              "BBN", "BBQ", "BBSI", "BBU", "BBVA", "BBW", "BBWI", "BBY", "BC", "BCAB", "BCAC", "BCAT", "BCBP", "BCC", "BCDA", "BCE", "BCEL",
              "BCH", "BCLI", "BCML", "BCO", "BCOR", "BCOV", "BCOW", "BCPC", "BCRX", "BCS", "BCSF", "BCTX", "BCX", "BCYC", "BDC", "BDJ", "BDL",
              "BDN", "BDR", "BDSI", "BDSX", "BDTX", "BDX", "BE", "BEAM", "BEAT", "BECN", "BEDU", "BEEM", "BEKE", "BELFA", "BELFB", "BEN", "BENE",
              "BEP", "BEPC", "BERY", "BEST", "BF-A", "BFAM", "BFC", "BFI", "BFIN", "BFK", "BFLY", "BFRA", "BFRI", "BFS", "BFST", "BFZ", "BG", "BGCP",
              "BGFV", "BGI", "BGIO", "BGNE", "BGR", "BGRY", "BGS", "BGSF", "BGSX", "BGT", "BGY", "BH", "BHAC", "BHAT", "BHB", "BHC", "BHE", "BHF", "BHG",
              "BHIL", "BHK", "BHLB", "BHP", "BHR", "BHSE", "BHTG", "BHV", "BHVN", "BIDU", "BIG", "BIGC", "BIIB", "BILI", "BILL", "BIMI", "BIO", "BIO-B",
              "BIOC", "BIOL", "BIOT", "BIOX", "BIP", "BIPC", "BIRD", "BIT", "BITE", "BITF", "BIVI", "BJ", "BJDX", "BJRI", "BK", "BKCC", "BKD", "BKE",
              "BKEP", "BKH", "BKI", "BKKT", "BKN", "BKNG", "BKR", "BKSC", "BKSY", "BKT", "BKTI", "BKU", "BKYI", "BL", "BLBD", "BLBX", "BLCM", "BLCT",
              "BLD", "BLDE", "BLDP", "BLDR", "BLE", "BLFS", "BLFY", "BLI", "BLIN", "BLK", "BLKB", "BLL","BLMN", "BLND", "BLNG", "BLNK", "BLPH", "BLRX",
              "BLSA", "BLTS", "BLU", "BLUA", "BLUE", "BLW", "BLX", "BLZE", "BMA", "BMAQ", "BMBL", "BME", "BMEA", "BMEZ", "BMI", "BMO", "BMRA", "BMRC",
              "BMRN", "BMTC", "BMTX", "BMY", "BNED", "BNFT", "BNGO", "BNIX", "BNL", "BNNR", "BNR", "BNS", "BNSO", "BNTC", "BNTX", "BNY", "BOAC", "BOAS",
              "BODY", "BOE", "BOH", "BOKF", "BOLT", "BOMN", "BON", "BOOM", "BOOT", "BORR", "BOSC", "BOTJ", "BOX", "BOXL", "BP", "BPMC", "BPMP", "BPOP",
              "BPRN", "BPT", "BPTH", "BPTS", "BQ", "BR", "BRAG", "BRBR", "BRBS", "BRC", "BRCN", "BRDG", "BRDS", "BREZ", "BRFS", "BRG", "BRID", "BRIV",
              "BRK-A", "BRKL", "BRKR", "BRLI", "BRLT", "BRMK", "BRN", "BRO", "BROG", "BROS", "BRP", "BRPM", "BRQS", "BRSP", "BRT", "BRTX", "BRX", "BRY",
              "BRZE", "BSAC", "BSAQ", "BSBK", "BSBR", "BSET", "BSFC", "BSGA", "BSGM", "BSIG", "BSKY", "BSM", "BSMX", "BSN", "BSQR", "BSRR", "BST", "BSTZ",
              "BSVN", "BSX", "BSY", "BTA", "BTAI", "BTAQ", "BTAQU", "BTB", "BTBD", "BTBT", "BTCM", "BTCS", "BTCY", "BTG", "BTI", "BTN", "BTNB", "BTRS",
              "BTT", "BTTR", "BTTX", "BTU", "BTWN", "BTX", "BTZ", "BUD", "BUI", "BUR", "BURL", "BUSE", "BV", "BVH", "BVN", "BVS", "BVXV", "BW", "BWA",
              "BWAC", "BWAY", "BWB", "BWC", "BWEN", "BWFG", "BWMN", "BWMX", "BWXT", "BX", "BXC", "BXMT", "BXP", "BXRX", "BY", "BYD", "BYFC", "BYM",
              "BYND", "BYRN", "BYSI", "BYTS", "BZ", "BZH", "BZUN", "C", "CAAP", "CAAS", "CABA", "CABO", "CAC", "CACC", "CACI", "CADE", "CADL", "CAE",
              "CAG", "CAH", "CAJ", "CAKE", "CAL", "CALA", "CALB", "CALM", "CALT", "CALX", "CAMP", "CAMT", "CAN","CANF", "CANG", "CANO", "CAPL", "CAPR",
              "CAR", "CARA", "CARE", "CARG", "CARR", "CARS", "CARV", "CAS", "CASA", "CASH", "CASI", "CASS", "CASY", "CAT", "CATC", "CATO", "CATY",
              "CB", "CBAH", "CBAN", "CBAT", "CBAY", "CBD", "CBFV", "CBIO", "CBL", "CBNK", "CBOE", "CBRE", "CBRL", "CBSH", "CBT", "CBTX", "CBU", "CBZ",
              "CC", "CCAC", "CCAI", "CCAP", "CCB", "CCBG", "CCCC", "CCCS", "CCEL", "CCEP", "CCF", "CCI", "CCJ", "CCK", "CCL", "CCLP", "CCM", "CCMP",
              "CCNC", "CCNE", "CCO", "CCOI", "CCRN", "CCS", "CCSI", "CCU", "CCV", "CCVI", "CCXI", "CD", "CDAK", "CDAY", "CDE", "CDEV", "CDK", "CDLX",
              "CDMO", "CDNA", "CDNS", "CDOR", "CDR", "CDRE", "CDTX", "CDW", "CDXC", "CDXS", "CDZI", "CE", "CEA", "CECE", "CEI", "CEIX", "CELC", "CELH",
              "CELP", "CELU", "CEMI", "CENQ", "CENT", "CENTA", "CENX", "CEPU", "CEQP", "CERE", "CERN", "CERS", "CERT", "CET", "CETX", "CEV", "CEVA",
              "CF", "CFB", "CFBK", "CFFE", "CFFI", "CFFN", "CFG", "CFIV", "CFLT", "CFMS", "CFR", "CFRX", "CFV", "CFVI", "CFX", "CG", "CGA", "CGAU",
              "CGBD", "CGC", "CGEM", "CGEN", "CGNT", "CGNX", "CGRN", "CGTX", "CHAA", "CHCI", "CHCO", "CHCT", "CHD", "CHDN", "CHE", "CHEF", "CHEK",
              "CHGG", "CHH", "CHK", "CHKP", "CHMG", "CHMI", "CHNG", "CHNR", "CHPM", "CHPT", "CHRA", "CHRS", "CHRW", "CHS", "CHT", "CHTR", "CHUY",
              "CHWA", "CHWY", "CHX", "CI", "CIA", "CIAN", "CIB", "CIDM", "CIEN", "CIFR", "CIG", "CIGI", "CIH", "CIIG", "CIM", "CINF", "CINR", "CINT",
              "CIO", "CION", "CIR", "CIT", "CIVB", "CIVI", "CIX", "CIXX", "CIZN", "CJJD", "CKPT", "CKX", "CL", "CLAA", "CLAR", "CLAS", "CLAY", "CLB",
              "CLBK","CLBR", "CLBS", "CLBT", "CLDT", "CLDX", "CLEU", "CLF", "CLFD", "CLGN", "CLH", "CLI", "CLIM", "CLIR", "CLLS", "CLMT", "CLNE", "CLNN",
              "CLOE", "CLOV", "CLPR", "CLPS", "CLPT", "CLR", "CLRB", "CLRM", "CLRO", "CLS", "CLSD", "CLSK", "CLSN", "CLST", "CLVR", "CLVS", "CLVT", "CLW",
              "CLWT", "CLX", "CLXT", "CM", "CMA", "CMAX", "CMBM", "CMC", "CMCL", "CMCM", "CMCO", "CMCSA", "CMCT", "CME", "CMG", "CMI", "CMLS", "CMLT", "CMMB",
              "CMP", "CMPI", "CMPR", "CMPS", "CMPX", "CMRE", "CMRX", "CMS", "CMT", "CMTG", "CMTL", "CMU", "CNA", "CNC", "CNCE", "CND", "CNDA", "CNDT", "CNET",
              "CNEY", "CNF", "CNFR", "CNHI", "CNI", "CNK", "CNM", "CNMD", "CNNB", "CNNE", "CNO", "CNOB", "CNP", "CNQ", "CNR", "CNS", "CNSL", "CNSP", "CNTA",
              "CNTB", "CNTG", "CNTQ", "CNTX", "CNTY", "CNVY", "CNX", "CNXC", "CNXN", "CO", "COCO", "COCP", "CODA", "CODI", "CODX", "COE", "COF", "COFS", "COGT",
              "COHN", "COHR", "COHU", "COIN", "COKE", "COLB", "COLD", "COLI", "COLL", "COLM", "COMM", "COMP", "COMS", "CONE", "CONN", "CONX", "COO", "COOK", "COOL",
              "COOP", "COP", "COR", "CORR", "CORS", "CORT", "COST", "COTY", "COUP", "COUR", "COVA", "COWN", "CP", "CPA", "CPAA", "CPAC", "CPAR", "CPB", "CPE", "CPF",
              "CPG", "CPHC", "CPHI", "CPIX", "CPK", "CPLG", "CPLP", "CPNG", "CPOP", "CPRI", "CPRT", "CPRX", "CPS", "CPSH", "CPSI", "CPSR", "CPSS", "CPT",
              "CPTK", "CPUH", "CPZ", "CQP", "CR", "CRAI", "CRBP", "CRBU", "CRC", "CRCT", "CRD-A", "CRDF", "CRDL", "CREG", "CRESY", "CREX", "CRH",
              "CRHC", "CRI", "CRIS", "CRK", "CRKN", "CRL", "CRM", "CRMD", "CRMT", "CRNC", "CRNT", "CRNX", "CRON", "CROX","CRSP", "CRSR", "CRT", "CRTD",
              "CRTO", "CRTX", "CRU", "CRUS", "CRVL", "CRVS", "CRWD", "CRWS", "CRXT", "CRY", "CRZN", "CS", "CSAN", "CSBR", "CSCO",
              "CSCW", "CSGP", "CSGS", "CSII", "CSIQ", "CSL", "CSLT", "CSPI", "CSPR", "CSQ", "CSR", "CSSE", "CSTA", "CSTE",
              "CSTL", "CSTM", "CSTR", "CSV", "CSWC", "CSWI", "CSX", "CTAQ", "CTAS", "CTBI", "CTEK", "CTG", "CTGO", "CTHR",
              "CTIB", "CTIC", "CTK", "CTKB", "CTLP", "CTLT", "CTMX", "CTO", "CTOS", "CTRA", "CTRE", "CTRM", "CTRN", "CTS",
              "CTSH", "CTSO", "CTT", "CTVA", "CTXR", "CTXS", "CUBE", "CUBI", "CUE", "CUEN", "CUK", "CULL", "CULP", "CURI",
                            "CURO", "CURV", "CUTR", "CUZ", "CVAC", "CVBF", "CVCO", "CVCY", "CVE", "CVEO", "CVET", "CVGI",
              "CVGW", "CVI", "CVII", "CVLG", "CVLT", "CVLY", "CVM", "CVNA", "CVR", "CVRX", "CVS", "CVU", "CVV", "CVX",
              "CW", "CWAN", "CWBC", "CWBR", "CWCO", "CWEN", "CWH", "CWK", "CWST", "CWT", "CX", "CXDO", "CXE", "CXH", "CXM",
              "CXP", "CXW", "CYAD", "CYAN", "CYBE", "CYBN", "CYBR", "CYCC", "CYCN", "CYD", "CYH", "CYN", "CYRN", "CYRX", "CYT",
              "CYTH", "CYTK", "CYTO", "CYXT", "CZNC", "CZOO", "CZR", "CZWI", "D", "DAC", "DADA", "DAIO", "DAKT", "DAL", "DALN",
              "DALS", "DAN", "DAO", "DAR", "DARE", "DASH", "DATS", "DAVA", "DAWN", "DB", "DBD", "DBDR", "DBGI", "DBI", "DBRG", "DBTX",
              "DBVT", "DBX", "DCBO", "DCGO", "DCI", "DCO", "DCOM", "DCP", "DCPH", "DCRC", "DCRD", "DCRN", "DCT", "DCTH", "DD", "DDD",
              "DDI", "DDL", "DDOG", "DDS", "DE", "DEA", "DECK", "DEI", "DELL", "DEN", "DENN", "DEO", "DERM", "DESP", "DEX", "DFFN",
              "DFH", "DFIN", "DFS", "DG", "DGHI", "DGICA","DGICB", "DGII", "DGLY", "DGNS", "DGNU", "DGX", "DH", "DHBC", "DHBCU",
              "DHC", "DHCA", "DHHC", "DHI", "DHIL", "DHR", "DHT", "DHX", "DIBS", "DICE", "DIDI", "DIN", "DIOD", "DIS", "DISA",
              "DISCA", "DISCB", "DISCK", "DISH", "DIT", "DJCO", "DK", "DKDCA", "DKL", "DKNG", "DKS", "DLA", "DLB", "DLCA", "DLHC",
              "DLNG", "DLO", "DLPN", "DLR", "DLTH", "DLTR", "DLX", "DM", "DMAC", "DMF", "DMLP", "DMRC", "DMS", "DMTK", "DMYQ", "DMYS",
              "DNA", "DNAA", "DNAB", "DNAC", "DNAD", "DNAY", "DNB", "DNLI", "DNMR", "DNN", "DNOW", "DNUT", "DNZ", "DOC", "DOCN", "DOCS",
              "DOCU", "DOGZ", "DOLE", "DOMA", "DOMO", "DOOO", "DOOR", "DORM", "DOV", "DOW", "DOX", "DOYU", "DPRO", "DPW", "DPZ", "DQ", "DRAY",
              "DRD", "DRE", "DRH", "DRI", "DRIO", "DRMA", "DRNA", "DRQ", "DRRX", "DRTT", "DRUG", "DRVN", "DS", "DSAC", "DSAQ", "DSEY", "DSGN",
              "DSGX", "DSKE", "DSP", "DSPG", "DSS", "DSWL", "DSX", "DT", "DTC", "DTE", "DTEA", "DTF", "DTIL", "DTM", "DTOC", "DTRT", "DTSS",
              "DTST", "DUK", "DUNE", "DUO", "DUOL", "DUOT", "DV", "DVA", "DVAX", "DVD", "DVN", "DWAC", "DWIN", "DWSN", "DX", "DXC", "DXCM",
              "DXF", "DXLG", "DXPE", "DXR", "DXYN", "DY", "DYAI", "DYFN", "DYN", "DYNS", "DYNT", "DZSI", "E", "EA", "EAC", "EAF",
              "EAR", "EARN", "EAST", "EAT", "EB", "EBAC", "EBAY", "EBC", "EBET", "EBF", "EBIX", "EBMT", "EBON", "EBR", "EBS",
              "EBTC", "EC", "ECC", "ECL", "ECOL", "ECOM", "ECOR", "ECPG", "ECVT", "ED", "EDAP", "EDIT", "EDN", "EDNC", "EDR",
              "EDRY", "EDSA", "EDTK", "EDTX", "EDU", "EDUC", "EEFT", "EEIQ", "EEX", "EFC", "EFL", "EFOI", "EFSC", "EFT",
              "EFTR", "EFX", "EGAN", "EGBN", "EGGF", "EGHT", "EGLE", "EGLX", "EGO", "EGP", "EGRX", "EGY", "EH", "EHC",
              "EHTH", "EIG", "EIGR", "EIX", "EJFA", "EJH", "EKSO", "EL", "ELA", "ELAN", "ELDN", "ELEV", "ELF", "ELLO",
              "ELMD", "ELMS", "ELOX", "ELS", "ELSE", "ELTK", "ELVT", "ELY", "ELYM", "ELYS", "EM", "EMAN", "EMBK", "EMCF",
              "EME", "EMKR", "EML", "EMN", "EMR", "EMX", "ENB", "ENBL", "ENDP", "ENFA", "ENFN", "ENG", "ENIA", "ENIC", "ENJY",
              "ENLC", "ENLV", "ENNV", "ENOB", "ENPC", "ENPH", "ENR", "ENS", "ENSC", "ENSG", "ENSV", "ENTA", "ENTG", "ENTX", "ENV",
              "ENVA", "ENVB", "ENVI", "ENVX", "ENZ", "EOCW", "EOG", "EOLS", "EOSE", "EOT", "EPAC", "EPAM", "EPAY", "EPC", "EPD",
              "EPHY", "EPIX", "EPM", "EPR", "EPRT", "EPSN", "EPWR", "EPZM", "EQ", "EQBK", "EQC", "EQD", "EQH", "EQHA", "EQIX",
              "EQNR", "EQOS", "EQR", "EQS", "EQT", "EQX", "ERAS", "ERES", "ERF", "ERIC", "ERIE", "ERII", "ERJ", "ERO", "ERYP",
              "ES", "ESBK", "ESCA", "ESE", "ESEA", "ESGC", "ESGR", "ESI", "ESLT", "ESM", "ESMT", "ESNT", "ESP", "ESPR", "ESQ",
              "ESRT", "ESS", "ESSA", "ESSC", "ESTA", "ESTC", "ESTE", "ESXB", "ET", "ETAC", "ETD", "ETN", "ETNB", "ETO", "ETON",
              "ETR", "ETRN", "ETSY", "ETTX", "ETWO", "ETX           ", "EUCR", "EURN", "EUSG", "EVA", "EVAX", "EVBG", "EVBN", "EVC",
              "EVCM", "EVER", "EVF", "EVFM", "EVGN", "EVGO", "EVH", "EVI", "EVK", "EVLO", "EVLV", "EVN", "EVO", "EVOJ", "EVOK", "EVOL",
              "EVOP", "EVR", "EVRG", "EVRI", "EVTC", "EW", "EWBC", "EWCZ", "EWTX", "EXAI", "EXAS", "EXC", "EXEL", "EXFY", "EXK", "EXLS",
              "EXN", "EXP", "EXPD", "EXPE", "EXPI", "EXPO", "EXPR", "EXR", "EXTN", "EXTR", "EYE", "EYEN", "EYES", "EYPT", "EZFL", "EZGO",
              "EZPW", "F", "FA", "FACA", "FACT", "FAF", "FAMI", "FANG", "FANH", "FARM", "FARO", "FAST", "FAT", "FATBB", "FATE", "FB",
              "FBC", "FBHS", "FBIO", "FBIZ", "FBK", "FBMS", "FBNC", "FBP", "FBRT", "FBRX", "FC", "FCAP", "FCAX", "FCBC", "FCCO", "FCCY",
              "FCEL", "FCF", "FCFS", "FCN", "FCNCA", "FCPT", "FCRD", "FCUV", "FCX", "FDBC", "FDMT", "FDP", "FDS", "FDUS", "FDX", "FE",
              "FEDU", "FEIM", "FELE", "FEMY", "FENC", "FENG", "FERG", "FET", "FF", "FFBC", "FFBW", "FFHL", "FFIC", "FFIE", "FFIN", "FFIV",
              "FFNW", "FFWM", "FGBI", "FGEN", "FGF", "FHB", "FHI", "FHN", "FHS", "FHTX", "FIBK", "FICO", "FICV", "FIGS", "FINM", "FINS",
              "FINV", "FINW", "FIS", "FISI", "FISV", "FITB", "FIVE", "FIVN", "FIX", "FIXX", "FIZZ", "FKWL", "FL", "FLAC", "FLAG", "FLDM",
              "FLEX", "FLGC", "FLGT", "FLIC", "FLL", "FLME", "FLMN", "FLNC", "FLNG", "FLNT", "FLO", "FLOW", "FLR", "FLS", "FLT", "FLUX",
              "FLWS", "FLXS", "FLYA", "FLYW", "FMAC", "FMAO", "FMBH", "FMBI", "FMC", "FMIV", "FMNB", "FMS", "FMTX", "FMX", "FN", "FNA",
              "FNB", "FNCB", "FNCH", "FND", "FNF", "FNHC", "FNKO", "FNLC", "FNV", "FNWB", "FNWD", "FOA", "FOCS", "FOE", "FOLD", "FONR",
              "FOR", "FORA", "FORD", "FORE", "FORG", "FORM", "FORR", "FORTY", "FOSL", "FOUR", "FOX", "FOXA", "FOXF", "FOXW", "FPAC",
              "FPAY", "FPH", "FPI", "FR", "FRAF", "FRBA", "FRBK", "FRC", "FRD", "FREE", "FREQ", "FREY", "FRG", "FRGI", "FRHC", "FRLN",
              "FRME", "FRO", "FROG", "FRON", "FRPH", "FRPT", "FRSG", "FRSH", "FRST", "FRSX", "FRT", "FRTA", "FRW", "FRXB", "FSBC", "FSBW",
              "FSEA", "FSFG", "FSI", "FSII", "FSK", "FSLR", "FSLY", "FSM", "FSNB", "FSP", "FSR", "FSRX", "FSS", "FSSI", "FST", "FSTR", "FSTX", "FSV", "FT", "FTAA", "FTAI", "FTCH", "FTCI", "FTCV", "FTDR", "FTEK", "FTEV", "FTF", "FTFT", "FTHM", "FTI", "FTK", "FTNT", "FTPA", "FTRP", "FTS", "FTSI", "FTV", "FUBO", "FUL", "FULC", "FULT", "FUN", "FUNC", "FUND", "FURY", "FUSB", "FUSN", "FUTU", "FUV", "FVAM", "FVCB", "FVE", "FVIV", "FVRR", "FVT", "FWAC", "FWBI", "FWONA", "FWONK", "FWP", "FWRD", "FWRG", "FXLV", "FXNC", "FYBR", "FZT", "G", "GAB", "GABC", "GACQ", "GAIA", "GAIN", "GALT", "GAM", "GAMB", "GAMC", "GAME", "GAN", "GANX", "GAPA", "GASS", "GATE", "GATO", "GATX", "GAU", "GB", "GBAB", "GBCI", "GBDC", "GBIO", "GBL", "GBLI", "GBNH", "GBNY", "GBOX", "GBR", "GBRG", "GBS", "GBT", "GBX", "GCAC", "GCBC", "GCI", "GCMG", "GCO", "GCP", "GD", "GDDY", "GDEN", "GDEV", "GDOT", "GDP", "GDRX", "GDS", "GDV", "GDYN", "GE", "GECC", "GEF", "GEG", "GEL", "GENC", "GENE", "GENI", "GEO", "GEOS", "GERN", "GES", "GET", "GEVO", "GFAI", "GFED", "GFF", "GFI", "GFL", "GFOR", "GFS", "GFX", "GGAL", "GGB", "GGG", "GGMC", "GGN", "GGPI", "GGT", "GGZ", "GH", "GHAC", "GHC", "GHG", "GHL", "GHLD", "GHM", "GHRS", "GHSI", "GIA", "GIAC", "GIB", "GIC", "GIFI", "GIG", "GIGM", "GIII", "GIIX", "GIL", "GILD", "GILT", "GIPR", "GIS", "GIW", "GKOS", "GL", "GLAD", "GLAQ", "GLBE", "GLBL", "GLBS", "GLBZ", "GLDD", "GLDG", "GLEE", "GLG", "GLHA", "GLMD", "GLNG", "GLOB", "GLOP", "GLP", "GLPG", "GLPI", "GLRE", "GLSI", "GLT", "GLTA", "GLTO", "GLU", "GLUE", "GLW", "GLYC", "GM", "GMAB", "GMBL", "GMBT", "GMDA", "GME", "GMED", "GMII", "GMRE", "GMS", "GMTX", "GMVD", "GNAC", "GNCA", "GNE", "GNFT", "GNK", "GNL", "GNLN", "GNOG", "GNPX", "GNRC", "GNSS", "GNT", "GNTX", "GNTY", "GNUS", "GNW", "GO", "GOAC", "GOBI", "GOCO", "GOED", "GOEV", "GOGL", "GOGO", "GOL", "GOLD", "GOLF", "GOOD", "GOOG", "GOOGL", "GOOS", "GORO", "GOSS", "GOTU", "GOVX", "GP", "GPAC", "GPC", "GPCO", "GPI", "GPK", "GPL", "GPMT", "GPN", "GPOR", "GPP", "GPRE", "GPRK", "GPRO", "GPS", "GRAY", "GRBK", "GRC", "GRCL", "GRCY", "GREE", "GRFS", "GRIL", "GRIN", "GRMN", "GRNQ", "GROM", "GROW", "GROY", "GRPH", "GRPN", "GRTS", "GRTX", "GRUB", "GRVI", "GRVY", "GRWG", "GRX", "GS", "GSAQ", "GSAT", "GSBC", "GSBD", "GSEV", "GSHD", "GSIT", "GSK", "GSKY", "GSL", "GSM", "GSMG", "GSQB", "GSQD", "GSS", "GSV", "GT", "GTACU", "GTBP", "GTE", "GTEC", "GTES", "GTH", "GTHX", "GTIM", "GTLB", "GTLS", "GTN", "GTPA", "GTPB", "GTS", "GTX", "GTY", "GTYH", "GURE", "GUT", "GVA", "GVP", "GWB", "GWGH", "GWH", "GWII", "GWRE", "GWRS", "GWW", "GXII", "GXO", "GYRO", "H", "HA", "HAAC", "HAE", "HAFC", "HAIN", "HAL", "HALL", "HALO", "HAPP", "HARP", "HAS", "HASI", "HAYN", "HAYW", "HBAN", "HBB", "HBCP", "HBI", "HBIO", "HBM", "HBMD", "HBNC", "HBP", "HBT", "HCA", "HCAQ", "HCAR", "HCAT", "HCC", "HCCC", "HCCI", "HCDI", "HCI", "HCIC", "HCII", "HCKT", "HCM", "HCNE", "HCSG", "HCTI", "HCWB", "HD", "HDB", "HDSN", "HE", "HEAR", "HEES", "HEI", "HEI-A", "HELE", "HEP", "HEPA", "HEPS", "HERA", "HES", "HESM", "HEXO", "HFBL", "HFC", "HFFG", "HFWA", "HGBL", "HGEN", "HGSH", "HGV", "HHC", "HHGC", "HHLA", "HHR", "HHS", "HI", "HIBB", "HIFS", "HIG", "HIGA", "HIHO", "HII", "HIII", "HIL", "HIMS", "HIMX", "HIPO", "HITI", "HIVE", "HIW", "HKIB", "HL", "HLAH", "HLBZ", "HLF", "HLG", "HLI", "HLIO", "HLIT", "HLLY", "HLMN", "HLNE", "HLT", "HLTH", "HLX", "HLXA", "HMC", "HMCO", "HMG", "HMHC", "HMLP", "HMN", "HMNF", "HMPT", "HMST", "HMTV", "HMY", "HNGR", "HNI", "HNNA", "HNP", "HNRG", "HNST", "HOFT", "HOFV", "HOG", "HOLI", "HOLX", "HOMB", "HON", "HONE", "HOOD", "HOOK", "HOPE", "HOTH", "HOV", "HOWL", "HP", "HPE", "HPK", "HPLT", "HPP", "HPQ", "HPX", "HQH", "HQI", "HQL", "HQY", "HR", "HRB", "HRC", "HRI", "HRL", "HRMY", "HROW", "HRT", "HRTG", "HRTX", "HRZN", "HSAQ", "HSBC", "HSC", "HSDT", "HSIC", "HSII", "HSKA", "HSON", "HST", "HSTM", "HSTO", "HSY", "HT", "HTA", "HTBI", "HTBK", "HTBX", "HTGC", "HTGM", "HTH", "HTHT", "HTLD", "HTLF", "HTOO", "HTPA", "HTZ", "HUBB", "HUBG", "HUBS", "HUDI", "HUGE", "HUGS", "HUIZ", "HUM", "HUMA", "HUN", "HURC", "HURN", "HUSA", "HUSN", "HUT", "HUYA", "HVBC", "HVT", "HVT-A", "HWBK", "HWC", "HWEL", "HWKN", "HWKZ", "HWM", "HX", "HXL", "HY", "HYAC", "HYFM", "HYLN", "HYMC", "HYRE", "HYW", "HYZN", "HZN", "HZNP", "HZO", "HZON", "IAA", "IAC", "IACC", "IAG", "IAIC", "IART", "IAS", "IBA", "IBCP", "IBER", "IBEX", "IBIO", "IBKR", "IBM", "IBN", "IBOC", "IBP", "IBRX", "IBTX", "ICAD", "ICBK", "ICCC", "ICCH", "ICCM", "ICD", "ICE", "ICFI", "ICHR", "ICL", "ICLK", "ICLR", "ICMB", "ICPT", "ICUI", "ICVX", "ID", "IDA", "IDBA", "IDCC", "IDEX", "IDN", "IDRA", "IDT", "IDW", "IDXX", "IDYA", "IEA", "IEP", "IESC", "IEX", "IFBD", "IFF", "IFRX", "IFS", "IGAC", "IGC", "IGI", "IGIC", "IGMS", "IGNY", "IGT", "IH", "IHC", "IHG", "IHRT", "IHS", "IHT", "IIAC", "III", "IIII", "IIIN", "IIIV", "IIM", "IIN", "IINN", "IIPR", "IIVI", "IKNA", "IKNX", "IKT", "ILMN", "ILPT", "IMAB", "IMAC", "IMAQ", "IMAX", "IMBI", "IMCC", "IMCR", "IMGN", "IMGO", "IMH", "IMKTA", "IMMP", "IMMR", "IMNM", "IMO", "IMOS", "IMPL", "IMPX", "IMRA", "IMRN", "IMRX", "IMTE", "IMTX", "IMUX", "IMV", "IMVT", "IMXI", "INAB", "INAQ", "INBK", "INBX", "INCR", "INCY", "INDB", "INDI", "INDO", "INDP", "INDT", "INFA", "INFI", "INFN", "INFO", "INFU", "INFY", "ING", "INGN", "INGR", "INKA", "INKT", "INM", "INMB", "INMD", "INN", "INNV", "INO", "INOD", "INPX", "INS", "INSE", "INSG", "INSM", "INSP", "INST", "INSW", "INT", "INTA", "INTC", "INTG", "INTT", "INTU", "INTZ", "INUV", "INVA", "INVE", "INVH", "INVO", "INVZ", "INZY", "IO", "IOBT", "IONM", "IONQ", "IONS", "IOR", "IOSP", "IOVA", "IP", "IPA", "IPAR", "IPAX", "IPDN", "IPG", "IPGP", "IPHA", "IPI", "IPOD", "IPOF", "IPSC", "IPVA", "IPVF", "IPVI", "IPW", "IPWR", "IQ", "IQI", "IQV", "IR", "IRBT", "IRCP", "IRDM", "IREN", "IRIX", "IRM", "IRMD", "IRNT", "IROQ", "IRS", "IRT", "IRTC", "IRWD", "IS", "ISAA", "ISBC", "ISDR", "ISEE", "ISIG", "ISLE", "ISO", "ISOS", "ISPC", "ISR", "ISRG", "ISSC", "ISTR", "ISUN", "IT", "ITCB", "ITCI", "ITGR", "ITHX", "ITI", "ITIC", "ITMR", "ITOS", "ITP", "ITQ", "ITRG", "ITRI", "ITRM", "ITRN", "ITT", "ITW", "IVA", "IVAC", "IVAN", "IVC", "IVR", "IVT", "IVZ", "IX", "IXAQ", "IZEA", "J", "JACK", "JAGX", "JAKK", "JAMF", "JAN", "JANX", "JAQC", "JAZZ", "JBGS", "JBHT", "JBI", "JBL", "JBLU", "JBSS", "JBT", "JCI", "JCIC", "JCS", "JCTCF", "JD", "JEF", "JELD", "JFIN", "JFU", "JG", "JHG", "JHI", "JHS", "JHX", "JILL", "JJSF", "JKHY", "JKS", "JLL", "JMAC", "JMIA", "JNCE", "JNJ", "JNPR", "JOAN", "JOB", "JOBS", "JOBY", "JOE", "JOFF", "JOUT", "JP", "JPM", "JRJC", "JRSH", "JRVR", "JSPR", "JT", "JUGG", "JUPW", "JVA", "JW-A", "JWEL", "JWN", "JWSM", "JXN", "JYAC", "JYNT", "JZXN", "K", "KAHC", "KAI", "KAII", "KAIR", "KALA", "KALU", "KALV", "KAMN", "KAR", "KARO", "KAVL", "KB", "KBAL", "KBH", "KBNT", "KBR", "KC", "KCGI", "KD", "KDNY", "KDP", "KE", "KELYA", "KELYB", "KEN", "KEP", "KEQU", "KERN", "KEX", "KEY", "KEYS", "KFFB", "KFRC", "KFS", "KFY", "KGC", "KHC", "KIDS", "KIII", "KIM", "KIND", "KINS", "KINZ", "KIQ", "KIRK", "KKR", "KL", "KLAC", "KLAQ", "KLDO", "KLIC", "KLR", "KLTR", "KLXE", "KMB", "KMDA", "KMF", "KMI", "KMPH", "KMPR", "KMT", "KMX", "KN", "KNBE", "KNDI", "KNOP", "KNSA", "KNSL", "KNTE", "KNX", "KO", "KOD", "KODK", "KOF", "KOP", "KOPN", "KOR", "KORE", "KOS", "KOSS", "KPLT", "KPRX", "KPTI", "KR", "KRA", "KRBP", "KRC", "KREF", "KRG", "KRKR", "KRMD", "KRNL", "KRNT", "KRNY", "KRO", "KRON", "KROS", "KRP", "KRT", "KRTX", "KRUS", "KRYS", "KSI", "KSM", "KSPN", "KSS", "KSU", "KT", "KTB", "KTCC", "KTF", "KTOS", "KTRA", "KTTA", "KUKE", "KULR", "KURA", "KVHI", "KVSA", "KVSC", "KW", "KWAC", "KWR", "KXIN", "KYMR", "KZIA", "KZR", "L", "LABP", "LAC", "LAD", "LADR", "LAIX", "LAKE", "LAMR", "LANC", "LAND", "LARK", "LASR", "LAUR", "LAW", "LAWS", "LAZ", "LAZR", "LAZY", "LBAI", "LBC", "LBPH", "LBPS", "LBRDA", "LBRDK", "LBRT", "LBTYA", "LBTYB", "LBTYK", "LC", "LCA", "LCAA", "LCAP", "LCI", "LCID", "LCII", "LCNB", "LCTX", "LCUT", "LDHA", "LDI", "LDOS", "LE", "LEA", "LEAP", "LECO", "LEDS", "LEE", "LEG", "LEGA", "LEGH", "LEGN", "LEJU", "LEN", "LEO", "LESL", "LEU", "LEV", "LEVI", "LEVL", "LEXX", "LFC", "LFG", "LFMD", "LFST", "LFT", "LFTR", "LFUS", "LFVN", "LGAC", "LGHL", "LGIH", "LGL", "LGND", "LGO", "LGV", "LGVN", "LH", "LHAA", "LHC", "LHCG", "LHDX", "LHX", "LI", "LIAN", "LICY", "LIDR", "LIFE", "LII", "LILA", "LILAK", "LILM", "LIN", "LINC", "LIND", "LINK", "LIQT", "LITB", "LITE", "LITM", "LITT", "LIVE", "LIVN", "LIXT", "LIZI", "LJAQ", "LJPC", "LKCO", "LKFN", "LKQ", "LL", "LLL", "LLNW", "LLY", "LMACA", "LMAO", "LMAT", "LMB", "LMDX", "LMND", "LMNL", "LMNR", "LMPX", "LMRK", "LMST", "LMT", "LNC", "LND", "LNDC", "LNFA", "LNG", "LNN", "LNSR", "LNT", "LNTH", "LOAN", "LOB", "LOCC", "LOCL", "LOCO", "LODE", "LOGC", "LOGI", "LOKM", "LOMA", "LOOP", "LOPE", "LOTZ", "LOV", "LOVE", "LOW", "LPCN", "LPG", "LPI", "LPL", "LPLA", "LPRO", "LPSN", "LPTH", "LPTX", "LPX", "LQDA", "LQDT", "LRCX", "LRFC", "LRMR", "LRN", "LSBK", "LSCC", "LSEA", "LSF", "LSI", "LSPD", "LSTR", "LSXMA", "LSXMB", "LSXMK", "LTBR", "LTC", "LTCH", "LTH", "LTHM", "LTRN", "LTRPA", "LTRPB", "LTRX", "LTRY", "LU", "LUB", "LUCD", "LULU", "LUMN", "LUMO", "LUNA", "LUNG", "LUV", "LUXA", "LVLU", "LVO", "LVOX", "LVRA", "LVS", "LVTX", "LW", "LWAY", "LWLG", "LX", "LXEH", "LXFR", "LXP", "LXRX", "LXU", "LYB", "LYEL", "LYFT", "LYG", "LYL", "LYLT", "LYRA", "LYTS", "LYV", "LZ", "LZB", "M", "MA", "MAA", "MAC", "MACA", "MACC", "MACK", "MACQ", "MACU", "MAG", "MAIN", "MAN", "MANH", "MANT", "MANU", "MAPS", "MAQC", "MAR", "MARA", "MARK", "MARPS", "MAS", "MASI", "MASS", "MAT", "MATW", "MATX", "MAX", "MAXN", "MAXR", "MAYS", "MBAC", "MBCN", "MBI", "MBII", "MBIN", "MBIO", "MBOT", "MBRX", "MBT", "MBTC", "MBUU", "MBWM", "MC", "MCAE", "MCB", "MCBC", "MCBS", "MCD", "MCF", "MCFE", "MCFT", "MCG", "MCHP", "MCHX", "MCI", "MCK", "MCLD", "MCMJ", "MCO", "MCR", "MCRB", "MCRI", "MCS", "MCW", "MCY", "MD", "MDB", "MDC", "MDGL", "MDGS", "MDH", "MDIA", "MDJH", "MDLZ", "MDNA", "MDRR", "MDRX", "MDT", "MDU", "MDVL", "MDWD", "MDWT", "MDXG", "MDXH", "ME", "MEAC", "MEC", "MED", "MEDP", "MEDS", "MEG", "MEI", "MEIP", "MEKA", "MELI", "MEOA", "MEOH", "MERC", "MESA", "MESO", "MET", "METC", "METX", "MF", "MFA", "MFC", "MFD", "MFG", "MFGP", "MFH", "MFIN", "MFV", "MG", "MGA", "MGEE", "MGF", "MGI", "MGIC", "MGLN", "MGM", "MGNI", "MGNX", "MGP", "MGPI", "MGRC", "MGTA", "MGTX", "MGY", "MGYR", "MHH", "MHK", "MHLD", "MHO", "MIC", "MICT", "MIDD", "MIGI", "MILE", "MIME", "MIMO", "MIN", "MIND", "MINM", "MIR", "MIRM", "MIRO", "MIST", "MIT", "MITA", "MITC", "MITK", "MITO", "MITQ", "MITT", "MIXT", "MKC", "MKD", "MKFG", "MKL", "MKSI", "MKTW", "MKTX", "ML", "MLAB", "MLAC", "MLCO", "MLI", "MLKN", "MLM", "MLNK", "MLP", "MLR", "MLSS", "MLVF", "MMAT", "MMC", "MMI", "MMLP", "MMM", "MMMB", "MMP", "MMS", "MMSI", "MMT", "MMX", "MMYT", "MN", "MNDO", "MNDT", "MNDY", "MNKD", "MNMD", "MNOV", "MNPR", "MNR", "MNRL", "MNRO", "MNSB", "MNSO", "MNST", "MNTK", "MNTS", "MNTV", "MNTX", "MO", "MOBQ", "MOD", "MODN", "MODV", "MOFG", "MOGO", "MOGU", "MOH", "MOHO", "MOLN", "MOMO", "MON", "MOR", "MORF", "MORN", "MOS", "MOSY", "MOTS", "MOTV", "MOV", "MOVE", "MOXC", "MP", "MPAA", "MPAC", "MPB", "MPC", "MPLN", "MPLX", "MPV", "MPW", "MPWR", "MPX", "MQ", "MRAI", "MRAM", "MRBK", "MRC", "MRCC", "MRCY", "MREO", "MRIN", "MRK", "MRKR", "MRLN", "MRM", "MRNA", "MRNS", "MRO", "MRSN", "MRTN", "MRTX", "MRUS", "MRVI", "MRVL", "MS", "MSA", "MSAC", "MSB", "MSBI", "MSC", "MSCI", "MSDA", "MSEX", "MSFT", "MSGE", "MSGM", "MSGS", "MSI", "MSM", "MSN", "MSP", "MSTR", "MSVB", "MT", "MTA", "MTAC", "MTAL", "MTB", "MTBC", "MTC", "MTCH", "MTCR", "MTD", "MTDR", "MTEM", "MTEX", "MTG", "MTH", "MTL", "MTLS", "MTN", "MTNB", "MTOR", "MTP", "MTR", "MTRN", "MTRX", "MTRY", "MTSI", "MTTR", "MTW", "MTX", "MTZ", "MU", "MUDS", "MUFG", "MULN", "MUR", "MUSA", "MUX", "MVBF", "MVIS", "MVO", "MVST", "MWA", "MX", "MXC", "MXCT", "MXL", "MYE", "MYFW", "MYGN", "MYMD", "MYNA", "MYNZ", "MYO", "MYOV", "MYPS", "MYRG", "MYSZ", "MYTE", "NAAC", "NABL", "NAII", "NAK", "NAKD", "NAOV", "NAPA", "NARI", "NAT", "NATH", "NATI", "NATR", "NAUT", "NAVB", "NAVI", "NBEV", "NBHC", "NBIX", "NBN", "NBR", "NBRV", "NBSE", "NBST", "NBTB", "NBTX", "NBY", "NC", "NCBS", "NCLH", "NCMI", "NCNA", "NCNO", "NCR", "NCSM", "NCTY", "NDAC", "NDAQ", "NDLS", "NDRA", "NDSN", "NE", "NECB", "NEE", "NEGG", "NEM", "NEN", "NEO", "NEOG", "NEON", "NEP", "NEPH", "NEPT", "NERV", "NES", "NESR", "NET", "NETI", "NEU", "NEW", "NEWP", "NEWR", "NEWT", "NEX", "NEXA", "NEXI", "NEXT", "NFBK", "NFE", "NFG", "NFGC", "NFH", "NFLX", "NFYS", "NG", "NGC", "NGCA", "NGD", "NGG", "NGL", "NGM", "NGMS", "NGS", "NGVC", "NGVT", "NH", "NHC", "NHI", "NHTC", "NI", "NICE", "NICK", "NINE", "NIO", "NISN", "NIU", "NJR", "NKE", "NKLA", "NKSH", "NKTR", "NKTX", "NL", "NLIT", "NLOK", "NLS", "NLSN", "NLSP", "NLTX", "NLY", "NM", "NMFC", "NMG", "NMIH", "NMM", "NMMC", "NMR", "NMRD", "NMRK", "NMTC", "NMTR", "NN", "NNBR", "NNDM", "NNI", "NNN", "NNOX", "NNVC", "NOA", "NOAC", "NOAH", "NOC", "NODK", "NOG", "NOK", "NOMD", "NOTV", "NOV", "NOVA", "NOVN", "NOVT", "NOW", "NP", "NPCE", "NPK", "NPO", "NPTN", "NR", "NRAC", "NRBO", "NRC", "NRDS", "NRDY", "NREF", "NRG", "NRIM", "NRIX", "NRP", "NRT", "NRXP", "NRZ", "NS", "NSA", "NSC", "NSEC", "NSIT", "NSP", "NSPR", "NSR", "NSSC", "NSTB", "NSTC", "NSTD", "NSTG", "NSYS", "NTAP", "NTB", "NTCO", "NTCT", "NTES", "NTGR", "NTIC", "NTIP", "NTLA", "NTNX", "NTP", "NTR", "NTRA", "NTRB", "NTRS", "NTST", "NTUS", "NTWK", "NTZ", "NUAN", "NUE", "NURO", "NUS", "NUVA", "NUVB", "NUVL", "NUWE", "NUZE", "NVAX", "NVCN", "NVCR", "NVDA", "NVEC", "NVEE", "NVEI", "NVFY", "NVGS", "NVIV", "NVMI", "NVNO", "NVO", "NVOS", "NVR", "NVRO", "NVS", "NVSA", "NVST", "NVT", "NVTA", "NVTS", "NVVE", "NWBI", "NWE", "NWFL", "NWG", "NWL", "NWLI", "NWN", "NWPX", "NWS", "NWSA", "NX", "NXC", "NXDT", "NXE", "NXGN", "NXN", "NXP", "NXPI", "NXQ", "NXR", "NXRT", "NXST", "NXTC", "NXTD", "NXTP", "NXU", "NYC", "NYCB", "NYMT", "NYMX", "NYT", "NYXH", "O", "OACB", "OAS", "OB", "OBAS", "OBCI", "OBLG", "OBNK", "OBSV", "OBT", "OC", "OCA", "OCAX", "OCC", "OCCI", "OCDX", "OCFC", "OCFT", "OCG", "OCGN", "OCN", "OCSL", "OCUL", "OCUP", "OCX", "ODC", "ODFL", "ODP", "ODT", "OEC", "OEG", "OEPW", "OESX", "OFC", "OFED", "OFG", "OFIX", "OFLX", "OFS", "OG", "OGE", "OGEN", "OGI", "OGN", "OGS", "OHI", "OHPA", "OI", "OIA", "OII", "OIIM", "OIS", "OKE", "OKTA", "OLB", "OLED", "OLK", "OLLI", "OLMA", "OLN", "OLO", "OLP", "OLPX", "OM", "OMAB", "OMC", "OMCL", "OMEG", "OMER", "OMEX", "OMF", "OMGA", "OMI", "OMIC", "OMP", "OMQS", "ON", "ONB", "ONCR", "ONCS", "ONCT", "ONCY", "ONDS", "ONEM", "ONEW", "ONL", "ONON", "ONTF", "ONTO", "ONTX", "ONVO", "OOMA", "OP", "OPA", "OPAD", "OPBK", "OPCH", "OPEN", "OPFI", "OPGN", "OPHC", "OPI", "OPK", "OPNT", "OPOF", "OPRA", "OPRT", "OPRX", "OPT", "OPTN", "OPTT", "OPY", "OR", "ORA", "ORAN", "ORC", "ORCC", "ORCL", "ORGN", "ORGO", "ORGS", "ORI", "ORIA", "ORIC", "ORLA", "ORLY", "ORMP", "ORN", "ORPH", "ORRF", "ORTX", "OSAT", "OSBC", "OSCR", "OSG", "OSH", "OSI", "OSIS", "OSK", "OSMT", "OSPN", "OSS", "OSTK", "OSTR", "OSUR", "OSW", "OTEC", "OTEX", "OTIC", "OTIS", "OTLK", "OTLY", "OTMO", "OTRA", "OTRK", "OTTR", "OUST", "OUT", "OVBC", "OVID", "OVLY", "OVV", "OWL", "OWLT", "OXAC", "OXBR", "OXLC", "OXM", "OXSQ", "OXUS", "OXY", "OYST", "OZK", "OZON", "PAA", "PAAS", "PAC", "PACB", "PACK", "PACW", "PACX", "PAE", "PAG", "PAGP", "PAGS", "PAHC", "PAIC", "PALI", "PALT", "PAM", "PANL", "PANW", "PAQC", "PAR", "PARR", "PASG", "PATH", "PATI", "PATK", "PAVM", "PAX", "PAY", "PAYA", "PAYC", "PAYO", "PAYS", "PAYX", "PB", "PBA", "PBAX", "PBBK", "PBCT", "PBF", "PBFS", "PBFX", "PBH", "PBHC", "PBI", "PBIP", "PBLA", "PBPB", "PBR", "PBT", "PBTS", "PBYI", "PCAR", "PCB", "PCG", "PCH", "PCOM", "PCOR", "PCPC", "PCRX", "PCSA", "PCSB", "PCT", "PCTI", "PCTY", "PCVX", "PCYG", "PCYO", "PD", "PDCE", "PDCO", "PDD", "PDEX", "PDFS", "PDLB", "PDM", "PDOT", "PDS", "PDSB", "PEAK", "PEB", "PEBK", "PEBO", "PECO", "PED", "PEG", "PEGA", "PEI", "PEN", "PENN", "PEP", "PERI", "PESI", "PETQ", "PETS", "PETV", "PETZ", "PFC", "PFDR", "PFE", "PFG", "PFGC", "PFHD", "PFIE", "PFIN", "PFIS", "PFLT", "PFMT", "PFS", "PFSI", "PFSW", "PFTA", "PFX", "PG", "PGC", "PGEN", "PGNY", "PGR", "PGRE", "PGRW", "PGTI", "PH", "PHAR", "PHAS", "PHAT", "PHCF", "PHG", "PHGE", "PHI", "PHIC", "PHIO", "PHM", "PHR", "PHUN", "PHVS", "PHX", "PI", "PIAI", "PICC", "PII", "PIK", "PIM", "PINC", "PINE", "PING", "PINS", "PIPP", "PIPR", "PIRS", "PIXY", "PJT", "PK", "PKBK", "PKE", "PKG", "PKI", "PKOH", "PKX", "PLAB", "PLAG", "PLAN", "PLAY", "PLBC", "PLBY", "PLCE", "PLD", "PLG", "PLIN", "PLL", "PLM", "PLMI", "PLMR", "PLNT", "PLOW", "PLPC", "PLRX", "PLSE", "PLTK", "PLTR", "PLUG", "PLUS", "PLX", "PLXP", "PLXS", "PLYA", "PLYM", "PM", "PMCB", "PMD", "PME", "PMGM", "PMM", "PMO", "PMT", "PMTS", "PMVC", "PMVP", "PNBK", "PNC", "PNFP", "PNM", "PNNT", "PNR", "PNRG", "PNT", "PNTG", "PNTM", "PNW", "POAI", "PODD", "POLA", "POLY", "POND", "PONO", "POOL", "POR", "POSH", "POST", "POW", "POWI", "POWL", "POWW", "PPBI", "PPBT", "PPC", "PPD", "PPG", "PPGH", "PPHP", "PPIH", "PPL", "PPSI", "PPT", "PPTA", "PRA", "PRAA", "PRAX", "PRBM", "PRCH", "PRCT", "PRDO", "PRFT", "PRFX", "PRG", "PRGO", "PRGS", "PRI", "PRIM", "PRK", "PRLB", "PRLD", "PRM", "PRMW", "PRO", "PROC", "PROF", "PROG", "PROV", "PRPB", "PRPC", "PRPH", "PRPL", "PRPO", "PRQR", "PRSR", "PRT", "PRTA", "PRTC", "PRTG", "PRTH", "PRTK", "PRTS", "PRTY", "PRU", "PRVA", "PRVB", "PSA", "PSAG", "PSB", "PSEC", "PSFE", "PSHG", "PSMT", "PSN", "PSNL", "PSO", "PSPC", "PSTG", "PSTH", "PSTI", "PSTL", "PSTV", "PSTX", "PSX", "PSXP", "PT", "PTC", "PTCT", "PTE", "PTEN", "PTGX", "PTIX", "PTLO", "PTMN", "PTN", "PTNR", "PTOC", "PTON", "PTPI", "PTR", "PTRA", "PTRS", "PTSI", "PTVE", "PUBM", "PUCK", "PUK", "PULM", "PUMP", "PUYI", "PV", "PVBC", "PVG", "PVH", "PVL", "PW", "PWFL", "PWOD", "PWP", "PWR", "PWSC", "PX", "PXD", "PXLW", "PXS", "PYCR", "PYPD", "PYPL", "PYR", "PYXS", "PZG", "PZN", "PZZA", "QCOM", "QCRH", "QD", "QDEL", "QFIN", "QFTA", "QGEN", "QH", "QIPT", "QIWI", "QK", "QLGN", "QLI", "QLYS", "QMCO", "QNRX", "QNST", "QRHC", "QRTEA", "QRTEB", "QRVO", "QS", "QSI", "QSR", "QTNT", "QTRX", "QTT", "QTWO", "QUAD", "QUBT", "QUIK", "QUMU", "QUOT", "QURE", "R", "RAAS", "RACE", "RAD", "RADA", "RADI", "RAIL", "RAIN", "RAM", "RAMP", "RAND", "RANI", "RAPT", "RARE", "RAVE", "RBA", "RBAC", "RBB", "RBBN", "RBCAA", "RBCN", "RBKB", "RBLX", "RBNC", "RBOT", "RC", "RCAT", "RCEL", "RCHG", "RCI", "RCII", "RCKT", "RCKY", "RCL", "RCLF", "RCM", "RCMT", "RCON", "RCOR", "RCRT", "RCUS", "RDBX", "RDCM", "RDFN", "RDHL", "RDI", "RDIB", "RDN", "RDNT", "RDS-B", "RDUS", "RDVT", "RDW", "RDWR", "RDY", "RE", "REAL", "REAX", "REDU", "REE", "REED", "REFR", "REG", "REGI", "REGN", "REI", "REKR", "RELI", "RELL", "RELX", "RELY", "RENN", "RENT", "REPH", "REPL", "REPX", "RERE", "RES", "RESN", "RETA", "RETO", "REV", "REVE", "REVG", "REVH", "REX", "REXR", "REYN", "REZI", "RF", "RFIL", "RFL", "RFP", "RGA", "RGC", "RGCO", "RGEN", "RGF", "RGLD", "RGLS", "RGNX", "RGP", "RGR", "RGS", "RGT", "RH", "RHE", "RHI", "RHP", "RIBT", "RICK", "RICO", "RIDE", "RIG", "RIGL", "RILY", "RIO", "RIOT", "RIVN", "RJF", "RKDA", "RKLB", "RKLY", "RKT", "RKTA", "RL", "RLAY", "RLGT", "RLGY", "RLI", "RLJ", "RLMD", "RLX", "RLYB", "RM", "RMAX", "RMBI", "RMBL", "RMBS", "RMCF", "RMD", "RMED", "RMGC", "RMNI", "RMO", "RMR", "RMT", "RMTI", "RNA", "RNAZ", "RNDB", "RNG", "RNGR", "RNLX", "RNR", "RNST", "RNW", "RNWK", "RNXT", "ROAD", "ROCC", "ROCG", "ROCK", "ROCR", "ROG", "ROIC", "ROIV", "ROK", "ROKU", "ROL", "ROLL", "RONI", "ROOT", "ROP", "ROSS", "ROST", "ROVR", "RPAY", "RPD", "RPHM", "RPID", "RPM", "RPRX", "RPT", "RPTX", "RRBI", "RRC", "RRD", "RRGB", "RRR", "RRX", "RS", "RSF", "RSG", "RSI", "RSKD", "RSLS", "RSSS", "RSVR", "RTLR", "RTX", "RUBY", "RUN", "RUSHA", "RUSHB", "RUTH", "RVAC", "RVI", "RVLV", "RVMD", "RVNC", "RVP", "RVPH", "RVSB", "RVT", "RWAY", "RWLK", "RWT", "RXDX", "RXRA", "RXRX", "RXST", "RXT", "RY", "RYAAY", "RYAM", "RYAN", "RYB", "RYI", "RYN", "RYTM", "RZLT", "S", "SA", "SABR", "SABS", "SACH", "SAFE", "SAFM", "SAFT", "SAGE", "SAH", "SAIA", "SAIC", "SAIL", "SAL", "SALM", "SAM", "SAMA", "SAMG", "SAN", "SANA", "SAND          ", "SANM", "SANW", "SAP", "SAR", "SASR", "SATS", "SAVA", "SAVE", "SB", "SBAC", "SBCF", "SBEA", "SBET", "SBEV", "SBFG", "SBGI", "SBH", "SBII", "SBLK", "SBNY", "SBOW", "SBR", "SBRA", "SBS", "SBSI", "SBSW", "SBT", "SBTX", "SBUX", "SC", "SCCO", "SCHL", "SCHN", "SCHW", "SCI", "SCKT", "SCL", "SCLE", "SCM", "SCOA", "SCOB", "SCOR", "SCPH", "SCPL", "SCPS", "SCS", "SCSC", "SCU", "SCVL", "SCVX", "SCWX", "SCX", "SCYX", "SD", "SDAC", "SDC", "SDGR", "SDH", "SDIG", "SDPI", "SE", "SEAC", "SEAH", "SEAS", "SEAT", "SEB", "SECO", "SEDG", "SEE", "SEED", "SEEL", "SEER", "SEIC", "SELB", "SELF", "SEM", "SEMR", "SENEA", "SENEB", "SENS", "SERA", "SESN", "SEV", "SEVN", "SF", "SFBC", "SFBS", "SFE", "SFET", "SFIX", "SFL", "SFM", "SFNC", "SFST", "SFT", "SFUN", "SG", "SGA", "SGBX", "SGC", "SGEN", "SGFY", "SGH", "SGHT", "SGLB", "SGMA", "SGML", "SGMO", "SGMS", "SGRP", "SGRY", "SGTX", "SGU", "SHAC", "SHAK", "SHBI", "SHC", "SHCR", "SHEN", "SHG", "SHI", "SHIP", "SHLS", "SHLX", "SHO", "SHOO", "SHOP", "SHPW", "SHW", "SHYF", "SI", "SIBN", "SID", "SIEB", "SIEN", "SIER", "SIF", "SIFY", "SIG", "SIGA", "SIGI", "SII", "SILC", "SILK", "SILV", "SIM", "SIMO", "SINO", "SINT", "SIOX", "SIRI", "SISI", "SITC", "SITE", "SITM", "SIVB", "SIX", "SJ", "SJI", "SJM", "SJR", "SJT", "SJW", "SKE", "SKIL", "SKIN", "SKLZ", "SKM", "SKT", "SKX", "SKY", "SKYA", "SKYT", "SKYW", "SLAB", "SLAC", "SLAM", "SLB", "SLCA", "SLCR", "SLDB", "SLF", "SLG", "SLGC", "SLGG", "SLGL", "SLGN", "SLHG", "SLI", "SLM", "SLN", "SLNG", "SLNH", "SLNO", "SLP", "SLQT", "SLRC", "SLRX", "SLS", "SLVM", "SLVR", "SM", "SMAP", "SMAR", "SMBC", "SMBK", "SMCI", "SMED", "SMFG", "SMFR", "SMG", "SMHI", "SMID", "SMIH", "SMIT", "SMLP", "SMLR", "SMM", "SMMF", "SMMT", "SMP", "SMPL", "SMRT", "SMSI", "SMTC", "SMTI", "SMTS", "SMWB", "SNA", "SNAP", "SNAX", "SNBR", "SNCE", "SNCR", "SNCY", "SND", "SNDA", "SNDL", "SNDR", "SNDX", "SNES", "SNEX", "SNFCA", "SNGX", "SNII", "SNMP", "SNN", "SNOA", "SNOW", "SNP", "SNPO", "SNPS", "SNPX", "SNRH", "SNSE", "SNT", "SNTG", "SNV", "SNX", "SNY", "SO", "SOFI", "SOFIW", "SOHO", "SOHU", "SOI", "SOL", "SOLO", "SOLY", "SON", "SONM", "SONN", "SONO", "SONX", "SONY", "SOPA", "SOPH", "SOR", "SOS", "SOTK", "SOVO", "SP", "SPAQ", "SPB", "SPCB", "SPCE", "SPFI", "SPG", "SPGI", "SPGS", "SPH", "SPI", "SPIR", "SPK", "SPKB", "SPLK", "SPLP", "SPNE", "SPNS", "SPNT", "SPOK", "SPOT", "SPPI", "SPR", "SPRB", "SPRO", "SPSC", "SPT", "SPTK", "SPTN", "SPWH", "SPWR", "SPXC", "SQ", "SQFT", "SQL", "SQM", "SQNS", "SQSP", "SQZ", "SR", "SRAD", "SRAX", "SRC", "SRCE", "SRCL", "SRDX", "SRE", "SREV", "SRG", "SRGA", "SRI", "SRL", "SRLP", "SRNE", "SRPT", "SRRA", "SRRK", "SRSA", "SRT", "SRTS", "SRZN", "SSAA", "SSB", "SSBI", "SSBK", "SSD", "SSKN", "SSL", "SSNC", "SSNT", "SSP", "SSRM", "SSSS", "SSTI", "SSTK", "SSY", "SSYS", "ST", "STAA", "STAB", "STAF", "STAG", "STAR          ", "STBA", "STC", "STCN", "STE", "STEM", "STEP", "STER", "STFC", "STG", "STGW", "STIM", "STKL", "STKS", "STL", "STLA", "STLD", "STM", "STN", "STNE", "STNG", "STOK", "STON", "STOR", "STRA", "STRC", "STRE", "STRL", "STRM", "STRN", "STRO", "STRR", "STRS", "STRT", "STSA", "STT", "STTK", "STVN", "STWD", "STX", "STXB", "STXS", "STZ", "STZ-B", "SU", "SUI", "SUM", "SUMO", "SUMR", "SUN", "SUNL", "SUNS", "SUNW", "SUP", "SUPN", "SUPV", "SURF", "SURG", "SUZ", "SV", "SVC", "SVFA", "SVFB", "SVFC", "SVFD", "SVM", "SVOK", "SVOKU", "SVRA", "SVT", "SWAV", "SWBI", "SWCH", "SWET", "SWI", "SWIM", "SWIR", "SWK", "SWKH", "SWKS", "SWM", "SWN", "SWSS", "SWTX", "SWX", "SXC", "SXI", "SXT", "SXTC", "SY", "SYBT", "SYBX", "SYF", "SYK", "SYN", "SYNA", "SYNH", "SYNL", "SYPR", "SYRS", "SYTA", "SYY", "T", "TA", "TAC", "TACA", "TACO", "TACT", "TAIT", "TAK", "TAL", "TALK", "TALO", "TALS", "TANH", "TAOP", "TAP", "TARA", "TARO", "TARS", "TASK", "TAST", "TATT", "TAYD", "TBBK", "TBCP", "TBI", "TBK", "TBLA", "TBLT", "TBNK", "TBPH", "TBSA", "TC", "TCAC", "TCBC", "TCBI", "TCBK", "TCBS", "TCBX", "TCDA", "TCFC", "TCI", "TCMD", "TCN", "TCOM", "TCON", "TCPC", "TCRR", "TCRX", "TCS", "TCVA", "TCX", "TD", "TDC", "TDCX", "TDG", "TDOC", "TDS", "TDUP", "TDW", "TDY", "TEAM", "TECH", "TECK", "TEDU", "TEF", "TEKK", "TEL", "TELA", "TELL", "TEN", "TENB", "TENX", "TEO", "TER", "TERN", "TESS", "TETC", "TEVA", "TEX", "TFC", "TFFP", "TFII", "TFSL", "TFX", "TG", "TGA", "TGB", "TGH", "TGI", "TGLS", "TGNA", "TGP", "TGS", "TGT", "TGTX", "TGVC", "TH", "THC", "THCA", "THCP", "THFF", "THG", "THM", "THMA", "THMO", "THO", "THR", "THRM", "THRN", "THRX", "THRY", "THS", "THTX", "TIG", "TIGO", "TIGR", "TIL", "TILE", "TIMB", "TINV", "TIOA", "TIPT", "TIRX", "TISI", "TITN", "TIVC", "TIXT", "TJX", "TK", "TKAT", "TKC", "TKNO", "TKR", "TLGA", "TLIS", "TLK", "TLMD", "TLRY", "TLS", "TLSA", "TLYS", "TM", "TMAC", "TMBR", "TMC", "TMCI", "TMDI", "TMDX", "TME", "TMHC", "TMKR", "TMO", "TMP", "TMPM", "TMQ", "TMST", "TMUS", "TMX", "TNC", "TNDM", "TNET", "TNGX", "TNK", "TNL", "TNP", "TNXP", "TNYA", "TOI", "TOL", "TOMZ", "TOPS", "TOST", "TOUR", "TOWN", "TPB", "TPBA", "TPC", "TPGS", "TPGY", "TPH", "TPHS", "TPIC", "TPL", "TPR", "TPST", "TPTX", "TPVG", "TPX", "TR", "TRC", "TRCA", "TRDA", "TREB", "TREC", "TREE", "TREX", "TRGP", "TRHC", "TRI", "TRIB", "TRIN", "TRIP", "TRIT", "TRKA", "TRMB", "TRMD", "TRMK", "TRMR", "TRN", "TRNO", "TRNS", "TRON", "TROO", "TROW", "TROX", "TRP", "TRQ", "TRS", "TRST", "TRT", "TRTL", "TRTN", "TRTX", "TRU", "TRUE", "TRUP", "TRV", "TRVG", "TRVI", "TRVN", "TRX", "TS", "TSAT", "TSBK", "TSC", "TSCO", "TSE", "TSEM", "TSHA", "TSIB", "TSLA", "TSLX", "TSM", "TSN", "TSP", "TSPQ", "TSQ", "TSRI", "TSVT", "TT", "TTC", "TTCF", "TTD", "TTE", "TTEC", "TTEK", "TTGT", "TTI", "TTM", "TTMI", "TTNP", "TTOO", "TTSH", "TTWO", "TU", "TUEM", "TUFN", "TUGC", "TUP", "TURN", "TUSK", "TUYA", "TV", "TVAC", "TVTX", "TVTY", "TW", "TWCB", "TWI", "TWIN", "TWKS", "TWLO", "TWLV", "TWND", "TWNI", "TWNK", "TWNT", "TWO", "TWOA", "TWOU", "TWST", "TWTR", "TX", "TXG", "TXMD", "TXN", "TXRH", "TXT", "TY", "TYG", "TYL", "TYME", "TYRA", "TZOO", "TZPS", "U", "UA", "UAA", "UAL", "UAMY", "UAN", "UAVS", "UBA", "UBCP", "UBER", "UBFO", "UBOH", "UBS", "UBSI", "UBX", "UCBI", "UCL", "UCTT", "UDMY", "UDR", "UE", "UEC", "UEIC", "UEPS", "UFAB", "UFCS", "UFI", "UFPI", "UFPT", "UG", "UGI", "UGP", "UGRO", "UHAL", "UHS", "UHT", "UI", "UIHC", "UIS", "UK", "UL", "ULBI", "ULCC", "ULH", "ULTA", "UMBF", "UMC", "UMH", "UMPQ", "UNAM", "UNB", "UNCY", "UNF", "UNFI", "UNH", "UNIT", "UNM", "UNP", "UNTY", "UNVR", "UONE", "UONEK", "UP", "UPC", "UPH", "UPLD", "UPS", "UPST", "UPTD", "UPWK", "URBN", "URG", "URGN", "URI", "UROY", "USAC", "USAK", "USAP", "USAS", "USAU", "USB", "USCB", "USDP", "USEG", "USER", "USFD", "USIO", "USLM", "USM", "USNA", "USPH", "USWS", "USX", "UTHR", "UTI", "UTL", "UTMD", "UTME", "UTRS", "UTSI", "UTZ", "UUU", "UUUU", "UVE", "UVSP", "UVV", "UWMC", "UXIN", "V", "VABK", "VAC", "VACC", "VAL", "VALE", "VALN", "VALU", "VAPO", "VAQC", "VATE", "VAXX", "VBFC", "VBIV", "VBLT", "VBNK", "VBTX", "VC", "VCEL", "VCKA", "VCNX", "VCRA", "VCTR", "VCV", "VCXA", "VCYT", "VEC", "VECO", "VECT", "VEEE", "VEEV", "VEL", "VELO", "VENA", "VEON", "VERA", "VERB", "VERI", "VERO", "VERU", "VERV", "VERX", "VERY", "VET", "VEV", "VFC", "VFF", "VG", "VGFC", "VGII", "VGM", "VGR", "VGZ", "VHAQ", "VHC", "VHI", "VIA", "VIAC", "VIACA", "VIAO", "VIAV", "VICI", "VICR", "VIEW", "VII", "VINC", "VINO", "VINP", "VIOT", "VIPS", "VIR", "VIRC", "VIRI", "VIRT", "VIRX", "VISL", "VIST", "VITL", "VIV", "VIVE", "VIVO", "VJET", "VKI", "VKQ", "VKTX", "VLAT", "VLCN", "VLD", "VLDR", "VLGEA", "VLN", "VLO", "VLON", "VLRS", "VLT", "VLTA", "VLY", "VMAC", "VMAR", "VMC", "VMD", "VMEO", "VMI", "VMO", "VMW", "VNCE", "VNDA", "VNE", "VNET", "VNO", "VNOM", "VNRX", "VNT", "VNTR", "VOC", "VOD", "VOLT", "VOR", "VOXX", "VOYA", "VPCB", "VPCC", "VPG", "VPV", "VQS", "VRA", "VRAR", "VRAY", "VRCA", "VRDN", "VREX", "VRM", "VRME", "VRNA", "VRNS", "VRNT", "VRPX", "VRRM", "VRS", "VRSK", "VRSN", "VRT", "VRTS", "VRTV", "VRTX", "VS", "VSAT", "VSCO", "VSEC", "VSH", "VST", "VSTA", "VSTM", "VSTO", "VTAQ", "VTEX", "VTGN", "VTIQ", "VTIQW", "VTN", "VTNR", "VTOL", "VTR", "VTRS", "VTRU", "VTSI", "VTVT", "VTYX", "VUZI", "VVI", "VVNT", "VVOS", "VVPR", "VVR", "VVV", "VWE", "VWTR", "VXRT", "VYGG", "VYGR", "VYNE", "VYNT", "VZ", "VZIO", "W", "WAB", "WABC", "WAFD", "WAFU", "WAL", "WALD", "WARR", "WASH", "WAT", "WATT", "WAVC", "WAVE", "WB", "WBA", "WBEV", "WBK", "WBS", "WBT", "WBX", "WCC", "WCN", "WD", "WDAY", "WDC", "WDFC", "WDH", "WE", "WEAV", "WEBR", "WEC", "WEI", "WEJO", "WELL", "WEN", "WERN", "WES", "WETF", "WEX", "WEYS", "WF", "WFC", "WFCF", "WFG", "WFRD", "WGO", "WH", "WHD", "WHF", "WHG", "WHLM", "WHLR", "WHR", "WILC", "WIMI", "WINA", "WING", "WINT", "WINV", "WIRE", "WISA", "WISH", "WIT", "WIX", "WK", "WKEY", "WKHS", "WKME", "WKSP", "WLDN", "WLFC", "WLK", "WLKP", "WLL", "WLMS", "WLTW", "WM", "WMB", "WMC", "WMG", "WMK", "WMPN", "WMS", "WMT", "WNC", "WNEB", "WNS", "WNW", "WOLF", "WOOF", "WOR", "WORX", "WOW", "WPC", "WPCA", "WPCB", "WPM", "WPP", "WPRT", "WQGA", "WRAP", "WRB", "WRBY", "WRE", "WRK", "WRLD", "WRN", "WSBC", "WSBF", "WSC", "WSFS", "WSM", "WSO", "WSO-B", "WSR", "WST", "WSTG", "WTBA", "WTER", "WTFC", "WTI", "WTM", "WTRG", "WTRH", "WTS", "WTT", "WTTR", "WU", "WVE", "WVFC", "WVVI", "WW", "WWD", "WWE", "WWR", "WWW", "WY", "WYNN", "WYY", "X", "XAIR", "XBIO", "XBIT", "XCUR", "XEL", "XELA", "XELB", "XENE", "XENT", "XERS", "XFLT", "XFOR", "XGN", "XHR", "XIN", "XL", "XLNX", "XLO", "XM", "XMTR", "XNCR", "XNET", "XOM", "XOMA", "XOS", "XP", "XPAX", "XPDI", "XPEL", "XPER", "XPEV", "XPL", "XPO", "XPOA", "XPOF", "XPRO", "XRAY", "XRTX", "XRX", "XSPA", "XTLB", "XTNT", "XXII", "XYF", "XYL", "Y", "YAC", "YALA", "YCBD", "YELL", "YELP", "YETI", "YEXT", "YGMZ", "YI", "YJ", "YMAB", "YMM", "YMTX", "YNDX", "YORW", "YOU", "YPF", "YQ", "YRD", "YSAC", "YSG", "YTEN", "YTPG", "YTRA", "YUM", "YUMC", "YVR", "YY", "Z", "ZBH", "ZBRA", "ZCMD", "ZD", "ZDGE", "ZEAL", "ZEN", "ZENV", "ZEPP", "ZEST", "ZETA", "ZEUS", "ZEV", "ZG", "ZGNX", "ZH", "ZI", "ZIM", "ZION", "ZIOP", "ZIP", "ZIVO", "ZIXI", "ZKIN", "ZLAB", "ZM", "ZME", "ZNGA", "ZNH", "ZNTE", "ZNTL", "ZOM", "ZS", "ZSAN", "ZT", "ZTO", "ZTS", "ZUMZ", "ZUO", "ZVIA", "ZVO", "ZWRK", "ZWS", "ZY", "ZYME", "ZYNE", "ZYXI" "CRS"]

'''
f = open('D:/data/filename1.csv', 'r')
rdr = csv.reader(f)

for line in rdr:
    print(line)
    stock_list.append(line)

f.close()
print(stock_list)
'''

# 파일 다운로드 함수

file_path = "D:\data"
def download(url, file_name = None):
    if not file_name:
        file_name = url.split('/')[-1]

    with open(file_name, "wb") as file:
        response = requests.get(url)
        if response.status_code == 200:
            file.write(response.content)
            return True
    return False
#file_path+


# 실적 정보 다운로드 함수
def download_data(ticker):

    income_url = "https://stockrow.com/api/companies/{ticker}/financials.xlsx?dimension=A&section=Income%20Statement&sort=desc"
    growth_url = "https://stockrow.com/api/companies/{ticker}/financials.xlsx?dimension=A&amp;section=Growth&amp;sort=desc"
    cashflow_url = "https://stockrow.com/api/companies/{ticker}/financials.xlsx?dimension=A&amp;section=Cash Flow&amp;sort=desc"
    metrics_url =   "https://stockrow.com/api/companies/{ticker}/financials.xlsx?dimension=A&amp;section=Metrics&amp;sort=desc"


    income_down = download(income_url.format(ticker=ticker), "{ticker}_INCOME.xlsx".format(ticker=ticker))
    growth_down = download(growth_url.format(ticker=ticker), "{ticker}_GROWTH.xlsx".format(ticker=ticker))
    cash_down = download(cashflow_url.format(ticker=ticker), "{ticker}_CASH.xlsx".format(ticker=ticker))
    metrics_down = download(metrics_url.format(ticker=ticker), "{ticker}_METRICS.xlsx".format(ticker=ticker))
    if income_down == True and growth_down == True and cash_down == True and metrics_down == True:

        return True
    else:
        return False





# 실적 정보 가져오는 함수
def get_stock_data(ticker):

    # Ticker 주식 정보 Read
    df_income = pd.read_excel("{ticker}_INCOME.xlsx".format(ticker=ticker), index_col=0).fillna(0)
    df_income = df_income.T
    df_growth = pd.read_excel("{ticker}_GROWTH.xlsx".format(ticker=ticker), index_col=0).fillna(0)
    df_growth = df_growth.T
    df_cash = pd.read_excel("{ticker}_CASH.xlsx".format(ticker=ticker), index_col=0).fillna(0)
    df_cash = df_cash.T
    df_metrics = pd.read_excel("{ticker}_METRICS.xlsx".format(ticker=ticker), index_col=0).fillna(0)
    df_metrics = df_metrics.T

  #file_path+
   # list_isnert = []


    revenue_isnert = ["{ticker}".format(ticker=ticker), "Revenue"]
    revenue_growth_isnert = ["{ticker}".format(ticker=ticker), "revenue_growth"]
    growth_margin_isnert = ["{ticker}".format(ticker=ticker), " growth_margin"]
    operating_income_isnert = ["{ticker}".format(ticker=ticker), "Operating_Income"]
    operating_growth_isnert = ["{ticker}".format(ticker=ticker), "operating_growth"]
    operating_margin_isnert = ["{ticker}".format(ticker=ticker), "operating_margin"]
    net_income_isnert = ["{ticker}".format(ticker=ticker), "net_income"]
    netincome_growth_isnert = ["{ticker}".format(ticker=ticker), "net_income_growth"]
    eps_isnert = ["{ticker}".format(ticker=ticker), "EPS"]
    eps_growth_isnert = ["{ticker}".format(ticker=ticker), "EPS_growth"]
    dividends_paid_isnert = ["{ticker}".format(ticker=ticker), "dividends_paid"]
    payout_ratio_isnert = ["{ticker}".format(ticker=ticker), "payout_ratio"]
    shares_isnert = ["{ticker}".format(ticker=ticker), "shares"]
    operating_cash_isnert = ["{ticker}".format(ticker=ticker), "operating_cash_flow"]
    operating_cash_growth_isnert = ["{ticker}".format(ticker=ticker), "OCF_growth"]
    capital_expenditures_isnert = ["{ticker}".format(ticker=ticker), "capital_expenditures"]
    netincome_capex_ratio_isnert = ["{ticker}".format(ticker=ticker), "netincome_capex_ratio"]
    free_cashflow_isnert = ["{ticker}".format(ticker=ticker), "Free_Cash_Flow"]
    free_cashflow_growth_isnert = ["{ticker}".format(ticker=ticker), "FCF_growth"]
    fcf_per_share_isnert = ["{ticker}".format(ticker=ticker), "fcf_per_share"]
    roe_isnert = ["{ticker}".format(ticker=ticker), "ROE"]
    roic_isnert = ["{ticker}".format(ticker=ticker), "ROIC"]
    bps_isnert = ["{ticker}".format(ticker=ticker), "BPS"]
    pe_isnert = ["{ticker}".format(ticker=ticker), "PER"]
    psr_isnert = ["{ticker}".format(ticker=ticker), "PSR"]
    p_fcf_ratio_isnert = ["{ticker}".format(ticker=ticker), "P/FCF"]
    null_value = float(0)

    # 매출액 최근 5분기
    if 'Revenue' in df_income.columns:
        for i in reversed(range(0,10)):
            revenue_isnert.append(float(df_income.iloc[i]['Revenue']))
    else : revenue_isnert = revenue_isnert + [0,0,0,0,0,0,0,0,0,0]


    #revenue growth
    if 'Revenue Growth' in df_income.columns:
        for i in reversed(range(0,10)):
            revenue_growth_isnert.append(round((float(df_income.iloc[i]['Revenue Growth']))*100,2))
    else : revenue_growth_isnert = revenue_growth_isnert + [0,0,0,0,0,0,0,0,0,0]


    #growth margin
    if 'Gross Margin' in df_income.columns:
        for i in reversed(range(0,10)):
            growth_margin_isnert.append(round((float(df_income.iloc[i]['Gross Margin']))*100,2))
    else : growth_margin_isnert = growth_margin_isnert + [0,0,0,0,0,0,0,0,0,0]


    # 영업이익
    if 'Operating Income' in df_income.columns:
        for i in reversed(range(0,10)):
            operating_income_isnert.append(float(df_income.iloc[i]['Operating Income']))
    else : operating_income_insert = operating_income_isnert + [0,0,0,0,0,0,0,0,0,0]
    
    
    
    #operating growth
    if 'Operating Income Growth' in df_growth.columns:
        for i in reversed(range(0,10)):
            operating_growth_isnert.append(round((float(df_growth.iloc[i]['Operating Income Growth']))*100,2))
    else : operating_growth_isnert = operating_growth_isnert + [0,0,0,0,0,0,0,0,0,0]
    
    
    #operating margin
    if 'Operating Income' in df_income.columns:
        for i in reversed(range(0,10)):
            operating_margin_isnert.append(round((float(df_income.iloc[i]['Operating Income'])/float(df_income.iloc[i]['Revenue']))*100,2))
    else : operating_margin_isnert = operating_margin_isnert + [0,0,0,0,0,0,0,0,0,0]


    # 순이익 최근 5분기
    if 'Net Income Common' in df_income.columns:
        for i in reversed(range(0,10)):
            net_income_isnert.append(float(df_income.iloc[i]['Net Income Common']))
    else : net_income_isnert = net_income_isnert + [0,0,0,0,0,0,0,0,0,0]



    # 순이익 성장률
    if 'Net Income Growth' in df_growth.columns:
        for i in reversed(range(0,10)):
            netincome_growth_isnert.append((float(df_growth.iloc[i]['Net Income Growth']))*100)
    else : netincome_growth_isnert = netincome_growth_isnert + [0,0,0,0,0,0,0,0,0,0]

    # eps 최근 5분기
    if 'EPS (Diluted)' in df_income.columns:
        for i in reversed(range(0, 10)):
            eps_isnert.append(round(float(df_income.iloc[i]['EPS (Diluted)']),2))
    else:
        eps_isnert = eps_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


    # eps 성장률
    if 'EPS Growth (diluted)' in df_growth.columns:
        for i in reversed(range(0,10)):
            eps_growth_isnert.append(round((float(df_growth.iloc[i]['EPS Growth (diluted)']))*100,2))
    else : eps_growth_isnert = eps_growth_isnert + [0,0,0,0,0,0,0,0,0,0]


    # dividend
    if 'Dividends Paid (Common)' in df_cash.columns:
        for i in reversed(range(0,10)):
            dividends_paid_isnert.append(float(df_cash.iloc[i]['Dividends Paid (Common)']))
    else : dividends_paid_isnert = dividends_paid_isnert + [0,0,0,0,0,0,0,0,0,0]

    # payout ratio
    if 'Dividends Paid (Common)' in df_cash.columns:
        for i in reversed(range(0,10)):
            payout_ratio_isnert.append(round((float(df_cash.iloc[i]['Dividends Paid (Common)'])/float(df_income.iloc[i]['Net Income Common']))*-100,2))
    else : payout_ratio_isnert = payout_ratio_isnert + [0,0,0,0,0,0,0,0,0,0]


    #share
    if 'Shares (Diluted, Average)' in df_income.columns:
        for i in reversed(range(0,10)):
            shares_isnert.append(float(df_income.iloc[i]['Shares (Diluted, Average)']))
    else : shares_isnert = shares_isnert + [0,0,0,0,0,0,0,0,0,0]

    # Operating Cash Flow
    if 'Operating Cash Flow' in df_cash.columns:
        for i in reversed(range(0,10)):
            operating_cash_isnert.append(float(df_cash.iloc[i]['Operating Cash Flow']))
    else : operating_cash_isnert = operating_cash_isnert + [0,0,0,0,0,0,0,0,0,0]

    # Operating Cash Flow Growth
    if 'Operating Cash Flow Growth' in df_growth.columns:
        for i in reversed(range(0,10)):
            operating_cash_growth_isnert.append(round((float(df_growth.iloc[i]['Operating Cash Flow Growth']))*100,2))
    else : operating_cash_growth_isnert = operating_cash_growth_isnert + [0,0,0,0,0,0,0,0,0,0]

    # Capital expenditures
    if 'Capital expenditures' in df_cash.columns:
        for i in reversed(range(0,10)):
            capital_expenditures_isnert.append(float(df_cash.iloc[i]['Capital expenditures']))
    else : capital_expenditures_isnert = capital_expenditures_isnert + [0,0,0,0,0,0,0,0,0,0]


    # 순이익대비 자본적 지출 비중
    if 'Capital expenditures' in df_cash.columns:
        for i in reversed(range(0,10)):
            netincome_capex_ratio_isnert.append(round(float((df_cash.iloc[i]['Capital expenditures'])/float(df_income.iloc[i]['Net Income Common']))*-100,2))
    else : netincome_capex_ratio_isnert = netincome_capex_ratio_isnert + [0,0,0,0,0,0,0,0,0,0]


    # FCF
    if 'Free Cash Flow' in df_metrics.columns:
        for i in reversed(range(0,10)):
            free_cashflow_isnert.append(float(df_metrics.iloc[i]['Free Cash Flow']))
    else : free_cashflow_isnert = free_cashflow_isnert + [0,0,0,0,0,0,0,0,0,0]

    # fcf 성장률
    if 'Free Cash Flow Growth' in df_growth.columns:
        for i in reversed(range(0,10)):
            free_cashflow_growth_isnert.append(round((float(df_growth.iloc[i]['Free Cash Flow Growth']))*100,2))
    else : free_cashflow_growth_isnert= free_cashflow_growth_isnert + [0,0,0,0,0,0,0,0,0,0]


    #Free Cash Flow per Share
    if 'Free Cash Flow per Share' in df_metrics.columns:
        for i in reversed(range(0,10)):
            fcf_per_share_isnert.append(round(float(df_metrics.iloc[i]['Free Cash Flow per Share']),2))
    else : fcf_per_share_isnert = fcf_per_share_isnert + [0,0,0,0,0,0,0,0,0,0]


    #ROE
    if 'ROE' in df_metrics.columns:
        for i in reversed(range(0,10)):
            roe_isnert.append(round((float(df_metrics.iloc[i]['ROE']))*100,2))
    else : roe_isnert = roe_isnert + [0,0,0,0,0,0,0,0,0,0]

    #ROIC
    if 'ROIC' in df_metrics.columns:
        for i in reversed(range(0,10)):
            roic_isnert.append(round((float(df_metrics.iloc[i]['ROIC']))*100,2))
    else : roic_isnert = roic_isnert + [0,0,0,0,0,0,0,0,0,0]

    #Book value per Share
    if 'Book value per Share' in df_metrics.columns:
        for i in reversed(range(0,10)):
            bps_isnert.append(round(float(df_metrics.iloc[i]['Book value per Share']),2))
    else : bps_isnert = bps_isnert + [0,0,0,0,0,0,0,0,0,0]

    #pe
    if 'P/E ratio' in df_metrics.columns:
        for i in reversed(range(0,10)):
            pe_isnert.append(round(float(df_metrics.iloc[i]['P/E ratio']),2))
    else : pe_isnert = pe_isnert + [0,0,0,0,0,0,0,0,0,0]

    #psr
    if 'P/S ratio' in df_metrics.columns:
        for i in reversed(range(0,10)):
            psr_isnert.append(round(float(df_metrics.iloc[i]['P/S ratio']),2))
    else : psr_isnert = psr_isnert + [0,0,0,0,0,0,0,0,0,0]

    # P/ FCF
    if 'P/FCF ratio' in df_metrics.columns:
        for i in reversed(range(0,10)):
            p_fcf_ratio_isnert.append(round(float(df_metrics.iloc[i]['P/FCF ratio']),2))
    else : p_fcf_ratio_isnert = p_fcf_ratio_isnert + [0,0,0,0,0,0,0,0,0,0]


    return revenue_isnert, revenue_growth_isnert, growth_margin_isnert, operating_income_isnert, operating_growth_isnert, \
           operating_margin_isnert, net_income_isnert, netincome_growth_isnert, eps_isnert, eps_growth_isnert, dividends_paid_isnert, \
           payout_ratio_isnert, shares_isnert, operating_cash_isnert, operating_cash_growth_isnert, capital_expenditures_isnert, \
           netincome_capex_ratio_isnert, free_cashflow_isnert, free_cashflow_growth_isnert, fcf_per_share_isnert, roe_isnert, \
            roic_isnert, bps_isnert, pe_isnert, psr_isnert, p_fcf_ratio_isnert


'''
conn = connect_db()
curs = conn.cursor()
sql = """insert into STOCK_INFO_USA(STOCK_CODE, AREA, Y2012, Y2013, Y2014, Y2015, Y2016, Y2017, Y2018, Y2019, Y2020, Y2021) 
    values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
'''
'''
result = []
'''
'''
# 반복문 돌면서 INSERT
for i, ticker in enumerate(stock_list):
    try:
        if download_data(ticker):
            stock_info = get_stock_data(ticker)
            result.append(stock_info)
            curs.execute(sql, result)
            conn.commit()
        # else:
          # print(i, ' 번 째 ', ticker, ' : NO DATA PASS')
    except Exception as e:
        print(i, ' 번 째 오류 발생 : ', ticker, ' 오류:', str(e))

conn.close()
'''
'''
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active

sheet.append(["티커", "영역", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"])

'''

# 반복문 돌면서 INSERT
for i, ticker in enumerate(stock_list):

    try:
        if download_data(ticker):
            stock_info = get_stock_data(ticker)
            #sheet.append(stock_info)
           # result=result.append(stock_info)
            data = pd.DataFrame(stock_info)
            print(data)
            data.to_csv('D:\data\AAAFinance2.csv',mode='a', header=False)
            # else:
          # print(i, ' 번 째 ', ticker, ' : NO DATA PASS')
    except Exception as e:
        print(i, ' 번 째 오류 발생 : ', ticker, ' 오류:', str(e))



'''
wb.save("Finance2021.xlsx")
'''