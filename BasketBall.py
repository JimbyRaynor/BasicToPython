
import random

loopstack = [] # for FOR loops, including nested for loops (just push/pop from same stack)
callstack = [] # for GOSUB/RETURN

state = {"dummy": 0} # real variable dictionary
stringstate = {"dummy": "dummystring"} # string variable dictionary

def basicGOSUB(returnline, targetline):
    callstack.append(returnline)
    return targetline

def basicRETURN():
    if not callstack:
        raise RuntimeError("RETURN without GOSUB")
    return callstack.pop()

def line_5(state):
    print('5 PRINT TAB(31);"BASKETBALL"')
    return "7"


def line_7(state):
    print('7 PRINT TAB(15);"CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY"')
    return "8"


def line_8(state):
    print('8 PRINT:PRINT:PRINT')
    return "10"


def line_10(state):
    print('10 PRINT "THIS IS DARTMOUTH COLLEGE BASKETBALL.  YOU WILL BE DARTMOUTH"')
    return "20"


def line_20(state):
    print('20 PRINT " CAPTAIN AND PLAYMAKER.  CALL SHOTS AS FOLLOWS:  1. LONG"')
    return "30"


def line_30(state):
    print('30 PRINT " (30 FT.) JUMP SHOT; 2. SHORT (15 FT.) JUMP SHOT; 3. LAY"')
    return "40"


def line_40(state):
    print('40 PRINT " UP; 4. SET SHOT."')
    return "60"


def line_60(state):
    print('60 PRINT "BOTH TEAMS WILL USE THE SAME DEFENSE.  CALL DEFENSE AS"')
    return "70"


def line_70(state):
    print('70 PRINT "FOLLOWS:  6. PRESS; 6.5 MAN-TO MAN; 7. ZONE; 7.5 NONE."')
    return "72"


def line_72(state):
    print('72 PRINT "TO CHANGE DEFENSE, JUST TYPE 0 AS YOUR NEXT SHOT."')
    return "76"


def line_76(state):
    print('76 INPUT "YOUR STARTING DEFENSE WILL BE";D:IF D<6 THEN 2010')
    D=input("starting defense: ")
    state["D"] = D
    if int(D) < 6:
        return "2010"
    return "79"


def line_79(state):
    print('79 PRINT')
    return "80"


def line_80(state):
    print('80 INPUT "CHOOSE YOUR OPPONENT";O$')
    stringstate["O"] = input("choose your opponent: ")
    return "370"


def line_370(state):
    print('370 PRINT "CENTER JUMP"')
    print("center jump")
    return "390"


def line_390(state):
    print('390 IF RND(1)> 3/5 THEN 420')
    if random.random() > 3/5:
        return "420"
    return "400"


def line_400(state):
    print('400 PRINT O$;" CONTROLS THE TAP."')
    print(stringstate["O"]+ " controls the tap")
    return "410"

def line_410(state):
    print('410 GOTO 3000')
    return "3000"


def line_420(state):
    print('420 PRINT "DARTMOUTH CONTROLS THE TAP."')
    print("darmouth controls the tap")
    return "425"


def line_425(state):
    print('425 PRINT')
    print()
    return "430"


def line_430(state):
    print('430 INPUT "YOUR SHOT";Z')
    state["Z"] = int(input("your shot: "))
    return "440"


def line_440(state):
    print('440 P=0')
    state["P"] = 0
    return "445"


def line_445(state):
    print('445 IF Z<>INT(Z) THEN 455')
    return "446"


def line_446(state):
    print('446 IF Z<0 OR Z>4 THEN 455')
    return "447"


def line_447(state):
    print('447 GOTO 460')
    return "455"


def line_455(state):
    print('455 PRINT "INCORRECT ANSWER.  RETYPE IT. ";:GOTO 430')
    return "460"


def line_460(state):
    print('460 IF RND(1)<.5 THEN 1000')
    return "480"


def line_480(state):
    print('480 IF T<100 THEN 1000')
    return "490"


def line_490(state):
    print('490 PRINT')
    return "491"


def line_491(state):
    print('491 IF S(1)<>S(0) THEN 510')
    return "492"


def line_492(state):
    print('492 PRINT:PRINT "   ***** END OF SECOND HALF *****":PRINT')
    return "493"


def line_493(state):
    print('493 PRINT "SCORE AT END OF REGULATION TIME:"')
    return "494"


def line_494(state):
    print('494 PRINT "        DARTMOUTH:";S(1);"  ";O$;":";S(0)')
    return "495"


def line_495(state):
    print('495 PRINT')
    return "496"


def line_496(state):
    print('496 PRINT "BEGIN TWO MINUTE OVERTIME PERIOD"')
    return "499"


def line_499(state):
    print('499 T=93')
    return "500"


def line_500(state):
    print('500 GOTO 370')
    return "510"


def line_510(state):
    print('510 PRINT "   ***** END OF GAME *****"')
    return "515"


def line_515(state):
    print('515 PRINT "FINAL SCORE: DARTMOUTH:";S(1);"  ";O$;":";S(0)')
    return "520"


def line_520(state):
    print('520 STOP')
    return "600"


def line_600(state):
    print('600 PRINT')
    return "610"


def line_610(state):
    print('610 PRINT "   *** TWO MINUTES LEFT IN THE GAME ***"')
    return "620"


def line_620(state):
    print('620 PRINT')
    return "630"


def line_630(state):
    print('630 RETURN')
    basicRETURN()
    return "1000"


def line_1000(state):
    print('1000 ON Z GOTO 1040,1040')
    return "1030"


def line_1030(state):
    print('1030 GOTO 1300')
    return "1040"


def line_1040(state):
    print('1040 T=T+1')
    return "1041"


def line_1041(state):
    print('1041 IF T=50 THEN 8000')
    return "1042"


def line_1042(state):
    print('1042 IF T=92 THEN 1046')
    return "1043"


def line_1043(state):
    print('1043 GOTO 1050')
    return "1046"


def line_1046(state):
    print('1046 GOSUB 600')
    return "1050"


def line_1050(state):
    print('1050 PRINT "JUMP SHOT"')
    return "1060"


def line_1060(state):
    print('1060 IF RND(1)>.341*D/8 THEN 1090')
    return "1070"


def line_1070(state):
    print('1070 PRINT "SHOT IS GOOD."')
    return "1075"


def line_1075(state):
    print('1075 GOSUB 7000')
    return "1085"


def line_1085(state):
    print('1085 GOTO 3000')
    return "1090"


def line_1090(state):
    print('1090 IF RND(1)>.682*D/8 THEN 1200')
    return "1100"


def line_1100(state):
    print('1100 PRINT "SHOT IS OFF TARGET."')
    return "1105"


def line_1105(state):
    print('1105 IF D/6*RND(1)>.45 THEN 1130')
    return "1110"


def line_1110(state):
    print('1110 PRINT "DARTMOUTH CONTROLS THE REBOUND."')
    return "1120"


def line_1120(state):
    print('1120 GOTO 1145')
    return "1130"


def line_1130(state):
    print('1130 PRINT "REBOUND TO ";O$')
    return "1140"


def line_1140(state):
    print('1140 GOTO 3000')
    return "1145"


def line_1145(state):
    print('1145 IF RND(1)>.4 THEN 1158')
    return "1150"


def line_1150(state):
    print('1150 GOTO 1300')
    return "1158"


def line_1158(state):
    print('1158 IF D=6 THEN 5100')
    return "1160"


def line_1160(state):
    print('1160 PRINT "BALL PASSED BACK TO YOU. ";')
    return "1170"


def line_1170(state):
    print('1170 GOTO 430')
    return "1180"


def line_1180(state):
    print('1180 IF RND(1)>.9 THEN 1190')
    return "1185"


def line_1185(state):
    print('1185 PRINT "PLAYER FOULED, TWO SHOTS."')
    return "1187"


def line_1187(state):
    print('1187 GOSUB 4000')
    return "1188"


def line_1188(state):
    print('1188 GOTO 3000')
    return "1190"


def line_1190(state):
    print('1190 PRINT "BALL STOLEN. ";O$;"S BALL."')
    return "1195"


def line_1195(state):
    print('1195 GOTO 3000')
    return "1200"


def line_1200(state):
    print('1200 IF RND(1)>.782*D/8 THEN 1250')
    return "1210"


def line_1210(state):
    print('1210 PRINT "SHOT IS BLOCKED.  BALL CONTROLLED BY ";')
    return "1230"


def line_1230(state):
    print('1230 IF RND(1)>.5 THEN 1242')
    return "1235"


def line_1235(state):
    print('1235 PRINT "DARTMOUTH."')
    return "1240"


def line_1240(state):
    print('1240 GOTO 430')
    return "1242"


def line_1242(state):
    print('1242 PRINT O$;"."')
    return "1245"


def line_1245(state):
    print('1245 GOTO 3000')
    return "1250"


def line_1250(state):
    print('1250 IF RND(1)>.843*D/8 THEN 1270')
    return "1255"


def line_1255(state):
    print('1255 PRINT "SHOOTER IS FOULED.  TWO SHOTS."')
    return "1260"


def line_1260(state):
    print('1260 GOSUB 4000')
    return "1265"


def line_1265(state):
    print('1265 GOTO 3000')
    return "1270"


def line_1270(state):
    print('1270 PRINT "CHARGING FOUL.  DARTMOUTH LOSES BALL."')
    return "1280"


def line_1280(state):
    print('1280 GOTO 3000')
    return "1300"


def line_1300(state):
    print('1300 T=T+1')
    return "1301"


def line_1301(state):
    print('1301 IF T=50 THEN 8000')
    return "1302"


def line_1302(state):
    print('1302 IF T=92 THEN 1304')
    return "1303"


def line_1303(state):
    print('1303 GOTO 1305')
    return "1304"


def line_1304(state):
    print('1304 GOSUB 600')
    return "1305"


def line_1305(state):
    print('1305 IF Z=0 THEN 2010')
    return "1310"


def line_1310(state):
    print('1310 IF Z>3 THEN 1700')
    return "1320"


def line_1320(state):
    print('1320 PRINT "LAY UP."')
    return "1330"


def line_1330(state):
    print('1330 IF 7/D*RND(1)>.4 THEN 1360')
    return "1340"


def line_1340(state):
    print('1340 PRINT "SHOT IS GOOD.  TWO POINTS."')
    return "1345"


def line_1345(state):
    print('1345 GOSUB 7000')
    return "1355"


def line_1355(state):
    print('1355 GOTO 3000')
    return "1360"


def line_1360(state):
    print('1360 IF 7/D*RND(1)>.7 THEN 1500')
    return "1370"


def line_1370(state):
    print('1370 PRINT "SHOT IS OFF THE RIM."')
    return "1380"


def line_1380(state):
    print('1380 IF RND(1)>2/3 THEN 1415')
    return "1390"


def line_1390(state):
    print('1390 PRINT O$;" CONTROLS THE REBOUND."')
    return "1400"


def line_1400(state):
    print('1400 GOTO 3000')
    return "1415"


def line_1415(state):
    print('1415 PRINT "DARTMOUTH CONTROLS THE REBOUND."')
    return "1420"


def line_1420(state):
    print('1420 IF RND(1)>.4 THEN 1440')
    return "1430"


def line_1430(state):
    print('1430 GOTO 1300')
    return "1440"


def line_1440(state):
    print('1440 PRINT "BALL PASSED BACK TO YOU.";')
    return "1450"


def line_1450(state):
    print('1450 GOTO 430')
    return "1500"


def line_1500(state):
    print('1500 IF 7/D*RND(1)>.875 THEN 1600')
    return "1510"


def line_1510(state):
    print('1510 PRINT "SHOOTER FOULED.  TWO SHOTS."')
    return "1520"


def line_1520(state):
    print('1520 GOSUB 4000')
    return "1530"


def line_1530(state):
    print('1530 GOTO 3000')
    return "1600"


def line_1600(state):
    print('1600 IF 7/D*RND(1)>.925 THEN 1630')
    return "1610"


def line_1610(state):
    print('1610 PRINT "SHOT BLOCKED. ";O$;"S BALL."')
    return "1620"


def line_1620(state):
    print('1620 GOTO 3000')
    return "1630"


def line_1630(state):
    print('1630 PRINT "CHARGING FOUL.  DARTMOUTH LOSES THE BALL."')
    return "1640"


def line_1640(state):
    print('1640 GOTO 3000')
    return "1700"


def line_1700(state):
    print('1700 PRINT "SET SHOT."')
    return "1710"


def line_1710(state):
    print('1710 GOTO 1330')
    return "2010"


def line_2010(state):
    print('2010 INPUT "YOUR NEW DEFENSIVE ALLIGNMENT IS";D')
    D = input("YOUR NEW DEFENSIVE ALLIGNMENT IS: ")
    state["D"] = D
    return "2030"


def line_2030(state):
    print('2030 IF D<6 THEN 2010')
    if state["D"] < 6:
       return "2010"
    return "2040"


def line_2040(state):
    print('2040 GOTO 425')
    return "425"


def line_3000(state):
    print('3000 P=1')
    state["P"] = 1
    return "3005"


def line_3005(state):
    print('3005 T=T+1')
    state["T"] = state["T"] + 1
    return "3008"


def line_3008(state):
    print('3008 IF T=50 THEN 8000')
    if state["T"] == 50:
       return "8000"
    return "3012"


def line_3012(state):
    print('3012 GOTO 3018')
    return "3018"


def line_3015(state):
    print('3015 GOSUB 600') # two minutes left in game
    basicGOSUB("3018","600") # return line, GOSUB line
    return "3018"


def line_3018(state):
    print('3018 PRINT')
    return "3020"


def line_3020(state):
    print('3020 Z1=10/4*RND(1)+1')
    return "3030"


def line_3030(state):
    print('3030 IF Z1>2 THEN 3500')
    return "3040"


def line_3040(state):
    print('3040 PRINT "JUMP SHOT."')
    return "3050"


def line_3050(state):
    print('3050 IF 8/D*RND(1)>.35 THEN 3100')
    return "3060"


def line_3060(state):
    print('3060 PRINT "SHOT IS GOOD."')
    return "3080"


def line_3080(state):
    print('3080 GOSUB 6000')
    return "3090"


def line_3090(state):
    print('3090 GOTO 425')
    return "3100"


def line_3100(state):
    print('3100 IF 8/D*RND(1)>.75 THEN 3200')
    return "3105"


def line_3105(state):
    print('3105 PRINT "SHOT IS OFF RIM."')
    return "3110"


def line_3110(state):
    print('3110 IF D/6*RND(1)>.5 THEN 3150')
    return "3120"


def line_3120(state):
    print('3120 PRINT "DARTMOUTH CONTROLS THE REBOUND."')
    return "3130"


def line_3130(state):
    print('3130 GOTO 425')
    return "3150"


def line_3150(state):
    print('3150 PRINT O$;" CONTROLS THE REBOUND."')
    return "3160"


def line_3160(state):
    print('3160 IF D=6 THEN 5000')
    return "3165"


def line_3165(state):
    print('3165 IF RND(1)>.5 THEN 3175')
    return "3168"


def line_3168(state):
    print('3168 PRINT "PASS BACK TO ";O$;" GUARD."')
    return "3170"


def line_3170(state):
    print('3170 GOTO 3000')
    return "3175"


def line_3175(state):
    print('3175 GOTO 3500')
    return "3200"


def line_3200(state):
    print('3200 IF 8/D*RND(1)>.9 THEN 3310')
    return "3210"


def line_3210(state):
    print('3210 PRINT "PLAYER FOULED.  TWO SHOTS."')
    return "3220"


def line_3220(state):
    print('3220 GOSUB 4000')
    return "3230"


def line_3230(state):
    print('3230 GOTO 425')
    return "3310"


def line_3310(state):
    print('3310 PRINT "OFFENSIVE FOUL.  DARTMOUTHS BALL."')
    return "3320"


def line_3320(state):
    print('3320 GOTO 425')
    return "3500"


def line_3500(state):
    print('3500 IF Z1>3 THEN 3800')
    return "3510"


def line_3510(state):
    print('3510 PRINT "LAY UP."')
    return "3520"


def line_3520(state):
    print('3520 IF 7/D*RND(1)>.413 THEN 3600')
    return "3530"


def line_3530(state):
    print('3530 PRINT "SHOT IS GOOD."')
    return "3540"


def line_3540(state):
    print('3540 GOSUB 6000')
    return "3550"


def line_3550(state):
    print('3550 GOTO 425')
    return "3600"


def line_3600(state):
    print('3600 PRINT "SHOT IS MISSED."')
    return "3610"


def line_3610(state):
    print('3610 GOTO 3110')
    return "3800"


def line_3800(state):
    print('3800 PRINT "SET SHOT."')
    return "3810"


def line_3810(state):
    print('3810 GOTO 3520')
    return "4000"


def line_4000(state):
    print('4000 REM FOUL SHOOTING')
    return "4010"


def line_4010(state):
    print('4010 IF RND(1)>.49 THEN 4050')
    return "4020"


def line_4020(state):
    print('4020 PRINT "SHOOTER MAKES BOTH SHOTS."')
    return "4030"


def line_4030(state):
    print('4030 S(1-P)=S(1-P)+2')
    return "4040"


def line_4040(state):
    print('4040 GOSUB 6010')
    return "4041"


def line_4041(state):
    print('4041 RETURN')
    return "4050"


def line_4050(state):
    print('4050 IF RND(1)>.75 THEN 4100')
    return "4060"


def line_4060(state):
    print('4060 PRINT "SHOOTER MAKES ONE SHOT AND MISSES ONE."')
    return "4070"


def line_4070(state):
    print('4070 S(1-P)=S(1-P)+1')
    return "4080"


def line_4080(state):
    print('4080 GOTO 4040')
    return "4100"


def line_4100(state):
    print('4100 PRINT "BOTH SHOTS MISSED."')
    return "4110"


def line_4110(state):
    print('4110 GOTO 4040')
    return "5000"


def line_5000(state):
    print('5000 IF RND(1)>.75 THEN 5010')
    return "5005"


def line_5005(state):
    print('5005 GOTO 3165')
    return "5010"


def line_5010(state):
    print('5010 PRINT "BALL STOLEN.  EASY LAY UP FOR DARTMOUTH."')
    return "5015"


def line_5015(state):
    print('5015 GOSUB 7000')
    return "5030"


def line_5030(state):
    print('5030 GOTO 3000')
    return "5100"


def line_5100(state):
    print('5100 IF RND(1)>.6 THEN 5120')
    return "5110"


def line_5110(state):
    print('5110 GOTO 1160')
    return "5120"


def line_5120(state):
    print('5120 PRINT "PASS STOLEN BY ";O$;" EASY LAYUP."')
    return "5130"


def line_5130(state):
    print('5130 GOSUB 6000')
    return "5140"


def line_5140(state):
    print('5140 GOTO 425')
    return "6000"


def line_6000(state):
    print('6000 S(0)=S(0)+2')
    return "6010"


def line_6010(state):
    print('6010 PRINT "SCORE: ";S(1);"TO";S(0)')
    return "6020"


def line_6020(state):
    print('6020 RETURN')
    return "7000"


def line_7000(state):
    print('7000 S(1)=S(1)+2')
    return "7010"


def line_7010(state):
    print('7010 GOSUB 6010')
    return "7020"


def line_7020(state):
    print('7020 RETURN')
    return "8000"


def line_8000(state):
    print('8000 PRINT:PRINT "   ***** END OF FIRST HALF *****":PRINT')
    return "8010"


def line_8010(state):
    print('8010 PRINT "SCORE: DARTMOUTH:";S(1);"  ";O$;":";S(0)')
    return "8015"


def line_8015(state):
    print('8015 PRINT')
    return "8016"


def line_8016(state):
    print('8016 PRINT')
    return "8020"


def line_8020(state):
    print('8020 GOTO 370')
    return "9999"


def line_9999(state):
    print('9999 END')
    return ""

program = {"5": line_5,
"7": line_7,
"8": line_8,
"10": line_10,
"20": line_20,
"30": line_30,
"40": line_40,
"60": line_60,
"70": line_70,
"72": line_72,
"76": line_76,
"79": line_79,
"80": line_80,
"370": line_370,
"390": line_390,
"400": line_400,
"410": line_410,
"420": line_420,
"425": line_425,
"430": line_430,
"440": line_440,
"445": line_445,
"446": line_446,
"447": line_447,
"455": line_455,
"460": line_460,
"480": line_480,
"490": line_490,
"491": line_491,
"492": line_492,
"493": line_493,
"494": line_494,
"495": line_495,
"496": line_496,
"499": line_499,
"500": line_500,
"510": line_510,
"515": line_515,
"520": line_520,
"600": line_600,
"610": line_610,
"620": line_620,
"630": line_630,
"1000": line_1000,
"1030": line_1030,
"1040": line_1040,
"1041": line_1041,
"1042": line_1042,
"1043": line_1043,
"1046": line_1046,
"1050": line_1050,
"1060": line_1060,
"1070": line_1070,
"1075": line_1075,
"1085": line_1085,
"1090": line_1090,
"1100": line_1100,
"1105": line_1105,
"1110": line_1110,
"1120": line_1120,
"1130": line_1130,
"1140": line_1140,
"1145": line_1145,
"1150": line_1150,
"1158": line_1158,
"1160": line_1160,
"1170": line_1170,
"1180": line_1180,
"1185": line_1185,
"1187": line_1187,
"1188": line_1188,
"1190": line_1190,
"1195": line_1195,
"1200": line_1200,
"1210": line_1210,
"1230": line_1230,
"1235": line_1235,
"1240": line_1240,
"1242": line_1242,
"1245": line_1245,
"1250": line_1250,
"1255": line_1255,
"1260": line_1260,
"1265": line_1265,
"1270": line_1270,
"1280": line_1280,
"1300": line_1300,
"1301": line_1301,
"1302": line_1302,
"1303": line_1303,
"1304": line_1304,
"1305": line_1305,
"1310": line_1310,
"1320": line_1320,
"1330": line_1330,
"1340": line_1340,
"1345": line_1345,
"1355": line_1355,
"1360": line_1360,
"1370": line_1370,
"1380": line_1380,
"1390": line_1390,
"1400": line_1400,
"1415": line_1415,
"1420": line_1420,
"1430": line_1430,
"1440": line_1440,
"1450": line_1450,
"1500": line_1500,
"1510": line_1510,
"1520": line_1520,
"1530": line_1530,
"1600": line_1600,
"1610": line_1610,
"1620": line_1620,
"1630": line_1630,
"1640": line_1640,
"1700": line_1700,
"1710": line_1710,
"2010": line_2010,
"2030": line_2030,
"2040": line_2040,
"3000": line_3000,
"3005": line_3005,
"3008": line_3008,
"3012": line_3012,
"3015": line_3015,
"3018": line_3018,
"3020": line_3020,
"3030": line_3030,
"3040": line_3040,
"3050": line_3050,
"3060": line_3060,
"3080": line_3080,
"3090": line_3090,
"3100": line_3100,
"3105": line_3105,
"3110": line_3110,
"3120": line_3120,
"3130": line_3130,
"3150": line_3150,
"3160": line_3160,
"3165": line_3165,
"3168": line_3168,
"3170": line_3170,
"3175": line_3175,
"3200": line_3200,
"3210": line_3210,
"3220": line_3220,
"3230": line_3230,
"3310": line_3310,
"3320": line_3320,
"3500": line_3500,
"3510": line_3510,
"3520": line_3520,
"3530": line_3530,
"3540": line_3540,
"3550": line_3550,
"3600": line_3600,
"3610": line_3610,
"3800": line_3800,
"3810": line_3810,
"4000": line_4000,
"4010": line_4010,
"4020": line_4020,
"4030": line_4030,
"4040": line_4040,
"4041": line_4041,
"4050": line_4050,
"4060": line_4060,
"4070": line_4070,
"4080": line_4080,
"4100": line_4100,
"4110": line_4110,
"5000": line_5000,
"5005": line_5005,
"5010": line_5010,
"5015": line_5015,
"5030": line_5030,
"5100": line_5100,
"5110": line_5110,
"5120": line_5120,
"5130": line_5130,
"5140": line_5140,
"6000": line_6000,
"6010": line_6010,
"6020": line_6020,
"7000": line_7000,
"7010": line_7010,
"7020": line_7020,
"8000": line_8000,
"8010": line_8010,
"8015": line_8015,
"8016": line_8016,
"8020": line_8020,
"9999": line_9999,
}

line = "5"
while line:
    line = program[line](state)