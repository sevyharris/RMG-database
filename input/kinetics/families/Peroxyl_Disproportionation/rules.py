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
sensitivities = [{'dA': -1.6178613268246882, 'dE0': -0.06581496351279292, 'dn': -0.09796059187996103, 'dA_dEa': -1.583842240911967, 'dE0_dEa': -0.06438279731019979, 'dn_dEa': -0.09582787805191141, 'name': 'CH3OCH2O2-1 + CH3OCH2O2-2 <=> CH3OCH2O + O2 + CH3OCH2O'}, {'dA': -3.2695372583372566, 'dE0': -0.1406981745080184, 'dn': -0.20943504750248682, 'dA_dEa': 0.619810774313902, 'dE0_dEa': 0.09375765531931217, 'dn_dEa': 0.037475177679700704, 'name': 'CH3O2-1 + CH3O2-2 <=> CH3O + O2 + CH3O'}, {'dA': -3.9150786791037766, 'dE0': -0.1669140619413039, 'dn': -0.2484969278746687, 'dA_dEa': -0.44182095954786044, 'dE0_dEa': -0.002948688577887788, 'dn_dEa': -0.026732371696101417, 'name': 'C2H5O2-1 + C2H5O2-2 <=> C2H5O + O2 + C2H5O'}, {'dA': 10.13300546051466, 'dE0': 0.40389145664479387, 'dn': 0.6014974549317732, 'dA_dEa': 4.6937743757068, 'dE0_dEa': 0.15384563329732145, 'dn_dEa': 0.2840175407972358, 'name': 'C2H3O3-1 + CH3O2-2 <=> C2H3O2 + O2 + CH3O'}, {'dA': -1.7798528543482035, 'dE0': -0.07265884405017532, 'dn': -0.10815243662779325, 'dA_dEa': -1.7684758358067214, 'dE0_dEa': -0.07475862980253181, 'dn_dEa': -0.10699858936449282, 'name': 'C2H3O3-1 + HO2 <=> C2H3O2 + O2 + OH'}, {'dA': -1.871999239092965, 'dE0': -0.08388753836615047, 'dn': -0.12487969104019767, 'dA_dEa': -1.7853918155632278, 'dE0_dEa': 0.2039562854921901, 'dn_dEa': -0.10810366649018362, 'name': 'CtCOO-1 + CtCOO-2 <=> CtCO + CtCO + O2'}, {'dA': -1.8780194867888802, 'dE0': -0.08410092986948141, 'dn': -0.12524956094161255, 'dA_dEa': -1.9638230490104323, 'dE0_dEa': 0.2522047193021343, 'dn_dEa': -0.11891919578317166, 'name': 'CbMeEtCOO-1 + CbMeEtCOO-2 <=> CbMeEtCO + CbMeEtCO + O2'}, {'dA': -1.8794040375242753, 'dE0': -0.07763981957446642, 'dn': -0.11556980374744473, 'dA_dEa': -1.1243547090275103, 'dE0_dEa': -0.010346336998935435, 'dn_dEa': -0.06803610174779612, 'name': 'CbMe2COO-1 + CbMe2COO-2 <=> CbMe2CO + CbMe2CO + O2'}]
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
sensitivities = [{'dA': 0.0, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH3OCH2O2-1 + CH3OCH2O2-2 <=> CH3OCH2O + O2 + CH3OCH2O'}, {'dA': -5.750602146613127, 'dE0': -0.23511919900125658, 'dn': -0.35998881166095803, 'dA_dEa': 0.9504086891106648, 'dE0_dEa': 0.05784911301050216, 'dn_dEa': 0.056661464716089134, 'name': 'C2H5O2-1 + C2H5O2-2 <=> C2H5O + O2 + C2H5O'}, {'dA': 3.2282505426021406, 'dE0': 0.10813673874298993, 'dn': 0.1737599780073308, 'dA_dEa': -13.967627397691846, 'dE0_dEa': -0.09010572462717081, 'dn_dEa': -0.8365858510080717, 'name': 'CtCOO-1 + CtCOO-2 <=> CtCO + CtCO + O2'}, {'dA': 3.2276343469565205, 'dE0': 0.10811360747972998, 'dn': 0.17372327187630998, 'dA_dEa': -16.60361112598535, 'dE0_dEa': -0.10254943231460133, 'dn_dEa': -0.9944008926230947, 'name': 'CbMeEtCOO-1 + CbMeEtCOO-2 <=> CbMeEtCO + CbMeEtCO + O2'}, {'dA': -0.7487952894465736, 'dE0': -0.02973723305500171, 'dn': -0.04767286752543055, 'dA_dEa': -4.376306748316721, 'dE0_dEa': -0.10943802153029498, 'dn_dEa': -0.2611649196966143, 'name': 'CbMe2COO-1 + CbMe2COO-2 <=> CbMe2CO + CbMe2CO + O2'}]
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
sensitivities = [{'dA': 1.475521692430866, 'dE0': 0.39086699850526063, 'dn': 0.10387091930027553, 'dA_dEa': 4.8131554894196045, 'dE0_dEa': 0.20743491138053427, 'dn_dEa': 0.9203127947568881, 'name': 'C2H3O3-1 + CH3O2-2 <=> C2H3O2 + O2 + CH3O'}, {'dA': -0.48197027733825926, 'dE0': -0.3964366681104736, 'dn': -0.10505938218830929, 'dA_dEa': -0.23492030627639082, 'dE0_dEa': -0.44852842595401116, 'dn_dEa': -0.05143432854075192, 'name': 'C2H3O3-1 + HO2 <=> C2H3O2 + O2 + OH'}]
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
sensitivities = [{'dA': -6.135351074857419, 'dE0': -0.25040415936523347, 'dn': -0.38571133246461964, 'dA_dEa': 0.30855906662455923, 'dE0_dEa': 0.03412385678442981, 'dn_dEa': 0.01850335278685257, 'name': 'C2H5O2-1 + C2H5O2-2 <=> C2H5O + O2 + C2H5O'}, {'dA': 2.5730707564977697, 'dE0': 0.08390646607845233, 'dn': 0.13563789891699127, 'dA_dEa': -14.3457031733101, 'dE0_dEa': -0.1022945178039419, 'dn_dEa': -0.8657878995745454, 'name': 'CtCOO-1 + CtCOO-2 <=> CtCO + CtCO + O2'}, {'dA': 2.5727118575996135, 'dE0': 0.08389257635784468, 'dn': 0.13561643838418638, 'dA_dEa': -16.94618829351855, 'dE0_dEa': -0.1134167892621225, 'dn_dEa': -1.0226203587917846, 'name': 'CbMeEtCOO-1 + CbMeEtCOO-2 <=> CbMeEtCO + CbMeEtCO + O2'}, {'dA': -1.4043536877218925, 'dE0': -0.05413357710522167, 'dn': -0.087439458771021, 'dA_dEa': -5.031682895361044, 'dE0_dEa': -0.1338158879039784, 'dn_dEa': -0.30251008279604574, 'name': 'CbMe2COO-1 + CbMe2COO-2 <=> CbMe2CO + CbMe2CO + O2'}]
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
sensitivities = [{'dA': 1.350145744210145, 'dE0': 0.030092389669718486, 'dn': 7.363016718527758, 'dA_dEa': 1.2890173411827275, 'dE0_dEa': 2.499644797690832, 'dn_dEa': 15.240155176567852, 'name': 'CbMeEtCOO-1 + CbMeEtCOO-2 <=> CbMeEtCO + CbMeEtCO + O2'}, {'dA': 0.6061054334321582, 'dE0': 0.028849177264870744, 'dn': 7.057440190211341, 'dA_dEa': 0.5827151855122923, 'dE0_dEa': 0.2936639403171047, 'dn_dEa': 8.337753266689974, 'name': 'CbMe2COO-1 + CbMe2COO-2 <=> CbMe2CO + CbMe2CO + O2'}]
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
sensitivities = [{'dA': -9.869905891322283, 'dE0': -0.3924156200910114, 'dn': -0.4769629942799198, 'dA_dEa': -5.8191664695505825, 'dE0_dEa': -0.1826651211342267, 'dn_dEa': -0.2680818437664045, 'name': 'C2H5O2-1 + C2H5O2-2 <=> C2H5O + O2 + C2H5O'}, {'dA': 2.554973514385776, 'dE0': 0.06745196441660455, 'dn': 0.09610576204058463, 'dA_dEa': -34.574759588782456, 'dE0_dEa': -0.6170293443222464, 'dn_dEa': -1.5981973405862577, 'name': 'CtCOO-1 + CtCOO-2 <=> CtCO + CtCO + O2'}]
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

