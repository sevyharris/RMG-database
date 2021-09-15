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
sensitivities = [{'dA': 0.019725179988940807, 'dE0': 0.0, 'dn': 3.1684411329471816e-05, 'dA_dEa': -0.17023907241766267, 'dE0_dEa': 0.0, 'dn_dEa': 0.01819927887822767, 'name': 'C8H12 <=> C8H12-2'}, {'dA': 0.31959111473515345, 'dE0': 0.0, 'dn': 2.9784021127130425e-05, 'dA_dEa': -2.991817564151563, 'dE0_dEa': 0.0, 'dn_dEa': 0.3197821284773361, 'name': 'C4H8 <=> C4H8-2'}, {'dA': 0.3195967037293098, 'dE0': 0.0, 'dn': 2.9110032382271033e-05, 'dA_dEa': -2.568776282277979, 'dE0_dEa': 0.0, 'dn_dEa': 0.27456568111466506, 'name': 'C5H10 <=> C5H10-2'}, {'dA': 0.31957443476574776, 'dE0': 0.0, 'dn': 3.177651790977435e-05, 'dA_dEa': -3.2033505406413783, 'dE0_dEa': 0.0, 'dn_dEa': 0.34239182665062, 'name': 'C6H12 <=> C6H12-2'}, {'dA': 0.020045193675601855, 'dE0': 0.0, 'dn': -6.567035313557725e-06, 'dA_dEa': -0.06600517864186645, 'dE0_dEa': 0.0, 'dn_dEa': 0.0070536882858450905, 'name': 'CH2S2 <=> CH2S2-2'}]
""",
)

entry(
    index = 2,
    label = "Root_1R!H->C",
    kinetics = ArrheniusBM(A=(8.69088e+06,'s^-1'), n=1.2163, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03637485531705511, var=0.9131482536096799, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C
    Total Standard Deviation in ln(k): 2.007094711412792"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 2.007094711412792""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 2.007094711412792
sensitivities = [{'dA': 0.02020632491373187, 'dE0': 0.0, 'dn': 2.2633418509334106e-05, 'dA_dEa': -0.17362758596919073, 'dE0_dEa': 0.0, 'dn_dEa': 0.01831865244165707, 'name': 'C8H12 <=> C8H12-2'}, {'dA': 0.32616351148110606, 'dE0': 0.0, 'dn': 2.4078770893976887e-05, 'dA_dEa': -3.0526841900954147, 'dE0_dEa': 0.0, 'dn_dEa': 0.3220350406048178, 'name': 'C4H8 <=> C4H8-2'}, {'dA': 0.32616475354000624, 'dE0': 0.0, 'dn': 2.3932883235326745e-05, 'dA_dEa': -2.6211372472995764, 'dE0_dEa': 0.0, 'dn_dEa': 0.27651191859120133, 'name': 'C5H10 <=> C5H10-2'}, {'dA': 0.32616811135003626, 'dE0': 0.0, 'dn': 2.353806351129983e-05, 'dA_dEa': -3.2686594388117434, 'dE0_dEa': 0.0, 'dn_dEa': 0.3448203836713127, 'name': 'C6H12 <=> C6H12-2'}]
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
sensitivities = [{'dA': 0.4999080830075382, 'dE0': 0.0, 'dn': -1.6362970421796746e-05, 'dA_dEa': -4.013329480260895, 'dE0_dEa': 0.0, 'dn_dEa': 0.3728507606994144, 'name': 'C5H10 <=> C5H10-2'}, {'dA': 0.49972853711827087, 'dE0': 0.0, 'dn': 2.3229911663477375e-06, 'dA_dEa': -5.004852307295079, 'dE0_dEa': 0.0, 'dn_dEa': 0.4649662270307751, 'name': 'C6H12 <=> C6H12-2'}]
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

