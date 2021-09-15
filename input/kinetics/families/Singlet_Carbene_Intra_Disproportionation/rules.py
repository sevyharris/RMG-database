#!/usr/bin/env python
# encoding: utf-8

name = "Singlet_Carbene_Intra_Disproportionation/rules"
shortDesc = "Convert a singlet carbene to a closed-shell molecule through a concerted 1,2-H shift + 1,2-bond formation"
longDesc = """
Reaction site *1 should always be a singlet in this family.
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.95161e+18,'s^-1'), n=-1.97082, w0=(539000,'J/mol'), E0=(112289,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.830576393636001, var=17.04186713927747, Tref=1000.0, N=4, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 4 training reactions at node Root
    Total Standard Deviation in ln(k): 10.362781890784488"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root
Total Standard Deviation in ln(k): 10.362781890784488""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root
Total Standard Deviation in ln(k): 10.362781890784488
sensitivities = [{'dA': 1.8424165295629433, 'dE0': 0.016300478566179527, 'dn': 0.10395314072641948, 'dA_dEa': -16.113286874885446, 'dE0_dEa': -0.06792019465906592, 'dn_dEa': -1.050177335044944, 'name': 'C6H6 <=> C6H6-2'}, {'dA': 10.102476176592436, 'dE0': 0.1008433926657503, 'dn': 0.6431293952290423, 'dA_dEa': -1.3680273146478414, 'dE0_dEa': -0.011536689942575116, 'dn_dEa': -0.08924875824551595, 'name': 'C6H6-3 <=> C6H6-4'}, {'dA': -6.723216118815175, 'dE0': -0.07138229896942776, 'dn': -0.4551632938353086, 'dA_dEa': 63.06239407432185, 'dE0_dEa': 0.8977754434888136, 'dn_dEa': 4.120580037008631, 'name': '[C]1C=CC=CC1 <=> C6H6-5'}, {'dA': -4.175597624091159, 'dE0': -0.045319698164394476, 'dn': -0.2888565417665357, 'dA_dEa': 9.812708991277589, 'dE0_dEa': 0.17624271700203392, 'dn_dEa': 0.6417922865832815, 'name': '[C]1C=CCC=C1 <=> C6H6-7'}]
""",
)

entry(
    index = 2,
    label = "Root_Ext-3C-R_Ext-4R!H-R_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1234.65,'s^-1'), n=2.90797, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.0720040911798123, var=5.164887496394838, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3C-R_Ext-4R!H-R_Sp-4R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3C-R_Ext-4R!H-R_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 9.762079318807448"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3C-R_Ext-4R!H-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 9.762079318807448""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3C-R_Ext-4R!H-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 9.762079318807448
sensitivities = [{'dA': 0.5006463776720534, 'dE0': 0.0, 'dn': -4.4158704501678525e-05, 'dA_dEa': -18.95625542166566, 'dE0_dEa': 0.0, 'dn_dEa': 0.8364146872209017, 'name': 'C6H6 <=> C6H6-2'}, {'dA': 0.4999330041402512, 'dE0': 0.0, 'dn': -8.955285163305893e-06, 'dA_dEa': -0.48341928294709285, 'dE0_dEa': 0.0, 'dn_dEa': 0.021327459804025884, 'name': 'C6H6-3 <=> C6H6-4'}]
""",
)

entry(
    index = 3,
    label = "Root_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1.19752e-13,'s^-1'), n=7.15292, w0=(539000,'J/mol'), E0=(-2634.84,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2245170669211892, var=51.16218975222246, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 14.90353211384042"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 14.90353211384042""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 14.90353211384042
sensitivities = [{'dA': 0.5000224610896549, 'dE0': -0.0, 'dn': -5.844458626521459e-06, 'dA_dEa': -49.336204323720985, 'dE0_dEa': -0.0, 'dn_dEa': 0.8849999938506486, 'name': '[C]1C=CC=CC1 <=> C6H6-5'}, {'dA': 0.4999064080025146, 'dE0': -0.0, 'dn': -3.5175920808965844e-06, 'dA_dEa': -14.815353779303065, 'dE0_dEa': -0.0, 'dn_dEa': 0.26575949199668697, 'name': '[C]1C=CCC=C1 <=> C6H6-7'}]
""",
)

entry(
    index = 4,
    label = "Root_Ext-3C-R_Ext-4R!H-R_Sp-4R!H-1C_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(8.067e+10,'s^-1'), n=0.649, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_Ext-4R!H-R_Sp-4R!H-1C_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-4R!H-R_Sp-4R!H-1C_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-4R!H-R_Sp-4R!H-1C_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-4R!H-R_Sp-4R!H-1C_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H6 <=> C6H6-2'}]
""",
)

entry(
    index = 5,
    label = "Root_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.61832e+16,'s^-1'), n=-0.885455, w0=(539000,'J/mol'), E0=(109382,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.8091245559088774, 'dn_dEa': -0.0, 'name': '[C]1C=CC=CC1 <=> C6H6-5'}]
""",
)

entry(
    index = 6,
    label = "Root_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(4.66894e+13,'s^-1'), n=-1.27142, w0=(539000,'J/mol'), E0=(78261.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.4126129236126302, 'dn_dEa': -0.0, 'name': '[C]1C=CCC=C1 <=> C6H6-7'}]
""",
)

