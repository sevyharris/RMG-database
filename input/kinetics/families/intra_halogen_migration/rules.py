#!/usr/bin/env python
# encoding: utf-8

name = "intra_halogen_migration/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(6038.41,'s^-1'), n=2.50417, w0=(416556,'J/mol'), E0=(163532,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03133558275859258, var=66.16490804632078, Tref=1000.0, N=18, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 18 training reactions at node Root
        Total Standard Deviation in ln(k): 16.385611521472462"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root
Total Standard Deviation in ln(k): 16.385611521472462""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root
Total Standard Deviation in ln(k): 16.385611521472462
sensitivities = [{'dA': 0.24635333010894428, 'dE0': 0.0014058757691048848, 'dn': -0.01372424720152883, 'dA_dEa': -4.287884278932925, 'dE0_dEa': 0.002070327564712686, 'dn_dEa': 0.27634713716111114, 'name': 'C3HF4O <=> C3HF4O-2'}, {'dA': 0.12250799398573448, 'dE0': 0.0005893455142957015, 'dn': -0.005744879686368847, 'dA_dEa': -2.4973162426873947, 'dE0_dEa': 0.0268300474691966, 'dn_dEa': 0.16095384289239167, 'name': 'C4H6F3 <=> C4H6F3-2'}, {'dA': 0.2627972761768694, 'dE0': 0.0015138979807067196, 'dn': -0.014784211653280336, 'dA_dEa': -3.579932963579008, 'dE0_dEa': 0.0015080266175645101, 'dn_dEa': 0.23072170054116467, 'name': 'C2H2F3 <=> C2H2F3-2'}, {'dA': -0.021475664134131968, 'dE0': -0.0003563549323487277, 'dn': 0.0035363541603776797, 'dA_dEa': 0.9630550633233875, 'dE0_dEa': 0.04112178226202258, 'dn_dEa': -0.06205493204226089, 'name': 'C3H6Cl <=> C3H6Cl-2'}, {'dA': -0.02115148262760391, 'dE0': -0.00035463934577682115, 'dn': 0.00351492787381282, 'dA_dEa': 1.2825566702706928, 'dE0_dEa': 0.055102686758781695, 'dn_dEa': -0.0826558177293902, 'name': 'C3H6F <=> C3H6F-2'}, {'dA': -0.021619449650958238, 'dE0': -0.0003572450655515766, 'dn': 0.00354568407232191, 'dA_dEa': 0.8858865900799183, 'dE0_dEa': 0.0378545311538163, 'dn_dEa': -0.05708206726814494, 'name': 'C4H8Cl <=> C4H8Cl-2'}, {'dA': -0.02097071963014461, 'dE0': -0.00035332047411711743, 'dn': 0.00350345911004088, 'dA_dEa': 0.6889307103677614, 'dE0_dEa': 0.02948845119138875, 'dn_dEa': -0.044390416497580104, 'name': 'C4H8Br <=> C4H8Br-2'}, {'dA': -0.02118009993346226, 'dE0': -0.0003545872530259697, 'dn': 0.0035170934022366123, 'dA_dEa': 0.7670075410076428, 'dE0_dEa': 0.032806759009505526, 'dn_dEa': -0.0494216020262101, 'name': 'C2H4F <=> C2H4F-2'}, {'dA': 0.0021188573917643285, 'dE0': -0.00021317743420127473, 'dn': 0.002001472191278004, 'dA_dEa': 0.281165559734151, 'dE0_dEa': 0.011534524914528102, 'dn_dEa': -0.018124783213135223, 'name': 'C2H4Cl <=> C2H4Cl-2'}, {'dA': -0.020903623086712203, 'dE0': -0.00035292717060059995, 'dn': 0.0034990788371609552, 'dA_dEa': 0.7625599363639552, 'dE0_dEa': 0.03262066079297453, 'dn_dEa': -0.04913498954238246, 'name': 'C3H6Br <=> C3H6Br-2'}, {'dA': -0.02139763807740516, 'dE0': -0.00035574772532942034, 'dn': 0.0035314516954467676, 'dA_dEa': 1.1418927498124822, 'dE0_dEa': 0.04898495841694854, 'dn_dEa': -0.07359131020834554, 'name': 'C4H8F <=> C4H8F-2'}, {'dA': -0.021384113406244378, 'dE0': -0.0003558139847047224, 'dn': 0.003530381719582997, 'dA_dEa': 1.1893889301096894, 'dE0_dEa': 0.05070980920323713, 'dn_dEa': -0.07664013581563615, 'name': 'C2F5 <=> C2F5-2'}, {'dA': -0.021487902024832785, 'dE0': -0.00035644163190478873, 'dn': 0.003537133391912255, 'dA_dEa': 0.7804323651968452, 'dE0_dEa': 0.033386690616277324, 'dn_dEa': -0.050286502238879004, 'name': 'C5H10Br <=> C5H10Br-2'}, {'dA': -0.02211419496056765, 'dE0': -0.00036024830303533296, 'dn': 0.00357786095914069, 'dA_dEa': 0.6697122902342327, 'dE0_dEa': 0.028697041325779684, 'dn_dEa': -0.04315157526235857, 'name': 'C5H10Cl <=> C5H10Cl-2'}, {'dA': -0.021125252290590365, 'dE0': -0.00035413294533941884, 'dn': 0.0035136844993844856, 'dA_dEa': 1.1327622135263309, 'dE0_dEa': 0.04807969485448697, 'dn_dEa': -0.07301060892723339, 'name': 'C5H10F <=> C5H10F-2'}, {'dA': 0.24612565146678247, 'dE0': 0.001404478602006391, 'dn': -0.013709459073697377, 'dA_dEa': -6.7283869982358215, 'dE0_dEa': 0.0033679574236641255, 'dn_dEa': 0.43361995380453516, 'name': 'O=C[C](F)C(F)(F)F <=> O=CC(F)(F)[C](F)F'}, {'dA': 0.12048413352518045, 'dE0': 0.0005773301045798661, 'dn': -0.00561287328487697, 'dA_dEa': -3.1351354916718934, 'dE0_dEa': 0.033769312380724725, 'dn_dEa': 0.20204729239753982, 'name': '[CH2]CCC(F)(F)F <=> FCCC[C](F)F'}, {'dA': 0.2631306985066152, 'dE0': 0.0015160188281670584, 'dn': -0.014805779748950759, 'dA_dEa': -5.759968848061371, 'dE0_dEa': 0.0026059537438955904, 'dn_dEa': 0.3712057328858236, 'name': '[CH2]C(F)(F)F <=> FC[C](F)F'}, {'dA': -0.02163330165494653, 'dE0': -0.00035730814621557315, 'dn': 0.0035466119126982983, 'dA_dEa': 0.9627863478770488, 'dE0_dEa': 0.041120158499416255, 'dn_dEa': -0.062037442341473, 'name': '[CH2]CCCl <=> [CH2]CCCl'}, {'dA': -0.01900229886509162, 'dE0': -0.000341550900444864, 'dn': 0.0033751804687284287, 'dA_dEa': 1.2858561121424112, 'dE0_dEa': 0.05512230969579039, 'dn_dEa': -0.08287107658619323, 'name': '[CH2]CCF <=> [CH2]CCF'}, {'dA': -0.02128032404691517, 'dE0': -0.00035516112372533173, 'dn': 0.0035236587231972263, 'dA_dEa': 0.885908525747423, 'dE0_dEa': 0.03785466956051666, 'dn_dEa': -0.05708348704493162, 'name': '[CH2]CCCCl <=> [CH2]CCCCl'}, {'dA': -0.02247290033530439, 'dE0': -0.0003624261512096117, 'dn': 0.003601191483861814, 'dA_dEa': 0.6884104808798289, 'dE0_dEa': 0.02948537628443942, 'dn_dEa': -0.044356467196359, 'name': '[CH2]CCCBr <=> [CH2]CCCBr'}, {'dA': -0.022127635919136017, 'dE0': -0.0003603294936459503, 'dn': 0.003578738963152273, 'dA_dEa': 0.7673034728875329, 'dE0_dEa': 0.03280856921528904, 'dn_dEa': -0.049440827891282534, 'name': '[CH2]CF <=> [CH2]CF'}, {'dA': -0.019080532965178747, 'dE0': -0.00034224884652099205, 'dn': 0.0033800116072712828, 'dA_dEa': 0.2653230460812076, 'dE0_dEa': 0.011437478106966263, 'dn_dEa': -0.01709544003539657, 'name': '[CH2]CCl <=> [CH2]CCl'}, {'dA': -0.023393990060685346, 'dE0': -0.00036800350479030086, 'dn': 0.0036611365231587274, 'dA_dEa': 0.7616681670140353, 'dE0_dEa': 0.032615364711448394, 'dn_dEa': -0.04907682303720448, 'name': '[CH2]CCBr <=> [CH2]CCBr'}, {'dA': -0.02041262841601335, 'dE0': -0.0003499188433244737, 'dn': 0.003467195130804595, 'dA_dEa': 1.1340051447633752, 'dE0_dEa': 0.04893582579755036, 'dn_dEa': -0.07307969186694592, 'name': '[CH2]CCCF <=> [CH2]CCCF'}, {'dA': -0.021431380242023096, 'dE0': -0.00035607525553831265, 'dn': 0.0035334859274107084, 'dA_dEa': 1.1893125799852444, 'dE0_dEa': 0.050709356785932726, 'dn_dEa': -0.07663515874508843, 'name': 'F[C](F)C(F)(F)F <=> F[C](F)C(F)(F)F'}, {'dA': -0.021313258134372366, 'dE0': -0.0003553722790899822, 'dn': 0.00352578582711949, 'dA_dEa': 0.7804701048695655, 'dE0_dEa': 0.03338691946868089, 'dn_dEa': -0.05028895553681926, 'name': '[CH2]CCCCBr <=> [CH2]CCCCBr'}, {'dA': -0.02123671991327803, 'dE0': -0.0003548883210967023, 'dn': 0.0035208425479005038, 'dA_dEa': 0.6699597620426118, 'dE0_dEa': 0.028698601886561967, 'dn_dEa': -0.04316758517741659, 'name': '[CH2]CCCCCl <=> [CH2]CCCCCl'}, {'dA': -0.021208453091505878, 'dE0': -0.0003547706866519719, 'dn': 0.0035189277858281203, 'dA_dEa': 1.1262093970360174, 'dE0_dEa': 0.04805344178217197, 'dn_dEa': -0.0725685764526746, 'name': '[CH2]CCCCF <=> [CH2]CCCCF'}]
""",
)

entry(
    index = 2,
    label = "F",
    kinetics = ArrheniusBM(A=(3.03181e+09,'s^-1'), n=0.874169, w0=(485000,'J/mol'), E0=(201592,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06358755078404826, var=61.63872441983877, Tref=1000.0, N=11, data_mean=0.0, correlation='F',), comment="""BM rule fitted to 11 training reactions at node F
        Total Standard Deviation in ln(k): 15.89900963505276"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node F
Total Standard Deviation in ln(k): 15.89900963505276""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node F
Total Standard Deviation in ln(k): 15.89900963505276
sensitivities = [{'dA': 0.07207626060790856, 'dE0': 3.150241496961038e-05, 'dn': -0.0009927445087871403, 'dA_dEa': -4.863674958664002, 'dE0_dEa': 0.020022455406962326, 'dn_dEa': 0.4801027131207973, 'name': 'C3HF4O <=> C3HF4O-2'}, {'dA': -0.08309564734433143, 'dE0': -0.000795222328540406, 'dn': 0.014321402466908736, 'dA_dEa': -2.55543800249242, 'dE0_dEa': 0.0519759738875712, 'dn_dEa': 0.25226784235218686, 'name': 'C4H6F3 <=> C4H6F3-2'}, {'dA': 0.09124311064568796, 'dE0': 0.00013397931453230515, 'dn': -0.002883551612764014, 'dA_dEa': -4.071913400072185, 'dE0_dEa': 0.016307045389381918, 'dn_dEa': 0.40191364432180626, 'name': 'C2H2F3 <=> C2H2F3-2'}, {'dA': -0.2625146717889782, 'dE0': -0.0017480613927152188, 'dn': 0.03203559705436548, 'dA_dEa': 2.007228202977495, 'dE0_dEa': 0.08140355661629284, 'dn_dEa': -0.1981476484145123, 'name': 'C3H6F <=> C3H6F-2'}, {'dA': -0.2619885200587935, 'dE0': -0.0017456916031334342, 'dn': 0.03198263662457608, 'dA_dEa': 1.0852364895087647, 'dE0_dEa': 0.04783600670474575, 'dn_dEa': -0.10713209500749706, 'name': 'C2H4F <=> C2H4F-2'}, {'dA': -0.2626186156718125, 'dE0': -0.0017485909382925252, 'dn': 0.03204590570472981, 'dA_dEa': 1.7446682052055495, 'dE0_dEa': 0.07214401503556161, 'dn_dEa': -0.17221547500222428, 'name': 'C4H8F <=> C4H8F-2'}, {'dA': -0.26182714342584784, 'dE0': -0.0017447728110592006, 'dn': 0.031966874682970256, 'dA_dEa': 1.820147102275827, 'dE0_dEa': 0.07466556448265486, 'dn_dEa': -0.17967817573082828, 'name': 'C2F5 <=> C2F5-2'}, {'dA': -0.2612604330814182, 'dE0': -0.001742009040197513, 'dn': 0.03191036513006161, 'dA_dEa': 1.6664104828729325, 'dE0_dEa': 0.07047385837124982, 'dn_dEa': -0.1644521258390335, 'name': 'C5H10F <=> C5H10F-2'}, {'dA': 0.06736417982367758, 'dE0': 8.527464210257764e-06, 'dn': -0.00052286401557387, 'dA_dEa': -7.488977045586979, 'dE0_dEa': 0.03237016222727027, 'dn_dEa': 0.7392368981581401, 'name': 'O=C[C](F)C(F)(F)F <=> O=CC(F)(F)[C](F)F'}, {'dA': -0.08562234876309081, 'dE0': -0.000807600261169337, 'dn': 0.014573256382929627, 'dA_dEa': -3.155090730942681, 'dE0_dEa': 0.06568506950653184, 'dn_dEa': 0.31146981510816946, 'name': '[CH2]CCC(F)(F)F <=> FCCC[C](F)F'}, {'dA': 0.09141514694733684, 'dE0': 0.00013481657819281945, 'dn': -0.0029006485516304406, 'dA_dEa': -6.451671066206188, 'dE0_dEa': 0.027072115984500825, 'dn_dEa': 0.6368282574763287, 'name': '[CH2]C(F)(F)F <=> FC[C](F)F'}, {'dA': -0.26113585905920933, 'dE0': -0.0017413863241293012, 'dn': 0.03189798188425653, 'dA_dEa': 1.9620729123774823, 'dE0_dEa': 0.08118037901831644, 'dn_dEa': -0.1936518680431612, 'name': '[CH2]CCF <=> [CH2]CCF'}, {'dA': -0.2631445870946726, 'dE0': -0.0017510828702266457, 'dn': 0.032098546999715837, 'dA_dEa': 1.089819801997414, 'dE0_dEa': 0.04786147473827054, 'dn_dEa': -0.10758191422740492, 'name': '[CH2]CF <=> [CH2]CF'}, {'dA': -0.26191751181062317, 'dE0': -0.0017452020502418634, 'dn': 0.0319759128600253, 'dA_dEa': 1.753254680284948, 'dE0_dEa': 0.07218649976941, 'dn_dEa': -0.17307033172733588, 'name': '[CH2]CCCF <=> [CH2]CCCF'}, {'dA': -0.2618313951714701, 'dE0': -0.0017447935303472712, 'dn': 0.03196729870140797, 'dA_dEa': 1.8015892421774136, 'dE0_dEa': 0.07457621044116776, 'dn_dEa': -0.1778250067269826, 'name': 'F[C](F)C(F)(F)F <=> F[C](F)C(F)(F)F'}, {'dA': -0.26163037946250295, 'dE0': -0.001743827919156866, 'dn': 0.031947214135072566, 'dA_dEa': 1.711297446625981, 'dE0_dEa': 0.0706882510462908, 'dn_dEa': -0.16893803867065277, 'name': '[CH2]CCCCF <=> [CH2]CCCCF'}]
""",
)

entry(
    index = 3,
    label = "Cl",
    kinetics = ArrheniusBM(A=(893.73,'s^-1'), n=2.71684, w0=(327000,'J/mol'), E0=(122883,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0008389315309072592, var=152.99185535827047, Tref=1000.0, N=4, data_mean=0.0, correlation='Cl',), comment="""BM rule fitted to 4 training reactions at node Cl
        Total Standard Deviation in ln(k): 24.798651271638853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Cl
Total Standard Deviation in ln(k): 24.798651271638853""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Cl
Total Standard Deviation in ln(k): 24.798651271638853
sensitivities = [{'dA': 0.09728007300237002, 'dE0': -0.00022379004640443904, 'dn': 0.0012773354145922792, 'dA_dEa': -0.027427182323516954, 'dE0_dEa': 0.1723391632925464, 'dn_dEa': 0.0012667090575714493, 'name': 'C3H6Cl <=> C3H6Cl-2'}, {'dA': 0.09738448272768004, 'dE0': -0.00022296748957582687, 'dn': 0.0012724951738243096, 'dA_dEa': -0.027900361557978447, 'dE0_dEa': 0.15864415694830564, 'dn_dEa': 0.0012885254837259996, 'name': 'C4H8Cl <=> C4H8Cl-2'}, {'dA': 0.07993366868054066, 'dE0': -0.00036435219911792107, 'dn': 0.002078275158400883, 'dA_dEa': -0.011004816161454092, 'dE0_dEa': 0.047987214911913045, 'dn_dEa': 0.0005087167577716629, 'name': 'C2H4Cl <=> C2H4Cl-2'}, {'dA': 0.09637800329543818, 'dE0': -0.00023067613236403016, 'dn': 0.0013192862010037562, 'dA_dEa': -0.01623609376899716, 'dE0_dEa': 0.12036217610855207, 'dn_dEa': 0.000750253627391141, 'name': 'C5H10Cl <=> C5H10Cl-2'}, {'dA': 0.09572265077651909, 'dE0': -0.0002363863806155143, 'dn': 0.0013492538077495943, 'dA_dEa': -0.02771703818904875, 'dE0_dEa': 0.17233674662410908, 'dn_dEa': 0.0012800427489367274, 'name': '[CH2]CCCl <=> [CH2]CCCl'}, {'dA': 0.0975365500188837, 'dE0': -0.00022174098317442471, 'dn': 0.0012654684369678747, 'dA_dEa': -0.027724865424797185, 'dE0_dEa': 0.15864562545118757, 'dn_dEa': 0.0012804491215645025, 'name': '[CH2]CCCCl <=> [CH2]CCCCl'}, {'dA': 0.09746774676068179, 'dE0': -0.0002225855023696924, 'dn': 0.001268467881490031, 'dA_dEa': 0.005138423736284491, 'dE0_dEa': 0.04811804860363228, 'dn_dEa': -0.00023673000940184065, 'name': '[CH2]CCl <=> [CH2]CCl'}, {'dA': 0.08362160316811396, 'dE0': -0.0003343617920156674, 'dn': 0.00190809242779951, 'dA_dEa': -0.040391169027214076, 'dE0_dEa': 0.12016551823586123, 'dn_dEa': 0.0018648570520866919, 'name': '[CH2]CCCCCl <=> [CH2]CCCCCl'}]
""",
)

entry(
    index = 4,
    label = "Br",
    kinetics = ArrheniusBM(A=(4.41068e+09,'s^-1'), n=0.61635, w0=(285000,'J/mol'), E0=(131360,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0008969427611604358, var=19.08034470564394, Tref=1000.0, N=3, data_mean=0.0, correlation='Br',), comment="""BM rule fitted to 3 training reactions at node Br
        Total Standard Deviation in ln(k): 8.759147723835769"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Br
Total Standard Deviation in ln(k): 8.759147723835769""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Br
Total Standard Deviation in ln(k): 8.759147723835769
sensitivities = [{'dA': 0.16083684793246172, 'dE0': -4.2676329082064e-05, 'dn': 0.0011727348301447584, 'dA_dEa': -0.005586622808807011, 'dE0_dEa': 0.15436524840794655, 'dn_dEa': 0.001140158859243304, 'name': 'C4H8Br <=> C4H8Br-2'}, {'dA': 0.15789853431160203, 'dE0': -6.448083862031002e-05, 'dn': 0.0017723667456982796, 'dA_dEa': -0.007060129565417905, 'dE0_dEa': 0.17073839120295925, 'dn_dEa': 0.0014408243673541125, 'name': 'C3H6Br <=> C3H6Br-2'}, {'dA': 0.15652723577732122, 'dE0': -7.499940237131231e-05, 'dn': 0.0020511727950812977, 'dA_dEa': -0.0041256287524054185, 'dE0_dEa': 0.17477178009145, 'dn_dEa': 0.000841817399709551, 'name': 'C5H10Br <=> C5H10Br-2'}, {'dA': 0.16125765098353284, 'dE0': -3.953707242934269e-05, 'dn': 0.001086903741951695, 'dA_dEa': -0.005502000178126461, 'dE0_dEa': 0.15436586466195726, 'dn_dEa': 0.0011228503097772378, 'name': '[CH2]CCCBr <=> [CH2]CCCBr'}, {'dA': 0.16303426868448787, 'dE0': -2.6379649155913678e-05, 'dn': 0.0007242104357159772, 'dA_dEa': -0.0057013541123757845, 'dE0_dEa': 0.17074851925370016, 'dn_dEa': 0.0011636848361814822, 'name': '[CH2]CCBr <=> [CH2]CCBr'}, {'dA': 0.16821961175141528, 'dE0': 1.2202554659941248e-05, 'dn': -0.000333664923971504, 'dA_dEa': -0.006469162734391178, 'dE0_dEa': 0.17475439995264938, 'dn_dEa': 0.0013202138339057595, 'name': '[CH2]CCCCBr <=> [CH2]CCCCBr'}]
""",
)

entry(
    index = 5,
    label = "R2F",
    kinetics = ArrheniusBM(A=(9.72231e+13,'s^-1'), n=-0.295801, w0=(485000,'J/mol'), E0=(173488,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0299576143045425, var=17.283834097384105, Tref=1000.0, N=6, data_mean=0.0, correlation='R2F',), comment="""BM rule fitted to 6 training reactions at node R2F
        Total Standard Deviation in ln(k): 8.409722084010028"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node R2F
Total Standard Deviation in ln(k): 8.409722084010028""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node R2F
Total Standard Deviation in ln(k): 8.409722084010028
sensitivities = [{'dA': 1.0505539683266554, 'dE0': 0.0056581262719119525, 'dn': 0.38587616236631656, 'dA_dEa': -7.775588085650899, 'dE0_dEa': 0.05791096962652877, 'dn_dEa': -3.2430212871191944, 'name': 'C3HF4O <=> C3HF4O-2'}, {'dA': 1.1001562528180178, 'dE0': 0.005960701872264596, 'dn': 0.40655995578181436, 'dA_dEa': -6.358465979219108, 'dE0_dEa': 0.04835972229871652, 'dn_dEa': -2.651697925474372, 'name': 'C2H2F3 <=> C2H2F3-2'}, {'dA': 0.23193286854452988, 'dE0': 0.0006645856514006103, 'dn': 0.04451627164910318, 'dA_dEa': 6.725466872418226, 'dE0_dEa': 0.13758771445962234, 'dn_dEa': 2.8038651305647555, 'name': 'C2H4F <=> C2H4F-2'}, {'dA': 0.24642095768004296, 'dE0': 0.000745763956003898, 'dn': 0.05061769761593337, 'dA_dEa': 10.163184308603643, 'dE0_dEa': 0.21114023655038103, 'dn_dEa': 4.237311701726277, 'name': 'C2F5 <=> C2F5-2'}, {'dA': 1.0493176163778362, 'dE0': 0.0056512007867387075, 'dn': 0.3853554663933553, 'dA_dEa': -12.389992216677058, 'dE0_dEa': 0.09009954225500492, 'dn_dEa': -5.166950016620222, 'name': 'O=C[C](F)C(F)(F)F <=> O=CC(F)(F)[C](F)F'}, {'dA': 1.1018755945572216, 'dE0': 0.005970341245125542, 'dn': 0.4072840035076454, 'dA_dEa': -10.590369457305572, 'dE0_dEa': 0.07627557785406584, 'dn_dEa': -4.416448301762424, 'name': '[CH2]C(F)(F)F <=> FC[C](F)F'}, {'dA': 0.22971412303720884, 'dE0': 0.0006521343019689868, 'dn': 0.04358204227507067, 'dA_dEa': 6.6210638757489635, 'dE0_dEa': 0.1370034523744395, 'dn_dEa': 2.7598910314783076, 'name': '[CH2]CF <=> [CH2]CF'}, {'dA': 0.23283130926190843, 'dE0': 0.0006696397079605707, 'dn': 0.044894552928084294, 'dA_dEa': 10.080776759680221, 'dE0_dEa': 0.21067778428350278, 'dn_dEa': 4.202612711922156, 'name': 'F[C](F)C(F)(F)F <=> F[C](F)C(F)(F)F'}]
""",
)

entry(
    index = 6,
    label = "R2Cl",
    kinetics = ArrheniusBM(A=(1.03108e+13,'s^-1'), n=-0.0707693, w0=(327000,'J/mol'), E0=(47264.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R2Cl',), comment="""BM rule fitted to 1 training reactions at node R2Cl
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R2Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R2Cl
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.49975016936448746, 'dE0': 1.9551776539289823e-11, 'dn': 1.7160622064403437e-09, 'dA_dEa': 2.5153212845910316e-08, 'dE0_dEa': 0.5000000005231462, 'dn_dEa': 4.466781870727852e-08, 'name': 'C2H4Cl <=> C2H4Cl-2'}, {'dA': 0.49975017325826165, 'dE0': 1.0068395162752397e-10, 'dn': 8.628747481177923e-09, 'dA_dEa': 1.5631940186723927e-09, 'dE0_dEa': 0.500000000033428, 'dn_dEa': 2.757347809936884e-09, 'name': '[CH2]CCl <=> [CH2]CCl'}]
""",
)

entry(
    index = 7,
    label = "R3F",
    kinetics = ArrheniusBM(A=(0.00930803,'s^-1'), n=4.16824, w0=(485000,'J/mol'), E0=(227637,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R3F',), comment="""BM rule fitted to 1 training reactions at node R3F
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R3F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R3F
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.4997500759032487, 'dE0': -4.032678893742233e-10, 'dn': 2.874694129938564e-09, 'dA_dEa': -7.296829807047182e-08, 'dE0_dEa': 0.4999999996845103, 'dn_dEa': 2.199009963751092e-09, 'name': 'C3H6F <=> C3H6F-2'}, {'dA': 0.49975007618924217, 'dE0': -4.019892974611788e-10, 'dn': 2.866170835505421e-09, 'dA_dEa': 1.30259358854815e-07, 'dE0_dEa': 0.5000000005672501, 'dn_dEa': -3.922633180493591e-09, 'name': '[CH2]CCF <=> [CH2]CCF'}]
""",
)

entry(
    index = 8,
    label = "R3Cl",
    kinetics = ArrheniusBM(A=(6.00221e+06,'s^-1'), n=1.90111, w0=(327000,'J/mol'), E0=(169648,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R3Cl',), comment="""BM rule fitted to 1 training reactions at node R3Cl
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R3Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R3Cl
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.4997501082702467, 'dE0': -2.2200376458240255e-10, 'dn': 4.21007718076701e-09, 'dA_dEa': 4.3156589413233836e-08, 'dE0_dEa': 0.5000000002534729, 'dn_dEa': -2.847636124515355e-09, 'name': 'C3H6Cl <=> C3H6Cl-2'}, {'dA': 0.4997501082809048, 'dE0': -2.2200376458240255e-10, 'dn': 4.209493194030512e-09, 'dA_dEa': -3.092814893080117e-08, 'dE0_dEa': 0.499999999817529, 'dn_dEa': 2.0398656705902416e-09, 'name': '[CH2]CCCl <=> [CH2]CCCl'}]
""",
)

entry(
    index = 9,
    label = "R3Br",
    kinetics = ArrheniusBM(A=(5.2885e+08,'s^-1'), n=1.30127, w0=(285000,'J/mol'), E0=(134618,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R3Br',), comment="""BM rule fitted to 1 training reactions at node R3Br
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R3Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R3Br
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.4997501641810782, 'dE0': 1.0810397840916595e-12, 'dn': -1.2627126395331261e-11, 'dA_dEa': 6.627551840666276e-07, 'dE0_dEa': 0.5000000056936191, 'dn_dEa': -6.856580823717829e-08, 'name': 'C3H6Br <=> C3H6Br-2'}, {'dA': 0.49975016440489917, 'dE0': 2.8107034386383145e-12, 'dn': -3.429800547921059e-11, 'dA_dEa': 8.08348943337567e-07, 'dE0_dEa': 0.5000000067590918, 'dn_dEa': -8.262150628361378e-08, 'name': '[CH2]CCBr <=> [CH2]CCBr'}]
""",
)

entry(
    index = 10,
    label = "R4F",
    kinetics = ArrheniusBM(A=(9.58733e-07,'s^-1'), n=5.29666, w0=(485000,'J/mol'), E0=(227349,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013351942602990101, var=1.2221974720133415, Tref=1000.0, N=3, data_mean=0.0, correlation='R4F',), comment="""BM rule fitted to 3 training reactions at node R4F
        Total Standard Deviation in ln(k): 2.2498431725504213"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node R4F
Total Standard Deviation in ln(k): 2.2498431725504213""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node R4F
Total Standard Deviation in ln(k): 2.2498431725504213
sensitivities = [{'dA': 0.5597163744877681, 'dE0': 0.001515210836428504, 'dn': -0.007035074660149068, 'dA_dEa': -8.203710477492814, 'dE0_dEa': 0.20085205296980252, 'dn_dEa': 0.18627697259801593, 'name': 'C4H6F3 <=> C4H6F3-2'}, {'dA': -0.0691492694766614, 'dE0': -0.0015577305137057479, 'dn': 0.0072449059727428934, 'dA_dEa': 7.93894108239089, 'dE0_dEa': 0.26981520597077546, 'dn_dEa': -0.1802822975318858, 'name': 'C4H8F <=> C4H8F-2'}, {'dA': 0.5600687902270258, 'dE0': 0.0015173905073714113, 'dn': -0.007042829657859511, 'dA_dEa': -10.317177412070748, 'dE0_dEa': 0.2526126490851144, 'dn_dEa': 0.2342661217984841, 'name': '[CH2]CCC(F)(F)F <=> FCCC[C](F)F'}, {'dA': -0.06909709497727384, 'dE0': -0.0015574985476975985, 'dn': 0.007243708185990375, 'dA_dEa': 7.936698819771756, 'dE0_dEa': 0.26980518069815523, 'dn_dEa': -0.1802308560349656, 'name': '[CH2]CCCF <=> [CH2]CCCF'}]
""",
)

entry(
    index = 11,
    label = "R4Cl",
    kinetics = ArrheniusBM(A=(2.50247e+07,'s^-1'), n=1.58353, w0=(327000,'J/mol'), E0=(156188,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R4Cl',), comment="""BM rule fitted to 1 training reactions at node R4Cl
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R4Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R4Cl
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.4997501907198494, 'dE0': 1.9529378634758595e-10, 'dn': -1.9436071743926124e-09, 'dA_dEa': -4.95397500799354e-07, 'dE0_dEa': 0.5000000009552232, 'dn_dEa': 4.584506734386522e-08, 'name': 'C4H8Cl <=> C4H8Cl-2'}, {'dA': 0.4997501911390696, 'dE0': 1.9790267280642774e-10, 'dn': -1.976699396682249e-09, 'dA_dEa': -4.86831908119765e-07, 'dE0_dEa': 0.5000000010156003, 'dn_dEa': 4.5176772719151614e-08, 'name': '[CH2]CCCCl <=> [CH2]CCCCl'}]
""",
)

entry(
    index = 12,
    label = "R4Br",
    kinetics = ArrheniusBM(A=(9.62119e+10,'s^-1'), n=0.157944, w0=(285000,'J/mol'), E0=(121704,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R4Br',), comment="""BM rule fitted to 1 training reactions at node R4Br
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R4Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R4Br
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.4997501775286235, 'dE0': 1.5712139415505996e-10, 'dn': -9.245883702070866e-09, 'dA_dEa': -1.4005507864568876e-06, 'dE0_dEa': 0.49999999142106394, 'dn_dEa': 1.171567725013284e-06, 'name': 'C4H8Br <=> C4H8Br-2'}, {'dA': 0.49975017326181437, 'dE0': 1.2268382831285503e-10, 'dn': -5.849364901112457e-09, 'dA_dEa': -1.6468568730944749e-06, 'dE0_dEa': 0.4999999894316967, 'dn_dEa': 1.3675349804478442e-06, 'name': '[CH2]CCCBr <=> [CH2]CCCBr'}]
""",
)

entry(
    index = 13,
    label = "R5nF",
    kinetics = ArrheniusBM(A=(1.64853e+07,'s^-1'), n=1.15307, w0=(485000,'J/mol'), E0=(198221,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R5nF',), comment="""BM rule fitted to 1 training reactions at node R5nF
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R5nF
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R5nF
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.4997502218096468, 'dE0': 3.1848185632942226e-10, 'dn': -5.541342287391414e-09, 'dA_dEa': -3.762323785850145e-08, 'dE0_dEa': 0.4999999983206709, 'dn_dEa': -2.6164240220596033e-09, 'name': 'C5H10F <=> C5H10F-2'}, {'dA': 0.4997502217634615, 'dE0': 3.181881893341899e-10, 'dn': -5.53652808259628e-09, 'dA_dEa': 4.037659095957214e-08, 'dE0_dEa': 0.49999999870875184, 'dn_dEa': -1.1113110349088076e-08, 'name': '[CH2]CCCCF <=> [CH2]CCCCF'}]
""",
)

entry(
    index = 14,
    label = "R5nCl",
    kinetics = ArrheniusBM(A=(4.11837e-16,'s^-1'), n=7.45351, w0=(327000,'J/mol'), E0=(118459,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R5nCl',), comment="""BM rule fitted to 1 training reactions at node R5nCl
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R5nCl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R5nCl
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.4997501698654201, 'dE0': 0.0, 'dn': 3.574873125682574e-13, 'dA_dEa': 3.886668764608176e-09, 'dE0_dEa': 0.5000000000329077, 'dn_dEa': -6.530101576246834e-11, 'name': 'C5H10Cl <=> C5H10Cl-2'}, {'dA': 0.4997501698227875, 'dE0': -3.6855134769376164e-13, 'dn': 9.532995001820196e-13, 'dA_dEa': 1.2148433370386075e-06, 'dE0_dEa': 0.5000000089679437, 'dn_dEa': -2.0089595341960836e-08, 'name': '[CH2]CCCCCl <=> [CH2]CCCCCl'}]
""",
)

entry(
    index = 15,
    label = "R5nBr",
    kinetics = ArrheniusBM(A=(1.68639e+09,'s^-1'), n=0.389834, w0=(285000,'J/mol'), E0=(137780,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R5nBr',), comment="""BM rule fitted to 1 training reactions at node R5nBr
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R5nBr
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R5nBr
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.49975016591124977, 'dE0': 5.49239767023679e-12, 'dn': -2.526120920295087e-10, 'dA_dEa': -1.5003109865576167e-07, 'dE0_dEa': 0.4999999989307443, 'dn_dEa': 4.836809577889247e-08, 'name': 'C5H10Br <=> C5H10Br-2'}, {'dA': 0.49975016566966524, 'dE0': -6.548627991436173e-12, 'dn': 2.819458524342881e-10, 'dA_dEa': 6.811120556449918e-07, 'dE0_dEa': 0.5000000070210461, 'dn_dEa': -2.2588134686841547e-07, 'name': '[CH2]CCCCBr <=> [CH2]CCCCBr'}]
""",
)

entry(
    index = 16,
    label = "R2F_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(5.90514e+16,'s^-1'), n=-1.0755, w0=(485000,'J/mol'), E0=(191377,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07401473862015331, var=25.994670041374917, Tref=1000.0, N=4, data_mean=0.0, correlation='R2F_Ext-1R!H-R',), comment="""BM rule fitted to 4 training reactions at node R2F_Ext-1R!H-R
        Total Standard Deviation in ln(k): 10.407102139811068"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node R2F_Ext-1R!H-R
Total Standard Deviation in ln(k): 10.407102139811068""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node R2F_Ext-1R!H-R
Total Standard Deviation in ln(k): 10.407102139811068
sensitivities = [{'dA': -0.18557829007195092, 'dE0': -0.002094133986372175, 'dn': -0.05211793457850909, 'dA_dEa': -10.433460839459213, 'dE0_dEa': 0.09274414409843533, 'dn_dEa': -1.4120114159439576, 'name': 'C3HF4O <=> C3HF4O-2'}, {'dA': -1.2762531101274972, 'dE0': -0.007982532858348414, 'dn': -0.19969322775466247, 'dA_dEa': 13.104562064037871, 'dE0_dEa': 0.2818722043760664, 'dn_dEa': 1.7726505841934206, 'name': 'C2F5 <=> C2F5-2'}, {'dA': -0.18664515445723065, 'dE0': -0.002099378340603403, 'dn': -0.05226387575565375, 'dA_dEa': -16.004531989347356, 'dE0_dEa': 0.14817670747249678, 'dn_dEa': -2.166046764618961, 'name': 'O=C[C](F)C(F)(F)F <=> O=CC(F)(F)[C](F)F'}, {'dA': -0.11539826670060754, 'dE0': -0.001716911034612062, 'dn': -0.042617053813623365, 'dA_dEa': -13.802310248615967, 'dE0_dEa': 0.12490323330167703, 'dn_dEa': -1.8678448916027002, 'name': '[CH2]C(F)(F)F <=> FC[C](F)F'}, {'dA': -1.27819731795867, 'dE0': -0.007992131261944157, 'dn': -0.19995904834187586, 'dA_dEa': 13.046234440382436, 'dE0_dEa': 0.2815749998218107, 'dn_dEa': 1.7647042867894023, 'name': 'F[C](F)C(F)(F)F <=> F[C](F)C(F)(F)F'}]
""",
)

entry(
    index = 17,
    label = "R2F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.36622e+11,'s^-1'), n=0.48217, w0=(485000,'J/mol'), E0=(152869,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R2F_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node R2F_Ext-2R!H-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R2F_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R2F_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.783629443210817, 'dn_dEa': 0.0, 'name': 'C2H2F3 <=> C2H2F3-2'}]
""",
)

entry(
    index = 18,
    label = "R4F_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(0.00363316,'s^-1'), n=4.43046, w0=(485000,'J/mol'), E0=(242580,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R4F_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node R4F_Ext-3R!H-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R4F_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R4F_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.1278241261939503, 'dn_dEa': 0.0, 'name': '[CH2]CCC(F)(F)F <=> FCCC[C](F)F'}]
""",
)

entry(
    index = 19,
    label = "R4F_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.000550858,'s^-1'), n=4.50663, w0=(485000,'J/mol'), E0=(241849,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R4F_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node R4F_Ext-4R!H-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R4F_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R4F_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330828247, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.8910585928854818, 'dn_dEa': 0.0, 'name': 'C4H6F3 <=> C4H6F3-2'}]
""",
)

entry(
    index = 20,
    label = "R2F_Ext-1R!H-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.00763e+12,'s^-1'), n=0.18834, w0=(485000,'J/mol'), E0=(183173,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R2F_Ext-1R!H-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_4R!H->C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.8127036290225224, 'dn_dEa': 0.0, 'name': 'C3HF4O <=> C3HF4O-2'}]
""",
)

entry(
    index = 21,
    label = "R2F_Ext-1R!H-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.78041e+19,'s^-1'), n=-1.75898, w0=(485000,'J/mol'), E0=(196019,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09439094690595154, var=46.93619104513436, Tref=1000.0, N=3, data_mean=0.0, correlation='R2F_Ext-1R!H-R_N-4R!H->C',), comment="""BM rule fitted to 3 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C
        Total Standard Deviation in ln(k): 13.971601741914824"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C
Total Standard Deviation in ln(k): 13.971601741914824""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C
Total Standard Deviation in ln(k): 13.971601741914824
sensitivities = [{'dA': -0.19483100285813051, 'dE0': -0.002382615131495739, 'dn': -0.04579457004236687, 'dA_dEa': 12.727286775566407, 'dE0_dEa': 0.326866590914973, 'dn_dEa': 1.3119708368827816, 'name': 'C2F5 <=> C2F5-2'}, {'dA': 1.1354901174273209, 'dE0': 0.004676062936724784, 'dn': 0.09136122081812387, 'dA_dEa': -22.684137149442673, 'dE0_dEa': 0.16779301971795846, 'dn_dEa': -2.338963991980187, 'name': 'O=C[C](F)C(F)(F)F <=> O=CC(F)(F)[C](F)F'}, {'dA': 1.214104118695181, 'dE0': 0.0050938786200233075, 'dn': 0.09946468120769657, 'dA_dEa': -19.408493306338677, 'dE0_dEa': 0.14200692166676607, 'dn_dEa': -2.0011331579193907, 'name': '[CH2]C(F)(F)F <=> FC[C](F)F'}, {'dA': -0.1921718220785563, 'dE0': -0.002369270693456173, 'dn': -0.04551865414304293, 'dA_dEa': 12.720788263999319, 'dE0_dEa': 0.3268335376029123, 'dn_dEa': 1.3112974050212438, 'name': 'F[C](F)C(F)(F)F <=> F[C](F)C(F)(F)F'}]
""",
)

entry(
    index = 22,
    label = "R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.94868e+19,'s^-1'), n=-1.85415, w0=(485000,'J/mol'), E0=(210642,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.020060994830987895, var=82.6111016070171, Tref=1000.0, N=2, data_mean=0.0, correlation='R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R
        Total Standard Deviation in ln(k): 18.27157182917452"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 18.27157182917452""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 18.27157182917452
sensitivities = [{'dA': -0.5849864371399538, 'dE0': -0.004657107536488209, 'dn': -0.11644589719329844, 'dA_dEa': 10.702997650782933, 'dE0_dEa': 0.38797968451070536, 'dn_dEa': 1.3553606272459404, 'name': 'C2F5 <=> C2F5-2'}, {'dA': 1.0478415426505894, 'dE0': 0.003700201398600338, 'dn': 0.09041182312506602, 'dA_dEa': -36.400568403881294, 'dE0_dEa': 0.18419358708878436, 'dn_dEa': -4.612941384416904, 'name': 'O=C[C](F)C(F)(F)F <=> O=CC(F)(F)[C](F)F'}, {'dA': -0.5652122374187397, 'dE0': -0.0045496005542650896, 'dn': -0.11395980694260094, 'dA_dEa': 10.655501658370989, 'dE0_dEa': 0.3877536426885354, 'dn_dEa': 1.3492919988925902, 'name': 'F[C](F)C(F)(F)F <=> F[C](F)C(F)(F)F'}]
""",
)

entry(
    index = 23,
    label = "R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(4.35648e+12,'s^-1'), n=0.369741, w0=(485000,'J/mol'), E0=(181542,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_5R!H->C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.2331693876808218, 'dn_dEa': -0.0, 'name': 'O=C[C](F)C(F)(F)F <=> O=CC(F)(F)[C](F)F'}]
""",
)

entry(
    index = 24,
    label = "R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.2804e+11,'s^-1'), n=0.253035, w0=(485000,'J/mol'), E0=(209151,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_N-5R!H->C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.49975016704811814, 'dE0': 2.3657224035576856e-12, 'dn': -2.5382418232467507e-10, 'dA_dEa': 3.766444933717554e-07, 'dE0_dEa': 0.500000001768831, 'dn_dEa': -1.8706973866118004e-07, 'name': 'C2F5 <=> C2F5-2'}, {'dA': 0.4997501523611998, 'dE0': -9.323729472844997e-11, 'dn': 7.782771557606027e-09, 'dA_dEa': -1.8179235894424165e-08, 'dE0_dEa': 0.49999999991452204, 'dn_dEa': 9.021617847655674e-09, 'name': 'F[C](F)C(F)(F)F <=> F[C](F)C(F)(F)F'}]
""",
)

