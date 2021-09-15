#!/usr/bin/env python
# encoding: utf-8

name = "CO_Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.29348e+08,'m^3/(mol*s)'), n=-0.306961, w0=(554731,'J/mol'), E0=(51511.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0007517332959458627, var=1.4486037996689085, Tref=1000.0, N=13, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 13 training reactions at node Root
    Total Standard Deviation in ln(k): 2.414746974819662"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root
Total Standard Deviation in ln(k): 2.414746974819662""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root
Total Standard Deviation in ln(k): 2.414746974819662
sensitivities = [{'dA': 0.3649324785400101, 'dE0': 0.03444737307387168, 'dn': 0.10641901219681504, 'dA_dEa': -0.004730503693651211, 'dE0_dEa': -3.997289559370472e-05, 'dn_dEa': -0.0022006050597635604, 'name': 'HCO + H <=> CO + H2'}, {'dA': -0.0023736399583642992, 'dE0': 0.0001815043338910015, 'dn': -0.0015099202047003206, 'dA_dEa': -0.004730503693651211, 'dE0_dEa': -3.997289559370472e-05, 'dn_dEa': -0.0022006050597635604, 'name': 'HCO + O <=> CO + OH'}, {'dA': -0.7812104195360242, 'dE0': -0.11971315889020336, 'dn': -0.37385116806819063, 'dA_dEa': -0.0014662153056123567, 'dE0_dEa': 0.11905133148035493, 'dn_dEa': 0.000166606235310802, 'name': 'HCO + O2 <=> CO + HO2'}, {'dA': 0.36521682158867225, 'dE0': 0.03445028461822281, 'dn': 0.10655105239337775, 'dA_dEa': -0.004730503693651211, 'dE0_dEa': -3.997289559370472e-05, 'dn_dEa': -0.0022006050597635604, 'name': 'HCO + CH3 <=> CO + CH4'}, {'dA': 0.3640419775017679, 'dE0': 0.034440350946362386, 'dn': 0.10600459034357868, 'dA_dEa': -0.004730503693651211, 'dE0_dEa': -3.997289559370472e-05, 'dn_dEa': -0.0022006050597635604, 'name': 'HCO + CH3O <=> CO + CH3OH'}, {'dA': 0.3663188647778219, 'dE0': 0.03445439619237946, 'dn': 0.10706565166344174, 'dA_dEa': -0.004730503693651211, 'dE0_dEa': -3.997289559370472e-05, 'dn_dEa': -0.0022006050597635604, 'name': 'HCO + HCO_Y <=> CO + CH2O'}, {'dA': -0.0023740352439463436, 'dE0': 0.00018150228169360895, 'dn': -0.0015101046145031749, 'dA_dEa': -0.004730503693651211, 'dE0_dEa': -3.997289559370472e-05, 'dn_dEa': -0.0022006050597635604, 'name': 'HCO + C2H3 <=> CO + C2H4'}, {'dA': -0.0023737466712250694, 'dE0': 0.00018150374149538827, 'dn': -0.0015099699141168928, 'dA_dEa': -0.004730503693651211, 'dE0_dEa': -3.997289559370472e-05, 'dn_dEa': -0.0022006050597635604, 'name': 'HCO + nC3H7 <=> CO + C3H8_n'}, {'dA': -0.002374545097439102, 'dE0': 0.00018149955800152273, 'dn': -0.0015103423225139307, 'dA_dEa': -0.004730503693651211, 'dE0_dEa': -3.997289559370472e-05, 'dn_dEa': -0.0022006050597635604, 'name': 'HCO + iC3H7 <=> CO + C3H8_i'}, {'dA': -0.8020232040665038, 'dE0': -0.12255288186641873, 'dn': -0.3825576481272417, 'dA_dEa': -0.004730503693651211, 'dE0_dEa': -3.997289559370472e-05, 'dn_dEa': -0.0022006050597635604, 'name': 'HCO + NO <=> CO + HNO'}, {'dA': 0.36332900241479843, 'dE0': 0.03443832107751025, 'dn': 0.10567143932727874, 'dA_dEa': -1.5850440404109958, 'dE0_dEa': -0.04722519366875866, 'dn_dEa': -0.6630117074616825, 'name': 'HCO + NO2 <=> CO + HONO'}, {'dA': 0.3652452031808598, 'dE0': 0.034447553086570236, 'dn': 0.1065653686013669, 'dA_dEa': -0.004730503693651211, 'dE0_dEa': -3.997289559370472e-05, 'dn_dEa': -0.0022006050597635604, 'name': 'CH2OH + HCO <=> CH3OH + CO'}, {'dA': 0.36500872683479924, 'dE0': 0.0344472613036223, 'dn': 0.10645475259098475, 'dA_dEa': -0.004730503693651211, 'dE0_dEa': -3.997289559370472e-05, 'dn_dEa': -0.0022006050597635604, 'name': 'C2H5 + HCO <=> C2H6 + CO'}]
""",
)

entry(
    index = 2,
    label = "Root_4R->N",
    kinetics = ArrheniusBM(A=(7.1e+06,'m^3/(mol*s)'), n=0, w0=(535000,'J/mol'), E0=(32802.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->N',), comment="""BM rule fitted to 1 training reactions at node Root_4R->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->N
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'HCO + NO <=> CO + HNO'}]
""",
)

entry(
    index = 3,
    label = "Root_N-4R->N",
    kinetics = ArrheniusBM(A=(8.38033e+07,'m^3/(mol*s)'), n=-0.159505, w0=(556375,'J/mol'), E0=(44765.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09920204661675035, var=1.474353864336599, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->N',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->N
    Total Standard Deviation in ln(k): 2.6834603275433544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->N
Total Standard Deviation in ln(k): 2.6834603275433544""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->N
Total Standard Deviation in ln(k): 2.6834603275433544
sensitivities = [{'dA': 0.26892960415739375, 'dE0': 0.05228195820534123, 'dn': 0.11654101281173651, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + H <=> CO + H2'}, {'dA': 0.002373150675083741, 'dE0': 0.0003046693286354016, 'dn': 0.001341134096056932, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + O <=> CO + OH'}, {'dA': -0.8985385939298419, 'dE0': -0.3678257026342042, 'dn': -0.826480956119924, 'dA_dEa': 0.021993097295338805, 'dE0_dEa': 0.3658320503626006, 'dn_dEa': 0.020947206495398937, 'name': 'HCO + O2 <=> CO + HO2'}, {'dA': 0.27095457583928495, 'dE0': 0.05229554397502292, 'dn': 0.11836222257395299, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + CH3 <=> CO + CH4'}, {'dA': 0.2694375788934464, 'dE0': 0.05228572438583176, 'dn': 0.11699779600627952, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + CH3O <=> CO + CH3OH'}, {'dA': 0.26971449405979925, 'dE0': 0.05228686346829152, 'dn': 0.1172470473052741, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + HCO_Y <=> CO + CH2O'}, {'dA': 0.002375446186420311, 'dE0': 0.0003046863125937418, 'dn': 0.0013431983691320688, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + C2H3 <=> CO + C2H4'}, {'dA': 0.0023726879447852184, 'dE0': 0.00030466593376164946, 'dn': 0.0013407179072203912, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + nC3H7 <=> CO + C3H8_n'}, {'dA': 0.0023703262463928123, 'dE0': 0.000304648557118147, 'dn': 0.00133859387569404, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + iC3H7 <=> CO + C3H8_i'}, {'dA': 0.2701197445063328, 'dE0': 0.05228732507798911, 'dn': 0.11761208478967611, 'dA_dEa': -1.5858938049364084, 'dE0_dEa': -0.07183027213830975, 'dn_dEa': -1.2764738085648752, 'name': 'HCO + NO2 <=> CO + HONO'}, {'dA': 0.2685930136579214, 'dE0': 0.0522779602528359, 'dn': 0.11623866138182205, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH2OH + HCO <=> CH3OH + CO'}, {'dA': 0.2676251555691362, 'dE0': 0.052268813556651195, 'dn': 0.11536887440042368, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + HCO <=> C2H6 + CO'}]
""",
)

entry(
    index = 4,
    label = "Root_N-4R->N_4BrCClFHIOPSSi->H",
    kinetics = ArrheniusBM(A=(9.03e+07,'m^3/(mol*s)'), n=0, w0=(558000,'J/mol'), E0=(55800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_4BrCClFHIOPSSi->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_4BrCClFHIOPSSi->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_4BrCClFHIOPSSi->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_4BrCClFHIOPSSi->H
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'HCO + H <=> CO + H2'}]
""",
)

entry(
    index = 5,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H",
    kinetics = ArrheniusBM(A=(6.61788e+07,'m^3/(mol*s)'), n=-0.153133, w0=(556227,'J/mol'), E0=(41225.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13684351688887914, var=1.473861144377546, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H
    Total Standard Deviation in ln(k): 2.7776301032250847"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H
Total Standard Deviation in ln(k): 2.7776301032250847""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H
Total Standard Deviation in ln(k): 2.7776301032250847
sensitivities = [{'dA': -0.0025178727511845907, 'dE0': -0.0009607273015040747, 'dn': -0.0030081652895543446, 'dA_dEa': -0.004691297899484487, 'dE0_dEa': -0.0015089936472745856, 'dn_dEa': -0.004072825895923531, 'name': 'HCO + O <=> CO + OH'}, {'dA': -1.025688586065001, 'dE0': -0.5063764298858418, 'dn': -0.9848532373593223, 'dA_dEa': 0.01820956145337705, 'dE0_dEa': 0.5016979752289517, 'dn_dEa': 0.020884009590293566, 'name': 'HCO + O2 <=> CO + HO2'}, {'dA': 0.32910258304145473, 'dE0': 0.08221813721326345, 'dn': 0.15725699678828636, 'dA_dEa': -0.004691297899484487, 'dE0_dEa': -0.0015089936472745856, 'dn_dEa': -0.004072825895923531, 'name': 'HCO + CH3 <=> CO + CH4'}, {'dA': 0.32940217666070104, 'dE0': 0.08222392628368261, 'dn': 0.15753691790184876, 'dA_dEa': -0.004691297899484487, 'dE0_dEa': -0.0015089936472745856, 'dn_dEa': -0.004072825895923531, 'name': 'HCO + CH3O <=> CO + CH3OH'}, {'dA': 0.3279001557459444, 'dE0': 0.08220880954328477, 'dn': 0.15613045206717768, 'dA_dEa': -0.004691297899484487, 'dE0_dEa': -0.0015089936472745856, 'dn_dEa': -0.004072825895923531, 'name': 'HCO + HCO_Y <=> CO + CH2O'}, {'dA': -0.002516032889588182, 'dE0': -0.0009607077173332264, 'dn': -0.0030064424084843325, 'dA_dEa': -0.004691297899484487, 'dE0_dEa': -0.0015089936472745856, 'dn_dEa': -0.004072825895923531, 'name': 'HCO + C2H3 <=> CO + C2H4'}, {'dA': -0.0025184039316175633, 'dE0': -0.0009607330274084658, 'dn': -0.0030086625646311886, 'dA_dEa': -0.004691297899484487, 'dE0_dEa': -0.0015089936472745856, 'dn_dEa': -0.004072825895923531, 'name': 'HCO + nC3H7 <=> CO + C3H8_n'}, {'dA': -0.002513317188146679, 'dE0': -0.0009606789199681296, 'dn': -0.003003899176758758, 'dA_dEa': -0.004691297899484487, 'dE0_dEa': -0.0015089936472745856, 'dn_dEa': -0.004072825895923531, 'name': 'HCO + iC3H7 <=> CO + C3H8_i'}, {'dA': 0.3304697543172006, 'dE0': 0.08222992189276611, 'dn': 0.15853782627840207, 'dA_dEa': -1.8493486723658397, 'dE0_dEa': -0.11659258629351818, 'dn_dEa': -1.5507626809192818, 'name': 'HCO + NO2 <=> CO + HONO'}, {'dA': 0.32606423852502825, 'dE0': 0.08218668909135521, 'dn': 0.15441191836678564, 'dA_dEa': -0.004691297899484487, 'dE0_dEa': -0.0015089936472745856, 'dn_dEa': -0.004072825895923531, 'name': 'CH2OH + HCO <=> CH3OH + CO'}, {'dA': 0.3293635347070641, 'dE0': 0.08221328478470671, 'dn': 0.15750288519236536, 'dA_dEa': -0.004691297899484487, 'dE0_dEa': -0.0015089936472745856, 'dn_dEa': -0.004072825895923531, 'name': 'C2H5 + HCO <=> C2H6 + CO'}]
""",
)

entry(
    index = 6,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R",
    kinetics = ArrheniusBM(A=(6.22674e+07,'m^3/(mol*s)'), n=-0.159943, w0=(555500,'J/mol'), E0=(38705.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1646505543805851, var=1.7864081759488528, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R
    Total Standard Deviation in ln(k): 3.093155231420864"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R
Total Standard Deviation in ln(k): 3.093155231420864""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R
Total Standard Deviation in ln(k): 3.093155231420864
sensitivities = [{'dA': -1.1363353088783699, 'dE0': -0.6755339478695677, 'dn': -1.0543344267694137, 'dA_dEa': -0.019044711397244608, 'dE0_dEa': 0.6795331935880922, 'dn_dEa': -0.0064821068219484985, 'name': 'HCO + O2 <=> CO + HO2'}, {'dA': 0.42987145400635046, 'dE0': 0.13702241440495957, 'dn': 0.2134855953158586, 'dA_dEa': 0.0030703886579889258, 'dE0_dEa': 0.0023997099671386776, 'dn_dEa': 0.0023456359386274965, 'name': 'HCO + CH3O <=> CO + CH3OH'}, {'dA': 0.43030964316064535, 'dE0': 0.13701771698061654, 'dn': 0.2138802533760606, 'dA_dEa': 0.0030703886579889258, 'dE0_dEa': 0.0023997099671386776, 'dn_dEa': 0.0023456359386274965, 'name': 'HCO + HCO_Y <=> CO + CH2O'}, {'dA': 0.0059331993611528725, 'dE0': 0.003333113863574898, 'dn': 0.0038026070752543942, 'dA_dEa': 0.0030703886579889258, 'dE0_dEa': 0.0023997099671386776, 'dn_dEa': 0.0023456359386274965, 'name': 'HCO + C2H3 <=> CO + C2H4'}, {'dA': 0.005932122242314306, 'dE0': 0.003333096575764253, 'dn': 0.003801642161359126, 'dA_dEa': 0.0030703886579889258, 'dE0_dEa': 0.0023997099671386776, 'dn_dEa': 0.0023456359386274965, 'name': 'HCO + nC3H7 <=> CO + C3H8_n'}, {'dA': 0.0059424745764153795, 'dE0': 0.003333261615667138, 'dn': 0.0038109174550769002, 'dA_dEa': 0.0030703886579889258, 'dE0_dEa': 0.0023997099671386776, 'dn_dEa': 0.0023456359386274965, 'name': 'HCO + iC3H7 <=> CO + C3H8_i'}, {'dA': 0.4293963548214681, 'dE0': 0.13701826057195202, 'dn': 0.21305956982443508, 'dA_dEa': -2.2053617576889493, 'dE0_dEa': -0.1840164365013534, 'dn_dEa': -1.7720612209180713, 'name': 'HCO + NO2 <=> CO + HONO'}, {'dA': 0.42991276560404873, 'dE0': 0.13702728641412074, 'dn': 0.21352198790885812, 'dA_dEa': 0.0030703886579889258, 'dE0_dEa': 0.0023997099671386776, 'dn_dEa': 0.0023456359386274965, 'name': 'CH2OH + HCO <=> CH3OH + CO'}, {'dA': 0.4277452120576202, 'dE0': 0.13699086626780244, 'dn': 0.21157988017117813, 'dA_dEa': 0.0030703886579889258, 'dE0_dEa': 0.0023997099671386776, 'dn_dEa': 0.0023456359386274965, 'name': 'C2H5 + HCO <=> C2H6 + CO'}]
""",
)

entry(
    index = 7,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_4CO->O",
    kinetics = ArrheniusBM(A=(3.01e+07,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(57150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_4CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_4CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_4CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_4CO->O
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'HCO + O <=> CO + OH'}]
""",
)

entry(
    index = 8,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_N-4CO->O",
    kinetics = ArrheniusBM(A=(4e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(1004,'K'), Tmax=(1006,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_N-4CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_N-4CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_N-4CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_N-4CO->O
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'HCO + CH3 <=> CO + CH4'}]
""",
)

entry(
    index = 9,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C",
    kinetics = ArrheniusBM(A=(6.25086e+07,'m^3/(mol*s)'), n=-9.38684e-08, w0=(552300,'J/mol'), E0=(55230,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0030358659440372195, var=1.0537932494619011, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C
    Total Standard Deviation in ln(k): 2.0655772190197625"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C
Total Standard Deviation in ln(k): 2.0655772190197625""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C
Total Standard Deviation in ln(k): 2.0655772190197625
sensitivities = [{'dA': 0.5405038448494421, 'dE0': 0.0, 'dn': 69575.90145217611, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + CH3O <=> CO + CH3OH'}, {'dA': 0.0, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + C2H3 <=> CO + C2H4'}, {'dA': 0.0, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + nC3H7 <=> CO + C3H8_n'}, {'dA': 0.0, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + iC3H7 <=> CO + C3H8_i'}, {'dA': 0.5335975431962102, 'dE0': 0.0, 'dn': 59034.491993635944, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + HCO <=> C2H6 + CO'}]
""",
)

entry(
    index = 10,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.90776e+07,'m^3/(mol*s)'), n=-0.209862, w0=(559500,'J/mol'), E0=(34468.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.29096274974430797, var=1.586398221480992, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C
    Total Standard Deviation in ln(k): 3.2560721511919475"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.2560721511919475""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.2560721511919475
sensitivities = [{'dA': 0.2505535647614741, 'dE0': 0.0, 'dn': 0.00043954881880051816, 'dA_dEa': -1.9955420255188794, 'dE0_dEa': 0.0, 'dn_dEa': -1.2201543589735357, 'name': 'HCO + O2 <=> CO + HO2'}, {'dA': 0.24883901572539355, 'dE0': 0.0, 'dn': -0.0007347639267145069, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + HCO_Y <=> CO + CH2O'}, {'dA': 0.25003841929918647, 'dE0': 0.0, 'dn': 8.679198065555192e-05, 'dA_dEa': -2.7797511172916463, 'dE0_dEa': 0.0, 'dn_dEa': -1.6995665716311577, 'name': 'HCO + NO2 <=> CO + HONO'}, {'dA': 0.24867888816973402, 'dE0': 0.0, 'dn': -0.0008444164921664398, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH2OH + HCO <=> CH3OH + CO'}]
""",
)

entry(
    index = 11,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Ext-4CO-R",
    kinetics = ArrheniusBM(A=(1.2e+08,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Ext-4CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Ext-4CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Ext-4CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Ext-4CO-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'HCO + iC3H7 <=> CO + C3H8_i'}]
""",
)

entry(
    index = 12,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO",
    kinetics = ArrheniusBM(A=(6.23054e+07,'m^3/(mol*s)'), n=-9.73051e-08, w0=(555500,'J/mol'), E0=(55550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0001191721661824122, var=1.0835923253238533, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO
    Total Standard Deviation in ln(k): 2.0871432574958804"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO
Total Standard Deviation in ln(k): 2.0871432574958804""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO
Total Standard Deviation in ln(k): 2.0871432574958804
sensitivities = [{'dA': 0.5171008255971402, 'dE0': 0.0, 'dn': 27842.145814568852, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + CH3O <=> CO + CH3OH'}, {'dA': 0.0, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + nC3H7 <=> CO + C3H8_n'}, {'dA': 0.47671970927614915, 'dE0': 0.0, 'dn': -31744.6687621099, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + HCO <=> C2H6 + CO'}]
""",
)

entry(
    index = 13,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_N-Sp-5C-4CO",
    kinetics = ArrheniusBM(A=(9.033e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_N-Sp-5C-4CO',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_N-Sp-5C-4CO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_N-Sp-5C-4CO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_N-Sp-5C-4CO
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'HCO + C2H3 <=> CO + C2H4'}]
""",
)

entry(
    index = 14,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.46682e+06,'m^3/(mol*s)'), n=0.34128, w0=(555500,'J/mol'), E0=(24469.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3426295535272028, var=1.1310263282658846, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 2.9929084486563107"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 2.9929084486563107""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 2.9929084486563107
sensitivities = [{'dA': 0.33313452677145367, 'dE0': 0.0, 'dn': 1.5602037160055612e-05, 'dA_dEa': -2.659804437812179, 'dE0_dEa': 0.0, 'dn_dEa': 1.0000033444449912, 'name': 'HCO + O2 <=> CO + HO2'}, {'dA': 0.33296355302074093, 'dE0': 0.0, 'dn': 8.765608070280513e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'HCO + HCO_Y <=> CO + CH2O'}, {'dA': 0.33306378482048987, 'dE0': 0.0, 'dn': 4.548865755681553e-05, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CH2OH + HCO <=> CH3OH + CO'}]
""",
)

entry(
    index = 15,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.24e+17,'m^3/(mol*s)'), n=-3.29, w0=(571500,'J/mol'), E0=(57150,'J/mol'), Tmin=(1140,'K'), Tmax=(1650,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330872656, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + NO2 <=> CO + HONO'}]
""",
)

entry(
    index = 16,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->O",
    kinetics = ArrheniusBM(A=(9.03e+07,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(57150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->O
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'HCO + CH3O <=> CO + CH3OH'}]
""",
)

entry(
    index = 17,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->O",
    kinetics = ArrheniusBM(A=(4.30916e+07,'m^3/(mol*s)'), n=-1.45648e-06, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.32890731525313555, var=0.22197044450561015, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->O
    Total Standard Deviation in ln(k): 1.7709059506268878"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->O
Total Standard Deviation in ln(k): 1.7709059506268878""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->O
Total Standard Deviation in ln(k): 1.7709059506268878
sensitivities = [{'dA': -0.002248610162070256, 'dE0': 0.0, 'dn': -871.8587429887991, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + nC3H7 <=> CO + C3H8_n'}, {'dA': 0.9759083285701928, 'dE0': 0.0, 'dn': -1727.941818810275, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + HCO <=> C2H6 + CO'}]
""",
)

entry(
    index = 18,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->O",
    kinetics = ArrheniusBM(A=(5.12e+07,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(53142.9,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->O
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.22726644515778532, 'dn_dEa': nan, 'name': 'HCO + O2 <=> CO + HO2'}]
""",
)

entry(
    index = 19,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->O",
    kinetics = ArrheniusBM(A=(1.34165e+07,'m^3/(mol*s)'), n=-4.9914e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.5990137911088773e-17, var=0.6909863268735121, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->O
    Total Standard Deviation in ln(k): 1.666447807467594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->O
Total Standard Deviation in ln(k): 1.666447807467594""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->O
Total Standard Deviation in ln(k): 1.666447807467594
sensitivities = [{'dA': 0.5217510549862545, 'dE0': 0.0, 'dn': 6322.217092262254, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + HCO_Y <=> CO + CH2O'}, {'dA': 0.4875906811996881, 'dE0': 0.0, 'dn': -3511.737185222198, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH2OH + HCO <=> CH3OH + CO'}]
""",
)

entry(
    index = 20,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->O_Ext-5C-R",
    kinetics = ArrheniusBM(A=(6e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->O_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->O_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->O_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->O_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'HCO + nC3H7 <=> CO + C3H8_n'}]
""",
)

entry(
    index = 21,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->O_Sp-5O-4C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->O_Sp-5O-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->O_Sp-5O-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->O_Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->O_Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'CH2OH + HCO <=> CH3OH + CO'}]
""",
)

entry(
    index = 22,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->O_N-Sp-5O-4C",
    kinetics = ArrheniusBM(A=(1.8e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->O_N-Sp-5O-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->O_N-Sp-5O-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->O_N-Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->O_N-Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'HCO + HCO_Y <=> CO + CH2O'}]
""",
)

