#!/usr/bin/env python
# encoding: utf-8

name = "Peroxyl_Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(8.59232e+10,'m^3/(mol*s)'), n=-1.53854, w0=(213000,'J/mol'), E0=(5492.44,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07089946866729961, var=0.46390042815407184, Tref=1000.0, N=8, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 8 training reactions at node Root
        Total Standard Deviation in ln(k): 1.5435691658384416"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root
Total Standard Deviation in ln(k): 1.5435691658384416""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root
Total Standard Deviation in ln(k): 1.5435691658384416
sensitivities = [{'dA': -1.6570084095024078, 'dE0': -0.08539606292120488, 'dn': -0.12286603050527706, 'dA_dEa': -1.6327871425440699, 'dE0_dEa': -0.08408609024347966, 'dn_dEa': -0.12098022970017742, 'name': 'CH3OCH2O2-1 + CH3OCH2O2-2 <=> CH3OCH2O + O2 + CH3OCH2O'}, {'dA': -2.073344659948135, 'dE0': -0.11661739254009394, 'dn': -0.16785466186781475, 'dA_dEa': -0.3380815692324663, 'dE0_dEa': 0.054534496754965064, 'dn_dEa': -0.02508413213791774, 'name': 'CH3O2-1 + CH3O2-2 <=> CH3O + O2 + CH3O'}, {'dA': -2.537065311919941, 'dE0': -0.14048843390309965, 'dn': -0.2022152781508539, 'dA_dEa': -0.9051097644104831, 'dE0_dEa': -0.030841743806489748, 'dn_dEa': -0.06706912020658727, 'name': 'C2H5O2-1 + C2H5O2-2 <=> C2H5O + O2 + C2H5O'}, {'dA': 4.716364140279503, 'dE0': 0.23293086523992615, 'dn': 0.33524150889417587, 'dA_dEa': 2.5615710414402293, 'dE0_dEa': 0.09320831031960514, 'dn_dEa': 0.1898195668282268, 'name': 'C2H3O3-1 + CH3O2-2 <=> C2H3O2 + O2 + CH3O'}, {'dA': -1.779191391517028, 'dE0': -0.09201888976977673, 'dn': -0.13239726570494523, 'dA_dEa': -1.7548290926223387, 'dE0_dEa': -0.09338586897849074, 'dn_dEa': -0.13002178174118842, 'name': 'C2H3O3-1 + HO2 <=> C2H3O2 + O2 + OH'}, {'dA': -1.450791082920393, 'dE0': -0.08454456570104539, 'dn': -0.12172937203621406, 'dA_dEa': -1.3430375958131493, 'dE0_dEa': 0.21215097368086558, 'dn_dEa': -0.09809186618907755, 'name': 'CtCOO-1 + CtCOO-2 <=> CtCO + CtCO + O2'}, {'dA': -1.445634230972263, 'dE0': -0.08431814811383324, 'dn': -0.12134038979816837, 'dA_dEa': -1.883888069443381, 'dE0_dEa': 0.2443001992943899, 'dn_dEa': -0.1384982380341266, 'name': 'CbMeEtCOO-1 + CbMeEtCOO-2 <=> CbMeEtCO + CbMeEtCO + O2'}, {'dA': -1.8819728650536345, 'dE0': -0.09849675326997438, 'dn': -0.14171993887440665, 'dA_dEa': -1.2946178835450444, 'dE0_dEa': -0.029554502163239647, 'dn_dEa': -0.0959394706554766, 'name': 'CbMe2COO-1 + CbMe2COO-2 <=> CbMe2CO + CbMe2CO + O2'}]
""",
)

entry(
    index = 2,
    label = "Root_Ext-5R-R",
    kinetics = ArrheniusBM(A=(8.00346e+13,'m^3/(mol*s)'), n=-2.39139, w0=(213000,'J/mol'), E0=(19271,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11014933828574046, var=0.6936015787958725, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-5R-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-5R-R
        Total Standard Deviation in ln(k): 1.9463555546516302"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-5R-R
Total Standard Deviation in ln(k): 1.9463555546516302""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-5R-R
Total Standard Deviation in ln(k): 1.9463555546516302
sensitivities = [{'dA': -0.4594348288052226, 'dE0': -0.039618217869632676, 'dn': -0.038469777458586374, 'dA_dEa': -0.4245657282453875, 'dE0_dEa': -0.03767781609605032, 'dn_dEa': -0.03513644896885519, 'name': 'CH3OCH2O2-1 + CH3OCH2O2-2 <=> CH3OCH2O + O2 + CH3OCH2O'}, {'dA': -5.97319336162693, 'dE0': -0.3461340379649467, 'dn': -0.5650369105772379, 'dA_dEa': 1.0570666465562537, 'dE0_dEa': 0.06676018699719215, 'dn_dEa': 0.0986533883218013, 'name': 'C2H5O2-1 + C2H5O2-2 <=> C2H5O + O2 + C2H5O'}, {'dA': 2.62265147994285, 'dE0': 0.10599872783587305, 'dn': 0.21168911473270746, 'dA_dEa': -14.252658736482864, 'dE0_dEa': -0.2774497191674394, 'dn_dEa': -1.286338502608601, 'name': 'CtCOO-1 + CtCOO-2 <=> CtCO + CtCO + O2'}, {'dA': 2.6229440885966016, 'dE0': 0.10601342147813199, 'dn': 0.21171570214555518, 'dA_dEa': -17.026702405461435, 'dE0_dEa': -0.3255374259664075, 'dn_dEa': -1.5373411311188474, 'name': 'CbMeEtCOO-1 + CbMeEtCOO-2 <=> CbMeEtCO + CbMeEtCO + O2'}, {'dA': 0.06298730114907142, 'dE0': -0.01468985304333402, 'dn': 0.0043555269928148834, 'dA_dEa': -2.193199843919544, 'dE0_dEa': -0.06834645587432095, 'dn_dEa': -0.19516713558494217, 'name': 'CbMe2COO-1 + CbMe2COO-2 <=> CbMe2CO + CbMe2CO + O2'}]
""",
)

entry(
    index = 3,
    label = "Root_Ext-3R-R",
    kinetics = ArrheniusBM(A=(2.13565e+09,'m^3/(mol*s)'), n=-0.982686, w0=(213000,'J/mol'), E0=(9815.71,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.155088700701577, var=3.6678857531903013, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R
        Total Standard Deviation in ln(k): 9.254209245766118"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R
Total Standard Deviation in ln(k): 9.254209245766118""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R
Total Standard Deviation in ln(k): 9.254209245766118
sensitivities = [{'dA': 0.0, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H3O3-1 + CH3O2-2 <=> C2H3O2 + O2 + CH3O'}, {'dA': 0.0, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H3O3-1 + HO2 <=> C2H3O2 + O2 + OH'}]
""",
)

entry(
    index = 4,
    label = "Root_Ext-5R-R_7R!H->C",
    kinetics = ArrheniusBM(A=(6.46293e+13,'m^3/(mol*s)'), n=-2.3617, w0=(213000,'J/mol'), E0=(19109.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.1175239280999607, var=6.252228011041329, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-5R-R_7R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-5R-R_7R!H->C
        Total Standard Deviation in ln(k): 7.820579993842215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-5R-R_7R!H->C
Total Standard Deviation in ln(k): 7.820579993842215""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-5R-R_7R!H->C
Total Standard Deviation in ln(k): 7.820579993842215
sensitivities = [{'dA': -5.002646815076002, 'dE0': -0.280153387054046, 'dn': -0.48551269444359607, 'dA_dEa': 2.0731457758496115, 'dE0_dEa': 0.13579879996000294, 'dn_dEa': 0.18914154719209805, 'name': 'C2H5O2-1 + C2H5O2-2 <=> C2H5O + O2 + C2H5O'}, {'dA': 3.6302594180778858, 'dE0': 0.17455708330787856, 'dn': 0.3024963734911569, 'dA_dEa': -13.249196492631691, 'dE0_dEa': -0.2086223988024646, 'dn_dEa': -1.211101892912081, 'name': 'CtCOO-1 + CtCOO-2 <=> CtCO + CtCO + O2'}, {'dA': 3.630179775381892, 'dE0': 0.17455359606210558, 'dn': 0.30248894861391395, 'dA_dEa': -16.02411803420799, 'dE0_dEa': -0.2566251196816394, 'dn_dEa': -1.4647405024398081, 'name': 'CbMeEtCOO-1 + CbMeEtCOO-2 <=> CbMeEtCO + CbMeEtCO + O2'}, {'dA': 1.0700346172251087, 'dE0': 0.05369923657614318, 'dn': 0.0930520617785532, 'dA_dEa': -1.1866641237433726, 'dE0_dEa': 7.214596116642849e-05, 'dn_dEa': -0.10853899174123867, 'name': 'CbMe2COO-1 + CbMe2COO-2 <=> CbMe2CO + CbMe2CO + O2'}]
""",
)

entry(
    index = 5,
    label = "Root_Ext-5R-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(3.094e+17,'m^3/(mol*s)'), n=-4.5, w0=(213000,'J/mol'), E0=(3793.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-5R-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-5R-R_N-7R!H->C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-5R-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-5R-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH3OCH2O2-1 + CH3OCH2O2-2 <=> CH3OCH2O + O2 + CH3OCH2O'}]
""",
)

entry(
    index = 6,
    label = "Root_Ext-3R-R_5R->C",
    kinetics = ArrheniusBM(A=(1.1e+06,'m^3/(mol*s)'), n=0, w0=(213000,'J/mol'), E0=(5168.55,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_5R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_5R->C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_5R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_5R->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 1.0455599571382066, 'dn_dEa': nan, 'name': 'C2H3O3-1 + CH3O2-2 <=> C2H3O2 + O2 + CH3O'}]
""",
)

entry(
    index = 7,
    label = "Root_Ext-3R-R_N-5R->C",
    kinetics = ArrheniusBM(A=(190000,'m^3/(mol*s)'), n=0, w0=(213000,'J/mol'), E0=(-4877.84,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-5R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-5R->C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-5R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-5R->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': -0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': -0.17016015250306143, 'dn_dEa': nan, 'name': 'C2H3O3-1 + HO2 <=> C2H3O2 + O2 + OH'}]
""",
)

entry(
    index = 8,
    label = "Root_Ext-5R-R_7R!H->C_7C-inRing",
    kinetics = ArrheniusBM(A=(2.74681e+06,'m^3/(mol*s)'), n=-0.0101077, w0=(213000,'J/mol'), E0=(16796.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.8243065462140909, var=3.014120957818995, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-5R-R_7R!H->C_7C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-5R-R_7R!H->C_7C-inRing
        Total Standard Deviation in ln(k): 5.551587432042679"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-5R-R_7R!H->C_7C-inRing
Total Standard Deviation in ln(k): 5.551587432042679""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-5R-R_7R!H->C_7C-inRing
Total Standard Deviation in ln(k): 5.551587432042679
sensitivities = [{'dA': 0.842865482887682, 'dE0': -0.001296994839766162, 'dn': -0.03143513362694728, 'dA_dEa': 0.16164234562234372, 'dE0_dEa': 2.3338636357026696, 'dn_dEa': -0.17122765084077893, 'name': 'CbMeEtCOO-1 + CbMeEtCOO-2 <=> CbMeEtCO + CbMeEtCO + O2'}, {'dA': 0.11667003157179898, 'dE0': -0.0014668430787850505, 'dn': -0.035478558050654696, 'dA_dEa': 0.005296784287623397, 'dE0_dEa': 0.24795267984371328, 'dn_dEa': -0.038419944038432144, 'name': 'CbMe2COO-1 + CbMe2COO-2 <=> CbMe2CO + CbMe2CO + O2'}]
""",
)

entry(
    index = 9,
    label = "Root_Ext-5R-R_7R!H->C_N-7C-inRing",
    kinetics = ArrheniusBM(A=(3.18266e+14,'m^3/(mol*s)'), n=-2.69381, w0=(213000,'J/mol'), E0=(-4280.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1238172880969069, var=0.2143724373616906, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-5R-R_7R!H->C_N-7C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-5R-R_7R!H->C_N-7C-inRing
        Total Standard Deviation in ln(k): 1.2392984962991611"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-5R-R_7R!H->C_N-7C-inRing
Total Standard Deviation in ln(k): 1.2392984962991611""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-5R-R_7R!H->C_N-7C-inRing
Total Standard Deviation in ln(k): 1.2392984962991611
sensitivities = [{'dA': -2.022063295410215, 'dE0': -0.11106062899706808, 'dn': -0.17770035665404776, 'dA_dEa': -4.318046690923203, 'dE0_dEa': -0.20079409162018125, 'dn_dEa': -0.2959430838340313, 'name': 'C2H5O2-1 + C2H5O2-2 <=> C2H5O + O2 + C2H5O'}, {'dA': 1.2684436022888665, 'dE0': 0.023259441370364616, 'dn': 0.05585833285855398, 'dA_dEa': -27.235037380662575, 'dE0_dEa': -0.6730488624369225, 'dn_dEa': -1.8812065843478833, 'name': 'CtCOO-1 + CtCOO-2 <=> CtCO + CtCO + O2'}]
""",
)

entry(
    index = 10,
    label = "Root_Ext-5R-R_7R!H->C_7C-inRing_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(4e+06,'m^3/(mol*s)'), n=0, w0=(213000,'J/mol'), E0=(22550.7,'J/mol'), Tmin=(303,'K'), Tmax=(329,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-5R-R_7R!H->C_7C-inRing_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-5R-R_7R!H->C_7C-inRing_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-5R-R_7R!H->C_7C-inRing_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-5R-R_7R!H->C_7C-inRing_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 1.8235654899150033, 'dn_dEa': nan, 'name': 'CbMeEtCOO-1 + CbMeEtCOO-2 <=> CbMeEtCO + CbMeEtCO + O2'}]
""",
)

entry(
    index = 11,
    label = "Root_Ext-5R-R_7R!H->C_N-7C-inRing_Ext-5R-R",
    kinetics = ArrheniusBM(A=(3.2e+06,'m^3/(mol*s)'), n=0, w0=(213000,'J/mol'), E0=(15374.8,'J/mol'), Tmin=(243,'K'), Tmax=(293,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-5R-R_7R!H->C_N-7C-inRing_Ext-5R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-5R-R_7R!H->C_N-7C-inRing_Ext-5R-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-5R-R_7R!H->C_N-7C-inRing_Ext-5R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-5R-R_7R!H->C_N-7C-inRing_Ext-5R-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 2.479122252093311, 'dn_dEa': nan, 'name': 'CtCOO-1 + CtCOO-2 <=> CtCO + CtCO + O2'}]
""",
)

