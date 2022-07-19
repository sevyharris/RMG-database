#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(9.99565e-05,'m^3/(mol*s)'), n=2.24812, w0=(861955,'J/mol'), E0=(156384,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11552723360577359, var=4.10540683265734, Tref=1000.0, N=22, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 22 training reactions at node Root
            Total Standard Deviation in ln(k): 4.352224262791556"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root
Total Standard Deviation in ln(k): 4.352224262791556""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root
Total Standard Deviation in ln(k): 4.352224262791556
sensitivities = [{'dA': 0.05179212948825411, 'dE0': 0.0003738611476484235, 'dn': -0.0023930239396135157, 'dA_dEa': -0.2076293550139725, 'dE0_dEa': -0.00032390094809207654, 'dn_dEa': 0.010009459547742882, 'name': 'C4H6 + C2H4 <=> C6H10'}, {'dA': 0.1852709736987128, 'dE0': 0.00114064561937579, 'dn': -0.007302461678413082, 'dA_dEa': -1.6935813962748103, 'dE0_dEa': 0.011462843765099548, 'dn_dEa': 0.08175529568127546, 'name': 'C4H6-2 + C4H6 <=> C8H12'}, {'dA': 0.18527097370048914, 'dE0': 0.00114064561937579, 'dn': -0.007302461678585178, 'dA_dEa': -1.694650079770286, 'dE0_dEa': 0.011455414088319422, 'dn_dEa': 0.0818072479543483, 'name': 'C4H6-3 + C4H6 <=> C8H12-2'}, {'dA': 0.12776626244460929, 'dE0': 0.0007080834252279188, 'dn': -0.004532976537563819, 'dA_dEa': -0.9364565899368992, 'dE0_dEa': 0.014801635422333993, 'dn_dEa': 0.045273161324461464, 'name': 'C5H8 + C4H6 <=> C9H14'}, {'dA': 0.1277662624197403, 'dE0': 0.0007080834250356695, 'dn': -0.00453297653635915, 'dA_dEa': -0.9364565899368992, 'dE0_dEa': 0.014801635422333993, 'dn_dEa': 0.045273161324461464, 'name': 'C5H8-2 + C4H6 <=> C9H14-2'}, {'dA': 0.05302146312580776, 'dE0': 0.0003831080852035287, 'dn': -0.002452230243806151, 'dA_dEa': -0.34018578324083587, 'dE0_dEa': -0.000726227040442972, 'dn_dEa': 0.01639820546628318, 'name': 'C5H8-3 + C2H4 <=> C7H12'}, {'dA': 0.05302146312580776, 'dE0': 0.0003831080852035287, 'dn': -0.002452230243806151, 'dA_dEa': -0.34018578324083587, 'dE0_dEa': -0.000726227040442972, 'dn_dEa': 0.01639820546628318, 'name': 'C2H4 + C5H8-4 <=> C7H12-2'}, {'dA': 0.20305379745624313, 'dE0': 0.0012743927780511164, 'dn': -0.00815891485341872, 'dA_dEa': -1.4587767064250743, 'dE0_dEa': 0.007544490570723044, 'dn_dEa': 0.07040173749148497, 'name': 'C4H6-3 + C5H8-3 <=> C9H14-3'}, {'dA': 0.2030537974580195, 'dE0': 0.0012743927780511164, 'dn': -0.00815891485341872, 'dA_dEa': -1.4592051166656903, 'dE0_dEa': 0.007541518218311238, 'dn_dEa': 0.07042257447934464, 'name': 'C4H6-2 + C5H8-4 <=> C9H14-4'}, {'dA': 0.25398367469267624, 'dE0': 0.0016575135886179218, 'dn': -0.010611736376292095, 'dA_dEa': -2.9480908618854023, 'dE0_dEa': 0.003600689027340223, 'dn_dEa': 0.14218605625013778, 'name': 'C2H4 + C6H10-2 <=> C8H14'}, {'dA': 0.19459331870132968, 'dE0': 0.0012108040670108075, 'dn': -0.007751408896572591, 'dA_dEa': -2.2746525104458133, 'dE0_dEa': 0.00925955517785695, 'dn_dEa': 0.10975652155132908, 'name': 'C3H6 + C6H10-2 <=> C9H16'}, {'dA': 0.19459331870132968, 'dE0': 0.0012108040670108075, 'dn': -0.007751408896572591, 'dA_dEa': -2.2757705030722892, 'dE0_dEa': 0.009251742334836409, 'dn_dEa': 0.10981082280274844, 'name': 'C3H6-2 + C6H10-2 <=> C9H16-2'}, {'dA': 0.04774679259079122, 'dE0': 0.00010621309759713999, 'dn': -0.0006791189290587153, 'dA_dEa': -0.07610101599198899, 'dE0_dEa': 0.019302651204842595, 'dn_dEa': 0.003821961210883832, 'name': 'C4H6-2 + C6H10-2 <=> C10H16'}, {'dA': 0.04774679265118735, 'dE0': 0.00010621309817388777, 'dn': -0.0006791189319843408, 'dA_dEa': -0.07610101606659597, 'dE0_dEa': 0.019302651204265844, 'dn_dEa': 0.0038219612144978397, 'name': 'C4H6-3 + C6H10-2 <=> C10H16-2'}, {'dA': -0.0048456643835242735, 'dE0': -0.0002894834782504355, 'dn': 0.001853724342249146, 'dA_dEa': 0.35291519481365774, 'dE0_dEa': 0.019182637997913515, 'dn_dEa': -0.01686630291926931, 'name': 'C5H8 + C6H10-2 <=> C11H18'}, {'dA': -0.00484566438530063, 'dE0': -0.0002894834782504355, 'dn': 0.001853724342249146, 'dA_dEa': 0.3515239980434291, 'dE0_dEa': 0.019172884070981097, 'dn_dEa': -0.01679876934508905, 'name': 'C5H8-2 + C6H10-2 <=> C11H18-2'}, {'dA': 0.0021270255050611763, 'dE0': 2.6978762152343347e-07, 'dn': -1.1027622152178513e-06, 'dA_dEa': 0.3818496293988426, 'dE0_dEa': 0.004404229874799659, 'dn_dEa': -0.018378154788347603, 'name': 'C7H10 + C4H8 <=> C11H18-3'}, {'dA': 0.10534429379306426, 'dE0': 0.0007767016465454831, 'dn': -0.004972141917570377, 'dA_dEa': -1.0860288988433584, 'dE0_dEa': -0.006430060258798002, 'dn_dEa': 0.05231803273679397, 'name': 'C3H4 + C4H6 <=> C7H10-2'}, {'dA': 0.0926588640180017, 'dE0': 0.0006812940193725584, 'dn': -0.004361188723589407, 'dA_dEa': -1.0407120166392483, 'dE0_dEa': -0.006033433565823956, 'dn_dEa': 0.05013599190660023, 'name': 'C3H4-2 + C4H6 <=> C7H10-3'}, {'dA': 2.0386503134484117, 'dE0': 0.013958164852432259, 'dn': -0.0893610301970031, 'dA_dEa': -22.466277627045258, 'dE0_dEa': -0.049900509464668945, 'dn_dEa': 1.0829360733136641, 'name': 'C4H6 + C2H4 <=> C6H10'}, {'dA': 0.21864889371949936, 'dE0': 0.0002669639764164994, 'dn': -0.001708545858368387, 'dA_dEa': -0.04176966733738146, 'dE0_dEa': 0.12069654507969964, 'dn_dEa': 0.002964063832687728, 'name': 'C4H6O + C2H4 <=> C6H10O'}, {'dA': -2.732469395811367, 'dE0': -0.021931648188854732, 'dn': 0.1404205199599446, 'dA_dEa': 39.87245102637522, 'dE0_dEa': 0.44363573884163954, 'dn_dEa': -1.9191690982491907, 'name': 'C4H6 + C2H4O <=> C6H10O-2'}]
""",
)

entry(
    index = 2,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd",
    kinetics = ArrheniusBM(A=(1.91831e-06,'m^3/(mol*s)'), n=2.76724, w0=(858000,'J/mol'), E0=(149896,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.054209388020816617, var=3.626490200834218, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd',), comment="""BM rule fitted to 19 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
            Total Standard Deviation in ln(k): 3.953890828477951"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
Total Standard Deviation in ln(k): 3.953890828477951""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
Total Standard Deviation in ln(k): 3.953890828477951
sensitivities = [{'dA': 0.10436026921923952, 'dE0': 0.0008048550552052346, 'dn': -0.004337063947428487, 'dA_dEa': -0.1259208833399722, 'dE0_dEa': 0.0006059493069770727, 'dn_dEa': 0.005378719331055531, 'name': 'C4H6 + C2H4 <=> C6H10'}, {'dA': 0.1294958267284017, 'dE0': 0.0006967018501300024, 'dn': -0.0037539314647567316, 'dA_dEa': 0.1966824250310356, 'dE0_dEa': 0.03285109769329658, 'dn_dEa': -0.00815065487869102, 'name': 'C4H6-2 + C4H6 <=> C8H12'}, {'dA': 0.12949582672662535, 'dE0': 0.0006967018501300024, 'dn': -0.0037539314647567316, 'dA_dEa': 0.19773142627956777, 'dE0_dEa': 0.03285872704578099, 'dn_dEa': -0.008195799576851582, 'name': 'C4H6-3 + C4H6 <=> C8H12-2'}, {'dA': 0.05185331934321485, 'dE0': 8.304684705950196e-05, 'dn': -0.0004449281030168058, 'dA_dEa': 1.0555949313567679, 'dE0_dEa': 0.03659024836352515, 'dn_dEa': -0.04477979330575714, 'name': 'C5H8 + C4H6 <=> C9H14'}, {'dA': 0.05185331934321485, 'dE0': 8.304684705950196e-05, 'dn': -0.0004449281030168058, 'dA_dEa': 1.0552523583325975, 'dE0_dEa': 0.03658773071149649, 'dn_dEa': -0.044765077741791434, 'name': 'C5H8-2 + C4H6 <=> C9H14-2'}, {'dA': 0.10602248927683634, 'dE0': 0.0008179911229399439, 'dn': -0.004407906145495463, 'dA_dEa': -0.25216978454881134, 'dE0_dEa': 0.00037725534271882734, 'dn_dEa': 0.010764945163567003, 'name': 'C5H8-3 + C2H4 <=> C7H12'}, {'dA': 0.10602248927683634, 'dE0': 0.0008179911229399439, 'dn': -0.004407906145495463, 'dA_dEa': -0.25216978453637684, 'dE0_dEa': 0.00037725534271882734, 'dn_dEa': 0.010764945162957756, 'name': 'C2H4 + C5H8-4 <=> C7H12-2'}, {'dA': 0.15338759609663824, 'dE0': 0.0008855641642264311, 'dn': -0.004772142297820266, 'dA_dEa': -0.08287890642756171, 'dE0_dEa': 0.023293585944290755, 'dn_dEa': 0.0037110149544662767, 'name': 'C4H6-3 + C5H8-3 <=> C9H14-3'}, {'dA': 0.1533875960859801, 'dE0': 0.0008855641640272259, 'dn': -0.004772142297363332, 'dA_dEa': -0.08252718017055315, 'dE0_dEa': 0.023296053709355325, 'dn_dEa': 0.0036958016999914735, 'name': 'C4H6-2 + C5H8-4 <=> C9H14-4'}, {'dA': 0.22221891011222855, 'dE0': 0.0014295518418549929, 'dn': -0.007705643086005536, 'dA_dEa': -1.4755042142839363, 'dE0_dEa': 0.02166966528823067, 'dn_dEa': 0.06312951677827412, 'name': 'C2H4 + C6H10-2 <=> C8H14'}, {'dA': 0.14217756450742203, 'dE0': 0.0007968951435651692, 'dn': -0.00429443379738477, 'dA_dEa': -0.42431908838129984, 'dE0_dEa': 0.030746708549099944, 'dn_dEa': 0.01833579727255003, 'name': 'C3H6 + C6H10-2 <=> C9H16'}, {'dA': 0.14217756450742203, 'dE0': 0.0007968951435651692, 'dn': -0.00429443379738477, 'dA_dEa': -0.42431908838129984, 'dE0_dEa': 0.030746708549099944, 'dn_dEa': 0.01833579727255003, 'name': 'C3H6-2 + C6H10-2 <=> C9H16-2'}, {'dA': -0.05612909206221325, 'dE0': -0.0007703523214644215, 'dn': 0.004157148012761513, 'dA_dEa': 2.102910235347598, 'dE0_dEa': 0.042321887059267524, 'dn_dEa': -0.08943202568403696, 'name': 'C4H6-2 + C6H10-2 <=> C10H16'}, {'dA': -0.05612909206221325, 'dE0': -0.0007703523214644215, 'dn': 0.004157148012761513, 'dA_dEa': 2.102910235347598, 'dE0_dEa': 0.042321887059267524, 'dn_dEa': -0.08943202568403696, 'name': 'C4H6-3 + C6H10-2 <=> C10H16-2'}, {'dA': -0.12742438531533634, 'dE0': -0.001333795402734687, 'dn': 0.007195674057230656, 'dA_dEa': 2.3677470855150538, 'dE0_dEa': 0.0400891848362051, 'dn_dEa': -0.10074941135048297, 'name': 'C5H8 + C6H10-2 <=> C11H18'}, {'dA': -0.12742438531355998, 'dE0': -0.001333795402734687, 'dn': 0.007195674057078344, 'dA_dEa': 2.3685737840380248, 'dE0_dEa': 0.040094939443829844, 'dn_dEa': -0.10078517148700888, 'name': 'C5H8-2 + C6H10-2 <=> C11H18-2'}, {'dA': 0.037279067910848895, 'dE0': 0.00027468214447969155, 'dn': -0.0014781603912279273, 'dA_dEa': 0.6962248788654136, 'dE0_dEa': 0.007483868268075894, 'dn_dEa': -0.029657148635746065, 'name': 'C7H10 + C4H8 <=> C11H18-3'}, {'dA': 2.0760800332999607, 'dE0': 0.01462587104640071, 'dn': -0.0788722443269625, 'dA_dEa': -20.02043326952084, 'dE0_dEa': -0.004225986730223323, 'dn_dEa': 0.8543799453768398, 'name': 'C4H6 + C2H4 <=> C6H10'}, {'dA': -0.6062471875321719, 'dE0': -0.006574689872240684, 'dn': 0.035444054920145886, 'dA_dEa': 13.19258412982872, 'dE0_dEa': 0.260741951852818, 'dn_dEa': -0.5610944360842446, 'name': 'C4H6O + C2H4 <=> C6H10O'}]
""",
)

entry(
    index = 3,
    label = "Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd",
    kinetics = ArrheniusBM(A=(4.03757e-13,'m^3/(mol*s)'), n=4.52954, w0=(887000,'J/mol'), E0=(143100,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.0855622054326055, var=71.1568223758254, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd',), comment="""BM rule fitted to 3 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
            Total Standard Deviation in ln(k): 32.20120048283609"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
Total Standard Deviation in ln(k): 32.20120048283609""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
Total Standard Deviation in ln(k): 32.20120048283609
sensitivities = [{'dA': 1.2626348811012602, 'dE0': 0.010323880698433239, 'dn': -0.02791619185273589, 'dA_dEa': -11.077029563204887, 'dE0_dEa': -0.08120745990954512, 'dn_dEa': 0.24713930353827335, 'name': 'C3H4 + C4H6 <=> C7H10-2'}, {'dA': 1.179723093251669, 'dE0': 0.00963989123033498, 'dn': -0.026066621804258408, 'dA_dEa': -10.846994020903141, 'dE0_dEa': -0.07898385016439725, 'dn_dEa': 0.24200891125472523, 'name': 'C3H4-2 + C4H6 <=> C7H10-3'}, {'dA': 0.08422687693610914, 'dE0': -0.007365061346341166, 'dn': 0.019917397537395583, 'dA_dEa': 34.17522184409826, 'dE0_dEa': 1.1226718836169576, 'dn_dEa': -0.7593606214516335, 'name': 'C4H6 + C2H4O <=> C6H10O-2'}]
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
    kinetics = ArrheniusBM(A=(1.87428e-06,'m^3/(mol*s)'), n=2.77013, w0=(858000,'J/mol'), E0=(149855,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05447034486536388, var=3.639180470167681, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing',), comment="""BM rule fitted to 18 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing
            Total Standard Deviation in ln(k): 3.9612203289789876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing
Total Standard Deviation in ln(k): 3.9612203289789876""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing
Total Standard Deviation in ln(k): 3.9612203289789876
sensitivities = [{'dA': 0.11370144646784128, 'dE0': 0.000876919976941431, 'dn': -0.004729715257886379, 'dA_dEa': -0.11593029762126006, 'dE0_dEa': 0.0006872478364645906, 'dn_dEa': 0.004944650309722944, 'name': 'C4H6 + C2H4 <=> C6H10'}, {'dA': 0.1369938185753634, 'dE0': 0.0007533452281151081, 'dn': -0.0040646550714897, 'dA_dEa': 0.2391451421246679, 'dE0_dEa': 0.03328410337696844, 'dn_dEa': -0.009947110848769262, 'name': 'C4H6-2 + C4H6 <=> C8H12'}, {'dA': 0.13699381854161263, 'dE0': 0.0007533452279158266, 'dn': -0.004064655069968702, 'dA_dEa': 0.2391451421495369, 'dE0_dEa': 0.03328410337716772, 'dn_dEa': -0.00994711084983396, 'name': 'C4H6-3 + C4H6 <=> C8H12-2'}, {'dA': 0.05902198532937259, 'dE0': 0.0001367824987303296, 'dn': -0.0007462210810250589, 'dA_dEa': 1.0947730722820166, 'dE0_dEa': 0.03699473219103654, 'dn_dEa': -0.04638335456458669, 'name': 'C5H8 + C4H6 <=> C9H14'}, {'dA': 0.05902198532937259, 'dE0': 0.0001367824987303296, 'dn': -0.0007462210810250589, 'dA_dEa': 1.0947730722820166, 'dE0_dEa': 0.03699473219103654, 'dn_dEa': -0.04638335456458669, 'name': 'C5H8-2 + C4H6 <=> C9H14-2'}, {'dA': 0.11536521279965789, 'dE0': 0.0008900778644543159, 'dn': -0.004800523103751608, 'dA_dEa': -0.2419881468203311, 'dE0_dEa': 0.00046193646788663225, 'dn_dEa': 0.010315262755282184, 'name': 'C5H8-3 + C2H4 <=> C7H12'}, {'dA': 0.11536521279965789, 'dE0': 0.0008900778644543159, 'dn': -0.004800523103751608, 'dA_dEa': -0.2419881468203311, 'dE0_dEa': 0.00046193646788663225, 'dn_dEa': 0.010315262755282184, 'name': 'C2H4 + C5H8-4 <=> C7H12-2'}, {'dA': 0.16098540927524493, 'dE0': 0.0009430971855637906, 'dn': -0.005085697953051183, 'dA_dEa': -0.0504755621317854, 'dE0_dEa': 0.02362346257442537, 'dn_dEa': 0.0023264422791238683, 'name': 'C4H6-3 + C5H8-3 <=> C9H14-3'}, {'dA': 0.16098540927879765, 'dE0': 0.0009430971855637906, 'dn': -0.005085697953051183, 'dA_dEa': -0.0504755621317854, 'dE0_dEa': 0.02362346257442537, 'dn_dEa': 0.0023264422791238683, 'name': 'C4H6-2 + C5H8-4 <=> C9H14-4'}, {'dA': 0.23006604589783966, 'dE0': 0.0014893524540380745, 'dn': -0.008025727489079322, 'dA_dEa': -1.4433799632060298, 'dE0_dEa': 0.022023280008896234, 'dn_dEa': 0.061675949311648944, 'name': 'C2H4 + C6H10-2 <=> C8H14'}, {'dA': 0.1496434372949716, 'dE0': 0.00085338654729387, 'dn': -0.004603006823067261, 'dA_dEa': -0.3873464398563158, 'dE0_dEa': 0.03114555441169812, 'dn_dEa': 0.016738216554799956, 'name': 'C3H6 + C6H10-2 <=> C9H16'}, {'dA': 0.14964343729319524, 'dE0': 0.00085338654729387, 'dn': -0.004603006823067261, 'dA_dEa': -0.3873464398563158, 'dE0_dEa': 0.03114555441169812, 'dn_dEa': 0.016738216554799956, 'name': 'C3H6-2 + C6H10-2 <=> C9H16-2'}, {'dA': -0.04923103773713509, 'dE0': -0.0007193062346045117, 'dn': 0.0038609108344386358, 'dA_dEa': 2.146268618103756, 'dE0_dEa': 0.04275351165832697, 'dn_dEa': -0.0911529836192043, 'name': 'C4H6-2 + C6H10-2 <=> C10H16'}, {'dA': -0.04923103772292423, 'dE0': -0.0007193062344052302, 'dn': 0.0038609108338302366, 'dA_dEa': 2.1452618608199945, 'dE0_dEa': 0.04274613971670189, 'dn_dEa': -0.09110975799236612, 'name': 'C4H6-3 + C6H10-2 <=> C10H16-2'}, {'dA': -0.1207014674999973, 'dE0': -0.0012845036778606313, 'dn': 0.006902619558031476, 'dA_dEa': 2.412978637217388, 'dE0_dEa': 0.04051961529113255, 'dn_dEa': -0.10253679174180798, 'name': 'C5H8 + C6H10-2 <=> C11H18'}, {'dA': -0.12070146750177366, 'dE0': -0.0012845036778606313, 'dn': 0.006902619558183576, 'dA_dEa': 2.4129786372209407, 'dE0_dEa': 0.04051961529133183, 'dn_dEa': -0.10253679174196008, 'name': 'C5H8-2 + C6H10-2 <=> C11H18-2'}, {'dA': 2.0803642241118485, 'dE0': 0.014662722628861768, 'dn': -0.07892010436332707, 'dA_dEa': -19.95038416248149, 'dE0_dEa': -0.003273748667525934, 'dn_dEa': 0.8502130570303303, 'name': 'C4H6 + C2H4 <=> C6H10'}, {'dA': -0.6136110153214923, 'dE0': -0.006641015459935931, 'dn': 0.03573307907709516, 'dA_dEa': 13.410117576371816, 'dE0_dEa': 0.26301517955442644, 'dn_dEa': -0.5695651898970596, 'name': 'C4H6O + C2H4 <=> C6H10O'}]
""",
)

entry(
    index = 6,
    label = "Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct",
    kinetics = ArrheniusBM(A=(1.22e-07,'m^3/(mol*s)'), n=2.98, w0=(846500,'J/mol'), E0=(211218,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
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
    kinetics = ArrheniusBM(A=(1.75475e-11,'m^3/(mol*s)'), n=4.0597, w0=(907250,'J/mol'), E0=(146666,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.193484162227714, var=73.27695532230449, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct',), comment="""BM rule fitted to 2 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
            Total Standard Deviation in ln(k): 32.72244315846819"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
Total Standard Deviation in ln(k): 32.72244315846819""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
Total Standard Deviation in ln(k): 32.72244315846819
sensitivities = [{'dA': 0.7192593669245977, 'dE0': 0.0056325432968387865, 'dn': -0.017568014561463202, 'dA_dEa': -10.425755773583216, 'dE0_dEa': -0.07271495774130116, 'dn_dEa': 0.25876891542753344, 'name': 'C3H4-2 + C4H6 <=> C7H10-3'}, {'dA': 0.44539152440142193, 'dE0': -0.004319040748654189, 'dn': 0.013469351546405203, 'dA_dEa': 14.532007317741781, 'dE0_dEa': 0.9357465774165338, 'dn_dEa': -0.357472311730295, 'name': 'C4H6 + C2H4O <=> C6H10O-2'}]
""",
)

entry(
    index = 8,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(5.38143e-07,'m^3/(mol*s)'), n=2.90426, w0=(858000,'J/mol'), E0=(147287,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22625272160794474, var=7.109026128865732, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R',), comment="""BM rule fitted to 8 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R
            Total Standard Deviation in ln(k): 5.913650604377937"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R
Total Standard Deviation in ln(k): 5.913650604377937""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R
Total Standard Deviation in ln(k): 5.913650604377937
sensitivities = [{'dA': 0.5765598772403204, 'dE0': 0.003971823465113899, 'dn': -0.021554621823909614, 'dA_dEa': -6.826827314493442, 'dE0_dEa': 0.010832809806698495, 'dn_dEa': 0.2970188381211873, 'name': 'C2H4 + C6H10-2 <=> C8H14'}, {'dA': 0.41586364476313836, 'dE0': 0.002686251554108649, 'dn': -0.014574286004850804, 'dA_dEa': -4.812597813480399, 'dE0_dEa': 0.028455047133066673, 'dn_dEa': 0.209535581068252, 'name': 'C3H6 + C6H10-2 <=> C9H16'}, {'dA': 0.41586364475958565, 'dE0': 0.002686251554108649, 'dn': -0.014574286004695569, 'dA_dEa': -4.814488774683132, 'dE0_dEa': 0.02844117924188468, 'dn_dEa': 0.20961855893259299, 'name': 'C3H6-2 + C6H10-2 <=> C9H16-2'}, {'dA': 0.018660644936831894, 'dE0': -0.0004917274112673155, 'dn': 0.0026792142795273944, 'dA_dEa': 1.1783075400019403, 'dE0_dEa': 0.059891839877558965, 'dn_dEa': -0.05081510778354641, 'name': 'C4H6-2 + C6H10-2 <=> C10H16'}, {'dA': 0.018660645187298208, 'dE0': -0.0004917274094426693, 'dn': 0.0026792142685057333, 'dA_dEa': 1.1770815357225093, 'dE0_dEa': 0.059883228455872274, 'dn_dEa': -0.050761045804889396, 'name': 'C4H6-3 + C6H10-2 <=> C10H16-2'}, {'dA': -0.12442181291839864, 'dE0': -0.0016362922961437648, 'dn': 0.008894507050119549, 'dA_dEa': 2.199157666775051, 'dE0_dEa': 0.059561470205902786, 'dn_dEa': -0.0952197326404551, 'name': 'C5H8 + C6H10-2 <=> C11H18'}, {'dA': -0.124421812920175, 'dE0': -0.0016362922963465032, 'dn': 0.008894507050274782, 'dA_dEa': 2.199157666775051, 'dE0_dEa': 0.059561470205902786, 'dn_dEa': -0.09521973264061033, 'name': 'C5H8-2 + C6H10-2 <=> C11H18-2'}, {'dA': 0.12685741737429598, 'dE0': -0.002485337662387756, 'dn': 0.013482895753340617, 'dA_dEa': 8.583333802390904, 'dE0_dEa': 0.3759320769455022, 'dn_dEa': -0.37060055782087215, 'name': 'C4H6O + C2H4 <=> C6H10O'}]
""",
)

entry(
    index = 9,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R",
    kinetics = ArrheniusBM(A=(0.446605,'m^3/(mol*s)'), n=1.06441, w0=(858000,'J/mol'), E0=(139969,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2479418310823012, var=3.746729545052508, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R',), comment="""BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R
            Total Standard Deviation in ln(k): 7.015991799694358"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R
Total Standard Deviation in ln(k): 7.015991799694358""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R
Total Standard Deviation in ln(k): 7.015991799694358
sensitivities = [{'dA': 0.506300122413317, 'dE0': 0.003782847541856879, 'dn': -0.04689789633160755, 'dA_dEa': -7.419705833775421, 'dE0_dEa': -0.005134323320513325, 'dn_dEa': 0.778617778558374, 'name': 'C2H4 + C5H8-4 <=> C7H12-2'}, {'dA': 0.47878749798551945, 'dE0': -0.003903559920705113, 'dn': 0.04841001426836561, 'dA_dEa': 3.7425233398897486, 'dE0_dEa': 0.6133325890084065, 'dn_dEa': -0.3818986283430345, 'name': 'C4H6-2 + C5H8-4 <=> C9H14-4'}]
""",
)

entry(
    index = 10,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    kinetics = ArrheniusBM(A=(2.15883,'m^3/(mol*s)'), n=0.926526, w0=(858000,'J/mol'), E0=(155877,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.018010594753247997, var=0.625832289615524, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R',), comment="""BM rule fitted to 3 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
            Total Standard Deviation in ln(k): 1.6311899018279374"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 1.6311899018279374""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 1.6311899018279374
sensitivities = [{'dA': 0.7160349530067289, 'dE0': 0.002853083773014554, 'dn': -0.04363650662689429, 'dA_dEa': -5.189813076709865, 'dE0_dEa': 0.19890231472437325, 'dn_dEa': 0.5959750580832236, 'name': 'C4H6-2 + C4H6 <=> C8H12'}, {'dA': 0.149889685535992, 'dE0': -0.001369818702690437, 'dn': 0.020881308581720024, 'dA_dEa': 1.2870204880466614, 'dE0_dEa': 0.2240681829780181, 'dn_dEa': -0.14257525457385567, 'name': 'C5H8 + C4H6 <=> C9H14'}, {'dA': 0.14988968553665813, 'dE0': -0.0013698187025007222, 'dn': 0.020881308581720024, 'dA_dEa': 1.2904318389968283, 'dE0_dEa': 0.22409174845594462, 'dn_dEa': -0.14296743193629766, 'name': 'C5H8-2 + C4H6 <=> C9H14-2'}]
""",
)

entry(
    index = 11,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R",
    kinetics = ArrheniusBM(A=(0.446605,'m^3/(mol*s)'), n=1.06441, w0=(858000,'J/mol'), E0=(139969,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2479418310823012, var=3.746729545052508, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R',), comment="""BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R
            Total Standard Deviation in ln(k): 7.015991799694358"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R
Total Standard Deviation in ln(k): 7.015991799694358""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R
Total Standard Deviation in ln(k): 7.015991799694358
sensitivities = [{'dA': 0.506300122413317, 'dE0': 0.003782847541856879, 'dn': -0.04689789633160755, 'dA_dEa': -7.419705833775421, 'dE0_dEa': -0.005134323320513325, 'dn_dEa': 0.778617778558374, 'name': 'C5H8-3 + C2H4 <=> C7H12'}, {'dA': 0.47878749798551945, 'dE0': -0.003903559920705113, 'dn': 0.04841001426836561, 'dA_dEa': 3.7425233398897486, 'dE0_dEa': 0.6133325890084065, 'dn_dEa': -0.3818986283430345, 'name': 'C4H6-3 + C5H8-3 <=> C9H14-3'}]
""",
)

entry(
    index = 12,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R",
    kinetics = ArrheniusBM(A=(8910,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(167318,'J/mol'), Tmin=(464,'K'), Tmax=(557,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.6432663222326738, 'dn_dEa': nan, 'name': 'C4H6-3 + C4H6 <=> C8H12-2'}]
""",
)

entry(
    index = 13,
    label = "Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_5COCdd->Cdd",
    kinetics = ArrheniusBM(A=(1.77e-07,'m^3/(mol*s)'), n=2.94, w0=(858000,'J/mol'), E0=(211660,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_5COCdd->Cdd',), comment="""BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_5COCdd->Cdd
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_5COCdd->Cdd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_5COCdd->Cdd
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.608946213992975, 'dn_dEa': 0.0, 'name': 'C3H4-2 + C4H6 <=> C7H10-3'}]
""",
)

entry(
    index = 14,
    label = "Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_N-5COCdd->Cdd",
    kinetics = ArrheniusBM(A=(2.74773e-08,'m^3/(mol*s)'), n=3.0576, w0=(956500,'J/mol'), E0=(149441,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_N-5COCdd->Cdd',), comment="""BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_N-5COCdd->Cdd
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_N-5COCdd->Cdd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_N-5COCdd->Cdd
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.7720966814258813, 'dn_dEa': 0.0, 'name': 'C4H6 + C2H4O <=> C6H10O-2'}]
""",
)

entry(
    index = 15,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R",
    kinetics = ArrheniusBM(A=(0.000165533,'m^3/(mol*s)'), n=2.05774, w0=(858000,'J/mol'), E0=(131083,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10166403055099561, var=13.658259824244146, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R',), comment="""BM rule fitted to 4 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R
            Total Standard Deviation in ln(k): 7.664353323599815"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R
Total Standard Deviation in ln(k): 7.664353323599815""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R
Total Standard Deviation in ln(k): 7.664353323599815
sensitivities = [{'dA': 3.1982904286852656, 'dE0': 0.02652951845076616, 'dn': -0.17016694199217738, 'dA_dEa': -19.27050629158379, 'dE0_dEa': 0.06089269095191054, 'dn_dEa': 1.1157104109726572, 'name': 'C3H6-2 + C6H10-2 <=> C9H16-2'}, {'dA': 1.4424670965171227, 'dE0': 0.010735806850733819, 'dn': -0.06882599039556432, 'dA_dEa': 5.795154812285403, 'dE0_dEa': 0.22871365292716428, 'dn_dEa': -0.33181590839079733, 'name': 'C4H6-3 + C6H10-2 <=> C10H16-2'}, {'dA': 0.814912678389935, 'dE0': 0.005089264071322952, 'dn': -0.03260673072891484, 'dA_dEa': 10.098497593447721, 'dE0_dEa': 0.237700396869785, 'dn_dEa': -0.5806266990028901, 'name': 'C5H8 + C6H10-2 <=> C11H18'}, {'dA': 0.8150398967022642, 'dE0': 0.005088817405497983, 'dn': -0.03261533844010019, 'dA_dEa': 10.096261936326957, 'dE0_dEa': 0.23768081088901843, 'dn_dEa': -0.5804972844551696, 'name': 'C5H8-2 + C6H10-2 <=> C11H18-2'}]
""",
)

entry(
    index = 16,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    kinetics = ArrheniusBM(A=(0.0106931,'m^3/(mol*s)'), n=1.53489, w0=(858000,'J/mol'), E0=(153249,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01820808251533475, var=28.348068215283774, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R',), comment="""BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
            Total Standard Deviation in ln(k): 10.719540669073005"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 10.719540669073005""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 10.719540669073005
sensitivities = [{'dA': 1.9665112838131937, 'dE0': 0.01109424099424698, 'dn': -0.1100726930192705, 'dA_dEa': -15.266629803177961, 'dE0_dEa': 0.2785533102911058, 'dn_dEa': 1.1525192706108067, 'name': 'C3H6 + C6H10-2 <=> C9H16'}, {'dA': -0.4512515075676901, 'dE0': -0.0071997139362765935, 'dn': 0.0713597514042971, 'dA_dEa': 16.124782308418517, 'dE0_dEa': 0.41902190669600936, 'dn_dEa': -1.2048029205430337, 'name': 'C4H6-2 + C6H10-2 <=> C10H16'}]
""",
)

entry(
    index = 17,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-4Cd-R",
    kinetics = ArrheniusBM(A=(4570,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(176716,'J/mol'), Tmin=(450,'K'), Tmax=(592,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-4Cd-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-4Cd-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-4Cd-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-4Cd-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.6479269364886524, 'dn_dEa': nan, 'name': 'C2H4 + C6H10-2 <=> C8H14'}]
""",
)

entry(
    index = 18,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    kinetics = ArrheniusBM(A=(1020,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(142478,'J/mol'), Tmin=(492,'K'), Tmax=(606,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.5907652510936465, 'dn_dEa': nan, 'name': 'C4H6-2 + C5H8-4 <=> C9H14-4'}]
""",
)

entry(
    index = 19,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-5Cd-R",
    kinetics = ArrheniusBM(A=(0.562362,'m^3/(mol*s)'), n=0.999299, w0=(858000,'J/mol'), E0=(151136,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-8.770761894538775e-15, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-5Cd-R',), comment="""BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-5Cd-R
            Total Standard Deviation in ln(k): 2.203709018728335e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-5Cd-R
Total Standard Deviation in ln(k): 2.203709018728335e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-5Cd-R
Total Standard Deviation in ln(k): 2.203709018728335e-14
sensitivities = [{'dA': 0.49977854661659116, 'dE0': 1.9633342472892941e-07, 'dn': -3.167027558766264e-06, 'dA_dEa': -0.8544332745564596, 'dE0_dEa': 0.32509215347603543, 'dn_dEa': 0.10072275573150369, 'name': 'C5H8 + C4H6 <=> C9H14'}, {'dA': 0.49976911224486287, 'dE0': 1.2778204991754608e-07, 'dn': -2.118353706724871e-06, 'dA_dEa': -0.8544402109561364, 'dE0_dEa': 0.32509210463051386, 'dn_dEa': 0.10072352782612409, 'name': 'C5H8-2 + C4H6 <=> C9H14-2'}]
""",
)

entry(
    index = 20,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R_Ext-5Cd-R",
    kinetics = ArrheniusBM(A=(1020,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(142478,'J/mol'), Tmin=(492,'K'), Tmax=(606,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R_Ext-5Cd-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R_Ext-5Cd-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R_Ext-5Cd-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R_Ext-5Cd-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.5907652510936465, 'dn_dEa': nan, 'name': 'C4H6-3 + C5H8-3 <=> C9H14-3'}]
""",
)

entry(
    index = 21,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    kinetics = ArrheniusBM(A=(0.492357,'m^3/(mol*s)'), n=1.06989, w0=(858000,'J/mol'), E0=(122997,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3988810110276873e-14, var=4.978412222288914e-60, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R',), comment="""BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
            Total Standard Deviation in ln(k): 3.514776409617305e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 3.514776409617305e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 3.514776409617305e-14
sensitivities = [{'dA': 0.49987545153024016, 'dE0': 1.0878246983690984e-06, 'dn': -1.4694153553795327e-05, 'dA_dEa': -0.7915185890723136, 'dE0_dEa': 0.3037952368425949, 'dn_dEa': 0.10138977601712673, 'name': 'C5H8 + C6H10-2 <=> C11H18'}, {'dA': 0.4998754515363464, 'dE0': 1.0878248166806789e-06, 'dn': -1.4694154176412007e-05, 'dA_dEa': -0.7915854508301107, 'dE0_dEa': 0.30379464643456366, 'dn_dEa': 0.10139760255471639, 'name': 'C5H8-2 + C6H10-2 <=> C11H18-2'}]
""",
)

entry(
    index = 22,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1020,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(143715,'J/mol'), Tmin=(379,'K'), Tmax=(581,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-8R!H-R
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
    index = 23,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1020,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(143715,'J/mol'), Tmin=(379,'K'), Tmax=(581,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.6203506326644614, 'dn_dEa': nan, 'name': 'C4H6-2 + C6H10-2 <=> C10H16'}]
""",
)

entry(
    index = 24,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-5Cd-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(899,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(155169,'J/mol'), Tmin=(515,'K'), Tmax=(572,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-5Cd-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-5Cd-R_Ext-7R!H-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-5Cd-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-5Cd-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.6295845433903577, 'dn_dEa': nan, 'name': 'C5H8 + C4H6 <=> C9H14'}]
""",
)

entry(
    index = 25,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1260,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(127005,'J/mol'), Tmin=(352,'K'), Tmax=(423,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.5913845582405394, 'dn_dEa': nan, 'name': 'C5H8-2 + C6H10-2 <=> C11H18-2'}]
""",
)

