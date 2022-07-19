#!/usr/bin/env python
# encoding: utf-8

name = "1,3_NH3_elimination/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(8.13848e+28,'s^-1'), n=-4.81619, w0=(650125,'J/mol'), E0=(293679,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.14582612901420383, var=13.966892144572673, Tref=1000.0, N=4, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 4 training reactions at node Root
            Total Standard Deviation in ln(k): 7.858554474439377"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root
Total Standard Deviation in ln(k): 7.858554474439377""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root
Total Standard Deviation in ln(k): 7.858554474439377
sensitivities = [{'dA': 6.288919467601044, 'dE0': 0.024085608249412718, 'dn': 0.458258837353428, 'dA_dEa': -131.44271739734873, 'dE0_dEa': -0.36023649591348217, 'dn_dEa': -10.084232645200405, 'name': 'NH2NNH_r <=> NH3 + N2'}, {'dA': -4.249733365789623, 'dE0': -0.018402779290843448, 'dn': -0.3503604016645166, 'dA_dEa': 89.41179943542029, 'dE0_dEa': 0.62492183001513, 'dn_dEa': 6.863214017474296, 'name': 'N3 <=> N2H2 + NH3'}, {'dA': -3.221411077156588, 'dE0': -0.01425300837899607, 'dn': -0.27146742005791147, 'dA_dEa': 57.57999599978015, 'dE0_dEa': 0.47934581643185475, 'dn_dEa': 4.4205318077503515, 'name': 'N4 <=> NH2NNH_p + NH3'}, {'dA': -1.6437771597496853, 'dE0': -0.006820335468678125, 'dn': -0.13003350357887156, 'dA_dEa': 16.352243537072678, 'dE0_dEa': 0.11786338300090675, 'dn_dEa': 1.2552305775144914, 'name': 'NCC <=> C2H4 + NH3'}]
""",
)

entry(
    index = 2,
    label = "Root_Sp-3R!H-2R!H",
    kinetics = ArrheniusBM(A=(1.97485e+10,'s^-1'), n=0.469968, w0=(623000,'J/mol'), E0=(253467,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1154245615347588, var=1.7024423165047282, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Sp-3R!H-2R!H',), comment="""BM rule fitted to 3 training reactions at node Root_Sp-3R!H-2R!H
            Total Standard Deviation in ln(k): 2.905743140982356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Sp-3R!H-2R!H
Total Standard Deviation in ln(k): 2.905743140982356""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Sp-3R!H-2R!H
Total Standard Deviation in ln(k): 2.905743140982356
sensitivities = [{'dA': -0.544997236861693, 'dE0': -0.0044063965945647455, 'dn': 0.13895592075221253, 'dA_dEa': 24.92755725045645, 'dE0_dEa': 0.5298965324542634, 'dn_dEa': -3.4417818045894446, 'name': 'N3 <=> N2H2 + NH3'}, {'dA': 1.6116544945854014, 'dE0': 0.005037925411613529, 'dn': -0.15837107523463576, 'dA_dEa': -29.443573218177168, 'dE0_dEa': 0.264211514793073, 'dn_dEa': 4.0540767830420315, 'name': 'N4 <=> NH2NNH_p + NH3'}, {'dA': -0.12462015086357732, 'dE0': -0.0008616206192898764, 'dn': 0.02741976312230372, 'dA_dEa': 4.646423207475948, 'dE0_dEa': 0.10298359504292791, 'dn_dEa': -0.6415713136075828, 'name': 'NCC <=> C2H4 + NH3'}]
""",
)

entry(
    index = 3,
    label = "Root_N-Sp-3R!H-2R!H",
    kinetics = ArrheniusBM(A=(4.9e+09,'s^-1'), n=1.34, w0=(731500,'J/mol'), E0=(256182,'J/mol'), Tmin=(500,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-Sp-3R!H-2R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-Sp-3R!H-2R!H
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-Sp-3R!H-2R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-Sp-3R!H-2R!H
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.5916504807565811, 'dn_dEa': 0.0, 'name': 'NH2NNH_r <=> NH3 + N2'}]
""",
)

entry(
    index = 4,
    label = "Root_Sp-3R!H-2R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.52e+09,'s^-1'), n=0.95, w0=(595000,'J/mol'), E0=(267575,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Sp-3R!H-2R!H_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Sp-3R!H-2R!H_Ext-3R!H-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Sp-3R!H-2R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Sp-3R!H-2R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.8231882635259662, 'dn_dEa': 0.0, 'name': 'N4 <=> NH2NNH_p + NH3'}]
""",
)

entry(
    index = 5,
    label = "Root_Sp-3R!H-2R!H_2R!H->C",
    kinetics = ArrheniusBM(A=(16333.3,'s^-1'), n=2.65, w0=(679000,'J/mol'), E0=(243587,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Sp-3R!H-2R!H_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Sp-3R!H-2R!H_2R!H->C
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Sp-3R!H-2R!H_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Sp-3R!H-2R!H_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.1183772315674445, 'dn_dEa': 0.0, 'name': 'NCC <=> C2H4 + NH3'}]
""",
)

entry(
    index = 6,
    label = "Root_Sp-3R!H-2R!H_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.13e+08,'s^-1'), n=1.06, w0=(595000,'J/mol'), E0=(249159,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Sp-3R!H-2R!H_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Sp-3R!H-2R!H_N-2R!H->C
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Sp-3R!H-2R!H_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Sp-3R!H-2R!H_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.9001661139884706, 'dn_dEa': 0.0, 'name': 'N3 <=> N2H2 + NH3'}]
""",
)

