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
sensitivities = [{'dA': 11.19411175286923, 'dE0': 0.06783962291377076, 'dn': 0.8453939141597809, 'dA_dEa': -12.164092875005313, 'dE0_dEa': -0.058487583372908526, 'dn_dEa': -0.9279270288987482, 'name': 'C6H6 + C6H4 <=> C12H10'}, {'dA': 5.318816805964719, 'dE0': 0.03187566772046639, 'dn': 0.39715963654129327, 'dA_dEa': 0.8404170546897165, 'dE0_dEa': 0.09562267081775795, 'dn_dEa': 0.06434928853109145, 'name': 'C#C + c1ccc2ccccc2c1 <=> C12H10-2'}, {'dA': 4.822847155186414, 'dE0': 0.029180461740632734, 'dn': 0.3637282596420378, 'dA_dEa': 9.53870709073817, 'dE0_dEa': 0.11428695946525196, 'dn_dEa': 0.7278444124961008, 'name': 'C12H10-3 + C2H2 <=> C14H12'}, {'dA': 5.122725454939423, 'dE0': 0.031018195793358336, 'dn': 0.3866031802327722, 'dA_dEa': 2.89348871896454, 'dE0_dEa': 0.07327828211457725, 'dn_dEa': 0.22087629775842457, 'name': 'C14H10 + C2H2 <=> C16H12'}, {'dA': 2.9733781221427056, 'dE0': 0.016842989163120662, 'dn': 0.2099804176247142, 'dA_dEa': 25.396150541548888, 'dE0_dEa': 0.3424483416733993, 'dn_dEa': 1.9379311249869902, 'name': 'C6H6 + C2H2 <=> C8H8'}, {'dA': 5.294854946751443, 'dE0': 0.03105651632607492, 'dn': 0.3870840248855251, 'dA_dEa': -0.9185621677866197, 'dE0_dEa': 0.1407703789606538, 'dn_dEa': -0.06966776872698952, 'name': 'C10H8 + C2H2 <=> C12H10-2'}, {'dA': 3.8881133501544713, 'dE0': 0.022443389391792752, 'dn': 0.27976511092922973, 'dA_dEa': 13.669496421440726, 'dE0_dEa': 0.30388277465314634, 'dn_dEa': 1.0434328251068046, 'name': 'C10H8-2 + C2H2 <=> C12H10-4'}]
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
sensitivities = [{'dA': -2.252147356002902, 'dE0': -0.018719295062742395, 'dn': 0.30921224280880655, 'dA_dEa': 14.242603977308603, 'dE0_dEa': 0.32361967543258663, 'dn_dEa': -1.8149949789361022, 'name': 'C12H10-3 + C2H2 <=> C14H12'}, {'dA': -0.7665881850335854, 'dE0': -0.007139522335617177, 'dn': 0.11946094220981023, 'dA_dEa': -26.428998662761853, 'dE0_dEa': 0.0071879475957399176, 'dn_dEa': 3.3836554296987247, 'name': 'C14H10 + C2H2 <=> C16H12'}, {'dA': -0.28787576510283913, 'dE0': -0.007432114528984109, 'dn': 0.12189637673241885, 'dA_dEa': -17.698601656269524, 'dE0_dEa': 0.7035707064710113, 'dn_dEa': 2.2848342041048535, 'name': 'C10H8-2 + C2H2 <=> C12H10-4'}]
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
sensitivities = [{'dA': -1.578778641716024, 'dE0': -0.011366765624487157, 'dn': 0.24370328749086237, 'dA_dEa': -20.46730841463654, 'dE0_dEa': 0.03917158693824915, 'dn_dEa': 2.7966123780333665, 'name': 'C#C + c1ccc2ccccc2c1 <=> C12H10-2'}, {'dA': -5.514677139363652, 'dE0': -0.03768496992560363, 'dn': 0.8087497125792978, 'dA_dEa': 37.569252053381824, 'dE0_dEa': 0.590364471861895, 'dn_dEa': -5.143478210804778, 'name': 'C6H6 + C2H2 <=> C8H8'}, {'dA': -0.46882897301353144, 'dE0': -0.005495831589905129, 'dn': 0.11866280642995328, 'dA_dEa': -31.572670370287806, 'dE0_dEa': 0.0732754348970547, 'dn_dEa': 4.31385990171575, 'name': 'C10H8 + C2H2 <=> C12H10-2'}]
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
sensitivities = [{'dA': 1.0362070188635362, 'dE0': 0.007860540962136293, 'dn': -0.05119975175579093, 'dA_dEa': -33.75637284559313, 'dE0_dEa': -0.008915020603906492, 'dn_dEa': 2.0720028496039764, 'name': 'C14H10 + C2H2 <=> C16H12'}, {'dA': 0.07887199376278334, 'dE0': -0.006780638298811699, 'dn': 0.0441187113311616, 'dA_dEa': 20.878645285556797, 'dE0_dEa': 1.4197709818006774, 'dn_dEa': -1.2557849614102667, 'name': 'C10H8-2 + C2H2 <=> C12H10-4'}]
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
sensitivities = [{'dA': 0.488122240657916, 'dE0': 0.00092093733897478, 'dn': -0.013587011297831717, 'dA_dEa': 0.057855585819950026, 'dE0_dEa': 0.29284200579186137, 'dn_dEa': -0.010213666236381038, 'name': 'C#C + c1ccc2ccccc2c1 <=> C12H10-2'}, {'dA': 0.7622251573922996, 'dE0': 0.0006110273799015873, 'dn': -0.009073490029053381, 'dA_dEa': 0.061572662579674316, 'dE0_dEa': 0.47369283353127756, 'dn_dEa': -0.013626979863375814, 'name': 'C10H8 + C2H2 <=> C12H10-2'}]
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

