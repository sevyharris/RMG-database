#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(9.17508e-08,'m^3/(mol*s)'), n=3.07766, w0=(857395,'J/mol'), E0=(135956,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12455772480097667, var=4.503087907907877, Tref=1000.0, N=19, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 19 training reactions at node Root
            Total Standard Deviation in ln(k): 4.567103260504657"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root
Total Standard Deviation in ln(k): 4.567103260504657""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root
Total Standard Deviation in ln(k): 4.567103260504657
sensitivities = [{'dA': 3.6190203647276755, 'dE0': 0.0260327771958781, 'dn': -0.14065187849409247, 'dA_dEa': 2.5393602925628, 'dE0_dEa': 0.02146844209183907, 'dn_dEa': -0.09880033404703636, 'name': 'C4H6 + C2H4 <=> C6H10'}, {'dA': 3.7716285590367593, 'dE0': 0.026627324389597765, 'dn': -0.14386432174430708, 'dA_dEa': 3.5514143111864986, 'dE0_dEa': 0.08771769550061771, 'dn_dEa': -0.13784833163373683, 'name': 'C4H6-2 + C4H6 <=> C8H12'}, {'dA': 3.7716285590367593, 'dE0': 0.026627324389597765, 'dn': -0.14386432174430708, 'dA_dEa': 3.5514143111864986, 'dE0_dEa': 0.08771769550061771, 'dn_dEa': -0.13784833163373683, 'name': 'C4H6-3 + C4H6 <=> C8H12-2'}, {'dA': 3.4917811833640693, 'dE0': 0.024611729842943374, 'dn': -0.1329740295918448, 'dA_dEa': 7.763558609419763, 'dE0_dEa': 0.11200529800090658, 'dn_dEa': -0.3017980823210763, 'name': 'C5H8 + C4H6 <=> C9H14'}, {'dA': 3.4917811833640693, 'dE0': 0.024611729842943374, 'dn': -0.1329740295918448, 'dA_dEa': 7.763558609416211, 'dE0_dEa': 0.11200529800090658, 'dn_dEa': -0.3017980823209414, 'name': 'C5H8-2 + C4H6 <=> C9H14-2'}, {'dA': 3.625465135283123, 'dE0': 0.02607919482834444, 'dn': -0.1409026779435486, 'dA_dEa': 1.950918277387574, 'dE0_dEa': 0.01875732951310319, 'dn_dEa': -0.07589230724452826, 'name': 'C5H8-3 + C2H4 <=> C7H12'}, {'dA': 3.625465135283123, 'dE0': 0.02607919482834444, 'dn': -0.1409026779435486, 'dA_dEa': 1.950918277387574, 'dE0_dEa': 0.01875732951310319, 'dn_dEa': -0.07589230724452826, 'name': 'C2H4 + C5H8-4 <=> C7H12-2'}, {'dA': 3.864857640387668, 'dE0': 0.02729882119025962, 'dn': -0.14749233122559938, 'dA_dEa': 2.474240858571892, 'dE0_dEa': 0.06536853678694562, 'dn_dEa': -0.09601132837484216, 'name': 'C4H6-3 + C5H8-3 <=> C9H14-3'}, {'dA': 3.8648576403912207, 'dE0': 0.02729882119047658, 'dn': -0.14749233122573424, 'dA_dEa': 2.4856357480767493, 'dE0_dEa': 0.06544506828856034, 'dn_dEa': -0.09645839070822608, 'name': 'C4H6-2 + C5H8-4 <=> C9H14-4'}, {'dA': 4.1889905743279945, 'dE0': 0.02963322499375009, 'dn': -0.1601061033004873, 'dA_dEa': -5.5013590571177335, 'dE0_dEa': 0.02656305425513402, 'dn_dEa': 0.21446732545927494, 'name': 'C2H4 + C6H10-2 <=> C8H14'}, {'dA': 3.8985103703663557, 'dE0': 0.027541125818831586, 'dn': -0.14880197914301177, 'dA_dEa': -0.51954515408076, 'dE0_dEa': 0.06396930531392828, 'dn_dEa': 0.020608015014154678, 'name': 'C3H6 + C6H10-2 <=> C9H16'}, {'dA': 3.8985103703699084, 'dE0': 0.027541125818831586, 'dn': -0.1488019791431466, 'dA_dEa': -0.5220796129031278, 'dE0_dEa': 0.06395282708449813, 'dn_dEa': 0.02070784592098663, 'name': 'C3H6-2 + C6H10-2 <=> C9H16-2'}, {'dA': 3.091013248642923, 'dE0': 0.021725259269382836, 'dn': -0.11737806672901689, 'dA_dEa': 12.983242117191915, 'dE0_dEa': 0.14453859887626597, 'dn_dEa': -0.5049522660488911, 'name': 'C4H6-2 + C6H10-2 <=> C10H16'}, {'dA': 3.091013248642923, 'dE0': 0.021725259269382836, 'dn': -0.11737806672901689, 'dA_dEa': 12.978294728499415, 'dE0_dEa': 0.14450572440689965, 'dn_dEa': -0.5047579222867773, 'name': 'C4H6-3 + C6H10-2 <=> C10H16-2'}, {'dA': 2.831744369025869, 'dE0': 0.019857706084239, 'dn': -0.10728870457820816, 'dA_dEa': 14.442380335376184, 'dE0_dEa': 0.14645436857380087, 'dn_dEa': -0.56178375602663, 'name': 'C5H8 + C6H10-2 <=> C11H18'}, {'dA': 2.831744369025869, 'dE0': 0.019857706084239, 'dn': -0.10728870457820816, 'dA_dEa': 14.442380335372631, 'dE0_dEa': 0.14645436857380087, 'dn_dEa': -0.56178375602663, 'name': 'C5H8-2 + C6H10-2 <=> C11H18-2'}, {'dA': 3.3565952590461166, 'dE0': 0.024142685879145292, 'dn': -0.13043956326584524, 'dA_dEa': 6.077412713257461, 'dE0_dEa': 0.047705727031401815, 'dn_dEa': -0.23647990855784562, 'name': 'C7H10 + C4H8 <=> C11H18-3'}, {'dA': 3.8918737336044296, 'dE0': 0.027998207518838882, 'dn': -0.15126986486076063, 'dA_dEa': -2.354460947590102, 'dE0_dEa': -0.012491514963618208, 'dn_dEa': 0.09165096717054819, 'name': 'C3H4 + C4H6 <=> C7H10-2'}, {'dA': 3.8753556758028656, 'dE0': 0.027879181844479003, 'dn': -0.15062709520035106, 'dA_dEa': -2.372338242821831, 'dE0_dEa': -0.012477499095191604, 'dn_dEa': 0.09234731903145534, 'name': 'C3H4-2 + C4H6 <=> C7H10-3'}]
""",
)

entry(
    index = 2,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd",
    kinetics = ArrheniusBM(A=(0.000164218,'m^3/(mol*s)'), n=2.11749, w0=(858000,'J/mol'), E0=(142431,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0614368558151701, var=3.784088113710139, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd',), comment="""BM rule fitted to 17 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
            Total Standard Deviation in ln(k): 4.054121528473931"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
Total Standard Deviation in ln(k): 4.054121528473931""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
Total Standard Deviation in ln(k): 4.054121528473931
sensitivities = [{'dA': 0.2730363724623731, 'dE0': 0.0018185798935097628, 'dn': -0.015331638873158146, 'dA_dEa': -0.7565575770770162, 'dE0_dEa': -0.0021067846192579544, 'dn_dEa': 0.043256572932154354, 'name': 'C4H6 + C2H4 <=> C6H10'}, {'dA': 0.4650710943306337, 'dE0': 0.002640405194971557, 'dn': -0.022263903357991117, 'dA_dEa': -1.8101259933535947, 'dE0_dEa': 0.046735863794425854, 'dn_dEa': 0.10390597320434176, 'name': 'C4H6-2 + C4H6 <=> C8H12'}, {'dA': 0.4650710943306337, 'dE0': 0.002640405194971557, 'dn': -0.022263903357991117, 'dA_dEa': -1.8054235557711562, 'dE0_dEa': 0.046765655055648114, 'dn_dEa': 0.10363519512467168, 'name': 'C4H6-3 + C4H6 <=> C8H12-2'}, {'dA': 0.20744291362719888, 'dE0': 0.000895133446398016, 'dn': -0.007542407383535384, 'dA_dEa': 1.8336172971482398, 'dE0_dEa': 0.06567145545572119, 'dn_dEa': -0.1043551705419551, 'name': 'C5H8 + C4H6 <=> C9H14'}, {'dA': 0.20744291362719888, 'dE0': 0.000895133446398016, 'dn': -0.007542407383535384, 'dA_dEa': 1.8299325450696697, 'dE0_dEa': 0.06564823462807329, 'dn_dEa': -0.10414285580987032, 'name': 'C5H8-2 + C4H6 <=> C9H14-2'}, {'dA': 0.27908982358229883, 'dE0': 0.0018595416973416084, 'dn': -0.015677594450135876, 'dA_dEa': -1.3138015306709887, 'dE0_dEa': -0.004431859873519204, 'dn_dEa': 0.07511041266826139, 'name': 'C5H8-3 + C2H4 <=> C7H12'}, {'dA': 0.27908982358229883, 'dE0': 0.0018595416973416084, 'dn': -0.015677594450135876, 'dA_dEa': -1.3138015306709887, 'dE0_dEa': -0.004431859873519204, 'dn_dEa': 0.07511041266826139, 'name': 'C2H4 + C5H8-4 <=> C7H12-2'}, {'dA': 0.5509845025138457, 'dE0': 0.0032224066412600847, 'dn': -0.027173209435920265, 'dA_dEa': -2.3818594016183208, 'dE0_dEa': 0.02900742214336426, 'dn_dEa': 0.13646668768148099, 'name': 'C4H6-3 + C5H8-3 <=> C9H14-3'}, {'dA': 0.5509845025120693, 'dE0': 0.0032224066412600847, 'dn': -0.027173209435722306, 'dA_dEa': -2.3825555590540186, 'dE0_dEa': 0.029002765959884255, 'dn_dEa': 0.13650654445363564, 'name': 'C4H6-2 + C5H8-4 <=> C9H14-4'}, {'dA': 0.8493365053930771, 'dE0': 0.005243493042934828, 'dn': -0.04422182825653708, 'dA_dEa': -9.421949974593929, 'dE0_dEa': -0.0009930438194183675, 'dn_dEa': 0.5388924081219869, 'name': 'C2H4 + C6H10-2 <=> C8H14'}, {'dA': 0.5818281034973368, 'dE0': 0.0034313590969369556, 'dn': -0.02893568259207419, 'dA_dEa': -5.313057029557785, 'dE0_dEa': 0.028292323029004744, 'dn_dEa': 0.3041139741710978, 'name': 'C3H6 + C6H10-2 <=> C9H16'}, {'dA': 0.5818281034955605, 'dE0': 0.0034313590969369556, 'dn': -0.02893568259207419, 'dA_dEa': -5.313057029614629, 'dE0_dEa': 0.028292323028592792, 'dn_dEa': 0.3041139741742651, 'name': 'C3H6-2 + C6H10-2 <=> C9H16-2'}, {'dA': -0.16150896262702832, 'dE0': -0.0016042094063242673, 'dn': 0.013540472184379714, 'dA_dEa': 6.291622424788894, 'dE0_dEa': 0.09106382739712313, 'dn_dEa': -0.35913852413414665, 'name': 'C4H6-2 + C6H10-2 <=> C10H16'}, {'dA': -0.1615089626110411, 'dE0': -0.0016042094061182908, 'dn': 0.013540472183389912, 'dA_dEa': 6.2954421806107606, 'dE0_dEa': 0.0910881884334355, 'dn_dEa': -0.35935831514390454, 'name': 'C4H6-3 + C6H10-2 <=> C10H16-2'}, {'dA': -0.4011239923880525, 'dE0': -0.0032271356251006573, 'dn': 0.027232969797255993, 'dA_dEa': 7.686578951701287, 'dE0_dEa': 0.09235816173027242, 'dn_dEa': -0.438911010457687, 'name': 'C5H8 + C6H10-2 <=> C11H18'}, {'dA': -0.40112399239160523, 'dE0': -0.0032271356251006573, 'dn': 0.027232969797453953, 'dA_dEa': 7.689111653040606, 'dE0_dEa': 0.0923742314627874, 'dn_dEa': -0.4390568542255562, 'name': 'C5H8-2 + C6H10-2 <=> C11H18-2'}, {'dA': 0.03154231284519319, 'dE0': 0.00018262984120868118, 'dn': -0.0015320622073729554, 'dA_dEa': 2.49174831551385, 'dE0_dEa': 0.02061480683667459, 'dn_dEa': -0.1423540797189104, 'name': 'C7H10 + C4H8 <=> C11H18-3'}]
""",
)

entry(
    index = 3,
    label = "Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd",
    kinetics = ArrheniusBM(A=(1.95896e-11,'m^3/(mol*s)'), n=4.15719, w0=(852250,'J/mol'), E0=(206824,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00023424662986478353, var=0.0043250921906934775, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
            Total Standard Deviation in ln(k): 0.1324308299850172"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
Total Standard Deviation in ln(k): 0.1324308299850172""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
Total Standard Deviation in ln(k): 0.1324308299850172
sensitivities = [{'dA': 0.9217044537771406, 'dE0': 0.001955999061943769, 'dn': -0.013051158787765974, 'dA_dEa': -5.16234686679752, 'dE0_dEa': 0.2835651198786664, 'dn_dEa': 0.1612750063002804, 'name': 'C3H4 + C4H6 <=> C7H10-2'}, {'dA': 0.07703470584631016, 'dE0': -0.001959287611350428, 'dn': 0.013074898018663147, 'dA_dEa': 3.196796789034192, 'dE0_dEa': 0.33216099902978674, 'dn_dEa': -0.09722526087108035, 'name': 'C3H4-2 + C4H6 <=> C7H10-3'}]
""",
)

entry(
    index = 4,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_1CdN3dN5dcS4dS6d-inRing",
    kinetics = ArrheniusBM(A=(8.11e-08,'m^3/(mol*s)'), n=3.05, w0=(858000,'J/mol'), E0=(145464,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_1CdN3dN5dcS4dS6d-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_1CdN3dN5dcS4dS6d-inRing
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_1CdN3dN5dcS4dS6d-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_1CdN3dN5dcS4dS6d-inRing
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.7345006522121899, 'dn_dEa': 0.0, 'name': 'C7H10 + C4H8 <=> C11H18-3'}]
""",
)

entry(
    index = 5,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing",
    kinetics = ArrheniusBM(A=(0.000127046,'m^3/(mol*s)'), n=2.15007, w0=(858000,'J/mol'), E0=(142104,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06358824511050899, var=3.792920539332787, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing',), comment="""BM rule fitted to 16 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing
            Total Standard Deviation in ln(k): 4.064075581202041"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing
Total Standard Deviation in ln(k): 4.064075581202041""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing
Total Standard Deviation in ln(k): 4.064075581202041
sensitivities = [{'dA': 0.3357255775658189, 'dE0': 0.0022499497970484977, 'dn': -0.01863295637784941, 'dA_dEa': -0.6942500464789046, 'dE0_dEa': -0.0016749431032605127, 'dn_dEa': 0.03911018458064382, 'name': 'C4H6 + C2H4 <=> C6H10'}, {'dA': 0.5177268389840466, 'dE0': 0.0030037359812270614, 'dn': -0.024879062682755096, 'dA_dEa': -1.533467577244876, 'dE0_dEa': 0.049033782286489434, 'dn_dEa': 0.0868014232643928, 'name': 'C4H6-2 + C4H6 <=> C8H12'}, {'dA': 0.5177268389822702, 'dE0': 0.0030037359812270614, 'dn': -0.024879062682755096, 'dA_dEa': -1.5288775000003603, 'dE0_dEa': 0.049063121157318534, 'dn_dEa': 0.08654118133917378, 'name': 'C4H6-3 + C4H6 <=> C8H12-2'}, {'dA': 0.25737721669119645, 'dE0': 0.001234941949469968, 'dn': -0.010221782014602448, 'dA_dEa': 2.140187456321621, 'dE0_dEa': 0.06820123714188497, 'dn_dEa': -0.12006673016577797, 'name': 'C5H8 + C4H6 <=> C9H14'}, {'dA': 0.25737721669119645, 'dE0': 0.001234941949469968, 'dn': -0.010221782014602448, 'dA_dEa': 2.134682449611582, 'dE0_dEa': 0.0681668140938284, 'dn_dEa': -0.11975380909948652, 'name': 'C5H8-2 + C4H6 <=> C9H14-2'}, {'dA': 0.3416588178116008, 'dE0': 0.002290293261320571, 'dn': -0.01896695488629068, 'dA_dEa': -1.252823324550927, 'dE0_dEa': -0.004008869937757914, 'dn_dEa': 0.07056845286044655, 'name': 'C5H8-3 + C2H4 <=> C7H12'}, {'dA': 0.3416588178116008, 'dE0': 0.002290293261320571, 'dn': -0.01896695488629068, 'dA_dEa': -1.2528233245491507, 'dE0_dEa': -0.004008869937757914, 'dn_dEa': 0.07056845286044655, 'name': 'C2H4 + C5H8-4 <=> C7H12-2'}, {'dA': 0.6044024820327065, 'dE0': 0.003592655499009081, 'dn': -0.029758714407115684, 'dA_dEa': -2.1719261246497985, 'dE0_dEa': 0.030734757892636754, 'dn_dEa': 0.12263685318153383, 'name': 'C4H6-3 + C5H8-3 <=> C9H14-3'}, {'dA': 0.6044024820327065, 'dE0': 0.003592655499009081, 'dn': -0.029758714407115684, 'dA_dEa': -2.163890029960552, 'dE0_dEa': 0.030786046057204242, 'dn_dEa': 0.12218116749031104, 'name': 'C4H6-2 + C5H8-4 <=> C9H14-4'}, {'dA': 0.9064901297418547, 'dE0': 0.00564471535813824, 'dn': -0.04676607768455101, 'dA_dEa': -9.249264623071648, 'dE0_dEa': 0.00048085627684298006, 'dn_dEa': 0.5212187676539568, 'name': 'C2H4 + C6H10-2 <=> C8H14'}, {'dA': 0.6364832226638119, 'dE0': 0.003810230822749586, 'dn': -0.031565181684085196, 'dA_dEa': -5.065064480153428, 'dE0_dEa': 0.03036667201486, 'dn_dEa': 0.2856657584774323, 'name': 'C3H6 + C6H10-2 <=> C9H16'}, {'dA': 0.6364832226531537, 'dE0': 0.003810230822749586, 'dn': -0.03156518168350009, 'dA_dEa': -5.069758850416609, 'dE0_dEa': 0.030336563729687484, 'dn_dEa': 0.28593177342913684, 'name': 'C3H6-2 + C6H10-2 <=> C9H16-2'}, {'dA': -0.11508574461772826, 'dE0': -0.0012956452639791814, 'dn': 0.010747202212532538, 'dA_dEa': 6.631999431219901, 'dE0_dEa': 0.09388115476110642, 'dn_dEa': -0.37298302364018565, 'name': 'C4H6-2 + C6H10-2 <=> C10H16'}, {'dA': -0.11508574461772826, 'dE0': -0.001295645264185642, 'dn': 0.010747202212532538, 'dA_dEa': 6.637832807515685, 'dE0_dEa': 0.09391768449991637, 'dn_dEa': -0.37331454653072516, 'name': 'C4H6-3 + C6H10-2 <=> C10H16-2'}, {'dA': -0.3564493802095507, 'dE0': -0.002935494626180404, 'dn': 0.024335551308249163, 'dA_dEa': 8.024642293267267, 'dE0_dEa': 0.09512122603657756, 'dn_dEa': -0.4514508936710066, 'name': 'C5H8 + C6H10-2 <=> C11H18'}, {'dA': -0.3564493802131034, 'dE0': -0.002935494626180404, 'dn': 0.024335551308444198, 'dA_dEa': 8.025501165261236, 'dE0_dEa': 0.09512551969135696, 'dn_dEa': -0.45150076619215385, 'name': 'C5H8-2 + C6H10-2 <=> C11H18-2'}]
""",
)

entry(
    index = 6,
    label = "Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct",
    kinetics = ArrheniusBM(A=(1.22e-07,'m^3/(mol*s)'), n=2.98, w0=(846500,'J/mol'), E0=(212387,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.599537448395895, 'dn_dEa': 0.0, 'name': 'C3H4 + C4H6 <=> C7H10-2'}]
""",
)

entry(
    index = 7,
    label = "Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct",
    kinetics = ArrheniusBM(A=(1.77e-07,'m^3/(mol*s)'), n=2.94, w0=(858000,'J/mol'), E0=(212844,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.6073954372956674, 'dn_dEa': 0.0, 'name': 'C3H4-2 + C4H6 <=> C7H10-3'}]
""",
)

entry(
    index = 8,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(3.26766e-09,'m^3/(mol*s)'), n=3.49827, w0=(858000,'J/mol'), E0=(131868,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.14443333294059355, var=8.305517039704704, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R',), comment="""BM rule fitted to 7 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R
            Total Standard Deviation in ln(k): 6.14040277086316"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R
Total Standard Deviation in ln(k): 6.14040277086316""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R
Total Standard Deviation in ln(k): 6.14040277086316
sensitivities = [{'dA': 3.9033696373213935, 'dE0': 0.028097726849297004, 'dn': -0.12881604925460474, 'dA_dEa': -24.839823116599895, 'dE0_dEa': -0.05439138759216445, 'dn_dEa': 0.8517794034955493, 'name': 'C2H4 + C6H10-2 <=> C8H14'}, {'dA': 3.3076176590615436, 'dE0': 0.02364743209400343, 'dn': -0.10840844609393364, 'dA_dEa': -14.151531127483134, 'dE0_dEa': 0.028473385348211602, 'dn_dEa': 0.4856701522569198, 'name': 'C3H6 + C6H10-2 <=> C9H16'}, {'dA': 3.3076176594487894, 'dE0': 0.023647432096691026, 'dn': -0.10840844610735047, 'dA_dEa': -14.140056359936318, 'dE0_dEa': 0.028550878537196758, 'dn_dEa': 0.48527248277342055, 'name': 'C3H6-2 + C6H10-2 <=> C9H16-2'}, {'dA': 1.6509816824312338, 'dE0': 0.01127229381605056, 'dn': -0.0516600583161261, 'dA_dEa': 16.766264751920517, 'dE0_dEa': 0.22636534802717498, 'dn_dEa': -0.5736518339695151, 'name': 'C4H6-2 + C6H10-2 <=> C10H16'}, {'dA': 1.6509816835716549, 'dE0': 0.011272293824001366, 'dn': -0.05166005835554545, 'dA_dEa': 16.76242187861206, 'dE0_dEa': 0.2263397837264011, 'dn_dEa': -0.5735184235912787, 'name': 'C4H6-3 + C6H10-2 <=> C10H16-2'}, {'dA': 1.1180534277636223, 'dE0': 0.007291446676222547, 'dn': -0.033404413756663906, 'dA_dEa': 20.76096139677348, 'dE0_dEa': 0.23917518791892803, 'dn_dEa': -0.7106053307590099, 'name': 'C5H8 + C6H10-2 <=> C11H18'}, {'dA': 1.1180534278240184, 'dE0': 0.007291446676670479, 'dn': -0.03340441375868237, 'dA_dEa': 20.725916907550054, 'dE0_dEa': 0.23893074203179848, 'dn_dEa': -0.7093951919400399, 'name': 'C5H8-2 + C6H10-2 <=> C11H18-2'}]
""",
)

entry(
    index = 9,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R",
    kinetics = ArrheniusBM(A=(0.891564,'m^3/(mol*s)'), n=0.985671, w0=(858000,'J/mol'), E0=(150184,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.007052630370330484, var=0.9912014232841642, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R',), comment="""BM rule fitted to 4 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R
            Total Standard Deviation in ln(k): 2.0136163611420597"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R
Total Standard Deviation in ln(k): 2.0136163611420597""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R
Total Standard Deviation in ln(k): 2.0136163611420597
sensitivities = [{'dA': 0.6051180024034375, 'dE0': 0.0022510631124624653, 'dn': -0.042467746287581834, 'dA_dEa': -5.13338990096569, 'dE0_dEa': 0.15077838798253565, 'dn_dEa': 0.6153901069222738, 'name': 'C4H6-3 + C4H6 <=> C8H12-2'}, {'dA': -0.15563983228896233, 'dE0': -0.0025863818412942266, 'dn': 0.04844035858600223, 'dA_dEa': 4.520562247312175, 'dE0_dEa': 0.19429169381435724, 'dn_dEa': -0.5384403875292031, 'name': 'C5H8 + C4H6 <=> C9H14'}, {'dA': -0.15563983230705897, 'dE0': -0.0025863818412942266, 'dn': 0.04844035858827827, 'dA_dEa': 4.465085516101634, 'dE0_dEa': 0.19396095601136795, 'dn_dEa': -0.5317620389309538, 'name': 'C5H8-2 + C4H6 <=> C9H14-2'}, {'dA': 0.8511754034178192, 'dE0': 0.0038177014997990296, 'dn': -0.07186632028033224, 'dA_dEa': -6.690835033402913, 'dE0_dEa': 0.09779743959884009, 'dn_dEa': 0.8010382160492491, 'name': 'C4H6-3 + C5H8-3 <=> C9H14-3'}]
""",
)

entry(
    index = 10,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R",
    kinetics = ArrheniusBM(A=(132000,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(197826,'J/mol'), Tmin=(1000,'K'), Tmax=(1180,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.6578886399861879, 'dn_dEa': nan, 'name': 'C5H8-3 + C2H4 <=> C7H12'}]
""",
)

entry(
    index = 11,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R",
    kinetics = ArrheniusBM(A=(0.0381414,'m^3/(mol*s)'), n=1.36206, w0=(858000,'J/mol'), E0=(137373,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1512664848213554, var=3.20497538350606, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R',), comment="""BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R
            Total Standard Deviation in ln(k): 6.4815953127947035"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R
Total Standard Deviation in ln(k): 6.4815953127947035""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R
Total Standard Deviation in ln(k): 6.4815953127947035
sensitivities = [{'dA': 0.9426320876847399, 'dE0': 0.006255716017038993, 'dn': -0.0774728517178877, 'dA_dEa': -15.610741205352717, 'dE0_dEa': -0.05228573089012652, 'dn_dEa': 1.3687871463508798, 'name': 'C2H4 + C5H8-4 <=> C7H12-2'}, {'dA': 0.08726763074974182, 'dE0': -0.006042507284759497, 'dn': 0.0748053386435081, 'dA_dEa': 10.188135346045136, 'dE0_dEa': 0.6602455719034978, 'dn_dEa': -0.8887032159207243, 'name': 'C4H6-2 + C5H8-4 <=> C9H14-4'}]
""",
)

entry(
    index = 12,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    kinetics = ArrheniusBM(A=(8910,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(169755,'J/mol'), Tmin=(464,'K'), Tmax=(557,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.6432663222326738, 'dn_dEa': nan, 'name': 'C4H6-2 + C4H6 <=> C8H12'}]
""",
)

entry(
    index = 13,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R",
    kinetics = ArrheniusBM(A=(3.03944e-10,'m^3/(mol*s)'), n=3.77961, w0=(858000,'J/mol'), E0=(119950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.14910705179089842, var=13.709980217686734, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R',), comment="""BM rule fitted to 4 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R
            Total Standard Deviation in ln(k): 7.797571490148185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R
Total Standard Deviation in ln(k): 7.797571490148185""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R
Total Standard Deviation in ln(k): 7.797571490148185
sensitivities = [{'dA': 13.24076998053915, 'dE0': 0.10765294906228991, 'dn': -0.4218963021189985, 'dA_dEa': -50.78391361817429, 'dE0_dEa': -0.1603610332700877, 'dn_dEa': 1.6510272186317991, 'name': 'C3H6-2 + C6H10-2 <=> C9H16-2'}, {'dA': 8.5432457240851, 'dE0': 0.06872105587826731, 'dn': -0.2693399656287893, 'dA_dEa': 22.310109548952866, 'dE0_dEa': 0.381203001472469, 'dn_dEa': -0.7232233229620262, 'name': 'C4H6-3 + C6H10-2 <=> C10H16-2'}, {'dA': 7.044073206718402, 'dE0': 0.0562921132659135, 'dn': -0.22065496998041811, 'dA_dEa': 33.88037218834601, 'dE0_dEa': 0.44401897326668444, 'dn_dEa': -1.0992053284154386, 'name': 'C5H8 + C6H10-2 <=> C11H18'}, {'dA': 7.017349196847595, 'dE0': 0.05608545346256477, 'dn': -0.2197799905227399, 'dA_dEa': 33.89348119627318, 'dE0_dEa': 0.444116227443432, 'dn_dEa': -1.0996364959832972, 'name': 'C5H8-2 + C6H10-2 <=> C11H18-2'}]
""",
)

entry(
    index = 14,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    kinetics = ArrheniusBM(A=(6.76344e-05,'m^3/(mol*s)'), n=2.19153, w0=(858000,'J/mol'), E0=(149206,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01321817248392336, var=26.283515993403185, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R',), comment="""BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
            Total Standard Deviation in ln(k): 10.310977355070442"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 10.310977355070442""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 10.310977355070442
sensitivities = [{'dA': 4.609409645003179, 'dE0': 0.02683672533419264, 'dn': -0.20350315625665485, 'dA_dEa': -34.90220085985592, 'dE0_dEa': 0.1825921244336756, 'dn_dEa': 1.7319670564343546, 'name': 'C3H6 + C6H10-2 <=> C9H16'}, {'dA': -0.6736432735224471, 'dE0': -0.007666569117484503, 'dn': 0.058100908306954656, 'dA_dEa': 39.916964147498526, 'dE0_dEa': 0.5699769015038603, 'dn_dEa': -1.9739046716495592, 'name': 'C4H6-2 + C6H10-2 <=> C10H16'}]
""",
)

entry(
    index = 15,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    kinetics = ArrheniusBM(A=(0.119605,'m^3/(mol*s)'), n=1.17525, w0=(858000,'J/mol'), E0=(149276,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7763568394002489e-15, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R',), comment="""BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
            Total Standard Deviation in ln(k): 4.463208139196605e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 4.463208139196605e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 4.463208139196605e-15
sensitivities = [{'dA': 0.4998924085218288, 'dE0': 8.495402884834047e-07, 'dn': -1.4782249979539281e-05, 'dA_dEa': -1.0089523707318415, 'dE0_dEa': 0.3259669408657731, 'dn_dEa': 0.1077326678355514, 'name': 'C5H8 + C4H6 <=> C9H14'}, {'dA': 0.499892408522717, 'dE0': 8.495402884834047e-07, 'dn': -1.4782249979539281e-05, 'dA_dEa': -1.0092073388171532, 'dE0_dEa': 0.32596541158478726, 'dn_dEa': 0.10775915384340301, 'name': 'C5H8-2 + C4H6 <=> C9H14-2'}]
""",
)

entry(
    index = 16,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-2CdN3dN5dcS4dS6d-R",
    kinetics = ArrheniusBM(A=(1020,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(143654,'J/mol'), Tmin=(492,'K'), Tmax=(606,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-2CdN3dN5dcS4dS6d-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-2CdN3dN5dcS4dS6d-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-2CdN3dN5dcS4dS6d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-2CdN3dN5dcS4dS6d-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.5907652510936465, 'dn_dEa': nan, 'name': 'C4H6-3 + C5H8-3 <=> C9H14-3'}]
""",
)

entry(
    index = 17,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    kinetics = ArrheniusBM(A=(1020,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(143654,'J/mol'), Tmin=(492,'K'), Tmax=(606,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.5907652510936465, 'dn_dEa': nan, 'name': 'C4H6-2 + C5H8-4 <=> C9H14-4'}]
""",
)

entry(
    index = 18,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    kinetics = ArrheniusBM(A=(0.20079,'m^3/(mol*s)'), n=1.18774, w0=(858000,'J/mol'), E0=(122278,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3988810110276873e-14, var=4.978412222288914e-60, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R',), comment="""BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
            Total Standard Deviation in ln(k): 3.514776409617305e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 3.514776409617305e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 3.514776409617305e-14
sensitivities = [{'dA': 0.5000636575236967, 'dE0': 2.320704269614345e-06, 'dn': -3.408327598380246e-05, 'dA_dEa': -0.9922133454577358, 'dE0_dEa': 0.3045649105294763, 'dn_dEa': 0.11356378884219183, 'name': 'C5H8 + C6H10-2 <=> C11H18'}, {'dA': 0.5001798241857642, 'dE0': 3.1905781765292986e-06, 'dn': -4.669733519834298e-05, 'dA_dEa': -0.9927129675356677, 'dE0_dEa': 0.30456120126680203, 'dn_dEa': 0.11361809063482818, 'name': 'C5H8-2 + C6H10-2 <=> C11H18-2'}]
""",
)

entry(
    index = 19,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1020,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(144918,'J/mol'), Tmin=(379,'K'), Tmax=(581,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-8R!H-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.6203506326644614, 'dn_dEa': nan, 'name': 'C4H6-3 + C6H10-2 <=> C10H16-2'}]
""",
)

entry(
    index = 20,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1020,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(144918,'J/mol'), Tmin=(379,'K'), Tmax=(581,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.6203506326644614, 'dn_dEa': nan, 'name': 'C4H6-2 + C6H10-2 <=> C10H16'}]
""",
)

entry(
    index = 21,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(899,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(156378,'J/mol'), Tmin=(515,'K'), Tmax=(572,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-7R!H-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.6295845433903577, 'dn_dEa': nan, 'name': 'C5H8-2 + C4H6 <=> C9H14-2'}]
""",
)

entry(
    index = 22,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1260,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(127005,'J/mol'), Tmin=(352,'K'), Tmax=(423,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.5913845582405394, 'dn_dEa': nan, 'name': 'C5H8-2 + C6H10-2 <=> C11H18-2'}]
""",
)

