#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition_Aromatic/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.11393e+21,'m^3/(mol*s)'), n=-4.96127, w0=(542929,'J/mol'), E0=(196526,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4651452533243257, var=30.086343983587437, Tref=1000.0, N=7, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 7 training reactions at node Root
            Total Standard Deviation in ln(k): 12.164883055192815"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 12.164883055192815""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 12.164883055192815
sensitivities = [{'dA': -2.625596075994286, 'dE0': -0.013021575443166105, 'dn': -0.08305168974070645, 'dA_dEa': -28.06833091834047, 'dE0_dEa': -0.11840520784580406, 'dn_dEa': -0.8513120799124095, 'name': 'C6H6 + C6H4 <=> C12H10'}, {'dA': -11.712028126717524, 'dE0': -0.05620262487178556, 'dn': -0.3586482496279786, 'dA_dEa': -10.338435543439745, 'dE0_dEa': 0.0356452196402955, 'dn_dEa': -0.31352577065088416, 'name': 'C#C + c1ccc2ccccc2c1 <=> C12H10-2'}, {'dA': -12.378747555560151, 'dE0': -0.05909947427898247, 'dn': -0.3771237716257871, 'dA_dEa': 2.5615483357415747, 'dE0_dEa': 0.06453631513840154, 'dn_dEa': 0.07772086779666655, 'name': 'C12H10-3 + C2H2 <=> C14H12'}, {'dA': -11.783084832644752, 'dE0': -0.05626864964355592, 'dn': -0.35905704844012803, 'dA_dEa': -9.316723000098253, 'dE0_dEa': 0.007782895156732602, 'dn_dEa': -0.2825561035668633, 'name': 'C14H10 + C2H2 <=> C16H12'}, {'dA': -15.305918042999432, 'dE0': -0.07379882176173669, 'dn': -0.47093576378749025, 'dA_dEa': 29.52689164652936, 'dE0_dEa': 0.31547769025247746, 'dn_dEa': 0.8956715346314212, 'name': 'C6H6 + C2H2 <=> C8H8'}, {'dA': -11.917387087323908, 'dE0': -0.05769526774599486, 'dn': -0.36816003799919694, 'dA_dEa': -9.938301883033446, 'dE0_dEa': 0.089200089464418, 'dn_dEa': -0.30078598939077905, 'name': 'C10H8 + C2H2 <=> C12H10-2'}, {'dA': -13.722598397309673, 'dE0': -0.06627415295460325, 'dn': -0.42291304964457466, 'dA_dEa': 9.50954964878397, 'dE0_dEa': 0.2515143906123577, 'dn_dEa': 0.28854665757987447, 'name': 'C10H8-2 + C2H2 <=> C12H10-4'}]
""",
)

entry(
    index = 2,
    label = "Root_Ext-1CbCbf-R",
    kinetics = ArrheniusBM(A=(5.11966e+06,'m^3/(mol*s)'), n=-1.00646, w0=(553500,'J/mol'), E0=(152881,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1301603542391048, var=34.258277475947885, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-1CbCbf-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-1CbCbf-R
            Total Standard Deviation in ln(k): 14.57342776864884"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-1CbCbf-R
Total Standard Deviation in ln(k): 14.57342776864884""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-1CbCbf-R
Total Standard Deviation in ln(k): 14.57342776864884
sensitivities = [{'dA': 4.77802412610248, 'dE0': 0.02773389114169871, 'dn': 0.7106622409416424, 'dA_dEa': 29.838725800020516, 'dE0_dEa': 0.3785914665602649, 'dn_dEa': 4.591910652564224, 'name': 'C12H10-3 + C2H2 <=> C14H12'}, {'dA': 7.909828666179824, 'dE0': 0.04654469160282239, 'dn': 1.1933765644556884, 'dA_dEa': -40.677447570012724, 'dE0_dEa': -0.046072485805745064, 'dn_dEa': -6.277080994860864, 'name': 'C14H10 + C2H2 <=> C16H12'}, {'dA': 5.408370241542101, 'dE0': 0.028508799356182776, 'dn': 0.7308215460278618, 'dA_dEa': -21.633212976914503, 'dE0_dEa': 0.6557273430983882, 'dn_dEa': -3.36306605543099, 'name': 'C10H8-2 + C2H2 <=> C12H10-4'}]
""",
)

entry(
    index = 3,
    label = "Root_5Ct-inRing",
    kinetics = ArrheniusBM(A=(0.000968167,'m^3/(mol*s)'), n=2.526, w0=(535000,'J/mol'), E0=(53500,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Ct-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_5Ct-inRing
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Ct-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Ct-inRing
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.3060697372636089, 'dn_dEa': 0.0, 'name': 'C6H6 + C6H4 <=> C12H10'}]
""",
)

entry(
    index = 4,
    label = "Root_N-5Ct-inRing",
    kinetics = ArrheniusBM(A=(1.18348e+06,'m^3/(mol*s)'), n=-0.13487, w0=(535000,'J/mol'), E0=(175229,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9442310184100462, var=74.4878913684149, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5Ct-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_N-5Ct-inRing
            Total Standard Deviation in ln(k): 19.674580054137156"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5Ct-inRing
Total Standard Deviation in ln(k): 19.674580054137156""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5Ct-inRing
Total Standard Deviation in ln(k): 19.674580054137156
sensitivities = [{'dA': 2.6918750265870397, 'dE0': 0.013188774998843182, 'dn': -2.3644384648787953, 'dA_dEa': -30.476081107982527, 'dE0_dEa': 0.008607425967468656, 'dn_dEa': 29.022744241168745, 'name': 'C#C + c1ccc2ccccc2c1 <=> C12H10-2'}, {'dA': -3.307704605728299, 'dE0': -0.019016906486016383, 'dn': 3.534535104092953, 'dA_dEa': 73.95093345482022, 'dE0_dEa': 0.726532920566531, 'dn_dEa': -70.48810324588734, 'name': 'C6H6 + C2H2 <=> C8H8'}, {'dA': 4.978260072335254, 'dE0': 0.02384016048547295, 'dn': -4.360874847897776, 'dA_dEa': -50.005444628635054, 'dE0_dEa': 0.010380170948896759, 'dn_dEa': 47.62137536490773, 'name': 'C10H8 + C2H2 <=> C12H10-2'}]
""",
)

entry(
    index = 5,
    label = "Root_Ext-1CbCbf-R_1CbCbf->Cb",
    kinetics = ArrheniusBM(A=(8.46e-06,'m^3/(mol*s)'), n=2.6, w0=(590500,'J/mol'), E0=(190992,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1CbCbf-R_1CbCbf->Cb',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1CbCbf-R_1CbCbf->Cb
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1CbCbf-R_1CbCbf->Cb
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1CbCbf-R_1CbCbf->Cb
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.9239767612853848, 'dn_dEa': 0.0, 'name': 'C12H10-3 + C2H2 <=> C14H12'}]
""",
)

entry(
    index = 6,
    label = "Root_Ext-1CbCbf-R_N-1CbCbf->Cb",
    kinetics = ArrheniusBM(A=(5.89304,'m^3/(mol*s)'), n=0.718971, w0=(535000,'J/mol'), E0=(127560,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3469736613209595, var=0.6454898770400953, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1CbCbf-R_N-1CbCbf->Cb',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbf-R_N-1CbCbf->Cb
            Total Standard Deviation in ln(k): 2.482445085884605"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1CbCbf-R_N-1CbCbf->Cb
Total Standard Deviation in ln(k): 2.482445085884605""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbf-R_N-1CbCbf->Cb
Total Standard Deviation in ln(k): 2.482445085884605
sensitivities = [{'dA': 2.8234828219833363, 'dE0': 0.019381561719422992, 'dn': -0.32620911362715965, 'dA_dEa': -66.50388762338915, 'dE0_dEa': -0.20001132838214153, 'dn_dEa': 8.274746253233427, 'name': 'C14H10 + C2H2 <=> C16H12'}, {'dA': -0.09160405765585754, 'dE0': -0.006768071171032645, 'dn': 0.11043832502422837, 'dA_dEa': 43.73773893308701, 'dE0_dEa': 1.4922970807697868, 'dn_dEa': -5.3855045133043475, 'name': 'C10H8-2 + C2H2 <=> C12H10-4'}]
""",
)

entry(
    index = 7,
    label = "Root_N-5Ct-inRing_Ext-4CbCbf-R_Ext-7R!H-R_Ext-7R!H-R_Ext-4CbCbf-R",
    kinetics = ArrheniusBM(A=(313.369,'m^3/(mol*s)'), n=1.07014, w0=(535000,'J/mol'), E0=(166607,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.243605515613325, var=342.40568138978, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5Ct-inRing_Ext-4CbCbf-R_Ext-7R!H-R_Ext-7R!H-R_Ext-4CbCbf-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-5Ct-inRing_Ext-4CbCbf-R_Ext-7R!H-R_Ext-7R!H-R_Ext-4CbCbf-R
            Total Standard Deviation in ln(k): 47.75835852248233"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5Ct-inRing_Ext-4CbCbf-R_Ext-7R!H-R_Ext-7R!H-R_Ext-4CbCbf-R
Total Standard Deviation in ln(k): 47.75835852248233""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5Ct-inRing_Ext-4CbCbf-R_Ext-7R!H-R_Ext-7R!H-R_Ext-4CbCbf-R
Total Standard Deviation in ln(k): 47.75835852248233
sensitivities = [{'dA': -0.03837131390671967, 'dE0': -0.0019368622555899194, 'dn': 0.037925036718251454, 'dA_dEa': 0.04845614772897556, 'dE0_dEa': 0.2916016502627305, 'dn_dEa': -0.010227842990938929, 'name': 'C#C + c1ccc2ccccc2c1 <=> C12H10-2'}, {'dA': 0.5086972290398456, 'dE0': -0.000787588497020594, 'dn': 0.01544727581820022, 'dA_dEa': 0.1284153945944197, 'dE0_dEa': 0.4721348767703324, 'dn_dEa': -0.021596733311846406, 'name': 'C10H8 + C2H2 <=> C12H10-2'}]
""",
)

entry(
    index = 8,
    label = "Root_Ext-1CbCbf-R_N-1CbCbf->Cb_2CbCbf->Cb",
    kinetics = ArrheniusBM(A=(1.66411e-05,'m^3/(mol*s)'), n=2.69336, w0=(535000,'J/mol'), E0=(136712,'J/mol'), Tmin=(303.03,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1CbCbf-R_N-1CbCbf->Cb_2CbCbf->Cb',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1CbCbf-R_N-1CbCbf->Cb_2CbCbf->Cb
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1CbCbf-R_N-1CbCbf->Cb_2CbCbf->Cb
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1CbCbf-R_N-1CbCbf->Cb_2CbCbf->Cb
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.3158619453646507, 'dn_dEa': 0.0, 'name': 'C10H8-2 + C2H2 <=> C12H10-4'}]
""",
)

entry(
    index = 9,
    label = "Root_Ext-1CbCbf-R_N-1CbCbf->Cb_N-2CbCbf->Cb",
    kinetics = ArrheniusBM(A=(2.162e-05,'m^3/(mol*s)'), n=2.58, w0=(535000,'J/mol'), E0=(127430,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1CbCbf-R_N-1CbCbf->Cb_N-2CbCbf->Cb',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1CbCbf-R_N-1CbCbf->Cb_N-2CbCbf->Cb
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1CbCbf-R_N-1CbCbf->Cb_N-2CbCbf->Cb
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1CbCbf-R_N-1CbCbf->Cb_N-2CbCbf->Cb
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.436549667867211, 'dn_dEa': 0.0, 'name': 'C14H10 + C2H2 <=> C16H12'}]
""",
)

