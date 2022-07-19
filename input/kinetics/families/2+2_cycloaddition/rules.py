#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.51258e+21,'m^3/(mol*s)'), n=-4.73433, w0=(662667,'J/mol'), E0=(260353,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.24606408429282084, var=11.431364239445765, Tref=1000.0, N=6, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 2 training reactions at node Root
            Total Standard Deviation in ln(k): 7.3963210190210456"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 7.3963210190210456""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 7.3963210190210456
sensitivities = [{'dA': 0.05336239581766355, 'dE0': -0.00047100272930603477, 'dn': -0.005304212414022817, 'dA_dEa': 27.160206459004293, 'dE0_dEa': 0.2676147005834102, 'dn_dEa': 1.267965408608072, 'name': 'CH2O + C2H4 <=> C3H6O'}, {'dA': 7.679328812614862, 'dE0': 0.03220416506440402, 'dn': 0.35069058133831804, 'dA_dEa': -207.21473751020065, 'dE0_dEa': -0.672490550026557, 'dn_dEa': -9.673094161447363, 'name': 'CH2O + C2H3O <=> C3H5O2'}, {'dA': 0.053816529522527176, 'dE0': -0.00046920586460669287, 'dn': -0.005282820171710227, 'dA_dEa': 27.85873302320448, 'dE0_dEa': 0.2748486270560189, 'dn_dEa': 1.3005610783189223, 'name': 'CH2O + C2H4 <=> C3H6O'}, {'dA': 0.761986699501533, 'dE0': 0.0025653656702814467, 'dn': 0.027775585439318625, 'dA_dEa': 5.514029204079559, 'dE0_dEa': 0.14573658926985475, 'dn_dEa': 0.2574654839004508, 'name': 'CH2S + C2H4 <=> C3H6S'}, {'dA': 0.053459218669621784, 'dE0': -0.0004706083757531868, 'dn': -0.005299669381827921, 'dA_dEa': 18.24150244145729, 'dE0_dEa': 0.20027858292967501, 'dn_dEa': 0.851596985610351, 'name': 'CH2O + C2H4 <=> C3H6O'}, {'dA': 0.9304859253235124, 'dE0': 0.003287198833404797, 'dn': 0.035641641265161554, 'dA_dEa': 2.783611149084515, 'dE0_dEa': 0.13404198310125184, 'dn_dEa': 0.12999837202468145, 'name': 'C2H2O + C2H4 <=> C4H6O'}]
""",
)

entry(
    index = 2,
    label = "Root_1COCSCdCdd->Cd",
    kinetics = ArrheniusBM(A=(0.0195885,'m^3/(mol*s)'), n=2.14699, w0=(658200,'J/mol'), E0=(219998,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04346154203493252, var=5.777042437712499, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1COCSCdCdd->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd
            Total Standard Deviation in ln(k): 4.927676610542817"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd
Total Standard Deviation in ln(k): 4.927676610542817""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd
Total Standard Deviation in ln(k): 4.927676610542817
sensitivities = [{'dA': -0.3165206308289108, 'dE0': -0.0025479635939612932, 'dn': 0.02362538047736504, 'dA_dEa': 16.327223385324906, 'dE0_dEa': 0.2894999106345646, 'dn_dEa': -0.7465004347633803, 'name': 'CH2O + C2H4 <=> C3H6O'}, {'dA': -0.3151262974761329, 'dE0': -0.0025423978104702374, 'dn': 0.02356012455388708, 'dA_dEa': 16.790633900136317, 'dE0_dEa': 0.29762629824069836, 'dn_dEa': -0.7676919070747015, 'name': 'CH2O + C2H4 <=> C3H6O'}, {'dA': 0.8678502544779821, 'dE0': 0.0032946117432910583, 'dn': -0.03055881484752825, 'dA_dEa': -15.228820470754812, 'dE0_dEa': 0.0935754425439298, 'dn_dEa': 0.6970698938768796, 'name': 'CH2S + C2H4 <=> C3H6S'}, {'dA': -0.3191968150062859, 'dE0': -0.0025600291840999177, 'dn': 0.023749133498991444, 'dA_dEa': 13.189721403694353, 'dE0_dEa': 0.23377295179473356, 'dn_dEa': -0.6030518148586003, 'name': 'CH2O + C2H4 <=> C3H6O'}, {'dA': 1.1505923991369673, 'dE0': 0.004688639643524269, 'dn': -0.04349500808045434, 'dA_dEa': -21.292914769060047, 'dE0_dEa': 0.06366123478903415, 'dn_dEa': 0.9744986814395432, 'name': 'C2H2O + C2H4 <=> C4H6O'}]
""",
)

entry(
    index = 3,
    label = "Root_N-1COCSCdCdd->Cd",
    kinetics = ArrheniusBM(A=(2.73271e-32,'m^3/(mol*s)'), n=10.9581, w0=(685000,'J/mol'), E0=(68500,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCSCdCdd->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCSCdCdd->Cd
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCSCdCdd->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCSCdCdd->Cd
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH2O + C2H3O <=> C3H5O2'}]
""",
)

entry(
    index = 4,
    label = "Root_1COCSCdCdd->Cd_3COCSCdCdd->CO",
    kinetics = ArrheniusBM(A=(0.113741,'m^3/(mol*s)'), n=2.0246, w0=(700500,'J/mol'), E0=(222212,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013070562052782878, var=13.242392200388787, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1COCSCdCdd->Cd_3COCSCdCdd->CO',), comment="""BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_3COCSCdCdd->CO
            Total Standard Deviation in ln(k): 7.328091167028413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_3COCSCdCdd->CO
Total Standard Deviation in ln(k): 7.328091167028413""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_3COCSCdCdd->CO
Total Standard Deviation in ln(k): 7.328091167028413
sensitivities = [{'dA': 0.3330626347715449, 'dE0': -5.178118236666293e-07, 'dn': 3.7511981618775598e-06, 'dA_dEa': -0.0034054884174853782, 'dE0_dEa': 0.3485987021042011, 'dn_dEa': 0.00033897140735620777, 'name': 'CH2O + C2H4 <=> C3H6O'}, {'dA': 0.33202605787256195, 'dE0': -5.225591084908536e-06, 'dn': 4.141528288666302e-05, 'dA_dEa': -0.002339209467905592, 'dE0_dEa': 0.3583526963794053, 'dn_dEa': 0.0003061840646099652, 'name': 'CH2O + C2H4 <=> C3H6O'}, {'dA': 0.33382242629191106, 'dE0': 3.018079491037164e-06, 'dn': -2.3784620191868677e-05, 'dA_dEa': -0.0007604883585089211, 'dE0_dEa': 0.281462618928915, 'dn_dEa': 0.00020143988663750902, 'name': 'CH2O + C2H4 <=> C3H6O'}]
""",
)

entry(
    index = 5,
    label = "Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO",
    kinetics = ArrheniusBM(A=(66.1612,'m^3/(mol*s)'), n=0.949831, w0=(594750,'J/mol'), E0=(226339,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.010964617442947782, var=1.2507574696173305, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO',), comment="""BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO
            Total Standard Deviation in ln(k): 2.2695902476071947"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO
Total Standard Deviation in ln(k): 2.2695902476071947""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO
Total Standard Deviation in ln(k): 2.2695902476071947
sensitivities = [{'dA': 0.1588736128033294, 'dE0': -0.0016224437938369156, 'dn': 0.05516033991124069, 'dA_dEa': 7.06958724915452, 'dE0_dEa': 0.44093818246415234, 'dn_dEa': -1.1376232863538382, 'name': 'CH2S + C2H4 <=> C3H6S'}, {'dA': 0.8343814771195421, 'dE0': 0.0015955965050592235, 'dn': -0.05413742754861142, 'dA_dEa': -7.524505068853434, 'dE0_dEa': 0.3714202679403727, 'dn_dEa': 1.2237382060445101, 'name': 'C2H2O + C2H4 <=> C4H6O'}]
""",
)

entry(
    index = 6,
    label = "Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO_3CSCd->Cd",
    kinetics = ArrheniusBM(A=(19.0618,'m^3/(mol*s)'), n=1.0884, w0=(602000,'J/mol'), E0=(227200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO_3CSCd->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO_3CSCd->Cd
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO_3CSCd->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO_3CSCd->Cd
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.7983439585669599, 'dn_dEa': nan, 'name': 'C2H2O + C2H4 <=> C4H6O'}]
""",
)

entry(
    index = 7,
    label = "Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO_N-3CSCd->Cd",
    kinetics = ArrheniusBM(A=(965.19,'m^3/(mol*s)'), n=0.627082, w0=(587500,'J/mol'), E0=(226772,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO_N-3CSCd->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO_N-3CSCd->Cd
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO_N-3CSCd->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO_N-3CSCd->Cd
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.8126025200366687, 'dn_dEa': nan, 'name': 'CH2S + C2H4 <=> C3H6S'}]
""",
)

