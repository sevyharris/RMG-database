#!/usr/bin/env python
# encoding: utf-8

name = "Birad_recombination/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.25413e+07,'s^-1'), n=1.20046, w0=(161000,'J/mol'), E0=(16100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07426102205682039, var=5.843756410023497, Tref=1000.0, N=5, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 5 training reactions at node Root
            Total Standard Deviation in ln(k): 5.032804546753876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root
Total Standard Deviation in ln(k): 5.032804546753876""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root
Total Standard Deviation in ln(k): 5.032804546753876
sensitivities = [{'dA': 0.020139418211331247, 'dE0': 0.0, 'dn': -2.148078169706939e-05, 'dA_dEa': -0.14063972220059057, 'dE0_dEa': 0.0, 'dn_dEa': 0.01797726280928475, 'name': 'C8H12 <=> C8H12-2'}, {'dA': 0.31998914390033634, 'dE0': 0.0, 'dn': -2.142523115134104e-05, 'dA_dEa': -2.4778594488561967, 'dE0_dEa': 0.0, 'dn_dEa': 0.31677361800733433, 'name': 'C4H8 <=> C4H8-2'}, {'dA': 0.3199837397361091, 'dE0': 0.0, 'dn': -2.064868789577102e-05, 'dA_dEa': -2.127391698749882, 'dE0_dEa': 0.0, 'dn_dEa': 0.2719683313571401, 'name': 'C5H10 <=> C5H10-2'}, {'dA': 0.32000404996427506, 'dE0': 0.0, 'dn': -2.356214568077914e-05, 'dA_dEa': -2.6530567010463892, 'dE0_dEa': 0.0, 'dn_dEa': 0.33917105215552873, 'name': 'C6H12 <=> C6H12-2'}, {'dA': 0.020527059607646822, 'dE0': 0.0, 'dn': -7.706493055283948e-05, 'dA_dEa': -0.05418238902522063, 'dE0_dEa': 0.0, 'dn_dEa': 0.00691783959584433, 'name': 'CH2S2 <=> CH2S2-2'}]
""",
)

entry(
    index = 2,
    label = "Root_1R!H->C",
    kinetics = ArrheniusBM(A=(8.69088e+06,'s^-1'), n=1.2163, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03637485531705508, var=0.9131482536096801, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C
            Total Standard Deviation in ln(k): 2.0070947114127926"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 2.0070947114127926""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 2.0070947114127926
sensitivities = [{'dA': 0.020007370814314456, 'dE0': 0.0, 'dn': 5.529123177404289e-05, 'dA_dEa': -0.1440651925541817, 'dE0_dEa': 0.0, 'dn_dEa': 0.01818263826667496, 'name': 'C8H12 <=> C8H12-2'}, {'dA': 0.3261278538957772, 'dE0': 0.0, 'dn': 3.3951236053852335e-05, 'dA_dEa': -2.5284399279324474, 'dE0_dEa': 0.0, 'dn_dEa': 0.3190084086713868, 'name': 'C4H8 <=> C4H8-2'}, {'dA': 0.32616864401195084, 'dE0': 0.0, 'dn': 2.8177455058730303e-05, 'dA_dEa': -2.1708260070954113, 'dE0_dEa': 0.0, 'dn_dEa': 0.2738880769897901, 'name': 'C5H10 <=> C5H10-2'}, {'dA': 0.326494612227926, 'dE0': 0.0, 'dn': -1.797207877875525e-05, 'dA_dEa': -2.707573444972709, 'dE0_dEa': 0.0, 'dn_dEa': 0.3416148032709991, 'name': 'C6H12 <=> C6H12-2'}]
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H->C",
    kinetics = ArrheniusBM(A=(2.18e+16,'s^-1'), n=0, w0=(113000,'J/mol'), E0=(11300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330872656, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'CH2S2 <=> CH2S2-2'}]
""",
)

entry(
    index = 4,
    label = "Root_1R!H->C_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2e+12,'s^-1'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(550,'K'), Tmax=(650,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-2R!H-R_Ext-2R!H-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'C8H12 <=> C8H12-2'}]
""",
)

entry(
    index = 5,
    label = "Root_1R!H->C_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.91273e+06,'s^-1'), n=1.38112, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9611482244452804, var=0.025199359283703242, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R
            Total Standard Deviation in ln(k): 2.733183069397409"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.733183069397409""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.733183069397409
sensitivities = [{'dA': 0.499752086391025, 'dE0': 0.0, 'dn': -2.000084910234958e-07, 'dA_dEa': -3.3243049120987074, 'dE0_dEa': 0.0, 'dn_dEa': 0.35860067671911655, 'name': 'C5H10 <=> C5H10-2'}, {'dA': 0.4997277950238849, 'dE0': 0.0, 'dn': 2.669689902977055e-06, 'dA_dEa': -4.145558718530852, 'dE0_dEa': 0.0, 'dn_dEa': 0.4471906673814558, 'name': 'C6H12 <=> C6H12-2'}]
""",
)

entry(
    index = 6,
    label = "Root_1R!H->C_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.21e+10,'s^-1'), n=0.137, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(600,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-4R!H-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H12 <=> C6H12-2'}]
""",
)

