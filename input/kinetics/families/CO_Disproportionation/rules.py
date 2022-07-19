#!/usr/bin/env python
# encoding: utf-8

name = "CO_Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.50424e+08,'m^3/(mol*s)'), n=-0.319767, w0=(554731,'J/mol'), E0=(51556.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0016473366032466322, var=1.5093311729901167, Tref=1000.0, N=13, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 13 training reactions at node Root
            Total Standard Deviation in ln(k): 2.467053109955428"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root
Total Standard Deviation in ln(k): 2.467053109955428""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root
Total Standard Deviation in ln(k): 2.467053109955428
sensitivities = [{'dA': -6.314791335317678, 'dE0': -362.0830288621028, 'dn': -4.18646431533786, 'dA_dEa': -6.425177754000797, 'dE0_dEa': -363.9212992963399, 'dn_dEa': -4.18612775158263, 'name': 'HCO + H <=> CO + H2'}, {'dA': -6.4248515080656405, 'dE0': -363.9094139814591, 'dn': -4.186490991468629, 'dA_dEa': -6.425177754000797, 'dE0_dEa': -363.9212992963399, 'dn_dEa': -4.18612775158263, 'name': 'HCO + O <=> CO + OH'}, {'dA': -6.314957390473082, 'dE0': -366.9167097345412, 'dn': -4.186622203619247, 'dA_dEa': -7.157885175499324, 'dE0_dEa': -376.1060460752813, 'dn_dEa': -4.806249548607183, 'name': 'HCO + O2 <=> CO + HO2'}, {'dA': -6.314538909134611, 'dE0': -362.08055756055563, 'dn': -4.186224466735652, 'dA_dEa': -6.425177754000797, 'dE0_dEa': -363.9212992963399, 'dn_dEa': -4.18612775158263, 'name': 'HCO + CH3 <=> CO + CH4'}, {'dA': -6.31563573747654, 'dE0': -362.08302296363166, 'dn': -4.187265902578558, 'dA_dEa': -6.425177754000797, 'dE0_dEa': -363.9212992963399, 'dn_dEa': -4.18612775158263, 'name': 'HCO + CH3O <=> CO + CH3OH'}, {'dA': -6.314541256739388, 'dE0': -362.07996565488276, 'dn': -4.186226714796463, 'dA_dEa': -6.425177754000797, 'dE0_dEa': -363.9212992963399, 'dn_dEa': -4.18612775158263, 'name': 'HCO + HCO_Y <=> CO + CH2O'}, {'dA': -6.4245994308159, 'dE0': -363.9094408972491, 'dn': -4.1862516510535395, 'dA_dEa': -6.425177754000797, 'dE0_dEa': -363.9212992963399, 'dn_dEa': -4.18612775158263, 'name': 'HCO + C2H3 <=> CO + C2H4'}, {'dA': -6.425031071245965, 'dE0': -363.9095746657383, 'dn': -4.186661406260586, 'dA_dEa': -6.425177754000797, 'dE0_dEa': -363.9212992963399, 'dn_dEa': -4.18612775158263, 'name': 'HCO + nC3H7 <=> CO + C3H8_n'}, {'dA': -6.425123933319552, 'dE0': -363.9094067890373, 'dn': -4.186749640593416, 'dA_dEa': -6.425177754000797, 'dE0_dEa': -363.9212992963399, 'dn_dEa': -4.18612775158263, 'name': 'HCO + iC3H7 <=> CO + C3H8_i'}, {'dA': -6.3147216336758865, 'dE0': -362.07806521801166, 'dn': -4.186397970703679, 'dA_dEa': -6.425177754000797, 'dE0_dEa': -363.9212992963399, 'dn_dEa': -4.18612775158263, 'name': 'HCO + NO <=> CO + HNO'}, {'dA': -6.314604782546225, 'dE0': -362.0652780073878, 'dn': -4.186287138847273, 'dA_dEa': -7.446104462318568, 'dE0_dEa': -386.33465398734995, 'dn_dEa': -5.0501730512105265, 'name': 'HCO + NO2 <=> CO + HONO'}, {'dA': -6.3143549453037755, 'dE0': -362.0800705098891, 'dn': -4.186049714650297, 'dA_dEa': -6.425177754000797, 'dE0_dEa': -363.9212992963399, 'dn_dEa': -4.18612775158263, 'name': 'CH2OH + HCO <=> CH3OH + CO'}, {'dA': -6.314644691848755, 'dE0': -362.07952576477317, 'dn': -4.186325228171608, 'dA_dEa': -6.425177754000797, 'dE0_dEa': -363.9212992963399, 'dn_dEa': -4.18612775158263, 'name': 'C2H5 + HCO <=> C2H6 + CO'}]
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
    kinetics = ArrheniusBM(A=(1.07003e+08,'m^3/(mol*s)'), n=-0.197496, w0=(556375,'J/mol'), E0=(42832.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11670695366806721, var=1.483284502084561, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->N',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->N
            Total Standard Deviation in ln(k): 2.73480377059182"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->N
Total Standard Deviation in ln(k): 2.73480377059182""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->N
Total Standard Deviation in ln(k): 2.73480377059182
sensitivities = [{'dA': 0.2482059536959287, 'dE0': 0.07789639354086875, 'dn': 0.08230643190288832, 'dA_dEa': -0.0033334028728408192, 'dE0_dEa': -0.0009426288960761433, 'dn_dEa': -0.002394297666244596, 'name': 'HCO + H <=> CO + H2'}, {'dA': -0.0017571694250763928, 'dE0': -0.00046428531607520864, 'dn': -0.001873812819814811, 'dA_dEa': -0.0033334028728408192, 'dE0_dEa': -0.0009426288960761433, 'dn_dEa': -0.002394297666244596, 'name': 'HCO + O <=> CO + OH'}, {'dA': -0.7831827937288846, 'dE0': -0.5561027802530802, 'dn': -0.6066016442798718, 'dA_dEa': -0.04193073886327632, 'dE0_dEa': 0.4804518950195167, 'dn_dEa': -0.036654115197729466, 'name': 'HCO + O2 <=> CO + HO2'}, {'dA': 0.25036609373788027, 'dE0': 0.07792386249538719, 'dn': 0.0839463290966031, 'dA_dEa': -0.0033334028728408192, 'dE0_dEa': -0.0009426288960761433, 'dn_dEa': -0.002394297666244596, 'name': 'HCO + CH3 <=> CO + CH4'}, {'dA': 0.2491653887020381, 'dE0': 0.07790640617526973, 'dn': 0.08303515090454694, 'dA_dEa': -0.0033334028728408192, 'dE0_dEa': -0.0009426288960761433, 'dn_dEa': -0.002394297666244596, 'name': 'HCO + CH3O <=> CO + CH3OH'}, {'dA': 0.2509710915106488, 'dE0': 0.0779197523091423, 'dn': 0.0844076312716408, 'dA_dEa': -0.0033334028728408192, 'dE0_dEa': -0.0009426288960761433, 'dn_dEa': -0.002394297666244596, 'name': 'HCO + HCO_Y <=> CO + CH2O'}, {'dA': -0.001757329862073414, 'dE0': -0.0004642874017920736, 'dn': -0.0018739346079936958, 'dA_dEa': -0.0033334028728408192, 'dE0_dEa': -0.0009426288960761433, 'dn_dEa': -0.002394297666244596, 'name': 'HCO + C2H3 <=> CO + C2H4'}, {'dA': -0.001756520187967874, 'dE0': -0.00046427687335873165, 'dn': -0.0018733199812028718, 'dA_dEa': -0.0033334028728408192, 'dE0_dEa': -0.0009426288960761433, 'dn_dEa': -0.002394297666244596, 'name': 'HCO + nC3H7 <=> CO + C3H8_n'}, {'dA': -0.001758113029382196, 'dE0': -0.0004642975862283929, 'dn': -0.0018745291117344607, 'dA_dEa': -0.0033334028728408192, 'dE0_dEa': -0.0009426288960761433, 'dn_dEa': -0.002394297666244596, 'name': 'HCO + iC3H7 <=> CO + C3H8_i'}, {'dA': 0.2511535330214364, 'dE0': 0.07792520427579307, 'dn': 0.08454566659461739, 'dA_dEa': -1.302384003082723, 'dE0_dEa': -0.09444926840316334, 'dn_dEa': -0.8818979504130405, 'name': 'HCO + NO2 <=> CO + HONO'}, {'dA': 0.2510416259440539, 'dE0': 0.07793715893157684, 'dn': 0.08445864329991991, 'dA_dEa': -0.0033334028728408192, 'dE0_dEa': -0.0009426288960761433, 'dn_dEa': -0.002394297666244596, 'name': 'CH2OH + HCO <=> CH3OH + CO'}, {'dA': 0.2515323813590264, 'dE0': 0.07793453755790948, 'dn': 0.08483258058815674, 'dA_dEa': -0.0033334028728408192, 'dE0_dEa': -0.0009426288960761433, 'dn_dEa': -0.002394297666244596, 'name': 'C2H5 + HCO <=> C2H6 + CO'}]
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
    kinetics = ArrheniusBM(A=(8.91879e+07,'m^3/(mol*s)'), n=-0.199685, w0=(556227,'J/mol'), E0=(38053.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1542009982792688, var=1.4652541492986535, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H
            Total Standard Deviation in ln(k): 2.8141250501210964"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H
Total Standard Deviation in ln(k): 2.8141250501210964""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H
Total Standard Deviation in ln(k): 2.8141250501210964
sensitivities = [{'dA': 0.0007715460412783554, 'dE0': 0.0, 'dn': -0.00010216874660908829, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + O <=> CO + OH'}, {'dA': 0.14244262812825217, 'dE0': 0.0, 'dn': 0.0001325291425841336, 'dA_dEa': -0.9403934549184682, 'dE0_dEa': 0.0, 'dn_dEa': -0.6220633262661814, 'name': 'HCO + O2 <=> CO + HO2'}, {'dA': 0.14287123169155944, 'dE0': 0.0, 'dn': 0.0004506471040503626, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + CH3 <=> CO + CH4'}, {'dA': 0.1426476125914335, 'dE0': 0.0, 'dn': 0.00028459886071558464, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + CH3O <=> CO + CH3OH'}, {'dA': 0.14293494940177862, 'dE0': 0.0, 'dn': 0.0004979805791704941, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + HCO_Y <=> CO + CH2O'}, {'dA': 0.0007710856024801554, 'dE0': 0.0, 'dn': -0.00010251054498144835, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + C2H3 <=> CO + C2H4'}, {'dA': 0.0007718876879892773, 'dE0': 0.0, 'dn': -0.00010191525185769285, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + nC3H7 <=> CO + C3H8_n'}, {'dA': 0.0007709936831191438, 'dE0': 0.0, 'dn': -0.00010257855957257173, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + iC3H7 <=> CO + C3H8_i'}, {'dA': 0.14301046438804274, 'dE0': 0.0, 'dn': 0.0005540731815984451, 'dA_dEa': -1.3101614223957392, 'dE0_dEa': 0.0, 'dn_dEa': -0.8666408264002022, 'name': 'HCO + NO2 <=> CO + HONO'}, {'dA': 0.14272607004885324, 'dE0': 0.0, 'dn': 0.00034298155213851814, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH2OH + HCO <=> CH3OH + CO'}, {'dA': 0.1430406058169511, 'dE0': 0.0, 'dn': 0.0005764305789972362, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + HCO <=> C2H6 + CO'}]
""",
)

entry(
    index = 6,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R",
    kinetics = ArrheniusBM(A=(8.66768e+07,'m^3/(mol*s)'), n=-0.211541, w0=(555500,'J/mol'), E0=(35759.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18304785255687206, var=1.7684092321847347, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R
            Total Standard Deviation in ln(k): 3.125846982830696"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R
Total Standard Deviation in ln(k): 3.125846982830696""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R
Total Standard Deviation in ln(k): 3.125846982830696
sensitivities = [{'dA': 0.1657628197051691, 'dE0': 0.0, 'dn': -0.00018461371443676078, 'dA_dEa': -1.0983865545172267, 'dE0_dEa': 0.0, 'dn_dEa': -0.6225484488062196, 'name': 'HCO + O2 <=> CO + HO2'}, {'dA': 0.1657583338854534, 'dE0': 0.0, 'dn': -0.0001874445270028535, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + CH3O <=> CO + CH3OH'}, {'dA': 0.16526357747894282, 'dE0': 0.0, 'dn': -0.0005020571492734553, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + HCO_Y <=> CO + CH2O'}, {'dA': 0.0007714300593875973, 'dE0': 0.0, 'dn': -0.00018594199242206815, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + C2H3 <=> CO + C2H4'}, {'dA': 0.0007669275419176237, 'dE0': 0.0, 'dn': -0.00018880557044327642, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + nC3H7 <=> CO + C3H8_n'}, {'dA': 0.0007671409569810229, 'dE0': 0.0, 'dn': -0.0001886697985135784, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + iC3H7 <=> CO + C3H8_i'}, {'dA': 0.16550740385314502, 'dE0': 0.0, 'dn': -0.00034702642172030365, 'dA_dEa': -1.5300538927613425, 'dE0_dEa': 0.0, 'dn_dEa': -0.8671732881901695, 'name': 'HCO + NO2 <=> CO + HONO'}, {'dA': 0.1657236557868385, 'dE0': 0.0, 'dn': -0.0002095231876242937, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH2OH + HCO <=> CH3OH + CO'}, {'dA': 0.16564031489709355, 'dE0': 0.0, 'dn': -0.0002625115486408121, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + HCO <=> C2H6 + CO'}]
""",
)

entry(
    index = 7,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_4CO->C",
    kinetics = ArrheniusBM(A=(4e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(1004,'K'), Tmax=(1006,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_4CO->C
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'HCO + CH3 <=> CO + CH4'}]
""",
)

entry(
    index = 8,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_N-4CO->C",
    kinetics = ArrheniusBM(A=(3.01e+07,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(57150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_N-4CO->C
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'HCO + O <=> CO + OH'}]
""",
)

entry(
    index = 9,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C",
    kinetics = ArrheniusBM(A=(6.25087e+07,'m^3/(mol*s)'), n=-3.44506e-07, w0=(552300,'J/mol'), E0=(55230,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.003035855795017244, var=1.0537930185332733, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C
            Total Standard Deviation in ln(k): 2.0655769680298164"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C
Total Standard Deviation in ln(k): 2.0655769680298164""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C
Total Standard Deviation in ln(k): 2.0655769680298164
sensitivities = [{'dA': 0.4928662303101393, 'dE0': 0.0, 'dn': -930.339840019963, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + CH3O <=> CO + CH3OH'}, {'dA': 0.0, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + C2H3 <=> CO + C2H4'}, {'dA': 0.0, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + nC3H7 <=> CO + C3H8_n'}, {'dA': 0.0, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + iC3H7 <=> CO + C3H8_i'}, {'dA': 0.49105427408596547, 'dE0': 0.0, 'dn': -1667.5844151966887, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + HCO <=> C2H6 + CO'}]
""",
)

entry(
    index = 10,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.11393e+08,'m^3/(mol*s)'), n=-0.330374, w0=(559500,'J/mol'), E0=(31017.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.30376782766715116, var=1.5882125761374941, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C
            Total Standard Deviation in ln(k): 3.2896892209923085"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.2896892209923085""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.2896892209923085
sensitivities = [{'dA': 0.24996195380214115, 'dE0': 0.0, 'dn': 3.771861247555392e-05, 'dA_dEa': -1.6520196368540894, 'dE0_dEa': 0.0, 'dn_dEa': -0.62219512812916, 'name': 'HCO + O2 <=> CO + HO2'}, {'dA': 0.2504156374918685, 'dE0': 0.0, 'dn': 0.00022950329897356592, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + HCO_Y <=> CO + CH2O'}, {'dA': 0.24961211020982338, 'dE0': 0.0, 'dn': -0.00011007133963439878, 'dA_dEa': -2.302866249511735, 'dE0_dEa': 0.0, 'dn_dEa': -0.867358353220918, 'name': 'HCO + NO2 <=> CO + HONO'}, {'dA': 0.2504139368646739, 'dE0': 0.0, 'dn': 0.00022878330434823813, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH2OH + HCO <=> CH3OH + CO'}]
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
    kinetics = ArrheniusBM(A=(6.23055e+07,'m^3/(mol*s)'), n=-3.48768e-07, w0=(555500,'J/mol'), E0=(55550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00011918107695963465, var=1.083592082729155, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO
            Total Standard Deviation in ln(k): 2.0871430462834097"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO
Total Standard Deviation in ln(k): 2.0871430462834097""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO
Total Standard Deviation in ln(k): 2.0871430462834097
sensitivities = [{'dA': 0.5234107791594632, 'dE0': 0.0, 'dn': 10037.537357693334, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + CH3O <=> CO + CH3OH'}, {'dA': -0.00025556207106095, 'dE0': 0.0, 'dn': -2601.534788925531, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + nC3H7 <=> CO + C3H8_n'}, {'dA': 0.49411964198148195, 'dE0': 0.0, 'dn': -1695.3860517905875, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + HCO <=> C2H6 + CO'}]
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
    kinetics = ArrheniusBM(A=(2.31568e+06,'m^3/(mol*s)'), n=0.274147, w0=(555500,'J/mol'), E0=(18779.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.349762835877399, var=1.1191068111594877, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O
            Total Standard Deviation in ln(k): 2.999567127888949"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 2.999567127888949""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 2.999567127888949
sensitivities = [{'dA': 0.333032229081135, 'dE0': -0.0, 'dn': 6.8586340290923e-05, 'dA_dEa': -2.203341895706388, 'dE0_dEa': -0.0, 'dn_dEa': 1.0000741912925333, 'name': 'HCO + O2 <=> CO + HO2'}, {'dA': 0.3329586235363647, 'dE0': -0.0, 'dn': 0.00010607256242433787, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'HCO + HCO_Y <=> CO + CH2O'}, {'dA': 0.3331002053990429, 'dE0': -0.0, 'dn': 3.3927185756900525e-05, 'dA_dEa': 0.0, 'dE0_dEa': -0.0, 'dn_dEa': 0.0, 'name': 'CH2OH + HCO <=> CH3OH + CO'}]
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
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C",
    kinetics = ArrheniusBM(A=(4.30914e+07,'m^3/(mol*s)'), n=-7.5687e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.32890731525313555, var=0.22197044450561015, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C
            Total Standard Deviation in ln(k): 1.7709059506268878"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C
Total Standard Deviation in ln(k): 1.7709059506268878""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C
Total Standard Deviation in ln(k): 1.7709059506268878
sensitivities = [{'dA': 0.0035228016557202198, 'dE0': 0.0, 'dn': -573.034068374068, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + nC3H7 <=> CO + C3H8_n'}, {'dA': 0.9947686827268528, 'dE0': 0.0, 'dn': 244.09759249833343, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'C2H5 + HCO <=> C2H6 + CO'}]
""",
)

entry(
    index = 17,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->C",
    kinetics = ArrheniusBM(A=(9.03e+07,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(57150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->C
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'HCO + CH3O <=> CO + CH3OH'}]
""",
)

entry(
    index = 18,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C",
    kinetics = ArrheniusBM(A=(1.34165e+07,'m^3/(mol*s)'), n=-5.25438e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.5990137911088773e-17, var=0.6909863268735121, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C
            Total Standard Deviation in ln(k): 1.666447807467594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C
Total Standard Deviation in ln(k): 1.666447807467594""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C
Total Standard Deviation in ln(k): 1.666447807467594
sensitivities = [{'dA': 0.49315028606150435, 'dE0': 0.0, 'dn': -1802.3955839175349, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'HCO + HCO_Y <=> CO + CH2O'}, {'dA': 0.4873294686192335, 'dE0': 0.0, 'dn': -3341.366752592967, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'CH2OH + HCO <=> CH3OH + CO'}]
""",
)

entry(
    index = 19,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->C",
    kinetics = ArrheniusBM(A=(5.12e+07,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(53142.9,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->C
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.2201001108515773, 'dn_dEa': nan, 'name': 'HCO + O2 <=> CO + HO2'}]
""",
)

entry(
    index = 20,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(6e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C_Ext-5C-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'HCO + nC3H7 <=> CO + C3H8_n'}]
""",
)

entry(
    index = 21,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C_Sp-5O-4C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C_Sp-5O-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C_Sp-5O-4C
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C_Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C_Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'CH2OH + HCO <=> CH3OH + CO'}]
""",
)

entry(
    index = 22,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C_N-Sp-5O-4C",
    kinetics = ArrheniusBM(A=(1.8e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C_N-Sp-5O-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C_N-Sp-5O-4C
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C_N-Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C_N-Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'HCO + HCO_Y <=> CO + CH2O'}]
""",
)

