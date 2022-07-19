#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/rules"
shortDesc = ""
longDesc = """
For some reason the definition of Cs_rad::

 Cs_rad
 1 * C 1 

which is not mutually exclusive from its L2 siblings such as::

 Cd_rad
 1 * C 1 {2,D}, {3,S}
 2   C 0 {1,D}
 3   R 0 {1,S}

is apparently not causing a problem
"""
entry(
    index = 1,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R",
    kinetics = ArrheniusBM(A=(7.98328e+06,'m^3/(mol*s)'), n=-8.3375e-07, w0=(122000,'J/mol'), E0=(12200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.6119682562e-08, var=0.123635288982, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R
        Total Standard Deviation in ln(k): 0.704901181513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R
Total Standard Deviation in ln(k): 0.704901181513""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R
Total Standard Deviation in ln(k): 0.704901181513
sensitivities = [{'dA': 0.4926958115927792, 'dE0': 0.0, 'dn': -1680.3544145835165, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C4H9 + CH3O <=> C5H12O'}, {'dA': 0.49562436299238527, 'dE0': 0.0, 'dn': -978.7926604980294, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'O2 + C4H9 <=> C4H9O2'}]
""",
)

entry(
    index = 2,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_2R-inRing",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=-1.21605e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_2R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_2R-inRing
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_2R-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_2R-inRing
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'C5H5 + C5H5 <=> C10H10-6'}]
""",
)

entry(
    index = 3,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_2R->C_3R!H->O",
    kinetics = ArrheniusBM(A=(10935.8,'m^3/(mol*s)'), n=0.77776, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0184655330759, var=0.0205899691821, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_2R->C_3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_2R->C_3R!H->O
        Total Standard Deviation in ln(k): 0.334059363082"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_2R->C_3R!H->O
Total Standard Deviation in ln(k): 0.334059363082""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_2R->C_3R!H->O
Total Standard Deviation in ln(k): 0.334059363082
sensitivities = [{'dA': 0.49987244546928444, 'dE0': 0.0, 'dn': -1.5111100008370605e-05, 'dA_dEa': -4.326179369718496, 'dE0_dEa': 0.0, 'dn_dEa': 0.4778696678528699, 'name': '[O][O] + [CH3] <=> CH3O2'}, {'dA': 0.49986810932539605, 'dE0': 0.0, 'dn': -1.458852383550891e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'O2 + CH3 <=> CH3O2-2'}]
""",
)

entry(
    index = 4,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C_3R!H->N",
    kinetics = ArrheniusBM(A=(1.32408e+08,'m^3/(mol*s)'), n=-0.361164, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C_3R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C_3R!H->N
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C_3R!H->N
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C_3R!H->N
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'OH + NO2-2 <=> HOONO'}]
""",
)

entry(
    index = 5,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H",
    kinetics = ArrheniusBM(A=(5.02478e+07,'m^3/(mol*s)'), n=0.0443013, w0=(190171,'J/mol'), E0=(19017.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0678871354549, var=2.2783709969, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H
        Total Standard Deviation in ln(k): 3.19657269522"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H
Total Standard Deviation in ln(k): 3.19657269522""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H
Total Standard Deviation in ln(k): 3.19657269522
sensitivities = [{'dA': 0.03237888701690751, 'dE0': 0.0, 'dn': -0.0003393193249012794, 'dA_dEa': 0.0031687664439065282, 'dE0_dEa': 0.0, 'dn_dEa': -0.002392512404086404, 'name': 'C6H7 + H <=> C6H8-2'}, {'dA': 0.0323944173956683, 'dE0': 0.0, 'dn': -0.00035226954168784757, 'dA_dEa': 0.0001555958810684104, 'dE0_dEa': 0.0, 'dn_dEa': -0.00015254489594479829, 'name': 'C6H7-2 + H <=> C6H8-3'}, {'dA': 0.03241754208716332, 'dE0': 0.0, 'dn': -0.00037155317366000093, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H7-3 + H <=> C6H8-4'}, {'dA': 0.03241756074601556, 'dE0': 0.0, 'dn': -0.0003715686741775061, 'dA_dEa': 0.0009456877272385687, 'dE0_dEa': 0.0, 'dn_dEa': -0.0007432199284982307, 'name': 'C6H7-4 + H <=> C6H8-5'}, {'dA': 0.032415226733920846, 'dE0': 0.0, 'dn': -0.00036962282286675364, 'dA_dEa': -0.0006819967310890048, 'dE0_dEa': 0.0, 'dn_dEa': 0.00046638842633512447, 'name': 'C6H7-5 + H <=> C6H8-6'}, {'dA': 0.011960527945832562, 'dE0': 0.0, 'dn': -0.0003758084953366531, 'dA_dEa': 0.03648080495822061, 'dE0_dEa': 0.0, 'dn_dEa': -0.027148838881611653, 'name': 'C6H7-6 + H <=> C6H8-7'}, {'dA': 0.032416781795777914, 'dE0': 0.0, 'dn': -0.0003709194615929177, 'dA_dEa': 0.03722425351071889, 'dE0_dEa': 0.0, 'dn_dEa': -0.027700622350149813, 'name': 'H + NJCO <=> HNCO'}, {'dA': 0.03237148196433638, 'dE0': 0.0, 'dn': -0.0003331473137976818, 'dA_dEa': 0.037169948569730424, 'dE0_dEa': 0.0, 'dn_dEa': -0.02765534417562198, 'name': 'H + NCOJ <=> NCOH'}, {'dA': 0.01245795742477322, 'dE0': 0.0, 'dn': -0.0007906207170551376, 'dA_dEa': 0.646188499452265, 'dE0_dEa': 0.0, 'dn_dEa': -0.4802222170418851, 'name': '[CH2]c1ccccc1[C]=C=C + [H] <=> C10H9'}, {'dA': 0.012520359913283088, 'dE0': 0.0, 'dn': -0.0008424949957714523, 'dA_dEa': 0.2388117393863617, 'dE0_dEa': 0.0, 'dn_dEa': -0.17753321020733034, 'name': 'C=C1[CH]c2ccccc2C1 + [H] <=> C10H10-3'}, {'dA': 0.011954879887811283, 'dE0': 0.0, 'dn': -0.0003710980913082832, 'dA_dEa': -0.061457929632531376, 'dE0_dEa': 0.0, 'dn_dEa': 0.045627930212699626, 'name': 'C=C1[CH]Cc2ccccc21 + [H] <=> C10H10-4'}, {'dA': 0.011890948847793825, 'dE0': 0.0, 'dn': -0.0003177955538894712, 'dA_dEa': -0.001184063240344943, 'dE0_dEa': 0.0, 'dn_dEa': 0.0008444016018563415, 'name': 'C=C1C[CH]c2ccccc21 + [H] <=> C10H10-5'}, {'dA': 0.011967997412655404, 'dE0': 0.0, 'dn': -0.00038203698144321775, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C9H7 + H <=> C9H8-3'}, {'dA': 0.000812054317123146, 'dE0': 0.0, 'dn': -0.0003711723080870983, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H3 + H <=> C3H4'}, {'dA': 0.0008120532406509013, 'dE0': 0.0, 'dn': -0.0003711714090643759, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H3-2 + H <=> C3H4-2'}, {'dA': 0.03241375992502428, 'dE0': 0.0, 'dn': -0.0003684017880730115, 'dA_dEa': -0.12503242613350052, 'dE0_dEa': 0.0, 'dn_dEa': 0.09286730389536839, 'name': 'C4H5 + H <=> C4H6-2'}, {'dA': 0.03241928130393392, 'dE0': 0.0, 'dn': -0.00037300464916020543, 'dA_dEa': 0.12705901428590471, 'dE0_dEa': 0.0, 'dn_dEa': -0.09445513529564918, 'name': 'C4H5-2 + H <=> C4H6-3'}, {'dA': 0.011955178656820815, 'dE0': 0.0, 'dn': -0.000371347382485835, 'dA_dEa': 0.002426693114898893, 'dE0_dEa': 0.0, 'dn_dEa': -0.0018436914436547778, 'name': 'C7H7 + H <=> C7H8-2'}, {'dA': 0.01195551930166648, 'dE0': 0.0, 'dn': -0.0003716349293675592, 'dA_dEa': 0.020080265986879276, 'dE0_dEa': 0.0, 'dn_dEa': -0.014961449178056132, 'name': 'C7H7-2 + H <=> C7H8-3'}, {'dA': 0.011951639098840767, 'dE0': 0.0, 'dn': -0.00036839574618948, 'dA_dEa': 0.015442225077323991, 'dE0_dEa': 0.0, 'dn_dEa': -0.01151512857392588, 'name': 'C7H7-3 + H <=> C7H8-4'}, {'dA': 0.006319282714884607, 'dE0': 0.0, 'dn': -0.0003727030293573455, 'dA_dEa': -0.005759726757759788, 'dE0_dEa': 0.0, 'dn_dEa': 0.00423945692449995, 'name': 'H + CH3 <=> CH4'}, {'dA': 0.0008120638632648009, 'dE0': 0.0, 'dn': -0.00037118027000735836, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C2H5 <=> C2H6-2'}, {'dA': 0.0008111518390308886, 'dE0': 0.0, 'dn': -0.00037041981479756273, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C3H7-2 <=> C3H8-2'}, {'dA': 0.006317253507859973, 'dE0': 0.0, 'dn': -0.00037101111831860267, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C2H3 <=> C2H4'}, {'dA': 0.0008121809926820773, 'dE0': 0.0, 'dn': -0.0003712779354667694, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C2H <=> C2H2'}, {'dA': 0.0063205419884589135, 'dE0': 0.0, 'dn': -0.0003737528865119752, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C6H5 <=> C6H6-4'}, {'dA': 0.0008169831922089988, 'dE0': 0.0, 'dn': -0.0003752816224403772, 'dA_dEa': 0.0069534345108487215, 'dE0_dEa': 0.0, 'dn_dEa': -0.005207625654073914, 'name': 'H + CHO <=> CH2O'}, {'dA': 0.006317701664926985, 'dE0': 0.0, 'dn': -0.00037138482055005726, 'dA_dEa': -0.0030003116968660955, 'dE0_dEa': 0.0, 'dn_dEa': 0.0021888322168211118, 'name': 'H + OH <=> H2O'}, {'dA': 0.0008120485510688453, 'dE0': 0.0, 'dn': -0.0003711675030228061, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + CH3 <=> CH4'}, {'dA': 0.0008120078263119452, 'dE0': 0.0, 'dn': -0.000371133554970096, 'dA_dEa': -0.00020135742673235143, 'dE0_dEa': 0.0, 'dn_dEa': 0.00010914901692632224, 'name': 'O2 + H <=> HO2-2'}, {'dA': 0.28819823714701776, 'dE0': 0.0, 'dn': -0.00037508646472928826, 'dA_dEa': 0.41705227250692517, 'dE0_dEa': 0.0, 'dn_dEa': -0.3099408871361668, 'name': 'CH3S-2 + H <=> CH4S'}, {'dA': 0.006317424958269398, 'dE0': 0.0, 'dn': -0.0003711540796721071, 'dA_dEa': -0.0024038464090383885, 'dE0_dEa': 0.0, 'dn_dEa': 0.0017457041588057106, 'name': 'H + C3H5 <=> C3H6-2'}, {'dA': 0.0008120557026814807, 'dE0': 0.0, 'dn': -0.0003711734635235653, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C4H7 <=> C4H8'}, {'dA': 0.0008120557026814807, 'dE0': 0.0, 'dn': -0.0003711734635235653, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C5H9 <=> C5H10'}, {'dA': 0.0008120557026814807, 'dE0': 0.0, 'dn': -0.0003711734635235653, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C6H9 <=> C6H10'}, {'dA': 0.0008116905334532915, 'dE0': 0.0, 'dn': -0.0003708692784230148, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H3-2 + H <=> C3H4-2'}, {'dA': 0.006321048275027138, 'dE0': 0.0, 'dn': -0.0003741765877661637, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C5H5 + H <=> C5H6'}, {'dA': 0.0008111518390308886, 'dE0': 0.0, 'dn': -0.0003704198133058215, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C5H7 <=> C5H8'}, {'dA': 0.07248909870228547, 'dE0': 0.0, 'dn': -0.0004603237279473043, 'dA_dEa': 0.044874048182213466, 'dE0_dEa': 0.0, 'dn_dEa': -0.03338095835950262, 'name': 'H + C12H9 <=> C12H10-2'}, {'dA': 0.07238349105876637, 'dE0': 0.0, 'dn': -0.00037228512268914024, 'dA_dEa': 0.04407555453767517, 'dE0_dEa': 0.0, 'dn_dEa': -0.03279179330787794, 'name': 'H + C12H9-2 <=> C12H10-3'}, {'dA': 0.07238211214045351, 'dE0': 0.0, 'dn': -0.0003711343185758633, 'dA_dEa': -0.0037741988556665154, 'dE0_dEa': 0.0, 'dn_dEa': 0.002763737715563099, 'name': 'H + C12H9-3 <=> C12H10-4'}, {'dA': 0.006317837502934494, 'dE0': 0.0, 'dn': -0.0003714982396257377, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C12H25 <=> C12H26-7'}, {'dA': 0.006316924320515923, 'dE0': 0.0, 'dn': -0.0003707366122388233, 'dA_dEa': 0.0006289250826797126, 'dE0_dEa': 0.0, 'dn_dEa': -0.000507827119958634, 'name': 'H + C12H25-2 <=> C12H26-8'}, {'dA': 0.006316924320515923, 'dE0': 0.0, 'dn': -0.0003707366124045723, 'dA_dEa': 0.0006289250826797126, 'dE0_dEa': 0.0, 'dn_dEa': -0.000507827119958634, 'name': 'H + C12H25-3 <=> C12H26-9'}, {'dA': 0.006316924320515923, 'dE0': 0.0, 'dn': -0.0003707366124045723, 'dA_dEa': 0.0006289250826797126, 'dE0_dEa': 0.0, 'dn_dEa': -0.000507827119958634, 'name': 'H + C12H25-4 <=> C12H26-10'}, {'dA': 0.006316924320515923, 'dE0': 0.0, 'dn': -0.0003707366124045723, 'dA_dEa': 0.0006289250826797126, 'dE0_dEa': 0.0, 'dn_dEa': -0.000507827119958634, 'name': 'H + C12H25-5 <=> C12H26-11'}, {'dA': 0.006316924320515923, 'dE0': 0.0, 'dn': -0.0003707366124045723, 'dA_dEa': 0.0006289250826797126, 'dE0_dEa': 0.0, 'dn_dEa': -0.000507827119958634, 'name': 'H + C12H25-6 <=> C12H26-12'}, {'dA': 0.006316906706161503, 'dE0': 0.0, 'dn': -0.0003707219190848285, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C10H21 <=> C10H22-6'}, {'dA': 0.006316906706161503, 'dE0': 0.0, 'dn': -0.0003707219190848285, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C10H21-2 <=> C10H22-7'}, {'dA': 0.006316906706161503, 'dE0': 0.0, 'dn': -0.0003707219190848285, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C10H21-3 <=> C10H22-8'}, {'dA': 0.006316906706161503, 'dE0': 0.0, 'dn': -0.0003707219190848285, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C10H21-4 <=> C10H22-9'}, {'dA': 0.006316906706161503, 'dE0': 0.0, 'dn': -0.0003707219190848285, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C10H21-5 <=> C10H22-10'}]
""",
)

entry(
    index = 6,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_3R!H->O",
    kinetics = ArrheniusBM(A=(3.77e+06,'m^3/(mol*s)'), n=-2.20284e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_3R!H->O
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_3R!H->O
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_3R!H->O
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330819365, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'O2 + C3H7-2 <=> C3H7O2-2'}]
""",
)

entry(
    index = 7,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_2R->C",
    kinetics = ArrheniusBM(A=(6.81404e+07,'m^3/(mol*s)'), n=-2.32247e-07, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.00612506154e-08, var=0.119534414219, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_2R->C
        Total Standard Deviation in ln(k): 0.69311210551"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_2R->C
Total Standard Deviation in ln(k): 0.69311210551""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_2R->C
Total Standard Deviation in ln(k): 0.69311210551
sensitivities = [{'dA': 0.4830195407486392, 'dE0': 0.0, 'dn': -2271.5711835471475, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH3 + OH <=> CH4O'}, {'dA': 0.5351490635839319, 'dE0': 0.0, 'dn': 4628.964457470648, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + OH <=> C2H6O-2'}]
""",
)

entry(
    index = 8,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_2CNO->O_3R!H->O",
    kinetics = ArrheniusBM(A=(5250.69,'m^3/(mol*s)'), n=1.27262, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_2CNO->O_3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_2CNO->O_3R!H->O
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_2CNO->O_3R!H->O
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_2CNO->O_3R!H->O
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330819365, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'O2 + H <=> HO2-2'}]
""",
)

entry(
    index = 9,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_N-Sp-3C-2CN",
    kinetics = ArrheniusBM(A=(1.81e+08,'m^3/(mol*s)'), n=-8.9089e-10, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_N-Sp-3C-2CN',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_N-Sp-3C-2CN
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_N-Sp-3C-2CN
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_N-Sp-3C-2CN
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'H + C2H <=> C2H2'}]
""",
)

entry(
    index = 10,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_N-3R!H->O",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=-5.81278e-09, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_N-3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_N-3R!H->O
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_N-3R!H->O
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_N-3R!H->O
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'C3H7-2 + CH3O <=> C4H10O'}]
""",
)

entry(
    index = 11,
    label = "Root_1R->H_2R->S_Ext-2S-R",
    kinetics = ArrheniusBM(A=(2.19756e+07,'m^3/(mol*s)'), n=0.830529, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_2R->S_Ext-2S-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_2R->S_Ext-2S-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_2R->S_Ext-2S-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_2R->S_Ext-2S-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': '[S]S + [H] <=> HSSH'}]
""",
)

entry(
    index = 12,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R",
    kinetics = ArrheniusBM(A=(104369,'m^3/(mol*s)'), n=0.705194, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0346096610536, var=0.973963688559, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R
        Total Standard Deviation in ln(k): 2.06542394964"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R
Total Standard Deviation in ln(k): 2.06542394964""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R
Total Standard Deviation in ln(k): 2.06542394964
sensitivities = [{'dA': 0.02120741699585216, 'dE0': 0.0, 'dn': 7.226533894040731e-06, 'dA_dEa': -0.0017479579756953505, 'dE0_dEa': 0.0, 'dn_dEa': 0.00026308625754438176, 'name': 'CH3 + C2H5 <=> C3H8'}, {'dA': 0.02120065518340886, 'dE0': 0.0, 'dn': 8.369893168501738e-06, 'dA_dEa': 0.0002212379239807904, 'dE0_dEa': 0.0, 'dn_dEa': -3.238290875299069e-05, 'name': 'C2H5 + C2H5 <=> C4H10'}, {'dA': 0.0002011593238649078, 'dE0': 0.0, 'dn': 7.194822126039859e-06, 'dA_dEa': -4.27761044363753e-05, 'dE0_dEa': 0.0, 'dn_dEa': 7.193070700495968e-06, 'name': 'CH3 + C2H5 <=> C3H8-3'}, {'dA': 0.00020117936117005624, 'dE0': 0.0, 'dn': 7.1914554418948295e-06, 'dA_dEa': -4.27761044363753e-05, 'dE0_dEa': 0.0, 'dn_dEa': 7.193070700495968e-06, 'name': 'C2H5 + C2H5 <=> C4H10-3'}, {'dA': 0.0002011698558846086, 'dE0': 0.0, 'dn': 7.1930511524392895e-06, 'dA_dEa': -4.27761044363753e-05, 'dE0_dEa': 0.0, 'dn_dEa': 7.193070700495968e-06, 'name': 'C2H5 + CHO <=> C3H6O-2'}, {'dA': 0.1910182843509955, 'dE0': 0.0, 'dn': 3.9619471603452147e-05, 'dA_dEa': 0.55374423598315, 'dE0_dEa': 0.0, 'dn_dEa': -0.08309508171089507, 'name': 'HSS + CH3 <=> CH4S2'}, {'dA': 0.19109491170789966, 'dE0': 0.0, 'dn': 2.6707863414698794e-05, 'dA_dEa': 0.55374423598315, 'dE0_dEa': 0.0, 'dn_dEa': -0.08309508171062728, 'name': 'HSS + C4H9 <=> C4H10S2'}, {'dA': 0.19120516724593248, 'dE0': 0.0, 'dn': 8.138647691446128e-06, 'dA_dEa': 0.9877405068811052, 'dE0_dEa': 0.0, 'dn_dEa': -0.14822034108862303, 'name': 'CH3S + C2H5 <=> C3H8S'}, {'dA': 0.19120516724770883, 'dE0': 0.0, 'dn': 8.13864728977373e-06, 'dA_dEa': 0.9877982197093993, 'dE0_dEa': 0.0, 'dn_dEa': -0.1482300858473623, 'name': 'CH3S + CH3 <=> C2H6S'}, {'dA': 0.19120516724415612, 'dE0': 0.0, 'dn': 8.138647959227725e-06, 'dA_dEa': 0.9877982197093993, 'dE0_dEa': 0.0, 'dn_dEa': -0.1482300858473623, 'name': 'CH3S + C4H9 <=> C5H12S'}]
""",
)

entry(
    index = 13,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=-1.37127e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'C2H3O + C2H3O <=> C4H6O2'}]
""",
)

entry(
    index = 14,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(3.63222,'m^3/(mol*s)'), n=1.59841, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_N-4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_N-4R!H-inRing
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330832688, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H3 + O2 <=> C3H3O2'}]
""",
)

entry(
    index = 15,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(6.79503e+06,'m^3/(mol*s)'), n=0.417452, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H7-5 + H <=> C6H8-6'}]
""",
)

entry(
    index = 16,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_N-2R->C",
    kinetics = ArrheniusBM(A=(1.81e+06,'m^3/(mol*s)'), n=-5.80997e-08, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_N-2R->C
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_N-2R->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_N-2R->C
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'CH3O + CH3O <=> C2H6O2'}]
""",
)

entry(
    index = 17,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(1.48138e+06,'m^3/(mol*s)'), n=-0.119415, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_Sp-5R!H-4R!H
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': '[O][O] + [CH2]CC <=> C3H7O2'}]
""",
)

entry(
    index = 18,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O",
    kinetics = ArrheniusBM(A=(8.46129e+07,'m^3/(mol*s)'), n=-5.23396e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00433609697246, var=0.183327166906, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O
        Total Standard Deviation in ln(k): 0.869256557712"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O
Total Standard Deviation in ln(k): 0.869256557712""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O
Total Standard Deviation in ln(k): 0.869256557712
sensitivities = [{'dA': 0.4576858976293401, 'dE0': 0.0, 'dn': -2845.280030096354, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH3 + C2H3 <=> C3H6'}, {'dA': 0.015202393047532578, 'dE0': 0.0, 'dn': -1609.1033588750536, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H3 + C2H3 <=> C4H6-4'}, {'dA': 0.49634409510451644, 'dE0': 0.0, 'dn': 1178.1970354860764, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H3 + C2H <=> C4H4'}]
""",
)

entry(
    index = 19,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_7R!H->O",
    kinetics = ArrheniusBM(A=(7.75e+08,'m^3/(mol*s)'), n=-0.75, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_7R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_7R!H->O
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_7R!H->O
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_7R!H->O
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C4H9 + C2H3O <=> C6H12O'}]
""",
)

entry(
    index = 20,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C",
    kinetics = ArrheniusBM(A=(315400,'m^3/(mol*s)'), n=0.546593, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0328000692469, var=0.856170432709, Tref=1000.0, N=59, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C
        Total Standard Deviation in ln(k): 1.93738313973"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C
Total Standard Deviation in ln(k): 1.93738313973""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C
Total Standard Deviation in ln(k): 1.93738313973
sensitivities = [{'dA': 0.006268475971183542, 'dE0': 0.0, 'dn': -4.213026709005398e-05, 'dA_dEa': 0.012098213790780132, 'dE0_dEa': 0.0, 'dn_dEa': -0.0026240269453720014, 'name': 'C5H5 + C2H5 <=> C7H10'}, {'dA': 0.017103299860823037, 'dE0': 0.0, 'dn': -4.1995967765656167e-05, 'dA_dEa': -0.008776483424456217, 'dE0_dEa': 0.0, 'dn_dEa': 0.001895716756864821, 'name': 'CH3 + CH3 <=> C2H6'}, {'dA': 0.017103516475105104, 'dE0': 0.0, 'dn': -4.204883265172554e-05, 'dA_dEa': -0.0011851283083787107, 'dE0_dEa': 0.0, 'dn_dEa': 0.0002520702348495347, 'name': 'CH3 + C2H5 <=> C3H8'}, {'dA': 0.01708821633528334, 'dE0': 0.0, 'dn': -3.833105813719416e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C2H5 <=> C4H10'}, {'dA': 0.017102083457844693, 'dE0': 0.0, 'dn': -4.170126209398301e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C5H5 + CH3 <=> C6H8'}, {'dA': 0.006268096637285916, 'dE0': 0.0, 'dn': -4.2037718911018705e-05, 'dA_dEa': -0.01067130737198003, 'dE0_dEa': 0.0, 'dn_dEa': 0.0023059976402277148, 'name': 'C3H3 + C7H7 <=> C10H10'}, {'dA': 0.006274565636844168, 'dE0': 0.0, 'dn': -4.3604478164261487e-05, 'dA_dEa': -0.028325996515480078, 'dE0_dEa': 0.0, 'dn_dEa': 0.0061285295314789795, 'name': 'C3H3-2 + C7H7 <=> C10H10-2'}, {'dA': 0.006268850613722756, 'dE0': 0.0, 'dn': -4.222098252285543e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H5 + C3H3 <=> C9H8'}, {'dA': 0.006268850613722756, 'dE0': 0.0, 'dn': -4.222098252285543e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H5 + C3H3-2 <=> C9H8-2'}, {'dA': 0.0003675023503291591, 'dE0': 0.0, 'dn': -4.20260708205614e-05, 'dA_dEa': 0.000955332836838457, 'dE0_dEa': 0.0, 'dn_dEa': -0.00021138122997033245, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}, {'dA': 0.00036738532394057935, 'dE0': 0.0, 'dn': -4.1997668759710015e-05, 'dA_dEa': 0.0006833424706088251, 'dE0_dEa': 0.0, 'dn_dEa': -0.00015249145676961612, 'name': 'C3H3 + C3H3-2 <=> C6H6-2'}, {'dA': 0.00036743538522902733, 'dE0': 0.0, 'dn': -4.2009851006732785e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H3 + C3H3 <=> C6H6-3'}, {'dA': 0.017103821674526395, 'dE0': 0.0, 'dn': -4.212174743772364e-05, 'dA_dEa': 0.15042184899451408, 'dE0_dEa': 0.0, 'dn_dEa': -0.032573505008550475, 'name': 'CH3 + C3H3-2 <=> C4H6'}, {'dA': 0.006268948681054789, 'dE0': 0.0, 'dn': -4.224496663560716e-05, 'dA_dEa': 0.004728477861704571, 'dE0_dEa': 0.0, 'dn_dEa': -0.001028339136236873, 'name': 'C6H5 + CH3 <=> C7H8'}, {'dA': 0.003283035063362056, 'dE0': 0.0, 'dn': -4.2085223106117024e-05, 'dA_dEa': -0.011994739859134896, 'dE0_dEa': 0.0, 'dn_dEa': 0.002592536340644653, 'name': 'CH3 + CH3 <=> C2H6-3'}, {'dA': 0.0003674465087755557, 'dE0': 0.0, 'dn': -4.2012535505696126e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C2H5 <=> C3H8-3'}, {'dA': 0.00036746986076256646, 'dE0': 0.0, 'dn': -4.201819428114477e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C3H7-2 <=> C4H10-2'}, {'dA': 0.00036735919195511493, 'dE0': 0.0, 'dn': -4.199138406481397e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C4H9 <=> C5H12'}, {'dA': 0.0032825473379464462, 'dE0': 0.0, 'dn': -4.196701821847332e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C2H3 <=> C3H6'}, {'dA': 0.003282836743779078, 'dE0': 0.0, 'dn': -4.203693032978897e-05, 'dA_dEa': -0.00038654037481937557, 'dE0_dEa': 0.0, 'dn_dEa': 7.915586184287782e-05, 'name': 'CH3 + C6H5 <=> C7H8-5'}, {'dA': 0.0003674403483700366, 'dE0': 0.0, 'dn': -4.2011035810427535e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + CHO <=> C2H4O'}, {'dA': 0.00036749234944015327, 'dE0': 0.0, 'dn': -4.202366315572402e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C2H3O <=> C3H6O'}, {'dA': 0.0003674468107562184, 'dE0': 0.0, 'dn': -4.201260795007662e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C2H5 <=> C4H10-3'}, {'dA': 0.00036751662158000684, 'dE0': 0.0, 'dn': -4.202957056028649e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C3H7-2 <=> C5H12-2'}, {'dA': 0.0003676953141962663, 'dE0': 0.0, 'dn': -4.207293557326127e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.0003674403483700366, 'dE0': 0.0, 'dn': -4.2011035810427535e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + CHO <=> C3H6O-2'}, {'dA': 0.00036746706122418757, 'dE0': 0.0, 'dn': -4.2017506156122645e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C2H3O <=> C4H8O'}, {'dA': 0.0003673136905746737, 'dE0': 0.0, 'dn': -4.198023516443446e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H7-2 + C3H7-2 <=> C6H14-2'}, {'dA': 0.00036735914754619395, 'dE0': 0.0, 'dn': -4.199131219998852e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H7-2 + C4H9 <=> C7H16'}, {'dA': 0.00036743642262142154, 'dE0': 0.0, 'dn': -4.201008166964026e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H7-2 + C2H3O <=> C5H10O'}, {'dA': 0.0003685233753714507, 'dE0': 0.0, 'dn': -4.22740137412224e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C4H9 + C4H9 <=> C8H18'}, {'dA': 0.0003674375754770103, 'dE0': 0.0, 'dn': -4.201036062880139e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C4H9 + CHO <=> C5H10O-2'}, {'dA': 0.000367396930656168, 'dE0': 0.0, 'dn': -4.200046066954149e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C4H9 + C2H3O <=> C6H12O'}, {'dA': 0.00036743179343549806, 'dE0': 0.0, 'dn': -4.200897877639172e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H3 + C2H3 <=> C4H6-4'}, {'dA': 0.003283881989446875, 'dE0': 0.0, 'dn': -4.229092399829331e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H3 + C2H <=> C4H4'}, {'dA': 0.0003674403483700366, 'dE0': 0.0, 'dn': -4.2011035810427535e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H3 + CHO <=> C3H4O'}, {'dA': 0.0032828746672212425, 'dE0': 0.0, 'dn': -4.204586706856591e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H5 + C6H5 <=> C12H10'}, {'dA': 0.0032827294518259784, 'dE0': 0.0, 'dn': -4.201092279719397e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CHO + CHO <=> C2H2O2'}, {'dA': 0.0003674403483700366, 'dE0': 0.0, 'dn': -4.2011035810427535e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CHO + C2H3O <=> C3H4O2'}, {'dA': 0.0003674375754770103, 'dE0': 0.0, 'dn': -4.201036062880139e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H3O + C2H3O <=> C4H6O2'}, {'dA': 0.0003674426487521437, 'dE0': 0.0, 'dn': -4.2011595660599934e-05, 'dA_dEa': -0.0002801639951144661, 'dE0_dEa': 0.0, 'dn_dEa': 5.612590552640581e-05, 'name': 'CH3 + C4H9 <=> C5H12'}, {'dA': 0.00036751852050546815, 'dE0': 0.0, 'dn': -4.203002415870085e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C3H7-2 <=> C4H10-2'}, {'dA': 0.0003676282869236452, 'dE0': 0.0, 'dn': -4.205674628266498e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C3H7-2 <=> C5H12-2'}, {'dA': 0.00036794061664128966, 'dE0': 0.0, 'dn': -4.213252870702029e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.15223720445691213, 'dE0': 0.0, 'dn': 3.2879266522415664e-05, 'dA_dEa': 0.44134826628199764, 'dE0_dEa': 0.0, 'dn_dEa': -0.0955633654626484, 'name': 'HSS + CH3 <=> CH4S2'}, {'dA': 0.15236854311774808, 'dE0': 0.0, 'dn': 9.366840097962846e-07, 'dA_dEa': 0.44134826628199764, 'dE0_dEa': 0.0, 'dn_dEa': -0.0955633654626484, 'name': 'HSS + C4H9 <=> C4H10S2'}, {'dA': 0.15254553419376551, 'dE0': 0.0, 'dn': -4.200384275959268e-05, 'dA_dEa': 0.7871995058740012, 'dE0_dEa': 0.0, 'dn_dEa': -0.17044729420052232, 'name': 'CH3S + C2H5 <=> C3H8S'}, {'dA': 0.15254553419376551, 'dE0': 0.0, 'dn': -4.200384275959268e-05, 'dA_dEa': 0.7871995058740012, 'dE0_dEa': 0.0, 'dn_dEa': -0.17044729420052232, 'name': 'CH3S + CH3 <=> C2H6S'}, {'dA': 0.15254553419376551, 'dE0': 0.0, 'dn': -4.200384275959268e-05, 'dA_dEa': 0.7871995058740012, 'dE0_dEa': 0.0, 'dn_dEa': -0.17044729420032914, 'name': 'CH3S + C4H9 <=> C5H12S'}, {'dA': 0.0003674667237163881, 'dE0': 0.0, 'dn': -4.201745129157849e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C3H5 <=> C6H10-2'}, {'dA': 0.0003674390320896186, 'dE0': 0.0, 'dn': -4.201071512330324e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C2H5 <=> C5H10-2'}, {'dA': 0.00036743968756529236, 'dE0': 0.0, 'dn': -4.2010874500940316e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + CH3 <=> C4H8-2'}, {'dA': 0.00036739249331678317, 'dE0': 0.0, 'dn': -4.199941399313222e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C3H7-2 <=> C6H12'}, {'dA': 0.00036720258655979657, 'dE0': 0.0, 'dn': -4.1953167239294146e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C4H9 <=> C7H14'}, {'dA': 0.0003674667237163881, 'dE0': 0.0, 'dn': -4.201745129157849e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C5H7 <=> C8H12'}, {'dA': 0.0032888148577829026, 'dE0': 0.0, 'dn': -4.348904915209306e-05, 'dA_dEa': 0.012710828636743067, 'dE0_dEa': 0.0, 'dn_dEa': -0.0027567800856865532, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}, {'dA': 0.00036741274911382285, 'dE0': 0.0, 'dn': -4.20043446542607e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H3-2 + CH3 <=> C4H6-5'}, {'dA': 0.0032832966585520105, 'dE0': 0.0, 'dn': -4.2148568086045236e-05, 'dA_dEa': -0.005910945422016963, 'dE0_dEa': 0.0, 'dn_dEa': 0.0012752917427961712, 'name': 'C5H5 + CH3 <=> C6H8'}, {'dA': 0.00036749287168906405, 'dE0': 0.0, 'dn': -4.20237935556089e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C5H5 + C5H5 <=> C10H10-6'}, {'dA': 0.03826597143863774, 'dE0': 0.0, 'dn': -4.1954249848116146e-05, 'dA_dEa': 0.08215409152790637, 'dE0_dEa': 0.0, 'dn_dEa': -0.01779233876627199, 'name': 'C6H5 + C6H5 <=> C12H10'}, {'dA': 0.0032827851068621136, 'dE0': 0.0, 'dn': -4.202444265725807e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C11H23 + CH3 <=> C12H26'}, {'dA': 0.0032826911358089525, 'dE0': 0.0, 'dn': -4.200157129019062e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C10H21 + C2H5 <=> C12H26-2'}, {'dA': 0.0032828886453732118, 'dE0': 0.0, 'dn': -4.204964692656222e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C9H19 + C3H7 <=> C12H26-3'}, {'dA': 0.003283185911584858, 'dE0': 0.0, 'dn': -4.2121646015590955e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C8H17 + C4H9-2 <=> C12H26-4'}, {'dA': 0.003282022525752743, 'dE0': 0.0, 'dn': -4.18392232403332e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C7H15 + C5H11 <=> C12H26-5'}, {'dA': 0.0032827278388939682, 'dE0': 0.0, 'dn': -4.201053179072435e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H13 + C6H13 <=> C12H26-6'}, {'dA': 0.003282788368253271, 'dE0': 0.0, 'dn': -4.202522911345264e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C9H19 <=> C10H22'}, {'dA': 0.0032828446467906567, 'dE0': 0.0, 'dn': -4.203894756771177e-05, 'dA_dEa': 0.0004654583438679596, 'dE0_dEa': 0.0, 'dn_dEa': -0.00010532356200847545, 'name': 'C8H17 + C2H5 <=> C10H22-2'}, {'dA': 0.0032829422735861933, 'dE0': 0.0, 'dn': -4.206254704909937e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C7H15 + C3H7 <=> C10H22-3'}, {'dA': 0.0032828423854884, 'dE0': 0.0, 'dn': -4.203836144437738e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H13 + C4H9-2 <=> C10H22-4'}, {'dA': 0.003282713681329958, 'dE0': 0.0, 'dn': -4.200709309746388e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C5H11 + C5H11 <=> C10H22-5'}, {'dA': 0.0032805624528013115, 'dE0': 0.0, 'dn': -4.148467252164194e-05, 'dA_dEa': -0.009756079029089556, 'dE0_dEa': 0.0, 'dn_dEa': 0.0021078328680399984, 'name': 'CH3 + C7H15-2 <=> C8H18-2'}, {'dA': 0.003281037463054665, 'dE0': 0.0, 'dn': -4.1600190205732087e-05, 'dA_dEa': 0.020024571304235725, 'dE0_dEa': 0.0, 'dn_dEa': -0.004340359007296811, 'name': 'C4H9-3 + C4H9 <=> C8H18-3'}, {'dA': 0.003280093247682109, 'dE0': 0.0, 'dn': -4.137058769080532e-05, 'dA_dEa': 0.024465167733469993, 'dE0_dEa': 0.0, 'dn_dEa': -0.005301807594019801, 'name': 'C5H11-2 + C3H7-2 <=> C8H18-4'}, {'dA': 0.0032795276752043694, 'dE0': 0.0, 'dn': -4.123173345013249e-05, 'dA_dEa': 0.026408334745656313, 'dE0_dEa': 0.0, 'dn_dEa': -0.005722438747048, 'name': 'C7H15-3 + CH3 <=> C8H18-5'}]
""",
)

entry(
    index = 21,
    label = "Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0",
    kinetics = ArrheniusBM(A=(1.03124e+31,'m^3/(mol*s)'), n=-7.48856, w0=(79333.3,'J/mol'), E0=(7933.33,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.354218852058, var=34.8187486739, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0
        Total Standard Deviation in ln(k): 12.7194203157"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0
Total Standard Deviation in ln(k): 12.7194203157""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0
Total Standard Deviation in ln(k): 12.7194203157
sensitivities = [{'dA': 0.0031693820830017865, 'dE0': 0.0, 'dn': -1.573385484038347e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'NO2 + NO2 <=> N2O4'}, {'dA': 0.0031709866163968253, 'dE0': 0.0, 'dn': -1.569253284181103e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'NO2 + NO3-2 <=> N2O5'}, {'dA': 0.3288513097246344, 'dE0': 0.0, 'dn': -1.3738976285931307e-05, 'dA_dEa': -3.0723104823028367, 'dE0_dEa': 0.0, 'dn_dEa': -0.07040124112865347, 'name': 'C[O] + [N]=O <=> CH3ONO'}, {'dA': 0.3288541900659332, 'dE0': 0.0, 'dn': -1.3675933672062108e-05, 'dA_dEa': 44.71148149048569, 'dE0_dEa': 0.0, 'dn_dEa': 1.0245238154384635, 'name': 'CN + NCN <=> NCNCN'}, {'dA': 0.0031707455647737187, 'dE0': 0.0, 'dn': -1.5698678892722225e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'NH2 + HO2 <=> NH2OOH'}, {'dA': 0.328758082034178, 'dE0': 0.0, 'dn': -1.613517461129037e-05, 'dA_dEa': -0.05215488529586884, 'dE0_dEa': 0.0, 'dn_dEa': -0.0011967666196140772, 'name': 'NH2 + CH3NH <=> CH3NHNH2'}]
""",
)

entry(
    index = 22,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_N-2R-inRing",
    kinetics = ArrheniusBM(A=(6.08474e+07,'m^3/(mol*s)'), n=-0.428622, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_N-2R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_N-2R-inRing
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_N-2R-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_N-2R-inRing
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330819365, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': '1-hydroxybutyl + O2 <=> 1-hydroxybutylO2'}]
""",
)

entry(
    index = 23,
    label = "Root_N-1R->H_1CNOS->N_Ext-1N-R_Ext-1N-R_N-2R->C",
    kinetics = ArrheniusBM(A=(3.65367e+06,'m^3/(mol*s)'), n=0.2352, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.470950179139, var=0.481323982295, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1CNOS->N_Ext-1N-R_Ext-1N-R_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-1N-R_Ext-1N-R_N-2R->C
        Total Standard Deviation in ln(k): 2.57412732042"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-1N-R_Ext-1N-R_N-2R->C
Total Standard Deviation in ln(k): 2.57412732042""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-1N-R_Ext-1N-R_N-2R->C
Total Standard Deviation in ln(k): 2.57412732042
sensitivities = [{'dA': 0.979509341665016, 'dE0': 0.0, 'dn': 5.850555540421444e-07, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'NO2 + OH <=> HNO3'}, {'dA': 0.01998767987032799, 'dE0': 0.0, 'dn': 1.3810508867012257e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'NO2 + OH <=> HNO3'}]
""",
)

entry(
    index = 24,
    label = "Root_N-1R->H_1CNOS->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R",
    kinetics = ArrheniusBM(A=(1.1146e+21,'m^3/(mol*s)'), n=-4.68812, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1CNOS->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'NO + O2 <=> NO3'}]
""",
)

entry(
    index = 25,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-6C-R",
    kinetics = ArrheniusBM(A=(1.33755e+09,'m^3/(mol*s)'), n=-0.828757, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-6C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-6C-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-6C-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-6C-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.058789532296550186, 'dE0': 0.0, 'dn': -6.973997854035834e-07, 'dA_dEa': 0.029782657907876323, 'dE0_dEa': 0.0, 'dn_dEa': 0.003937208356888374, 'name': 'C3H5 + C4H9 <=> C7H14'}, {'dA': 0.9403217422027025, 'dE0': 0.0, 'dn': -5.7085163143980475e-05, 'dA_dEa': 6.003237793312572, 'dE0_dEa': 0.0, 'dn_dEa': 0.7940238011833649, 'name': 'C4H9-3 + C4H9 <=> C8H18-3'}]
""",
)

entry(
    index = 26,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C",
    kinetics = ArrheniusBM(A=(129687,'m^3/(mol*s)'), n=0.801692, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0247533941213, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C
        Total Standard Deviation in ln(k): 0.0621944575911"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C
Total Standard Deviation in ln(k): 0.0621944575911""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C
Total Standard Deviation in ln(k): 0.0621944575911
sensitivities = [{'dA': 0.49975991798772945, 'dE0': 0.0, 'dn': -1.487373402632114e-06, 'dA_dEa': 1.447079555937751, 'dE0_dEa': 0.0, 'dn_dEa': -0.20234486494117607, 'name': 'HSS + CH3 <=> CH4S2'}, {'dA': 0.49979746133571545, 'dE0': 0.0, 'dn': -7.371821239547058e-06, 'dA_dEa': 1.4470795559395273, 'dE0_dEa': 0.0, 'dn_dEa': -0.20234486494155035, 'name': 'HSS + C4H9 <=> C4H10S2'}]
""",
)

entry(
    index = 27,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_N-1CS->C",
    kinetics = ArrheniusBM(A=(1.74988e+07,'m^3/(mol*s)'), n=0.493661, w0=(113000,'J/mol'), E0=(11300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.78036942243, var=24.8279862009, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_N-1CS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_N-1CS->C
        Total Standard Deviation in ln(k): 16.9749844749"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_N-1CS->C
Total Standard Deviation in ln(k): 16.9749844749""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_N-1CS->C
Total Standard Deviation in ln(k): 16.9749844749
sensitivities = [{'dA': 0.10008714785315612, 'dE0': 0.0, 'dn': -2.76285093146401e-05, 'dA_dEa': 0.24342180455152923, 'dE0_dEa': 0.0, 'dn_dEa': -0.043740184571472204, 'name': '[SH] + [SH] <=> HSSH'}, {'dA': 0.899541241809231, 'dE0': 0.0, 'dn': 1.8429874914837437e-06, 'dA_dEa': 3.34389130041083, 'dE0_dEa': 0.0, 'dn_dEa': -0.6008569477535911, 'name': 'CH3S + CH3S <=> C2H6S2'}]
""",
)

entry(
    index = 28,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R_Ext-2CN-R_Ext-5R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.62598e+07,'m^3/(mol*s)'), n=0.255122, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R_Ext-2CN-R_Ext-5R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R_Ext-2CN-R_Ext-5R!H-R_Ext-3R!H-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R_Ext-2CN-R_Ext-5R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R_Ext-2CN-R_Ext-5R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C6H9 <=> C6H10'}]
""",
)

entry(
    index = 29,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(5.69413e+09,'m^3/(mol*s)'), n=-0.523824, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16007161633, var=0.288590491554, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C
        Total Standard Deviation in ln(k): 1.47914608549"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 1.47914608549""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 1.47914608549
sensitivities = [{'dA': 0.008654626732608037, 'dE0': 0.0, 'dn': 9.273370191073289e-05, 'dA_dEa': 0.00130996980374235, 'dE0_dEa': 0.0, 'dn_dEa': 0.0003852496349899401, 'name': 'C3H3 + H <=> C3H4'}, {'dA': 0.7288598016047224, 'dE0': 0.0, 'dn': 2.718025038268281e-05, 'dA_dEa': 2.8859437569333917, 'dE0_dEa': 0.0, 'dn_dEa': 0.8265086166807045, 'name': 'C4H5-2 + H <=> C4H6-3'}, {'dA': 0.2623751621513582, 'dE0': 0.0, 'dn': 5.16875447215664e-06, 'dA_dEa': 0.04546255728144434, 'dE0_dEa': 0.0, 'dn_dEa': 0.013030251283056193, 'name': 'C7H7 + H <=> C7H8-2'}]
""",
)

entry(
    index = 30,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.52619e+07,'m^3/(mol*s)'), n=-6.53409e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.159897533582, var=0.0656793251983, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R
        Total Standard Deviation in ln(k): 0.915525659817"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 0.915525659817""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 0.915525659817
sensitivities = [{'dA': 0.05778479416563368, 'dE0': 0.0, 'dn': -235.47179599838893, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H3 + CHO <=> C3H4O'}, {'dA': 0.933041819323069, 'dE0': 0.0, 'dn': -1254.2897060702599, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CHO + CHO <=> C2H2O2'}]
""",
)

entry(
    index = 31,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R",
    kinetics = ArrheniusBM(A=(7.82306e+07,'m^3/(mol*s)'), n=0.0632962, w0=(209857,'J/mol'), E0=(20985.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0177752274534, var=0.222667283872, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R
        Total Standard Deviation in ln(k): 0.990648434191"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R
Total Standard Deviation in ln(k): 0.990648434191""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R
Total Standard Deviation in ln(k): 0.990648434191
sensitivities = [{'dA': 0.2337950835525051, 'dE0': 0.0, 'dn': -0.0005023746611970959, 'dA_dEa': 0.0014100950522790033, 'dE0_dEa': 0.0, 'dn_dEa': -0.0016325788903783427, 'name': 'C6H7-3 + H <=> C6H8-4'}, {'dA': 0.2336558139006941, 'dE0': 0.0, 'dn': -0.000328849580200541, 'dA_dEa': -0.007705919212953343, 'dE0_dEa': 0.0, 'dn_dEa': 0.008484409678084597, 'name': 'C6H7-5 + H <=> C6H8-6'}, {'dA': 0.08427644500486982, 'dE0': 0.0, 'dn': -0.0003180885715244522, 'dA_dEa': 0.26353891305322524, 'dE0_dEa': 0.0, 'dn_dEa': -0.29261157847473734, 'name': 'C6H7-6 + H <=> C6H8-7'}, {'dA': 0.0031909327127269864, 'dE0': 0.0, 'dn': -0.0006373087615711501, 'dA_dEa': 0.0008387884591344132, 'dE0_dEa': 0.0, 'dn_dEa': -0.001000404394196691, 'name': 'C3H3 + H <=> C3H4'}, {'dA': 0.2336010822503711, 'dE0': 0.0, 'dn': -0.00026068565438111893, 'dA_dEa': 0.9247047870212152, 'dE0_dEa': 0.0, 'dn_dEa': -1.0265335212230564, 'name': 'C4H5-2 + H <=> C4H6-3'}, {'dA': 0.08429177230696401, 'dE0': 0.0, 'dn': -0.00033718705193306, 'dA_dEa': 0.014978423024560301, 'dE0_dEa': 0.0, 'dn_dEa': -0.01669618660823481, 'name': 'C7H7 + H <=> C7H8-2'}, {'dA': 0.043244232351473996, 'dE0': 0.0, 'dn': -0.00046875944343999557, 'dA_dEa': -0.0202871542818195, 'dE0_dEa': 0.0, 'dn_dEa': 0.022450278459338047, 'name': 'H + C3H5 <=> C3H6-2'}, {'dA': 0.04303160163133176, 'dE0': 0.0, 'dn': -0.00020391888331093385, 'dA_dEa': 5.837318184376915e-06, 'dE0_dEa': 0.0, 'dn_dEa': -7.543078194642634e-05, 'name': 'H + C12H25 <=> C12H26-7'}, {'dA': 0.043239495163054684, 'dE0': 0.0, 'dn': -0.0004628562511792464, 'dA_dEa': -0.0004951317826851755, 'dE0_dEa': 0.0, 'dn_dEa': 0.0004803635905921782, 'name': 'H + C10H21 <=> C10H22-6'}]
""",
)

entry(
    index = 32,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.53609e+09,'m^3/(mol*s)'), n=-0.946459, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.000724761308015, var=1.22133425516, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C
        Total Standard Deviation in ln(k): 2.2173337826"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 2.2173337826""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 2.2173337826
sensitivities = [{'dA': 0.04528539803061948, 'dE0': 0.0, 'dn': -2.1550023139614115e-05, 'dA_dEa': -0.0001484555340880597, 'dE0_dEa': 0.0, 'dn_dEa': -2.1861306328113394e-05, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.04542152291620528, 'dE0': 0.0, 'dn': -1.4755491679035108e-06, 'dA_dEa': -0.0001484555340880597, 'dE0_dEa': 0.0, 'dn_dEa': -2.1861306328113394e-05, 'name': 'C3H7-2 + C4H9 <=> C7H16'}, {'dA': 0.04538084740346948, 'dE0': 0.0, 'dn': -7.506804863711212e-06, 'dA_dEa': -0.0001484555340880597, 'dE0_dEa': 0.0, 'dn_dEa': -2.1861306328113394e-05, 'name': 'C4H9 + C4H9 <=> C8H18'}, {'dA': 0.045279536283975845, 'dE0': 0.0, 'dn': -2.2428206354351693e-05, 'dA_dEa': -0.0001484555340880597, 'dE0_dEa': 0.0, 'dn_dEa': -2.1861306328113394e-05, 'name': 'C4H9 + C2H3O <=> C6H12O'}, {'dA': 0.0451898584898963, 'dE0': 0.0, 'dn': -3.565410260642152e-05, 'dA_dEa': -0.0001484555340880597, 'dE0_dEa': 0.0, 'dn_dEa': -2.1861306328113394e-05, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.045302692850417985, 'dE0': 0.0, 'dn': -1.900632894096687e-05, 'dA_dEa': 0.022897926449163854, 'dE0_dEa': 0.0, 'dn_dEa': 0.003004009276090205, 'name': 'C3H5 + C4H9 <=> C7H14'}, {'dA': 0.7266295445021688, 'dE0': 0.0, 'dn': -4.125414989114611e-05, 'dA_dEa': 4.638931012135372, 'dE0_dEa': 0.0, 'dn_dEa': 0.6092697214499063, 'name': 'C4H9-3 + C4H9 <=> C8H18-3'}]
""",
)

entry(
    index = 33,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-2CNO-R_N-Sp-3R!H-=2CNO",
    kinetics = ArrheniusBM(A=(4.01625e+07,'m^3/(mol*s)'), n=0.214672, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-2CNO-R_N-Sp-3R!H-=2CNO',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-2CNO-R_N-Sp-3R!H-=2CNO
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-2CNO-R_N-Sp-3R!H-=2CNO
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-2CNO-R_N-Sp-3R!H-=2CNO
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H7 + H <=> C6H8-2'}]
""",
)

entry(
    index = 34,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_Sp-3CCSS#2R",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=-1.34483e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_Sp-3CCSS#2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_Sp-3CCSS#2R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_Sp-3CCSS#2R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_Sp-3CCSS#2R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'C2H3 + C2H <=> C4H4'}]
""",
)

entry(
    index = 35,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO",
    kinetics = ArrheniusBM(A=(8.24474e+12,'m^3/(mol*s)'), n=-1.49865, w0=(184786,'J/mol'), E0=(18478.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.381367412635, var=9.46235787476, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO
        Total Standard Deviation in ln(k): 7.12496428854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO
Total Standard Deviation in ln(k): 7.12496428854""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO
Total Standard Deviation in ln(k): 7.12496428854
sensitivities = [{'dA': 0.38825444870131787, 'dE0': 0.0, 'dn': 0.00010230729283671708, 'dA_dEa': 0.4465966933722635, 'dE0_dEa': 0.0, 'dn_dEa': 0.07160626276019097, 'name': 'H + NJCO <=> HNCO'}, {'dA': 0.1401796338171989, 'dE0': 0.0, 'dn': 0.00011016674561149938, 'dA_dEa': 7.828232159607903, 'dE0_dEa': 0.0, 'dn_dEa': 1.2549589722277443, 'name': '[CH2]c1ccccc1[C]=C=C + [H] <=> C10H9'}, {'dA': 0.005123099320770162, 'dE0': 0.0, 'dn': 0.00012120665985925425, 'dA_dEa': 0.003685959971023018, 'dE0_dEa': 0.0, 'dn_dEa': 0.0006042624920507008, 'name': 'C3H3-2 + H <=> C3H4-2'}, {'dA': 0.3883388504668944, 'dE0': 0.0, 'dn': 0.00011738186665342785, 'dA_dEa': -1.5208507317547313, 'dE0_dEa': 0.0, 'dn_dEa': -0.24379511662002357, 'name': 'C4H5 + H <=> C4H6-2'}, {'dA': 0.07188222930310753, 'dE0': 0.0, 'dn': 0.00012153092534192805, 'dA_dEa': 0.0006732174497870633, 'dE0_dEa': 0.0, 'dn_dEa': 0.00012131545499590216, 'name': 'H + C2H3 <=> C2H4'}, {'dA': 0.005114018264862915, 'dE0': 0.0, 'dn': 0.00011957579255861758, 'dA_dEa': 0.07955853532593858, 'dE0_dEa': 0.0, 'dn_dEa': 0.012767446405131142, 'name': 'H + CHO <=> CH2O'}, {'dA': 0.005123011568742295, 'dE0': 0.0, 'dn': 0.00012119094627919771, 'dA_dEa': 0.0006732174497870633, 'dE0_dEa': 0.0, 'dn_dEa': 0.00012131545499590216, 'name': 'C3H3-2 + H <=> C3H4-2'}]
""",
)

entry(
    index = 36,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(2.13947e+08,'m^3/(mol*s)'), n=-0.514474, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.000121059371351, var=1.09982367998, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R
        Total Standard Deviation in ln(k): 2.10271953737"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 2.10271953737""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 2.10271953737
sensitivities = [{'dA': 0.012276257233879947, 'dE0': 0.0, 'dn': 0.0001188943684051485, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH3 + C3H7-2 <=> C4H10-2'}, {'dA': 0.012254054684747401, 'dE0': 0.0, 'dn': 0.00011379085523922518, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH3 + C4H9 <=> C5H12'}, {'dA': 0.012273371101657845, 'dE0': 0.0, 'dn': 0.00011822642420430968, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH3 + C2H3O <=> C3H6O'}, {'dA': 0.01227492811750743, 'dE0': 0.0, 'dn': 0.00011858598995237637, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + C3H7-2 <=> C5H12-2'}, {'dA': 0.012278637665731583, 'dE0': 0.0, 'dn': 0.00011943613688660966, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.012291593296966073, 'dE0': 0.0, 'dn': 0.0001224154477126476, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + C2H3O <=> C4H8O'}, {'dA': 0.012278911391662393, 'dE0': 0.0, 'dn': 0.00011950271005249335, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C3H7-2 + C3H7-2 <=> C6H14-2'}, {'dA': 0.012205999155413772, 'dE0': 0.0, 'dn': 0.00010275123088529189, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C3H7-2 + C4H9 <=> C7H16'}, {'dA': 0.012295720956957657, 'dE0': 0.0, 'dn': 0.00012336922574505946, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C3H7-2 + C2H3O <=> C5H10O'}, {'dA': 0.012324278905852217, 'dE0': 0.0, 'dn': 0.00012992354816532213, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C4H9 + C4H9 <=> C8H18'}, {'dA': 0.012274699717097734, 'dE0': 0.0, 'dn': 0.00011852878954037228, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C4H9 + CHO <=> C5H10O-2'}, {'dA': 0.012264608979962973, 'dE0': 0.0, 'dn': 0.00011621055696608464, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C4H9 + C2H3O <=> C6H12O'}, {'dA': 0.012274882710273901, 'dE0': 0.0, 'dn': 0.0001185714262275439, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CHO + C2H3O <=> C3H4O2'}, {'dA': 0.012274699720650447, 'dE0': 0.0, 'dn': 0.00011852878972303073, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H3O + C2H3O <=> C4H6O2'}, {'dA': 0.012288108713677491, 'dE0': 0.0, 'dn': 0.00012161659054510844, 'dA_dEa': -0.02688988635668762, 'dE0_dEa': 0.0, 'dn_dEa': -0.005491530377549824, 'name': 'CH3 + C4H9 <=> C5H12'}, {'dA': 0.01227141946103096, 'dE0': 0.0, 'dn': 0.00011777836243857935, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH3 + C3H7-2 <=> C4H10-2'}, {'dA': 0.012221515220291149, 'dE0': 0.0, 'dn': 0.00010631202251791766, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + C3H7-2 <=> C5H12-2'}, {'dA': 0.01229774212774395, 'dE0': 0.0, 'dn': 0.0001238257402139748, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.012261578575591087, 'dE0': 0.0, 'dn': 0.00011551926389881971, 'dA_dEa': 0.006477737510835627, 'dE0_dEa': 0.0, 'dn_dEa': 0.0013385528507713386, 'name': 'C3H5 + C3H7-2 <=> C6H12'}, {'dA': 0.012243760419751408, 'dE0': 0.0, 'dn': 0.00011142064007468085, 'dA_dEa': 0.006504596772317234, 'dE0_dEa': 0.0, 'dn_dEa': 0.001344712396736309, 'name': 'C3H5 + C4H9 <=> C7H14'}, {'dA': 0.012281833715378741, 'dE0': 0.0, 'dn': 0.00012016875825845234, 'dA_dEa': 0.012477386015065359, 'dE0_dEa': 0.0, 'dn_dEa': 0.0025672473899263797, 'name': 'C3H5 + C5H7 <=> C8H12'}, {'dA': 0.18864921701935292, 'dE0': 0.0, 'dn': 0.0001167173209617287, 'dA_dEa': -0.600199452776517, 'dE0_dEa': 0.0, 'dn_dEa': -0.12285937438624303, 'name': 'CH3 + C7H15-2 <=> C8H18-2'}, {'dA': 0.18871142488665474, 'dE0': 0.0, 'dn': 0.00013099847479080306, 'dA_dEa': 1.201240560373539, 'dE0_dEa': 0.0, 'dn_dEa': 0.24593056145847828, 'name': 'C4H9-3 + C4H9 <=> C8H18-3'}, {'dA': 0.1886626802019217, 'dE0': 0.0, 'dn': 0.00011981254319729084, 'dA_dEa': 1.469949645887587, 'dE0_dEa': 0.0, 'dn_dEa': 0.30094061046738607, 'name': 'C5H11-2 + C3H7-2 <=> C8H18-4'}, {'dA': 0.18860964950919568, 'dE0': 0.0, 'dn': 0.00010763474380139597, 'dA_dEa': 1.587686818311515, 'dE0_dEa': 0.0, 'dn_dEa': 0.32504241464190625, 'name': 'C7H15-3 + CH3 <=> C8H18-5'}]
""",
)

entry(
    index = 37,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(7.04085e+06,'m^3/(mol*s)'), n=-0.0872803, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'O2 + C10H7-2 <=> C10H7O2-2'}]
""",
)

entry(
    index = 38,
    label = "Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C_Ext-1N-R",
    kinetics = ArrheniusBM(A=(2.57593e+11,'m^3/(mol*s)'), n=-1.2919, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C_Ext-1N-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C_Ext-1N-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C_Ext-1N-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C_Ext-1N-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C[O] + [N]=O <=> CH3ONO'}]
""",
)

entry(
    index = 39,
    label = "Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C",
    kinetics = ArrheniusBM(A=(9.29149e+06,'m^3/(mol*s)'), n=-0.3, w0=(75166.7,'J/mol'), E0=(7516.67,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.40309720458e-11, var=16.7795781874, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C
        Total Standard Deviation in ln(k): 8.21197292804"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C
Total Standard Deviation in ln(k): 8.21197292804""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C
Total Standard Deviation in ln(k): 8.21197292804
sensitivities = [{'dA': 0.3347754850296183, 'dE0': 0.0, 'dn': 0.0007486445637648303, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'NO2 + NO2 <=> N2O4'}, {'dA': 0.33535994690229526, 'dE0': 0.0, 'dn': 0.0010210508188732003, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'NO2 + NO3-2 <=> N2O5'}, {'dA': 0.33438596567951023, 'dE0': 0.0, 'dn': 0.0005675025738303011, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'NH2 + HO2 <=> NH2OOH'}]
""",
)

entry(
    index = 40,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_3R!H-inRing",
    kinetics = ArrheniusBM(A=(6.75496e+10,'m^3/(mol*s)'), n=-1.29253, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_3R!H-inRing
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_3R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_3R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C3H3 + C7H7 <=> C10H10'}]
""",
)

entry(
    index = 41,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(6.16957e+06,'m^3/(mol*s)'), n=-1.87134e-07, w0=(122000,'J/mol'), E0=(12200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.52051667475e-07, var=0.241111252513, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O
        Total Standard Deviation in ln(k): 0.984387063055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O
Total Standard Deviation in ln(k): 0.984387063055""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O
Total Standard Deviation in ln(k): 0.984387063055
sensitivities = [{'dA': 0.2456673764897048, 'dE0': 0.0, 'dn': -1520.7223425750642, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C3H7-2 + CH3O <=> C4H10O'}, {'dA': 0.25909714526942207, 'dE0': 0.0, 'dn': 3385.6642081115056, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C4H9 + CH3O <=> C5H12O'}, {'dA': 0.25428255051276905, 'dE0': 0.0, 'dn': 1636.1349811229331, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'O2 + C3H7-2 <=> C3H7O2-2'}, {'dA': 0.2712466229901921, 'dE0': 0.0, 'dn': 7846.796565217686, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'O2 + C4H9 <=> C4H9O2'}]
""",
)

entry(
    index = 42,
    label = "Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C",
    kinetics = ArrheniusBM(A=(1.03468e+10,'m^3/(mol*s)'), n=-0.848331, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00516292776992, var=0.173847691771, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C
        Total Standard Deviation in ln(k): 0.848847406671"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C
Total Standard Deviation in ln(k): 0.848847406671""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C
Total Standard Deviation in ln(k): 0.848847406671
sensitivities = [{'dA': 0.4996158700479309, 'dE0': 0.0, 'dn': 9.041223619138378e-05, 'dA_dEa': -4.660315099059689, 'dE0_dEa': 0.0, 'dn_dEa': 2.7963469704091026, 'name': 'C[O] + [N]=O <=> CH3ONO'}, {'dA': 0.4995449365453037, 'dE0': 0.0, 'dn': 0.0001383693692810747, 'dA_dEa': -0.07805155799013057, 'dE0_dEa': 0.0, 'dn_dEa': 0.04682148425680767, 'name': 'NH2 + CH3NH <=> CH3NHNH2'}]
""",
)

entry(
    index = 43,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-2CNO-R_Sp-3R!H-=2CNO",
    kinetics = ArrheniusBM(A=(2.2e+08,'m^3/(mol*s)'), n=1.30791e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-2CNO-R_Sp-3R!H-=2CNO',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-2CNO-R_Sp-3R!H-=2CNO
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-2CNO-R_Sp-3R!H-=2CNO
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-2CNO-R_Sp-3R!H-=2CNO
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.03924165175917415, 'dE0': 0.0, 'dn': -3.302779247985092e-05, 'dA_dEa': 3.8342911068416144e-05, 'dE0_dEa': 0.0, 'dn_dEa': -2.7794149324871314e-05, 'name': 'H + C6H5 <=> C6H6-4'}, {'dA': 0.4801898589299998, 'dE0': 0.0, 'dn': -2.7354526522005868e-05, 'dA_dEa': 0.2912543463687066, 'dE0_dEa': 0.0, 'dn_dEa': -0.18819635240585178, 'name': 'H + C12H9-2 <=> C12H10-3'}, {'dA': 0.4801904608556203, 'dE0': 0.0, 'dn': -2.7790948070764795e-05, 'dA_dEa': -0.028143884986068003, 'dE0_dEa': 0.0, 'dn_dEa': 0.01818209097555311, 'name': 'H + C12H9-3 <=> C12H10-4'}]
""",
)

entry(
    index = 44,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(6.64e+07,'m^3/(mol*s)'), n=-0.35, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_6R!H->C
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C3H7-2 + C2H3O <=> C5H10O'}]
""",
)

entry(
    index = 45,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(8.43648e+08,'m^3/(mol*s)'), n=-0.692983, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.486034813833, var=0.494552119499, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_4R!H->C
        Total Standard Deviation in ln(k): 2.63101090859"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 2.63101090859""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 2.63101090859
sensitivities = [{'dA': 0.9881546563940113, 'dE0': 0.0, 'dn': -4.1228404010500734e-07, 'dA_dEa': 0.012371101018261695, 'dE0_dEa': 0.0, 'dn_dEa': 0.0022225066330518453, 'name': 'C2H5 + C2H5 <=> C4H10'}, {'dA': 0.011343971291212368, 'dE0': 0.0, 'dn': 6.785040996313296e-08, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + C2H5 <=> C4H10-3'}]
""",
)

entry(
    index = 46,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=-1.42812e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_N-5R!H->C
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'CHO + C2H3O <=> C3H4O2'}]
""",
)

entry(
    index = 47,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N",
    kinetics = ArrheniusBM(A=(403.078,'m^3/(mol*s)'), n=1.76559, w0=(71000,'J/mol'), E0=(13653.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.726705389742, var=5.98513001094, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N
        Total Standard Deviation in ln(k): 6.73038215317"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N
Total Standard Deviation in ln(k): 6.73038215317""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N
Total Standard Deviation in ln(k): 6.73038215317
sensitivities = [{'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': '[SH] + [O][O] <=> HSOO'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'OH + CH3O <=> CH4O2'}]
""",
)

entry(
    index = 48,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(9.99999e+06,'m^3/(mol*s)'), n=9.65418e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_Sp-4R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_Sp-4R!H-2R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_Sp-4R!H-2R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_Sp-4R!H-2R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'C6H5 + C3H3 <=> C9H8'}]
""",
)

entry(
    index = 49,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(9.33146e+06,'m^3/(mol*s)'), n=0.409212, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-3R!H-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H7-2 + H <=> C6H8-3'}]
""",
)

entry(
    index = 50,
    label = "Root_N-1R->H",
    kinetics = ArrheniusBM(A=(4.12325e+06,'m^3/(mol*s)'), n=0.220072, w0=(146681,'J/mol'), E0=(1439.78,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0580211370054, var=4.8972964562, Tref=1000.0, N=102, data_mean=0.0, correlation='Root_N-1R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H
        Total Standard Deviation in ln(k): 4.58222761906"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 4.58222761906""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 4.58222761906
sensitivities = [{'dA': 0.0015246315605567675, 'dE0': -0.0, 'dn': -0.0005043705448292664, 'dA_dEa': 0.00036738378739191327, 'dE0_dEa': -0.0, 'dn_dEa': -0.0001725534427832334, 'name': '[O][O] + [CH3] <=> CH3O2'}, {'dA': 0.0015249146727571176, 'dE0': -0.0, 'dn': -0.0005044721513305112, 'dA_dEa': 0.00010553120688429116, 'dE0_dEa': -0.0, 'dn_dEa': -8.881433525609091e-05, 'name': '[O][O] + C[CH2] <=> C2H5O2'}, {'dA': 0.0015256050502900369, 'dE0': -0.0, 'dn': -0.0005047197531110475, 'dA_dEa': -0.0001311079103061419, 'dE0_dEa': -0.0, 'dn_dEa': -1.3126884454308314e-05, 'name': '[O][O] + [CH2]CC <=> C3H7O2'}, {'dA': 0.001524271116437771, 'dE0': -0.0, 'dn': -0.0005042410882020006, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': '1-hydroxybutyl + O2 <=> 1-hydroxybutylO2'}, {'dA': 0.0015239253041700609, 'dE0': -0.0, 'dn': -0.0005041171648153537, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'NO2 + NO2 <=> N2O4'}, {'dA': 0.001524718447498853, 'dE0': -0.0, 'dn': -0.0005044017546521236, 'dA_dEa': -9.519513710644017e-05, 'dE0_dEa': -0.0, 'dn_dEa': -2.460841895229333e-05, 'name': 'NO + O2 <=> NO3'}, {'dA': 0.0015248181153283981, 'dE0': -0.0, 'dn': -0.0005044373940353555, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'NO2 + NO3-2 <=> N2O5'}, {'dA': 0.005161048507674195, 'dE0': -0.0, 'dn': -0.0005038978723260648, 'dA_dEa': 0.008755065374900083, 'dE0_dEa': -0.0, 'dn_dEa': -0.0028552242495908943, 'name': 'C5H5 + C2H5 <=> C7H10'}, {'dA': 0.01185156054006728, 'dE0': -0.0, 'dn': -0.0005076380945672252, 'dA_dEa': -0.23426927303840467, 'dE0_dEa': -0.0, 'dn_dEa': 0.07487422090098259, 'name': '[CH3] + [O-][N+]=O <=> CH3NO2'}, {'dA': 0.011842270307484054, 'dE0': -0.0, 'dn': -0.0005043017092841108, 'dA_dEa': -0.004114221180629327, 'dE0_dEa': -0.0, 'dn_dEa': 0.0012608865219987397, 'name': 'CH3 + CH3 <=> C2H6'}, {'dA': 0.011842788953943167, 'dE0': -0.0, 'dn': -0.0005044878305816176, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C2H5 <=> C3H8'}, {'dA': 0.011829634020800365, 'dE0': -0.0, 'dn': -0.0004997636191153647, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C2H5 <=> C4H10'}, {'dA': 0.01184221017247597, 'dE0': -0.0, 'dn': -0.000504280032347758, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C5H5 + CH3 <=> C6H8'}, {'dA': 0.011884933153184707, 'dE0': -0.0, 'dn': -0.0005196169272644189, 'dA_dEa': -0.09589622997020432, 'dE0_dEa': -0.0, 'dn_dEa': 0.030615052613103537, 'name': 'C[O] + [N]=O <=> CH3ONO'}, {'dA': 0.012055334471129603, 'dE0': -0.0, 'dn': -0.0005808184798326768, 'dA_dEa': 1.4182403331323596, 'dE0_dEa': -0.0, 'dn_dEa': -0.453664377718702, 'name': 'CN + NCN <=> NCNCN'}, {'dA': 0.011833425906716736, 'dE0': -0.0, 'dn': -0.0005011245623017254, 'dA_dEa': -0.11275104888676245, 'dE0_dEa': -0.0, 'dn_dEa': 0.03600732616468826, 'name': '[SH] + [O][O] <=> HSOO'}, {'dA': 0.005163178872891763, 'dE0': -0.0, 'dn': -0.0005046623825705845, 'dA_dEa': 0.004345543537454456, 'dE0_dEa': -0.0, 'dn_dEa': -0.0014449379748645412, 'name': 'OH + NO2-2 <=> HOONO'}, {'dA': 0.011846242216507957, 'dE0': -0.0, 'dn': -0.0005057353953433329, 'dA_dEa': 0.01194315521324672, 'dE0_dEa': -0.0, 'dn_dEa': -0.003875509734009105, 'name': '[NH2] + [NH2] <=> N2H4'}, {'dA': 0.0015245465672110727, 'dE0': -0.0, 'dn': -0.0005043399855142609, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'NH2 + HO2 <=> NH2OOH'}, {'dA': 0.001517639327986043, 'dE0': -0.0, 'dn': -0.0005018605309613408, 'dA_dEa': 0.0006249131541125741, 'dE0_dEa': -0.0, 'dn_dEa': -0.0002543113786363496, 'name': 'NH2 + O2 <=> NH2OO'}, {'dA': 0.011843032600823616, 'dE0': -0.0, 'dn': -0.0005045754877631433, 'dA_dEa': -0.00022848945668843285, 'dE0_dEa': -0.0, 'dn_dEa': 1.8009582548694494e-05, 'name': 'NH2 + CH3NH <=> CH3NHNH2'}, {'dA': 0.011849496468486959, 'dE0': -0.0, 'dn': -0.0005068963282688664, 'dA_dEa': -0.03140936629897686, 'dE0_dEa': -0.0, 'dn_dEa': 0.009991621732956897, 'name': 'CH3 + NHNH2 <=> CH3NHNH2'}, {'dA': 0.011831882508418682, 'dE0': -0.0, 'dn': -0.0005005733745424332, 'dA_dEa': 0.026826394147863766, 'dE0_dEa': -0.0, 'dn_dEa': -0.00863529991832166, 'name': '[SH] + [SH] <=> HSSH'}, {'dA': 0.005162250346302812, 'dE0': -0.0, 'dn': -0.0005043287928981381, 'dA_dEa': -0.005280532576535406, 'dE0_dEa': -0.0, 'dn_dEa': 0.001633863411673485, 'name': 'C3H3 + C7H7 <=> C10H10'}, {'dA': 0.005146948732104873, 'dE0': -0.0, 'dn': -0.0004988381022560547, 'dA_dEa': -0.016178379491195834, 'dE0_dEa': -0.0, 'dn_dEa': 0.00511994457370015, 'name': 'C3H3-2 + C7H7 <=> C10H10-2'}, {'dA': 0.0051621434735699264, 'dE0': -0.0, 'dn': -0.0005042908044667019, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C6H5 + C3H3 <=> C9H8'}, {'dA': 0.0051621434735699264, 'dE0': -0.0, 'dn': -0.0005042908044667019, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C6H5 + C3H3-2 <=> C9H8-2'}, {'dA': 0.0051525940598656905, 'dE0': -0.0, 'dn': -0.0005008650831524493, 'dA_dEa': 0.017043747611468974, 'dE0_dEa': -0.0, 'dn_dEa': -0.005506127078256568, 'name': 'C3H3 + O2 <=> C3H3O2'}, {'dA': 0.005143820464681992, 'dE0': -0.0, 'dn': -0.0004977137393152467, 'dA_dEa': -0.027842364556110735, 'dE0_dEa': -0.0, 'dn_dEa': 0.00885014944169448, 'name': 'C3H3-2 + O2 <=> C3H3O2-2'}, {'dA': 0.001524430249588872, 'dE0': -0.0, 'dn': -0.0005042982240231356, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}, {'dA': 0.001524596470403762, 'dE0': -0.0, 'dn': -0.0005043579052291285, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H3 + C3H3-2 <=> C6H6-2'}, {'dA': 0.001524609356096275, 'dE0': -0.0, 'dn': -0.0005043625189978026, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H3 + C3H3 <=> C6H6-3'}, {'dA': 0.011842990200962217, 'dE0': -0.0, 'dn': -0.0005045600009961546, 'dA_dEa': 0.0940349310205694, 'dE0_dEa': -0.0, 'dn_dEa': -0.03013119965509392, 'name': 'CH3 + C3H3-2 <=> C4H6'}, {'dA': 0.005162288630345415, 'dE0': -0.0, 'dn': -0.0005043428127049987, 'dA_dEa': 0.004212819254334941, 'dE0_dEa': -0.0, 'dn_dEa': -0.0014024721773614568, 'name': 'C6H5 + CH3 <=> C7H8'}, {'dA': 0.0033217115991139076, 'dE0': -0.0, 'dn': -0.0005042916874108972, 'dA_dEa': -0.0060971391491200285, 'dE0_dEa': -0.0, 'dn_dEa': 0.0018950670107485857, 'name': 'CH3 + CH3 <=> C2H6-3'}, {'dA': 0.001524547448284065, 'dE0': -0.0, 'dn': -0.0005043402975696836, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C2H5 <=> C3H8-3'}, {'dA': 0.0015244890345657582, 'dE0': -0.0, 'dn': -0.0005043193380611609, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C3H7-2 <=> C4H10-2'}, {'dA': 0.0015245443236723845, 'dE0': -0.0, 'dn': -0.0005043391884673516, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C4H9 <=> C5H12'}, {'dA': 0.003322735055988712, 'dE0': -0.0, 'dn': -0.0005046588761920041, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C2H3 <=> C3H6'}, {'dA': 0.0033218847246278323, 'dE0': -0.0, 'dn': -0.0005043538896023527, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C6H5 <=> C7H8-5'}, {'dA': 0.0015245478000027192, 'dE0': -0.0, 'dn': -0.0005043404267009856, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + CHO <=> C2H4O'}, {'dA': 0.001524557879051426, 'dE0': -0.0, 'dn': -0.0005043440465153506, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C2H3O <=> C3H6O'}, {'dA': 0.0015244656932368885, 'dE0': -0.0, 'dn': -0.0005043109854775628, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + OH <=> CH4O'}, {'dA': 0.0015245517985819647, 'dE0': -0.0, 'dn': -0.0005043418609859, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + CH3O <=> C2H6O'}, {'dA': 0.0015245587956515551, 'dE0': -0.0, 'dn': -0.0005043443748370366, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C2H5 <=> C4H10-3'}, {'dA': 0.0015244892619394337, 'dE0': -0.0, 'dn': -0.0005043194058372587, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C3H7-2 <=> C5H12-2'}, {'dA': 0.0015246047180285673, 'dE0': -0.0, 'dn': -0.0005043608616938549, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.0015245478000027192, 'dE0': -0.0, 'dn': -0.0005043404267009856, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + CHO <=> C3H6O-2'}, {'dA': 0.0015244665778625945, 'dE0': -0.0, 'dn': -0.0005043112832643333, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C2H3O <=> C4H8O'}, {'dA': 0.0015245569304768738, 'dE0': -0.0, 'dn': -0.0005043436642581594, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + OH <=> C2H6O-2'}, {'dA': 0.0015246913811496911, 'dE0': -0.0, 'dn': -0.0005043919235507892, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H7-2 + C3H7-2 <=> C6H14-2'}, {'dA': 0.0015248711058292743, 'dE0': -0.0, 'dn': -0.0005044564224244954, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H7-2 + C4H9 <=> C7H16'}, {'dA': 0.0015245846807234189, 'dE0': -0.0, 'dn': -0.0005043536730042129, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H7-2 + C2H3O <=> C5H10O'}, {'dA': 0.0015246258655567404, 'dE0': -0.0, 'dn': -0.0005043684566120235, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H7-2 + CH3O <=> C4H10O'}, {'dA': 0.0015247544205012078, 'dE0': -0.0, 'dn': -0.0005044146806241101, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C4H9 + C4H9 <=> C8H18'}, {'dA': 0.0015245517985819647, 'dE0': -0.0, 'dn': -0.0005043418609859, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C4H9 + CHO <=> C5H10O-2'}, {'dA': 0.0015244534274929124, 'dE0': -0.0, 'dn': -0.0005043065136819778, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C4H9 + C2H3O <=> C6H12O'}, {'dA': 0.0015246098357126216, 'dE0': -0.0, 'dn': -0.0005043627030634154, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C4H9 + CH3O <=> C5H12O'}, {'dA': 0.001524602819103106, 'dE0': -0.0, 'dn': -0.0005043601625298993, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H3 + C2H3 <=> C4H6-4'}, {'dA': 0.00332466824914982, 'dE0': -0.0, 'dn': -0.0005053530064524591, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H3 + C2H <=> C4H4'}, {'dA': 0.0015245478000027192, 'dE0': -0.0, 'dn': -0.0005043404267009856, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H3 + CHO <=> C3H4O'}, {'dA': 0.0033211578056583694, 'dE0': -0.0, 'dn': -0.0005040933819686294, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C6H5 + C6H5 <=> C12H10'}, {'dA': 0.0033219009925037676, 'dE0': -0.0, 'dn': -0.0005043596681211022, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CHO + CHO <=> C2H2O2'}, {'dA': 0.0015245478000027192, 'dE0': -0.0, 'dn': -0.0005043404267009856, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CHO + C2H3O <=> C3H4O2'}, {'dA': 0.0015245517985819647, 'dE0': -0.0, 'dn': -0.0005043418609859, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H3O + C2H3O <=> C4H6O2'}, {'dA': 0.0015245498410367277, 'dE0': -0.0, 'dn': -0.0005043411598243333, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'OH + OH <=> H2O2'}, {'dA': 0.0015244443645203178, 'dE0': -0.0, 'dn': -0.0005043033040913621, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3O + CH3O <=> C2H6O2'}, {'dA': 0.0015245483986349741, 'dE0': -0.0, 'dn': -0.00050434063859047, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C4H9 <=> C5H12'}, {'dA': 0.0015245334168413906, 'dE0': -0.0, 'dn': -0.0005043352822811378, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C3H7-2 <=> C4H10-2'}, {'dA': 0.0, 'dE0': -0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C3H7-2 <=> C5H12-2'}, {'dA': 0.0015244905355872875, 'dE0': -0.0, 'dn': -0.0005043198627195007, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.0015245469864312868, 'dE0': -0.0, 'dn': -0.000504340135192422, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'OH + CH3O <=> CH4O2'}, {'dA': 0.09531092821292103, 'dE0': -0.0, 'dn': -0.0004926169343878239, 'dA_dEa': 0.273376375826503, 'dE0_dEa': -0.0, 'dn_dEa': -0.0874903183695251, 'name': 'HSS + CH3 <=> CH4S2'}, {'dA': 0.09511222202364049, 'dE0': -0.0, 'dn': -0.0004212125718231844, 'dA_dEa': 0.3496050819205395, 'dE0_dEa': -0.0, 'dn_dEa': -0.11183348926744004, 'name': 'CH3S + CH3S <=> C2H6S2'}, {'dA': 0.0015245593552039595, 'dE0': -0.0, 'dn': -0.0005043446004244272, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + CH3 <=> CH3O2-2'}, {'dA': 0.0015245593552039595, 'dE0': -0.0, 'dn': -0.0005043446004244272, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + C2H5 <=> C2H5O2-2'}, {'dA': 0.0953109282058156, 'dE0': -0.0, 'dn': -0.0004926169318194666, 'dA_dEa': 0.27337637583183205, 'dE0_dEa': -0.0, 'dn_dEa': -0.0874903183715227, 'name': 'HSS + C4H9 <=> C4H10S2'}, {'dA': 0.0015244625846124195, 'dE0': -0.0, 'dn': -0.0005043098217262931, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + C3H7-2 <=> C3H7O2-2'}, {'dA': 0.09535109375137181, 'dE0': -0.0, 'dn': -0.000507035053099139, 'dA_dEa': 0.4866030401054469, 'dE0_dEa': -0.0, 'dn_dEa': -0.15568995420430276, 'name': 'CH3S + C2H5 <=> C3H8S'}, {'dA': 0.0015246153495242511, 'dE0': -0.0, 'dn': -0.0005043646829815884, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + C4H9 <=> C4H9O2'}, {'dA': 0.09535109375137181, 'dE0': -0.0, 'dn': -0.0005070350529564525, 'dA_dEa': 0.4866030401054469, 'dE0_dEa': -0.0, 'dn_dEa': -0.15568995420430276, 'name': 'CH3S + CH3 <=> C2H6S'}, {'dA': 0.0015245591100667157, 'dE0': -0.0, 'dn': -0.0005043444789981973, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + C2H3 <=> C2H3O2'}, {'dA': 0.09535109374604274, 'dE0': -0.0, 'dn': -0.0005070350513869007, 'dA_dEa': 0.48660304010367056, 'dE0_dEa': -0.0, 'dn_dEa': -0.15568995420430276, 'name': 'CH3S + C4H9 <=> C5H12S'}, {'dA': 0.003323711268877016, 'dE0': -0.0, 'dn': -0.0005050095414458567, 'dA_dEa': -0.0009903893900543562, 'dE0_dEa': -0.0, 'dn_dEa': 0.00026150307254293255, 'name': 'O2 + C6H5 <=> C6H5O2'}, {'dA': 0.001524570356181866, 'dE0': -0.0, 'dn': -0.0005043484642327441, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + CHO <=> CHO3'}, {'dA': 0.0, 'dE0': -0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + C2H3O <=> C2H3O3'}, {'dA': 0.0015245564934930913, 'dE0': -0.0, 'dn': -0.0005043435508223747, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C3H5 <=> C6H10-2'}, {'dA': 0.0015245474322968535, 'dE0': -0.0, 'dn': -0.0005043402950013261, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C2H5 <=> C5H10-2'}, {'dA': 0.0015245937863285776, 'dE0': -0.0, 'dn': -0.0005043569386706315, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + CH3 <=> C4H8-2'}, {'dA': 0.001524601094260615, 'dE0': -0.0, 'dn': -0.0005043595652441201, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C3H7-2 <=> C6H12'}, {'dA': 0.001524609809067269, 'dE0': -0.0, 'dn': -0.0005043627472962371, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C4H9 <=> C7H14'}, {'dA': 0.0015245564934930913, 'dE0': -0.0, 'dn': -0.0005043435508223747, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C5H7 <=> C8H12'}, {'dA': 0.0033228508478092885, 'dE0': -0.0, 'dn': -0.0005047011686196759, 'dA_dEa': 0.009131682377373392, 'dE0_dEa': -0.0, 'dn_dEa': -0.002975741003383664, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}, {'dA': 0.0015246360085542933, 'dE0': -0.0, 'dn': -0.0005043720999696646, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H3-2 + CH3 <=> C4H6-5'}, {'dA': 0.0033220707003071333, 'dE0': -0.0, 'dn': -0.0005044205794275973, 'dA_dEa': -0.0023460476583639176, 'dE0_dEa': -0.0, 'dn_dEa': 0.0006953065431685115, 'name': 'C5H5 + CH3 <=> C6H8'}, {'dA': 0.001524526576091202, 'dE0': -0.0, 'dn': -0.0005043328116640173, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C5H5 + C5H5 <=> C10H10-6'}, {'dA': 0.0953437894910641, 'dE0': -0.0, 'dn': -0.000504415580690688, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'NO2 + OH <=> HNO3'}, {'dA': 0.0033217281032453024, 'dE0': -0.0, 'dn': -0.0005042977006489746, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'NO2 + OH <=> HNO3'}, {'dA': 0.02489008860884486, 'dE0': -0.0, 'dn': -0.0005045871944788033, 'dA_dEa': 0.059399885840256565, 'dE0_dEa': -0.0, 'dn_dEa': -0.01905368603679712, 'name': 'O2 + C6H5 <=> C6H5O2'}, {'dA': 0.024874558764767483, 'dE0': -0.0, 'dn': -0.0004990145221542751, 'dA_dEa': 0.09746704203551466, 'dE0_dEa': -0.0, 'dn_dEa': -0.03122858705863898, 'name': 'O2 + C10H7 <=> C10H7O2'}, {'dA': 0.024877722479391094, 'dE0': -0.0, 'dn': -0.0005001348317990657, 'dA_dEa': 0.06620146479897233, 'dE0_dEa': -0.0, 'dn_dEa': -0.0212283167742813, 'name': 'O2 + C10H7-2 <=> C10H7O2-2'}, {'dA': 0.02458256343374203, 'dE0': -0.0, 'dn': -0.00039419741864636204, 'dA_dEa': 0.0996905717549733, 'dE0_dEa': -0.0, 'dn_dEa': -0.03193846234825871, 'name': 'O2 + C7H7 <=> C7H7O2'}, {'dA': 0.02489086658563896, 'dE0': -0.0, 'dn': -0.0005048511648290315, 'dA_dEa': 0.05194738335135302, 'dE0_dEa': -0.0, 'dn_dEa': -0.016669926588978472, 'name': 'C6H5 + C6H5 <=> C12H10'}, {'dA': 0.0033218385357972943, 'dE0': -0.0, 'dn': -0.0005043372851718408, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C11H23 + CH3 <=> C12H26'}, {'dA': 0.0033217444705972207, 'dE0': -0.0, 'dn': -0.0005043036750763181, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C10H21 + C2H5 <=> C12H26-2'}, {'dA': 0.0033223974469368863, 'dE0': -0.0, 'dn': -0.0005045380057261722, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C9H19 + C3H7 <=> C12H26-3'}, {'dA': 0.0033209177168206697, 'dE0': -0.0, 'dn': -0.0005040068953873263, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C8H17 + C4H9-2 <=> C12H26-4'}, {'dA': 0.0033224707802762873, 'dE0': -0.0, 'dn': -0.000504564398452062, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C7H15 + C5H11 <=> C12H26-5'}, {'dA': 0.0033218985358022587, 'dE0': -0.0, 'dn': -0.0005043588413953963, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C6H13 + C6H13 <=> C12H26-6'}, {'dA': 0.003321849522564346, 'dE0': -0.0, 'dn': -0.0005043412327371458, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C9H19 <=> C10H22'}, {'dA': 0.003321957088076399, 'dE0': -0.0, 'dn': -0.0005043798528418127, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C8H17 + C2H5 <=> C10H22-2'}, {'dA': 0.003321887371399523, 'dE0': -0.0, 'dn': -0.0005043547739734132, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C7H15 + C3H7 <=> C10H22-3'}, {'dA': 0.003320536638540627, 'dE0': -0.0, 'dn': -0.0005038699528543943, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C6H13 + C4H9-2 <=> C10H22-4'}, {'dA': 0.0033218420032458448, 'dE0': -0.0, 'dn': -0.0005043385389583055, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C5H11 + C5H11 <=> C10H22-5'}, {'dA': 0.0033301744171158392, 'dE0': -0.0, 'dn': -0.0005073300132496081, 'dA_dEa': -0.004710089729798547, 'dE0_dEa': -0.0, 'dn_dEa': 0.001451169614781961, 'name': 'CH3 + C7H15-2 <=> C8H18-2'}, {'dA': 0.0033243512422846174, 'dE0': -0.0, 'dn': -0.0005052389338578866, 'dA_dEa': 0.013638270242923137, 'dE0_dEa': -0.0, 'dn_dEa': -0.004417056729651116, 'name': 'C4H9-3 + C4H9 <=> C8H18-3'}, {'dA': 0.003320951259766868, 'dE0': -0.0, 'dn': -0.0005040179150673852, 'dA_dEa': 0.01637573565460751, 'dE0_dEa': -0.0, 'dn_dEa': -0.005292580916781654, 'name': 'C5H11-2 + C3H7-2 <=> C8H18-4'}, {'dA': 0.00333755468417999, 'dE0': -0.0, 'dn': -0.0005099742106638852, 'dA_dEa': 0.017587659209896404, 'dE0_dEa': -0.0, 'dn_dEa': -0.005680655399810168, 'name': 'C7H15-3 + CH3 <=> C8H18-5'}]
""",
)

entry(
    index = 51,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_N-2CNO->O",
    kinetics = ArrheniusBM(A=(5.37e+07,'m^3/(mol*s)'), n=0.15395, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.07241189931, var=2.92956615883, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_N-2CNO->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_N-2CNO->O
        Total Standard Deviation in ln(k): 6.12580189805"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_N-2CNO->O
Total Standard Deviation in ln(k): 6.12580189805""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_N-2CNO->O
Total Standard Deviation in ln(k): 6.12580189805
sensitivities = [{'dA': 0.9411626248622056, 'dE0': 0.0, 'dn': -0.0005152775105053205, 'dA_dEa': -0.993700823880171, 'dE0_dEa': 0.0, 'dn_dEa': 0.9998267645527623, 'name': 'H + CH3 <=> CH4'}, {'dA': 0.05902364647170739, 'dE0': 0.0, 'dn': -0.00025909797622238875, 'dA_dEa': 0.0004535981510401188, 'dE0_dEa': 0.0, 'dn_dEa': -0.0005120821752344353, 'name': 'H + CH3 <=> CH4'}]
""",
)

entry(
    index = 52,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_2CNO->O",
    kinetics = ArrheniusBM(A=(7.97874e+07,'m^3/(mol*s)'), n=0.0908733, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_2CNO->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_2CNO->O
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_2CNO->O
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_2CNO->O
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'H + OH <=> H2O'}]
""",
)

entry(
    index = 53,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(308.407,'m^3/(mol*s)'), n=0.967216, w0=(139000,'J/mol'), E0=(13900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0049236047651, var=0.0302625193734, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R
        Total Standard Deviation in ln(k): 0.361117102774"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R
Total Standard Deviation in ln(k): 0.361117102774""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R
Total Standard Deviation in ln(k): 0.361117102774
sensitivities = [{'dA': 0.0044628438216070465, 'dE0': 0.0, 'dn': -1.0897772012281752e-05, 'dA_dEa': -0.05602369921132228, 'dE0_dEa': 0.0, 'dn_dEa': 0.006351359770421504, 'name': '[O][O] + [CH2]CC <=> C3H7O2'}, {'dA': 0.1373448277659657, 'dE0': 0.0, 'dn': -1.0953244770965918e-05, 'dA_dEa': 0.5715457151920863, 'dE0_dEa': 0.0, 'dn_dEa': -0.06480852002277031, 'name': 'C3H3 + O2 <=> C3H3O2'}, {'dA': 0.8579526354194179, 'dE0': 0.0, 'dn': -1.1100926283311198e-05, 'dA_dEa': 3.5918476822129413, 'dE0_dEa': 0.0, 'dn_dEa': -0.4072794872723825, 'name': 'O2 + C7H7 <=> C7H7O2'}]
""",
)

entry(
    index = 54,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2CNO_N-Sp-5R!H-=4R!H",
    kinetics = ArrheniusBM(A=(1.5283e+07,'m^3/(mol*s)'), n=-0.385614, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0775690385099, var=0.0415445018793, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2CNO_N-Sp-5R!H-=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2CNO_N-Sp-5R!H-=4R!H
        Total Standard Deviation in ln(k): 0.603511575689"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2CNO_N-Sp-5R!H-=4R!H
Total Standard Deviation in ln(k): 0.603511575689""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2CNO_N-Sp-5R!H-=4R!H
Total Standard Deviation in ln(k): 0.603511575689
sensitivities = [{'dA': 0.5000768517931515, 'dE0': 0.0, 'dn': 3.4149099904108235e-05, 'dA_dEa': 10.33138173858575, 'dE0_dEa': 0.0, 'dn_dEa': 0.9623316353628342, 'name': 'C=C1[CH]c2ccccc2C1 + [H] <=> C10H10-3'}, {'dA': 0.5001403075333695, 'dE0': 0.0, 'dn': 4.0768748182133035e-05, 'dA_dEa': -0.06799985186845742, 'dE0_dEa': 0.0, 'dn_dEa': -0.006330269647070976, 'name': 'C=C1C[CH]c2ccccc21 + [H] <=> C10H10-5'}]
""",
)

entry(
    index = 55,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(4.50099e+08,'m^3/(mol*s)'), n=-0.701965, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0017319911826, var=1.36934858384, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R
        Total Standard Deviation in ln(k): 2.35027605843"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 2.35027605843""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 2.35027605843
sensitivities = [{'dA': 0.024305945920846575, 'dE0': 0.0, 'dn': -1.776014078527371e-05, 'dA_dEa': -5.55717249994875e-06, 'dE0_dEa': 0.0, 'dn_dEa': -1.4080677916084728e-06, 'name': 'CH3 + C4H9 <=> C5H12'}, {'dA': 0.024373194165153066, 'dE0': 0.0, 'dn': -1.2366994505328198e-06, 'dA_dEa': -5.55717249994875e-06, 'dE0_dEa': 0.0, 'dn_dEa': -1.4080677916084728e-06, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.024413852816709738, 'dE0': 0.0, 'dn': 8.739622234369133e-06, 'dA_dEa': -5.55717249994875e-06, 'dE0_dEa': 0.0, 'dn_dEa': -1.4080677916084728e-06, 'name': 'C3H7-2 + C4H9 <=> C7H16'}, {'dA': 0.02437010459033486, 'dE0': 0.0, 'dn': -1.9776671167308898e-06, 'dA_dEa': -5.55717249994875e-06, 'dE0_dEa': 0.0, 'dn_dEa': -1.4080677916084728e-06, 'name': 'C4H9 + C4H9 <=> C8H18'}, {'dA': 0.02441162340005845, 'dE0': 0.0, 'dn': 8.205688228963425e-06, 'dA_dEa': -5.55717249994875e-06, 'dE0_dEa': 0.0, 'dn_dEa': -1.4080677916084728e-06, 'name': 'C4H9 + CHO <=> C5H10O-2'}, {'dA': 0.024342309341565577, 'dE0': 0.0, 'dn': -8.831015947317848e-06, 'dA_dEa': -5.55717249994875e-06, 'dE0_dEa': 0.0, 'dn_dEa': -1.4080677916084728e-06, 'name': 'C4H9 + C2H3O <=> C6H12O'}, {'dA': 0.024370467734516253, 'dE0': 0.0, 'dn': -1.9061633513173563e-06, 'dA_dEa': -0.05686784213310774, 'dE0_dEa': 0.0, 'dn_dEa': -0.012454631727243088, 'name': 'CH3 + C4H9 <=> C5H12'}, {'dA': 0.024400293302309552, 'dE0': 0.0, 'dn': 5.430957892851397e-06, 'dA_dEa': -5.55717249994875e-06, 'dE0_dEa': 0.0, 'dn_dEa': -1.4080677916084728e-06, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.02437688918277827, 'dE0': 0.0, 'dn': -3.2475072959385225e-07, 'dA_dEa': 0.012253617398984246, 'dE0_dEa': 0.0, 'dn_dEa': 0.0026795976284051787, 'name': 'C3H5 + C4H9 <=> C7H14'}, {'dA': 0.38989758262535223, 'dE0': 0.0, 'dn': -3.724504230840651e-05, 'dA_dEa': -1.2455237677359272, 'dE0_dEa': 0.0, 'dn_dEa': -0.2727753268024211, 'name': 'CH3 + C7H15-2 <=> C8H18-2'}, {'dA': 0.3900946698039295, 'dE0': 0.0, 'dn': 1.1211356898445315e-05, 'dA_dEa': 2.4893168781122097, 'dE0_dEa': 0.0, 'dn_dEa': 0.5451659803802863, 'name': 'C4H9-3 + C4H9 <=> C8H18-3'}]
""",
)

entry(
    index = 56,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=1.10623e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->O
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->O
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->O
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'O2 + C2H3 <=> C2H3O2'}]
""",
)

entry(
    index = 57,
    label = "Root_N-1R->H_1CNOS->N_Ext-1N-R_Ext-1N-R",
    kinetics = ArrheniusBM(A=(1.08281e+07,'m^3/(mol*s)'), n=0.100375, w0=(75166.7,'J/mol'), E0=(7516.67,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.09139294411, var=4.01089233273, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1CNOS->N_Ext-1N-R_Ext-1N-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-1N-R_Ext-1N-R
        Total Standard Deviation in ln(k): 6.75711883075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-1N-R_Ext-1N-R
Total Standard Deviation in ln(k): 6.75711883075""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-1N-R_Ext-1N-R
Total Standard Deviation in ln(k): 6.75711883075
sensitivities = [{'dA': 0.09812265739129715, 'dE0': 0.0, 'dn': 9.48331375711206e-06, 'dA_dEa': -2.216054757914665, 'dE0_dEa': 0.0, 'dn_dEa': 0.7560697029764245, 'name': '[CH3] + [O-][N+]=O <=> CH3NO2'}, {'dA': 0.8831941374031067, 'dE0': 0.0, 'dn': 5.048623422459821e-05, 'dA_dEa': -0.0002219859425167914, 'dE0_dEa': 0.0, 'dn_dEa': 8.499429236083773e-05, 'name': 'NO2 + OH <=> HNO3'}, {'dA': 0.017800926540802748, 'dE0': 0.0, 'dn': 8.658205468176594e-05, 'dA_dEa': -0.0002219859425167914, 'dE0_dEa': 0.0, 'dn_dEa': 8.499429236083773e-05, 'name': 'NO2 + OH <=> HNO3'}]
""",
)

entry(
    index = 58,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C_3C-inRing",
    kinetics = ArrheniusBM(A=(4.64183e+06,'m^3/(mol*s)'), n=0.438923, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.000133802134542, var=0.433753886377, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C_3C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C_3C-inRing
        Total Standard Deviation in ln(k): 1.32065459619"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C_3C-inRing
Total Standard Deviation in ln(k): 1.32065459619""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C_3C-inRing
Total Standard Deviation in ln(k): 1.32065459619
sensitivities = [{'dA': 0.4997517746439524, 'dE0': 0.0, 'dn': -5.131240122659368e-07, 'dA_dEa': 0.0019599157745633306, 'dE0_dEa': 0.0, 'dn_dEa': -0.0005563803464704602, 'name': 'C6H7-3 + H <=> C6H8-4'}, {'dA': 0.49975007116037595, 'dE0': 0.0, 'dn': 2.7684636452938e-08, 'dA_dEa': -0.017607265350607356, 'dE0_dEa': 0.0, 'dn_dEa': 0.0049972198818675345, 'name': 'C6H7-5 + H <=> C6H8-6'}]
""",
)

entry(
    index = 59,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C",
    kinetics = ArrheniusBM(A=(9.3042e+08,'m^3/(mol*s)'), n=-0.614675, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0056097018252, var=3.01068616167, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C
        Total Standard Deviation in ln(k): 3.4925765058"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C
Total Standard Deviation in ln(k): 3.4925765058""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C
Total Standard Deviation in ln(k): 3.4925765058
sensitivities = [{'dA': 0.4913180106989587, 'dE0': 0.0, 'dn': 6.250330092696199e-06, 'dA_dEa': -0.0393775876048651, 'dE0_dEa': 0.0, 'dn_dEa': -0.007957478914946605, 'name': 'CH3 + C2H5 <=> C3H8'}, {'dA': 0.49132021161218814, 'dE0': 0.0, 'dn': 6.758370239752609e-06, 'dA_dEa': 0.006186584858625792, 'dE0_dEa': 0.0, 'dn_dEa': 0.0012511880150112146, 'name': 'C2H5 + C2H5 <=> C4H10'}, {'dA': 0.005666413080974222, 'dE0': 0.0, 'dn': 6.040103505656965e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH3 + C2H5 <=> C3H8-3'}, {'dA': 0.005664189046684156, 'dE0': 0.0, 'dn': 5.5355690013853895e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + C2H5 <=> C4H10-3'}, {'dA': 0.005664487154888944, 'dE0': 0.0, 'dn': 5.603221541761059e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + CHO <=> C3H6O-2'}]
""",
)

entry(
    index = 60,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing",
    kinetics = ArrheniusBM(A=(1.79861e+10,'m^3/(mol*s)'), n=-0.973503, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0958344498313, var=0.310258299277, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing
        Total Standard Deviation in ln(k): 1.35744424775"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing
Total Standard Deviation in ln(k): 1.35744424775""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing
Total Standard Deviation in ln(k): 1.35744424775
sensitivities = [{'dA': 0.2331073692048137, 'dE0': 0.0, 'dn': 2.016678667313579e-06, 'dA_dEa': 0.4560398616320574, 'dE0_dEa': 0.0, 'dn_dEa': 0.058691182449378425, 'name': 'C5H5 + C2H5 <=> C7H10'}, {'dA': 0.6474940886037219, 'dE0': 0.0, 'dn': 1.7897472784041368e-06, 'dA_dEa': -0.005053950122402841, 'dE0_dEa': 0.0, 'dn_dEa': -0.0006502220592593209, 'name': 'C5H5 + CH3 <=> C6H8'}, {'dA': 0.11892395579239579, 'dE0': 0.0, 'dn': -1.8248682138857525e-07, 'dA_dEa': -0.2326502059553349, 'dE0_dEa': 0.0, 'dn_dEa': -0.029941129253418537, 'name': 'C5H5 + CH3 <=> C6H8'}]
""",
)

entry(
    index = 61,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R",
    kinetics = ArrheniusBM(A=(6.35497e+07,'m^3/(mol*s)'), n=0.0334649, w0=(186521,'J/mol'), E0=(18652.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.265312187046, var=2.03347824868, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R
        Total Standard Deviation in ln(k): 3.5253673363"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R
Total Standard Deviation in ln(k): 3.5253673363""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R
Total Standard Deviation in ln(k): 3.5253673363
sensitivities = [{'dA': 0.053240504950486135, 'dE0': 0.0, 'dn': 0.0003632781425659192, 'dA_dEa': -0.0002697618839420399, 'dE0_dEa': 0.0, 'dn_dEa': 0.00022142800778873908, 'name': 'C6H7-3 + H <=> C6H8-4'}, {'dA': 0.05323811816993516, 'dE0': 0.0, 'dn': 0.00036508488022686953, 'dA_dEa': -0.002388038819134671, 'dE0_dEa': 0.0, 'dn_dEa': 0.0016507639514736928, 'name': 'C6H7-5 + H <=> C6H8-6'}, {'dA': 0.01886116322680417, 'dE0': 0.0, 'dn': 0.00036185867266042444, 'dA_dEa': 0.060068288235022256, 'dE0_dEa': 0.0, 'dn_dEa': -0.040455131921144506, 'name': 'C6H7-6 + H <=> C6H8-7'}, {'dA': 0.05323973277172076, 'dE0': 0.0, 'dn': 0.00036386160164200417, 'dA_dEa': 0.061322251529112394, 'dE0_dEa': 0.0, 'dn_dEa': -0.0412998725400581, 'name': 'H + NJCO <=> HNCO'}, {'dA': 0.053231238055679066, 'dE0': 0.0, 'dn': 0.00037029704479735653, 'dA_dEa': 0.061277040018132924, 'dE0_dEa': 0.0, 'dn_dEa': -0.041265662943391825, 'name': 'H + NCOJ <=> NCOH'}, {'dA': 0.018215867029882434, 'dE0': 0.0, 'dn': 0.0008499474786790931, 'dA_dEa': 1.0842043575892775, 'dE0_dEa': 0.0, 'dn_dEa': -0.7308578853270413, 'name': '[CH2]c1ccccc1[C]=C=C + [H] <=> C10H9'}, {'dA': 0.00013648216068419655, 'dE0': 0.0, 'dn': 0.00036331737839402715, 'dA_dEa': -0.00040496538034067185, 'dE0_dEa': 0.0, 'dn_dEa': 0.0003125967736678698, 'name': 'C3H3 + H <=> C3H4'}, {'dA': 0.00013641101404006487, 'dE0': 0.0, 'dn': 0.00036337118055677784, 'dA_dEa': -6.261240415029314e-05, 'dE0_dEa': 0.0, 'dn_dEa': 8.180789976500081e-05, 'name': 'C3H3-2 + H <=> C3H4-2'}, {'dA': 0.05324353252334522, 'dE0': 0.0, 'dn': 0.0003609883825475442, 'dA_dEa': -0.21131649206298617, 'dE0_dEa': 0.0, 'dn_dEa': 0.1424948371514312, 'name': 'C4H5 + H <=> C4H6-2'}, {'dA': 0.053234102061600376, 'dE0': 0.0, 'dn': 0.0003681206955487106, 'dA_dEa': 0.21224944838496135, 'dE0_dEa': 0.0, 'dn_dEa': -0.14304470821150142, 'name': 'C4H5-2 + H <=> C4H6-3'}, {'dA': 0.01885780769583997, 'dE0': 0.0, 'dn': 0.0003643922484507741, 'dA_dEa': 0.0028486882008852215, 'dE0_dEa': 0.0, 'dn_dEa': -0.001880736657717679, 'name': 'C7H7 + H <=> C7H8-2'}, {'dA': 0.0001364948367666025, 'dE0': 0.0, 'dn': 0.00036330776589733535, 'dA_dEa': -0.00048022227971960835, 'dE0_dEa': 0.0, 'dn_dEa': 0.0003633273149412527, 'name': 'H + C2H5 <=> C2H6-2'}, {'dA': 0.00013617177074822073, 'dE0': 0.0, 'dn': 0.0003635518231659027, 'dA_dEa': -0.00048022227971960835, 'dE0_dEa': 0.0, 'dn_dEa': 0.0003633273149412527, 'name': 'H + C3H7-2 <=> C3H8-2'}, {'dA': 0.00938785482063157, 'dE0': 0.0, 'dn': 0.0003625584893360808, 'dA_dEa': -0.00048022227971960835, 'dE0_dEa': 0.0, 'dn_dEa': 0.0003633273149412527, 'name': 'H + C2H3 <=> C2H4'}, {'dA': 0.00013606293691738436, 'dE0': 0.0, 'dn': 0.00036363441936137185, 'dA_dEa': -0.00048022227971960835, 'dE0_dEa': 0.0, 'dn_dEa': 0.0003633273149412527, 'name': 'H + C2H <=> C2H2'}, {'dA': 0.00014147449078906642, 'dE0': 0.0, 'dn': 0.00035954171044179063, 'dA_dEa': 0.010439964437837275, 'dE0_dEa': 0.0, 'dn_dEa': -0.006997413412754477, 'name': 'H + CHO <=> CH2O'}, {'dA': 0.00013642076979182685, 'dE0': 0.0, 'dn': 0.00036336380212912556, 'dA_dEa': -0.0015661640730970153, 'dE0_dEa': 0.0, 'dn_dEa': 0.001095400393498065, 'name': 'O2 + H <=> HO2-2'}, {'dA': 0.48300710029641525, 'dE0': 0.0, 'dn': 0.00036229754264391654, 'dA_dEa': 0.6995041338307633, 'dE0_dEa': 0.0, 'dn_dEa': -0.4715185910135708, 'name': 'CH3S-2 + H <=> CH4S'}, {'dA': 0.009386166873072067, 'dE0': 0.0, 'dn': 0.0003638353117454987, 'dA_dEa': -0.0052688717495647215, 'dE0_dEa': 0.0, 'dn_dEa': 0.003591601432389684, 'name': 'H + C3H5 <=> C3H6-2'}, {'dA': 0.00013642705454232465, 'dE0': 0.0, 'dn': 0.0003633590562549278, 'dA_dEa': -0.0007795128631472329, 'dE0_dEa': 0.0, 'dn_dEa': 0.000565094442281928, 'name': 'H + C4H7 <=> C4H8'}, {'dA': 0.00013642705454232465, 'dE0': 0.0, 'dn': 0.0003633590562549278, 'dA_dEa': -0.0007795128631472329, 'dE0_dEa': 0.0, 'dn_dEa': 0.000565094442281928, 'name': 'H + C5H9 <=> C5H10'}, {'dA': 0.00013642705454232465, 'dE0': 0.0, 'dn': 0.0003633590562549278, 'dA_dEa': -0.0007795128631472329, 'dE0_dEa': 0.0, 'dn_dEa': 0.000565094442281928, 'name': 'H + C6H9 <=> C6H10'}, {'dA': 0.00013606662463418295, 'dE0': 0.0, 'dn': 0.0003636319944709275, 'dA_dEa': -0.00048022227971960835, 'dE0_dEa': 0.0, 'dn_dEa': 0.0003633273149412527, 'name': 'C3H3-2 + H <=> C3H4-2'}, {'dA': 0.00013617177074822073, 'dE0': 0.0, 'dn': 0.0003635518228651598, 'dA_dEa': -0.00048022227971960835, 'dE0_dEa': 0.0, 'dn_dEa': 0.0003633273149412527, 'name': 'H + C5H7 <=> C5H8'}, {'dA': 0.009389505589042425, 'dE0': 0.0, 'dn': 0.0003613094494104529, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C12H25 <=> C12H26-7'}, {'dA': 0.009388470854078047, 'dE0': 0.0, 'dn': 0.00036209200453299594, 'dA_dEa': -0.00017125508477990547, 'dE0_dEa': 0.0, 'dn_dEa': 0.00015503454742268858, 'name': 'H + C12H25-2 <=> C12H26-8'}, {'dA': 0.009388470854078047, 'dE0': 0.0, 'dn': 0.0003620920043826244, 'dA_dEa': -0.00017125508477990547, 'dE0_dEa': 0.0, 'dn_dEa': 0.00015503454742268858, 'name': 'H + C12H25-3 <=> C12H26-9'}, {'dA': 0.009388470854078047, 'dE0': 0.0, 'dn': 0.0003620920043826244, 'dA_dEa': -0.00017125508477990547, 'dE0_dEa': 0.0, 'dn_dEa': 0.00015503454742268858, 'name': 'H + C12H25-4 <=> C12H26-10'}, {'dA': 0.009388470854078047, 'dE0': 0.0, 'dn': 0.00036209200453299594, 'dA_dEa': -0.00017125508477990547, 'dE0_dEa': 0.0, 'dn_dEa': 0.00015503454742268858, 'name': 'H + C12H25-5 <=> C12H26-11'}, {'dA': 0.009388470854078047, 'dE0': 0.0, 'dn': 0.00036209200453299594, 'dA_dEa': -0.00017125508477990547, 'dE0_dEa': 0.0, 'dn_dEa': 0.00015503454757306008, 'name': 'H + C12H25-6 <=> C12H26-12'}, {'dA': 0.009390689733380565, 'dE0': 0.0, 'dn': 0.0003604139654587658, 'dA_dEa': -0.0007099478089856675, 'dE0_dEa': 0.0, 'dn_dEa': 0.0005180335269949303, 'name': 'H + C10H21 <=> C10H22-6'}, {'dA': 0.009390689733380565, 'dE0': 0.0, 'dn': 0.0003604139654587658, 'dA_dEa': -0.0007099478089856675, 'dE0_dEa': 0.0, 'dn_dEa': 0.0005180335269949303, 'name': 'H + C10H21-2 <=> C10H22-7'}, {'dA': 0.009390689733380565, 'dE0': 0.0, 'dn': 0.00036041396530839433, 'dA_dEa': -0.0007099478089856675, 'dE0_dEa': 0.0, 'dn_dEa': 0.0005180335269949303, 'name': 'H + C10H21-3 <=> C10H22-8'}, {'dA': 0.009390689733380565, 'dE0': 0.0, 'dn': 0.0003604139654587658, 'dA_dEa': -0.0007099478089856675, 'dE0_dEa': 0.0, 'dn_dEa': 0.0005180335269949303, 'name': 'H + C10H21-4 <=> C10H22-9'}, {'dA': 0.009390689733380565, 'dE0': 0.0, 'dn': 0.00036041396530839433, 'dA_dEa': -0.0007099478089856675, 'dE0_dEa': 0.0, 'dn_dEa': 0.0005180335269949303, 'name': 'H + C10H21-5 <=> C10H22-10'}]
""",
)

entry(
    index = 62,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.08049e+08,'m^3/(mol*s)'), n=-0.685207, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.691788023649, var=1.05747121089, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R
        Total Standard Deviation in ln(k): 3.79969848986"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.79969848986""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.79969848986
sensitivities = [{'dA': 0.9770678582975388, 'dE0': 0.0, 'dn': 4.073981938892644e-08, 'dA_dEa': 0.012234711771698341, 'dE0_dEa': 0.0, 'dn_dEa': 0.002223003861435974, 'name': 'C2H5 + C2H5 <=> C4H10'}, {'dA': 0.011216722590746811, 'dE0': 0.0, 'dn': 7.865088318787361e-08, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + C2H5 <=> C4H10-3'}, {'dA': 0.011216537217252479, 'dE0': 0.0, 'dn': 4.0738036117020324e-08, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + CHO <=> C3H6O-2'}]
""",
)

entry(
    index = 63,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R",
    kinetics = ArrheniusBM(A=(4.63831e+07,'m^3/(mol*s)'), n=-6.58468e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0123271345724, var=1.99454645199, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R
        Total Standard Deviation in ln(k): 2.86222822617"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R
Total Standard Deviation in ln(k): 2.86222822617""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R
Total Standard Deviation in ln(k): 2.86222822617
sensitivities = [{'dA': 0.1973288307049121, 'dE0': 0.0, 'dn': -16476.22936733264, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH3 + C2H3 <=> C3H6'}, {'dA': -0.003922723237792957, 'dE0': 0.0, 'dn': -4544.281951462628, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH3 + CHO <=> C2H4O'}, {'dA': -0.015453493482199857, 'dE0': 0.0, 'dn': -6977.253043512561, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H3 + C2H3 <=> C4H6-4'}, {'dA': 0.22043072626234603, 'dE0': 0.0, 'dn': -13216.131432833927, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H3 + C2H <=> C4H4'}, {'dA': -0.003922723703198449, 'dE0': 0.0, 'dn': -4544.282108283668, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H3 + CHO <=> C3H4O'}, {'dA': 0.2905045772508039, 'dE0': 0.0, 'dn': -3315.0332729253555, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CHO + CHO <=> C2H2O2'}]
""",
)

entry(
    index = 64,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(5.15801e+06,'m^3/(mol*s)'), n=0.423463, w0=(201667,'J/mol'), E0=(20166.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00140340965819, var=0.294742016181, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C
        Total Standard Deviation in ln(k): 1.09189979396"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 1.09189979396""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 1.09189979396
sensitivities = [{'dA': 0.45773333772918856, 'dE0': 0.0, 'dn': -6.03385173580939e-06, 'dA_dEa': 0.00179818774093141, 'dE0_dEa': 0.0, 'dn_dEa': -0.0005307453710883445, 'name': 'C6H7-3 + H <=> C6H8-4'}, {'dA': 0.4577226664573224, 'dE0': 0.0, 'dn': -2.50220287625788e-06, 'dA_dEa': -0.016103690692050417, 'dE0_dEa': 0.0, 'dn_dEa': 0.004750229558757381, 'name': 'C6H7-5 + H <=> C6H8-6'}, {'dA': 0.08409164588663957, 'dE0': 0.0, 'dn': -7.12514869824634e-06, 'dA_dEa': -0.04076985258372639, 'dE0_dEa': 0.0, 'dn_dEa': 0.012026832510298405, 'name': 'H + C3H5 <=> C3H6-2'}]
""",
)

entry(
    index = 65,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R_Ext-3R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=1.78837e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R_Ext-3R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R_Ext-3R!H-R_Ext-4R!H-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'H + C5H7 <=> C5H8'}]
""",
)

entry(
    index = 66,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C_N-3C-inRing",
    kinetics = ArrheniusBM(A=(1.62598e+07,'m^3/(mol*s)'), n=0.255122, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C_N-3C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C_N-3C-inRing
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C_N-3C-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C_N-3C-inRing
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C3H5 <=> C3H6-2'}]
""",
)

entry(
    index = 67,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_4R!H-inRing",
    kinetics = ArrheniusBM(A=(601.137,'m^3/(mol*s)'), n=0.87177, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_4R!H-inRing
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_4R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_4R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'O2 + C7H7 <=> C7H7O2'}]
""",
)

entry(
    index = 68,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(45504,'m^3/(mol*s)'), n=0.740315, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R_Ext-1C-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330828247, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3S + C4H9 <=> C5H12S'}]
""",
)

entry(
    index = 69,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.48129e+07,'m^3/(mol*s)'), n=-0.157514, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R_Ext-5R!H-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'C3H5 + C3H5 <=> C6H10-2'}]
""",
)

entry(
    index = 70,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_N-3R!H->O",
    kinetics = ArrheniusBM(A=(9.04e+06,'m^3/(mol*s)'), n=-5.64022e-08, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_N-3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_N-3R!H->O
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_N-3R!H->O
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_N-3R!H->O
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'C4H9 + CH3O <=> C5H12O'}]
""",
)

entry(
    index = 71,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-3CS-R_2CNO->N",
    kinetics = ArrheniusBM(A=(1.12206e+07,'m^3/(mol*s)'), n=0.314888, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-3CS-R_2CNO->N',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-3CS-R_2CNO->N
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-3CS-R_2CNO->N
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-3CS-R_2CNO->N
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + NJCO <=> HNCO'}]
""",
)

entry(
    index = 72,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-2CNO-R",
    kinetics = ArrheniusBM(A=(9.28426e+17,'m^3/(mol*s)'), n=-3.05017, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.08884453463, var=70.5675449198, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-2CNO-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-2CNO-R
        Total Standard Deviation in ln(k): 24.6015908735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-2CNO-R
Total Standard Deviation in ln(k): 24.6015908735""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-2CNO-R
Total Standard Deviation in ln(k): 24.6015908735
sensitivities = [{'dA': 0.26526703884147274, 'dE0': 0.0, 'dn': 5.6515420867710694e-05, 'dA_dEa': 14.83916599673826, 'dE0_dEa': 0.0, 'dn_dEa': 1.0790986946756438, 'name': '[CH2]c1ccccc1[C]=C=C + [H] <=> C10H9'}, {'dA': 0.7354181567685558, 'dE0': 0.0, 'dn': 4.0148605206824626e-05, 'dA_dEa': -2.883839975261855, 'dE0_dEa': 0.0, 'dn_dEa': -0.20970685999349564, 'name': 'C4H5 + H <=> C4H6-2'}]
""",
)

entry(
    index = 73,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_5R!H-inRing",
    kinetics = ArrheniusBM(A=(1.11452e+11,'m^3/(mol*s)'), n=-1.43904, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_5R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_5R!H-inRing
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_5R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_5R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C3H3-2 + C7H7 <=> C10H10-2'}]
""",
)

entry(
    index = 74,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C",
    kinetics = ArrheniusBM(A=(15.724,'m^3/(mol*s)'), n=2.04268, w0=(71000,'J/mol'), E0=(-696.447,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.461512523709, var=5.42084271959, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C
        Total Standard Deviation in ln(k): 5.82714440121"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C
Total Standard Deviation in ln(k): 5.82714440121""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C
Total Standard Deviation in ln(k): 5.82714440121
sensitivities = [{'dA': 0.7319404380652623, 'dE0': -0.0, 'dn': -0.0001987927382390102, 'dA_dEa': -7.96218899433625, 'dE0_dEa': -0.0, 'dn_dEa': 0.4545393953923679, 'name': '[SH] + [O][O] <=> HSOO'}, {'dA': 0.2591340888959134, 'dE0': -0.0, 'dn': 0.00020921169261785692, 'dA_dEa': 0.17501971685748002, 'dE0_dEa': -0.0, 'dn_dEa': -0.00978409386436403, 'name': 'OH + NO2-2 <=> HOONO'}, {'dA': 0.01455315005588647, 'dE0': -0.0, 'dn': -0.00039178581655093875, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'OH + CH3O <=> CH4O2'}]
""",
)

entry(
    index = 75,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(8.65419e+10,'m^3/(mol*s)'), n=-1.4012, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.218338226454, var=0.11719079963, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C
        Total Standard Deviation in ln(k): 1.23487231009"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 1.23487231009""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 1.23487231009
sensitivities = [{'dA': 0.9685543843148637, 'dE0': 0.0, 'dn': -5.364119540060577e-06, 'dA_dEa': -4.529280073129415, 'dE0_dEa': 0.0, 'dn_dEa': -0.3667417253094805, 'name': 'C3H3-2 + C7H7 <=> C10H10-2'}, {'dA': 0.030849840186423293, 'dE0': 0.0, 'dn': -3.368797956250298e-06, 'dA_dEa': 0.08102027132040672, 'dE0_dEa': 0.0, 'dn_dEa': 0.006559686177519925, 'name': 'C3H3 + C3H3-2 <=> C6H6-2'}]
""",
)

entry(
    index = 76,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing",
    kinetics = ArrheniusBM(A=(9.99999e+06,'m^3/(mol*s)'), n=1.28714e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.49162334898e-09, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing
        Total Standard Deviation in ln(k): 6.26036017332e-09"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing
Total Standard Deviation in ln(k): 6.26036017332e-09""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing
Total Standard Deviation in ln(k): 6.26036017332e-09
sensitivities = [{'dA': 0.4994974112584866, 'dE0': 0.0, 'dn': 307.1168407542454, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H5 + C3H3 <=> C9H8'}, {'dA': 0.5009406103049782, 'dE0': 0.0, 'dn': -1641.9230492625134, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H5 + C3H3-2 <=> C9H8-2'}]
""",
)

entry(
    index = 77,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C",
    kinetics = ArrheniusBM(A=(45504,'m^3/(mol*s)'), n=0.740315, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0441547025686, var=0.0, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C
        Total Standard Deviation in ln(k): 0.11094146374"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C
Total Standard Deviation in ln(k): 0.11094146374""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C
Total Standard Deviation in ln(k): 0.11094146374
sensitivities = [{'dA': 0.3333659609126383, 'dE0': 0.0, 'dn': -3.095084902978694e-05, 'dA_dEa': 1.7209660503516253, 'dE0_dEa': 0.0, 'dn_dEa': -0.23856868616624452, 'name': 'CH3S + C2H5 <=> C3H8S'}, {'dA': 0.3333356852906289, 'dE0': 0.0, 'dn': -2.6274891579523016e-05, 'dA_dEa': 1.720909300303409, 'dE0_dEa': 0.0, 'dn_dEa': -0.23855988697573513, 'name': 'CH3S + CH3 <=> C2H6S'}, {'dA': 0.33336596091619103, 'dE0': 0.0, 'dn': -3.0950849648212626e-05, 'dA_dEa': 1.7209093003051854, 'dE0_dEa': 0.0, 'dn_dEa': -0.2385598869761062, 'name': 'CH3S + C4H9 <=> C5H12S'}]
""",
)

entry(
    index = 78,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.23e+07,'m^3/(mol*s)'), n=-8.53421e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R_Ext-1C-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R_Ext-1C-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R_Ext-1C-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'C2H3 + C2H3 <=> C4H6-4'}]
""",
)

entry(
    index = 79,
    label = "Root_1R->H_N-2R->S_2CHNO->H",
    kinetics = ArrheniusBM(A=(30255.8,'m^3/(mol*s)'), n=0.454367, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0250878995306, var=56.1568697784, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2CHNO->H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2CHNO->H
        Total Standard Deviation in ln(k): 15.0860960863"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2CHNO->H
Total Standard Deviation in ln(k): 15.0860960863""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2CHNO->H
Total Standard Deviation in ln(k): 15.0860960863
sensitivities = [{'dA': 0.4988334110134768, 'dE0': 0.0, 'dn': 0.00035093981924563296, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + H <=> H2'}, {'dA': 0.49894723204607583, 'dE0': 0.0, 'dn': 0.0003072789967189484, 'dA_dEa': -2.9342331996658935, 'dE0_dEa': 0.0, 'dn_dEa': 1.0003761057698874, 'name': 'H + H <=> H2'}]
""",
)

entry(
    index = 80,
    label = "Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_N-2NO->O",
    kinetics = ArrheniusBM(A=(2.63e+08,'m^3/(mol*s)'), n=-1.1, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_N-2NO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_N-2NO->O
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_N-2NO->O
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_N-2NO->O
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'NO2 + NO2 <=> N2O4'}]
""",
)

entry(
    index = 81,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_3C-inRing",
    kinetics = ArrheniusBM(A=(8.89521e+07,'m^3/(mol*s)'), n=0.0353438, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_3C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_3C-inRing
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_3C-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_3C-inRing
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C7H7 + H <=> C7H8-2'}]
""",
)

entry(
    index = 82,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(3.10427e+07,'m^3/(mol*s)'), n=-0.214439, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_N-5R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_N-5R!H-inRing
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_N-5R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_N-5R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H3 + C3H3-2 <=> C6H6-2'}]
""",
)

entry(
    index = 83,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2CNO_N-Sp-5R!H-=4R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.73063e+08,'m^3/(mol*s)'), n=-0.91824, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2CNO_N-Sp-5R!H-=4R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2CNO_N-Sp-5R!H-=4R!H_Ext-3R!H-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2CNO_N-Sp-5R!H-=4R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2CNO_N-Sp-5R!H-=4R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C=C1[CH]c2ccccc2C1 + [H] <=> C10H10-3'}]
""",
)

entry(
    index = 84,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C",
    kinetics = ArrheniusBM(A=(1.72215e+10,'m^3/(mol*s)'), n=-0.966317, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.100863834071, var=0.318288919583, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C
        Total Standard Deviation in ln(k): 1.38444011628"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C
Total Standard Deviation in ln(k): 1.38444011628""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C
Total Standard Deviation in ln(k): 1.38444011628
sensitivities = [{'dA': 0.2313641400278043, 'dE0': 0.0, 'dn': -1.2629485584964744e-06, 'dA_dEa': 0.45266753133793014, 'dE0_dEa': 0.0, 'dn_dEa': 0.058690304505665744, 'name': 'C5H5 + C2H5 <=> C7H10'}, {'dA': 0.6426951152072744, 'dE0': 0.0, 'dn': -1.037088269252469e-06, 'dA_dEa': -0.005039072348723139, 'dE0_dEa': 0.0, 'dn_dEa': -0.000653489685853835, 'name': 'C5H5 + CH3 <=> C6H8'}, {'dA': 0.11803976405745566, 'dE0': 0.0, 'dn': -1.1060664723927946e-06, 'dA_dEa': -0.2309770625821527, 'dE0_dEa': 0.0, 'dn_dEa': -0.029947564247502067, 'name': 'C5H5 + CH3 <=> C6H8'}, {'dA': 0.007370959593800665, 'dE0': 0.0, 'dn': -1.021024693613435e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C5H5 + C5H5 <=> C10H10-6'}]
""",
)

entry(
    index = 85,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-2CNO-R",
    kinetics = ArrheniusBM(A=(5.22915e+07,'m^3/(mol*s)'), n=0.181361, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.150824113586, var=0.0951888293469, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-2CNO-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-2CNO-R
        Total Standard Deviation in ln(k): 0.997469697333"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-2CNO-R
Total Standard Deviation in ln(k): 0.997469697333""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-2CNO-R
Total Standard Deviation in ln(k): 0.997469697333
sensitivities = [{'dA': 0.17588289891891923, 'dE0': 0.0, 'dn': -2.0036393075102787e-05, 'dA_dEa': 0.015158925091187107, 'dE0_dEa': 0.0, 'dn_dEa': -0.009580154134773464, 'name': 'C6H7 + H <=> C6H8-2'}, {'dA': 0.03232938546915776, 'dE0': 0.0, 'dn': -2.0953587334668928e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C6H5 <=> C6H6-4'}, {'dA': 0.39570314469377005, 'dE0': 0.0, 'dn': -2.1417061972025962e-05, 'dA_dEa': 0.2400132701332589, 'dE0_dEa': 0.0, 'dn_dEa': -0.15166155506863988, 'name': 'H + C12H9-2 <=> C12H10-3'}, {'dA': 0.3957074560539278, 'dE0': 0.0, 'dn': -2.4475408835102994e-05, 'dA_dEa': -0.023192267807561673, 'dE0_dEa': 0.0, 'dn_dEa': 0.014652237142379095, 'name': 'H + C12H9-3 <=> C12H10-4'}]
""",
)

entry(
    index = 86,
    label = "Root_N-1R->H_1CNOS->N_Ext-1N-R_Ext-1N-R_2R->C",
    kinetics = ArrheniusBM(A=(2.33137e+11,'m^3/(mol*s)'), n=-1.13781, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1CNOS->N_Ext-1N-R_Ext-1N-R_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-1N-R_Ext-1N-R_2R->C
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-1N-R_Ext-1N-R_2R->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-1N-R_Ext-1N-R_2R->C
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': '[CH3] + [O-][N+]=O <=> CH3NO2'}]
""",
)

entry(
    index = 87,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(2.46571e+08,'m^3/(mol*s)'), n=-0.461716, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_N-3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_N-3R!H-inRing
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_N-3R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_N-3R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C3H3 + C3H3 <=> C6H6-3'}]
""",
)

entry(
    index = 88,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H",
    kinetics = ArrheniusBM(A=(6.28654e+07,'m^3/(mol*s)'), n=-0.211676, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00579809229276, var=0.287312654976, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H
        Total Standard Deviation in ln(k): 1.0891372184"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H
Total Standard Deviation in ln(k): 1.0891372184""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H
Total Standard Deviation in ln(k): 1.0891372184
sensitivities = [{'dA': 0.333051555262679, 'dE0': 0.0, 'dn': -8.421159730391826e-05, 'dA_dEa': 0.3388410880909394, 'dE0_dEa': 0.0, 'dn_dEa': 0.22071444211312813, 'name': 'C3H5 + C3H5 <=> C6H10-2'}, {'dA': 0.3331995122799836, 'dE0': 0.0, 'dn': 2.393081469420924e-05, 'dA_dEa': 0.16946740960223838, 'dE0_dEa': 0.0, 'dn_dEa': 0.11039148278501693, 'name': 'C3H5 + C2H5 <=> C5H10-2'}, {'dA': 0.33317598330743553, 'dE0': 0.0, 'dn': 6.733128821475445e-06, 'dA_dEa': 0.1693550451804713, 'dE0_dEa': 0.0, 'dn_dEa': 0.11030935151524884, 'name': 'C3H5 + CH3 <=> C4H8-2'}]
""",
)

entry(
    index = 89,
    label = "Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C",
    kinetics = ArrheniusBM(A=(9.18826e+09,'m^3/(mol*s)'), n=-0.839049, w0=(78500,'J/mol'), E0=(7850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0465430889647, var=0.673853817501, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C
        Total Standard Deviation in ln(k): 1.76260138417"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C
Total Standard Deviation in ln(k): 1.76260138417""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C
Total Standard Deviation in ln(k): 1.76260138417
sensitivities = [{'dA': 0.006068206603871531, 'dE0': 0.0, 'dn': -0.0003007793646108132, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'NO2 + NO2 <=> N2O4'}, {'dA': 0.0060976405453778745, 'dE0': 0.0, 'dn': -0.00032145439475181375, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'NO2 + NO3-2 <=> N2O5'}, {'dA': 0.49091518950566815, 'dE0': 0.0, 'dn': 0.00026346277658547134, 'dA_dEa': -4.5823965753731315, 'dE0_dEa': 0.0, 'dn_dEa': 2.8684677567402397, 'name': 'C[O] + [N]=O <=> CH3ONO'}, {'dA': 0.006100580902668857, 'dE0': 0.0, 'dn': -0.00032352006595393697, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'NH2 + HO2 <=> NH2OOH'}, {'dA': 0.49098348664960845, 'dE0': 0.0, 'dn': 0.00021546966023669738, 'dA_dEa': -0.07675191962342744, 'dE0_dEa': 0.0, 'dn_dEa': 0.04803281550125275, 'name': 'NH2 + CH3NH <=> CH3NHNH2'}]
""",
)

entry(
    index = 90,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(2.41364e+09,'m^3/(mol*s)'), n=-0.390932, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00603156000563, var=0.104335976043, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C
        Total Standard Deviation in ln(k): 0.662705751806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 0.662705751806""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 0.662705751806
sensitivities = [{'dA': 0.17149840292065235, 'dE0': 0.0, 'dn': 3.966116737898939e-05, 'dA_dEa': 0.5367268158736374, 'dE0_dEa': 0.0, 'dn_dEa': 0.3178615708226707, 'name': 'C6H7-6 + H <=> C6H8-7'}, {'dA': 0.00496012841111392, 'dE0': 0.0, 'dn': -0.00033667052497089663, 'dA_dEa': 0.00016073288477970842, 'dE0_dEa': 0.0, 'dn_dEa': 5.8572843260481544e-05, 'name': 'C3H3 + H <=> C3H4'}, {'dA': 0.47623343564145687, 'dE0': 0.0, 'dn': 9.826533668174702e-06, 'dA_dEa': 1.8858191776482813, 'dE0_dEa': 0.0, 'dn_dEa': 1.1168111589107912, 'name': 'C4H5-2 + H <=> C4H6-3'}, {'dA': 0.17146477062725762, 'dE0': 0.0, 'dn': 1.7311418959229638e-05, 'dA_dEa': 0.02900489161561701, 'dE0_dEa': 0.0, 'dn_dEa': 0.017140122709535327, 'name': 'C7H7 + H <=> C7H8-2'}, {'dA': 0.08757865478160452, 'dE0': 0.0, 'dn': 7.30438235569903e-05, 'dA_dEa': -0.001532185638808583, 'dE0_dEa': 0.0, 'dn_dEa': -0.0009439052795756839, 'name': 'H + C12H25 <=> C12H26-7'}, {'dA': 0.08741855474881785, 'dE0': 0.0, 'dn': -3.333738433297825e-05, 'dA_dEa': -0.0025606243845291464, 'dE0_dEa': 0.0, 'dn_dEa': -0.0015530808745777389, 'name': 'H + C10H21 <=> C10H22-6'}]
""",
)

entry(
    index = 91,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(4.65276e+06,'m^3/(mol*s)'), n=-1.19345e-07, w0=(132200,'J/mol'), E0=(13220,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.53321347418e-07, var=0.780952341849, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R
        Total Standard Deviation in ln(k): 1.77161500365"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 1.77161500365""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 1.77161500365
sensitivities = [{'dA': 0.15622654201232267, 'dE0': 0.0, 'dn': -18242.194122101817, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C3H7-2 + CH3O <=> C4H10O'}, {'dA': 0.014567431010805093, 'dE0': 0.0, 'dn': -77492.43172843561, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C4H9 + CH3O <=> C5H12O'}, {'dA': 0.2652861147272326, 'dE0': 0.0, 'dn': 27375.355556412662, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'O2 + C3H7-2 <=> C3H7O2-2'}, {'dA': 0.18174515703963448, 'dE0': 0.0, 'dn': -7570.044850406289, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'O2 + C4H9 <=> C4H9O2'}, {'dA': 0.19679733400759183, 'dE0': 0.0, 'dn': -1275.1606832785828, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'O2 + C2H3O <=> C2H3O3'}]
""",
)

entry(
    index = 92,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O",
    kinetics = ArrheniusBM(A=(4.52905e+07,'m^3/(mol*s)'), n=-0.17, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.93790333559e-10, var=0.843006791659, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O
        Total Standard Deviation in ln(k): 1.84065555863"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O
Total Standard Deviation in ln(k): 1.84065555863""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O
Total Standard Deviation in ln(k): 1.84065555863
sensitivities = [{'dA': 0.19985223858400827, 'dE0': 0.0, 'dn': -3.935794789930892e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH3 + C2H3O <=> C3H6O'}, {'dA': 0.20017724325784841, 'dE0': 0.0, 'dn': 0.00022760270957341224, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + C2H3O <=> C4H8O'}, {'dA': 0.19982043707857924, 'dE0': 0.0, 'dn': -6.548678612178642e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C3H7-2 + C2H3O <=> C5H10O'}, {'dA': 0.19996874148733282, 'dE0': 0.0, 'dn': 5.63604938892559e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CHO + C2H3O <=> C3H4O2'}, {'dA': 0.19998144963297976, 'dE0': 0.0, 'dn': 6.676533104255462e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H3O + C2H3O <=> C4H6O2'}]
""",
)

entry(
    index = 93,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2CNO_Sp-5R!H-=4R!H",
    kinetics = ArrheniusBM(A=(2.13385e+08,'m^3/(mol*s)'), n=-0.687855, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2CNO_Sp-5R!H-=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2CNO_Sp-5R!H-=4R!H
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2CNO_Sp-5R!H-=4R!H
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2CNO_Sp-5R!H-=4R!H
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C=C1[CH]Cc2ccccc21 + [H] <=> C10H10-4'}]
""",
)

entry(
    index = 94,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.67503e+10,'m^3/(mol*s)'), n=-0.732092, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing_Ext-4R!H-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C4H5-2 + H <=> C4H6-3'}]
""",
)

entry(
    index = 95,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN",
    kinetics = ArrheniusBM(A=(7.82867e+07,'m^3/(mol*s)'), n=0.0631113, w0=(205250,'J/mol'), E0=(20525,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0175378549852, var=0.221368827459, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN
        Total Standard Deviation in ln(k): 0.987289785558"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN
Total Standard Deviation in ln(k): 0.987289785558""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN
Total Standard Deviation in ln(k): 0.987289785558
sensitivities = [{'dA': 0.23249621282775199, 'dE0': 0.0, 'dn': 0.000339245012911635, 'dA_dEa': 0.0005059502647953298, 'dE0_dEa': 0.0, 'dn_dEa': -0.0005081068876445683, 'name': 'C6H7-3 + H <=> C6H8-4'}, {'dA': 0.23282818007788542, 'dE0': 0.0, 'dn': -7.534595657444325e-05, 'dA_dEa': -0.008580845829443242, 'dE0_dEa': 0.0, 'dn_dEa': 0.009602804998849798, 'name': 'C6H7-5 + H <=> C6H8-6'}, {'dA': 0.0837490969587499, 'dE0': 0.0, 'dn': 5.912731275630083e-05, 'dA_dEa': 0.26191947059931, 'dE0_dEa': 0.0, 'dn_dEa': -0.2914690801142243, 'name': 'C6H7-6 + H <=> C6H8-7'}, {'dA': 0.0022741094802827553, 'dE0': 0.0, 'dn': 0.0004970275701238991, 'dA_dEa': -7.175886906907971e-05, 'dE0_dEa': 0.0, 'dn_dEa': 0.00013394727495097427, 'name': 'C3H3 + H <=> C3H4'}, {'dA': 0.2327233247001715, 'dE0': 0.0, 'dn': 5.560313552804264e-05, 'dA_dEa': 0.9219020944969308, 'dE0_dEa': 0.0, 'dn_dEa': -1.026120985188145, 'name': 'C4H5-2 + H <=> C4H6-3'}, {'dA': 0.08381428149562921, 'dE0': 0.0, 'dn': -2.227621830689769e-05, 'dA_dEa': 0.014029603246258784, 'dE0_dEa': 0.0, 'dn_dEa': -0.015561251019228266, 'name': 'C7H7 + H <=> C7H8-2'}, {'dA': 0.0022741036822540315, 'dE0': 0.0, 'dn': 0.0004970348192423286, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C2H5 <=> C2H6-2'}, {'dA': 0.042730760796421394, 'dE0': 0.0, 'dn': 2.8154324946738186e-05, 'dA_dEa': -0.021141323216513738, 'dE0_dEa': 0.0, 'dn_dEa': 0.02358476245149521, 'name': 'H + C3H5 <=> C3H6-2'}, {'dA': 0.04250187499366589, 'dE0': 0.0, 'dn': 0.00031398241415077143, 'dA_dEa': -0.0009008858548044, 'dE0_dEa': 0.0, 'dn_dEa': 0.0010569259497985699, 'name': 'H + C12H25 <=> C12H26-7'}, {'dA': 0.04281677061613226, 'dE0': 0.0, 'dn': -7.927676283317192e-05, 'dA_dEa': -0.0014016215494906826, 'dE0_dEa': 0.0, 'dn_dEa': 0.001614101994219885, 'name': 'H + C10H21 <=> C10H22-6'}]
""",
)

entry(
    index = 96,
    label = "Root_1R->H_2R->S",
    kinetics = ArrheniusBM(A=(1.20053e+07,'m^3/(mol*s)'), n=0.538331, w0=(181667,'J/mol'), E0=(18166.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.2341883877, var=16.20347081, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_2R->S',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_2R->S
        Total Standard Deviation in ln(k): 13.6833060254"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_2R->S
Total Standard Deviation in ln(k): 13.6833060254""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_2R->S
Total Standard Deviation in ln(k): 13.6833060254
sensitivities = [{'dA': 0.10228960098680479, 'dE0': 0.0, 'dn': -0.00039918345680525395, 'dA_dEa': -4.932489078573898, 'dE0_dEa': 0.0, 'dn_dEa': 0.4256036370212929, 'name': '[S]S + [H] <=> HSSH'}, {'dA': 0.8858448134391049, 'dE0': 0.0, 'dn': -0.00024217352206884414, 'dA_dEa': 0.27599222425858927, 'dE0_dEa': 0.0, 'dn_dEa': -0.02381053872287834, 'name': 'SH + H <=> H2S'}, {'dA': 0.01768469269336687, 'dE0': 0.0, 'dn': 3.294359954988338e-05, 'dA_dEa': -0.03067422638914135, 'dE0_dEa': 0.0, 'dn_dEa': 0.002650329312662904, 'name': 'H + SH <=> H2S-2'}]
""",
)

entry(
    index = 97,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O",
    kinetics = ArrheniusBM(A=(37804.6,'m^3/(mol*s)'), n=0.550145, w0=(125643,'J/mol'), E0=(-16673.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0547341013006, var=4.25993866024, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O
        Total Standard Deviation in ln(k): 4.27521965564"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O
Total Standard Deviation in ln(k): 4.27521965564""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O
Total Standard Deviation in ln(k): 4.27521965564
sensitivities = [{'dA': 0.0068313096015522904, 'dE0': -0.0, 'dn': -0.00022335729413542412, 'dA_dEa': -0.0028170423469478837, 'dE0_dEa': -0.0, 'dn_dEa': 7.282739341826118e-05, 'name': '[O][O] + [CH3] <=> CH3O2'}, {'dA': 0.006833128972872558, 'dE0': -0.0, 'dn': -0.0002234269842026411, 'dA_dEa': -0.005003560174188788, 'dE0_dEa': -0.0, 'dn_dEa': 0.00014770671899645246, 'name': '[O][O] + C[CH2] <=> C2H5O2'}, {'dA': 0.006832993939554697, 'dE0': -0.0, 'dn': -0.000223421817308407, 'dA_dEa': -0.006977146377097001, 'dE0_dEa': -0.0, 'dn_dEa': 0.00021529412376870702, 'name': '[O][O] + [CH2]CC <=> C3H7O2'}, {'dA': 0.006832842341709309, 'dE0': -0.0, 'dn': -0.00022341600166492172, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': '1-hydroxybutyl + O2 <=> 1-hydroxybutylO2'}, {'dA': 0.09276854217611286, 'dE0': -0.0, 'dn': -0.0002189779751367955, 'dA_dEa': -0.9462809578356589, 'dE0_dEa': -0.0, 'dn_dEa': 0.032382648310777945, 'name': '[SH] + [O][O] <=> HSOO'}, {'dA': 0.03717728829500243, 'dE0': -0.0, 'dn': -0.00022362303578635868, 'dA_dEa': 0.03034484831055174, 'dE0_dEa': -0.0, 'dn_dEa': -0.0010627681437890245, 'name': 'OH + NO2-2 <=> HOONO'}, {'dA': 0.03726221949485319, 'dE0': -0.0, 'dn': -0.00022687450470065644, 'dA_dEa': 0.13627079813717638, 'dE0_dEa': -0.0, 'dn_dEa': -0.004690181290027464, 'name': 'C3H3 + O2 <=> C3H3O2'}, {'dA': 0.037041919787487915, 'dE0': -0.0, 'dn': -0.00021844535200155852, 'dA_dEa': -0.23814240260480582, 'dE0_dEa': -0.0, 'dn_dEa': 0.008132000083283606, 'name': 'C3H3-2 + O2 <=> C3H3O2-2'}, {'dA': 0.006833571848830686, 'dE0': -0.0, 'dn': -0.00022344393723789654, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + OH <=> CH4O'}, {'dA': 0.006833635495696242, 'dE0': -0.0, 'dn': -0.0002234465147572934, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + CH3O <=> C2H6O'}, {'dA': 0.006839069783382754, 'dE0': -0.0, 'dn': -0.0002236546856565724, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + OH <=> C2H6O-2'}, {'dA': 0.006833157950581679, 'dE0': -0.0, 'dn': -0.00022342805278114587, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H7-2 + CH3O <=> C4H10O'}, {'dA': 0.006832676714197603, 'dE0': -0.0, 'dn': -0.00022340966438206113, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C4H9 + CH3O <=> C5H12O'}, {'dA': 0.006832716389127611, 'dE0': -0.0, 'dn': -0.00022341108055718803, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'OH + OH <=> H2O2'}, {'dA': 0.006833375969962006, 'dE0': -0.0, 'dn': -0.00022343644802178564, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3O + CH3O <=> C2H6O2'}, {'dA': 0.006833526279948685, 'dE0': -0.0, 'dn': -0.00022344220218809056, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'OH + CH3O <=> CH4O2'}, {'dA': 0.006833037609511237, 'dE0': -0.0, 'dn': -0.00022342346435906812, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + CH3 <=> CH3O2-2'}, {'dA': 0.006833141563689835, 'dE0': -0.0, 'dn': -0.00022342744656481467, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + C2H5 <=> C2H5O2-2'}, {'dA': 0.006835532039063039, 'dE0': -0.0, 'dn': -0.00022351910659631181, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + C3H7-2 <=> C3H7O2-2'}, {'dA': 0.006833461874578759, 'dE0': -0.0, 'dn': -0.00022343978844487991, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + C4H9 <=> C4H9O2'}, {'dA': 0.006832849688721197, 'dE0': -0.0, 'dn': -0.0002234162781289018, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + C2H3 <=> C2H3O2'}, {'dA': 0.02181442661886264, 'dE0': -0.0, 'dn': -0.00022310803374655177, 'dA_dEa': -0.01419213981002244, 'dE0_dEa': -0.0, 'dn_dEa': 0.0004623971439390767, 'name': 'O2 + C6H5 <=> C6H5O2'}, {'dA': 0.0068334036811287, 'dE0': -0.0, 'dn': -0.0002234375442222442, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + CHO <=> CHO3'}, {'dA': 0.006833201995349512, 'dE0': -0.0, 'dn': -0.00022342976265341872, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + C2H3O <=> C2H3O3'}, {'dA': 0.20170421464806854, 'dE0': -0.0, 'dn': -0.0002236469235208914, 'dA_dEa': 0.48947103658042285, 'dE0_dEa': -0.0, 'dn_dEa': -0.016785855165079105, 'name': 'O2 + C6H5 <=> C6H5O2'}, {'dA': 0.20176324933987025, 'dE0': -0.0, 'dn': -0.00022590480215727233, 'dA_dEa': 0.8070768558266829, 'dE0_dEa': -0.0, 'dn_dEa': -0.027662539565254423, 'name': 'O2 + C10H7 <=> C10H7O2'}, {'dA': 0.20172220051331013, 'dE0': -0.0, 'dn': -0.00022433930262588935, 'dA_dEa': 0.5464793174763718, 'dE0_dEa': -0.0, 'dn_dEa': -0.018738625116471543, 'name': 'O2 + C10H7-2 <=> C10H7O2-2'}, {'dA': 0.20017771190519157, 'dE0': -0.0, 'dn': -0.00016508947008712902, 'dA_dEa': 0.8252216037743864, 'dE0_dEa': -0.0, 'dn_dEa': -0.028281112185637516, 'name': 'O2 + C7H7 <=> C7H7O2'}]
""",
)

entry(
    index = 98,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.63105e+07,'m^3/(mol*s)'), n=-0.118135, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00652285405283, var=0.794920323305, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R
        Total Standard Deviation in ln(k): 1.80377688208"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R
Total Standard Deviation in ln(k): 1.80377688208""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R
Total Standard Deviation in ln(k): 1.80377688208
sensitivities = [{'dA': 0.4997412943908425, 'dE0': 0.0, 'dn': -1.3055830199457919e-05, 'dA_dEa': 0.5085809720598028, 'dE0_dEa': 0.0, 'dn_dEa': 0.6668890157252011, 'name': 'C3H5 + C3H5 <=> C6H10-2'}, {'dA': 0.5000378619791075, 'dE0': 0.0, 'dn': 0.0004232756959867572, 'dA_dEa': 0.2547042490661791, 'dE0_dEa': 0.0, 'dn_dEa': 0.3340532207086973, 'name': 'C3H5 + C2H5 <=> C5H10-2'}]
""",
)

entry(
    index = 99,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_N-Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(3.45106e-07,'m^3/(mol*s)'), n=3.72998, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_N-Sp-4R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_N-Sp-4R!H-2R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H3-2 + O2 <=> C3H3O2-2'}]
""",
)

entry(
    index = 100,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_2R->C",
    kinetics = ArrheniusBM(A=(3.7586e+07,'m^3/(mol*s)'), n=-0.395795, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00722098163323, var=0.0433403113763, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_2R->C
        Total Standard Deviation in ln(k): 0.435495654232"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_2R->C
Total Standard Deviation in ln(k): 0.435495654232""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_2R->C
Total Standard Deviation in ln(k): 0.435495654232
sensitivities = [{'dA': 0.4997097071726681, 'dE0': 0.0, 'dn': 2.00128363709367e-05, 'dA_dEa': -5.41987676095583, 'dE0_dEa': 0.0, 'dn_dEa': 2.384372195908453, 'name': '[O][O] + C[CH2] <=> C2H5O2'}, {'dA': 0.4995663517651234, 'dE0': 0.0, 'dn': 9.077812623207916e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'O2 + C2H5 <=> C2H5O2-2'}]
""",
)

entry(
    index = 101,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O",
    kinetics = ArrheniusBM(A=(7.88213e+06,'m^3/(mol*s)'), n=0.314663, w0=(193067,'J/mol'), E0=(19306.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.379272271586, var=0.88677526262, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O
        Total Standard Deviation in ln(k): 2.84077927867"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O
Total Standard Deviation in ln(k): 2.84077927867""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O
Total Standard Deviation in ln(k): 2.84077927867
sensitivities = [{'dA': 0.06659023761380234, 'dE0': 0.0, 'dn': -1.1374715725069492e-05, 'dA_dEa': 0.00028406463137290247, 'dE0_dEa': 0.0, 'dn_dEa': -0.0001057034410080372, 'name': 'C6H7-3 + H <=> C6H8-4'}, {'dA': 0.06659258268016566, 'dE0': 0.0, 'dn': -1.2347655994322899e-05, 'dA_dEa': -0.0023198001457560903, 'dE0_dEa': 0.0, 'dn_dEa': 0.0008536084068430891, 'name': 'C6H7-5 + H <=> C6H8-6'}, {'dA': 0.023976375334913567, 'dE0': 0.0, 'dn': -5.687618378611385e-06, 'dA_dEa': 0.07502635491719305, 'dE0_dEa': 0.0, 'dn_dEa': -0.027642614772848545, 'name': 'C6H7-6 + H <=> C6H8-7'}, {'dA': 0.0007876978429522709, 'dE0': 0.0, 'dn': -9.733892280315388e-06, 'dA_dEa': 0.00011694234203220199, 'dE0_dEa': 0.0, 'dn_dEa': -4.41327833259438e-05, 'name': 'C3H3 + H <=> C3H4'}, {'dA': 0.06662372300603915, 'dE0': 0.0, 'dn': -2.5239579053055183e-05, 'dA_dEa': 0.2636124900093086, 'dE0_dEa': 0.0, 'dn_dEa': -0.09712410333706017, 'name': 'C4H5-2 + H <=> C4H6-3'}, {'dA': 0.023987101871017356, 'dE0': 0.0, 'dn': -1.0121985956045572e-05, 'dA_dEa': 0.004148563462536461, 'dE0_dEa': 0.0, 'dn_dEa': -0.0015294705109501828, 'name': 'C7H7 + H <=> C7H8-2'}, {'dA': 0.0007877330769901804, 'dE0': 0.0, 'dn': -9.748461292629104e-06, 'dA_dEa': 2.360543582824708e-05, 'dE0_dEa': 0.0, 'dn_dEa': -9.742337439011797e-06, 'name': 'H + C2H5 <=> C2H6-2'}, {'dA': 0.0007883333452697075, 'dE0': 0.0, 'dn': -9.996686270081695e-06, 'dA_dEa': 2.360543582824708e-05, 'dE0_dEa': 0.0, 'dn_dEa': -9.742337439011797e-06, 'name': 'H + C3H7-2 <=> C3H8-2'}, {'dA': 0.0007876740255597682, 'dE0': 0.0, 'dn': -9.724060058419762e-06, 'dA_dEa': 2.360543582824708e-05, 'dE0_dEa': 0.0, 'dn_dEa': -9.742337439011797e-06, 'name': 'H + C2H <=> C2H2'}, {'dA': 0.5990649212961989, 'dE0': 0.0, 'dn': -1.782579199861917e-07, 'dA_dEa': 0.8673196288136853, 'dE0_dEa': 0.0, 'dn_dEa': -0.3195465337795672, 'name': 'CH3S-2 + H <=> CH4S'}, {'dA': 0.012249382313812802, 'dE0': 0.0, 'dn': -9.730632459906561e-06, 'dA_dEa': -0.005908698648582995, 'dE0_dEa': 0.0, 'dn_dEa': 0.002175908799691594, 'name': 'H + C3H5 <=> C3H6-2'}, {'dA': 0.0007877164929227277, 'dE0': 0.0, 'dn': -9.74160684345302e-06, 'dA_dEa': -0.00034716356900336634, 'dE0_dEa': 0.0, 'dn_dEa': 0.00012686085854946935, 'name': 'H + C4H7 <=> C4H8'}, {'dA': 0.0007877164929227277, 'dE0': 0.0, 'dn': -9.74160684345302e-06, 'dA_dEa': -0.00034716356900336634, 'dE0_dEa': 0.0, 'dn_dEa': 0.00012686085854946935, 'name': 'H + C5H9 <=> C5H10'}, {'dA': 0.0007877164929227277, 'dE0': 0.0, 'dn': -9.74160684345302e-06, 'dA_dEa': -0.00034716356900336634, 'dE0_dEa': 0.0, 'dn_dEa': 0.00012686085854946935, 'name': 'H + C6H9 <=> C6H10'}, {'dA': 0.0007883333452697075, 'dE0': 0.0, 'dn': -9.996686270081695e-06, 'dA_dEa': 2.360543582824708e-05, 'dE0_dEa': 0.0, 'dn_dEa': -9.742337439011797e-06, 'name': 'H + C5H7 <=> C5H8'}, {'dA': 0.012249525227049602, 'dE0': 0.0, 'dn': -9.78970764428106e-06, 'dA_dEa': -0.00011980329084339202, 'dE0_dEa': 0.0, 'dn_dEa': 4.3088985313659756e-05, 'name': 'H + C12H25 <=> C12H26-7'}, {'dA': 0.012249800718679111, 'dE0': 0.0, 'dn': -9.903713095414479e-06, 'dA_dEa': 0.00040599373996035335, 'dE0_dEa': 0.0, 'dn_dEa': -0.0001506112420750935, 'name': 'H + C12H25-2 <=> C12H26-8'}, {'dA': 0.012249800718679111, 'dE0': 0.0, 'dn': -9.903713095414479e-06, 'dA_dEa': 0.00040599373996035335, 'dE0_dEa': 0.0, 'dn_dEa': -0.0001506112420750935, 'name': 'H + C12H25-3 <=> C12H26-9'}, {'dA': 0.012249800718679111, 'dE0': 0.0, 'dn': -9.903713095414479e-06, 'dA_dEa': 0.00040599373996035335, 'dE0_dEa': 0.0, 'dn_dEa': -0.0001506112420750935, 'name': 'H + C12H25-4 <=> C12H26-10'}, {'dA': 0.012249800718679111, 'dE0': 0.0, 'dn': -9.903713095414479e-06, 'dA_dEa': 0.00040599373996035335, 'dE0_dEa': 0.0, 'dn_dEa': -0.0001506112420750935, 'name': 'H + C12H25-5 <=> C12H26-11'}, {'dA': 0.012249800716902754, 'dE0': 0.0, 'dn': -9.903713095414479e-06, 'dA_dEa': 0.00040599373996035335, 'dE0_dEa': 0.0, 'dn_dEa': -0.0001506112420750935, 'name': 'H + C12H25-6 <=> C12H26-12'}, {'dA': 0.012249345843430532, 'dE0': 0.0, 'dn': -9.715741459583926e-06, 'dA_dEa': -0.00026300394040393424, 'dE0_dEa': 0.0, 'dn_dEa': 9.583380473035478e-05, 'name': 'H + C10H21 <=> C10H22-6'}, {'dA': 0.012249345843430532, 'dE0': 0.0, 'dn': -9.715741459583926e-06, 'dA_dEa': -0.00026300394040393424, 'dE0_dEa': 0.0, 'dn_dEa': 9.583380473035478e-05, 'name': 'H + C10H21-2 <=> C10H22-7'}, {'dA': 0.012249345841654175, 'dE0': 0.0, 'dn': -9.715740966493562e-06, 'dA_dEa': -0.00026300394040393424, 'dE0_dEa': 0.0, 'dn_dEa': 9.583380473035478e-05, 'name': 'H + C10H21-3 <=> C10H22-8'}, {'dA': 0.012249345841654175, 'dE0': 0.0, 'dn': -9.715740802130105e-06, 'dA_dEa': -0.00026300394040393424, 'dE0_dEa': 0.0, 'dn_dEa': 9.583380473035478e-05, 'name': 'H + C10H21-4 <=> C10H22-9'}, {'dA': 0.012249345841654175, 'dE0': 0.0, 'dn': -9.715740802130105e-06, 'dA_dEa': -0.00026300394040393424, 'dE0_dEa': 0.0, 'dn_dEa': 9.583380473035478e-05, 'name': 'H + C10H21-5 <=> C10H22-10'}]
""",
)

entry(
    index = 102,
    label = "Root_1R->H_N-2R->S",
    kinetics = ArrheniusBM(A=(4.98692e+07,'m^3/(mol*s)'), n=0.0447198, w0=(191462,'J/mol'), E0=(19146.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0663544083182, var=2.30770893713, Tref=1000.0, N=40, data_mean=0.0, correlation='Root_1R->H_N-2R->S',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S
        Total Standard Deviation in ln(k): 3.2121417918"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S
Total Standard Deviation in ln(k): 3.2121417918""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S
Total Standard Deviation in ln(k): 3.2121417918
sensitivities = [{'dA': 0.032452628381921776, 'dE0': 0.0, 'dn': -0.00046113248065243637, 'dA_dEa': 0.0032632009165926277, 'dE0_dEa': 0.0, 'dn_dEa': -0.0025104249584113674, 'name': 'C6H7 + H <=> C6H8-2'}, {'dA': 0.03247772094994519, 'dE0': 0.0, 'dn': -0.00048203746146842575, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H7-2 + H <=> C6H8-3'}, {'dA': 0.03246711277072125, 'dE0': 0.0, 'dn': -0.0004732034867808341, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H7-3 + H <=> C6H8-4'}, {'dA': 0.03246751475672129, 'dE0': 0.0, 'dn': -0.00047353831386449117, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H7-4 + H <=> C6H8-5'}, {'dA': 0.03246835412796047, 'dE0': 0.0, 'dn': -0.00047423760716229214, 'dA_dEa': -0.0006025540564281282, 'dE0_dEa': 0.0, 'dn_dEa': 0.0003587466209312668, 'name': 'C6H7-5 + H <=> C6H8-6'}, {'dA': 0.012016710208230466, 'dE0': 0.0, 'dn': -0.0004704513944663099, 'dA_dEa': 0.036518739033657016, 'dE0_dEa': 0.0, 'dn_dEa': -0.02720050258264004, 'name': 'C6H7-6 + H <=> C6H8-7'}, {'dA': 0.03246543709068208, 'dE0': 0.0, 'dn': -0.00047180722678096237, 'dA_dEa': 0.03727281777444047, 'dE0_dEa': 0.0, 'dn_dEa': -0.027760716913139492, 'name': 'H + NJCO <=> HNCO'}, {'dA': 0.032425605684952806, 'dE0': 0.0, 'dn': -0.0004386198041358763, 'dA_dEa': 0.0372312710759145, 'dE0_dEa': 0.0, 'dn_dEa': -0.027726098971293748, 'name': 'H + NCOJ <=> NCOH'}, {'dA': 0.01146786721761954, 'dE0': 0.0, 'dn': -1.3231698351992414e-05, 'dA_dEa': 0.6457396612376699, 'dE0_dEa': 0.0, 'dn_dEa': -0.4795173681648392, 'name': '[CH2]c1ccccc1[C]=C=C + [H] <=> C10H9'}, {'dA': 0.011615459488468928, 'dE0': 0.0, 'dn': -0.00013618932828360106, 'dA_dEa': 0.23858546352076146, 'dE0_dEa': 0.0, 'dn_dEa': -0.17724828453389083, 'name': 'C=C1[CH]c2ccccc2C1 + [H] <=> C10H10-3'}, {'dA': 0.01203535531146959, 'dE0': 0.0, 'dn': -0.00048598494820281955, 'dA_dEa': -0.06131793085373936, 'dE0_dEa': 0.0, 'dn_dEa': 0.04543485814022645, 'name': 'C=C1[CH]Cc2ccccc21 + [H] <=> C10H10-4'}, {'dA': 0.01211869502171359, 'dE0': 0.0, 'dn': -0.0005554199498364244, 'dA_dEa': -0.0009766821200686247, 'dE0_dEa': 0.0, 'dn_dEa': 0.0006298758402790403, 'name': 'C=C1C[CH]c2ccccc21 + [H] <=> C10H10-5'}, {'dA': 0.012009625653065726, 'dE0': 0.0, 'dn': -0.0004645464196493506, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C9H7 + H <=> C9H8-3'}, {'dA': 0.0008859927724814563, 'dE0': 0.0, 'dn': -0.00047380036449052194, 'dA_dEa': 0.0005640413434094337, 'dE0_dEa': 0.0, 'dn_dEa': -0.000507067971802601, 'name': 'C3H3 + H <=> C3H4'}, {'dA': 0.00088599695757817, 'dE0': 0.0, 'dn': -0.00047380384519299585, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H3-2 + H <=> C3H4-2'}, {'dA': 0.032465002355767346, 'dE0': 0.0, 'dn': -0.00047144317358765634, 'dA_dEa': -0.12486559701942167, 'dE0_dEa': 0.0, 'dn_dEa': 0.09261528968317995, 'name': 'C4H5 + H <=> C4H6-2'}, {'dA': 0.032465504890669926, 'dE0': 0.0, 'dn': -0.00047186304735866673, 'dA_dEa': 0.12703534037329667, 'dE0_dEa': 0.0, 'dn_dEa': -0.09440333500567408, 'name': 'C4H5-2 + H <=> C4H6-3'}, {'dA': 0.012020820165049786, 'dE0': 0.0, 'dn': -0.0004738758499276453, 'dA_dEa': 0.0024998428855840782, 'dE0_dEa': 0.0, 'dn_dEa': -0.0019442974698504953, 'name': 'C7H7 + H <=> C7H8-2'}, {'dA': 0.012016095645607452, 'dE0': 0.0, 'dn': -0.00046993642339260955, 'dA_dEa': 0.020151220439859063, 'dE0_dEa': 0.0, 'dn_dEa': -0.015050063229809979, 'name': 'C7H7-2 + H <=> C7H8-3'}, {'dA': 0.01201871788936292, 'dE0': 0.0, 'dn': -0.00047212443059336764, 'dA_dEa': 0.015504107313548163, 'dE0_dEa': 0.0, 'dn_dEa': -0.011598854473703136, 'name': 'C7H7-3 + H <=> C7H8-4'}, {'dA': 0.0008837813325613816, 'dE0': 0.0, 'dn': -0.00047195782288930857, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + H <=> H2'}, {'dA': 0.0008647238765036988, 'dE0': 0.0, 'dn': -0.0004560842451938761, 'dA_dEa': -0.0016487963634405783, 'dE0_dEa': 0.0, 'dn_dEa': 0.0011372023250368066, 'name': 'H + H <=> H2'}, {'dA': 0.00638869865810036, 'dE0': 0.0, 'dn': -0.00047492809851240586, 'dA_dEa': -0.005681586177531187, 'dE0_dEa': 0.0, 'dn_dEa': 0.0041299809663554645, 'name': 'H + CH3 <=> CH4'}, {'dA': 0.0008859950959562023, 'dE0': 0.0, 'dn': -0.00047380229826932043, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C2H5 <=> C2H6-2'}, {'dA': 0.0008862154530221299, 'dE0': 0.0, 'dn': -0.00047398588288523677, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C3H7-2 <=> C3H8-2'}, {'dA': 0.006387212199144436, 'dE0': 0.0, 'dn': -0.0004736898039128866, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C2H3 <=> C2H4'}, {'dA': 0.000885911955350691, 'dE0': 0.0, 'dn': -0.00047373303629774904, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C2H <=> C2H2'}, {'dA': 0.006386259336466786, 'dE0': 0.0, 'dn': -0.00047289501701774255, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C6H5 <=> C6H6-4'}, {'dA': 0.0008832493456624042, 'dE0': 0.0, 'dn': -0.0004715130993072302, 'dA_dEa': 0.007020612862619009, 'dE0_dEa': 0.0, 'dn_dEa': -0.005300647652955033, 'name': 'H + CHO <=> CH2O'}, {'dA': 0.006386652021462417, 'dE0': 0.0, 'dn': -0.00047322348450788904, 'dA_dEa': -0.002924571486318295, 'dE0_dEa': 0.0, 'dn_dEa': 0.0020829441714310098, 'name': 'H + OH <=> H2O'}, {'dA': 0.0008860528701860469, 'dE0': 0.0, 'dn': -0.000473850438381741, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + CH3 <=> CH4'}, {'dA': 0.0008858626472375429, 'dE0': 0.0, 'dn': -0.00047369195910662505, 'dA_dEa': -0.0001266395983634678, 'dE0_dEa': 0.0, 'dn_dEa': 5.723989218296174e-06, 'name': 'O2 + H <=> HO2-2'}, {'dA': 0.28741209284536107, 'dE0': 0.0, 'dn': 6.330367367768184e-05, 'dA_dEa': 0.41681919157459263, 'dE0_dEa': 0.0, 'dn_dEa': -0.3095477100065688, 'name': 'CH3S-2 + H <=> CH4S'}, {'dA': 0.0063873508509011785, 'dE0': 0.0, 'dn': -0.00047380530219272776, 'dA_dEa': -0.0023276169542898804, 'dE0_dEa': 0.0, 'dn_dEa': 0.0016397520979443878, 'name': 'H + C3H5 <=> C3H6-2'}, {'dA': 0.0008859981939225302, 'dE0': 0.0, 'dn': -0.0004738048772482731, 'dA_dEa': 0.00034131271320351635, 'dE0_dEa': 0.0, 'dn_dEa': -0.0003417075469539056, 'name': 'H + C4H7 <=> C4H8'}, {'dA': 0.0008859981939225302, 'dE0': 0.0, 'dn': -0.0004738048772482731, 'dA_dEa': 0.00034131271320351635, 'dE0_dEa': 0.0, 'dn_dEa': -0.0003417075469539056, 'name': 'H + C5H9 <=> C5H10'}, {'dA': 0.0008859981939225302, 'dE0': 0.0, 'dn': -0.0004738048772482731, 'dA_dEa': 0.00034131271320351635, 'dE0_dEa': 0.0, 'dn_dEa': -0.0003417075469539056, 'name': 'H + C6H9 <=> C6H10'}, {'dA': 0.0008837813290086679, 'dE0': 0.0, 'dn': -0.00047195781990840436, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H3-2 + H <=> C3H4-2'}, {'dA': 0.006389529566775558, 'dE0': 0.0, 'dn': -0.0004756190775715683, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C5H5 + H <=> C5H6'}, {'dA': 0.0008862154530221299, 'dE0': 0.0, 'dn': -0.00047398588305084253, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C5H7 <=> C5H8'}, {'dA': 0.07228948883409544, 'dE0': 0.0, 'dn': -0.0003787400483631386, 'dA_dEa': 0.044831258605886826, 'dE0_dEa': 0.0, 'dn_dEa': -0.03336052968429821, 'name': 'H + C12H9 <=> C12H10-2'}, {'dA': 0.07240362826977619, 'dE0': 0.0, 'dn': -0.0004738478961672735, 'dA_dEa': 0.04411824071227019, 'dE0_dEa': 0.0, 'dn_dEa': -0.032843046335007356, 'name': 'H + C12H9-2 <=> C12H10-3'}, {'dA': 0.0724037950163927, 'dE0': 0.0, 'dn': -0.0004739872411839184, 'dA_dEa': -0.003703352451367844, 'dE0_dEa': 0.0, 'dn_dEa': 0.0026614819951973115, 'name': 'H + C12H9-3 <=> C12H10-4'}, {'dA': 0.00638668986141581, 'dE0': 0.0, 'dn': -0.00047325463445998926, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C12H25 <=> C12H26-7'}, {'dA': 0.006387523551865819, 'dE0': 0.0, 'dn': -0.00047394918911374277, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C12H25-2 <=> C12H26-8'}, {'dA': 0.006387523551865819, 'dE0': 0.0, 'dn': -0.00047394918911374277, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C12H25-3 <=> C12H26-9'}, {'dA': 0.006387523551865819, 'dE0': 0.0, 'dn': -0.00047394918911374277, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C12H25-4 <=> C12H26-10'}, {'dA': 0.006387523551865819, 'dE0': 0.0, 'dn': -0.00047394918911374277, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C12H25-5 <=> C12H26-11'}, {'dA': 0.006387523551865819, 'dE0': 0.0, 'dn': -0.00047394918911374277, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C12H25-6 <=> C12H26-12'}, {'dA': 0.006389043939237375, 'dE0': 0.0, 'dn': -0.0004752155709518999, 'dA_dEa': 0.00038163680571305685, 'dE0_dEa': 0.0, 'dn_dEa': -0.00037165806484661416, 'name': 'H + C10H21 <=> C10H22-6'}, {'dA': 0.006389043939237375, 'dE0': 0.0, 'dn': -0.0004752155709518999, 'dA_dEa': 0.00038163680571305685, 'dE0_dEa': 0.0, 'dn_dEa': -0.00037165806468100835, 'name': 'H + C10H21-2 <=> C10H22-7'}, {'dA': 0.006389043939237375, 'dE0': 0.0, 'dn': -0.0004752155709518999, 'dA_dEa': 0.00038163680571305685, 'dE0_dEa': 0.0, 'dn_dEa': -0.00037165806468100835, 'name': 'H + C10H21-3 <=> C10H22-8'}, {'dA': 0.006389043939237375, 'dE0': 0.0, 'dn': -0.0004752155709518999, 'dA_dEa': 0.00038163680571305685, 'dE0_dEa': 0.0, 'dn_dEa': -0.00037165806468100835, 'name': 'H + C10H21-4 <=> C10H22-9'}, {'dA': 0.006389043939237375, 'dE0': 0.0, 'dn': -0.0004752155709518999, 'dA_dEa': 0.00038163680571305685, 'dE0_dEa': 0.0, 'dn_dEa': -0.00037165806484661416, 'name': 'H + C10H21-5 <=> C10H22-10'}]
""",
)

entry(
    index = 103,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(1.57643e+07,'m^3/(mol*s)'), n=-0.222444, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0398748526415, var=2.83447135176, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H
        Total Standard Deviation in ln(k): 3.47533765731"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 3.47533765731""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 3.47533765731
sensitivities = [{'dA': 0.11171115465559277, 'dE0': 0.0, 'dn': -0.26510788056936135, 'dA_dEa': 1.8594400023206163, 'dE0_dEa': 0.0, 'dn_dEa': -19.13381665661524, 'name': 'C=C1[CH]c2ccccc2C1 + [H] <=> C10H10-3'}, {'dA': 0.12467543421480749, 'dE0': 0.0, 'dn': -0.4145586206388914, 'dA_dEa': -0.4419056317886348, 'dE0_dEa': 0.0, 'dn_dEa': 4.493641153334641, 'name': 'C=C1[CH]Cc2ccccc21 + [H] <=> C10H10-4'}, {'dA': 0.1222418642825708, 'dE0': 0.0, 'dn': -0.3865051974054822, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C=C1C[CH]c2ccccc21 + [H] <=> C10H10-5'}, {'dA': 0.12340003212331334, 'dE0': 0.0, 'dn': -0.3998565384695309, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C9H7 + H <=> C9H8-3'}, {'dA': 0.12602476799729312, 'dE0': 0.0, 'dn': -0.4301134508690887, 'dA_dEa': 0.18730676716673786, 'dE0_dEa': 0.0, 'dn_dEa': -1.9706876172127794, 'name': 'C7H7-2 + H <=> C7H8-3'}, {'dA': 0.526987608893195, 'dE0': 0.0, 'dn': 0.32461821215057785, 'dA_dEa': 0.39137181208208505, 'dE0_dEa': 0.0, 'dn_dEa': -4.082708206086258, 'name': 'H + C12H9 <=> C12H10-2'}]
""",
)

entry(
    index = 104,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO",
    kinetics = ArrheniusBM(A=(7.27792e+06,'m^3/(mol*s)'), n=0.315465, w0=(187235,'J/mol'), E0=(18723.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.200606974831, var=0.612647101718, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO
        Total Standard Deviation in ln(k): 2.07317938705"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO
Total Standard Deviation in ln(k): 2.07317938705""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO
Total Standard Deviation in ln(k): 2.07317938705
sensitivities = [{'dA': 0.06222370098286209, 'dE0': 0.0, 'dn': 5.693540653956268e-05, 'dA_dEa': 0.00035390235986202957, 'dE0_dEa': 0.0, 'dn_dEa': -0.00013476411515103947, 'name': 'C6H7-3 + H <=> C6H8-4'}, {'dA': 0.06246099808216576, 'dE0': 0.0, 'dn': -4.075309453687674e-05, 'dA_dEa': -0.0020927972208542116, 'dE0_dEa': 0.0, 'dn_dEa': 0.0007632672836661414, 'name': 'C6H7-5 + H <=> C6H8-6'}, {'dA': 0.022553943425765152, 'dE0': 0.0, 'dn': -4.265313666971513e-05, 'dA_dEa': 0.07038361839129757, 'dE0_dEa': 0.0, 'dn_dEa': -0.025829751727495437, 'name': 'C6H7-6 + H <=> C6H8-7'}, {'dA': 0.06245713418807219, 'dE0': 0.0, 'dn': -3.9169256633083935e-05, 'dA_dEa': 0.071833296814824, 'dE0_dEa': 0.0, 'dn_dEa': -0.026361023550036732, 'name': 'H + NCOJ <=> NCOH'}, {'dA': 0.0008265148885301188, 'dE0': 0.0, 'dn': -4.553436869057528e-05, 'dA_dEa': 0.00019807844608978848, 'dE0_dEa': 0.0, 'dn_dEa': -7.762516146622674e-05, 'name': 'C3H3 + H <=> C3H4'}, {'dA': 0.06245873784217059, 'dE0': 0.0, 'dn': -3.9825691511381725e-05, 'dA_dEa': 0.2470511162542538, 'dE0_dEa': 0.0, 'dn_dEa': -0.09065211493763654, 'name': 'C4H5-2 + H <=> C4H6-3'}, {'dA': 0.02256128684763574, 'dE0': 0.0, 'dn': -4.56777315200796e-05, 'dA_dEa': 0.0039764070187691064, 'dE0_dEa': 0.0, 'dn_dEa': -0.0014639823932931296, 'name': 'C7H7 + H <=> C7H8-2'}, {'dA': 0.0008265693214327486, 'dE0': 0.0, 'dn': -4.5556778355531695e-05, 'dA_dEa': 0.00011069739969117419, 'dE0_dEa': 0.0, 'dn_dEa': -4.556427105117036e-05, 'name': 'H + C2H5 <=> C2H6-2'}, {'dA': 0.0008255026795468211, 'dE0': 0.0, 'dn': -4.511742212896505e-05, 'dA_dEa': 0.00011069739969117419, 'dE0_dEa': 0.0, 'dn_dEa': -4.556427105117036e-05, 'name': 'H + C3H7-2 <=> C3H8-2'}, {'dA': 0.00082626586284116, 'dE0': 0.0, 'dn': -4.54318084291042e-05, 'dA_dEa': 0.00011069739969117419, 'dE0_dEa': 0.0, 'dn_dEa': -4.556427105117036e-05, 'name': 'H + C2H <=> C2H2'}, {'dA': 0.0008266787041578483, 'dE0': 0.0, 'dn': -4.5601824721946727e-05, 'dA_dEa': -0.0011498734320271198, 'dE0_dEa': 0.0, 'dn_dEa': 0.00041696231977679597, 'name': 'O2 + H <=> HO2-2'}, {'dA': 0.5613420804966914, 'dE0': 0.0, 'dn': -3.468095467044863e-05, 'dA_dEa': 0.8126835304179465, 'dE0_dEa': 0.0, 'dn_dEa': -0.2981926033976088, 'name': 'CH3S-2 + H <=> CH4S'}, {'dA': 0.011565230277456203, 'dE0': 0.0, 'dn': -4.5683995566846325e-05, 'dA_dEa': -0.005446900063433336, 'dE0_dEa': 0.0, 'dn_dEa': 0.001993615093478371, 'name': 'H + C3H5 <=> C3H6-2'}, {'dA': 0.00082660570654989, 'dE0': 0.0, 'dn': -4.557175441654181e-05, 'dA_dEa': -0.00023665243986672855, 'dE0_dEa': 0.0, 'dn_dEa': 8.188443843394261e-05, 'name': 'H + C4H7 <=> C4H8'}, {'dA': 0.00082660570654989, 'dE0': 0.0, 'dn': -4.557175441654181e-05, 'dA_dEa': -0.00023665243986672855, 'dE0_dEa': 0.0, 'dn_dEa': 8.188443843394261e-05, 'name': 'H + C5H9 <=> C5H10'}, {'dA': 0.00082660570654989, 'dE0': 0.0, 'dn': -4.557175441654181e-05, 'dA_dEa': -0.00023665243986672855, 'dE0_dEa': 0.0, 'dn_dEa': 8.188443843394261e-05, 'name': 'H + C6H9 <=> C6H10'}, {'dA': 0.0008255026795468211, 'dE0': 0.0, 'dn': -4.511742212896505e-05, 'dA_dEa': 0.00011069739969117419, 'dE0_dEa': 0.0, 'dn_dEa': -4.556427105117036e-05, 'name': 'H + C5H7 <=> C5H8'}, {'dA': 0.011567408900960027, 'dE0': 0.0, 'dn': -4.658110321470103e-05, 'dA_dEa': -2.415989008852914e-05, 'dE0_dEa': 0.0, 'dn_dEa': 3.93472935182627e-06, 'name': 'H + C12H25 <=> C12H26-7'}, {'dA': 0.011565491695010473, 'dE0': 0.0, 'dn': -4.5791732489731585e-05, 'dA_dEa': 0.0004698644175960516, 'dE0_dEa': 0.0, 'dn_dEa': -0.00017737637641116155, 'name': 'H + C12H25-2 <=> C12H26-8'}, {'dA': 0.01156549169678683, 'dE0': 0.0, 'dn': -4.5791732817109386e-05, 'dA_dEa': 0.0004698644211487653, 'dE0_dEa': 0.0, 'dn_dEa': -0.00017737637772067272, 'name': 'H + C12H25-3 <=> C12H26-9'}, {'dA': 0.011565491695010473, 'dE0': 0.0, 'dn': -4.5791732489731585e-05, 'dA_dEa': 0.0004698644211487653, 'dE0_dEa': 0.0, 'dn_dEa': -0.00017737637772067272, 'name': 'H + C12H25-4 <=> C12H26-10'}, {'dA': 0.011565491695010473, 'dE0': 0.0, 'dn': -4.5791732326042685e-05, 'dA_dEa': 0.00046986441937240845, 'dE0_dEa': 0.0, 'dn_dEa': -0.00017737637772067272, 'name': 'H + C12H25-5 <=> C12H26-11'}, {'dA': 0.011565491695010473, 'dE0': 0.0, 'dn': -4.5791732489731585e-05, 'dA_dEa': 0.00046986441937240845, 'dE0_dEa': 0.0, 'dn_dEa': -0.00017737637772067272, 'name': 'H + C12H25-6 <=> C12H26-12'}, {'dA': 0.011564096237039075, 'dE0': 0.0, 'dn': -4.521697591643789e-05, 'dA_dEa': -0.00015782966222845435, 'dE0_dEa': 0.0, 'dn_dEa': 5.2945616661890655e-05, 'name': 'H + C10H21 <=> C10H22-6'}, {'dA': 0.011564096237039075, 'dE0': 0.0, 'dn': -4.521697608012679e-05, 'dA_dEa': -0.00015782966222845435, 'dE0_dEa': 0.0, 'dn_dEa': 5.2945616661890655e-05, 'name': 'H + C10H21-2 <=> C10H22-7'}, {'dA': 0.011564096237039075, 'dE0': 0.0, 'dn': -4.521697608012679e-05, 'dA_dEa': -0.00015782966222845435, 'dE0_dEa': 0.0, 'dn_dEa': 5.2945616661890655e-05, 'name': 'H + C10H21-3 <=> C10H22-8'}, {'dA': 0.011564096237039075, 'dE0': 0.0, 'dn': -4.521697608012679e-05, 'dA_dEa': -0.00015782966222845435, 'dE0_dEa': 0.0, 'dn_dEa': 5.2945616661890655e-05, 'name': 'H + C10H21-4 <=> C10H22-9'}, {'dA': 0.011564096237039075, 'dE0': 0.0, 'dn': -4.521697591643789e-05, 'dA_dEa': -0.00015782966222845435, 'dE0_dEa': 0.0, 'dn_dEa': 5.2945616661890655e-05, 'name': 'H + C10H21-5 <=> C10H22-10'}]
""",
)

entry(
    index = 105,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(6.30526e+07,'m^3/(mol*s)'), n=-0.283333, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-6.50053689359e-11, var=0.305422193575, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C
        Total Standard Deviation in ln(k): 1.10791715097"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 1.10791715097""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 1.10791715097
sensitivities = [{'dA': 0.3331522272489818, 'dE0': 0.0, 'dn': -7.190723100295984e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + C2H3O <=> C4H8O'}, {'dA': 0.3331676636655712, 'dE0': 0.0, 'dn': 4.1025163574570474e-07, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C3H7-2 + C2H3O <=> C5H10O'}, {'dA': 0.33315187341646296, 'dE0': 0.0, 'dn': -7.360988862221756e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H3O + C2H3O <=> C4H6O2'}]
""",
)

entry(
    index = 106,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_2R->C_N-3R!H->O",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=-1.37127e-07, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_2R->C_N-3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_2R->C_N-3R!H->O
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_2R->C_N-3R!H->O
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_2R->C_N-3R!H->O
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'CH3 + CH3O <=> C2H6O'}]
""",
)

entry(
    index = 107,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-3CS-R_N-2CNO->N",
    kinetics = ArrheniusBM(A=(2.1534e+07,'m^3/(mol*s)'), n=0.0505704, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00289490297729, var=9.94451676066, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-3CS-R_N-2CNO->N',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-3CS-R_N-2CNO->N
        Total Standard Deviation in ln(k): 6.32919123293"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-3CS-R_N-2CNO->N
Total Standard Deviation in ln(k): 6.32919123293""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-3CS-R_N-2CNO->N
Total Standard Deviation in ln(k): 6.32919123293
sensitivities = [{'dA': 0.4970507103401737, 'dE0': 0.0, 'dn': 0.006190689151516686, 'dA_dEa': 0.33688276837654896, 'dE0_dEa': 0.0, 'dn_dEa': -0.6881118698232935, 'name': 'C3H3-2 + H <=> C3H4-2'}, {'dA': 0.4980374494998878, 'dE0': 0.0, 'dn': 0.003928022998882531, 'dA_dEa': -0.003337050728191938, 'dE0_dEa': 0.0, 'dn_dEa': 0.007652724855984468, 'name': 'C3H3-2 + H <=> C3H4-2'}]
""",
)

entry(
    index = 108,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_2R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.7e+07,'m^3/(mol*s)'), n=4.95181e-08, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_2R->C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_2R->C_Ext-2C-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'C2H5 + OH <=> C2H6O-2'}]
""",
)

entry(
    index = 109,
    label = "Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_2NO->O",
    kinetics = ArrheniusBM(A=(122000,'m^3/(mol*s)'), n=0.2, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_2NO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_2NO->O
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_2NO->O
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_2NO->O
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330819365, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'NO2 + NO3-2 <=> N2O5'}]
""",
)

entry(
    index = 110,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=-1.37127e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_N-6R!H->C
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'C4H9 + CHO <=> C5H10O-2'}]
""",
)

entry(
    index = 111,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.12455e+08,'m^3/(mol*s)'), n=-0.428757, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-5R!H-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.05875075141404487, 'dE0': 0.0, 'dn': -8.128897628879144e-06, 'dA_dEa': 0.029750397665398942, 'dE0_dEa': 0.0, 'dn_dEa': 0.00498705356859251, 'name': 'C3H5 + C3H7-2 <=> C6H12'}, {'dA': 0.9406361301601477, 'dE0': 0.0, 'dn': -1.3142014777393963e-05, 'dA_dEa': 7.346949277558777, 'dE0_dEa': 0.0, 'dn_dEa': 1.2323565822552236, 'name': 'C5H11-2 + C3H7-2 <=> C8H18-4'}]
""",
)

entry(
    index = 112,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing",
    kinetics = ArrheniusBM(A=(199626,'m^3/(mol*s)'), n=0.610916, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0324341459036, var=0.917134149564, Tref=1000.0, N=50, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing
        Total Standard Deviation in ln(k): 2.00136989945"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing
Total Standard Deviation in ln(k): 2.00136989945""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing
Total Standard Deviation in ln(k): 2.00136989945
sensitivities = [{'dA': 0.018700231340320457, 'dE0': 0.0, 'dn': -2.3507260330346676e-05, 'dA_dEa': -0.009706842716284927, 'dE0_dEa': 0.0, 'dn_dEa': 0.0017457686700253995, 'name': 'CH3 + CH3 <=> C2H6'}, {'dA': 0.018700801202699964, 'dE0': 0.0, 'dn': -2.36226366780963e-05, 'dA_dEa': -0.0013733618224877468, 'dE0_dEa': 0.0, 'dn_dEa': 0.0002448238967340936, 'name': 'CH3 + C2H5 <=> C3H8'}, {'dA': 0.018695070174603427, 'dE0': 0.0, 'dn': -2.246802550444739e-05, 'dA_dEa': 0.0003506820132060215, 'dE0_dEa': 0.0, 'dn_dEa': -6.570724031227877e-05, 'name': 'C2H5 + C2H5 <=> C4H10'}, {'dA': 0.0068063285247895455, 'dE0': 0.0, 'dn': -2.343654832955299e-05, 'dA_dEa': -0.011787162577549158, 'dE0_dEa': 0.0, 'dn_dEa': 0.002120481250233084, 'name': 'C3H3 + C7H7 <=> C10H10'}, {'dA': 0.006808159682237441, 'dE0': 0.0, 'dn': -2.380695314080466e-05, 'dA_dEa': -0.03116546409920661, 'dE0_dEa': 0.0, 'dn_dEa': 0.005610674354382253, 'name': 'C3H3-2 + C7H7 <=> C10H10-2'}, {'dA': 0.00033088657147576674, 'dE0': 0.0, 'dn': -2.370919762398212e-05, 'dA_dEa': 0.0009762692254612314, 'dE0_dEa': 0.0, 'dn_dEa': -0.00017837441849155697, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}, {'dA': 0.0003308811464819792, 'dE0': 0.0, 'dn': -2.3708110644498393e-05, 'dA_dEa': 0.0006775499024059464, 'dE0_dEa': 0.0, 'dn_dEa': -0.00012456927489318484, 'name': 'C3H3 + C3H3-2 <=> C6H6-2'}, {'dA': 0.0003309272855745258, 'dE0': 0.0, 'dn': -2.3717422606823068e-05, 'dA_dEa': 0.0003707526605723341, 'dE0_dEa': 0.0, 'dn_dEa': -6.931411255537063e-05, 'name': 'C3H3 + C3H3 <=> C6H6-3'}, {'dA': 0.01870257105274426, 'dE0': 0.0, 'dn': -2.398071654974056e-05, 'dA_dEa': 0.1650404259372533, 'dE0_dEa': 0.0, 'dn_dEa': -0.02972796182836257, 'name': 'CH3 + C3H3-2 <=> C4H6'}, {'dA': 0.003530750827707541, 'dE0': 0.0, 'dn': -2.368279353600852e-05, 'dA_dEa': -0.013238435492725423, 'dE0_dEa': 0.0, 'dn_dEa': 0.0023818316958496657, 'name': 'CH3 + CH3 <=> C2H6-3'}, {'dA': 0.0003309272127438954, 'dE0': 0.0, 'dn': -2.3717408465162132e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'CH3 + C2H5 <=> C3H8-3'}, {'dA': 0.0003309278326924323, 'dE0': 0.0, 'dn': -2.3717534936607092e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'CH3 + C3H7-2 <=> C4H10-2'}, {'dA': 0.00033093660256614844, 'dE0': 0.0, 'dn': -2.3719304894033727e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'CH3 + C4H9 <=> C5H12'}, {'dA': 0.003530834037590969, 'dE0': 0.0, 'dn': -2.3699680607573878e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'CH3 + C2H3 <=> C3H6'}, {'dA': 0.00033092769058388517, 'dE0': 0.0, 'dn': -2.371750472487691e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'CH3 + CHO <=> C2H4O'}, {'dA': 0.00033089926887445477, 'dE0': 0.0, 'dn': -2.3711754371998994e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'CH3 + C2H3O <=> C3H6O'}, {'dA': 0.0003309372313964696, 'dE0': 0.0, 'dn': -2.371942718726068e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'C2H5 + C2H5 <=> C4H10-3'}, {'dA': 0.00033088977779986185, 'dE0': 0.0, 'dn': -2.370982548158752e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'C2H5 + C3H7-2 <=> C5H12-2'}, {'dA': 0.00033109213859464954, 'dE0': 0.0, 'dn': -2.3750725896924907e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.00033092769058388517, 'dE0': 0.0, 'dn': -2.371750472487691e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'C2H5 + CHO <=> C3H6O-2'}, {'dA': 0.0003309440170795961, 'dE0': 0.0, 'dn': -2.372080471359636e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'C2H5 + C2H3O <=> C4H8O'}, {'dA': 0.00033107950159209405, 'dE0': 0.0, 'dn': -2.3748236643198865e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'C3H7-2 + C3H7-2 <=> C6H14-2'}, {'dA': 0.00033082963390999344, 'dE0': 0.0, 'dn': -2.3697697721729744e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'C3H7-2 + C4H9 <=> C7H16'}, {'dA': 0.0003310482092900112, 'dE0': 0.0, 'dn': -2.3741891054956113e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'C3H7-2 + C2H3O <=> C5H10O'}, {'dA': 0.0003307557285836902, 'dE0': 0.0, 'dn': -2.3682768948802576e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'C4H9 + C4H9 <=> C8H18'}, {'dA': 0.00033092835316498627, 'dE0': 0.0, 'dn': -2.3717639552757877e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'C4H9 + CHO <=> C5H10O-2'}, {'dA': 0.00033087003536994876, 'dE0': 0.0, 'dn': -2.3705781609362723e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'C4H9 + C2H3O <=> C6H12O'}, {'dA': 0.00033092291040763035, 'dE0': 0.0, 'dn': -2.3716550644865836e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'C2H3 + C2H3 <=> C4H6-4'}, {'dA': 0.0035311275290443316, 'dE0': 0.0, 'dn': -2.3758850602533767e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'C2H3 + C2H <=> C4H4'}, {'dA': 0.00033092769058388517, 'dE0': 0.0, 'dn': -2.371750472487691e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'C2H3 + CHO <=> C3H4O'}, {'dA': 0.00353080875115136, 'dE0': 0.0, 'dn': -2.3694381180838976e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'CHO + CHO <=> C2H2O2'}, {'dA': 0.00033092769058388517, 'dE0': 0.0, 'dn': -2.371750472487691e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'CHO + C2H3O <=> C3H4O2'}, {'dA': 0.00033092835316498627, 'dE0': 0.0, 'dn': -2.3717639392057184e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'C2H3O + C2H3O <=> C4H6O2'}, {'dA': 0.0003309298026721672, 'dE0': 0.0, 'dn': -2.371793042101121e-05, 'dA_dEa': -0.0003799209924438137, 'dE0_dEa': 0.0, 'dn_dEa': 6.588994157232733e-05, 'name': 'CH3 + C4H9 <=> C5H12'}, {'dA': 0.00033089892603758476, 'dE0': 0.0, 'dn': -2.3711713875424496e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'CH3 + C3H7-2 <=> C4H10-2'}, {'dA': 0.0003310312042259876, 'dE0': 0.0, 'dn': -2.3738524857551374e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'C2H5 + C3H7-2 <=> C5H12-2'}, {'dA': 0.00033093247253649684, 'dE0': 0.0, 'dn': -2.3718471339541994e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.1673573899054943, 'dE0': 0.0, 'dn': -2.103752177499433e-05, 'dA_dEa': 0.484392187960534, 'dE0_dEa': 0.0, 'dn_dEa': -0.08724590370690048, 'name': 'HSS + CH3 <=> CH4S2'}, {'dA': 0.1673573899054943, 'dE0': 0.0, 'dn': -2.1037521935695024e-05, 'dA_dEa': 0.484392187960534, 'dE0_dEa': 0.0, 'dn_dEa': -0.08724590370690048, 'name': 'HSS + C4H9 <=> C4H10S2'}, {'dA': 0.1673783318914175, 'dE0': 0.0, 'dn': -2.5262830545391335e-05, 'dA_dEa': 0.8639774320188095, 'dE0_dEa': 0.0, 'dn_dEa': -0.15561300533661765, 'name': 'CH3S + C2H5 <=> C3H8S'}, {'dA': 0.1673783318914175, 'dE0': 0.0, 'dn': -2.5262830706092025e-05, 'dA_dEa': 0.8639953999268598, 'dE0_dEa': 0.0, 'dn_dEa': -0.15561663035566506, 'name': 'CH3S + CH3 <=> C2H6S'}, {'dA': 0.1673783318914175, 'dE0': 0.0, 'dn': -2.5262830706092025e-05, 'dA_dEa': 0.8639953999268598, 'dE0_dEa': 0.0, 'dn_dEa': -0.15561663035566506, 'name': 'CH3S + C4H9 <=> C5H12S'}, {'dA': 0.00033090617534984636, 'dE0': 0.0, 'dn': -2.371315616413923e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C3H5 <=> C6H10-2'}, {'dA': 0.0003309284402064714, 'dE0': 0.0, 'dn': -2.3717657390534736e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C2H5 <=> C5H10-2'}, {'dA': 0.00033094814355653403, 'dE0': 0.0, 'dn': -2.3721653213252493e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + CH3 <=> C4H8-2'}, {'dA': 0.0003309652516492543, 'dE0': 0.0, 'dn': -2.3725112777759547e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C3H7-2 <=> C6H12'}, {'dA': 0.00033088712747545747, 'dE0': 0.0, 'dn': -2.3709220604181142e-05, 'dA_dEa': 0.00022632226226451386, 'dE0_dEa': 0.0, 'dn_dEa': -4.3304907161795726e-05, 'name': 'C3H5 + C4H9 <=> C7H14'}, {'dA': 0.00033090617534984636, 'dE0': 0.0, 'dn': -2.371315616413923e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C5H7 <=> C8H12'}, {'dA': 0.0035348047013887282, 'dE0': 0.0, 'dn': -2.4502935626550618e-05, 'dA_dEa': 0.01387947691178379, 'dE0_dEa': 0.0, 'dn_dEa': -0.002502479660436564, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}, {'dA': 0.00033085554562720977, 'dE0': 0.0, 'dn': -2.3702960026604692e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'C3H3-2 + CH3 <=> C4H6-5'}, {'dA': 0.0035309197645720385, 'dE0': 0.0, 'dn': -2.371681515820561e-05, 'dA_dEa': 0.00011759550311297903, 'dE0_dEa': 0.0, 'dn_dEa': -2.371767571041368e-05, 'name': 'C11H23 + CH3 <=> C12H26'}, {'dA': 0.0035306354497781083, 'dE0': 0.0, 'dn': -2.365938185562902e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C10H21 + C2H5 <=> C12H26-2'}, {'dA': 0.0035309390344910323, 'dE0': 0.0, 'dn': -2.3720715203310665e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C9H19 + C3H7 <=> C12H26-3'}, {'dA': 0.0035310290442684415, 'dE0': 0.0, 'dn': -2.3738901379273785e-05, 'dA_dEa': 0.0003048260417415685, 'dE0_dEa': 0.0, 'dn_dEa': -5.744508643696318e-05, 'name': 'C8H17 + C4H9-2 <=> C12H26-4'}, {'dA': 0.0035304828003294712, 'dE0': 0.0, 'dn': -2.3628720163509666e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C7H15 + C5H11 <=> C12H26-5'}, {'dA': 0.003530880878344467, 'dE0': 0.0, 'dn': -2.3708936967458967e-05, 'dA_dEa': 2.4031036716112712e-05, 'dE0_dEa': 0.0, 'dn_dEa': -6.864226747433127e-06, 'name': 'C6H13 + C6H13 <=> C12H26-6'}, {'dA': 0.0035309771782014447, 'dE0': 0.0, 'dn': -2.3728432854065552e-05, 'dA_dEa': 0.0002111283681216724, 'dE0_dEa': 0.0, 'dn_dEa': -4.056474308819637e-05, 'name': 'CH3 + C9H19 <=> C10H22'}, {'dA': 0.0035309581445379106, 'dE0': 0.0, 'dn': -2.372459210751601e-05, 'dA_dEa': 0.00043797816573492405, 'dE0_dEa': 0.0, 'dn_dEa': -8.14180118957324e-05, 'name': 'C8H17 + C2H5 <=> C10H22-2'}, {'dA': 0.00353072178249686, 'dE0': 0.0, 'dn': -2.3676833790128342e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C7H15 + C3H7 <=> C10H22-3'}, {'dA': 0.0035312666497592797, 'dE0': 0.0, 'dn': -2.3786700514637338e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H13 + C4H9-2 <=> C10H22-4'}, {'dA': 0.003530912236371753, 'dE0': 0.0, 'dn': -2.3715296375961268e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C5H11 + C5H11 <=> C10H22-5'}, {'dA': 0.003528036057077022, 'dE0': 0.0, 'dn': -2.3134297485472595e-05, 'dA_dEa': -0.010784966992362166, 'dE0_dEa': 0.0, 'dn_dEa': 0.0019400271436570784, 'name': 'CH3 + C7H15-2 <=> C8H18-2'}, {'dA': 0.0035218665903617432, 'dE0': 0.0, 'dn': -2.188591970758912e-05, 'dA_dEa': 0.021902256627017915, 'dE0_dEa': 0.0, 'dn_dEa': -0.003947367294745087, 'name': 'C4H9-3 + C4H9 <=> C8H18-3'}, {'dA': 0.0035325105258725014, 'dE0': 0.0, 'dn': -2.4037675945975117e-05, 'dA_dEa': 0.026769545618424324, 'dE0_dEa': 0.0, 'dn_dEa': -0.004823841636141806, 'name': 'C5H11-2 + C3H7-2 <=> C8H18-4'}, {'dA': 0.003531878084217899, 'dE0': 0.0, 'dn': -2.3913743250556712e-05, 'dA_dEa': 0.02892172216739971, 'dE0_dEa': 0.0, 'dn_dEa': -0.0052118109546562645, 'name': 'C7H15-3 + CH3 <=> C8H18-5'}]
""",
)

entry(
    index = 113,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_3R!H->O",
    kinetics = ArrheniusBM(A=(7.05e+06,'m^3/(mol*s)'), n=8.99479e-09, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_3R!H->O
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_3R!H->O
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_3R!H->O
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'O2 + C4H9 <=> C4H9O2'}]
""",
)

entry(
    index = 114,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R",
    kinetics = ArrheniusBM(A=(1.76637e+07,'m^3/(mol*s)'), n=0.153073, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00248871722291, var=1.13870876508, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R
        Total Standard Deviation in ln(k): 2.14551182899"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R
Total Standard Deviation in ln(k): 2.14551182899""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R
Total Standard Deviation in ln(k): 2.14551182899
sensitivities = [{'dA': 0.0067348800811835785, 'dE0': 0.0, 'dn': -1.7707275387474924e-05, 'dA_dEa': 2.9742917462275366e-05, 'dE0_dEa': 0.0, 'dn_dEa': -1.962816094983114e-05, 'name': 'H + C3H7-2 <=> C3H8-2'}, {'dA': 0.006738019106223479, 'dE0': 0.0, 'dn': -1.97735871571313e-05, 'dA_dEa': -0.0032250599204534324, 'dE0_dEa': 0.0, 'dn_dEa': 0.0018945996712902689, 'name': 'H + C4H7 <=> C4H8'}, {'dA': 0.006738019106223479, 'dE0': 0.0, 'dn': -1.97735871571313e-05, 'dA_dEa': -0.0032250599204534324, 'dE0_dEa': 0.0, 'dn_dEa': 0.0018945996712902689, 'name': 'H + C5H9 <=> C5H10'}, {'dA': 0.006738019106223479, 'dE0': 0.0, 'dn': -1.97735871571313e-05, 'dA_dEa': -0.0032250599204534324, 'dE0_dEa': 0.0, 'dn_dEa': 0.0018945996712902689, 'name': 'H + C6H9 <=> C6H10'}, {'dA': 0.0067348800811835785, 'dE0': 0.0, 'dn': -1.7707275125102037e-05, 'dA_dEa': 2.9742917462275366e-05, 'dE0_dEa': 0.0, 'dn_dEa': -1.962816094983114e-05, 'name': 'H + C5H7 <=> C5H8'}, {'dA': 0.1073586515261245, 'dE0': 0.0, 'dn': -1.963689717985583e-05, 'dA_dEa': 0.0033894891053879842, 'dE0_dEa': 0.0, 'dn_dEa': -0.0019955720683881247, 'name': 'H + C12H25-2 <=> C12H26-8'}, {'dA': 0.1073586515261245, 'dE0': 0.0, 'dn': -1.963689717985583e-05, 'dA_dEa': 0.0033894891053879842, 'dE0_dEa': 0.0, 'dn_dEa': -0.001995572069044057, 'name': 'H + C12H25-3 <=> C12H26-9'}, {'dA': 0.1073586515261245, 'dE0': 0.0, 'dn': -1.963689717985583e-05, 'dA_dEa': 0.0033894891053879842, 'dE0_dEa': 0.0, 'dn_dEa': -0.001995572069044057, 'name': 'H + C12H25-4 <=> C12H26-10'}, {'dA': 0.1073586515261245, 'dE0': 0.0, 'dn': -1.963689717985583e-05, 'dA_dEa': 0.0033894891053879842, 'dE0_dEa': 0.0, 'dn_dEa': -0.001995572068781684, 'name': 'H + C12H25-5 <=> C12H26-11'}, {'dA': 0.1073586515261245, 'dE0': 0.0, 'dn': -1.963689717985583e-05, 'dA_dEa': 0.0033894891053879842, 'dE0_dEa': 0.0, 'dn_dEa': -0.001995572068781684, 'name': 'H + C12H25-6 <=> C12H26-12'}, {'dA': 0.10735904912452315, 'dE0': 0.0, 'dn': -1.989951407382856e-05, 'dA_dEa': -0.0024901950261838023, 'dE0_dEa': 0.0, 'dn_dEa': 0.0014624144691722971, 'name': 'H + C10H21-2 <=> C10H22-7'}, {'dA': 0.10735904912452315, 'dE0': 0.0, 'dn': -1.989951407382856e-05, 'dA_dEa': -0.0024901950261838023, 'dE0_dEa': 0.0, 'dn_dEa': 0.0014624144693034836, 'name': 'H + C10H21-3 <=> C10H22-8'}, {'dA': 0.10734665628221524, 'dE0': 0.0, 'dn': -1.1723202352095062e-05, 'dA_dEa': -0.0024901950261838023, 'dE0_dEa': 0.0, 'dn_dEa': 0.0014624144693034836, 'name': 'H + C10H21-4 <=> C10H22-9'}, {'dA': 0.10734665628221524, 'dE0': 0.0, 'dn': -1.1723202352095062e-05, 'dA_dEa': -0.0024901950261838023, 'dE0_dEa': 0.0, 'dn_dEa': 0.0014624144691722971, 'name': 'H + C10H21-5 <=> C10H22-10'}]
""",
)

entry(
    index = 115,
    label = "Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R",
    kinetics = ArrheniusBM(A=(5.66445e+06,'m^3/(mol*s)'), n=-0.45, w0=(77250,'J/mol'), E0=(7725,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.16655300091e-16, var=3.401841873, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R
        Total Standard Deviation in ln(k): 3.69754995947"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R
Total Standard Deviation in ln(k): 3.69754995947""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R
Total Standard Deviation in ln(k): 3.69754995947
sensitivities = [{'dA': 0.49997781642657735, 'dE0': 0.0, 'dn': 7.067746138151829e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'NO2 + NO2 <=> N2O4'}, {'dA': 0.49992543395843647, 'dE0': 0.0, 'dn': 5.4422562749663494e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'NO2 + NO3-2 <=> N2O5'}]
""",
)

entry(
    index = 116,
    label = "Root_N-1R->H_1CNOS->N_Ext-2R-R_N-3R!H-u0",
    kinetics = ArrheniusBM(A=(6.60235e+128,'m^3/(mol*s)'), n=-37.2419, w0=(71000,'J/mol'), E0=(271802,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.394167378209, var=243.949911149, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1CNOS->N_Ext-2R-R_N-3R!H-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_N-3R!H-u0
        Total Standard Deviation in ln(k): 32.3021189072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_N-3R!H-u0
Total Standard Deviation in ln(k): 32.3021189072""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_N-3R!H-u0
Total Standard Deviation in ln(k): 32.3021189072
sensitivities = [{'dA': 8.778819570879193, 'dE0': 0.08297508435043488, 'dn': 0.0711621561355004, 'dA_dEa': -17.479671614113606, 'dE0_dEa': -0.11239485721519724, 'dn_dEa': -0.1502137101475093, 'name': 'NO + O2 <=> NO3'}, {'dA': -11.03371962851562, 'dE0': -0.11553950369367637, 'dn': -0.09914052842749564, 'dA_dEa': 6.135169309801079, 'dE0_dEa': 0.09342722160080573, 'dn_dEa': 0.05275590142788015, 'name': 'NH2 + O2 <=> NH2OO'}]
""",
)

entry(
    index = 117,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_2R-inRing",
    kinetics = ArrheniusBM(A=(1.77136e+06,'m^3/(mol*s)'), n=0.0494766, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0355540882513, var=0.00255574629843, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_2R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_2R-inRing
        Total Standard Deviation in ln(k): 0.190680037989"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_2R-inRing
Total Standard Deviation in ln(k): 0.190680037989""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_2R-inRing
Total Standard Deviation in ln(k): 0.190680037989
sensitivities = [{'dA': 0.07554604118276964, 'dE0': 0.0, 'dn': -0.0001347195950373351, 'dA_dEa': -0.09434229311012717, 'dE0_dEa': 0.0, 'dn_dEa': 0.10107446774478085, 'name': 'O2 + C6H5 <=> C6H5O2'}, {'dA': 0.924180501257967, 'dE0': 0.0, 'dn': -0.00013724871676741495, 'dA_dEa': 2.281920390508925, 'dE0_dEa': 0.0, 'dn_dEa': -2.445125382633507, 'name': 'O2 + C6H5 <=> C6H5O2'}]
""",
)

entry(
    index = 118,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.40832e+09,'m^3/(mol*s)'), n=-1.11667, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.14473363032e-10, var=3.4189890868, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R
        Total Standard Deviation in ln(k): 3.70685712135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.70685712135""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.70685712135
sensitivities = [{'dA': 0.3331058975853208, 'dE0': 0.0, 'dn': -7.615785779341256e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C3H7-2 + C4H9 <=> C7H16'}, {'dA': 0.3331165661002811, 'dE0': 0.0, 'dn': -6.259549666887788e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C4H9 + C4H9 <=> C8H18'}, {'dA': 0.3331002731137656, 'dE0': 0.0, 'dn': -8.336239124884158e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C4H9 + C2H3O <=> C6H12O'}]
""",
)

entry(
    index = 119,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(3.17094e+06,'m^3/(mol*s)'), n=0.460394, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H7-3 + H <=> C6H8-4'}]
""",
)

entry(
    index = 120,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C",
    kinetics = ArrheniusBM(A=(7.84783e+07,'m^3/(mol*s)'), n=0.0629272, w0=(201667,'J/mol'), E0=(20166.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0177834035034, var=0.220663363462, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C
        Total Standard Deviation in ln(k): 0.986402595487"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C
Total Standard Deviation in ln(k): 0.986402595487""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C
Total Standard Deviation in ln(k): 0.986402595487
sensitivities = [{'dA': 0.23153492673702367, 'dE0': 0.0, 'dn': 0.0007666832073158937, 'dA_dEa': 0.0003091469764627049, 'dE0_dEa': 0.0, 'dn_dEa': -0.000263412820840965, 'name': 'C6H7-3 + H <=> C6H8-4'}, {'dA': 0.23193070305540853, 'dE0': 0.0, 'dn': 0.0002710914989162484, 'dA_dEa': -0.008793102995953008, 'dE0_dEa': 0.0, 'dn_dEa': 0.009897200661443426, 'name': 'C6H7-5 + H <=> C6H8-6'}, {'dA': 0.08303256845111155, 'dE0': 0.0, 'dn': 0.0006767005843119377, 'dA_dEa': 0.26098310524250257, 'dE0_dEa': 0.0, 'dn_dEa': -0.29117117364679573, 'name': 'C6H7-6 + H <=> C6H8-7'}, {'dA': 0.002045616039225931, 'dE0': 0.0, 'dn': 0.0007755105820986321, 'dA_dEa': -0.0002939939953705885, 'dE0_dEa': 0.0, 'dn_dEa': 0.00041242569188528025, 'name': 'C3H3 + H <=> C3H4'}, {'dA': 0.23173472661144667, 'dE0': 0.0, 'dn': 0.0005165564093072383, 'dA_dEa': 0.918819974348496, 'dE0_dEa': 0.0, 'dn_dEa': -1.0253398478208864, 'name': 'C4H5-2 + H <=> C4H6-3'}, {'dA': 0.08351004207797029, 'dE0': 0.0, 'dn': 7.880891275959875e-05, 'dA_dEa': 0.013770511401391256, 'dE0_dEa': 0.0, 'dn_dEa': -0.015283706027852992, 'name': 'C7H7 + H <=> C7H8-2'}, {'dA': 0.0020456185936270663, 'dE0': 0.0, 'dn': 0.0007755073906400087, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C2H5 <=> C2H6-2'}, {'dA': 0.00204565284178693, 'dE0': 0.0, 'dn': 0.000775464486239058, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C2H <=> C2H2'}, {'dA': 0.04267579774364564, 'dE0': 0.0, 'dn': -4.574272363803161e-05, 'dA_dEa': -0.021306743107632045, 'dE0_dEa': 0.0, 'dn_dEa': 0.023862448938676062, 'name': 'H + C3H5 <=> C3H6-2'}, {'dA': 0.04252333635790719, 'dE0': 0.0, 'dn': 0.00014517756996543734, 'dA_dEa': -0.001120086874806371, 'dE0_dEa': 0.0, 'dn_dEa': 0.0013343732558054307, 'name': 'H + C12H25 <=> C12H26-7'}, {'dA': 0.04214580611617189, 'dE0': 0.0, 'dn': 0.0006179068123900279, 'dA_dEa': -0.0016192081595535874, 'dE0_dEa': 0.0, 'dn_dEa': 0.0018911997825200512, 'name': 'H + C10H21 <=> C10H22-6'}]
""",
)

entry(
    index = 121,
    label = "Root_1R->H",
    kinetics = ArrheniusBM(A=(3.20048e+07,'m^3/(mol*s)'), n=0.198453, w0=(190779,'J/mol'), E0=(19077.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0115767819513, var=3.42756550074, Tref=1000.0, N=43, data_mean=0.0, correlation='Root_1R->H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H
        Total Standard Deviation in ln(k): 3.74059086132"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 3.74059086132""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 3.74059086132
sensitivities = [{'dA': 0.01811116826644565, 'dE0': 0.0, 'dn': 0.0017412796761929867, 'dA_dEa': -0.003916352687483458, 'dE0_dEa': 0.0, 'dn_dEa': 0.0012039306854738346, 'name': 'C6H7 + H <=> C6H8-2'}, {'dA': 0.018111417125157066, 'dE0': 0.0, 'dn': 0.001741207304027333, 'dA_dEa': -0.0061803462951821745, 'dE0_dEa': 0.0, 'dn_dEa': 0.0017901616628655287, 'name': 'C6H7-2 + H <=> C6H8-3'}, {'dA': 0.018112901512880916, 'dE0': 0.0, 'dn': 0.0017407773156898165, 'dA_dEa': -0.005893640578236808, 'dE0_dEa': 0.0, 'dn_dEa': 0.0017158050137234, 'name': 'C6H7-3 + H <=> C6H8-4'}, {'dA': 0.018118143239933323, 'dE0': 0.0, 'dn': 0.001739251893304834, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H7-4 + H <=> C6H8-5'}, {'dA': 0.01811139158469843, 'dE0': 0.0, 'dn': 0.0017412145824128838, 'dA_dEa': -0.006840877491144014, 'dE0_dEa': 0.0, 'dn_dEa': 0.0019612036959353214, 'name': 'C6H7-5 + H <=> C6H8-6'}, {'dA': 0.002685667263691312, 'dE0': 0.0, 'dn': 0.001741204926760996, 'dA_dEa': 0.021170813532480737, 'dE0_dEa': 0.0, 'dn_dEa': -0.005291885227116946, 'name': 'C6H7-6 + H <=> C6H8-7'}, {'dA': 0.018111398540911813, 'dE0': 0.0, 'dn': 0.001741212674593116, 'dA_dEa': 0.021736702917609825, 'dE0_dEa': 0.0, 'dn_dEa': -0.0054384112698732025, 'name': 'H + NJCO <=> HNCO'}, {'dA': 0.01809247203788033, 'dE0': 0.0, 'dn': 0.0017467180097763834, 'dA_dEa': 0.021718070961187667, 'dE0_dEa': 0.0, 'dn_dEa': -0.005432991113944804, 'name': 'H + NCOJ <=> NCOH'}, {'dA': 0.019771320305397258, 'dE0': 0.0, 'dn': 0.0012589114067373189, 'dA_dEa': -1.2088483643940773, 'dE0_dEa': 0.0, 'dn_dEa': 0.3129074466759254, 'name': '[S]S + [H] <=> HSSH'}, {'dA': 0.0025424827025946643, 'dE0': 0.0, 'dn': 0.0017828511827173888, 'dA_dEa': 0.48070468274380185, 'dE0_dEa': 0.0, 'dn_dEa': -0.1242800226531652, 'name': '[CH2]c1ccccc1[C]=C=C + [H] <=> C10H9'}, {'dA': 0.0027796137693772713, 'dE0': 0.0, 'dn': 0.0017138895162399782, 'dA_dEa': 0.17329576077431375, 'dE0_dEa': 0.0, 'dn_dEa': -0.04467870772036909, 'name': 'C=C1[CH]c2ccccc2C1 + [H] <=> C10H10-3'}, {'dA': 0.002683365558198443, 'dE0': 0.0, 'dn': 0.0017418754232955613, 'dA_dEa': -0.0526546322792201, 'dE0_dEa': 0.0, 'dn_dEa': 0.013823825076530462, 'name': 'C=C1[CH]Cc2ccccc21 + [H] <=> C10H10-4'}, {'dA': 0.0026479668768789183, 'dE0': 0.0, 'dn': 0.001752156054691725, 'dA_dEa': -0.007195634735169503, 'dE0_dEa': 0.0, 'dn_dEa': 0.002053605566819733, 'name': 'C=C1C[CH]c2ccccc21 + [H] <=> C10H10-5'}, {'dA': 0.002681259894999084, 'dE0': 0.0, 'dn': 0.0017424836166234044, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C9H7 + H <=> C9H8-3'}, {'dA': -0.005714554934144819, 'dE0': 0.0, 'dn': 0.0017411825505394489, 'dA_dEa': -0.005957474662921614, 'dE0_dEa': 0.0, 'dn_dEa': 0.0017324387808229892, 'name': 'C3H3 + H <=> C3H4'}, {'dA': -0.005714682169256155, 'dE0': 0.0, 'dn': 0.001741219511717374, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H3-2 + H <=> C3H4-2'}, {'dA': 0.01811036349330863, 'dE0': 0.0, 'dn': 0.001741513606015855, 'dA_dEa': -0.10058686605952658, 'dE0_dEa': 0.0, 'dn_dEa': 0.026234812297255553, 'name': 'C4H5 + H <=> C4H6-2'}, {'dA': 0.018118725604312266, 'dE0': 0.0, 'dn': 0.0017390837242365986, 'dA_dEa': 0.08945883867640267, 'dE0_dEa': 0.0, 'dn_dEa': -0.022973872879617725, 'name': 'C4H5-2 + H <=> C4H6-3'}, {'dA': 0.00268516827617334, 'dE0': 0.0, 'dn': 0.0017413501481627586, 'dA_dEa': -0.004497747752907839, 'dE0_dEa': 0.0, 'dn_dEa': 0.0013544845498758749, 'name': 'C7H7 + H <=> C7H8-2'}, {'dA': 0.0026784192606047093, 'dE0': 0.0, 'dn': 0.0017433131058395275, 'dA_dEa': 0.008810358259837418, 'dE0_dEa': 0.0, 'dn_dEa': -0.002091338802070983, 'name': 'C7H7-2 + H <=> C7H8-3'}, {'dA': 0.0026856115198373347, 'dE0': 0.0, 'dn': 0.0017412210059990717, 'dA_dEa': 0.005317674173000472, 'dE0_dEa': 0.0, 'dn_dEa': -0.0011871202739703237, 'name': 'C7H7-3 + H <=> C7H8-4'}, {'dA': -0.005714197486739811, 'dE0': 0.0, 'dn': 0.0017410786564921424, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + H <=> H2'}, {'dA': -0.005721445029749991, 'dE0': 0.0, 'dn': 0.0017431852191912836, 'dA_dEa': -0.007621506462386081, 'dE0_dEa': 0.0, 'dn_dEa': 0.002163504421399381, 'name': 'H + H <=> H2'}, {'dA': -0.0015642248794025039, 'dE0': 0.0, 'dn': 0.0017411870249520616, 'dA_dEa': -0.010668401127845792, 'dE0_dEa': 0.0, 'dn_dEa': 0.0029522385213380875, 'name': 'H + CH3 <=> CH4'}, {'dA': -0.005714465382667474, 'dE0': 0.0, 'dn': 0.0017411565319485074, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C2H5 <=> C2H6-2'}, {'dA': -0.005714265000734206, 'dE0': 0.0, 'dn': 0.0017410982256218887, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C3H7-2 <=> C3H8-2'}, {'dA': -0.0015642772481784864, 'dE0': 0.0, 'dn': 0.0017412023033355447, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C2H3 <=> C2H4'}, {'dA': -0.005714566404080931, 'dE0': 0.0, 'dn': 0.0017411858825242639, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C2H <=> C2H2'}, {'dA': -0.0015642241315562745, 'dE0': 0.0, 'dn': 0.001741186799123311, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C6H5 <=> C6H6-4'}, {'dA': -0.005714188286987739, 'dE0': 0.0, 'dn': 0.0017410770719944579, 'dA_dEa': -0.0010859590666713135, 'dE0_dEa': 0.0, 'dn_dEa': 0.00047103434954810086, 'name': 'H + CHO <=> CH2O'}, {'dA': -0.001564149144428656, 'dE0': 0.0, 'dn': 0.001741165032812661, 'dA_dEa': -0.008589567420004109, 'dE0_dEa': 0.0, 'dn_dEa': 0.002413963114201343, 'name': 'H + OH <=> H2O'}, {'dA': -0.005714634550458361, 'dE0': 0.0, 'dn': 0.0017412056998923659, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + CH3 <=> CH4'}, {'dA': -0.005714850054517403, 'dE0': 0.0, 'dn': 0.0017412682837967168, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'O2 + H <=> HO2-2'}, {'dA': 0.2109537475743172, 'dE0': 0.0, 'dn': 0.0017352959266710886, 'dA_dEa': 0.3080251907192972, 'dE0_dEa': 0.0, 'dn_dEa': -0.07956561243422688, 'name': 'CH3S-2 + H <=> CH4S'}, {'dA': 0.21091781019502256, 'dE0': 0.0, 'dn': 0.0017457339059531167, 'dA_dEa': 0.06189476513896579, 'dE0_dEa': 0.0, 'dn_dEa': -0.015835920607180705, 'name': 'SH + H <=> H2S'}, {'dA': -0.0015641752533214815, 'dE0': 0.0, 'dn': 0.001741172548462792, 'dA_dEa': -0.008139450557110637, 'dE0_dEa': 0.0, 'dn_dEa': 0.0022974230532984913, 'name': 'H + C3H5 <=> C3H6-2'}, {'dA': -0.00571456409481704, 'dE0': 0.0, 'dn': 0.0017411852086189283, 'dA_dEa': -0.006125518797973193, 'dE0_dEa': 0.0, 'dn_dEa': 0.0017759508642975891, 'name': 'H + C4H7 <=> C4H8'}, {'dA': -0.00571456409481704, 'dE0': 0.0, 'dn': 0.0017411852086189283, 'dA_dEa': -0.006125518797973193, 'dE0_dEa': 0.0, 'dn_dEa': 0.0017759508642975891, 'name': 'H + C5H9 <=> C5H10'}, {'dA': -0.00571456409481704, 'dE0': 0.0, 'dn': 0.0017411852086189283, 'dA_dEa': -0.006125518797973193, 'dE0_dEa': 0.0, 'dn_dEa': 0.0017759508642975891, 'name': 'H + C6H9 <=> C6H10'}, {'dA': -0.005714197484963454, 'dE0': 0.0, 'dn': 0.0017410786563766291, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H3-2 + H <=> C3H4-2'}, {'dA': -0.0015641505886067665, 'dE0': 0.0, 'dn': 0.0017411652483607166, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C5H5 + H <=> C5H6'}, {'dA': -0.005714265000734206, 'dE0': 0.0, 'dn': 0.0017410982256218887, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C5H7 <=> C5H8'}, {'dA': -0.0015656233181006788, 'dE0': 0.0, 'dn': 0.0017415982807080736, 'dA_dEa': -0.013433936841168817, 'dE0_dEa': 0.0, 'dn_dEa': 0.0036681265970185638, 'name': 'H + SH <=> H2S-2'}, {'dA': 0.048231721915930933, 'dE0': 0.0, 'dn': 0.0017435706691320873, 'dA_dEa': 0.02753877740424874, 'dE0_dEa': 0.0, 'dn_dEa': -0.00694080395005385, 'name': 'H + C12H9 <=> C12H10-2'}, {'dA': 0.048237784886500976, 'dE0': 0.0, 'dn': 0.0017418094007875015, 'dA_dEa': 0.02689989735849293, 'dE0_dEa': 0.0, 'dn_dEa': -0.006775303724723452, 'name': 'H + C12H9-2 <=> C12H10-3'}, {'dA': 0.04824630425482289, 'dE0': 0.0, 'dn': 0.0017393322420191943, 'dA_dEa': -0.009169373718976758, 'dE0_dEa': 0.0, 'dn_dEa': 0.002563939660859566, 'name': 'H + C12H9-3 <=> C12H10-4'}, {'dA': -0.0015640922654826584, 'dE0': 0.0, 'dn': 0.0017411485036497852, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C12H25 <=> C12H26-7'}, {'dA': -0.001564399871867467, 'dE0': 0.0, 'dn': 0.0017412378371140468, 'dA_dEa': -0.005852689186625715, 'dE0_dEa': 0.0, 'dn_dEa': 0.0017053072564736874, 'name': 'H + C12H25-2 <=> C12H26-8'}, {'dA': -0.001564399871867467, 'dE0': 0.0, 'dn': 0.0017412378371140468, 'dA_dEa': -0.005852689186625715, 'dE0_dEa': 0.0, 'dn_dEa': 0.0017053072564736874, 'name': 'H + C12H25-3 <=> C12H26-9'}, {'dA': -0.001564399871867467, 'dE0': 0.0, 'dn': 0.0017412378371140468, 'dA_dEa': -0.005852689186625715, 'dE0_dEa': 0.0, 'dn_dEa': 0.0017053072564736874, 'name': 'H + C12H25-4 <=> C12H26-10'}, {'dA': -0.001564399871867467, 'dE0': 0.0, 'dn': 0.0017412378371140468, 'dA_dEa': -0.005852689186625715, 'dE0_dEa': 0.0, 'dn_dEa': 0.0017053072564736874, 'name': 'H + C12H25-5 <=> C12H26-11'}, {'dA': -0.001564399871867467, 'dE0': 0.0, 'dn': 0.0017412378371140468, 'dA_dEa': -0.005852689186625715, 'dE0_dEa': 0.0, 'dn_dEa': 0.0017053072564736874, 'name': 'H + C12H25-6 <=> C12H26-12'}, {'dA': -0.0015640806285690035, 'dE0': 0.0, 'dn': 0.0017411451074395045, 'dA_dEa': -0.006095461866806989, 'dE0_dEa': 0.0, 'dn_dEa': 0.001768176377338572, 'name': 'H + C10H21 <=> C10H22-6'}, {'dA': -0.0015640806285690035, 'dE0': 0.0, 'dn': 0.0017411451074395045, 'dA_dEa': -0.006095461866806989, 'dE0_dEa': 0.0, 'dn_dEa': 0.001768176377338572, 'name': 'H + C10H21-2 <=> C10H22-7'}, {'dA': -0.0015640806285690035, 'dE0': 0.0, 'dn': 0.001741145107323991, 'dA_dEa': -0.006095461866806989, 'dE0_dEa': 0.0, 'dn_dEa': 0.001768176377338572, 'name': 'H + C10H21-3 <=> C10H22-8'}, {'dA': -0.0015640806285690035, 'dE0': 0.0, 'dn': 0.0017411451074395045, 'dA_dEa': -0.006095461866806989, 'dE0_dEa': 0.0, 'dn_dEa': 0.001768176377338572, 'name': 'H + C10H21-4 <=> C10H22-9'}, {'dA': -0.0015640806285690035, 'dE0': 0.0, 'dn': 0.0017411451074395045, 'dA_dEa': -0.006095461866806989, 'dE0_dEa': 0.0, 'dn_dEa': 0.001768176377338572, 'name': 'H + C10H21-5 <=> C10H22-10'}]
""",
)

entry(
    index = 122,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.80332e+07,'m^3/(mol*s)'), n=0.127561, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00207394171242, var=4.85073603852, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R_Ext-3R!H-R
        Total Standard Deviation in ln(k): 4.42051694063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.42051694063""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.42051694063
sensitivities = [{'dA': 0.499708871863957, 'dE0': 0.0, 'dn': 4.8014247910207084e-05, 'dA_dEa': -0.24249838837778098, 'dE0_dEa': 0.0, 'dn_dEa': 0.2510949422113383, 'name': 'H + C4H7 <=> C4H8'}, {'dA': 0.4995973096449386, 'dE0': 0.0, 'dn': 0.00017765417620270332, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C5H7 <=> C5H8'}]
""",
)

entry(
    index = 123,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.8345e+07,'m^3/(mol*s)'), n=-0.175, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.38215142465e-09, var=1.02308715893, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R
        Total Standard Deviation in ln(k): 2.02774485734"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.02774485734""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.02774485734
sensitivities = [{'dA': 0.4997617073563827, 'dE0': 0.0, 'dn': 9.17971271929921e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C3H7-2 + C2H3O <=> C5H10O'}, {'dA': 0.4996696137845031, 'dE0': 0.0, 'dn': -6.428265454201407e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H3O + C2H3O <=> C4H6O2'}]
""",
)

entry(
    index = 124,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing",
    kinetics = ArrheniusBM(A=(6.35832e+07,'m^3/(mol*s)'), n=0.0354724, w0=(181241,'J/mol'), E0=(18124.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.256587721226, var=1.96898110437, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing
        Total Standard Deviation in ln(k): 3.45774478839"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing
Total Standard Deviation in ln(k): 3.45774478839""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing
Total Standard Deviation in ln(k): 3.45774478839
sensitivities = [{'dA': 0.052837894646279575, 'dE0': 0.0, 'dn': -0.00014452252813475585, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H7-3 + H <=> C6H8-4'}, {'dA': 0.052836789624427775, 'dE0': 0.0, 'dn': -0.0001436768213776169, 'dA_dEa': -0.001648473137550081, 'dE0_dEa': 0.0, 'dn_dEa': 0.0011045123034575687, 'name': 'C6H7-5 + H <=> C6H8-6'}, {'dA': 0.019144333904821287, 'dE0': 0.0, 'dn': -0.00014574258434299248, 'dA_dEa': 0.05952851449820374, 'dE0_dEa': 0.0, 'dn_dEa': -0.04052083140395752, 'name': 'C6H7-6 + H <=> C6H8-7'}, {'dA': 0.05283320457394907, 'dE0': 0.0, 'dn': -0.0001409429921670962, 'dA_dEa': 0.060751407655608186, 'dE0_dEa': 0.0, 'dn_dEa': -0.04135181822172768, 'name': 'H + NJCO <=> HNCO'}, {'dA': 0.05281228773413331, 'dE0': 0.0, 'dn': -0.00012495775762436258, 'dA_dEa': 0.060764610125836366, 'dE0_dEa': 0.0, 'dn_dEa': -0.041361891704916956, 'name': 'H + NCOJ <=> NCOH'}, {'dA': 0.019061288448087733, 'dE0': 0.0, 'dn': -8.240279769926247e-05, 'dA_dEa': 1.0629304576818048, 'dE0_dEa': 0.0, 'dn_dEa': -0.7232301854275007, 'name': '[CH2]c1ccccc1[C]=C=C + [H] <=> C10H9'}, {'dA': 0.0007936514485607823, 'dE0': 0.0, 'dn': -0.00014456457483838926, 'dA_dEa': 0.00026309145795269786, 'dE0_dEa': 0.0, 'dn_dEa': -0.00019480018100519685, 'name': 'C3H3 + H <=> C3H4'}, {'dA': 0.0007936696420075314, 'dE0': 0.0, 'dn': -0.00014457848279851758, 'dA_dEa': 0.0005986099438360475, 'dE0_dEa': 0.0, 'dn_dEa': -0.0004230910755887372, 'name': 'C3H3-2 + H <=> C3H4-2'}, {'dA': 0.05282404879381501, 'dE0': 0.0, 'dn': -0.00013395454650943781, 'dA_dEa': -0.20645922426256788, 'dE0_dEa': 0.0, 'dn_dEa': 0.14046475267812572, 'name': 'C4H5 + H <=> C4H6-2'}, {'dA': 0.05282935667950155, 'dE0': 0.0, 'dn': -0.0001380008175066786, 'dA_dEa': 0.20865912507519535, 'dE0_dEa': 0.0, 'dn_dEa': -0.1419904598257386, 'name': 'C4H5-2 + H <=> C4H6-3'}, {'dA': 0.01913972067413494, 'dE0': 0.0, 'dn': -0.00014221908757719958, 'dA_dEa': 0.003451144952038401, 'dE0_dEa': 0.0, 'dn_dEa': -0.0023639000857334155, 'name': 'C7H7 + H <=> C7H8-2'}, {'dA': 0.009853599792110066, 'dE0': 0.0, 'dn': -0.00014011144470779094, 'dA_dEa': -0.010030336834888626, 'dE0_dEa': 0.0, 'dn_dEa': 0.006809314703509677, 'name': 'H + CH3 <=> CH4'}, {'dA': 0.0007937409840509154, 'dE0': 0.0, 'dn': -0.00014463294977375976, 'dA_dEa': 0.0001892815504334275, 'dE0_dEa': 0.0, 'dn_dEa': -0.00014457642823419506, 'name': 'H + C2H5 <=> C2H6-2'}, {'dA': 0.0007930896295250441, 'dE0': 0.0, 'dn': -0.00014413556975699643, 'dA_dEa': 0.0001892815504334275, 'dE0_dEa': 0.0, 'dn_dEa': -0.00014457642823419506, 'name': 'H + C3H7-2 <=> C3H8-2'}, {'dA': 0.009859677167157719, 'dE0': 0.0, 'dn': -0.0001447514334946316, 'dA_dEa': 0.0001892815504334275, 'dE0_dEa': 0.0, 'dn_dEa': -0.00014457642823419506, 'name': 'H + C2H3 <=> C2H4'}, {'dA': 0.0007937198915898044, 'dE0': 0.0, 'dn': -0.00014461683866258575, 'dA_dEa': 0.0001892815504334275, 'dE0_dEa': 0.0, 'dn_dEa': -0.00014457642823419506, 'name': 'H + C2H <=> C2H2'}, {'dA': 0.0007859645130282344, 'dE0': 0.0, 'dn': -0.0001386975275991232, 'dA_dEa': 0.01090657077185262, 'dE0_dEa': 0.0, 'dn_dEa': -0.007437180538718557, 'name': 'H + CHO <=> CH2O'}, {'dA': 0.009858255786810963, 'dE0': 0.0, 'dn': -0.0001436660273641684, 'dA_dEa': -0.005487307440433292, 'dE0_dEa': 0.0, 'dn_dEa': 0.0037179516887757944, 'name': 'H + OH <=> H2O'}, {'dA': 0.0007936435579837017, 'dE0': 0.0, 'dn': -0.00014455858295356339, 'dA_dEa': 0.0001892815504334275, 'dE0_dEa': 0.0, 'dn_dEa': -0.00014457642823419506, 'name': 'H + CH3 <=> CH4'}, {'dA': 0.0007937128216895836, 'dE0': 0.0, 'dn': -0.00014461147056880403, 'dA_dEa': -0.000874740742062937, 'dE0_dEa': 0.0, 'dn_dEa': 0.0005793892587736112, 'name': 'O2 + H <=> HO2-2'}, {'dA': 0.4740246396473491, 'dE0': 0.0, 'dn': -0.00014244133704110137, 'dA_dEa': 0.6861923378665625, 'dE0_dEa': 0.0, 'dn_dEa': -0.46691344885934105, 'name': 'CH3S-2 + H <=> CH4S'}, {'dA': 0.009858164073507345, 'dE0': 0.0, 'dn': -0.00014359628266865824, 'dA_dEa': -0.004502965115449838, 'dE0_dEa': 0.0, 'dn_dEa': 0.0030481407739939665, 'name': 'H + C3H5 <=> C3H6-2'}, {'dA': 0.0007935867003539862, 'dE0': 0.0, 'dn': -0.00014451516436495465, 'dA_dEa': -0.00010398386862676725, 'dE0_dEa': 0.0, 'dn_dEa': 5.4968397455245676e-05, 'name': 'H + C4H7 <=> C4H8'}, {'dA': 0.0007935867003539862, 'dE0': 0.0, 'dn': -0.00014451516436495465, 'dA_dEa': -0.00010398386862676725, 'dE0_dEa': 0.0, 'dn_dEa': 5.4968397455245676e-05, 'name': 'H + C5H9 <=> C5H10'}, {'dA': 0.0007935867003539862, 'dE0': 0.0, 'dn': -0.00014451516436495465, 'dA_dEa': -0.00010398386862676725, 'dE0_dEa': 0.0, 'dn_dEa': 5.4968397455245676e-05, 'name': 'H + C6H9 <=> C6H10'}, {'dA': 0.0007912141022360136, 'dE0': 0.0, 'dn': -0.00014270408496230033, 'dA_dEa': 0.0001892815504334275, 'dE0_dEa': 0.0, 'dn_dEa': -0.00014457642823419506, 'name': 'C3H3-2 + H <=> C3H4-2'}, {'dA': 0.0007930896295250441, 'dE0': 0.0, 'dn': -0.0001441355712747362, 'dA_dEa': 0.0001892815504334275, 'dE0_dEa': 0.0, 'dn_dEa': -0.00014457642823419506, 'name': 'H + C5H7 <=> C5H8'}, {'dA': 0.009865774526219815, 'dE0': 0.0, 'dn': -0.00014940689366533454, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C12H25 <=> C12H26-7'}, {'dA': 0.009858353529069695, 'dE0': 0.0, 'dn': -0.00014374058405360962, 'dA_dEa': 0.0004902699295428732, 'dE0_dEa': 0.0, 'dn_dEa': -0.0003492315328936877, 'name': 'H + C12H25-2 <=> C12H26-8'}, {'dA': 0.009858353529069695, 'dE0': 0.0, 'dn': -0.00014374058405360962, 'dA_dEa': 0.0004902699295428732, 'dE0_dEa': 0.0, 'dn_dEa': -0.0003492315328936877, 'name': 'H + C12H25-3 <=> C12H26-9'}, {'dA': 0.009858353529069695, 'dE0': 0.0, 'dn': -0.00014374058420538362, 'dA_dEa': 0.0004902699295428732, 'dE0_dEa': 0.0, 'dn_dEa': -0.0003492315328936877, 'name': 'H + C12H25-4 <=> C12H26-10'}, {'dA': 0.009858353529069695, 'dE0': 0.0, 'dn': -0.00014374058420538362, 'dA_dEa': 0.0004902699295428732, 'dE0_dEa': 0.0, 'dn_dEa': -0.0003492315328936877, 'name': 'H + C12H25-5 <=> C12H26-11'}, {'dA': 0.009858353529069695, 'dE0': 0.0, 'dn': -0.00014374058420538362, 'dA_dEa': 0.0004902699295428732, 'dE0_dEa': 0.0, 'dn_dEa': -0.0003492315328936877, 'name': 'H + C12H25-6 <=> C12H26-12'}, {'dA': 0.009859008475389095, 'dE0': 0.0, 'dn': -0.00014424135348682047, 'dA_dEa': -3.46111228566353e-05, 'dE0_dEa': 0.0, 'dn_dEa': 7.503351470832472e-06, 'name': 'H + C10H21 <=> C10H22-6'}, {'dA': 0.009859008475389095, 'dE0': 0.0, 'dn': -0.00014424135348682047, 'dA_dEa': -3.46111228566353e-05, 'dE0_dEa': 0.0, 'dn_dEa': 7.503351470832472e-06, 'name': 'H + C10H21-2 <=> C10H22-7'}, {'dA': 0.009859008475389095, 'dE0': 0.0, 'dn': -0.00014424135348682047, 'dA_dEa': -3.46111228566353e-05, 'dE0_dEa': 0.0, 'dn_dEa': 7.503351470832472e-06, 'name': 'H + C10H21-3 <=> C10H22-8'}, {'dA': 0.009859008475389095, 'dE0': 0.0, 'dn': -0.00014424135363859446, 'dA_dEa': -3.46111228566353e-05, 'dE0_dEa': 0.0, 'dn_dEa': 7.503351470832472e-06, 'name': 'H + C10H21-4 <=> C10H22-9'}, {'dA': 0.009859008475389095, 'dE0': 0.0, 'dn': -0.00014424135363859446, 'dA_dEa': -3.46111228566353e-05, 'dE0_dEa': 0.0, 'dn_dEa': 7.503351470832472e-06, 'name': 'H + C10H21-5 <=> C10H22-10'}]
""",
)

entry(
    index = 125,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(3.56381e+06,'m^3/(mol*s)'), n=-0.0535546, w0=(152600,'J/mol'), E0=(15260,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0261245836817, var=0.43760691139, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R
        Total Standard Deviation in ln(k): 1.39180927994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R
Total Standard Deviation in ln(k): 1.39180927994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R
Total Standard Deviation in ln(k): 1.39180927994
sensitivities = [{'dA': -7.374612920330849e-06, 'dE0': 0.0, 'dn': 0.006177663854126996, 'dA_dEa': 0.0020070554818121247, 'dE0_dEa': 0.0, 'dn_dEa': -0.0059870920169478115, 'name': '1-hydroxybutyl + O2 <=> 1-hydroxybutylO2'}, {'dA': 0.02477337462458979, 'dE0': 0.0, 'dn': 0.0061785976187080805, 'dA_dEa': -0.0347575450607745, 'dE0_dEa': 0.0, 'dn_dEa': 0.11599158788974617, 'name': 'O2 + C6H5 <=> C6H5O2'}, {'dA': 0.32301312916519725, 'dE0': 0.0, 'dn': 0.0029481174788823887, 'dA_dEa': 0.7999502781289352, 'dE0_dEa': 0.0, 'dn_dEa': -2.6542515319558775, 'name': 'O2 + C6H5 <=> C6H5O2'}, {'dA': 0.3232401461908197, 'dE0': 0.0, 'dn': 0.0021030349862450406, 'dA_dEa': 1.32347208076148, 'dE0_dEa': 0.0, 'dn_dEa': -4.390590795952461, 'name': 'O2 + C10H7 <=> C10H7O2'}, {'dA': 0.3239232381489289, 'dE0': 0.0, 'dn': -0.0004399376077799474, 'dA_dEa': 0.8933554641786674, 'dE0_dEa': 0.0, 'dn_dEa': -2.963892187395326, 'name': 'O2 + C10H7-2 <=> C10H7O2-2'}]
""",
)

entry(
    index = 126,
    label = "Root_N-1R->H_1CNOS->N_Ext-1N-R",
    kinetics = ArrheniusBM(A=(6.74236e+06,'m^3/(mol*s)'), n=0.142499, w0=(77250,'J/mol'), E0=(7725,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0607054911525, var=1.94482475529, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_1CNOS->N_Ext-1N-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-1N-R
        Total Standard Deviation in ln(k): 2.94826923214"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-1N-R
Total Standard Deviation in ln(k): 2.94826923214""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-1N-R
Total Standard Deviation in ln(k): 2.94826923214
sensitivities = [{'dA': 0.08932851682531424, 'dE0': 0.0, 'dn': 1.5971030114202266e-05, 'dA_dEa': -2.0176638661821844, 'dE0_dEa': 0.0, 'dn_dEa': 0.6701252516732507, 'name': '[CH3] + [O-][N+]=O <=> CH3NO2'}, {'dA': 0.08929595643537443, 'dE0': 0.0, 'dn': 2.8127843269801518e-05, 'dA_dEa': -0.2807834079004177, 'dE0_dEa': 0.0, 'dn_dEa': 0.09325596245939982, 'name': 'CH3 + NHNH2 <=> CH3NHNH2'}, {'dA': 0.8042567571796331, 'dE0': 0.0, 'dn': 3.192168147930559e-05, 'dA_dEa': -3.902044554138658e-05, 'dE0_dEa': 0.0, 'dn_dEa': 1.4549363586633512e-05, 'name': 'NO2 + OH <=> HNO3'}, {'dA': 0.016377470503316643, 'dE0': 0.0, 'dn': 1.4050113571427166e-05, 'dA_dEa': -3.902044554138658e-05, 'dE0_dEa': 0.0, 'dn_dEa': 1.4549363586633512e-05, 'name': 'NO2 + OH <=> HNO3'}]
""",
)

entry(
    index = 127,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(106477,'m^3/(mol*s)'), n=0.348287, w0=(140789,'J/mol'), E0=(14078.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0108230153501, var=2.70964383578, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R
        Total Standard Deviation in ln(k): 3.32718707999"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R
Total Standard Deviation in ln(k): 3.32718707999""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R
Total Standard Deviation in ln(k): 3.32718707999
sensitivities = [{'dA': -0.0590077849445046, 'dE0': -0.002101894828443318, 'dn': -0.010224618269790138, 'dA_dEa': -0.04602039551571631, 'dE0_dEa': -0.0011709098133372896, 'dn_dEa': -0.007839551903093885, 'name': '[O][O] + C[CH2] <=> C2H5O2'}, {'dA': -0.059734783217641946, 'dE0': -0.0021274326870738473, 'dn': -0.010348111315071202, 'dA_dEa': -0.04451902304226032, 'dE0_dEa': -0.0010390136172538445, 'dn_dEa': -0.007587286760289872, 'name': '[O][O] + [CH2]CC <=> C3H7O2'}, {'dA': -0.048928401415798524, 'dE0': -0.0017480922179891512, 'dn': -0.008512294688734644, 'dA_dEa': -0.04792470049608783, 'dE0_dEa': -0.0017617699519827086, 'dn_dEa': -0.008144516596516847, 'name': '1-hydroxybutyl + O2 <=> 1-hydroxybutylO2'}, {'dA': -0.9939582913603957, 'dE0': -0.03614421853809469, 'dn': -0.17494731609567138, 'dA_dEa': -0.5486634576570886, 'dE0_dEa': -0.024486882681970166, 'dn_dEa': -0.09302945633438967, 'name': 'C3H3 + O2 <=> C3H3O2'}, {'dA': -1.0379486076815858, 'dE0': -0.03770280016352062, 'dn': -0.1824114789160123, 'dA_dEa': 0.8164514600893302, 'dE0_dEa': 0.038436396113864124, 'dn_dEa': 0.1383625859278886, 'name': 'C3H3-2 + O2 <=> C3H3O2-2'}, {'dA': 0.019984792384521978, 'dE0': 0.0006709324207125229, 'dn': 0.0031948991885258665, 'dA_dEa': -0.05009426141456271, 'dE0_dEa': -0.0017489085773602425, 'dn_dEa': -0.00851623631350743, 'name': 'C3H7-2 + CH3O <=> C4H10O'}, {'dA': 0.01998554750670898, 'dE0': 0.0006709476630906665, 'dn': 0.0031950346504960713, 'dA_dEa': -0.05009426141456271, 'dE0_dEa': -0.0017489085773602425, 'dn_dEa': -0.00851623631350743, 'name': 'C4H9 + CH3O <=> C5H12O'}, {'dA': -0.055492026547205316, 'dE0': -0.0019784939105555377, 'dn': -0.009627342994387611, 'dA_dEa': -0.05009426141456271, 'dE0_dEa': -0.0017489085773602425, 'dn_dEa': -0.00851623631350743, 'name': 'CH3O + CH3O <=> C2H6O2'}, {'dA': -0.059006809912893594, 'dE0': -0.0021018759231740867, 'dn': -0.010224442895730495, 'dA_dEa': -0.05009426141456271, 'dE0_dEa': -0.0017489085773602425, 'dn_dEa': -0.00851623631350743, 'name': 'O2 + C2H5 <=> C2H5O2-2'}, {'dA': -0.06075416630580535, 'dE0': -0.002163211293489813, 'dn': -0.010521290091769478, 'dA_dEa': -0.05009426141456271, 'dE0_dEa': -0.0017489085773602425, 'dn_dEa': -0.00851623631350743, 'name': 'O2 + C3H7-2 <=> C3H7O2-2'}, {'dA': -0.056659808080900674, 'dE0': -0.0020194799523147833, 'dn': -0.009825733258194287, 'dA_dEa': -0.05009426141456271, 'dE0_dEa': -0.0017489085773602425, 'dn_dEa': -0.00851623631350743, 'name': 'O2 + C4H9 <=> C4H9O2'}, {'dA': -0.03688276615321635, 'dE0': -0.0013252622858737507, 'dn': -0.006465942457844436, 'dA_dEa': -0.05009426141456271, 'dE0_dEa': -0.0017489085773602425, 'dn_dEa': -0.00851623631350743, 'name': 'O2 + C2H3 <=> C2H3O2'}, {'dA': 0.1907878820510899, 'dE0': 0.006064908320176554, 'dn': 0.029299707540383052, 'dA_dEa': -0.10798729855566815, 'dE0_dEa': -0.002977516347628246, 'dn_dEa': -0.01837972474160972, 'name': 'O2 + C6H5 <=> C6H5O2'}, {'dA': -0.05400982294646068, 'dE0': -0.001926476095467523, 'dn': -0.00937553437163342, 'dA_dEa': -0.05009426141456271, 'dE0_dEa': -0.0017489085773602425, 'dn_dEa': -0.00851623631350743, 'name': 'O2 + CHO <=> CHO3'}, {'dA': -0.05525640404258678, 'dE0': -0.0019702227228452817, 'dn': -0.009587314844857486, 'dA_dEa': -0.05009426141456271, 'dE0_dEa': -0.0017489085773602425, 'dn_dEa': -0.00851623631350743, 'name': 'O2 + C2H3O <=> C2H3O3'}, {'dA': 2.574568326327692, 'dE0': 0.0825048827605009, 'dn': 0.3993315142037806, 'dA_dEa': 1.2525051365594166, 'dE0_dEa': 0.02454139490414037, 'dn_dEa': 0.21347375466438998, 'name': 'O2 + C6H5 <=> C6H5O2'}, {'dA': 2.574175333048884, 'dE0': 0.08249849550373013, 'dn': 0.39926008856399636, 'dA_dEa': 2.1027754860585373, 'dE0_dEa': 0.041645432074132537, 'dn_dEa': 0.3583680156062497, 'name': 'O2 + C10H7 <=> C10H7O2'}, {'dA': 2.5746555272941403, 'dE0': 0.08251024005304093, 'dn': 0.39934487837521004, 'dA_dEa': 1.4034812542186739, 'dE0_dEa': 0.027577717057399073, 'dn_dEa': 0.23919011171859647, 'name': 'O2 + C10H7-2 <=> C10H7O2-2'}, {'dA': -5.249900124220242, 'dE0': -0.19218031647052883, 'dn': -0.9299059073366791, 'dA_dEa': -2.3057432566384914, 'dE0_dEa': -0.11388949939172702, 'dn_dEa': -0.3905229984950958, 'name': 'O2 + C7H7 <=> C7H7O2'}]
""",
)

entry(
    index = 128,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(8.92033e+06,'m^3/(mol*s)'), n=1.17885e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0370545850026, var=0.142813102216, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R
        Total Standard Deviation in ln(k): 0.850703803965"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R
Total Standard Deviation in ln(k): 0.850703803965""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R
Total Standard Deviation in ln(k): 0.850703803965
sensitivities = [{'dA': 0.11406459683983718, 'dE0': 0.0, 'dn': -8.508805421461391e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C6H5 + C3H3 <=> C9H8'}, {'dA': 0.11406459684338989, 'dE0': 0.0, 'dn': -8.508804767314267e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C6H5 + C3H3-2 <=> C9H8-2'}, {'dA': 0.05814700876172837, 'dE0': 0.0, 'dn': -1.784604304000099e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C6H5 + C6H5 <=> C12H10'}, {'dA': 0.7129521078859898, 'dE0': 0.0, 'dn': -3.980899894882715e-05, 'dA_dEa': 1.5346386190417418, 'dE0_dEa': 0.0, 'dn_dEa': 0.37504108752424925, 'name': 'C6H5 + C6H5 <=> C12H10'}]
""",
)

entry(
    index = 129,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_N-1CS->C_Ext-1S-R",
    kinetics = ArrheniusBM(A=(9.40412e+06,'m^3/(mol*s)'), n=0.634469, w0=(113000,'J/mol'), E0=(11300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_N-1CS->C_Ext-1S-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_N-1CS->C_Ext-1S-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_N-1CS->C_Ext-1S-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_N-1CS->C_Ext-1S-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3S + CH3S <=> C2H6S2'}]
""",
)

entry(
    index = 130,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_3R!H->O",
    kinetics = ArrheniusBM(A=(9.10287e+13,'m^3/(mol*s)'), n=-2.74437, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_3R!H->O
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_3R!H->O
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_3R!H->O
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'H + CHO <=> CH2O'}]
""",
)

entry(
    index = 131,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.51e+07,'m^3/(mol*s)'), n=2.42855e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_N-4R!H->C
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'CHO + CHO <=> C2H2O2'}]
""",
)

entry(
    index = 132,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(3.24036e+06,'m^3/(mol*s)'), n=3.5707e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.50055194392e-09, var=0.0475248579916, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R
        Total Standard Deviation in ln(k): 0.437036213272"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 0.437036213272""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 0.437036213272
sensitivities = [{'dA': 0.5111732575429636, 'dE0': 0.0, 'dn': -6129.386952926135, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'O2 + C2H3 <=> C2H3O2'}, {'dA': 0.47693802106612815, 'dE0': 0.0, 'dn': 11693.591415943534, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'O2 + CHO <=> CHO3'}]
""",
)

entry(
    index = 133,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R_Ext-2CN-R",
    kinetics = ArrheniusBM(A=(1.62598e+07,'m^3/(mol*s)'), n=0.255122, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00414786628487, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R_Ext-2CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R_Ext-2CN-R
        Total Standard Deviation in ln(k): 0.0104217745851"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R_Ext-2CN-R
Total Standard Deviation in ln(k): 0.0104217745851""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_Ext-2CN-R_Ext-2CN-R
Total Standard Deviation in ln(k): 0.0104217745851
sensitivities = [{'dA': 0.49977825355546024, 'dE0': 0.0, 'dn': -1.6320567031129823e-05, 'dA_dEa': -0.24245392225810575, 'dE0_dEa': 0.0, 'dn_dEa': 0.12552159335119625, 'name': 'H + C5H9 <=> C5H10'}, {'dA': 0.49977825355546024, 'dE0': 0.0, 'dn': -1.6320566915647483e-05, 'dA_dEa': -0.24245392225810575, 'dE0_dEa': 0.0, 'dn_dEa': 0.1255215933514272, 'name': 'H + C6H9 <=> C6H10'}]
""",
)

entry(
    index = 134,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O",
    kinetics = ArrheniusBM(A=(590543,'m^3/(mol*s)'), n=0.538327, w0=(171033,'J/mol'), E0=(17103.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0201293645259, var=3.62478427822, Tref=1000.0, N=61, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O
        Total Standard Deviation in ln(k): 3.86736459191"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O
Total Standard Deviation in ln(k): 3.86736459191""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O
Total Standard Deviation in ln(k): 3.86736459191
sensitivities = [{'dA': 0.00561431369661198, 'dE0': 0.0, 'dn': -9.492514192221442e-05, 'dA_dEa': 0.010599537597856314, 'dE0_dEa': 0.0, 'dn_dEa': -0.0022391532137068216, 'name': 'C5H5 + C2H5 <=> C7H10'}, {'dA': 0.014878302094347125, 'dE0': 0.0, 'dn': -9.448353502396159e-05, 'dA_dEa': -0.007253220367432167, 'dE0_dEa': 0.0, 'dn_dEa': 0.001514880089613155, 'name': 'CH3 + CH3 <=> C2H6'}, {'dA': 0.014882853561106165, 'dE0': 0.0, 'dn': -9.555903865834334e-05, 'dA_dEa': -0.0007585406045508006, 'dE0_dEa': 0.0, 'dn_dEa': 0.00014914990266980496, 'name': 'CH3 + C2H5 <=> C3H8'}, {'dA': 0.014880738701707448, 'dE0': 0.0, 'dn': -9.50595595203008e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C2H5 <=> C4H10'}, {'dA': 0.014878105321970954, 'dE0': 0.0, 'dn': -9.443696132572992e-05, 'dA_dEa': 0.0002854364247184863, 'dE0_dEa': 0.0, 'dn_dEa': -7.026644851298265e-05, 'name': 'C5H5 + CH3 <=> C6H8'}, {'dA': 0.014877292603189792, 'dE0': 0.0, 'dn': -9.424519999888917e-05, 'dA_dEa': 0.0356647280703765, 'dE0_dEa': 0.0, 'dn_dEa': -0.007509827186465674, 'name': '[SH] + [SH] <=> HSSH'}, {'dA': 0.005608799819257278, 'dE0': 0.0, 'dn': -9.362527193887798e-05, 'dA_dEa': -0.008876600393393642, 'dE0_dEa': 0.0, 'dn_dEa': 0.0018563264591545633, 'name': 'C3H3 + C7H7 <=> C10H10'}, {'dA': 0.00561673594567997, 'dE0': 0.0, 'dn': -9.549719161031997e-05, 'dA_dEa': -0.02395672656696754, 'dE0_dEa': 0.0, 'dn_dEa': 0.005026832679385865, 'name': 'C3H3-2 + C7H7 <=> C10H10-2'}, {'dA': 0.005615008211279978, 'dE0': 0.0, 'dn': -9.508887415315758e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C6H5 + C3H3 <=> C9H8'}, {'dA': 0.005615008211279978, 'dE0': 0.0, 'dn': -9.508887415315758e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C6H5 + C3H3-2 <=> C9H8-2'}, {'dA': 0.0005692124283030525, 'dE0': 0.0, 'dn': -9.510026462599261e-05, 'dA_dEa': 0.0010720391543374078, 'dE0_dEa': 0.0, 'dn_dEa': -0.00023578233365715808, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}, {'dA': 0.0005692374394073512, 'dE0': 0.0, 'dn': -9.510619775804122e-05, 'dA_dEa': 0.000839308164302203, 'dE0_dEa': 0.0, 'dn_dEa': -0.00018684217463889468, 'name': 'C3H3 + C3H3-2 <=> C6H6-2'}, {'dA': 0.0005691609761271992, 'dE0': 0.0, 'dn': -9.508814958460295e-05, 'dA_dEa': 0.0006002220409585086, 'dE0_dEa': 0.0, 'dn_dEa': -0.0001365684743999825, 'name': 'C3H3 + C3H3 <=> C6H6-3'}, {'dA': 0.014879483149600721, 'dE0': 0.0, 'dn': -9.476251943311505e-05, 'dA_dEa': 0.1288911935013601, 'dE0_dEa': 0.0, 'dn_dEa': -0.02711298881325987, 'name': 'CH3 + C3H3-2 <=> C4H6'}, {'dA': 0.005615056439368168, 'dE0': 0.0, 'dn': -9.510032447513008e-05, 'dA_dEa': 0.0042984840167297495, 'dE0_dEa': 0.0, 'dn_dEa': -0.0009142226929667955, 'name': 'C6H5 + CH3 <=> C7H8'}, {'dA': 0.003062251746399962, 'dE0': 0.0, 'dn': -9.510818159747589e-05, 'dA_dEa': -0.010002299305257303, 'dE0_dEa': 0.0, 'dn_dEa': 0.00209287236142828, 'name': 'CH3 + CH3 <=> C2H6-3'}, {'dA': 0.0005692118314471544, 'dE0': 0.0, 'dn': -9.510015956167604e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'CH3 + C2H5 <=> C3H8-3'}, {'dA': 0.0005692931690504737, 'dE0': 0.0, 'dn': -9.511937488710249e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'CH3 + C3H7-2 <=> C4H10-2'}, {'dA': 0.0005691975424327383, 'dE0': 0.0, 'dn': -9.509679656547153e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'CH3 + C4H9 <=> C5H12'}, {'dA': 0.0030618478881198107, 'dE0': 0.0, 'dn': -9.50128738160031e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'CH3 + C2H3 <=> C3H6'}, {'dA': 0.0030623931550625193, 'dE0': 0.0, 'dn': -9.514154608450675e-05, 'dA_dEa': -7.562016079988022e-05, 'dE0_dEa': 0.0, 'dn_dEa': 5.5434847081127566e-06, 'name': 'CH3 + C6H5 <=> C7H8-5'}, {'dA': 0.0005692100870647381, 'dE0': 0.0, 'dn': -9.50997464337741e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'CH3 + CHO <=> C2H4O'}, {'dA': 0.0005692093285603677, 'dE0': 0.0, 'dn': -9.509956876251018e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'CH3 + C2H3O <=> C3H6O'}, {'dA': 0.0005692167590610269, 'dE0': 0.0, 'dn': -9.51013195842999e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C2H5 + C2H5 <=> C4H10-3'}, {'dA': 0.0005691627382731839, 'dE0': 0.0, 'dn': -9.508856440103855e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C2H5 + C3H7-2 <=> C5H12-2'}, {'dA': 0.0005692868487728391, 'dE0': 0.0, 'dn': -9.511793869541795e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.0005692100870647381, 'dE0': 0.0, 'dn': -9.50997464337741e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C2H5 + CHO <=> C3H6O-2'}, {'dA': 0.0005692650351108513, 'dE0': 0.0, 'dn': -9.511273988789622e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C2H5 + C2H3O <=> C4H8O'}, {'dA': 0.0005691330553503975, 'dE0': 0.0, 'dn': -9.508154873129957e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C3H7-2 + C3H7-2 <=> C6H14-2'}, {'dA': 0.0005688907265267234, 'dE0': 0.0, 'dn': -9.502440781419915e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C3H7-2 + C4H9 <=> C7H16'}, {'dA': 0.000569142805773089, 'dE0': 0.0, 'dn': -9.50839479500144e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C3H7-2 + C2H3O <=> C5H10O'}, {'dA': 0.000568679315193839, 'dE0': 0.0, 'dn': -9.49748506646066e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C4H9 + C4H9 <=> C8H18'}, {'dA': 0.000569230937941319, 'dE0': 0.0, 'dn': -9.510466850939056e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C4H9 + CHO <=> C5H10O-2'}, {'dA': 0.0005690899929078968, 'dE0': 0.0, 'dn': -9.507134304624871e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C4H9 + C2H3O <=> C6H12O'}, {'dA': 0.000569189836596769, 'dE0': 0.0, 'dn': -9.509496750828896e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C2H3 + C2H3 <=> C4H6-4'}, {'dA': 0.0030627525724472625, 'dE0': 0.0, 'dn': -9.522631347603448e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C2H3 + C2H <=> C4H4'}, {'dA': 0.0005692100870647381, 'dE0': 0.0, 'dn': -9.50997464337741e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C2H3 + CHO <=> C3H4O'}, {'dA': 0.003063410153103856, 'dE0': 0.0, 'dn': -9.538108278269993e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C6H5 + C6H5 <=> C12H10'}, {'dA': 0.0030631100109704866, 'dE0': 0.0, 'dn': -9.531063453183163e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'CHO + CHO <=> C2H2O2'}, {'dA': 0.0005692100870647381, 'dE0': 0.0, 'dn': -9.50997464337741e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'CHO + C2H3O <=> C3H4O2'}, {'dA': 0.000569230937941319, 'dE0': 0.0, 'dn': -9.510466850939056e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C2H3O + C2H3O <=> C4H6O2'}, {'dA': 0.0005692650972833407, 'dE0': 0.0, 'dn': -9.511271925026261e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C4H9 <=> C5H12'}, {'dA': 0.0005692554339021343, 'dE0': 0.0, 'dn': -9.511044742203164e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'CH3 + C3H7-2 <=> C4H10-2'}, {'dA': 0.0005692912292688051, 'dE0': 0.0, 'dn': -9.51188596967216e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C2H5 + C3H7-2 <=> C5H12-2'}, {'dA': 0.0005687613473526825, 'dE0': 0.0, 'dn': -9.49939811881204e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.13070712045860963, 'dE0': 0.0, 'dn': -9.580851988171476e-05, 'dA_dEa': 0.37770430863308385, 'dE0_dEa': 0.0, 'dn_dEa': -0.07943209997986661, 'name': 'HSS + CH3 <=> CH4S2'}, {'dA': 0.13042240707152092, 'dE0': 0.0, 'dn': -2.8626316181728362e-05, 'dA_dEa': 0.4850096238744862, 'dE0_dEa': 0.0, 'dn_dEa': -0.10200176487961207, 'name': 'CH3S + CH3S <=> C2H6S2'}, {'dA': 0.13070712045860963, 'dE0': 0.0, 'dn': -9.580851988171476e-05, 'dA_dEa': 0.3777043086472947, 'dE0_dEa': 0.0, 'dn_dEa': -0.07943209998305606, 'name': 'HSS + C4H9 <=> C4H10S2'}, {'dA': 0.130672327109963, 'dE0': 0.0, 'dn': -8.76023477978045e-05, 'dA_dEa': 0.6734426773303457, 'dE0_dEa': 0.0, 'dn_dEa': -0.14161887072117668, 'name': 'CH3S + C2H5 <=> C3H8S'}, {'dA': 0.130672327109963, 'dE0': 0.0, 'dn': -8.76023477978045e-05, 'dA_dEa': 0.6734426773303457, 'dE0_dEa': 0.0, 'dn_dEa': -0.14161887072117668, 'name': 'CH3S + CH3 <=> C2H6S'}, {'dA': 0.13067232711173934, 'dE0': 0.0, 'dn': -8.760234836064906e-05, 'dA_dEa': 0.673442677326793, 'dE0_dEa': 0.0, 'dn_dEa': -0.1416188707202386, 'name': 'CH3S + C4H9 <=> C5H12S'}, {'dA': 0.000569153733920365, 'dE0': 0.0, 'dn': -9.50864345972498e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C3H5 <=> C6H10-2'}, {'dA': 0.0005692120783607551, 'dE0': 0.0, 'dn': -9.510021809750956e-05, 'dA_dEa': 0.00048753981118926186, 'dE0_dEa': 0.0, 'dn_dEa': -0.00011287394909455208, 'name': 'C3H5 + C2H5 <=> C5H10-2'}, {'dA': 0.0005692046887163032, 'dE0': 0.0, 'dn': -9.509847365462479e-05, 'dA_dEa': 0.0004875536117055472, 'dE0_dEa': 0.0, 'dn_dEa': -0.00011287721340534495, 'name': 'C3H5 + CH3 <=> C4H8-2'}, {'dA': 0.0005691911884043238, 'dE0': 0.0, 'dn': -9.509530465217623e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C3H7-2 <=> C6H12'}, {'dA': 0.000569523894711273, 'dE0': 0.0, 'dn': -9.517377475122954e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C4H9 <=> C7H14'}, {'dA': 0.000569153733920365, 'dE0': 0.0, 'dn': -9.50864345972498e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C5H7 <=> C8H12'}, {'dA': 0.0030637349013321645, 'dE0': 0.0, 'dn': -9.545866283689998e-05, 'dA_dEa': 0.011113794519347468, 'dE0_dEa': 0.0, 'dn_dEa': -0.00234713338569573, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}, {'dA': 0.0005693036282395441, 'dE0': 0.0, 'dn': -9.51217538434134e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C3H3-2 + CH3 <=> C4H6-5'}, {'dA': 0.003062164894985013, 'dE0': 0.0, 'dn': -9.508772519980995e-05, 'dA_dEa': -0.004799613831707989, 'dE0_dEa': 0.0, 'dn_dEa': 0.0009988789772912164, 'name': 'C5H5 + CH3 <=> C6H8'}, {'dA': 0.0005692226867638, 'dE0': 0.0, 'dn': -9.510272144246669e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C5H5 + C5H5 <=> C10H10-6'}, {'dA': 0.03298466514856466, 'dE0': 0.0, 'dn': -9.660809685378496e-05, 'dA_dEa': 0.07050982724977284, 'dE0_dEa': 0.0, 'dn_dEa': -0.014836809297234192, 'name': 'C6H5 + C6H5 <=> C12H10'}, {'dA': 0.0030622128850413865, 'dE0': 0.0, 'dn': -9.509902693082044e-05, 'dA_dEa': 0.00040301262771440526, 'dE0_dEa': 0.0, 'dn_dEa': -9.510043910780407e-05, 'name': 'C11H23 + CH3 <=> C12H26'}, {'dA': 0.0030637780703560756, 'dE0': 0.0, 'dn': -9.546807022075976e-05, 'dA_dEa': 0.00041329883870848795, 'dE0_dEa': 0.0, 'dn_dEa': -9.72599496444603e-05, 'name': 'C10H21 + C2H5 <=> C12H26-2'}, {'dA': 0.0030616327926228414, 'dE0': 0.0, 'dn': -9.496244069267115e-05, 'dA_dEa': 0.00035925885732983125, 'dE0_dEa': 0.0, 'dn_dEa': -8.584553021269199e-05, 'name': 'C9H19 + C3H7 <=> C12H26-3'}, {'dA': 0.003063334261810606, 'dE0': 0.0, 'dn': -9.536378300490237e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C8H17 + C4H9-2 <=> C12H26-4'}, {'dA': 0.0030627841596245807, 'dE0': 0.0, 'dn': -9.523355297029072e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C7H15 + C5H11 <=> C12H26-5'}, {'dA': 0.003062063303361011, 'dE0': 0.0, 'dn': -9.506383469991096e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H13 + C6H13 <=> C12H26-6'}, {'dA': 0.0030622184361565096, 'dE0': 0.0, 'dn': -9.510032053521822e-05, 'dA_dEa': 0.00047587882967553254, 'dE0_dEa': 0.0, 'dn_dEa': -0.00011042308545207415, 'name': 'CH3 + C9H19 <=> C10H22'}, {'dA': 0.0030627615128512352, 'dE0': 0.0, 'dn': -9.522837498801746e-05, 'dA_dEa': 0.0006520366877538926, 'dE0_dEa': 0.0, 'dn_dEa': -0.00014744550692544518, 'name': 'C8H17 + C2H5 <=> C10H22-2'}, {'dA': 0.0030624750149147494, 'dE0': 0.0, 'dn': -9.516094227064959e-05, 'dA_dEa': 0.00048642282735050584, 'dE0_dEa': 0.0, 'dn_dEa': -0.00011264381827929984, 'name': 'C7H15 + C3H7 <=> C10H22-3'}, {'dA': 0.0030635806798077246, 'dE0': 0.0, 'dn': -9.542216687039078e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H13 + C4H9-2 <=> C10H22-4'}, {'dA': 0.0030620156401542963, 'dE0': 0.0, 'dn': -9.505249619638967e-05, 'dA_dEa': 0.000413035602164814, 'dE0_dEa': 0.0, 'dn_dEa': -9.719822004333368e-05, 'name': 'C5H11 + C5H11 <=> C10H22-5'}, {'dA': 0.003055312232547517, 'dE0': 0.0, 'dn': -9.347059568917862e-05, 'dA_dEa': -0.008091559259072238, 'dE0_dEa': 0.0, 'dn_dEa': 0.0016911915925686529, 'name': 'CH3 + C7H15-2 <=> C8H18-2'}, {'dA': 0.003058550486656823, 'dE0': 0.0, 'dn': -9.423456992904532e-05, 'dA_dEa': 0.017372108045423353, 'dE0_dEa': 0.0, 'dn_dEa': -0.003663220322088639, 'name': 'C4H9-3 + C4H9 <=> C8H18-3'}, {'dA': 0.0030680337932412808, 'dE0': 0.0, 'dn': -9.64720179261928e-05, 'dA_dEa': 0.02117335479035154, 'dE0_dEa': 0.0, 'dn_dEa': -0.0044626106680380855, 'name': 'C5H11-2 + C3H7-2 <=> C8H18-4'}, {'dA': 0.003057306356524573, 'dE0': 0.0, 'dn': -9.394167688052647e-05, 'dA_dEa': 0.022835261464851115, 'dE0_dEa': 0.0, 'dn_dEa': -0.004811990331367193, 'name': 'C7H15-3 + CH3 <=> C8H18-5'}]
""",
)

entry(
    index = 135,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_2R-inRing",
    kinetics = ArrheniusBM(A=(5.7e+06,'m^3/(mol*s)'), n=1.36803e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_2R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_2R-inRing
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_2R-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_2R-inRing
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.07536757559024329, 'dE0': 0.0, 'dn': -1.407329577477925e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C6H5 + C6H5 <=> C12H10'}, {'dA': 0.9241204835178559, 'dE0': 0.0, 'dn': 1.1456302630135368e-05, 'dA_dEa': 1.9887618874430104, 'dE0_dEa': 0.0, 'dn_dEa': 0.375062676581836, 'name': 'C6H5 + C6H5 <=> C12H10'}]
""",
)

entry(
    index = 136,
    label = "Root_N-1R->H_N-1CNOS->N",
    kinetics = ArrheniusBM(A=(388820,'m^3/(mol*s)'), n=0.540123, w0=(156753,'J/mol'), E0=(-102376,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0275389427923, var=4.36991544586, Tref=1000.0, N=89, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N
        Total Standard Deviation in ln(k): 4.25996023581"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N
Total Standard Deviation in ln(k): 4.25996023581""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N
Total Standard Deviation in ln(k): 4.25996023581
sensitivities = [{'dA': 0.00033534679566575104, 'dE0': -0.0, 'dn': -4.368195849157989e-05, 'dA_dEa': -0.0010408074651026037, 'dE0_dEa': -0.0, 'dn_dEa': 0.0002072699834147432, 'name': '[O][O] + [CH3] <=> CH3O2'}, {'dA': 0.0003357709914553567, 'dE0': -0.0, 'dn': -4.377881991755707e-05, 'dA_dEa': -0.0013520084500841347, 'dE0_dEa': -0.0, 'dn_dEa': 0.0002705603929047696, 'name': '[O][O] + C[CH2] <=> C2H5O2'}, {'dA': 0.0003352434916337557, 'dE0': -0.0, 'dn': -4.365843342336765e-05, 'dA_dEa': -0.0016343052955393868, 'dE0_dEa': -0.0, 'dn_dEa': 0.00032800753227905146, 'name': '[O][O] + [CH2]CC <=> C3H7O2'}, {'dA': 0.0003354676998413112, 'dE0': -0.0, 'dn': -4.3709601422289525e-05, 'dA_dEa': 0.000509248764046844, 'dE0_dEa': -0.0, 'dn_dEa': -0.00010804815828855263, 'name': '1-hydroxybutyl + O2 <=> 1-hydroxybutylO2'}, {'dA': 0.004662134191591408, 'dE0': -0.0, 'dn': -4.379065151225383e-05, 'dA_dEa': 0.008936495055068423, 'dE0_dEa': -0.0, 'dn_dEa': -0.0018223353334224969, 'name': 'C5H5 + C2H5 <=> C7H10'}, {'dA': 0.012606165618934961, 'dE0': -0.0, 'dn': -4.367076232691678e-05, 'dA_dEa': -0.0063699940504598285, 'dE0_dEa': -0.0, 'dn_dEa': 0.0012913524742491139, 'name': 'CH3 + CH3 <=> C2H6'}, {'dA': 0.012606048370501777, 'dE0': -0.0, 'dn': -4.3644086244475995e-05, 'dA_dEa': -0.0008031163805100935, 'dE0_dEa': -0.0, 'dn_dEa': 0.00015892300743591746, 'name': 'CH3 + C2H5 <=> C3H8'}, {'dA': 0.012598208980919845, 'dE0': -0.0, 'dn': -4.1852119462718335e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C2H5 <=> C4H10'}, {'dA': 0.01260289871041348, 'dE0': -0.0, 'dn': -4.292521468238405e-05, 'dA_dEa': 9.633609820981443e-05, 'dE0_dEa': -0.0, 'dn_dEa': -2.406578105596339e-05, 'name': 'C5H5 + CH3 <=> C6H8'}, {'dA': 0.012613303203680428, 'dE0': -0.0, 'dn': -4.530031112297923e-05, 'dA_dEa': -0.1355677965691065, 'dE0_dEa': -0.0, 'dn_dEa': 0.02757283976058091, 'name': '[SH] + [O][O] <=> HSOO'}, {'dA': 0.004661502154946165, 'dE0': -0.0, 'dn': -4.364617131166438e-05, 'dA_dEa': 0.003689364790560441, 'dE0_dEa': -0.0, 'dn_dEa': -0.0007549287567563582, 'name': 'OH + NO2-2 <=> HOONO'}, {'dA': 0.012602048029110302, 'dE0': -0.0, 'dn': -4.272816821009946e-05, 'dA_dEa': 0.03041639202372772, 'dE0_dEa': -0.0, 'dn_dEa': -0.006191601439509701, 'name': '[SH] + [SH] <=> HSSH'}, {'dA': 0.004662454598403601, 'dE0': -0.0, 'dn': -4.386383250637729e-05, 'dA_dEa': -0.007758000551306454, 'dE0_dEa': -0.0, 'dn_dEa': 0.0015736820686471184, 'name': 'C3H3 + C7H7 <=> C10H10'}, {'dA': 0.004662078747941736, 'dE0': -0.0, 'dn': -4.3777602236867056e-05, 'dA_dEa': -0.02070418126010282, 'dE0_dEa': -0.0, 'dn_dEa': 0.004207231498690288, 'name': 'C3H3-2 + C7H7 <=> C10H10-2'}, {'dA': 0.00466162160073276, 'dE0': -0.0, 'dn': -4.36734087723097e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C6H5 + C3H3 <=> C9H8'}, {'dA': 0.00466162160073276, 'dE0': -0.0, 'dn': -4.36734087723097e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C6H5 + C3H3-2 <=> C9H8-2'}, {'dA': 0.004665124386349875, 'dE0': -0.0, 'dn': -4.447134917493799e-05, 'dA_dEa': 0.01880176609070568, 'dE0_dEa': -0.0, 'dn_dEa': -0.003829209853799089, 'name': 'C3H3 + O2 <=> C3H3O2'}, {'dA': 0.004663646242520317, 'dE0': -0.0, 'dn': -4.413269455143626e-05, 'dA_dEa': -0.0345792227172164, 'dE0_dEa': -0.0, 'dn_dEa': 0.0070294818332027435, 'name': 'C3H3-2 + O2 <=> C3H3O2-2'}, {'dA': 0.0003353651294446905, 'dE0': -0.0, 'dn': -4.368614786491226e-05, 'dA_dEa': 0.0007663886343324001, 'dE0_dEa': -0.0, 'dn_dEa': -0.00016035255240551987, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}, {'dA': 0.0003352971020831688, 'dE0': -0.0, 'dn': -4.367058790581929e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H3 + C3H3-2 <=> C6H6-2'}, {'dA': 0.00033528410625653177, 'dE0': -0.0, 'dn': -4.3667633274137564e-05, 'dA_dEa': 0.0003619090289675285, 'dE0_dEa': -0.0, 'dn_dEa': -7.807209493048583e-05, 'name': 'C3H3 + C3H3 <=> C6H6-3'}, {'dA': 0.012609518492469331, 'dE0': -0.0, 'dn': -4.4436530113788396e-05, 'dA_dEa': 0.1103615682041103, 'dE0_dEa': -0.0, 'dn_dEa': -0.022454426376320686, 'name': 'CH3 + C3H3-2 <=> C4H6'}, {'dA': 0.004661403293582625, 'dE0': -0.0, 'dn': -4.362365973711334e-05, 'dA_dEa': 0.0035324993952205457, 'dE0_dEa': -0.0, 'dn_dEa': -0.0007230313871110048, 'name': 'C6H5 + CH3 <=> C7H8'}, {'dA': 0.002472808354525841, 'dE0': -0.0, 'dn': -4.367182500696449e-05, 'dA_dEa': -0.008728910456668865, 'dE0_dEa': -0.0, 'dn_dEa': 0.001771194121842305, 'name': 'CH3 + CH3 <=> C2H6-3'}, {'dA': 0.00033533669707711905, 'dE0': -0.0, 'dn': -4.3679655261894955e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C2H5 <=> C3H8-3'}, {'dA': 0.00033538139909698256, 'dE0': -0.0, 'dn': -4.3689853178861674e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C3H7-2 <=> C4H10-2'}, {'dA': 0.0003351925670358838, 'dE0': -0.0, 'dn': -4.3646692215462313e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C4H9 <=> C5H12'}, {'dA': 0.0024719659492691785, 'dE0': -0.0, 'dn': -4.347968229036372e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C2H3 <=> C3H6'}, {'dA': 0.0024727963925388844, 'dE0': -0.0, 'dn': -4.3669100698251256e-05, 'dA_dEa': -0.00021758259016737733, 'dE0_dEa': -0.0, 'dn_dEa': 3.980875525159939e-05, 'name': 'CH3 + C6H5 <=> C7H8-5'}, {'dA': 0.0003353319240062916, 'dE0': -0.0, 'dn': -4.367856426791259e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + CHO <=> C2H4O'}, {'dA': 0.00033533120102905795, 'dE0': -0.0, 'dn': -4.367840581877824e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C2H3O <=> C3H6O'}, {'dA': 0.0003353040884946182, 'dE0': -0.0, 'dn': -4.3672199077601265e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + OH <=> CH4O'}, {'dA': 0.00033533466314853794, 'dE0': -0.0, 'dn': -4.367918481498058e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + CH3O <=> C2H6O'}, {'dA': 0.0003353358337676951, 'dE0': -0.0, 'dn': -4.367945670135316e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C2H5 <=> C4H10-3'}, {'dA': 0.00033531826204583976, 'dE0': -0.0, 'dn': -4.367544193061787e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C3H7-2 <=> C5H12-2'}, {'dA': 0.00033520842634974596, 'dE0': -0.0, 'dn': -4.365032474807968e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.0003353319240062916, 'dE0': -0.0, 'dn': -4.367856426791259e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + CHO <=> C3H6O-2'}, {'dA': 0.00033539829580323893, 'dE0': -0.0, 'dn': -4.3693712041456744e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C2H3O <=> C4H8O'}, {'dA': 0.0003352871367212998, 'dE0': -0.0, 'dn': -4.36683641729509e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + OH <=> C2H6O-2'}, {'dA': 0.00033520385400724134, 'dE0': -0.0, 'dn': -4.364938076875806e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H7-2 + C3H7-2 <=> C6H14-2'}, {'dA': 0.0003352278241664322, 'dE0': -0.0, 'dn': -4.365485352562882e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H7-2 + C4H9 <=> C7H16'}, {'dA': 0.00033542708699489193, 'dE0': -0.0, 'dn': -4.3700285411787674e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H7-2 + C2H3O <=> C5H10O'}, {'dA': 0.00033526101361761957, 'dE0': -0.0, 'dn': -4.366234473934168e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H7-2 + CH3O <=> C4H10O'}, {'dA': 0.0003353352031610171, 'dE0': -0.0, 'dn': -4.367931367968321e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C4H9 + C4H9 <=> C8H18'}, {'dA': 0.00033533466314853794, 'dE0': -0.0, 'dn': -4.367918481498058e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C4H9 + CHO <=> C5H10O-2'}, {'dA': 0.00033549168776407046, 'dE0': -0.0, 'dn': -4.3715090514122596e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C4H9 + C2H3O <=> C6H12O'}, {'dA': 0.00033534357690715805, 'dE0': -0.0, 'dn': -4.368122414427451e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C4H9 + CH3O <=> C5H12O'}, {'dA': 0.00033527806309056413, 'dE0': -0.0, 'dn': -4.36662792872621e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H3 + C2H3 <=> C4H6-4'}, {'dA': 0.002473488732946111, 'dE0': -0.0, 'dn': -4.3827284843216714e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H3 + C2H <=> C4H4'}, {'dA': 0.0003353319240062916, 'dE0': -0.0, 'dn': -4.367856426791259e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H3 + CHO <=> C3H4O'}, {'dA': 0.0024739974229251397, 'dE0': -0.0, 'dn': -4.394328921151857e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C6H5 + C6H5 <=> C12H10'}, {'dA': 0.00247288228472114, 'dE0': -0.0, 'dn': -4.3688691218543075e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CHO + CHO <=> C2H2O2'}, {'dA': 0.0003353319240062916, 'dE0': -0.0, 'dn': -4.367856426791259e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CHO + C2H3O <=> C3H4O2'}, {'dA': 0.00033533466314853794, 'dE0': -0.0, 'dn': -4.367918481498058e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H3O + C2H3O <=> C4H6O2'}, {'dA': 0.0003353352653335065, 'dE0': -0.0, 'dn': -4.3679326747653057e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'OH + OH <=> H2O2'}, {'dA': 0.00033505669172488123, 'dE0': -0.0, 'dn': -4.361571295945177e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3O + CH3O <=> C2H6O2'}, {'dA': 0.0003353286377461387, 'dE0': -0.0, 'dn': -4.367781376714449e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C4H9 <=> C5H12'}, {'dA': 0.00033526804976706043, 'dE0': -0.0, 'dn': -4.366393431267349e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C3H7-2 <=> C4H10-2'}, {'dA': 0.0003352095472309116, 'dE0': -0.0, 'dn': -4.3650601897940116e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C3H7-2 <=> C5H12-2'}, {'dA': 0.0003351443087496278, 'dE0': -0.0, 'dn': -4.363574670172079e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.00033533208032569345, 'dE0': -0.0, 'dn': -4.3678599297331756e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'OH + CH3O <=> CH4O2'}, {'dA': 0.11190149439778263, 'dE0': -0.0, 'dn': -4.1023626872593985e-05, 'dA_dEa': 0.3236758970413335, 'dE0_dEa': -0.0, 'dn_dEa': -0.06584656268819739, 'name': 'HSS + CH3 <=> CH4S2'}, {'dA': 0.11179434426546019, 'dE0': -0.0, 'dn': -1.6482654503208533e-05, 'dA_dEa': 0.4155142064910424, 'dE0_dEa': -0.0, 'dn_dEa': -0.08452925908281672, 'name': 'CH3S + CH3S <=> C2H6S2'}, {'dA': 0.00033536240984236937, 'dE0': -0.0, 'dn': -4.368548956593139e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + CH3 <=> CH3O2-2'}, {'dA': 0.00033536240984236937, 'dE0': -0.0, 'dn': -4.368548956593139e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + C2H5 <=> C2H5O2-2'}, {'dA': 0.11190149439778263, 'dE0': -0.0, 'dn': -4.10236266910944e-05, 'dA_dEa': 0.3236758970413335, 'dE0_dEa': -0.0, 'dn_dEa': -0.06584656268819739, 'name': 'HSS + C4H9 <=> C4H10S2'}, {'dA': 0.0003352682238500307, 'dE0': -0.0, 'dn': -4.366403141494941e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + C3H7-2 <=> C3H7O2-2'}, {'dA': 0.11191969405822799, 'dE0': -0.0, 'dn': -4.517386816926603e-05, 'dA_dEa': 0.5772513461597765, 'dE0_dEa': -0.0, 'dn_dEa': -0.1174296948026575, 'name': 'CH3S + C2H5 <=> C3H8S'}, {'dA': 0.0003352996760242291, 'dE0': -0.0, 'dn': -4.36711774164589e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + C4H9 <=> C4H9O2'}, {'dA': 0.11191969405822799, 'dE0': -0.0, 'dn': -4.517386798776645e-05, 'dA_dEa': 0.5772513461597765, 'dE0_dEa': -0.0, 'dn_dEa': -0.1174296948026575, 'name': 'CH3S + CH3 <=> C2H6S'}, {'dA': 0.0003353457174171495, 'dE0': -0.0, 'dn': -4.368171310414616e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + C2H3 <=> C2H3O2'}, {'dA': 0.11191969405822799, 'dE0': -0.0, 'dn': -4.517386798776645e-05, 'dA_dEa': 0.5772513461597765, 'dE0_dEa': -0.0, 'dn_dEa': -0.1174296948026575, 'name': 'CH3S + C4H9 <=> C5H12S'}, {'dA': 0.0024734467434231414, 'dE0': -0.0, 'dn': -4.381745210340729e-05, 'dA_dEa': -0.002662161140421242, 'dE0_dEa': -0.0, 'dn_dEa': 0.0005370878836290887, 'name': 'O2 + C6H5 <=> C6H5O2'}, {'dA': 0.0003353156436958585, 'dE0': -0.0, 'dn': -4.367488363790622e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + CHO <=> CHO3'}, {'dA': 0.0003351935635720707, 'dE0': -0.0, 'dn': -4.3646957204850805e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + C2H3O <=> C2H3O3'}, {'dA': 0.000335338821599899, 'dE0': -0.0, 'dn': -4.368013659878419e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C3H5 <=> C6H10-2'}, {'dA': 0.0003353341337941998, 'dE0': -0.0, 'dn': -4.367906756625116e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C2H5 <=> C5H10-2'}, {'dA': 0.00033533084575769007, 'dE0': -0.0, 'dn': -4.367832160297258e-05, 'dA_dEa': 0.00026531858310366454, 'dE0_dEa': -0.0, 'dn_dEa': -5.8423930008685425e-05, 'name': 'C3H5 + CH3 <=> C4H8-2'}, {'dA': 0.00033528754528337285, 'dE0': -0.0, 'dn': -4.366842170831813e-05, 'dA_dEa': 0.00026531275487687447, 'dE0_dEa': -0.0, 'dn_dEa': -5.8422591630773944e-05, 'name': 'C3H5 + C3H7-2 <=> C6H12'}, {'dA': 0.0003355770630264857, 'dE0': -0.0, 'dn': -4.3734522766779645e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C4H9 <=> C7H14'}, {'dA': 0.000335338821599899, 'dE0': -0.0, 'dn': -4.368013659878419e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C5H7 <=> C8H12'}, {'dA': 0.002473117890034177, 'dE0': -0.0, 'dn': -4.3742185497596696e-05, 'dA_dEa': 0.009380780291224834, 'dE0_dEa': -0.0, 'dn_dEa': -0.0019126681920588614, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}, {'dA': 0.0003352726380967766, 'dE0': -0.0, 'dn': -4.3665007882696065e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H3-2 + CH3 <=> C4H6-5'}, {'dA': 0.002472827732802602, 'dE0': -0.0, 'dn': -4.3676235083787547e-05, 'dA_dEa': -0.004267558869842007, 'dE0_dEa': -0.0, 'dn_dEa': 0.0008636480965030551, 'name': 'C5H5 + CH3 <=> C6H8'}, {'dA': 0.0003353118209759401, 'dE0': -0.0, 'dn': -4.3673975051002924e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C5H5 + C5H5 <=> C10H10-6'}, {'dA': 0.028144020744139454, 'dE0': -0.0, 'dn': -4.850598739888214e-05, 'dA_dEa': 0.06919346318490989, 'dE0_dEa': -0.0, 'dn_dEa': -0.01408066839255445, 'name': 'O2 + C6H5 <=> C6H5O2'}, {'dA': 0.02812223321058437, 'dE0': -0.0, 'dn': -4.353604026980891e-05, 'dA_dEa': 0.11445217379525569, 'dE0_dEa': -0.0, 'dn_dEa': -0.023286493527370188, 'name': 'O2 + C10H7 <=> C10H7O2'}, {'dA': 0.02812058817270068, 'dE0': -0.0, 'dn': -4.314438994660301e-05, 'dA_dEa': 0.07727376739198062, 'dE0_dEa': -0.0, 'dn_dEa': -0.015723555040714727, 'name': 'O2 + C10H7-2 <=> C10H7O2-2'}, {'dA': 0.028152011751106702, 'dE0': -0.0, 'dn': -5.0341985797529976e-05, 'dA_dEa': 0.11707838181786069, 'dE0_dEa': -0.0, 'dn_dEa': -0.02381929912458282, 'name': 'O2 + C7H7 <=> C7H7O2'}, {'dA': 0.028123755960510522, 'dE0': -0.0, 'dn': -4.387166239830859e-05, 'dA_dEa': 0.060302409504948674, 'dE0_dEa': -0.0, 'dn_dEa': -0.012271232984502868, 'name': 'C6H5 + C6H5 <=> C12H10'}, {'dA': 0.002472886709626027, 'dE0': -0.0, 'dn': -4.3689720139668676e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C11H23 + CH3 <=> C12H26'}, {'dA': 0.0024735392525346237, 'dE0': -0.0, 'dn': -4.383873474429428e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C10H21 + C2H5 <=> C12H26-2'}, {'dA': 0.00247279627707569, 'dE0': -0.0, 'dn': -4.36690424368857e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C9H19 + C3H7 <=> C12H26-3'}, {'dA': 0.0024736598831512305, 'dE0': -0.0, 'dn': -4.386615642701448e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C8H17 + C4H9-2 <=> C12H26-4'}, {'dA': 0.002472096074513092, 'dE0': -0.0, 'dn': -4.350907759952947e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C7H15 + C5H11 <=> C12H26-5'}, {'dA': 0.0024729154670669, 'dE0': -0.0, 'dn': -4.369627644903898e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C6H13 + C6H13 <=> C12H26-6'}, {'dA': 0.002472819778276675, 'dE0': -0.0, 'dn': -4.3674425351463784e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C9H19 <=> C10H22'}, {'dA': 0.0024729693155481295, 'dE0': -0.0, 'dn': -4.370850153482769e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C8H17 + C2H5 <=> C10H22-2'}, {'dA': 0.002473409617565198, 'dE0': -0.0, 'dn': -4.380932600415953e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C7H15 + C3H7 <=> C10H22-3'}, {'dA': 0.0024732939394314594, 'dE0': -0.0, 'dn': -4.3782824161316655e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C6H13 + C4H9-2 <=> C10H22-4'}, {'dA': 0.002472833164901817, 'dE0': -0.0, 'dn': -4.3677480352413894e-05, 'dA_dEa': 0.00020176053538991658, 'dE0_dEa': -0.0, 'dn_dEa': -4.549510119247082e-05, 'name': 'C5H11 + C5H11 <=> C10H22-5'}, {'dA': 0.002474776605865531, 'dE0': -0.0, 'dn': -4.4121689505832116e-05, 'dA_dEa': -0.007088128228361582, 'dE0_dEa': -0.0, 'dn_dEa': 0.0014374448285332608, 'name': 'CH3 + C7H15-2 <=> C8H18-2'}, {'dA': 0.0024705627534873874, 'dE0': -0.0, 'dn': -4.3158512973511924e-05, 'dA_dEa': 0.014738123327974709, 'dE0_dEa': -0.0, 'dn_dEa': -0.003002348748526824, 'name': 'C4H9-3 + C4H9 <=> C8H18-3'}, {'dA': 0.0024721280329489895, 'dE0': -0.0, 'dn': -4.351681728616893e-05, 'dA_dEa': 0.01800239588867412, 'dE0_dEa': -0.0, 'dn_dEa': -0.0036665675275430786, 'name': 'C5H11-2 + C3H7-2 <=> C8H18-4'}, {'dA': 0.0024670797689199607, 'dE0': -0.0, 'dn': -4.236473054478846e-05, 'dA_dEa': 0.01942401341281866, 'dE0_dEa': -0.0, 'dn_dEa': -0.003955612233099419, 'name': 'C7H15-3 + CH3 <=> C8H18-5'}]
""",
)

entry(
    index = 137,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O",
    kinetics = ArrheniusBM(A=(1.54072e+07,'m^3/(mol*s)'), n=-6.19948e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.142131114327, var=0.0599978326704, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O
        Total Standard Deviation in ln(k): 0.848162284374"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O
Total Standard Deviation in ln(k): 0.848162284374""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O
Total Standard Deviation in ln(k): 0.848162284374
sensitivities = [{'dA': 0.06849896956851653, 'dE0': 0.0, 'dn': -2415.420569749371, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + CHO <=> C2H4O'}, {'dA': 0.06823055930738815, 'dE0': 0.0, 'dn': -2357.094905102777, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H3 + CHO <=> C3H4O'}, {'dA': 0.8867430322220127, 'dE0': 0.0, 'dn': 324.8704949922556, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CHO + CHO <=> C2H2O2'}]
""",
)

entry(
    index = 138,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C",
    kinetics = ArrheniusBM(A=(2.58432e+07,'m^3/(mol*s)'), n=-0.0956355, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0184614839253, var=0.814135090552, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C
        Total Standard Deviation in ln(k): 1.85524676771"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C
Total Standard Deviation in ln(k): 1.85524676771""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C
Total Standard Deviation in ln(k): 1.85524676771
sensitivities = [{'dA': 0.09736777280978622, 'dE0': 0.0, 'dn': 1.46464585671731e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C6H5 + C3H3 <=> C9H8'}, {'dA': 0.09745821700591868, 'dE0': 0.0, 'dn': 4.152603935926187e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C6H5 + C3H3-2 <=> C9H8-2'}, {'dA': 0.09732979791722235, 'dE0': 0.0, 'dn': 3.362456384560541e-06, 'dA_dEa': 0.07277204871770329, 'dE0_dEa': 0.0, 'dn_dEa': 0.019276261077228747, 'name': 'C6H5 + CH3 <=> C7H8'}, {'dA': 0.049780492993539635, 'dE0': 0.0, 'dn': 3.8103203385218454e-05, 'dA_dEa': -0.008929667632885259, 'dE0_dEa': 0.0, 'dn_dEa': -0.002364948612109238, 'name': 'CH3 + C6H5 <=> C7H8-5'}, {'dA': 0.04974946033798326, 'dE0': 0.0, 'dn': 2.8878030030815224e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C6H5 + C6H5 <=> C12H10'}, {'dA': 0.6082729490480391, 'dE0': 0.0, 'dn': 9.662166567012589e-06, 'dA_dEa': 1.3090121765914395, 'dE0_dEa': 0.0, 'dn_dEa': 0.34671601156353427, 'name': 'C6H5 + C6H5 <=> C12H10'}]
""",
)

entry(
    index = 139,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_2R->C",
    kinetics = ArrheniusBM(A=(113109,'m^3/(mol*s)'), n=0.518507, w0=(139000,'J/mol'), E0=(13900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0123104015705, var=1.98462212699, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_2R->C
        Total Standard Deviation in ln(k): 2.8551336178"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_2R->C
Total Standard Deviation in ln(k): 2.8551336178""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_2R->C
Total Standard Deviation in ln(k): 2.8551336178
sensitivities = [{'dA': 0.33310244652188575, 'dE0': 0.0, 'dn': 1.2021618270717842e-05, 'dA_dEa': -2.8842319795877436, 'dE0_dEa': 0.0, 'dn_dEa': 0.4778905992811797, 'name': '[O][O] + [CH3] <=> CH3O2'}, {'dA': 0.33308644795941095, 'dE0': 0.0, 'dn': 1.4982211637781962e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + CH3O <=> C2H6O'}, {'dA': 0.3331293241793188, 'dE0': 0.0, 'dn': 6.9853140793678975e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'O2 + CH3 <=> CH3O2-2'}]
""",
)

entry(
    index = 140,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R",
    kinetics = ArrheniusBM(A=(37016,'m^3/(mol*s)'), n=0.5518, w0=(132200,'J/mol'), E0=(-16592.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0638405962927, var=4.31215946294, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R
        Total Standard Deviation in ln(k): 4.32338419159"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R
Total Standard Deviation in ln(k): 4.32338419159""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R
Total Standard Deviation in ln(k): 4.32338419159
sensitivities = [{'dA': 0.0017502331317588978, 'dE0': -0.0, 'dn': -2.8280985635252337e-05, 'dA_dEa': -0.007929501343540741, 'dE0_dEa': -0.0, 'dn_dEa': 0.0002679937477845656, 'name': '[O][O] + [CH3] <=> CH3O2'}, {'dA': 0.0017502998712617109, 'dE0': -0.0, 'dn': -2.828355786094327e-05, 'dA_dEa': -0.010121901340199862, 'dE0_dEa': -0.0, 'dn_dEa': 0.00034284645245144925, 'name': '[O][O] + C[CH2] <=> C2H5O2'}, {'dA': 0.0017504168017270212, 'dE0': -0.0, 'dn': -2.8288008960476093e-05, 'dA_dEa': -0.012101253371811449, 'dE0_dEa': -0.0, 'dn_dEa': 0.0004104273063216476, 'name': '[O][O] + [CH2]CC <=> C3H7O2'}, {'dA': 0.0017503870317627497, 'dE0': -0.0, 'dn': -2.8286788831818015e-05, 'dA_dEa': 0.0029723210044355574, 'dE0_dEa': -0.0, 'dn_dEa': -0.00010422800326057125, 'name': '1-hydroxybutyl + O2 <=> 1-hydroxybutylO2'}, {'dA': 0.08803182694984006, 'dE0': -0.0, 'dn': -2.717278334047097e-05, 'dA_dEa': -0.9541311014854499, 'dE0_dEa': -0.0, 'dn_dEa': 0.03257396699235976, 'name': '[SH] + [O][O] <=> HSOO'}, {'dA': 0.032175514760982786, 'dE0': -0.0, 'dn': -2.808929748875681e-05, 'dA_dEa': 0.025365541658220487, 'dE0_dEa': -0.0, 'dn_dEa': -0.000868876655827681, 'name': 'OH + NO2-2 <=> HOONO'}, {'dA': 0.03212434884681058, 'dE0': -0.0, 'dn': -2.6132673193298076e-05, 'dA_dEa': 0.1315249223203952, 'dE0_dEa': -0.0, 'dn_dEa': -0.004493037352970748, 'name': 'C3H3 + O2 <=> C3H3O2'}, {'dA': 0.03219517267716653, 'dE0': -0.0, 'dn': -2.8832735661860715e-05, 'dA_dEa': -0.24393192068575176, 'dE0_dEa': -0.0, 'dn_dEa': 0.008325982328881137, 'name': 'C3H3-2 + O2 <=> C3H3O2-2'}, {'dA': 0.0017492871347004318, 'dE0': -0.0, 'dn': -2.824497179478128e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3 + CH3O <=> C2H6O'}, {'dA': 0.0017494441930667444, 'dE0': -0.0, 'dn': -2.8250834090757643e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C3H7-2 + CH3O <=> C4H10O'}, {'dA': 0.001750907260955807, 'dE0': -0.0, 'dn': -2.8306646111952965e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'C4H9 + CH3O <=> C5H12O'}, {'dA': 0.0017504140217285676, 'dE0': -0.0, 'dn': -2.8287934385549625e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH3O + CH3O <=> C2H6O2'}, {'dA': 0.0017512999868076458, 'dE0': -0.0, 'dn': -2.832175033721556e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'OH + CH3O <=> CH4O2'}, {'dA': 0.0017505063549807227, 'dE0': -0.0, 'dn': -2.8291447693196643e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + CH3 <=> CH3O2-2'}, {'dA': 0.0017504588836205466, 'dE0': -0.0, 'dn': -2.8289641079046578e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + C2H5 <=> C2H5O2-2'}, {'dA': 0.0017501865006155067, 'dE0': -0.0, 'dn': -2.827920643835465e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + C3H7-2 <=> C3H7O2-2'}, {'dA': 0.0017520026371899687, 'dE0': -0.0, 'dn': -2.834853516497262e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + C4H9 <=> C4H9O2'}, {'dA': 0.0017495075379516374, 'dE0': -0.0, 'dn': -2.825331297593603e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + C2H3 <=> C2H3O2'}, {'dA': 0.01678683554296086, 'dE0': -0.0, 'dn': -2.8351586278671766e-05, 'dA_dEa': -0.01933703509848996, 'dE0_dEa': -0.0, 'dn_dEa': 0.000657495710655821, 'name': 'O2 + C6H5 <=> C6H5O2'}, {'dA': 0.0017504519203017362, 'dE0': -0.0, 'dn': -2.828928428920229e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + CHO <=> CHO3'}, {'dA': 0.0017501766169660522, 'dE0': -0.0, 'dn': -2.8278839778299508e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'O2 + C2H3O <=> C2H3O3'}, {'dA': 0.1972231818321508, 'dE0': -0.0, 'dn': -2.9100073491119256e-05, 'dA_dEa': 0.48587478280387253, 'dE0_dEa': -0.0, 'dn_dEa': -0.016592039837658244, 'name': 'O2 + C6H5 <=> C6H5O2'}, {'dA': 0.19718151999550354, 'dE0': -0.0, 'dn': -2.750402530157354e-05, 'dA_dEa': 0.8044057817802928, 'dE0_dEa': -0.0, 'dn_dEa': -0.027467555243140783, 'name': 'O2 + C10H7 <=> C10H7O2'}, {'dA': 0.19727838256502436, 'dE0': -0.0, 'dn': -3.1214791269097895e-05, 'dA_dEa': 0.5429860195552182, 'dE0_dEa': -0.0, 'dn_dEa': -0.018542193060813172, 'name': 'O2 + C10H7-2 <=> C10H7O2-2'}, {'dA': 0.1971776822795807, 'dE0': -0.0, 'dn': -2.7359870140890643e-05, 'dA_dEa': 0.8236407975702261, 'dE0_dEa': -0.0, 'dn_dEa': -0.028125769300675167, 'name': 'O2 + C7H7 <=> C7H7O2'}]
""",
)

entry(
    index = 141,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_2CNO->O_N-3R!H->O",
    kinetics = ArrheniusBM(A=(2.80515e+06,'m^3/(mol*s)'), n=0.314888, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_2CNO->O_N-3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_2CNO->O_N-3R!H->O
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_2CNO->O_N-3R!H->O
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_2CNO->O_N-3R!H->O
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + NCOJ <=> NCOH'}]
""",
)

entry(
    index = 142,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.02093e+07,'m^3/(mol*s)'), n=0.125846, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.344634126617, var=1.10803912264, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-5R!H-R
        Total Standard Deviation in ln(k): 2.97616794166"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.97616794166""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.97616794166
sensitivities = [{'dA': 0.7350041916361604, 'dE0': 0.0, 'dn': -7.915463034283095e-05, 'dA_dEa': 0.011408778728850967, 'dE0_dEa': 0.0, 'dn_dEa': -0.010374316083364175, 'name': 'C6H7-4 + H <=> C6H8-5'}, {'dA': 0.2646090264484549, 'dE0': 0.0, 'dn': -3.62009623150076e-05, 'dA_dEa': 0.344775161199389, 'dE0_dEa': 0.0, 'dn_dEa': -0.3138329825660271, 'name': 'C7H7-3 + H <=> C7H8-4'}]
""",
)

entry(
    index = 143,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(1.36745e+07,'m^3/(mol*s)'), n=-0.263863, w0=(139000,'J/mol'), E0=(13900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00481396807501, var=0.0768145972539, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R
        Total Standard Deviation in ln(k): 0.567716674236"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R
Total Standard Deviation in ln(k): 0.567716674236""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R
Total Standard Deviation in ln(k): 0.567716674236
sensitivities = [{'dA': 0.33316559414235175, 'dE0': 0.0, 'dn': 9.470145121421006e-07, 'dA_dEa': -3.612842211403631, 'dE0_dEa': 0.0, 'dn_dEa': 2.384068623408563, 'name': '[O][O] + C[CH2] <=> C2H5O2'}, {'dA': 0.33335718360842154, 'dE0': 0.0, 'dn': -0.0001408764991640846, 'dA_dEa': 0.00019536077644490766, 'dE0_dEa': 0.0, 'dn_dEa': -0.0001445541858578585, 'name': 'CH3O + CH3O <=> C2H6O2'}, {'dA': 0.33337243543133727, 'dE0': 0.0, 'dn': -0.00015218025093642075, 'dA_dEa': 0.00019536077644490766, 'dE0_dEa': 0.0, 'dn_dEa': -0.0001445541858578585, 'name': 'O2 + C2H5 <=> C2H5O2-2'}]
""",
)

entry(
    index = 144,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C",
    kinetics = ArrheniusBM(A=(91220.9,'m^3/(mol*s)'), n=0.645371, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0563208528418, var=0.081353830223, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C
        Total Standard Deviation in ln(k): 0.713312104122"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C
Total Standard Deviation in ln(k): 0.713312104122""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C
Total Standard Deviation in ln(k): 0.713312104122
sensitivities = [{'dA': 0.03436407964052913, 'dE0': 0.0, 'dn': 1.0600160790569966e-05, 'dA_dEa': -0.0026268782118424434, 'dE0_dEa': 0.0, 'dn_dEa': 0.00041032907405584877, 'name': 'CH3 + C2H5 <=> C3H8'}, {'dA': 0.03444256564755601, 'dE0': 0.0, 'dn': -3.174649402737035e-06, 'dA_dEa': 0.0005598645991256652, 'dE0_dEa': 0.0, 'dn_dEa': -9.049695819441836e-05, 'name': 'C2H5 + C2H5 <=> C4H10'}, {'dA': 0.0005310144430837356, 'dE0': 0.0, 'dn': -2.397612380459251e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C2H5 <=> C3H8-3'}, {'dA': 0.000530954290312083, 'dE0': 0.0, 'dn': -2.396551783422108e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C2H5 <=> C4H10-3'}, {'dA': 0.0005309570099144041, 'dE0': 0.0, 'dn': -2.3965994976659635e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + CHO <=> C3H6O-2'}, {'dA': 0.3098314455698756, 'dE0': 0.0, 'dn': -1.7147830232465378e-06, 'dA_dEa': 1.6003975120108636, 'dE0_dEa': 0.0, 'dn_dEa': -0.25157412746425556, 'name': 'CH3S + C2H5 <=> C3H8S'}, {'dA': 0.30995828620564797, 'dE0': 0.0, 'dn': -2.4085662356350896e-05, 'dA_dEa': 1.6003975120108636, 'dE0_dEa': 0.0, 'dn_dEa': -0.25157412746425556, 'name': 'CH3S + CH3 <=> C2H6S'}, {'dA': 0.3099582862092007, 'dE0': 0.0, 'dn': -2.4085663197871953e-05, 'dA_dEa': 1.6003494737796928, 'dE0_dEa': 0.0, 'dn_dEa': -0.2515656883933512, 'name': 'CH3S + C4H9 <=> C5H12S'}]
""",
)

entry(
    index = 145,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.61526e+07,'m^3/(mol*s)'), n=-0.2125, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.11811042808e-10, var=0.384383286643, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R
        Total Standard Deviation in ln(k): 1.24290872788"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 1.24290872788""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 1.24290872788
sensitivities = [{'dA': 0.24989746504291954, 'dE0': 0.0, 'dn': 1.4711762983285259e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + C2H3O <=> C4H8O'}, {'dA': 0.24989830266267088, 'dE0': 0.0, 'dn': 1.5262015925243682e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C3H7-2 + C2H3O <=> C5H10O'}, {'dA': 0.25001264158322467, 'dE0': 0.0, 'dn': 9.037697724046019e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CHO + C2H3O <=> C3H4O2'}, {'dA': 0.2499677065479764, 'dE0': 0.0, 'dn': 6.0850394751296526e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H3O + C2H3O <=> C4H6O2'}]
""",
)

entry(
    index = 146,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(45504,'m^3/(mol*s)'), n=0.740315, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0441547038934, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R
        Total Standard Deviation in ln(k): 0.110941467069"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.110941467069""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.110941467069
sensitivities = [{'dA': 0.4996108790643045, 'dE0': 0.0, 'dn': 2.1665106490211347e-05, 'dA_dEa': 2.5812791609197205, 'dE0_dEa': 0.0, 'dn_dEa': -0.3578266624853529, 'name': 'CH3S + C2H5 <=> C3H8S'}, {'dA': 0.4996108790643045, 'dE0': 0.0, 'dn': 2.1665106490211347e-05, 'dA_dEa': 2.58126747293403, 'dE0_dEa': 0.0, 'dn_dEa': -0.35782484452941504, 'name': 'CH3S + C4H9 <=> C5H12S'}]
""",
)

entry(
    index = 147,
    label = "Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_2R->C",
    kinetics = ArrheniusBM(A=(6.89518e+73,'m^3/(mol*s)'), n=-21.0166, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_2R->C
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_2R->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0_2R->C
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'CN + NCN <=> NCNCN'}]
""",
)

entry(
    index = 148,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing",
    kinetics = ArrheniusBM(A=(7.49725e+08,'m^3/(mol*s)'), n=-0.546607, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0173097986373, var=0.452291225768, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing
        Total Standard Deviation in ln(k): 1.39172842662"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing
Total Standard Deviation in ln(k): 1.39172842662""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing
Total Standard Deviation in ln(k): 1.39172842662
sensitivities = [{'dA': 0.06855757092694903, 'dE0': 0.0, 'dn': 1.205047651076579e-05, 'dA_dEa': 0.13408087471590646, 'dE0_dEa': 0.0, 'dn_dEa': 0.02713649001169993, 'name': 'C5H5 + C2H5 <=> C7H10'}, {'dA': 0.19034421843857494, 'dE0': 0.0, 'dn': 1.2229706772179227e-05, 'dA_dEa': -0.0014350865988889598, 'dE0_dEa': 0.0, 'dn_dEa': -0.00028908570313683176, 'name': 'C5H5 + CH3 <=> C6H8'}, {'dA': 0.06856019518864587, 'dE0': 0.0, 'dn': 1.2646166588963517e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C6H5 + C3H3 <=> C9H8'}, {'dA': 0.06856019518864587, 'dE0': 0.0, 'dn': 1.2646166588963517e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C6H5 + C3H3-2 <=> C9H8-2'}, {'dA': 0.06854941781498569, 'dE0': 0.0, 'dn': 1.0198933002724917e-05, 'dA_dEa': 0.051238562480909834, 'dE0_dEa': 0.0, 'dn_dEa': 0.010370608961056764, 'name': 'C6H5 + CH3 <=> C7H8'}, {'dA': 0.03500396743305986, 'dE0': 0.0, 'dn': 1.1969373634742114e-05, 'dA_dEa': -0.0062379500427318865, 'dE0_dEa': 0.0, 'dn_dEa': -0.001261108586315091, 'name': 'CH3 + C6H5 <=> C7H8-5'}, {'dA': 0.03501309089415758, 'dE0': 0.0, 'dn': 1.4040854583912173e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C6H5 + C6H5 <=> C12H10'}, {'dA': 0.03499918206629035, 'dE0': 0.0, 'dn': 1.088474146047435e-05, 'dA_dEa': -0.06833049737765193, 'dE0_dEa': 0.0, 'dn_dEa': -0.013827396374515511, 'name': 'C5H5 + CH3 <=> C6H8'}, {'dA': 0.002237329656651601, 'dE0': 0.0, 'dn': 1.2015876933824677e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C5H5 + C5H5 <=> C10H10-6'}, {'dA': 0.42820649734314487, 'dE0': 0.0, 'dn': 1.2065220961586595e-05, 'dA_dEa': 0.9214928685069472, 'dE0_dEa': 0.0, 'dn_dEa': 0.18649220602903968, 'name': 'C6H5 + C6H5 <=> C12H10'}]
""",
)

entry(
    index = 149,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(129687,'m^3/(mol*s)'), n=0.801692, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C_Ext-1C-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'HSS + C4H9 <=> C4H10S2'}]
""",
)

entry(
    index = 150,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.78708e+06,'m^3/(mol*s)'), n=-0.129357, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-4R!H-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'O2 + C10H7 <=> C10H7O2'}]
""",
)

entry(
    index = 151,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-3CS-R",
    kinetics = ArrheniusBM(A=(1.1386e+07,'m^3/(mol*s)'), n=0.308956, w0=(171833,'J/mol'), E0=(17183.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.11188672232, var=3.33851088254, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-3CS-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-3CS-R
        Total Standard Deviation in ln(k): 6.45665544921"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-3CS-R
Total Standard Deviation in ln(k): 6.45665544921""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-3CS-R
Total Standard Deviation in ln(k): 6.45665544921
sensitivities = [{'dA': 0.9769367926645255, 'dE0': 0.0, 'dn': 5.3221542856763404e-05, 'dA_dEa': 1.123896398514414, 'dE0_dEa': 0.0, 'dn_dEa': -0.40719516857592, 'name': 'H + NJCO <=> HNCO'}, {'dA': 0.01108598979726716, 'dE0': 0.0, 'dn': 5.301018506156006e-05, 'dA_dEa': 0.007466127353695496, 'dE0_dEa': 0.0, 'dn_dEa': -0.002699279211863441, 'name': 'C3H3-2 + H <=> C3H4-2'}, {'dA': 0.011093561830933907, 'dE0': 0.0, 'dn': 4.9936846217612724e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H3-2 + H <=> C3H4-2'}]
""",
)

entry(
    index = 152,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_2CNO->O",
    kinetics = ArrheniusBM(A=(2.61215e+06,'m^3/(mol*s)'), n=0.325758, w0=(143500,'J/mol'), E0=(14350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.336871845639, var=0.241325868577, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_2CNO->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_2CNO->O
        Total Standard Deviation in ln(k): 1.83123636332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_2CNO->O
Total Standard Deviation in ln(k): 1.83123636332""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_2CNO->O
Total Standard Deviation in ln(k): 1.83123636332
sensitivities = [{'dA': 0.988294519897901, 'dE0': 0.0, 'dn': -5.3502793418976004e-05, 'dA_dEa': 1.1367611419307453, 'dE0_dEa': 0.0, 'dn_dEa': -0.3931440073679349, 'name': 'H + NCOJ <=> NCOH'}, {'dA': 0.01147736572626583, 'dE0': 0.0, 'dn': -5.1917513063306986e-05, 'dA_dEa': -0.01984100218521908, 'dE0_dEa': 0.0, 'dn_dEa': 0.006856297323419158, 'name': 'O2 + H <=> HO2-2'}]
""",
)

entry(
    index = 153,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=-1.42812e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_N-4R!H->C
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'C2H5 + CHO <=> C3H6O-2'}]
""",
)

entry(
    index = 154,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_4R!H->O",
    kinetics = ArrheniusBM(A=(3.5e+06,'m^3/(mol*s)'), n=1.0712e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_4R!H->O
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_4R!H->O
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_4R!H->O
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'O2 + CHO <=> CHO3'}]
""",
)

entry(
    index = 155,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(4.12e+09,'m^3/(mol*s)'), n=-1.1, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_N-7R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_N-7R!H->O
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_N-7R!H->O
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_N-7R!H->O
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C3H7-2 + C4H9 <=> C7H16'}]
""",
)

entry(
    index = 156,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R",
    kinetics = ArrheniusBM(A=(3.18795e+10,'m^3/(mol*s)'), n=-1.17734, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.298025015457, var=0.3094099417, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R
        Total Standard Deviation in ln(k): 1.86393303255"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R
Total Standard Deviation in ln(k): 1.86393303255""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R
Total Standard Deviation in ln(k): 1.86393303255
sensitivities = [{'dA': 0.14774501722316052, 'dE0': 0.0, 'dn': -0.0029160618140105414, 'dA_dEa': -0.2644131198295277, 'dE0_dEa': 0.0, 'dn_dEa': -1.2423265641493833, 'name': 'C3H3 + C7H7 <=> C10H10'}, {'dA': 0.004164370402293575, 'dE0': 0.0, 'dn': -0.002975500917662676, 'dA_dEa': 0.005046972294309727, 'dE0_dEa': 0.0, 'dn_dEa': 0.023383058858018464, 'name': 'C3H3 + C3H3 <=> C6H6-3'}, {'dA': 0.004164576001386881, 'dE0': 0.0, 'dn': -0.0029744172710177265, 'dA_dEa': 0.004246718194878453, 'dE0_dEa': 0.0, 'dn_dEa': 0.019624117505838586, 'name': 'C3H5 + C3H5 <=> C6H10-2'}, {'dA': 0.004152880659802806, 'dE0': 0.0, 'dn': -0.0030360584987284382, 'dA_dEa': 0.0018395428327268953, 'dE0_dEa': 0.0, 'dn_dEa': 0.008316132126101874, 'name': 'C3H5 + C2H5 <=> C5H10-2'}, {'dA': 0.004163906154986311, 'dE0': 0.0, 'dn': -0.0029779478391137033, 'dA_dEa': 0.0018404619233083148, 'dE0_dEa': 0.0, 'dn_dEa': 0.008320975648565654, 'name': 'C3H5 + CH3 <=> C4H8-2'}, {'dA': 0.07523575905921949, 'dE0': 0.0, 'dn': -0.0022489241000018846, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C11H23 + CH3 <=> C12H26'}, {'dA': 0.07508418322999805, 'dE0': 0.0, 'dn': -0.0030476481102689077, 'dA_dEa': -0.0002704130892539367, 'dE0_dEa': 0.0, 'dn_dEa': -0.0015950846083213417, 'name': 'C10H21 + C2H5 <=> C12H26-2'}, {'dA': 0.07508161255388163, 'dE0': 0.0, 'dn': -0.003061198131766998, 'dA_dEa': -0.0017571023995801285, 'dE0_dEa': 0.0, 'dn_dEa': -0.008582047835258092, 'name': 'C9H19 + C3H7 <=> C12H26-3'}, {'dA': 0.07509705028852781, 'dE0': 0.0, 'dn': -0.0029798304753943117, 'dA_dEa': 0.0035718590716275526, 'dE0_dEa': 0.0, 'dn_dEa': 0.01644915705419894, 'name': 'C8H17 + C4H9-2 <=> C12H26-4'}, {'dA': 0.07510769083297336, 'dE0': 0.0, 'dn': -0.0029237484886478486, 'dA_dEa': -0.0023448498396308275, 'dE0_dEa': 0.0, 'dn_dEa': -0.011340311561868365, 'name': 'C7H15 + C5H11 <=> C12H26-5'}, {'dA': 0.07518633410442395, 'dE0': 0.0, 'dn': -0.0025090172282253138, 'dA_dEa': -0.0026464857825206495, 'dE0_dEa': 0.0, 'dn_dEa': -0.012760336330764026, 'name': 'C6H13 + C6H13 <=> C12H26-6'}, {'dA': 0.07544705740515077, 'dE0': 0.0, 'dn': -0.0011350359914416026, 'dA_dEa': 0.0013401348688547954, 'dE0_dEa': 0.0, 'dn_dEa': 0.005874937478826394, 'name': 'CH3 + C9H19 <=> C10H22'}, {'dA': 0.07510181744763972, 'dE0': 0.0, 'dn': -0.0029547069183772307, 'dA_dEa': 0.006541198132482161, 'dE0_dEa': 0.0, 'dn_dEa': 0.030401789212589108, 'name': 'C8H17 + C2H5 <=> C10H22-2'}, {'dA': 0.07511129831173352, 'dE0': 0.0, 'dn': -0.002904740027107176, 'dA_dEa': 0.0018147320162144932, 'dE0_dEa': 0.0, 'dn_dEa': 0.00820658227340594, 'name': 'C7H15 + C3H7 <=> C10H22-3'}, {'dA': 0.07507998187251391, 'dE0': 0.0, 'dn': -0.003069792490512659, 'dA_dEa': 0.00030469563228056076, 'dE0_dEa': 0.0, 'dn_dEa': 0.0010965729146928862, 'name': 'C6H13 + C4H9-2 <=> C10H22-4'}, {'dA': 0.07518649302796494, 'dE0': 0.0, 'dn': -0.0025081860608766136, 'dA_dEa': -0.00026620498871923905, 'dE0_dEa': 0.0, 'dn_dEa': -0.001572900335980234, 'name': 'C5H11 + C5H11 <=> C10H22-5'}]
""",
)

entry(
    index = 157,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.25e+08,'m^3/(mol*s)'), n=-0.7, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-1C-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C3H7-2 + C3H7-2 <=> C6H14-2'}]
""",
)

entry(
    index = 158,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R",
    kinetics = ArrheniusBM(A=(2.14111e+08,'m^3/(mol*s)'), n=-0.500739, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.279825822694, var=1.16058598837, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R
        Total Standard Deviation in ln(k): 2.86279100961"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R
Total Standard Deviation in ln(k): 2.86279100961""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R
Total Standard Deviation in ln(k): 2.86279100961
sensitivities = [{'dA': 0.22779443141021383, 'dE0': 0.0, 'dn': -8.559061921919064e-05, 'dA_dEa': -1.0663680117845085, 'dE0_dEa': 0.0, 'dn_dEa': -0.38328629552766325, 'name': 'C3H3-2 + C7H7 <=> C10H10-2'}, {'dA': 0.007036838120200948, 'dE0': 0.0, 'dn': -9.428261958960831e-05, 'dA_dEa': 0.029029764807123472, 'dE0_dEa': 0.0, 'dn_dEa': 0.010423733673913946, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}, {'dA': 0.0070370414704264955, 'dE0': 0.0, 'dn': -9.420070695606079e-05, 'dA_dEa': 0.018852952486272244, 'dE0_dEa': 0.0, 'dn_dEa': 0.006765933470793039, 'name': 'C3H3 + C3H3-2 <=> C6H6-2'}, {'dA': 0.6331281024856836, 'dE0': 0.0, 'dn': -9.023928784567034e-05, 'dA_dEa': 5.62051089601274, 'dE0_dEa': 0.0, 'dn_dEa': 2.0201298934908314, 'name': 'CH3 + C3H3-2 <=> C4H6'}, {'dA': 0.11615790562303943, 'dE0': 0.0, 'dn': -6.937430932448785e-05, 'dA_dEa': 0.46863976670513285, 'dE0_dEa': 0.0, 'dn_dEa': 0.16843060131449644, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}, {'dA': 0.007036962305307591, 'dE0': 0.0, 'dn': -9.423263439855702e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C3H3-2 + CH3 <=> C4H6-5'}]
""",
)

entry(
    index = 159,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.6895e+08,'m^3/(mol*s)'), n=-0.811251, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.000621224287992, var=1.52046208061, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R
        Total Standard Deviation in ln(k): 2.47353991738"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.47353991738""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.47353991738
sensitivities = [{'dA': 0.04316747169142352, 'dE0': 0.0, 'dn': -4.449802422112846e-05, 'dA_dEa': -0.0002135202237241409, 'dE0_dEa': 0.0, 'dn_dEa': -3.286654184710533e-05, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.043169445493878335, 'dE0': 0.0, 'dn': -4.421610364418068e-05, 'dA_dEa': -0.0002135202237241409, 'dE0_dEa': 0.0, 'dn_dEa': -3.286654184710533e-05, 'name': 'C3H7-2 + C4H9 <=> C7H16'}, {'dA': 0.04321320839651342, 'dE0': 0.0, 'dn': -3.743570857278788e-05, 'dA_dEa': -0.0002135202237241409, 'dE0_dEa': 0.0, 'dn_dEa': -3.286654184710533e-05, 'name': 'C4H9 + C4H9 <=> C8H18'}, {'dA': 0.04325655016402174, 'dE0': 0.0, 'dn': -3.07811563884898e-05, 'dA_dEa': -0.0002135202237241409, 'dE0_dEa': 0.0, 'dn_dEa': -3.286654184710533e-05, 'name': 'C4H9 + CHO <=> C5H10O-2'}, {'dA': 0.0432757082329308, 'dE0': 0.0, 'dn': -2.7826371559422377e-05, 'dA_dEa': -0.0002135202237241409, 'dE0_dEa': 0.0, 'dn_dEa': -3.286654184710533e-05, 'name': 'C4H9 + C2H3O <=> C6H12O'}, {'dA': 0.04334649154458725, 'dE0': 0.0, 'dn': -1.691711285245632e-05, 'dA_dEa': -0.0002135202237241409, 'dE0_dEa': 0.0, 'dn_dEa': -3.286654184710533e-05, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.043192935624607784, 'dE0': 0.0, 'dn': -4.059709159840737e-05, 'dA_dEa': 0.021777020808857638, 'dE0_dEa': 0.0, 'dn_dEa': 0.00298469196210491, 'name': 'C3H5 + C4H9 <=> C7H14'}, {'dA': 0.6952931379267879, 'dE0': 0.0, 'dn': -1.7198653273834753e-06, 'dA_dEa': 4.436990970916588, 'dE0_dEa': 0.0, 'dn_dEa': 0.6092315377341254, 'name': 'C4H9-3 + C4H9 <=> C8H18-3'}]
""",
)

entry(
    index = 160,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.48129e+07,'m^3/(mol*s)'), n=-0.157514, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-3C-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.05837558277833143, 'dE0': 0.0, 'dn': -8.37446384670476e-05, 'dA_dEa': 0.05941033953860796, 'dE0_dEa': 0.0, 'dn_dEa': 0.010589298874377566, 'name': 'C3H5 + C5H7 <=> C8H12'}, {'dA': 0.9403507257524849, 'dE0': 0.0, 'dn': -7.112316963000385e-05, 'dA_dEa': 7.935760575613834, 'dE0_dEa': 0.0, 'dn_dEa': 1.4156370646996301, 'name': 'C7H15-3 + CH3 <=> C8H18-5'}]
""",
)

entry(
    index = 161,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.4834e+08,'m^3/(mol*s)'), n=-0.557189, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00108714239892, var=1.14816174436, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R
        Total Standard Deviation in ln(k): 2.15085144951"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 2.15085144951""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 2.15085144951
sensitivities = [{'dA': 0.05073693837687746, 'dE0': 0.0, 'dn': 0.00014764586527979339, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + C3H7-2 <=> C5H12-2'}, {'dA': 0.050809833908266364, 'dE0': 0.0, 'dn': 0.00016177280093207933, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C3H7-2 + C3H7-2 <=> C6H14-2'}, {'dA': 0.05077497207040542, 'dE0': 0.0, 'dn': 0.00015500643270652088, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + C3H7-2 <=> C5H12-2'}, {'dA': 0.050729683064082466, 'dE0': 0.0, 'dn': 0.0001462446095803592, 'dA_dEa': 0.02613261943196509, 'dE0_dEa': 0.0, 'dn_dEa': 0.004527833564493132, 'name': 'C3H5 + C3H7-2 <=> C6H12'}, {'dA': 0.7999905278667001, 'dE0': 0.0, 'dn': 7.560333960530654e-05, 'dA_dEa': 6.2456497513607925, 'dE0_dEa': 0.0, 'dn_dEa': 1.078573241695786, 'name': 'C5H11-2 + C3H7-2 <=> C8H18-4'}]
""",
)

entry(
    index = 162,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-5R!H-R_Ext-2CNO-R",
    kinetics = ArrheniusBM(A=(3.10431e+07,'m^3/(mol*s)'), n=0.0432612, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-5R!H-R_Ext-2CNO-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-5R!H-R_Ext-2CNO-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-5R!H-R_Ext-2CNO-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H_Ext-5R!H-R_Ext-5R!H-R_Ext-2CNO-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C7H7-3 + H <=> C7H8-4'}]
""",
)

entry(
    index = 163,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_N-2R->C",
    kinetics = ArrheniusBM(A=(1.57e+07,'m^3/(mol*s)'), n=1.44035e-07, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_N-2R->C
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_N-2R->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_N-2R->C
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'OH + OH <=> H2O2'}]
""",
)

entry(
    index = 164,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O",
    kinetics = ArrheniusBM(A=(8.15666e+12,'m^3/(mol*s)'), n=-1.49308, w0=(186750,'J/mol'), E0=(18675,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.399348053434, var=9.35827249741, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O
        Total Standard Deviation in ln(k): 7.13613102162"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O
Total Standard Deviation in ln(k): 7.13613102162""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O
Total Standard Deviation in ln(k): 7.13613102162
sensitivities = [{'dA': 0.38840055668391943, 'dE0': 0.0, 'dn': -0.0001851718792946475, 'dA_dEa': 0.4469728135454924, 'dE0_dEa': 0.0, 'dn_dEa': 0.07222916107894164, 'name': 'H + NJCO <=> HNCO'}, {'dA': 0.1383362802371987, 'dE0': 0.0, 'dn': -0.0003365209063320722, 'dA_dEa': 7.86109411743483, 'dE0_dEa': 0.0, 'dn_dEa': 1.270642820526125, 'name': '[CH2]c1ccccc1[C]=C=C + [H] <=> C10H9'}, {'dA': 0.003413997259116662, 'dE0': 0.0, 'dn': -0.0001915773952015845, 'dA_dEa': 0.0019703678475482215, 'dE0_dEa': 0.0, 'dn_dEa': 0.00029765424368474616, 'name': 'C3H3-2 + H <=> C3H4-2'}, {'dA': 0.38836024668502506, 'dE0': 0.0, 'dn': -0.00019233391220798806, 'dA_dEa': -1.5293488267433284, 'dE0_dEa': 0.0, 'dn_dEa': -0.24722551120629363, 'name': 'C4H5 + H <=> C4H6-2'}, {'dA': 0.07047243261127599, 'dE0': 0.0, 'dn': -0.00019111806512102912, 'dA_dEa': -0.001057170042173655, 'dE0_dEa': 0.0, 'dn_dEa': -0.000191717992976244, 'name': 'H + C2H3 <=> C2H4'}, {'dA': 0.0034121689758141323, 'dE0': 0.0, 'dn': -0.00019190928102040962, 'dA_dEa': -0.001057170042173655, 'dE0_dEa': 0.0, 'dn_dEa': -0.000191717992976244, 'name': 'C3H3-2 + H <=> C3H4-2'}]
""",
)

entry(
    index = 165,
    label = "Root_N-1R->H_1CNOS->N",
    kinetics = ArrheniusBM(A=(4.41861e+11,'m^3/(mol*s)'), n=-1.35036, w0=(77730.8,'J/mol'), E0=(47723.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.522069824462, var=8.72526504015, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_1CNOS->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N
        Total Standard Deviation in ln(k): 7.23343188649"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N
Total Standard Deviation in ln(k): 7.23343188649""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N
Total Standard Deviation in ln(k): 7.23343188649
sensitivities = [{'dA': -1.3206253868249041e-05, 'dE0': 0.00012696964862713125, 'dn': 5.451112162821159e-06, 'dA_dEa': -1.3206488347351842e-05, 'dE0_dEa': 0.00012695684072372237, 'dn_dEa': 5.450990284902297e-06, 'name': 'NO2 + NO2 <=> N2O4'}, {'dA': -1.3206282289958472e-05, 'dE0': 0.0001269698417733462, 'dn': 5.451123683619459e-06, 'dA_dEa': -1.3205529114658566e-05, 'dE0_dEa': 0.00012692860001785498, 'dn_dEa': 5.450275752864553e-06, 'name': 'NO + O2 <=> NO3'}, {'dA': -1.3206296500813187e-05, 'dE0': 0.0001269699309984999, 'dn': 5.451128898296584e-06, 'dA_dEa': -1.3206488347351842e-05, 'dE0_dEa': 0.00012695684072372237, 'dn_dEa': 5.450990284902297e-06, 'name': 'NO2 + NO3-2 <=> N2O5'}, {'dA': -1.3025768907938598e-05, 'dE0': 0.00012695566589087572, 'dn': 5.39543214463554e-06, 'dA_dEa': -1.3551581190542166e-05, 'dE0_dEa': 0.00012599168215948796, 'dn_dEa': 5.543671226538704e-06, 'name': '[CH3] + [O-][N+]=O <=> CH3NO2'}, {'dA': -1.3114362928946856e-05, 'dE0': 0.0001275803257331049, 'dn': 5.4321295253690034e-06, 'dA_dEa': -1.323757459204135e-05, 'dE0_dEa': 0.00012578659216048782, 'dn_dEa': 5.443367397117415e-06, 'name': 'C[O] + [N]=O <=> CH3ONO'}, {'dA': -1.3052009251170222e-05, 'dE0': 0.00012714090780693166, 'dn': 5.406301593381462e-06, 'dA_dEa': -1.1314071457492329e-05, 'dE0_dEa': 0.00013535565608248942, 'dn_dEa': 4.9906120297979826e-06, 'name': 'CN + NCN <=> NCNCN'}, {'dA': -1.2991204556557544e-05, 'dE0': 0.0001267116019248778, 'dn': 5.381116764482201e-06, 'dA_dEa': -1.3187190006648594e-05, 'dE0_dEa': 0.00012697380651929138, 'dn_dEa': 5.445261780172677e-06, 'name': '[NH2] + [NH2] <=> N2H4'}, {'dA': -1.3205287530128406e-05, 'dE0': 0.00012696291454235832, 'dn': 5.450713058113722e-06, 'dA_dEa': -1.3206488347351842e-05, 'dE0_dEa': 0.00012695684072372237, 'dn_dEa': 5.450990284902297e-06, 'name': 'NH2 + HO2 <=> NH2OOH'}, {'dA': -1.3206438609360339e-05, 'dE0': 0.00012697094417636227, 'dn': 5.451189048990868e-06, 'dA_dEa': -1.320587372788541e-05, 'dE0_dEa': 0.00012694157041601427, 'dn_dEa': 5.45057395963319e-06, 'name': 'NH2 + O2 <=> NH2OO'}, {'dA': -1.298428031759756e-05, 'dE0': 0.00012666261038745275, 'dn': 5.378248692063218e-06, 'dA_dEa': -1.3209788818359448e-05, 'dE0_dEa': 0.00012695634379210192, 'dn_dEa': 5.452005934226144e-06, 'name': 'NH2 + CH3NH <=> CH3NHNH2'}, {'dA': -1.2998690124278777e-05, 'dE0': 0.00012676442657490368, 'dn': 5.3842168293974855e-06, 'dA_dEa': -1.3261079345740296e-05, 'dE0_dEa': 0.00012686564799797742, 'dn_dEa': 5.466557430108859e-06, 'name': 'CH3 + NHNH2 <=> CH3NHNH2'}, {'dA': -1.1642615760366798e-05, 'dE0': 0.00012739878340683162, 'dn': 4.97708139791624e-06, 'dA_dEa': -1.3206488347351842e-05, 'dE0_dEa': 0.00012695684072372237, 'dn_dEa': 5.450990284902297e-06, 'name': 'NO2 + OH <=> HNO3'}, {'dA': -1.3174620505652998e-05, 'dE0': 0.00012696597758939774, 'dn': 5.44133488575411e-06, 'dA_dEa': -1.3206488347351842e-05, 'dE0_dEa': 0.00012695684072372237, 'dn_dEa': 5.450990284902297e-06, 'name': 'NO2 + OH <=> HNO3'}]
""",
)

entry(
    index = 166,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=-1.42812e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_4R!H->C
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'C2H3 + CHO <=> C3H4O'}]
""",
)

entry(
    index = 167,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.95338e+06,'m^3/(mol*s)'), n=0.346862, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C7H7-2 + H <=> C7H8-3'}]
""",
)

entry(
    index = 168,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing",
    kinetics = ArrheniusBM(A=(2.43996e+07,'m^3/(mol*s)'), n=0.0713965, w0=(212091,'J/mol'), E0=(21209.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10688619938, var=4.94781535513, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing
        Total Standard Deviation in ln(k): 4.72782790609"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing
Total Standard Deviation in ln(k): 4.72782790609""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing
Total Standard Deviation in ln(k): 4.72782790609
sensitivities = [{'dA': 0.0822681858352416, 'dE0': 0.0, 'dn': -0.0008346108324901618, 'dA_dEa': 0.007877000530954505, 'dE0_dEa': 0.0, 'dn_dEa': -0.006917208982593216, 'name': 'C6H7 + H <=> C6H8-2'}, {'dA': 0.08225945871843461, 'dE0': 0.0, 'dn': -0.0008261240471355356, 'dA_dEa': 0.000212026364465624, 'dE0_dEa': 0.0, 'dn_dEa': -0.00027391875023725785, 'name': 'C6H7-2 + H <=> C6H8-3'}, {'dA': 0.08226805814360656, 'dE0': 0.0, 'dn': -0.0008344851185897611, 'dA_dEa': 0.0021319290013368645, 'dE0_dEa': 0.0, 'dn_dEa': -0.001938296044930737, 'name': 'C6H7-4 + H <=> C6H8-5'}, {'dA': 0.02952446663329381, 'dE0': 0.0, 'dn': -0.0002107237130606055, 'dA_dEa': 0.6061734050782476, 'dE0_dEa': 0.0, 'dn_dEa': -0.5252429249400474, 'name': 'C=C1[CH]c2ccccc2C1 + [H] <=> C10H10-3'}, {'dA': 0.030176122862716197, 'dE0': 0.0, 'dn': -0.0008447396133641946, 'dA_dEa': -0.1567202897270365, 'dE0_dEa': 0.0, 'dn_dEa': 0.13569448719448288, 'name': 'C=C1[CH]Cc2ccccc21 + [H] <=> C10H10-4'}, {'dA': 0.030030514508897464, 'dE0': 0.0, 'dn': -0.0007032331166497533, 'dA_dEa': -0.003324396473658819, 'dE0_dEa': 0.0, 'dn_dEa': 0.0028077599992839073, 'name': 'C=C1C[CH]c2ccccc21 + [H] <=> C10H10-5'}, {'dA': 0.03005679101164891, 'dE0': 0.0, 'dn': -0.0007287004542745334, 'dA_dEa': 0.0008573791525635478, 'dE0_dEa': 0.0, 'dn_dEa': -0.0008339449766522028, 'name': 'C9H7 + H <=> C9H8-3'}, {'dA': 0.03014558799918964, 'dE0': 0.0, 'dn': -0.0008150357909884468, 'dA_dEa': 0.050807991033968755, 'dE0_dEa': 0.0, 'dn_dEa': -0.04410768754059463, 'name': 'C7H7-2 + H <=> C7H8-3'}, {'dA': 0.03020890594030212, 'dE0': 0.0, 'dn': -0.000876609719734965, 'dA_dEa': 0.039067111075046096, 'dE0_dEa': 0.0, 'dn_dEa': -0.03394250364417, 'name': 'C7H7-3 + H <=> C7H8-4'}, {'dA': 0.015816788071278474, 'dE0': 0.0, 'dn': -0.0008402939641486117, 'dA_dEa': 0.0008573791525635478, 'dE0_dEa': 0.0, 'dn_dEa': -0.0008339449766522028, 'name': 'H + C6H5 <=> C6H6-4'}, {'dA': 0.015825245977653744, 'dE0': 0.0, 'dn': -0.0008485079984105577, 'dA_dEa': 0.0008573791525635478, 'dE0_dEa': 0.0, 'dn_dEa': -0.0008339449766522028, 'name': 'C5H5 + H <=> C5H6'}, {'dA': 0.18440505182584033, 'dE0': 0.0, 'dn': -0.0011984189941078845, 'dA_dEa': 0.11428663365010842, 'dE0_dEa': 0.0, 'dn_dEa': -0.09913252981141073, 'name': 'H + C12H9 <=> C12H10-2'}, {'dA': 0.18403021496384647, 'dE0': 0.0, 'dn': -0.0008340013271873182, 'dA_dEa': 0.11195307556378775, 'dE0_dEa': 0.0, 'dn_dEa': -0.0970912461617995, 'name': 'H + C12H9-2 <=> C12H10-3'}, {'dA': 0.18403134572510887, 'dE0': 0.0, 'dn': -0.0008351005995011064, 'dA_dEa': -0.009892750199470536, 'dE0_dEa': 0.0, 'dn_dEa': 0.00848024037474696, 'name': 'H + C12H9-3 <=> C12H10-4'}]
""",
)

entry(
    index = 169,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.95927e+08,'m^3/(mol*s)'), n=-0.639165, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0851650107975, var=0.528125578779, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R
        Total Standard Deviation in ln(k): 1.67086850823"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.67086850823""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.67086850823
sensitivities = [{'dA': 0.08976714407183828, 'dE0': 0.0, 'dn': -8.073604993952885e-05, 'dA_dEa': -0.16016236800810535, 'dE0_dEa': 0.0, 'dn_dEa': -0.1307259214810257, 'name': 'C3H3 + C7H7 <=> C10H10'}, {'dA': 0.08974183864652752, 'dE0': 0.0, 'dn': -0.00010389870602119649, 'dA_dEa': -0.4205232836263414, 'dE0_dEa': 0.0, 'dn_dEa': -0.34319494320311605, 'name': 'C3H3-2 + C7H7 <=> C10H10-2'}, {'dA': 0.0025741259079839545, 'dE0': 0.0, 'dn': -0.00026658791165964045, 'dA_dEa': 0.011239536718222882, 'dE0_dEa': 0.0, 'dn_dEa': 0.009142635218796973, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}, {'dA': 0.002572025149305829, 'dE0': 0.0, 'dn': -0.00026851138836270623, 'dA_dEa': 0.007228539566029554, 'dE0_dEa': 0.0, 'dn_dEa': 0.005869487246529182, 'name': 'C3H3 + C3H3-2 <=> C6H6-2'}, {'dA': 0.0025721243552825957, 'dE0': 0.0, 'dn': -0.00026842056652143746, 'dA_dEa': 0.0031067647547903345, 'dE0_dEa': 0.0, 'dn_dEa': 0.0025060108812989573, 'name': 'C3H3 + C3H3 <=> C6H6-3'}, {'dA': 0.24929046918134548, 'dE0': 0.0, 'dn': -0.0002816785925963987, 'dA_dEa': 2.2149650596577026, 'dE0_dEa': 0.0, 'dn_dEa': 1.8074629071561377, 'name': 'CH3 + C3H3-2 <=> C4H6'}, {'dA': 0.0025721257372882168, 'dE0': 0.0, 'dn': -0.00026841928599206867, 'dA_dEa': 0.002622276586095329, 'dE0_dEa': 0.0, 'dn_dEa': 0.0021106970635189582, 'name': 'C3H5 + C3H5 <=> C6H10-2'}, {'dA': 0.0025667857812553038, 'dE0': 0.0, 'dn': -0.00027330864163478935, 'dA_dEa': 0.0011598547153825079, 'dE0_dEa': 0.0, 'dn_dEa': 0.0009168315946964314, 'name': 'C3H5 + C2H5 <=> C5H10-2'}, {'dA': 0.0025720870695525367, 'dE0': 0.0, 'dn': -0.00026845472471060864, 'dA_dEa': 0.0011644622972541046, 'dE0_dEa': 0.0, 'dn_dEa': 0.000921050362682896, 'name': 'C3H5 + CH3 <=> C4H8-2'}, {'dA': 0.04545568585357319, 'dE0': 0.0, 'dn': -0.00035603700414837996, 'dA_dEa': 0.1845072119160055, 'dE0_dEa': 0.0, 'dn_dEa': 0.1505370250542775, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}, {'dA': 0.0025720747487414986, 'dE0': 0.0, 'dn': -0.0002684659089105427, 'dA_dEa': -0.00029318060512654076, 'dE0_dEa': 0.0, 'dn_dEa': -0.000268439406230141, 'name': 'C3H3-2 + CH3 <=> C4H6-5'}, {'dA': 0.045546975464110816, 'dE0': 0.0, 'dn': -0.00027245922764262975, 'dA_dEa': -0.00029318060512654076, 'dE0_dEa': 0.0, 'dn_dEa': -0.000268439406230141, 'name': 'C11H23 + CH3 <=> C12H26'}, {'dA': 0.04555234533044019, 'dE0': 0.0, 'dn': -0.00026754593656701513, 'dA_dEa': -0.00011397221655330559, 'dE0_dEa': 0.0, 'dn_dEa': -0.00012221816067028423, 'name': 'C10H21 + C2H5 <=> C12H26-2'}, {'dA': 0.04555144289853321, 'dE0': 0.0, 'dn': -0.0002683722165720251, 'dA_dEa': -0.0010105726531152162, 'dE0_dEa': 0.0, 'dn_dEa': -0.0008538358227983329, 'name': 'C9H19 + C3H7 <=> C12H26-3'}, {'dA': 0.04555229537573315, 'dE0': 0.0, 'dn': -0.00026759159603958316, 'dA_dEa': 0.002218467525239265, 'dE0_dEa': 0.0, 'dn_dEa': 0.0017811588823482374, 'name': 'C8H17 + C4H9-2 <=> C12H26-4'}, {'dA': 0.04555194786349195, 'dE0': 0.0, 'dn': -0.0002679101549779638, 'dA_dEa': -0.001368596777240478, 'dE0_dEa': 0.0, 'dn_dEa': -0.0011459189394939582, 'name': 'C7H15 + C5H11 <=> C12H26-5'}, {'dA': 0.045570240772013236, 'dE0': 0.0, 'dn': -0.00025115443583220633, 'dA_dEa': -0.0015277797835723823, 'dE0_dEa': 0.0, 'dn_dEa': -0.0012738015790732405, 'name': 'C6H13 + C6H13 <=> C12H26-6'}, {'dA': 0.04553765633020181, 'dE0': 0.0, 'dn': -0.0002810014686886708, 'dA_dEa': 0.0009857986569273812, 'dE0_dEa': 0.0, 'dn_dEa': 0.0007775617023600326, 'name': 'CH3 + C9H19 <=> C10H22'}, {'dA': 0.045556277868291105, 'dE0': 0.0, 'dn': -0.00026394519555734627, 'dA_dEa': 0.00401251339354802, 'dE0_dEa': 0.0, 'dn_dEa': 0.003245167137589771, 'name': 'C8H17 + C2H5 <=> C10H22-2'}, {'dA': 0.04555034818665651, 'dE0': 0.0, 'dn': -0.0002693748293846055, 'dA_dEa': 0.0011409508786642964, 'dE0_dEa': 0.0, 'dn_dEa': 0.0009017557850104806, 'name': 'C7H15 + C3H7 <=> C10H22-3'}, {'dA': 0.04555103414461361, 'dE0': 0.0, 'dn': -0.00026874657491894355, 'dA_dEa': 0.0002457003951406293, 'dE0_dEa': 0.0, 'dn_dEa': 0.00017137441546772228, 'name': 'C6H13 + C4H9-2 <=> C10H22-4'}, {'dA': 0.04555660555283727, 'dE0': 0.0, 'dn': -0.0002636420573961646, 'dA_dEa': -0.00011083928441736446, 'dE0_dEa': 0.0, 'dn_dEa': -0.00011934944833553817, 'name': 'C5H11 + C5H11 <=> C10H22-5'}]
""",
)

entry(
    index = 170,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_N-3R!H->C",
    kinetics = ArrheniusBM(A=(2.8686e+06,'m^3/(mol*s)'), n=0.425846, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_N-3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_N-3R!H->C
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_N-3R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_N-3R!H->C
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3S-2 + H <=> CH4S'}]
""",
)

entry(
    index = 171,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_2OS->O",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=1.78837e-07, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_2OS->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_2OS->O
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_2OS->O
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_2OS->O
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'OH + CH3O <=> CH4O2'}]
""",
)

entry(
    index = 172,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O",
    kinetics = ArrheniusBM(A=(2.49263e+08,'m^3/(mol*s)'), n=-0.519467, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00186367249776, var=0.658318197044, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O
        Total Standard Deviation in ln(k): 1.6312606891"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O
Total Standard Deviation in ln(k): 1.6312606891""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O
Total Standard Deviation in ln(k): 1.6312606891
sensitivities = [{'dA': 0.025391023715573578, 'dE0': 0.0, 'dn': -4.6930775265321564e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH3 + C3H7-2 <=> C4H10-2'}, {'dA': 0.025427000291958237, 'dE0': 0.0, 'dn': -3.9813306796405785e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + C3H7-2 <=> C5H12-2'}, {'dA': 0.025348438722264128, 'dE0': 0.0, 'dn': -5.536719899507314e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C3H7-2 + C3H7-2 <=> C6H14-2'}, {'dA': 0.025452891712521325, 'dE0': 0.0, 'dn': -3.469814496981299e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH3 + C3H7-2 <=> C4H10-2'}, {'dA': 0.025376085559972193, 'dE0': 0.0, 'dn': -4.989899075464002e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + C3H7-2 <=> C5H12-2'}, {'dA': 0.025454690145923525, 'dE0': 0.0, 'dn': -3.434560173265479e-05, 'dA_dEa': 0.012812126588103457, 'dE0_dEa': 0.0, 'dn_dEa': 0.0022545017795311583, 'name': 'C3H5 + C3H7-2 <=> C6H12'}, {'dA': 0.0254384726048357, 'dE0': 0.0, 'dn': -3.755049686905581e-05, 'dA_dEa': 0.025865547126360872, 'dE0_dEa': 0.0, 'dn_dEa': 0.004556771120139482, 'name': 'C3H5 + C5H7 <=> C8H12'}, {'dA': 0.4098324816546491, 'dE0': 0.0, 'dn': -4.332861427133539e-05, 'dA_dEa': 3.202390360862137, 'dE0_dEa': 0.0, 'dn_dEa': 0.5647191732363375, 'name': 'C5H11-2 + C3H7-2 <=> C8H18-4'}, {'dA': 0.4095141633620354, 'dE0': 0.0, 'dn': -0.00010631868070245166, 'dA_dEa': 3.459108883479826, 'dE0_dEa': 0.0, 'dn_dEa': 0.6099899984294758, 'name': 'C7H15-3 + CH3 <=> C8H18-5'}]
""",
)

entry(
    index = 173,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing",
    kinetics = ArrheniusBM(A=(2.5021e+10,'m^3/(mol*s)'), n=-0.72284, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21796197679, var=0.116043798991, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing
        Total Standard Deviation in ln(k): 1.23056021221"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing
Total Standard Deviation in ln(k): 1.23056021221""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing
Total Standard Deviation in ln(k): 1.23056021221
sensitivities = [{'dA': 0.011384249177127803, 'dE0': 0.0, 'dn': 9.358720845217343e-06, 'dA_dEa': 0.0014255541422871125, 'dE0_dEa': 0.0, 'dn_dEa': 0.00029488054312227564, 'name': 'C3H3 + H <=> C3H4'}, {'dA': 0.9881961551131391, 'dE0': 0.0, 'dn': 9.09153020297898e-06, 'dA_dEa': 3.913051482534944, 'dE0_dEa': 0.0, 'dn_dEa': 0.806717649372599, 'name': 'C4H5-2 + H <=> C4H6-3'}]
""",
)

entry(
    index = 174,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(9.17499e+07,'m^3/(mol*s)'), n=0.115342, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_Sp-4R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_Sp-4R!H-3C
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_N-Sp-3R!H=2CCNNOO_N-2CNO->O_3R!H->C_Sp-3C-2CN_Ext-3C-R_N-Sp-4R!H=3C_Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.49451088250412784, 'dE0': 0.0, 'dn': 0.00012542069735897845, 'dA_dEa': 1.548592646273221, 'dE0_dEa': 0.0, 'dn_dEa': -0.9048458982946783, 'name': 'C6H7-6 + H <=> C6H8-7'}, {'dA': 0.25240986001409677, 'dE0': 0.0, 'dn': -7.058285262236433e-06, 'dA_dEa': -0.002795355346308123, 'dE0_dEa': 0.0, 'dn_dEa': 0.0016213851683487754, 'name': 'H + C12H25 <=> C12H26-7'}, {'dA': 0.25237247472989505, 'dE0': 0.0, 'dn': 1.7428692015549624e-05, 'dA_dEa': -0.005762081702443491, 'dE0_dEa': 0.0, 'dn_dEa': 0.003355125372190784, 'name': 'H + C10H21 <=> C10H22-6'}]
""",
)

entry(
    index = 175,
    label = "Root",
    kinetics = ArrheniusBM(A=(7.25239e+06,'m^3/(mol*s)'), n=0.211611, w0=(159759,'J/mol'), E0=(7480.68,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0396322771044, var=5.01691061618, Tref=1000.0, N=145, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 2 training reactions at node Root
        Total Standard Deviation in ln(k): 4.58987665919"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 4.58987665919""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 4.58987665919
sensitivities = [{'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': -0.0008058058700300741, 'dE0_dEa': 0.0, 'dn_dEa': 0.00025410363179705406, 'name': '[O][O] + [CH3] <=> CH3O2'}, {'dA': 1.1518768161523799e-06, 'dE0': 0.0, 'dn': 2.8761233453748796e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': '[O][O] + C[CH2] <=> C2H5O2'}, {'dA': 1.0377689818598135e-06, 'dE0': 0.0, 'dn': 2.8801230482664764e-05, 'dA_dEa': -0.0011537061546108723, 'dE0_dEa': 0.0, 'dn_dEa': 0.0003624872136820964, 'name': '[O][O] + [CH2]CC <=> C3H7O2'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': '1-hydroxybutyl + O2 <=> 1-hydroxybutylO2'}, {'dA': 1.2929461945533662e-06, 'dE0': 0.0, 'dn': 2.871180014486214e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'NO2 + NO2 <=> N2O4'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': -0.001128870152911201, 'dE0_dEa': 0.0, 'dn_dEa': 0.00035476144000355365, 'name': 'NO + O2 <=> NO3'}, {'dA': 1.8650592181759074e-06, 'dE0': 0.0, 'dn': 2.85117496751838e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'NO2 + NO3-2 <=> N2O5'}, {'dA': 0.0025399310139565, 'dE0': 0.0, 'dn': 2.8649268736760892e-05, 'dA_dEa': 0.0050481291573595275, 'dE0_dEa': 0.0, 'dn_dEa': -0.0015697111868803698, 'name': 'C5H5 + C2H5 <=> C7H10'}, {'dA': 0.007204004976558392, 'dE0': 0.0, 'dn': 2.7730273305445424e-05, 'dA_dEa': -0.1645422428105018, 'dE0_dEa': 0.0, 'dn_dEa': 0.05126723565002281, 'name': '[CH3] + [O-][N+]=O <=> CH3NO2'}, {'dA': 0.007199241343514811, 'dE0': 0.0, 'dn': 2.9401268059240944e-05, 'dA_dEa': -0.003932252885974641, 'dE0_dEa': 0.0, 'dn_dEa': 0.0012281539622662286, 'name': 'CH3 + CH3 <=> C2H6'}, {'dA': 0.00720054412184447, 'dE0': 0.0, 'dn': 2.894513305726981e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C2H5 <=> C3H8'}, {'dA': 0.0072006367055629395, 'dE0': 0.0, 'dn': 2.8918319745144315e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C2H5 <=> C4H10'}, {'dA': 0.007203929278888038, 'dE0': 0.0, 'dn': 2.7763495565690404e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C5H5 + CH3 <=> C6H8'}, {'dA': 0.007206522212755656, 'dE0': 0.0, 'dn': 2.6854212030665385e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H7 + H <=> C6H8-2'}, {'dA': 0.007204088774415934, 'dE0': 0.0, 'dn': 2.7706478290848996e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H7-2 + H <=> C6H8-3'}, {'dA': 0.007201250086908655, 'dE0': 0.0, 'dn': 2.8698322882097204e-05, 'dA_dEa': -5.133498781618183e-05, 'dE0_dEa': 0.0, 'dn_dEa': 1.8964165882925184e-05, 'name': 'C6H7-3 + H <=> C6H8-4'}, {'dA': 0.0072030322453294935, 'dE0': 0.0, 'dn': 2.807516188853283e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H7-4 + H <=> C6H8-5'}, {'dA': 0.00719868415721771, 'dE0': 0.0, 'dn': 2.959598369220635e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H7-5 + H <=> C6H8-6'}, {'dA': 0.0025416402937852877, 'dE0': 0.0, 'dn': 2.8051488350821668e-05, 'dA_dEa': 0.008125850273544628, 'dE0_dEa': 0.0, 'dn_dEa': -0.002528573856704333, 'name': 'C6H7-6 + H <=> C6H8-7'}, {'dA': 0.007249142525368145, 'dE0': 0.0, 'dn': 1.1957885340888472e-05, 'dA_dEa': -0.06796673631371457, 'dE0_dEa': 0.0, 'dn_dEa': 0.02117688832112701, 'name': 'C[O] + [N]=O <=> CH3ONO'}, {'dA': 0.007215783252690584, 'dE0': 0.0, 'dn': 2.3629635353275742e-05, 'dA_dEa': 0.9885698160730906, 'dE0_dEa': 0.0, 'dn_dEa': -0.3079871296422007, 'name': 'CN + NCN <=> NCNCN'}, {'dA': 0.007190198944685104, 'dE0': 0.0, 'dn': 3.2561790697776394e-05, 'dA_dEa': -0.0797486282113712, 'dE0_dEa': 0.0, 'dn_dEa': 0.024849315528622865, 'name': '[SH] + [O][O] <=> HSOO'}, {'dA': 0.0025403466317189282, 'dE0': 0.0, 'dn': 2.8504049513947484e-05, 'dA_dEa': 0.0019695663748822093, 'dE0_dEa': 0.0, 'dn_dEa': -0.0006105543823221222, 'name': 'OH + NO2-2 <=> HOONO'}, {'dA': 0.007188510059209189, 'dE0': 0.0, 'dn': 3.315679657389452e-05, 'dA_dEa': 0.007251554299259854, 'dE0_dEa': 0.0, 'dn_dEa': -0.0022557979546366457, 'name': '[NH2] + [NH2] <=> N2H4'}, {'dA': 0.007196921799846561, 'dE0': 0.0, 'dn': 3.021105354687051e-05, 'dA_dEa': 0.008293925603198663, 'dE0_dEa': 0.0, 'dn_dEa': -0.0025808266742587123, 'name': 'H + NJCO <=> HNCO'}, {'dA': 0.007201725795270246, 'dE0': 0.0, 'dn': 2.85318317223741e-05, 'dA_dEa': 0.008297730184737366, 'dE0_dEa': 0.0, 'dn_dEa': -0.0025821568353111717, 'name': 'H + NCOJ <=> NCOH'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'NH2 + HO2 <=> NH2OOH'}, {'dA': 5.820140813739913e-06, 'dE0': 0.0, 'dn': 2.712926919539084e-05, 'dA_dEa': -0.0006075563234731576, 'dE0_dEa': 0.0, 'dn_dEa': 0.00019204355345467562, 'name': 'NH2 + O2 <=> NH2OO'}, {'dA': 0.007201393550816075, 'dE0': 0.0, 'dn': 2.8648228816788868e-05, 'dA_dEa': -0.0012220034992795018, 'dE0_dEa': 0.0, 'dn_dEa': 0.0003837717944730865, 'name': 'NH2 + CH3NH <=> CH3NHNH2'}, {'dA': 0.007193643471126957, 'dE0': 0.0, 'dn': 3.1354461817890554e-05, 'dA_dEa': -0.02296878301244729, 'dE0_dEa': 0.0, 'dn_dEa': 0.0071590922255694925, 'name': 'CH3 + NHNH2 <=> CH3NHNH2'}, {'dA': 0.00719561547590865, 'dE0': 0.0, 'dn': 3.066762914578248e-05, 'dA_dEa': 0.017654995337681167, 'dE0_dEa': 0.0, 'dn_dEa': -0.005497382003903701, 'name': '[SH] + [SH] <=> HSSH'}, {'dA': 0.006921617366374074, 'dE0': 0.0, 'dn': 0.00012698943585006886, 'dA_dEa': -0.3667039547768218, 'dE0_dEa': 0.0, 'dn_dEa': 0.11426536265773062, 'name': '[S]S + [H] <=> HSSH'}, {'dA': 0.0024871540649232214, 'dE0': 0.0, 'dn': 4.710389190203866e-05, 'dA_dEa': 0.14692664050743273, 'dE0_dEa': 0.0, 'dn_dEa': -0.04577032101106147, 'name': '[CH2]c1ccccc1[C]=C=C + [H] <=> C10H9'}, {'dA': 0.002550356946074143, 'dE0': 0.0, 'dn': 2.5004564946631905e-05, 'dA_dEa': -0.004746418255763797, 'dE0_dEa': 0.0, 'dn_dEa': 0.0014817826979710064, 'name': 'C3H3 + C7H7 <=> C10H10'}, {'dA': 0.0025426247773910364, 'dE0': 0.0, 'dn': 2.7710731788697677e-05, 'dA_dEa': -0.01232973810871976, 'dE0_dEa': 0.0, 'dn_dEa': 0.00384392577646965, 'name': 'C3H3-2 + C7H7 <=> C10H10-2'}, {'dA': 0.0025353344792480876, 'dE0': 0.0, 'dn': 3.0244292346874462e-05, 'dA_dEa': 0.0541179588946565, 'dE0_dEa': 0.0, 'dn_dEa': -0.016857367247830185, 'name': 'C=C1[CH]c2ccccc2C1 + [H] <=> C10H10-3'}, {'dA': 0.002540050582311717, 'dE0': 0.0, 'dn': 2.860743329278612e-05, 'dA_dEa': -0.014182206964365347, 'dE0_dEa': 0.0, 'dn_dEa': 0.004421564687447601, 'name': 'C=C1[CH]Cc2ccccc21 + [H] <=> C10H10-4'}, {'dA': 0.0025388869193679353, 'dE0': 0.0, 'dn': 2.901396819838511e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C=C1C[CH]c2ccccc21 + [H] <=> C10H10-5'}, {'dA': 0.0025384415529575177, 'dE0': 0.0, 'dn': 2.9170744265057625e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H5 + C3H3 <=> C9H8'}, {'dA': 0.0025384415529575177, 'dE0': 0.0, 'dn': 2.9170744265057625e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H5 + C3H3-2 <=> C9H8-2'}, {'dA': 0.0025384415529575177, 'dE0': 0.0, 'dn': 2.9170744265057625e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C9H7 + H <=> C9H8-3'}, {'dA': 0.0025673955619257057, 'dE0': 0.0, 'dn': 1.9040288108271074e-05, 'dA_dEa': 0.010851627566311835, 'dE0_dEa': 0.0, 'dn_dEa': -0.0033784546572233586, 'name': 'C3H3 + O2 <=> C3H3O2'}, {'dA': 0.002542085013601816, 'dE0': 0.0, 'dn': 2.7891374032627093e-05, 'dA_dEa': -0.020489045445162314, 'dE0_dEa': 0.0, 'dn_dEa': 0.006386469039803051, 'name': 'C3H3-2 + O2 <=> C3H3O2-2'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': -7.17261325888864e-05, 'dE0_dEa': 0.0, 'dn_dEa': 2.539687982919725e-05, 'name': 'C3H3 + H <=> C3H4'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': -2.5307681283950902e-05, 'dE0_dEa': 0.0, 'dn_dEa': 1.0935173806669531e-05, 'name': 'C3H3-2 + H <=> C3H4-2'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0007277909155335129, 'dE0_dEa': 0.0, 'dn_dEa': -0.0002424379557679196, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0003378463482306787, 'dE0_dEa': 0.0, 'dn_dEa': -0.0001097726091906095, 'name': 'C3H3 + C3H3-2 <=> C6H6-2'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H3 + C3H3 <=> C6H6-3'}, {'dA': 0.0071973519784060015, 'dE0': 0.0, 'dn': 3.0062389328544326e-05, 'dA_dEa': 0.06455743423573068, 'dE0_dEa': 0.0, 'dn_dEa': -0.020110056329085992, 'name': 'CH3 + C3H3-2 <=> C4H6'}, {'dA': 0.007203052911464963, 'dE0': 0.0, 'dn': 2.8067561104839953e-05, 'dA_dEa': -0.028666208530484343, 'dE0_dEa': 0.0, 'dn_dEa': 0.008934043471264455, 'name': 'C4H5 + H <=> C4H6-2'}, {'dA': 0.007203481018792329, 'dE0': 0.0, 'dn': 2.7918209583083984e-05, 'dA_dEa': 0.028764977084708546, 'dE0_dEa': 0.0, 'dn_dEa': -0.00895894764696256, 'name': 'C4H5-2 + H <=> C4H6-3'}, {'dA': 0.0025399158900543694, 'dE0': 0.0, 'dn': 2.8654502389065967e-05, 'dA_dEa': 0.0018775178034504529, 'dE0_dEa': 0.0, 'dn_dEa': -0.0005818877486452992, 'name': 'C6H5 + CH3 <=> C7H8'}, {'dA': 0.002539593815243104, 'dE0': 0.0, 'dn': 2.8767307020032875e-05, 'dA_dEa': 0.00036847092133034006, 'dE0_dEa': 0.0, 'dn_dEa': -0.00011170808539265476, 'name': 'C7H7 + H <=> C7H8-2'}, {'dA': 0.0025402039476321602, 'dE0': 0.0, 'dn': 2.8553834883418092e-05, 'dA_dEa': 0.004391580256780032, 'dE0_dEa': 0.0, 'dn_dEa': -0.0013651649142471455, 'name': 'C7H7-2 + H <=> C7H8-3'}, {'dA': 0.002540131148976168, 'dE0': 0.0, 'dn': 2.857925176732133e-05, 'dA_dEa': 0.0033346699339635087, 'dE0_dEa': 0.0, 'dn_dEa': -0.001035876530782047, 'name': 'C7H7-3 + H <=> C7H8-4'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + H <=> H2'}, {'dA': 7.295550830122814e-07, 'dE0': 0.0, 'dn': 2.890891918549344e-05, 'dA_dEa': -0.0005739423887263861, 'dE0_dEa': 0.0, 'dn_dEa': 0.00018191184819861233, 'name': 'H + H <=> H2'}, {'dA': 0.0012556219814997822, 'dE0': 0.0, 'dn': 2.865968850693768e-05, 'dA_dEa': -0.001496219157459842, 'dE0_dEa': 0.0, 'dn_dEa': 0.00046923712215402334, 'name': 'H + CH3 <=> CH4'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C2H5 <=> C2H6-2'}, {'dA': 1.653738479490312e-06, 'dE0': 0.0, 'dn': 2.8585661827357385e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C3H7-2 <=> C3H8-2'}, {'dA': 0.0012545280689836562, 'dE0': 0.0, 'dn': 2.9041950968763024e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C2H3 <=> C2H4'}, {'dA': 1.6035777150593223e-06, 'dE0': 0.0, 'dn': 2.860321259647625e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C2H <=> C2H2'}, {'dA': 0.0012556345918569851, 'dE0': 0.0, 'dn': 2.8655195391068172e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C6H5 <=> C6H6-4'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + CHO <=> CH2O'}, {'dA': 0.0012562340891976438, 'dE0': 0.0, 'dn': 2.844530557166255e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + OH <=> H2O'}, {'dA': 0.001256558521234435, 'dE0': 0.0, 'dn': 2.8332088697627343e-05, 'dA_dEa': -0.005316676126910255, 'dE0_dEa': 0.0, 'dn_dEa': 0.0016594780551282158, 'name': 'CH3 + CH3 <=> C2H6-3'}, {'dA': 1.6813999081934558e-06, 'dE0': 0.0, 'dn': 2.857599315682359e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C2H5 <=> C3H8-3'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C3H7-2 <=> C4H10-2'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C4H9 <=> C5H12'}, {'dA': 0.001256039483976817, 'dE0': 0.0, 'dn': 2.851351873444655e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C2H3 <=> C3H6'}, {'dA': 0.0012547332453040343, 'dE0': 0.0, 'dn': 2.897018495455897e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C6H5 <=> C7H8-5'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + CHO <=> C2H4O'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C2H3O <=> C3H6O'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + OH <=> CH4O'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + CH3O <=> C2H6O'}, {'dA': 1.5881518322659688e-06, 'dE0': 0.0, 'dn': 2.8608598442361832e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C2H5 <=> C4H10-3'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C3H7-2 <=> C5H12-2'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + CHO <=> C3H6O-2'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C2H3O <=> C4H8O'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + OH <=> C2H6O-2'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H7-2 + C3H7-2 <=> C6H14-2'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H7-2 + C4H9 <=> C7H16'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H7-2 + C2H3O <=> C5H10O'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H7-2 + CH3O <=> C4H10O'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C4H9 + C4H9 <=> C8H18'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C4H9 + CHO <=> C5H10O-2'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C4H9 + C2H3O <=> C6H12O'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C4H9 + CH3O <=> C5H12O'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H3 + C2H3 <=> C4H6-4'}, {'dA': 0.001255971316283105, 'dE0': 0.0, 'dn': 2.853733960110323e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H3 + C2H <=> C4H4'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H3 + CHO <=> C3H4O'}, {'dA': 0.001258947351701206, 'dE0': 0.0, 'dn': 2.749682002806906e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C6H5 + C6H5 <=> C12H10'}, {'dA': 0.0012555589758990455, 'dE0': 0.0, 'dn': 2.8681447880273713e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CHO + CHO <=> C2H2O2'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CHO + C2H3O <=> C3H4O2'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H3O + C2H3O <=> C4H6O2'}, {'dA': 1.6329853025355966e-06, 'dE0': 0.0, 'dn': 2.8592918750851012e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'OH + OH <=> H2O2'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3O + CH3O <=> C2H6O2'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + CH3 <=> CH4'}, {'dA': 1.5961560961843072e-06, 'dE0': 0.0, 'dn': 2.8605797941490902e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C4H9 <=> C5H12'}, {'dA': 1.5100507511080493e-06, 'dE0': 0.0, 'dn': 2.8635886820841828e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C3H7-2 <=> C4H10-2'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C3H7-2 <=> C5H12-2'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 1.653738479490312e-06, 'dE0': 0.0, 'dn': 2.8585661827357385e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'OH + CH3O <=> CH4O2'}, {'dA': 1.682922246004822e-06, 'dE0': 0.0, 'dn': 2.8575460548786597e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'O2 + H <=> HO2-2'}, {'dA': 0.06546994813128759, 'dE0': 0.0, 'dn': 2.8539929810752876e-05, 'dA_dEa': 0.18972952277709212, 'dE0_dEa': 0.0, 'dn_dEa': -0.05910778551589839, 'name': 'HSS + CH3 <=> CH4S2'}, {'dA': 0.0656781895624975, 'dE0': 0.0, 'dn': -4.432034400608027e-05, 'dA_dEa': 0.24354477536550528, 'dE0_dEa': 0.0, 'dn_dEa': -0.07587230089866329, 'name': 'CH3S + CH3S <=> C2H6S2'}, {'dA': 0.06546714777756091, 'dE0': 0.0, 'dn': 2.952016821684419e-05, 'dA_dEa': 0.09482136380790586, 'dE0_dEa': 0.0, 'dn_dEa': -0.029538753352467768, 'name': 'CH3S-2 + H <=> CH4S'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'O2 + CH3 <=> CH3O2-2'}, {'dA': 0.06546690713627623, 'dE0': 0.0, 'dn': 2.95871784248891e-05, 'dA_dEa': 0.020405699199701505, 'dE0_dEa': 0.0, 'dn_dEa': -0.006353161341417723, 'name': 'SH + H <=> H2S'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'O2 + C2H5 <=> C2H5O2-2'}, {'dA': 0.0654699481348403, 'dE0': 0.0, 'dn': 2.8539928559846732e-05, 'dA_dEa': 0.18972952277886848, 'dE0_dEa': 0.0, 'dn_dEa': -0.05910778551617637, 'name': 'HSS + C4H9 <=> C4H10S2'}, {'dA': 1.3579608548754226e-06, 'dE0': 0.0, 'dn': 2.868906145100714e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'O2 + C3H7-2 <=> C3H7O2-2'}, {'dA': 0.06549496303166091, 'dE0': 0.0, 'dn': 1.9794209656521382e-05, 'dA_dEa': 0.3385175369992428, 'dE0_dEa': 0.0, 'dn_dEa': -0.10546381016006315, 'name': 'CH3S + C2H5 <=> C3H8S'}, {'dA': 1.633438273529644e-06, 'dE0': 0.0, 'dn': 2.8592793243268184e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'O2 + C4H9 <=> C4H9O2'}, {'dA': 0.06549496302633184, 'dE0': 0.0, 'dn': 1.9794210907427523e-05, 'dA_dEa': 0.33851753699746645, 'dE0_dEa': 0.0, 'dn_dEa': -0.10546381015950718, 'name': 'CH3S + CH3 <=> C2H6S'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'O2 + C2H3 <=> C2H3O2'}, {'dA': 0.0654949630281082, 'dE0': 0.0, 'dn': 1.9794210907427523e-05, 'dA_dEa': 0.33851753699746645, 'dE0_dEa': 0.0, 'dn_dEa': -0.1054638101593682, 'name': 'CH3S + C4H9 <=> C5H12S'}, {'dA': 0.0012558794093565913, 'dE0': 0.0, 'dn': 2.8569372666576675e-05, 'dA_dEa': -0.0017565294871959283, 'dE0_dEa': 0.0, 'dn_dEa': 0.0005502826987767002, 'name': 'O2 + C6H5 <=> C6H5O2'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'O2 + CHO <=> CHO3'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'O2 + C2H3O <=> C2H3O3'}, {'dA': 0.0012554817647726642, 'dE0': 0.0, 'dn': 2.870856961025779e-05, 'dA_dEa': -0.0007316198633589816, 'dE0_dEa': 0.0, 'dn_dEa': 0.00023101100822634836, 'name': 'H + C3H5 <=> C3H6-2'}, {'dA': 1.6575096850603592e-06, 'dE0': 0.0, 'dn': 2.8584349348836158e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C4H7 <=> C4H8'}, {'dA': 1.6575096850603592e-06, 'dE0': 0.0, 'dn': 2.8584349348836158e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C5H9 <=> C5H10'}, {'dA': 1.6575096850603592e-06, 'dE0': 0.0, 'dn': 2.8584349348836158e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C6H9 <=> C6H10'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 3.167565765238927e-06, 'dE0_dEa': 0.0, 'dn_dEa': 2.0621132141316226e-06, 'name': 'C3H5 + C3H5 <=> C6H10-2'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C2H5 <=> C5H10-2'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + CH3 <=> C4H8-2'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C3H7-2 <=> C6H12'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': -3.939797998953488e-05, 'dE0_dEa': 0.0, 'dn_dEa': 1.5324813747247253e-05, 'name': 'C3H5 + C4H9 <=> C7H14'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 3.167565765238927e-06, 'dE0_dEa': 0.0, 'dn_dEa': 2.0621132141316226e-06, 'name': 'C3H5 + C5H7 <=> C8H12'}, {'dA': 0.0012586465576448767, 'dE0': 0.0, 'dn': 2.7602308803964138e-05, 'dA_dEa': 0.005310745423870474, 'dE0_dEa': 0.0, 'dn_dEa': -0.00165156335473235, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}, {'dA': 1.586364817285532e-06, 'dE0': 0.0, 'dn': 2.8609208189610865e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H3-2 + CH3 <=> C4H6-5'}, {'dA': 0.0, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H3-2 + H <=> C3H4-2'}, {'dA': 0.0012555747410659952, 'dE0': 0.0, 'dn': 2.8675492455125187e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C5H5 + H <=> C5H6'}, {'dA': 0.0012558543360798031, 'dE0': 0.0, 'dn': 2.857825257129368e-05, 'dA_dEa': -0.002699321244748218, 'dE0_dEa': 0.0, 'dn_dEa': 0.0008440332882635061, 'name': 'C5H5 + CH3 <=> C6H8'}, {'dA': 1.6797887525401197e-06, 'dE0': 0.0, 'dn': 2.85765566205454e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C5H5 + C5H5 <=> C10H10-6'}, {'dA': 1.6537420322039909e-06, 'dE0': 0.0, 'dn': 2.8585660437461675e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C5H7 <=> C5H8'}, {'dA': 0.0654908728670095, 'dE0': 0.0, 'dn': 2.1226869402229848e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'NO2 + OH <=> HNO3'}, {'dA': 0.0012558353326143352, 'dE0': 0.0, 'dn': 2.858486277631232e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'NO2 + OH <=> HNO3'}, {'dA': 0.0012519266725520553, 'dE0': 0.0, 'dn': 2.995196211419349e-05, 'dA_dEa': -0.0023271635409829803, 'dE0_dEa': 0.0, 'dn_dEa': 0.0007278699390042122, 'name': 'H + SH <=> H2S-2'}, {'dA': 0.01626478423055923, 'dE0': 0.0, 'dn': 4.299746795300779e-05, 'dA_dEa': 0.040350993765874144, 'dE0_dEa': 0.0, 'dn_dEa': -0.012567125932210845, 'name': 'O2 + C6H5 <=> C6H5O2'}, {'dA': 0.01623275488072019, 'dE0': 0.0, 'dn': 5.420725957836808e-05, 'dA_dEa': 0.06687098834490994, 'dE0_dEa': 0.0, 'dn_dEa': -0.02082748524696394, 'name': 'O2 + C10H7 <=> C10H7O2'}, {'dA': 0.016274603821033313, 'dE0': 0.0, 'dn': 3.9563456508068774e-05, 'dA_dEa': 0.04510224214727074, 'dE0_dEa': 0.0, 'dn_dEa': -0.01404705451222028, 'name': 'O2 + C10H7-2 <=> C10H7O2-2'}, {'dA': 0.01616410155058823, 'dE0': 0.0, 'dn': 7.816702282226547e-05, 'dA_dEa': 0.06834800781519632, 'dE0_dEa': 0.0, 'dn_dEa': -0.021283991224609777, 'name': 'O2 + C7H7 <=> C7H7O2'}, {'dA': 0.016304462322482415, 'dE0': 0.0, 'dn': 2.9117394647022116e-05, 'dA_dEa': 0.035185872768299084, 'dE0_dEa': 0.0, 'dn_dEa': -0.01095917539674005, 'name': 'C6H5 + C6H5 <=> C12H10'}, {'dA': 0.016277162739443813, 'dE0': 0.0, 'dn': 3.8673571608512267e-05, 'dA_dEa': 0.010038135904723017, 'dE0_dEa': 0.0, 'dn_dEa': -0.0031239093761954275, 'name': 'H + C12H9 <=> C12H10-2'}, {'dA': 0.0163062989830838, 'dE0': 0.0, 'dn': 2.847664452321722e-05, 'dA_dEa': 0.009863145024270301, 'dE0_dEa': 0.0, 'dn_dEa': -0.0030700580071976375, 'name': 'H + C12H9-2 <=> C12H10-3'}, {'dA': 0.016299873809801486, 'dE0': 0.0, 'dn': 3.07225909038548e-05, 'dA_dEa': -0.0010484279719947854, 'dE0_dEa': 0.0, 'dn_dEa': 0.00032986821918547406, 'name': 'H + C12H9-3 <=> C12H10-4'}, {'dA': 0.0012557828128480215, 'dE0': 0.0, 'dn': 2.8603221630798384e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C11H23 + CH3 <=> C12H26'}, {'dA': 0.0012555873336596297, 'dE0': 0.0, 'dn': 2.8671762530991366e-05, 'dA_dEa': -7.800622903176595e-05, 'dE0_dEa': 0.0, 'dn_dEa': 2.74032824094467e-05, 'name': 'C10H21 + C2H5 <=> C12H26-2'}, {'dA': 0.0012548433456772972, 'dE0': 0.0, 'dn': 2.8931524310370478e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C9H19 + C3H7 <=> C12H26-3'}, {'dA': 0.0012548737338137488, 'dE0': 0.0, 'dn': 2.8921046025584206e-05, 'dA_dEa': -8.790296490702589e-06, 'dE0_dEa': 0.0, 'dn_dEa': 5.794573490656783e-06, 'name': 'C8H17 + C4H9-2 <=> C12H26-4'}, {'dA': 0.0012557720818763547, 'dE0': 0.0, 'dn': 2.860696503692061e-05, 'dA_dEa': -0.00011352460482784295, 'dE0_dEa': 0.0, 'dn_dEa': 3.84261243051451e-05, 'name': 'C7H15 + C5H11 <=> C12H26-5'}, {'dA': 0.0012562462412547821, 'dE0': 0.0, 'dn': 2.8441249716984173e-05, 'dA_dEa': -0.00011851970782573912, 'dE0_dEa': 0.0, 'dn_dEa': 3.997338609495575e-05, 'name': 'C6H13 + C6H13 <=> C12H26-6'}, {'dA': 0.0012569289520315825, 'dE0': 0.0, 'dn': 2.8202554725907603e-05, 'dA_dEa': 9.330712202882869e-05, 'dE0_dEa': 0.0, 'dn_dEa': -3.425057139104532e-05, 'name': 'H + C12H25 <=> C12H26-7'}, {'dA': 0.001255117455301185, 'dE0': 0.0, 'dn': 2.883593645658274e-05, 'dA_dEa': -4.089837091215027e-05, 'dE0_dEa': 0.0, 'dn_dEa': 1.5824544357123356e-05, 'name': 'H + C12H25-2 <=> C12H26-8'}, {'dA': 0.001255117455301185, 'dE0': 0.0, 'dn': 2.883593645658274e-05, 'dA_dEa': -4.089837091215027e-05, 'dE0_dEa': 0.0, 'dn_dEa': 1.5824544357123356e-05, 'name': 'H + C12H25-3 <=> C12H26-9'}, {'dA': 0.001255117455301185, 'dE0': 0.0, 'dn': 2.883593645658274e-05, 'dA_dEa': -4.089837091215027e-05, 'dE0_dEa': 0.0, 'dn_dEa': 1.5824544357123356e-05, 'name': 'H + C12H25-4 <=> C12H26-10'}, {'dA': 0.001255117455301185, 'dE0': 0.0, 'dn': 2.883593645658274e-05, 'dA_dEa': -4.089837091215027e-05, 'dE0_dEa': 0.0, 'dn_dEa': 1.5824544357123356e-05, 'name': 'H + C12H25-5 <=> C12H26-11'}, {'dA': 0.001255117455301185, 'dE0': 0.0, 'dn': 2.883593645658274e-05, 'dA_dEa': -4.089837091215027e-05, 'dE0_dEa': 0.0, 'dn_dEa': 1.5824544357123356e-05, 'name': 'H + C12H25-6 <=> C12H26-12'}, {'dA': 0.0012559209032760028, 'dE0': 0.0, 'dn': 2.855497807264155e-05, 'dA_dEa': -4.5387920977196244e-05, 'dE0_dEa': 0.0, 'dn_dEa': 1.719485782883947e-05, 'name': 'CH3 + C9H19 <=> C10H22'}, {'dA': 0.0012543822212053573, 'dE0': 0.0, 'dn': 2.909283463382558e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C8H17 + C2H5 <=> C10H22-2'}, {'dA': 0.0012563176099435187, 'dE0': 0.0, 'dn': 2.8416195734851443e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C7H15 + C3H7 <=> C10H22-3'}, {'dA': 0.0012558442676892374, 'dE0': 0.0, 'dn': 2.8582022663413587e-05, 'dA_dEa': -6.663028351284362e-05, 'dE0_dEa': 0.0, 'dn_dEa': 2.38246856731287e-05, 'name': 'C6H13 + C4H9-2 <=> C10H22-4'}, {'dA': 0.0012550257189049279, 'dE0': 0.0, 'dn': 2.8868074598172046e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C5H11 + C5H11 <=> C10H22-5'}, {'dA': 0.001256200185651007, 'dE0': 0.0, 'dn': 2.845749996068494e-05, 'dA_dEa': -0.000112758014481086, 'dE0_dEa': 0.0, 'dn_dEa': 3.815820328197586e-05, 'name': 'H + C10H21 <=> C10H22-6'}, {'dA': 0.001256200185651007, 'dE0': 0.0, 'dn': 2.845749996068494e-05, 'dA_dEa': -0.000112758014481086, 'dE0_dEa': 0.0, 'dn_dEa': 3.815820328197586e-05, 'name': 'H + C10H21-2 <=> C10H22-7'}, {'dA': 0.001256200185651007, 'dE0': 0.0, 'dn': 2.845749996068494e-05, 'dA_dEa': -0.000112758014481086, 'dE0_dEa': 0.0, 'dn_dEa': 3.815820328197586e-05, 'name': 'H + C10H21-3 <=> C10H22-8'}, {'dA': 0.001256200185651007, 'dE0': 0.0, 'dn': 2.845749996068494e-05, 'dA_dEa': -0.000112758014481086, 'dE0_dEa': 0.0, 'dn_dEa': 3.815820328197586e-05, 'name': 'H + C10H21-4 <=> C10H22-9'}, {'dA': 0.001256200185651007, 'dE0': 0.0, 'dn': 2.845749996068494e-05, 'dA_dEa': -0.000112758014481086, 'dE0_dEa': 0.0, 'dn_dEa': 3.815820328197586e-05, 'name': 'H + C10H21-5 <=> C10H22-10'}, {'dA': 0.0012553742294586774, 'dE0': 0.0, 'dn': 2.8746541144152067e-05, 'dA_dEa': -0.004355023994762544, 'dE0_dEa': 0.0, 'dn_dEa': 0.001359930869157544, 'name': 'CH3 + C7H15-2 <=> C8H18-2'}, {'dA': 0.0012562345830248452, 'dE0': 0.0, 'dn': 2.844417169474037e-05, 'dA_dEa': 0.008458261980593783, 'dE0_dEa': 0.0, 'dn_dEa': -0.00263223791593578, 'name': 'C4H9-3 + C4H9 <=> C8H18-3'}, {'dA': 0.0012537194553631497, 'dE0': 0.0, 'dn': 2.9324439071925294e-05, 'dA_dEa': 0.010366049119526797, 'dE0_dEa': 0.0, 'dn_dEa': -0.0032265047548988316, 'name': 'C5H11-2 + C3H7-2 <=> C8H18-4'}, {'dA': 0.001257211872385394, 'dE0': 0.0, 'dn': 2.8104230723420425e-05, 'dA_dEa': 0.011205469117926537, 'dE0_dEa': 0.0, 'dn_dEa': -0.0034880986243383274, 'name': 'C7H15-3 + CH3 <=> C8H18-5'}]
""",
)

entry(
    index = 176,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.76793e+10,'m^3/(mol*s)'), n=-1.00291, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing_Ext-2R-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing_Ext-2R-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing_Ext-2R-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C5H5 + C2H5 <=> C7H10'}]
""",
)

entry(
    index = 177,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(101631,'m^3/(mol*s)'), n=0.35323, w0=(139000,'J/mol'), E0=(13900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0148472730165, var=2.75207767881, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R
        Total Standard Deviation in ln(k): 3.36303735057"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.36303735057""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.36303735057
sensitivities = [{'dA': 0.001222826540470258, 'dE0': 0.0, 'dn': -1.939949450067826e-05, 'dA_dEa': -0.014750066702264267, 'dE0_dEa': 0.0, 'dn_dEa': 0.0041450960563314, 'name': '[O][O] + [CH2]CC <=> C3H7O2'}, {'dA': 0.0012235331503519756, 'dE0': 0.0, 'dn': -1.962243426457845e-05, 'dA_dEa': 0.0026332660034714254, 'dE0_dEa': 0.0, 'dn_dEa': -0.0007407257727242003, 'name': '1-hydroxybutyl + O2 <=> 1-hydroxybutylO2'}, {'dA': 0.036284019769187825, 'dE0': 0.0, 'dn': -9.651052219093978e-06, 'dA_dEa': 0.15094374863268697, 'dE0_dEa': 0.0, 'dn_dEa': -0.042424009979462815, 'name': 'C3H3 + O2 <=> C3H3O2'}, {'dA': 0.03624964110216355, 'dE0': 0.0, 'dn': 1.1954261437541586e-06, 'dA_dEa': -0.28211272993597714, 'dE0_dEa': 0.0, 'dn_dEa': 0.07929320413056905, 'name': 'C3H3-2 + O2 <=> C3H3O2-2'}, {'dA': 0.018559309451051487, 'dE0': 0.0, 'dn': -1.892454138483491e-05, 'dA_dEa': -0.023088718384303476, 'dE0_dEa': 0.0, 'dn_dEa': 0.00648876279204512, 'name': 'O2 + C6H5 <=> C6H5O2'}, {'dA': 0.22655377214244873, 'dE0': 0.0, 'dn': 4.142294784337739e-07, 'dA_dEa': 0.5594995969940347, 'dE0_dEa': 0.0, 'dn_dEa': -0.1572556804766365, 'name': 'O2 + C6H5 <=> C6H5O2'}, {'dA': 0.22661906952594899, 'dE0': 0.0, 'dn': -2.0156078111103728e-05, 'dA_dEa': 0.9268437200003942, 'dE0_dEa': 0.0, 'dn_dEa': -0.2605024335182557, 'name': 'O2 + C10H7 <=> C10H7O2'}, {'dA': 0.22666217192759683, 'dE0': 0.0, 'dn': -3.375142566677481e-05, 'dA_dEa': 0.6253016052256277, 'dE0_dEa': 0.0, 'dn_dEa': -0.17575014935221497, 'name': 'O2 + C10H7-2 <=> C10H7O2-2'}, {'dA': 0.22656109675447675, 'dE0': 0.0, 'dn': -1.9119345458818487e-06, 'dA_dEa': 0.9485077982384006, 'dE0_dEa': 0.0, 'dn_dEa': -0.2665880340888157, 'name': 'O2 + C7H7 <=> C7H7O2'}]
""",
)

entry(
    index = 178,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R",
    kinetics = ArrheniusBM(A=(164141,'m^3/(mol*s)'), n=0.637502, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0311760265022, var=0.946024688451, Tref=1000.0, N=48, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R
        Total Standard Deviation in ln(k): 2.02821325078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R
Total Standard Deviation in ln(k): 2.02821325078""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R
Total Standard Deviation in ln(k): 2.02821325078
sensitivities = [{'dA': 0.01896419017733062, 'dE0': 0.0, 'dn': 7.332824013422182e-06, 'dA_dEa': -0.001562494874818471, 'dE0_dEa': 0.0, 'dn_dEa': 0.0002713869343853001, 'name': 'CH3 + C2H5 <=> C3H8'}, {'dA': 0.018963451436706392, 'dE0': 0.0, 'dn': 7.476347514186852e-06, 'dA_dEa': 0.00020235566111639355, 'dE0_dEa': 0.0, 'dn_dEa': -3.427706467545872e-05, 'name': 'C2H5 + C2H5 <=> C4H10'}, {'dA': 0.006807622868976931, 'dE0': 0.0, 'dn': 6.4333340290300176e-06, 'dA_dEa': -0.012204089244961759, 'dE0_dEa': 0.0, 'dn_dEa': 0.0021140111357958453, 'name': 'C3H3 + C7H7 <=> C10H10'}, {'dA': 0.006793338354072669, 'dE0': 0.0, 'dn': 9.204336083435525e-06, 'dA_dEa': -0.03203368840765461, 'dE0_dEa': 0.0, 'dn_dEa': 0.005548059053642183, 'name': 'C3H3-2 + C7H7 <=> C10H10-2'}, {'dA': 0.00017973232857572999, 'dE0': 0.0, 'dn': 7.472945981045959e-06, 'dA_dEa': 0.000839607988467698, 'dE0_dEa': 0.0, 'dn_dEa': -0.00014456746150635395, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}, {'dA': 0.00017986358180623646, 'dE0': 0.0, 'dn': 7.4474678550891166e-06, 'dA_dEa': 0.0005343386817458529, 'dE0_dEa': 0.0, 'dn_dEa': -9.170686830906681e-05, 'name': 'C3H3 + C3H3-2 <=> C6H6-2'}, {'dA': 0.00017984490696678384, 'dE0': 0.0, 'dn': 7.451088936676286e-06, 'dA_dEa': 0.00022055999160388792, 'dE0_dEa': 0.0, 'dn_dEa': -3.7372259752575115e-05, 'name': 'C3H3 + C3H3 <=> C6H6-3'}, {'dA': 0.018965672241579724, 'dE0': 0.0, 'dn': 7.043907991798119e-06, 'dA_dEa': 0.16859704339824058, 'dE0_dEa': 0.0, 'dn_dEa': -0.029194052653570793, 'name': 'CH3 + C3H3-2 <=> C4H6'}, {'dA': 0.00017986047851083803, 'dE0': 0.0, 'dn': 7.448067016858756e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C2H5 <=> C3H8-3'}, {'dA': 0.0001798486159998645, 'dE0': 0.0, 'dn': 7.450368644729391e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C3H7-2 <=> C4H10-2'}, {'dA': 0.00017985798628219235, 'dE0': 0.0, 'dn': 7.448558181187194e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C4H9 <=> C5H12'}, {'dA': 0.0034510522155532432, 'dE0': 0.0, 'dn': 7.6060199954862286e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C2H3 <=> C3H6'}, {'dA': 0.00017984606692779997, 'dE0': 0.0, 'dn': 7.4508632081189264e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + CHO <=> C2H4O'}, {'dA': 0.00017981638222865675, 'dE0': 0.0, 'dn': 7.456614728499689e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C2H3O <=> C3H6O'}, {'dA': 0.00017984387845617383, 'dE0': 0.0, 'dn': 7.451287318242097e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C2H5 <=> C4H10-3'}, {'dA': 0.0001798242159623185, 'dE0': 0.0, 'dn': 7.455092103631251e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C3H7-2 <=> C5H12-2'}, {'dA': 0.00017981051669837305, 'dE0': 0.0, 'dn': 7.4577633021447385e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.00017984606692779997, 'dE0': 0.0, 'dn': 7.4508632081189264e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + CHO <=> C3H6O-2'}, {'dA': 0.0001798534761121771, 'dE0': 0.0, 'dn': 7.4494305038667675e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C2H3O <=> C4H8O'}, {'dA': 0.00017980342548187017, 'dE0': 0.0, 'dn': 7.4591243171083155e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H7-2 + C3H7-2 <=> C6H14-2'}, {'dA': 0.00017960205944691257, 'dE0': 0.0, 'dn': 7.498175203028874e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H7-2 + C4H9 <=> C7H16'}, {'dA': 0.0001798751476656178, 'dE0': 0.0, 'dn': 7.445244869132032e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H7-2 + C2H3O <=> C5H10O'}, {'dA': 0.00018001613177889047, 'dE0': 0.0, 'dn': 7.417765932211592e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C4H9 + C4H9 <=> C8H18'}, {'dA': 0.00017984700306785433, 'dE0': 0.0, 'dn': 7.450682439869705e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C4H9 + CHO <=> C5H10O-2'}, {'dA': 0.00017975147770245872, 'dE0': 0.0, 'dn': 7.469172250715004e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C4H9 + C2H3O <=> C6H12O'}, {'dA': 0.00017979678901271817, 'dE0': 0.0, 'dn': 7.460425539497151e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H3 + C2H3 <=> C4H6-4'}, {'dA': 0.0034517421330097415, 'dE0': 0.0, 'dn': 7.472056817563681e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H3 + C2H <=> C4H4'}, {'dA': 0.00017984606692779997, 'dE0': 0.0, 'dn': 7.4508632081189264e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H3 + CHO <=> C3H4O'}, {'dA': 0.0034517144342775447, 'dE0': 0.0, 'dn': 7.4775041219763105e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CHO + CHO <=> C2H2O2'}, {'dA': 0.00017984606692779997, 'dE0': 0.0, 'dn': 7.4508632081189264e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CHO + C2H3O <=> C3H4O2'}, {'dA': 0.00017984700306785433, 'dE0': 0.0, 'dn': 7.450682439869705e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H3O + C2H3O <=> C4H6O2'}, {'dA': 0.00017984091726932255, 'dE0': 0.0, 'dn': 7.4518605235451815e-06, 'dA_dEa': -0.0005470064685653745, 'dE0_dEa': 0.0, 'dn_dEa': 9.55424528998223e-05, 'name': 'CH3 + C4H9 <=> C5H12'}, {'dA': 0.0001798744531100936, 'dE0': 0.0, 'dn': 7.445369243867608e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH3 + C3H7-2 <=> C4H10-2'}, {'dA': 0.00018023132142277228, 'dE0': 0.0, 'dn': 7.376031333052602e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C3H7-2 <=> C5H12-2'}, {'dA': 0.00017993246537175472, 'dE0': 0.0, 'dn': 7.434001084030499e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H5 + C4H9 <=> C6H14'}, {'dA': 0.17096101310622663, 'dE0': 0.0, 'dn': 1.08484080143237e-05, 'dA_dEa': 0.4951404128288862, 'dE0_dEa': 0.0, 'dn_dEa': -0.08573905676797665, 'name': 'HSS + CH3 <=> CH4S2'}, {'dA': 0.17096101310622663, 'dE0': 0.0, 'dn': 1.08484080143237e-05, 'dA_dEa': 0.4951404128288862, 'dE0_dEa': 0.0, 'dn_dEa': -0.08573905676797665, 'name': 'HSS + C4H9 <=> C4H10S2'}, {'dA': 0.17098377554349503, 'dE0': 0.0, 'dn': 6.449661264504083e-06, 'dA_dEa': 0.8832747678334392, 'dE0_dEa': 0.0, 'dn_dEa': -0.15294991294591034, 'name': 'CH3S + C2H5 <=> C3H8S'}, {'dA': 0.1709722327607654, 'dE0': 0.0, 'dn': 8.724606351028415e-06, 'dA_dEa': 0.8832747678334392, 'dE0_dEa': 0.0, 'dn_dEa': -0.15294991294591034, 'name': 'CH3S + CH3 <=> C2H6S'}, {'dA': 0.1709722327607654, 'dE0': 0.0, 'dn': 8.724606351028415e-06, 'dA_dEa': 0.8832747678334392, 'dE0_dEa': 0.0, 'dn_dEa': -0.15294991294575583, 'name': 'CH3S + C4H9 <=> C5H12S'}, {'dA': 0.00017984208966483655, 'dE0': 0.0, 'dn': 7.451637267032255e-06, 'dA_dEa': 0.00018364514531301414, 'dE0_dEa': 0.0, 'dn_dEa': -3.0979988390126434e-05, 'name': 'C3H5 + C3H5 <=> C6H10-2'}, {'dA': 0.00017984761591096393, 'dE0': 0.0, 'dn': 7.450562700217443e-06, 'dA_dEa': 7.267185253568533e-05, 'dE0_dEa': 0.0, 'dn_dEa': -1.1763224674205351e-05, 'name': 'C3H5 + C2H5 <=> C5H10-2'}, {'dA': 0.00017986296541041319, 'dE0': 0.0, 'dn': 7.447592229824692e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + CH3 <=> C4H8-2'}, {'dA': 0.00017987432165968747, 'dE0': 0.0, 'dn': 7.445390874256403e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H5 + C3H7-2 <=> C6H12'}, {'dA': 0.0001796804589560195, 'dE0': 0.0, 'dn': 7.483121379443765e-06, 'dA_dEa': 7.273434476929543e-05, 'dE0_dEa': 0.0, 'dn_dEa': -1.1775315907039345e-05, 'name': 'C3H5 + C4H9 <=> C7H14'}, {'dA': 0.00017984208966483655, 'dE0': 0.0, 'dn': 7.451637267032255e-06, 'dA_dEa': 0.00018364514531301414, 'dE0_dEa': 0.0, 'dn_dEa': -3.0979988390126434e-05, 'name': 'C3H5 + C5H7 <=> C8H12'}, {'dA': 0.0034544627087744113, 'dE0': 0.0, 'dn': 6.943442251975625e-06, 'dA_dEa': 0.014029411328665855, 'dE0_dEa': 0.0, 'dn_dEa': -0.002428586968754456, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}, {'dA': 0.00017988219802591337, 'dE0': 0.0, 'dn': 7.44386268728799e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C3H3-2 + CH3 <=> C4H6-5'}, {'dA': 0.003451891680939337, 'dE0': 0.0, 'dn': 7.4431196834328595e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C11H23 + CH3 <=> C12H26'}, {'dA': 0.0034520751288628555, 'dE0': 0.0, 'dn': 7.407654343460735e-06, 'dA_dEa': -2.434630630432634e-05, 'dE0_dEa': 0.0, 'dn_dEa': 5.030940904200079e-06, 'name': 'C10H21 + C2H5 <=> C12H26-2'}, {'dA': 0.0034521284515424606, 'dE0': 0.0, 'dn': 7.397361986460655e-06, 'dA_dEa': -9.283938595673247e-05, 'dE0_dEa': 0.0, 'dn_dEa': 1.6895724116370435e-05, 'name': 'C9H19 + C3H7 <=> C12H26-3'}, {'dA': 0.0034518221117000787, 'dE0': 0.0, 'dn': 7.456647483088437e-06, 'dA_dEa': 0.00015278925147301243, 'dE0_dEa': 0.0, 'dn_dEa': -2.5634116750200537e-05, 'name': 'C8H17 + C4H9-2 <=> C12H26-4'}, {'dA': 0.003452373455559535, 'dE0': 0.0, 'dn': 7.349627426455305e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C7H15 + C5H11 <=> C12H26-5'}, {'dA': 0.0034518934572961763, 'dE0': 0.0, 'dn': 7.442799244673131e-06, 'dA_dEa': -0.00013386451591658553, 'dE0_dEa': 0.0, 'dn_dEa': 2.4000867120837933e-05, 'name': 'C6H13 + C6H13 <=> C12H26-6'}, {'dA': 0.003451871005922083, 'dE0': 0.0, 'dn': 7.447147107323833e-06, 'dA_dEa': 5.7282745657977954e-05, 'dE0_dEa': 0.0, 'dn_dEa': -9.097862966633368e-06, 'name': 'CH3 + C9H19 <=> C10H22'}, {'dA': 0.0034517198663767596, 'dE0': 0.0, 'dn': 7.476511596136146e-06, 'dA_dEa': 0.0002893187343034106, 'dE0_dEa': 0.0, 'dn_dEa': -4.927540816734121e-05, 'name': 'C8H17 + C2H5 <=> C10H22-2'}, {'dA': 0.003451748463945517, 'dE0': 0.0, 'dn': 7.4708808969270836e-06, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C7H15 + C3H7 <=> C10H22-3'}, {'dA': 0.0034517602394150055, 'dE0': 0.0, 'dn': 7.468589311736961e-06, 'dA_dEa': 2.6250202012082064e-06, 'dE0_dEa': 0.0, 'dn_dEa': 3.6737268634420596e-07, 'name': 'C6H13 + C4H9-2 <=> C10H22-4'}, {'dA': 0.00345184653127755, 'dE0': 0.0, 'dn': 7.451896059183917e-06, 'dA_dEa': -2.4628956651898065e-05, 'dE0_dEa': 0.0, 'dn_dEa': 5.085633496772658e-06, 'name': 'C5H11 + C5H11 <=> C10H22-5'}, {'dA': 0.003448302942743833, 'dE0': 0.0, 'dn': 8.140452054140875e-06, 'dA_dEa': -0.011181439509401325, 'dE0_dEa': 0.0, 'dn_dEa': 0.0019370190676290587, 'name': 'CH3 + C7H15-2 <=> C8H18-2'}, {'dA': 0.003445674222391328, 'dE0': 0.0, 'dn': 8.652715281821638e-06, 'dA_dEa': 0.022236327650307038, 'dE0_dEa': 0.0, 'dn_dEa': -0.0038497032215454555, 'name': 'C4H9-3 + C4H9 <=> C8H18-3'}, {'dA': 0.003450120560799899, 'dE0': 0.0, 'dn': 7.785838979644447e-06, 'dA_dEa': 0.02721877334011269, 'dE0_dEa': 0.0, 'dn_dEa': -0.004712435901692068, 'name': 'C5H11-2 + C3H7-2 <=> C8H18-4'}, {'dA': 0.0034618245443599964, 'dE0': 0.0, 'dn': 5.507963284443859e-06, 'dA_dEa': 0.02939663027845864, 'dE0_dEa': 0.0, 'dn_dEa': -0.005089412311481002, 'name': 'C7H15-3 + CH3 <=> C8H18-5'}]
""",
)

entry(
    index = 179,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_N-Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(578146,'m^3/(mol*s)'), n=0.175759, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.614494871354, var=0.864366397977, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_N-Sp-5R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_N-Sp-5R!H-1C
        Total Standard Deviation in ln(k): 3.40778537242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 3.40778537242""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 3.40778537242
sensitivities = [{'dA': 0.05877447042302401, 'dE0': 0.0, 'dn': 9.166401033252247e-06, 'dA_dEa': 0.23661813168554366, 'dE0_dEa': 0.0, 'dn_dEa': -0.09863622986497352, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}, {'dA': 0.940689058023129, 'dE0': 0.0, 'dn': 7.981236550676056e-06, 'dA_dEa': 3.7911949779876064, 'dE0_dEa': 0.0, 'dn_dEa': -1.5803954607003972, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}]
""",
)

entry(
    index = 180,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_4R!H->O",
    kinetics = ArrheniusBM(A=(1.505e+06,'m^3/(mol*s)'), n=1.79841e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_4R!H->O
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_4R!H->O
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_4R!H->O
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'O2 + C2H3O <=> C2H3O3'}]
""",
)

entry(
    index = 181,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H",
    kinetics = ArrheniusBM(A=(5.67927e+10,'m^3/(mol*s)'), n=-1.26686, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.103891372706, var=0.0257351059192, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H
        Total Standard Deviation in ln(k): 0.582636509508"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H
Total Standard Deviation in ln(k): 0.582636509508""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H
Total Standard Deviation in ln(k): 0.582636509508
sensitivities = [{'dA': 0.9686268323997284, 'dE0': 0.0, 'dn': 1.424296573223854e-06, 'dA_dEa': -1.7233634402027087, 'dE0_dEa': 0.0, 'dn_dEa': -0.16266994202660398, 'name': 'C3H3 + C7H7 <=> C10H10'}, {'dA': 0.030840947161440212, 'dE0': 0.0, 'dn': -4.86564829369861e-06, 'dA_dEa': 0.03666300242600022, 'dE0_dEa': 0.0, 'dn_dEa': 0.003460807433447082, 'name': 'C3H3 + C3H3 <=> C6H6-3'}]
""",
)

entry(
    index = 182,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_N-2OS->O",
    kinetics = ArrheniusBM(A=(2.85887e+07,'m^3/(mol*s)'), n=0.338251, w0=(71000,'J/mol'), E0=(24020.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_N-2OS->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_N-2OS->O
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_N-2OS->O
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_N-2OS->O
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.6438132239820088, 'dn_dEa': 0.0, 'name': '[SH] + [O][O] <=> HSOO'}]
""",
)

entry(
    index = 183,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-2CNO-R_Ext-3CS-R",
    kinetics = ArrheniusBM(A=(1.52804e+49,'m^3/(mol*s)'), n=-12.7885, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-2CNO-R_Ext-3CS-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-2CNO-R_Ext-3CS-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-2CNO-R_Ext-3CS-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_N-2CNO-inRing_Ext-2CNO-R_Sp-3R!H=2CCNNOO_N-3R!H->O_Ext-2CNO-R_Ext-3CS-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': '[CH2]c1ccccc1[C]=C=C + [H] <=> C10H9'}]
""",
)

entry(
    index = 184,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2CNO",
    kinetics = ArrheniusBM(A=(3.68011e+07,'m^3/(mol*s)'), n=-0.486361, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0713195572652, var=0.229115083648, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2CNO',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2CNO
        Total Standard Deviation in ln(k): 1.13878070638"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2CNO
Total Standard Deviation in ln(k): 1.13878070638""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_Sp-4R!H-3R!H_Ext-5R!H-R_Ext-6R!H-R_Int-6R!H-2CNO
Total Standard Deviation in ln(k): 1.13878070638
sensitivities = [{'dA': 0.3332783407295293, 'dE0': 0.0, 'dn': 2.471344118076718e-05, 'dA_dEa': 6.88880709766058, 'dE0_dEa': 0.0, 'dn_dEa': 1.3574069904657802, 'name': 'C=C1[CH]c2ccccc2C1 + [H] <=> C10H10-3'}, {'dA': 0.3345131758579014, 'dE0': 0.0, 'dn': 0.0002976721733350956, 'dA_dEa': -1.7902672525133863, 'dE0_dEa': 0.0, 'dn_dEa': -0.3527233020057945, 'name': 'C=C1[CH]Cc2ccccc21 + [H] <=> C10H10-4'}, {'dA': 0.33457141094221177, 'dE0': 0.0, 'dn': 0.0003105734082504106, 'dA_dEa': -0.04416468969737284, 'dE0_dEa': 0.0, 'dn_dEa': -0.008668969649522263, 'name': 'C=C1C[CH]c2ccccc21 + [H] <=> C10H10-5'}]
""",
)

entry(
    index = 185,
    label = "Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(3.01298e+07,'m^3/(mol*s)'), n=0.213298, w0=(208833,'J/mol'), E0=(20883.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0012800000741, var=0.535898560478, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H
        Total Standard Deviation in ln(k): 1.47078425342"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 1.47078425342""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2CHNO->H_2CNO-inRing_Ext-2CNO-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 1.47078425342
sensitivities = [{'dA': 0.12140719384846847, 'dE0': 0.0, 'dn': 5.22128330297228e-05, 'dA_dEa': 0.010381801391902179, 'dE0_dEa': 0.0, 'dn_dEa': -0.0061948240027716915, 'name': 'C6H7 + H <=> C6H8-2'}, {'dA': 0.12145731004765908, 'dE0': 0.0, 'dn': 1.8631187487617874e-05, 'dA_dEa': -0.001023637729247297, 'dE0_dEa': 0.0, 'dn_dEa': 0.0006166507392748987, 'name': 'C6H7-2 + H <=> C6H8-3'}, {'dA': 0.1215058014700921, 'dE0': 0.0, 'dn': -1.386056274328655e-05, 'dA_dEa': 0.0018161610881863633, 'dE0_dEa': 0.0, 'dn_dEa': -0.001078472493344166, 'name': 'C6H7-4 + H <=> C6H8-5'}, {'dA': 0.043648255061872566, 'dE0': 0.0, 'dn': 5.7876751853650254e-05, 'dA_dEa': 0.05686232299596044, 'dE0_dEa': 0.0, 'dn_dEa': -0.03395106731681494, 'name': 'C7H7-3 + H <=> C7H8-4'}, {'dA': 0.022222267119789366, 'dE0': 0.0, 'dn': 6.11848749540302e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'H + C6H5 <=> C6H6-4'}, {'dA': 0.02226436591002102, 'dE0': 0.0, 'dn': 3.297467050093923e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C5H5 + H <=> C5H6'}, {'dA': 0.27334049232055857, 'dE0': 0.0, 'dn': 6.925727959447928e-07, 'dA_dEa': 0.1656938951555458, 'dE0_dEa': 0.0, 'dn_dEa': -0.09895152779469525, 'name': 'H + C12H9-2 <=> C12H10-3'}, {'dA': 0.27324832617029127, 'dE0': 0.0, 'dn': 6.245332117407332e-05, 'dA_dEa': -0.01612967924558184, 'dE0_dEa': 0.0, 'dn_dEa': 0.009639453377094242, 'name': 'H + C12H9-3 <=> C12H10-4'}]
""",
)

entry(
    index = 186,
    label = "Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(297.12,'m^3/(mol*s)'), n=0.971996, w0=(122000,'J/mol'), E0=(12200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0290918489436, var=0.0160072644778, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H
        Total Standard Deviation in ln(k): 0.326733816017"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 0.326733816017""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 0.326733816017
sensitivities = [{'dA': 0.1379581874872012, 'dE0': 0.0, 'dn': -1.215579049462196e-05, 'dA_dEa': 0.5740260736689172, 'dE0_dEa': 0.0, 'dn_dEa': -0.06496909835509172, 'name': 'C3H3 + O2 <=> C3H3O2'}, {'dA': 0.8616211484940689, 'dE0': 0.0, 'dn': 2.1503722037993457e-06, 'dA_dEa': 3.607573433443043, 'dE0_dEa': 0.0, 'dn_dEa': -0.40830589692479763, 'name': 'O2 + C7H7 <=> C7H7O2'}]
""",
)

entry(
    index = 187,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.24e+10,'m^3/(mol*s)'), n=-1.5, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_Ext-1C-R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C4H9 + C4H9 <=> C8H18'}]
""",
)

entry(
    index = 188,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R",
    kinetics = ArrheniusBM(A=(7.23001e+07,'m^3/(mol*s)'), n=-9.93442e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.23272519859e-11, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R
        Total Standard Deviation in ln(k): 8.12242512209e-11"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R
Total Standard Deviation in ln(k): 8.12242512209e-11""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R
Total Standard Deviation in ln(k): 8.12242512209e-11
sensitivities = [{'dA': 0.9407206952084449, 'dE0': 0.0, 'dn': -9.192918904198994, 'dA_dEa': 1.42485063747715e-05, 'dE0_dEa': 0.0, 'dn_dEa': -3.4642761523958185, 'name': 'CH3 + C2H3 <=> C3H6'}, {'dA': 0.05880864035390879, 'dE0': 0.0, 'dn': -9.192747552746283, 'dA_dEa': 1.42485063747715e-05, 'dE0_dEa': 0.0, 'dn_dEa': -3.4642761523958185, 'name': 'C2H3 + C2H3 <=> C4H6-4'}]
""",
)

entry(
    index = 189,
    label = "Root_N-1R->H_1CNOS->N_Ext-2R-R",
    kinetics = ArrheniusBM(A=(406124,'m^3/(mol*s)'), n=0.906369, w0=(77250,'J/mol'), E0=(43534.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.153305029067, var=35.949358839, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_1CNOS->N_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R
        Total Standard Deviation in ln(k): 12.4051358263"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R
Total Standard Deviation in ln(k): 12.4051358263""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R
Total Standard Deviation in ln(k): 12.4051358263
sensitivities = [{'dA': 0.19081890356178347, 'dE0': -0.010352809278700708, 'dn': 0.005236446146045707, 'dA_dEa': 0.15361948580762702, 'dE0_dEa': -0.00848988684436751, 'dn_dEa': 0.004300408490541322, 'name': 'NO2 + NO2 <=> N2O4'}, {'dA': 0.19136897338258738, 'dE0': -0.010383395932993882, 'dn': 0.005251841307603655, 'dA_dEa': 0.04780644646729642, 'dE0_dEa': -0.00521296469362756, 'dn_dEa': 0.0014413652944083313, 'name': 'NO + O2 <=> NO3'}, {'dA': 0.19160935305253424, 'dE0': -0.010396825691013313, 'dn': 0.005258567847557213, 'dA_dEa': 0.15361948580762702, 'dE0_dEa': -0.00848988684436751, 'dn_dEa': 0.004300408490541322, 'name': 'NO2 + NO3-2 <=> N2O5'}, {'dA': 1.7411459190201626, 'dE0': -0.07868805845691683, 'dn': 0.03958040025308509, 'dA_dEa': -4.559177311080522, 'dE0_dEa': 0.08419540213618285, 'dn_dEa': -0.12095754507883393, 'name': 'C[O] + [N]=O <=> CH3ONO'}, {'dA': 0.5311698082053925, 'dE0': -0.011326016233125381, 'dn': 0.005717312476183956, 'dA_dEa': 43.55814355849699, 'dE0_dEa': 0.045628120217885565, 'dn_dEa': 1.1224457995034767, 'name': 'CN + NCN <=> NCNCN'}, {'dA': 0.17091006892402055, 'dE0': -0.009243918846934943, 'dn': 0.004679276846340514, 'dA_dEa': 0.15361948580762702, 'dE0_dEa': -0.00848988684436751, 'dn_dEa': 0.004300408490541322, 'name': 'NH2 + HO2 <=> NH2OOH'}, {'dA': 0.19442907098012804, 'dE0': -0.010553607232669836, 'dn': 0.005337485280482186, 'dA_dEa': 0.09726593573590142, 'dE0_dEa': -0.006683703710240541, 'dn_dEa': 0.002775397014546486, 'name': 'NH2 + O2 <=> NH2OO'}, {'dA': -0.9957898300642074, 'dE0': 0.07374777523378209, 'dn': -0.03701573584604669, 'dA_dEa': 0.13673405400994995, 'dE0_dEa': -0.010401398248103294, 'dn_dEa': 0.003939163228748416, 'name': 'NH2 + CH3NH <=> CH3NHNH2'}]
""",
)

entry(
    index = 190,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.42839e+09,'m^3/(mol*s)'), n=-0.858081, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.283695694404, var=1.87999745198, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R
        Total Standard Deviation in ln(k): 3.46155564072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R
Total Standard Deviation in ln(k): 3.46155564072""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R
Total Standard Deviation in ln(k): 3.46155564072
sensitivities = [{'dA': 0.6350049798023594, 'dE0': 0.0, 'dn': -1.5104515059571385e-06, 'dA_dEa': -2.969323483132385, 'dE0_dEa': 0.0, 'dn_dEa': -0.40841212916881736, 'name': 'C3H3-2 + C7H7 <=> C10H10-2'}, {'dA': 0.020240345449453755, 'dE0': 0.0, 'dn': -1.3619849336930624e-06, 'dA_dEa': 0.08149055708984508, 'dE0_dEa': 0.0, 'dn_dEa': 0.011208381208312163, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}, {'dA': 0.020240136212381642, 'dE0': 0.0, 'dn': -1.3940973865030033e-06, 'dA_dEa': 0.05314972488080247, 'dE0_dEa': 0.0, 'dn_dEa': 0.007310291127233885, 'name': 'C3H3 + C3H3-2 <=> C6H6-2'}, {'dA': 0.32399692613086745, 'dE0': 0.0, 'dn': 1.5150684173496334e-06, 'dA_dEa': 1.3057399593671466, 'dE0_dEa': 0.0, 'dn_dEa': 0.1795957740996282, 'name': 'C3H3-2 + C3H3-2 <=> C6H6'}]
""",
)

entry(
    index = 191,
    label = "Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_N-Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(9.99999e+06,'m^3/(mol*s)'), n=9.65418e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_N-Sp-4R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_N-Sp-4R!H-2R
        Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CNOS->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 11.5401827615
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'C6H5 + C3H3-2 <=> C9H8-2'}]
""",
)

