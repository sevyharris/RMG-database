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
sensitivities = [{'dA': 2.2293505157054097, 'dE0': 0.006716450381503214, 'dn': 0.03638531068723998, 'dA_dEa': 50.41870591684572, 'dE0_dEa': 0.3028004376524773, 'dn_dEa': 0.8893621200583052, 'name': 'CH2O + C2H4 <=> C3H6O'}, {'dA': 13.889590651460646, 'dE0': 0.044669891955026776, 'dn': 0.2420697637523695, 'dA_dEa': -334.52075865688744, 'dE0_dEa': -0.8913363261067456, 'dn_dEa': -5.9009244062376665, 'name': 'CH2O + C2H3O <=> C3H5O2'}, {'dA': 2.229390882718253, 'dE0': 0.006716583996409044, 'dn': 0.03638602135840148, 'dA_dEa': 51.7497389661287, 'dE0_dEa': 0.3110068448886102, 'dn_dEa': 0.9128438406746269, 'name': 'CH2O + C2H4 <=> C3H6O'}, {'dA': 3.3916767318235412, 'dE0': 0.01049964245992055, 'dn': 0.05688860404931534, 'dA_dEa': 11.57258060193683, 'dE0_dEa': 0.14963914296314332, 'dn_dEa': 0.20413059109460796, 'name': 'CH2S + C2H4 <=> C3H6S'}, {'dA': 2.2292547657232444, 'dE0': 0.006716145056554085, 'dn': 0.03638361836466081, 'dA_dEa': 41.42489341444845, 'dE0_dEa': 0.24680548973474664, 'dn_dEa': 0.7307202729552936, 'name': 'CH2O + C2H4 <=> C3H6O'}, {'dA': 3.65790658119676, 'dE0': 0.011366033084040163, 'dn': 0.06158496082575321, 'dA_dEa': 7.085183106412599, 'dE0_dEa': 0.1350402663949817, 'dn_dEa': 0.124968951352439, 'name': 'C2H2O + C2H4 <=> C4H6O'}]
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
sensitivities = [{'dA': -0.6749050508521781, 'dE0': -0.003561777634189902, 'dn': 0.042640375368388425, 'dA_dEa': 33.604992450473475, 'dE0_dEa': 0.3450606421315924, 'dn_dEa': -1.637538790649847, 'name': 'CH2O + C2H4 <=> C3H6O'}, {'dA': -0.674841574089665, 'dE0': -0.003561512366704956, 'dn': 0.042637294511775996, 'dA_dEa': 34.54504495412561, 'dE0_dEa': 0.3547114767281033, 'dn_dEa': -1.6833467047764972, 'name': 'CH2O + C2H4 <=> C3H6O'}, {'dA': 1.5157732104704174, 'dE0': 0.005358395952129277, 'dn': -0.06413821969097003, 'dA_dEa': -31.977749892976494, 'dE0_dEa': 0.03790219039710768, 'dn_dEa': 1.5590165908203644, 'name': 'CH2S + C2H4 <=> C3H6S'}, {'dA': -0.6733526565190959, 'dE0': -0.0035558609921610075, 'dn': 0.04256413231585054, 'dA_dEa': 27.164540676858245, 'dE0_dEa': 0.2787263190111055, 'dn_dEa': -1.3237057455429215, 'name': 'CH2O + C2H4 <=> C3H6O'}, {'dA': 2.0143295921457582, 'dE0': 0.0073886853941064, 'dn': -0.08843865372908719, 'dA_dEa': -44.27448560623536, 'dE0_dEa': -0.012170152013253239, 'dn_dEa': 2.158384991992425, 'name': 'C2H2O + C2H4 <=> C4H6O'}]
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
sensitivities = [{'dA': 0.31827842415225355, 'dE0': -5.63619345189153e-05, 'dn': 0.0006867149758792287, 'dA_dEa': -0.0935386683167497, 'dE0_dEa': 0.3424702743490375, 'dn_dEa': 0.004645611868652943, 'name': 'CH2O + C2H4 <=> C3H6O'}, {'dA': 0.32281596664422096, 'dE0': -3.93147313073457e-05, 'dn': 0.0004772483073638072, 'dA_dEa': -0.10563751737714452, 'dE0_dEa': 0.35201196972242565, 'dn_dEa': 0.0052130974680597245, 'name': 'CH2O + C2H4 <=> C3H6O'}, {'dA': 0.32700692477320153, 'dE0': -2.329664424934264e-05, 'dn': 0.00028415778772482883, 'dA_dEa': -0.07912682842104762, 'dE0_dEa': 0.27649205796493054, 'dn_dEa': 0.003917336011771752, 'name': 'CH2O + C2H4 <=> C3H6O'}]
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
sensitivities = [{'dA': -0.13018100338070596, 'dE0': -0.0024912129133565367, 'dn': 0.08978119268509145, 'dA_dEa': 14.653864779245412, 'dE0_dEa': 0.46640510196859014, 'dn_dEa': -2.0841256950522555, 'name': 'CH2S + C2H4 <=> C3H6S'}, {'dA': 1.1204136279908807, 'dE0': 0.0024564587342261065, 'dn': -0.08845242182695832, 'dA_dEa': -15.084711075377895, 'dE0_dEa': 0.3487285831574059, 'dn_dEa': 2.15408391843224, 'name': 'C2H2O + C2H4 <=> C4H6O'}]
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

