#!/usr/bin/env python
# encoding: utf-8

name = "LithiumPrimaryChargedKinetics"
shortDesc = ""
longDesc = """

"""
autoGenerated=False
entry(
    index = 0,
    label = "[Lip] + N=C <=> [Li]N[CH2]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(16042,'m^3/(mol*s)'), n=1.52384, Ea=(2.76381,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-2.65419313965326,B=1.2542197583042969,E=-0.21990942778263972,L=-9.14111680402368,A=3.645314481406821,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.04604, dn = +|- 0.00586241, dEa = +|- 0.0335255 kJ/mol"""),
)

entry(
    index = 1,
    label = "[Li]OC(=O)OC[CH2] + [Lip] <=> C=C + [Li]OC(=O)O[Li]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(2.23949e+06,'cm^3/(mol*s)'), n=2.34337, Ea=(16.2698,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-1.3791416734787092,B=0.9825775784337702,E=1.344561385839825,L=1.6867692078977448,A=2.9918711355986547,comment='')),
)

entry(
    index = 2,
    label = "N#CCC[CH2] + [Lip] <=> C=C + [Li]N=C=C",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(162517,'cm^3/(mol*s)'), n=2.55635, Ea=(59.4607,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
)

entry(
    index = 3,
    label = "O=COC[CH2] + [Lip] <=> C=C + [Li]OC=O",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(419384,'cm^3/(mol*s)'), n=2.21898, Ea=(48.2832,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.0247091484586592,B=2.5777645372278832,E=0.3431344611927818,L=9.346538089381045,A=0.8860009592023523,comment='')),
)

entry(
    index = 4,
    label = "O=CCC[O] + [Lip] <=> C=O + [Li]OC=C",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(1.74272e+07,'cm^3/(mol*s)'), n=2.05933, Ea=(-27.3358,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=3.2490249849978214,B=2.6960753668589854,E=2.1706425235190108,L=14.985510873166351,A=0.7334126588566799,comment='')),
)

entry(
    index = 5,
    label = "N=CCN[CH2] + [Lip] <=> N=C + [Li]NC=C",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(2.45437e+09,'cm^3/(mol*s)'), n=0.869935, Ea=(-36.817,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
)

entry(
    index = 6,
    label = "[Lip] + C=O <=> [Li]O[CH2]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(500060,'m^3/(mol*s)'), n=1.50675, Ea=(-0.985354,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-0.4735938637413528,B=2.67486764340657,E=-5.09678040094995,L=-4.876934525239067,A=3.9944267641274602,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.03252, dn = +|- 0.00416775, dEa = +|- 0.0238342 kJ/mol"""),
)

entry(
    index = 7,
    label = "[Lip] + COCC <=> [Li]OC + C[CH2]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(0.000236033,'m^3/(mol*s)'), n=3.84908, Ea=(56.4483,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07254, dn = +|- 0.00912116, dEa = +|- 0.0521614 kJ/mol"""),
)

entry(
    index = 8,
    label = "[Lip] + CNC <=> [Li]NC + [CH3]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(5.84081,'m^3/(mol*s)'), n=2.5402, Ea=(97.8358,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=5.9720845035693655,B=-11.11835148496454,E=1.2672065293713617,L=34.51723438776737,A=-10.461680798130194,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.31573, dn = +|- 0.0357396, dEa = +|- 0.204385 kJ/mol"""),
)

entry(
    index = 9,
    label = "[Lip] + CNC <=> [Li]N(C)C + [H]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(0.0200172,'m^3/(mol*s)'), n=2.76621, Ea=(72.0709,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.996332219215656,B=1.029302623121347,E=1.007550487792502,L=7.3685642232941575,A=0.4814345945968402,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.20383, dn = +|- 0.024163, dEa = +|- 0.138181 kJ/mol"""),
)

entry(
    index = 10,
    label = "[Lip] + CNCC <=> [Li]NC + C[CH2]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(117.529,'m^3/(mol*s)'), n=2.07905, Ea=(110.968,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=0.9175438008860265,B=1.1395826064596657,E=0.4944811262263229,L=5.415263196320309,A=0.6943364764189893,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.06164, dn = +|- 0.00779066, dEa = +|- 0.0445526 kJ/mol"""),
)

entry(
    index = 11,
    label = "[Lip] + CNCC <=> [Li]NCC + [CH3]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(1.61257,'m^3/(mol*s)'), n=2.55041, Ea=(96.84,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.877486735996646,B=0.6916407047808263,E=0.748415650862252,L=5.385263016210897,A=0.5210754074032086,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.25373, dn = +|- 0.029453, dEa = +|- 0.168434 kJ/mol"""),
)

entry(
    index = 12,
    label = "[Lip] + CNCC <=> [Li]N(C)CC + [H]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(0.00331961,'m^3/(mol*s)'), n=3.0459, Ea=(70.8277,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.1131935806214712,B=1.1556454917670655,E=1.2169728270193971,L=7.839572648134702,A=0.31656236651087616,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.28575, dn = +|- 0.0327372, dEa = +|- 0.187215 kJ/mol"""),
)

entry(
    index = 13,
    label = "[Lip] + O <=> [Li]O + [H]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(2206.42,'m^3/(mol*s)'), n=1.35569, Ea=(48.8442,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.6576610150461983,B=2.4435784684265482,E=0.404796645816695,L=7.698368077501874,A=0.9750486732350473,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.12448, dn = +|- 0.0152811, dEa = +|- 0.0873886 kJ/mol"""),
)

entry(
    index = 14,
    label = "[Lip] + N <=> [Li]N + [H]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(1.86167,'m^3/(mol*s)'), n=2.44198, Ea=(87.1355,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.9471505265788214,B=1.7274624400621788,E=0.6115119617819315,L=6.871072605917964,A=0.6704069036466952,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.22038, dn = +|- 0.025941, dEa = +|- 0.148349 kJ/mol"""),
)

entry(
    index = 15,
    label = "[Lip] + CO <=> [Li]OC + [H]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(4.02602,'m^3/(mol*s)'), n=2.23116, Ea=(40.7702,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.4067121409688057,B=1.4628968939845368,E=0.9656443938025181,L=7.661570379273675,A=0.443175955652443,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.0796, dn = +|- 0.00997547, dEa = +|- 0.057047 kJ/mol"""),
)

entry(
    index = 16,
    label = "[Lip] + CO <=> [Li]O + [CH3]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(153.764,'m^3/(mol*s)'), n=2.01928, Ea=(47.7262,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.4173362998736376,B=2.357499252462657,E=0.5167298959343533,L=7.9017680525604375,A=1.0064038665607862,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.49606, dn = +|- 0.0524693, dEa = +|- 0.300058 kJ/mol"""),
)

entry(
    index = 17,
    label = "[Lip] + CN <=> [Li]NC + [H]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(0.0885541,'m^3/(mol*s)'), n=2.76407, Ea=(81.1221,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-5.4761368991675985,B=-6.829449919467144,E=14.43663245128814,L=28.957970295010895,A=0.4259943743771139,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.19079, dn = +|- 0.0227446, dEa = +|- 0.13007 kJ/mol"""),
)

entry(
    index = 18,
    label = "[Lip] + CCO <=> [Li]O + C[CH2]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(0.609636,'m^3/(mol*s)'), n=2.90468, Ea=(55.2021,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.9913576154323054,B=3.1755887609180435,E=-0.2623364392566645,L=7.244831699370673,A=0.5572363451823703,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.27825, dn = +|- 0.0319751, dEa = +|- 0.182857 kJ/mol"""),
)

entry(
    index = 19,
    label = "[Lip] + CCO <=> [Li]OCC + [H]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(3.88747,'m^3/(mol*s)'), n=2.22783, Ea=(40.8372,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-8.623486006056842,B=14.917486429580572,E=-5.719694357458241,L=40.120001635540106,A=-6.502228345652631,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.09972, dn = +|- 0.0123813, dEa = +|- 0.0708054 kJ/mol"""),
)

entry(
    index = 20,
    label = "[Lip] + CCN <=> [Li]N + C[CH2]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(0.00130946,'m^3/(mol*s)'), n=3.2505, Ea=(88.6985,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.6195332200790409,B=2.120893670736446,E=10.142480436000628,L=-0.8781474558081529,A=3.410407959634951,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.25466, dn = +|- 0.0295493, dEa = +|- 0.168984 kJ/mol"""),
)

entry(
    index = 21,
    label = "[Lip] + COC <=> [Li]OC + [CH3]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(0.327198,'m^3/(mol*s)'), n=2.90093, Ea=(61.3447,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.223920620501668,B=0.8264175269682525,E=0.40415741933873844,L=5.605210034978575,A=0.4397271958947774,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.20785, dn = +|- 0.0245968, dEa = +|- 0.140662 kJ/mol"""),
)

entry(
    index = 22,
    label = "[Lip] + COCC <=> [Li]OCC + [CH3]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(0.137812,'m^3/(mol*s)'), n=2.70251, Ea=(63.027,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.091886494292463,B=0.5254418313743373,E=1.2963729646265112,L=5.721969023897385,A=0.6575614317431779,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.12328, dn = +|- 0.0151425, dEa = +|- 0.086596 kJ/mol"""),
)

entry(
    index = 23,
    label = "[Lip] + CN <=> [Li]N + [CH3]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(0.141645,'m^3/(mol*s)'), n=2.88935, Ea=(85.5741,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=0.8306578175990244,B=1.956506108230911,E=0.011774617070094268,L=6.100850860272114,A=1.0441801517777485,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.50683, dn = +|- 0.0534042, dEa = +|- 0.305404 kJ/mol"""),
)

entry(
    index = 24,
    label = "[Lip] + CCN <=> [Li]NCC + [H]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(0.00450332,'m^3/(mol*s)'), n=2.99604, Ea=(78.6799,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.9852422925798727,B=1.2991389460904967,E=1.413033851489418,L=7.445245509701895,A=0.5371087291175491,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.17557, dn = +|- 0.0210685, dEa = +|- 0.120485 kJ/mol"""),
)

entry(
    index = 25,
    label = "[Lip] + C <=> [CH3] + [Li][H]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(0.67868,'m^3/(mol*s)'), n=3.09275, Ea=(215.149,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=3.39470212956669,B=1.6022203760198037,E=1.4946262264125265,L=10.49010693814182,A=0.4943151788298517,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.37586, dn = +|- 0.0415605, dEa = +|- 0.237673 kJ/mol"""),
)

entry(
    index = 26,
    label = "[Lip] + CF <=> [CH3] + [Li]F",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(329.871,'m^3/(mol*s)'), n=2.2276, Ea=(25.9849,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.8681935378213759,B=2.373498032935028,E=0.32859248603303737,L=5.004153890392606,A=0.8849787213003473,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.4013, dn = +|- 0.043947, dEa = +|- 0.251321 kJ/mol"""),
)

entry(
    index = 27,
    label = "[Lip] + CCl <=> [CH3] + [Li]Cl",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(4264.72,'m^3/(mol*s)'), n=1.78731, Ea=(-2.88557,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.40096476096442,B=0.7611537028291462,E=0.36695032193123533,L=5.182274882516309,A=0.578711830957878,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.33939, dn = +|- 0.0380613, dEa = +|- 0.217662 kJ/mol"""),
)

entry(
    index = 28,
    label = "[Lip] + OC[CH2] <=> [Li]O + C=C",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(32.4209,'m^3/(mol*s)'), n=1.65654, Ea=(57.4026,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.8538812901233412,B=2.675568430768142,E=-6.952996746174581,L=1.5707766756804364,A=-0.4046889575036062,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.06371, dn = +|- 0.00804458, dEa = +|- 0.0460048 kJ/mol"""),
)

entry(
    index = 29,
    label = "O=S(=O)(C)CC[CH2] + [Lip] <=> C=C + [Li]OS(=O)(=C)C",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(312580,'cm^3/(mol*s)'), n=2.72776, Ea=(68.0852,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
)

entry(
    index = 30,
    label = "CCOC(=O)OC[CH2] + [Lip] <=> C=C + [Li]OC(=O)OCC",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(9.5603e+07,'cm^3/(mol*s)'), n=1.70021, Ea=(38.7352,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.1943783976602214,B=0.894154843812189,E=5.394280864555017,L=8.956244842828797,A=0.23494209646668668,comment='')),
)

entry(
    index = 31,
    label = "[Lip] + O1CC1 <=> [Li]OC[CH2]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(885.706,'m^3/(mol*s)'), n=1.77542, Ea=(-0.0494826,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=0.9429002183123382,B=0.4142522035781646,E=0.9271382422782674,L=0.5080999191526422,A=1.2701035125702795,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.16129, dn = +|- 0.0194768, dEa = +|- 0.111383 kJ/mol"""),
)

entry(
    index = 32,
    label = "[Lip] + N1CCCC1 <=> [Li]NCCC[CH2]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(7.84401,'m^3/(mol*s)'), n=2.34419, Ea=(76.6884,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=0.7063184659079954,B=0.6546888841685338,E=1.4167685288377097,L=7.086460323740072,A=0.6763993010322846,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.4264, dn = +|- 0.0462593, dEa = +|- 0.264544 kJ/mol"""),
)

entry(
    index = 33,
    label = "[Lip] + O=C1OCCO1 <=> [Li]O[C]1OCCO1",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(303.68,'m^3/(mol*s)'), n=1.59181, Ea=(-29.6323,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-2.018725993417632,B=4.93569039446143,E=-4.315782362402726,L=-1.68464261284562,A=3.5698295734222367,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.03673, dn = +|- 0.0046983, dEa = +|- 0.0268683 kJ/mol"""),
)

entry(
    index = 34,
    label = "[Lip] + O1CCCCCC1 <=> [Li]OCCCCC[CH2]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(1.42961e+06,'m^3/(mol*s)'), n=0.521642, Ea=(61.8184,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.8745309700808286,B=0.6489379258617733,E=0.27349172242979114,L=6.280608540134562,A=0.35178208431790287,comment=''), comment="""Fitted to 50 data points; dA = *|/ 3.24532, dn = +|- 0.153333, dEa = +|- 0.876872 kJ/mol"""),
)

entry(
    index = 35,
    label = "[Lip] + O1CCCC1 <=> [Li]OCCC[CH2]",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(1.83813e+10,'m^3/(mol*s)'), n=0.232048, Ea=(63.9513,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.975919765798433,B=0.5933221434562257,E=0.10249027371088437,L=4.734916369654065,A=0.4382337255257122,comment=''), comment="""Fitted to 50 data points; dA = *|/ 2.45172, dn = +|- 0.116808, dEa = +|- 0.667992 kJ/mol"""),
)