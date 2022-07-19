#!/usr/bin/env python
# encoding: utf-8

name = "XY_elimination_hydroxyl/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(8.29471e-53,'s^-1'), n=19.0642, w0=(1.25393e+06,'J/mol'), E0=(-11777.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6030706655901165, var=48.63557807331129, Tref=1000.0, N=14, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 14 training reactions at node Root
        Total Standard Deviation in ln(k): 15.496117553334454"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root
Total Standard Deviation in ln(k): 15.496117553334454""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root
Total Standard Deviation in ln(k): 15.496117553334454
sensitivities = [{'dA': 10.014061226440989, 'dE0': 0.07984592890191988, 'dn': -0.3101787983607087, 'dA_dEa': 40.40954602144754, 'dE0_dEa': 0.43296241238130084, 'dn_dEa': -1.2602988252491178, 'name': 'FCH2CH2COOH <=> C2H4 + HF + CO2'}, {'dA': 11.312380009163371, 'dE0': 0.09022594940584083, 'dn': -0.35070352593940823, 'dA_dEa': -19.616519995310828, 'dE0_dEa': 0.02582093362307338, 'dn_dEa': 0.6126227958883109, 'name': 'CH3CH2COOH <=> C2H4 + H2 + CO2'}, {'dA': 10.014548140129024, 'dE0': 0.07985592034388295, 'dn': -0.31019116132197466, 'dA_dEa': 31.926719058184414, 'dE0_dEa': 0.33009269852060463, 'dn_dEa': -0.9957760984794775, 'name': 'FCH2OCOOH <=> CH2O + HF + CO2'}, {'dA': 10.181703504215777, 'dE0': 0.08119485293693539, 'dn': -0.31540746547768767, 'dA_dEa': 34.3242725889359, 'dE0_dEa': 0.39180225639008665, 'dn_dEa': -1.0703924463597503, 'name': 'BrCH2CH2COOH <=> C2H4 + HBr + CO2'}, {'dA': 10.112408376273367, 'dE0': 0.08063588915555993, 'dn': -0.3132468322088035, 'dA_dEa': 37.574130350709694, 'dE0_dEa': 0.41711112357913355, 'dn_dEa': -1.1718295538988541, 'name': 'ClCH2CH2COOH <=> C2H4 + HCl + CO2'}, {'dA': 10.040679392037562, 'dE0': 0.0800558716464551, 'dn': -0.3110109790973114, 'dA_dEa': 30.964638297628824, 'dE0_dEa': 0.31935479593354277, 'dn_dEa': -0.9657920726906173, 'name': 'BrCH2OCOOH <=> CH2O + HBr + CO2'}, {'dA': 11.11506643509397, 'dE0': 0.08868388007791395, 'dn': -0.3445283768292416, 'dA_dEa': -9.856572453676746, 'dE0_dEa': 0.07522625346020498, 'dn_dEa': 0.30806088861647124, 'name': 'CF3CF2COOH <=> CF2CF2 + HF + CO2'}, {'dA': 10.009952151195593, 'dE0': 0.07981780514677494, 'dn': -0.31004834724923025, 'dA_dEa': 31.459202911136153, 'dE0_dEa': 0.32410485842289083, 'dn_dEa': -0.9811634563294838, 'name': 'ClCH2OCOOH <=> CH2O + HCl + CO2'}, {'dA': 10.752495793584357, 'dE0': 0.08577488162008165, 'dn': -0.3332161005269837, 'dA_dEa': 10.399688770263351, 'dE0_dEa': 0.201940365272195, 'dn_dEa': -0.32380515178610236, 'name': 'CH3CH(OH)CH2CH2F <=> C2H4 + HF + CH3CHO'}, {'dA': 11.493369676146271, 'dE0': 0.0917229292657341, 'dn': -0.35632973047046185, 'dA_dEa': -23.57198038798096, 'dE0_dEa': -0.056833706259855246, 'dn_dEa': 0.735869409388792, 'name': 'CH2C(OH)CH2CH2F <=> C2H4 + HF + CH2CO'}, {'dA': 11.285913776939793, 'dE0': 0.09005752699438294, 'dn': -0.349857498615973, 'dA_dEa': -12.265444397290732, 'dE0_dEa': 0.025021861074302678, 'dn_dEa': 0.38307842642720874, 'name': 'CH2(OH)CH2CH2F <=> C2H4 + HF + CH2O-2'}, {'dA': 10.259379009293987, 'dE0': 0.08182543112741553, 'dn': -0.3178275333986013, 'dA_dEa': 25.041513234265715, 'dE0_dEa': 0.279111179562009, 'dn_dEa': -0.7809401482917687, 'name': 'CH2C(OH)OCH2F <=> CH2O + HF + CH2CO'}, {'dA': 10.453870638855541, 'dE0': 0.08337670639799681, 'dn': -0.3238999754233685, 'dA_dEa': 23.91144167330458, 'dE0_dEa': 0.3166503953623789, 'dn_dEa': -0.7455211914371586, 'name': 'F2C(OH)CH2CH2F <=> C2H4 + HF + CF2O'}, {'dA': 10.255799992658485, 'dE0': 0.08177976121589103, 'dn': -0.31772374432698874, 'dA_dEa': 25.19683607911738, 'dE0_dEa': 0.2726932463708329, 'dn_dEa': -0.7858338832634357, 'name': 'F2C(OH)OCH2F <=> CH2O + HF + CF2O'}]
""",
)

entry(
    index = 2,
    label = "Root_1R!H->C",
    kinetics = ArrheniusBM(A=(786687,'s^-1'), n=2.06826, w0=(1.22572e+06,'J/mol'), E0=(186848,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06572426672533703, var=35.397976975874734, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C
        Total Standard Deviation in ln(k): 12.092548062853473"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 12.092548062853473""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 12.092548062853473
sensitivities = [{'dA': 0.2115170669938726, 'dE0': 0.0005750974626597699, 'dn': -0.009981542684288046, 'dA_dEa': 17.925785111943625, 'dE0_dEa': 0.2197126188916449, 'dn_dEa': -1.7831462566528526, 'name': 'FCH2CH2COOH <=> C2H4 + HF + CO2'}, {'dA': 1.186244534224687, 'dE0': 0.006073749994759814, 'dn': -0.10700470835209419, 'dA_dEa': -15.27751179760441, 'dE0_dEa': 0.11421009026440802, 'dn_dEa': 1.522764070383788, 'name': 'CH3CH2COOH <=> C2H4 + H2 + CO2'}, {'dA': 0.34992164518858304, 'dE0': 0.0013553756843941043, 'dn': -0.023759220901955348, 'dA_dEa': 14.653640727461175, 'dE0_dEa': 0.20958477750549348, 'dn_dEa': -1.45736183661396, 'name': 'BrCH2CH2COOH <=> C2H4 + HBr + CO2'}, {'dA': 0.2904678719453422, 'dE0': 0.0010203766572491175, 'dn': -0.017840415679364428, 'dA_dEa': 16.392751612487572, 'dE0_dEa': 0.21866160095498338, 'dn_dEa': -1.6304526379723663, 'name': 'ClCH2CH2COOH <=> C2H4 + HCl + CO2'}, {'dA': 1.088873932222021, 'dE0': 0.005523339095555432, 'dn': -0.09731488396865273, 'dA_dEa': -10.199477473002773, 'dE0_dEa': 0.11114203247548318, 'dn_dEa': 1.016973416644892, 'name': 'CF3CF2COOH <=> CF2CF2 + HF + CO2'}, {'dA': 0.8003327956594746, 'dE0': 0.003896614572685948, 'dn': -0.06859171053120784, 'dA_dEa': 1.170840716934536, 'dE0_dEa': 0.13553470902660855, 'dn_dEa': -0.11523328568881651, 'name': 'CH3CH(OH)CH2CH2F <=> C2H4 + HF + CH3CHO'}, {'dA': 1.3974215637057459, 'dE0': 0.007262247206020581, 'dn': -0.12803093091781573, 'dA_dEa': -18.700135596953444, 'dE0_dEa': 0.039221215612269156, 'dn_dEa': 1.8628926938127168, 'name': 'CH2C(OH)CH2CH2F <=> C2H4 + HF + CH2CO'}, {'dA': 1.2295293362606619, 'dE0': 0.006316319864725582, 'dn': -0.11131656079344204, 'dA_dEa': -12.382127413617582, 'dE0_dEa': 0.06516965430845283, 'dn_dEa': 1.2339190648193403, 'name': 'CH2(OH)CH2CH2F <=> C2H4 + HF + CH2O-2'}, {'dA': 0.562267503205822, 'dE0': 0.002553283586194893, 'dn': -0.044895788139263426, 'dA_dEa': 8.75118741767008, 'dE0_dEa': 0.18557293990458887, 'dn_dEa': -0.8697092296698584, 'name': 'F2C(OH)CH2CH2F <=> C2H4 + HF + CF2O'}]
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H->C",
    kinetics = ArrheniusBM(A=(3.36992e+13,'s^-1'), n=-0.177525, w0=(1.3047e+06,'J/mol'), E0=(113716,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06700689405116313, var=2.0097828678992498, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R!H->C
        Total Standard Deviation in ln(k): 3.0104080169355436"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 3.0104080169355436""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 3.0104080169355436
sensitivities = [{'dA': -0.21649126333047772, 'dE0': -0.00392959366024854, 'dn': 0.6847767074766421, 'dA_dEa': 7.1582621046858534, 'dE0_dEa': 0.31502385713552056, 'dn_dEa': -11.713743899526246, 'name': 'FCH2OCOOH <=> CH2O + HF + CO2'}, {'dA': -0.1725943849031543, 'dE0': -0.0035121263080446327, 'dn': 0.6126536831692154, 'dA_dEa': 6.028967271920703, 'dE0_dEa': 0.29418306248127046, 'dn_dEa': -9.863517039040339, 'name': 'BrCH2OCOOH <=> CH2O + HBr + CO2'}, {'dA': -0.24313113286924995, 'dE0': -0.004185253942194219, 'dn': 0.728497630703899, 'dA_dEa': 7.588053218307192, 'dE0_dEa': 0.3113455561929528, 'dn_dEa': -12.422032024345336, 'name': 'ClCH2OCOOH <=> CH2O + HCl + CO2'}, {'dA': 0.8183860334548334, 'dE0': 0.00597654538030156, 'dn': -1.0141854950198297, 'dA_dEa': -13.973214946021645, 'dE0_dEa': 0.12673043564619121, 'dn_dEa': 22.974957126627285, 'name': 'CH2C(OH)OCH2F <=> CH2O + HF + CH2CO'}, {'dA': 0.6880987404152753, 'dE0': 0.004727788703088268, 'dn': -0.800326261761262, 'dA_dEa': -9.793403923280065, 'dE0_dEa': 0.14139717251801767, 'dn_dEa': 16.111538155188555, 'name': 'F2C(OH)OCH2F <=> CH2O + HF + CF2O'}]
""",
)

entry(
    index = 4,
    label = "Root_1R!H->C_5Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(68453,'s^-1'), n=2.17099, w0=(1.1725e+06,'J/mol'), E0=(282524,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_5Br1sCl1sF1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_5Br1sCl1sF1sH->H
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_5Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_5Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.2201114138843874, 'dn_dEa': 0.0, 'name': 'CH3CH2COOH <=> C2H4 + H2 + CO2'}]
""",
)

entry(
    index = 5,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(2.25497e+12,'s^-1'), n=0.192523, w0=(1.23238e+06,'J/mol'), E0=(188273,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03627415907183131, var=5.083062161268406, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H
        Total Standard Deviation in ln(k): 4.610946119247431"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 4.610946119247431""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 4.610946119247431
sensitivities = [{'dA': -0.40896336212630285, 'dE0': -0.0031100519288526003, 'dn': 0.15112829111972684, 'dA_dEa': 15.846300659335423, 'dE0_dEa': 0.2281620468171022, 'dn_dEa': -4.48614032386617, 'name': 'FCH2CH2COOH <=> C2H4 + HF + CO2'}, {'dA': -0.24629773580644934, 'dE0': -0.00217079064284776, 'dn': 0.10503351989744772, 'dA_dEa': 12.13313269360006, 'dE0_dEa': 0.21626215093457346, 'dn_dEa': -3.4340058129735636, 'name': 'BrCH2CH2COOH <=> C2H4 + HBr + CO2'}, {'dA': -0.31590209523816454, 'dE0': -0.0025726181949957887, 'dn': 0.12475788903946715, 'dA_dEa': 14.06305286831055, 'dE0_dEa': 0.2265648048677004, 'dn_dEa': -3.980806288002965, 'name': 'ClCH2CH2COOH <=> C2H4 + HCl + CO2'}, {'dA': 0.6232116950820175, 'dE0': 0.002851653971724159, 'dn': -0.14135001116136045, 'dA_dEa': -16.287324342036076, 'dE0_dEa': 0.1002181898273985, 'dn_dEa': 4.620914413163153, 'name': 'CF3CF2COOH <=> CF2CF2 + HF + CO2'}, {'dA': 0.2871089184069181, 'dE0': 0.0009094707489757576, 'dn': -0.046116976066313056, 'dA_dEa': -2.770275526963267, 'dE0_dEa': 0.1325026874122643, 'dn_dEa': 0.7893018383237802, 'name': 'CH3CH(OH)CH2CH2F <=> C2H4 + HF + CH3CHO'}, {'dA': 0.9854692911163119, 'dE0': 0.004942795014462163, 'dn': -0.2440070266400886, 'dA_dEa': -25.028480290838132, 'dE0_dEa': 0.022122082925591133, 'dn_dEa': 7.097058346044204, 'name': 'CH2C(OH)CH2CH2F <=> C2H4 + HF + CH2CO'}, {'dA': 0.7896873115847728, 'dE0': 0.0038121859907684014, 'dn': -0.18852883599295575, 'dA_dEa': -17.82764859985716, 'dE0_dEa': 0.05254551381314856, 'dn_dEa': 5.056312881873985, 'name': 'CH2(OH)CH2CH2F <=> C2H4 + HF + CH2O-2'}, {'dA': 0.004282010632295413, 'dE0': -0.0007235310517851192, 'dn': 0.03402862049581197, 'dA_dEa': 5.3809372103798365, 'dE0_dEa': 0.18796688321529934, 'dn_dEa': -1.52021128584315, 'name': 'F2C(OH)CH2CH2F <=> C2H4 + HF + CF2O'}]
""",
)

entry(
    index = 6,
    label = "Root_N-1R!H->C_5Br1sCl1sF1sH->F1s",
    kinetics = ArrheniusBM(A=(3.91271e+15,'s^-1'), n=-0.91308, w0=(1.3745e+06,'J/mol'), E0=(113186,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09110474360371991, var=4.490802463962393, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_5Br1sCl1sF1sH->F1s',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s
        Total Standard Deviation in ln(k): 4.477243445960722"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 4.477243445960722""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 4.477243445960722
sensitivities = [{'dA': -0.8305007580241357, 'dE0': -0.011263952875037042, 'dn': -0.4137597053498738, 'dA_dEa': 18.908029431904033, 'dE0_dEa': 0.6003418463416496, 'dn_dEa': 6.7027305965904445, 'name': 'FCH2OCOOH <=> CH2O + HF + CO2'}, {'dA': 0.9018135844948033, 'dE0': 0.005543297752181251, 'dn': 0.20201593894302644, 'dA_dEa': -15.912193665348772, 'dE0_dEa': 0.28603360397109023, 'dn_dEa': -5.673258290838497, 'name': 'CH2C(OH)OCH2F <=> CH2O + HF + CH2CO'}, {'dA': 0.6510390273533779, 'dE0': 0.0031164705600650847, 'dn': 0.11284643209847543, 'dA_dEa': -9.530735556581844, 'dE0_dEa': 0.3050096997048341, 'dn_dEa': -3.4035534490286823, 'name': 'F2C(OH)OCH2F <=> CH2O + HF + CF2O'}]
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s",
    kinetics = ArrheniusBM(A=(1.46638e+11,'s^-1'), n=0.708452, w0=(1.2e+06,'J/mol'), E0=(116018,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0002077660778895548, var=2.128133909944111, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s
        Total Standard Deviation in ln(k): 2.925054615266597"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 2.925054615266597""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 2.925054615266597
sensitivities = [{'dA': 0.5812700589765215, 'dE0': 0.0007440376522198359, 'dn': -0.01911102128582736, 'dA_dEa': -1.6992225297444914, 'dE0_dEa': 0.5549588246439706, 'dn_dEa': 0.40307080223886177, 'name': 'BrCH2OCOOH <=> CH2O + HBr + CO2'}, {'dA': 0.41835356313417893, 'dE0': -0.0007591126644735554, 'dn': 0.019031756542124446, 'dA_dEa': 1.9841300711471686, 'dE0_dEa': 0.5943332259410811, 'dn_dEa': -0.4590249421397374, 'name': 'ClCH2OCOOH <=> CH2O + HCl + CO2'}]
""",
)

entry(
    index = 8,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.5706e+11,'s^-1'), n=0.715494, w0=(1.276e+06,'J/mol'), E0=(231823,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_Ext-1C-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = None
""",
)

entry(
    index = 9,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(5.80016e+14,'s^-1'), n=-0.567338, w0=(1.276e+06,'J/mol'), E0=(183244,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07747427306529306, var=2.173071636799296, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s
        Total Standard Deviation in ln(k): 3.149907515166377"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 3.149907515166377""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 3.149907515166377
sensitivities = [{'dA': -0.7566446719665388, 'dE0': -0.005392522463222296, 'dn': 0.5161659036253924, 'dA_dEa': 26.88919971816913, 'dE0_dEa': 0.33959846391749166, 'dn_dEa': -15.030795646584997, 'name': 'FCH2CH2COOH <=> C2H4 + HF + CO2'}, {'dA': 0.6267693647004771, 'dE0': 0.0026513983805564693, 'dn': -0.257715760755202, 'dA_dEa': -13.793683617540706, 'dE0_dEa': 0.18053841670549908, 'dn_dEa': 7.733587454426592, 'name': 'CF3CF2COOH <=> CF2CF2 + HF + CO2'}, {'dA': 0.17814447836885536, 'dE0': 4.073026204482613e-05, 'dn': -0.006780175044463061, 'dA_dEa': 2.3479918420615062, 'dE0_dEa': 0.21294940673822627, 'dn_dEa': -1.3002830844829154, 'name': 'CH3CH(OH)CH2CH2F <=> C2H4 + HF + CH3CHO'}, {'dA': 1.1237764502177854, 'dE0': 0.005534083155352671, 'dn': -0.5358265951210863, 'dA_dEa': -26.531659940789687, 'dE0_dEa': 0.06941497074641413, 'dn_dEa': 14.856791172858859, 'name': 'CH2C(OH)CH2CH2F <=> C2H4 + HF + CH2CO'}, {'dA': 0.850302007389652, 'dE0': 0.003949548892133149, 'dn': -0.3827788525149421, 'dA_dEa': -17.39529318590463, 'dE0_dEa': 0.10754976800178132, 'dn_dEa': 9.74493686530228, 'name': 'CH2(OH)CH2CH2F <=> C2H4 + HF + CH2O-2'}, {'dA': -0.20213874810794957, 'dE0': -0.0021691136825260525, 'dn': 0.20596595869919593, 'dA_dEa': 13.634902339811186, 'dE0_dEa': 0.2897799128686968, 'dn_dEa': -7.614066340879382, 'name': 'F2C(OH)CH2CH2F <=> C2H4 + HF + CF2O'}]
""",
)

entry(
    index = 10,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(3.9456e+10,'s^-1'), n=0.819032, w0=(1.1015e+06,'J/mol'), E0=(191246,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00032049782896238706, var=0.9987135204554455, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s
        Total Standard Deviation in ln(k): 2.0042504079825347"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 2.0042504079825347""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 2.0042504079825347
sensitivities = [{'dA': 0.6382319597442879, 'dE0': 0.0007843147994032417, 'dn': -0.015389317187648537, 'dA_dEa': -4.254971822771594, 'dE0_dEa': 0.550390030265789, 'dn_dEa': 0.4763039256458604, 'name': 'BrCH2CH2COOH <=> C2H4 + HBr + CO2'}, {'dA': 0.3675911061833808, 'dE0': -0.0007528897333597167, 'dn': 0.014676172017476653, 'dA_dEa': 4.008859100807613, 'dE0_dEa': 0.5938946444886065, 'dn_dEa': -0.44188379631500624, 'name': 'ClCH2CH2COOH <=> C2H4 + HCl + CO2'}]
""",
)

entry(
    index = 11,
    label = "Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(5.29418e+10,'s^-1'), n=0.745914, w0=(1.3745e+06,'J/mol'), E0=(117272,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_7R!H->C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.2729930620428505, 'dn_dEa': 0.0, 'name': 'CH2C(OH)OCH2F <=> CH2O + HF + CH2CO'}]
""",
)

entry(
    index = 12,
    label = "Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(6.77496e+17,'s^-1'), n=-1.58758, w0=(1.3745e+06,'J/mol'), E0=(116506,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.030405532278326947, var=15.727862887171884, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C
        Total Standard Deviation in ln(k): 8.026848298408312"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 8.026848298408312""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 8.026848298408312
sensitivities = [{'dA': -0.6207626759860547, 'dE0': -0.010628458408954135, 'dn': -0.233928205898567, 'dA_dEa': 16.518197955585777, 'dE0_dEa': 0.7634899471475419, 'dn_dEa': 3.4393790633546737, 'name': 'FCH2OCOOH <=> CH2O + HF + CO2'}, {'dA': 1.4038861426827633, 'dE0': 0.008518220416588661, 'dn': 0.18891265117547815, 'dA_dEa': -23.064135749119128, 'dE0_dEa': 0.36192518276819025, 'dn_dEa': -4.82797160907297, 'name': 'F2C(OH)OCH2F <=> CH2O + HF + CF2O'}]
""",
)

entry(
    index = 13,
    label = "Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_5Br1sCl1sH->Cl1s",
    kinetics = ArrheniusBM(A=(3.42848e+09,'s^-1'), n=1.33002, w0=(1.227e+06,'J/mol'), E0=(125091,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_5Br1sCl1sH->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_5Br1sCl1sH->Cl1s
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_5Br1sCl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_5Br1sCl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.0742275103562435, 'dn_dEa': 0.0, 'name': 'ClCH2OCOOH <=> CH2O + HCl + CO2'}]
""",
)

entry(
    index = 14,
    label = "Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_N-5Br1sCl1sH->Cl1s",
    kinetics = ArrheniusBM(A=(4.74683e+09,'s^-1'), n=1.36442, w0=(1.173e+06,'J/mol'), E0=(121189,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_N-5Br1sCl1sH->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_N-5Br1sCl1sH->Cl1s
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_N-5Br1sCl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_N-5Br1sCl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.1000138614297714, 'dn_dEa': 0.0, 'name': 'BrCH2OCOOH <=> CH2O + HBr + CO2'}]
""",
)

entry(
    index = 15,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R",
    kinetics = ArrheniusBM(A=(4.9833e+15,'s^-1'), n=-0.802106, w0=(1.276e+06,'J/mol'), E0=(186956,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08107442052799871, var=3.1845085066262686, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R
        Total Standard Deviation in ln(k): 3.7811926598735495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R
Total Standard Deviation in ln(k): 3.7811926598735495""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R
Total Standard Deviation in ln(k): 3.7811926598735495
sensitivities = [{'dA': -0.9123556416953288, 'dE0': -0.006372746738557974, 'dn': 0.2824458321976586, 'dA_dEa': 28.882557720269002, 'dE0_dEa': 0.38257981708562466, 'dn_dEa': -7.32797694432302, 'name': 'FCH2CH2COOH <=> C2H4 + HF + CO2'}, {'dA': 0.710334942642355, 'dE0': 0.0029328427242650227, 'dn': -0.12957462400185876, 'dA_dEa': -20.621716207918578, 'dE0_dEa': 0.1903619423410952, 'dn_dEa': 5.244690508028909, 'name': 'CF3CF2COOH <=> CF2CF2 + HF + CO2'}, {'dA': 0.18268332172512794, 'dE0': -9.482915015754353e-05, 'dn': 0.004392815543479547, 'dA_dEa': -0.4242002506594146, 'dE0_dEa': 0.23344633737218737, 'dn_dEa': 0.11414019076682505, 'name': 'CH3CH(OH)CH2CH2F <=> C2H4 + HF + CH3CHO'}, {'dA': 1.2822473532062864, 'dE0': 0.00620963503560366, 'dn': -0.27480587881254565, 'dA_dEa': -35.232805933642524, 'dE0_dEa': 0.06272948632130244, 'dn_dEa': 8.953535607280687, 'name': 'CH2C(OH)CH2CH2F <=> C2H4 + HF + CH2CO'}, {'dA': -0.26145824536530465, 'dE0': -0.002641186628882234, 'dn': 0.11716917031213514, 'dA_dEa': 12.755704728517243, 'dE0_dEa': 0.3223194340467372, 'dn_dEa': -3.232198950016892, 'name': 'F2C(OH)CH2CH2F <=> C2H4 + HF + CF2O'}]
""",
)

entry(
    index = 16,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_5Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.20378e+08,'s^-1'), n=1.70445, w0=(1.1285e+06,'J/mol'), E0=(197060,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_5Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_5Br1sCl1s->Cl1s
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_5Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_5Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.1001828234364401, 'dn_dEa': 0.0, 'name': 'ClCH2CH2COOH <=> C2H4 + HCl + CO2'}]
""",
)

entry(
    index = 17,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_N-5Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(3.23964e+08,'s^-1'), n=1.60341, w0=(1.0745e+06,'J/mol'), E0=(193601,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_N-5Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_N-5Br1sCl1s->Cl1s
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_N-5Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_N-5Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.1281892083647864, 'dn_dEa': 0.0, 'name': 'BrCH2CH2COOH <=> C2H4 + HBr + CO2'}]
""",
)

entry(
    index = 18,
    label = "Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(6.14547e+10,'s^-1'), n=0.631481, w0=(1.3745e+06,'J/mol'), E0=(98182.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C_Ext-2C-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.296111688787411, 'dn_dEa': 0.0, 'name': 'F2C(OH)OCH2F <=> CH2O + HF + CF2O'}]
""",
)

entry(
    index = 19,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_7R!H->O",
    kinetics = ArrheniusBM(A=(2.6978e+09,'s^-1'), n=1.11971, w0=(1.276e+06,'J/mol'), E0=(193858,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_7R!H->O
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': -1.153315570235363, 'dE0': -0.008908754812711263, 'dn': 0.18425010643736597, 'dA_dEa': 59.77019961830213, 'dE0_dEa': 0.831708727932513, 'dn_dEa': -6.657720996580838, 'name': 'FCH2CH2COOH <=> C2H4 + HF + CO2'}, {'dA': 2.728826197970181, 'dE0': 0.01200498373947288, 'dn': -0.24847242372945771, 'dA_dEa': -65.61168342196322, 'dE0_dEa': 0.37145729014386986, 'dn_dEa': 7.320043237593305, 'name': 'CF3CF2COOH <=> CF2CF2 + HF + CO2'}]
""",
)

entry(
    index = 20,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(1.97392e+12,'s^-1'), n=0.222289, w0=(1.276e+06,'J/mol'), E0=(175596,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.028034265391885454, var=0.7275535203596748, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O
        Total Standard Deviation in ln(k): 1.7804116779216648"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O
Total Standard Deviation in ln(k): 1.7804116779216648""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O
Total Standard Deviation in ln(k): 1.7804116779216648
sensitivities = [{'dA': -0.08759321199037627, 'dE0': -0.002566199821854685, 'dn': 0.11204519344234798, 'dA_dEa': 7.912885562221011, 'dE0_dEa': 0.46774290011024666, 'dn_dEa': -2.0921011098206446, 'name': 'CH3CH(OH)CH2CH2F <=> C2H4 + HF + CH3CHO'}, {'dA': 1.862566030301088, 'dE0': 0.00937410515785378, 'dn': -0.4070187856047865, 'dA_dEa': -54.56253146851499, 'dE0_dEa': 0.1369663464922967, 'dn_dEa': 14.540887564749019, 'name': 'CH2C(OH)CH2CH2F <=> C2H4 + HF + CH2CO'}, {'dA': -0.8821722632746803, 'dE0': -0.007427335337599173, 'dn': 0.32355504458644185, 'dA_dEa': 32.4297903486759, 'dE0_dEa': 0.6413495169553454, 'dn_dEa': -8.617828920205408, 'name': 'F2C(OH)CH2CH2F <=> C2H4 + HF + CF2O'}]
""",
)

entry(
    index = 21,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C",
    kinetics = ArrheniusBM(A=(2.39251e+11,'s^-1'), n=0.443131, w0=(1.276e+06,'J/mol'), E0=(173250,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0002426586333114885, var=0.5095614775048485, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C
        Total Standard Deviation in ln(k): 1.4316612619170346"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C
Total Standard Deviation in ln(k): 1.4316612619170346""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C
Total Standard Deviation in ln(k): 1.4316612619170346
sensitivities = [{'dA': 1.1265844106810439, 'dE0': 0.0038326101179730317, 'dn': -0.10382057238152684, 'dA_dEa': -19.304405426483832, 'dE0_dEa': 0.5106160045410653, 'dn_dEa': 3.208690927634868, 'name': 'CH3CH(OH)CH2CH2F <=> C2H4 + HF + CH3CHO'}, {'dA': -0.1204190934132176, 'dE0': -0.0037884623551365615, 'dn': 0.10272799453121743, 'dA_dEa': 17.14791187677112, 'dE0_dEa': 0.7688725295285738, 'dn_dEa': -2.828559914199603, 'name': 'F2C(OH)CH2CH2F <=> C2H4 + HF + CF2O'}]
""",
)

entry(
    index = 22,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_N-Sp-7BrCClFINPSSi-2C",
    kinetics = ArrheniusBM(A=(1.52349e+10,'s^-1'), n=1.11612, w0=(1.276e+06,'J/mol'), E0=(182141,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_N-Sp-7BrCClFINPSSi-2C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_N-Sp-7BrCClFINPSSi-2C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_N-Sp-7BrCClFINPSSi-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_N-Sp-7BrCClFINPSSi-2C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.4056656023809373, 'dn_dEa': 0.0, 'name': 'CH2C(OH)CH2CH2F <=> C2H4 + HF + CH2CO'}]
""",
)

entry(
    index = 23,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.98542e+10,'s^-1'), n=0.978818, w0=(1.276e+06,'J/mol'), E0=(185739,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C_Ext-2C-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.1913460014802528, 'dn_dEa': 0.0, 'name': 'F2C(OH)CH2CH2F <=> C2H4 + HF + CF2O'}]
""",
)

