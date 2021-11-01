#!/usr/bin/env python
# encoding: utf-8

name = "XY_Addition_MultipleBond/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(18.531,'m^3/(mol*s)'), n=1.32297, w0=(756348,'J/mol'), E0=(210473,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05578922274092243, var=4.422146091546833, Tref=1000.0, N=33, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 33 training reactions at node Root
        Total Standard Deviation in ln(k): 4.355911149190311"""),
    rank = 11,
    shortDesc = """BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 4.355911149190311""",
    longDesc = 
"""
BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 4.355911149190311
sensitivities = [{'dA': -0.031055189739784918, 'dE0': -0.00013354621550918373, 'dn': 0.004162662544613211, 'dA_dEa': 0.034733383630584584, 'dE0_dEa': 0.00038194986119125744, 'dn_dEa': -0.0046299111789412425, 'name': 'C=C + F <=> C2H5F'}, {'dA': -0.029842953797934956, 'dE0': -0.00012843906705125717, 'dn': 0.004001242424797289, 'dA_dEa': -0.002226513304393297, 'dE0_dEa': 0.0002002942606074707, 'dn_dEa': 0.00029147354273125387, 'name': 'C=CF + F <=> C2H4F2'}, {'dA': -0.02675435034138768, 'dE0': -0.00011542728592448547, 'dn': 0.003589965245745901, 'dA_dEa': -0.07292041127993891, 'dE0_dEa': -0.0001186113243880658, 'dn_dEa': 0.009704898522856456, 'name': 'C=C(F)F + F <=> C2H3F3'}, {'dA': -0.031528262920414024, 'dE0': -0.00013554444268569773, 'dn': 0.004225637474331522, 'dA_dEa': 0.05998724049494747, 'dE0_dEa': 0.0005239754961215861, 'dn_dEa': -0.007992452539524858, 'name': 'C=CF + F <=> C2H4F2-2'}, {'dA': -0.02976569059232376, 'dE0': -0.00012811341170447562, 'dn': 0.003990954628235464, 'dA_dEa': -0.0005767318853600681, 'dE0_dEa': 0.00024005529421257577, 'dn_dEa': 7.201532628339725e-05, 'name': 'FC=CF + F <=> C2H3F3-2'}, {'dA': -0.031183243354607863, 'dE0': -0.00013408918480876174, 'dn': 0.004179700549291196, 'dA_dEa': 0.04683612901246708, 'dE0_dEa': 0.0004630231093242361, 'dn_dEa': -0.00624128154622066, 'name': 'C=C(F)F + F <=> C2H3F3-3'}, {'dA': -0.02610479973874934, 'dE0': -0.00011269221916856345, 'dn': 0.0035034661442527476, 'dA_dEa': -0.08712697323699352, 'dE0_dEa': -0.00017981429626919896, 'dn_dEa': 0.011596630986766504, 'name': 'FC=C(F)F + F <=> C2H2F4'}, {'dA': -0.02835117658062415, 'dE0': -0.00012215905237309213, 'dn': 0.003802580866797312, 'dA_dEa': -0.038918608461284546, 'dE0_dEa': 5.2402085431059034e-05, 'dn_dEa': 0.005177396201642433, 'name': 'FC=C(F)F + F <=> C2H2F4-2'}, {'dA': -0.024286894426242444, 'dE0': -0.00010503231443919298, 'dn': 0.003261399750670002, 'dA_dEa': -0.11658968049844849, 'dE0_dEa': -0.00032452017705396797, 'dn_dEa': 0.015519728527184976, 'name': 'FC(F)=C(F)F + F <=> C2HF5'}, {'dA': -0.029869965262111456, 'dE0': -0.00012856358699082647, 'dn': 0.004004798443794897, 'dA_dEa': -0.007196207009841598, 'dE0_dEa': 0.00013251734272376676, 'dn_dEa': 0.0009528690355641063, 'name': 'C=C + Br <=> C2H5Br'}, {'dA': 0.5555010615463986, 'dE0': 0.0021277739177076294, 'dn': -0.06734780090300876, 'dA_dEa': -16.236247354273214, 'dE0_dEa': -0.01746278258664234, 'dn_dEa': 2.162352762139908, 'name': 'BrH + C3HF3 <=> C3H2BrF3'}, {'dA': -0.027262585875934223, 'dE0': -0.00011758431014574623, 'dn': 0.0036575816233656517, 'dA_dEa': -0.09028691293889608, 'dE0_dEa': -7.946827961843525e-06, 'dn_dEa': 0.01201866732351224, 'name': 'C#CC(F)(F)F + F <=> C3H2F4'}, {'dA': -0.02811588469331693, 'dE0': -0.00012115826145852959, 'dn': 0.003771284325432491, 'dA_dEa': -0.056661315684720236, 'dE0_dEa': 0.0001274659695984252, 'dn_dEa': 0.007541073294503599, 'name': 'C#CC(F)(F)F + F <=> C3H2F4-2'}, {'dA': -0.031879264438931146, 'dE0': -0.00013701802379024965, 'dn': 0.004272395389089988, 'dA_dEa': 0.052240596853720046, 'dE0_dEa': 0.00044042854970156566, 'dn_dEa': -0.006961280258377346, 'name': 'O=C(F)F + F <=> CF3OH'}, {'dA': -0.29234978818773905, 'dE0': -0.0014430544142272144, 'dn': 0.04555556086915028, 'dA_dEa': 7.4797899226818805, 'dE0_dEa': 0.07365414038707428, 'dn_dEa': -0.9957193181977138, 'name': 'C=C + Cl <=> C2H5Cl'}, {'dA': -0.4183921550904762, 'dE0': -0.0019741027937104656, 'dn': 0.062339115586333836, 'dA_dEa': 11.207944985000564, 'dE0_dEa': 0.09176234606209459, 'dn_dEa': -1.4921348672768548, 'name': 'C=CCl + Cl <=> C2H4Cl2'}, {'dA': -0.4457552547654722, 'dE0': -0.002089418958722173, 'dn': 0.06598262210406416, 'dA_dEa': 12.34265330493181, 'dE0_dEa': 0.09787358311399545, 'dn_dEa': -1.643239970681156, 'name': 'C=C(Cl)Cl + Cl <=> C2H3Cl3'}, {'dA': -0.41947200299401644, 'dE0': -0.0019786753496405167, 'dn': 0.06248282255324691, 'dA_dEa': 10.907817466689764, 'dE0_dEa': 0.08934007094777391, 'dn_dEa': -1.452188959799417, 'name': 'C=CCl + Cl <=> C2H4Cl2-2'}, {'dA': -0.4730963263526699, 'dE0': -0.00220458455127953, 'dn': 0.06962342000610149, 'dA_dEa': 13.451258293063855, 'dE0_dEa': 0.1039851898180962, 'dn_dEa': -1.7908663665436992, 'name': 'ClC=CCl + Cl <=> C2H3Cl3-2'}, {'dA': -0.4459709319917729, 'dE0': -0.0020902931675656736, 'dn': 0.06601147234717306, 'dA_dEa': 12.302017072834316, 'dE0_dEa': 0.09777071172133252, 'dn_dEa': -1.6378434608382226, 'name': 'C=C(Cl)Cl + Cl <=> C2H3Cl3-3'}, {'dA': -0.4833768545032235, 'dE0': -0.0022481205224152722, 'dn': 0.07099152945745103, 'dA_dEa': 11.459984034412882, 'dE0_dEa': 0.08764626633603864, 'dn_dEa': -1.5257664587887891, 'name': 'ClC=C(Cl)Cl + Cl <=> C2H2Cl4'}, {'dA': -0.5579092727146576, 'dE0': -0.002562475861613792, 'dn': 0.08091484623649461, 'dA_dEa': 16.360850537297214, 'dE0_dEa': 0.11752704955761537, 'dn_dEa': -2.178291761661362, 'name': 'ClC(Cl)=C(Cl)Cl + Cl <=> C2HCl5'}, {'dA': 0.22845899935488875, 'dE0': 0.0007510057926893679, 'dn': -0.023795203851784907, 'dA_dEa': -5.893541893550608, 'dE0_dEa': 0.0230862474096514, 'dn_dEa': 0.7850938841040359, 'name': 'C#C + Cl <=> C2H3Cl-3'}, {'dA': 0.6377171116645634, 'dE0': 0.0024750815725449542, 'dn': -0.07829208527981053, 'dA_dEa': -12.565821910208326, 'dE0_dEa': -0.018917310882870422, 'dn_dEa': 1.673480177897105, 'name': 'C#CCl + Cl <=> C2H2Cl2-4'}, {'dA': 0.7193490026243492, 'dE0': 0.0028190079182910657, 'dn': -0.08916206039877014, 'dA_dEa': -13.631484481536562, 'dE0_dEa': -0.024791820361702605, 'dn_dEa': 1.8153651964728896, 'name': 'C#CCl + Cl <=> C2H2Cl2-5'}, {'dA': 1.068953509952959, 'dE0': 0.004291834254564977, 'dn': -0.1357152561324214, 'dA_dEa': -20.42001858739309, 'dE0_dEa': -0.053702702087195915, 'dn_dEa': 2.719350249104277, 'name': 'ClC#CCl + Cl <=> C2HCl3-2'}, {'dA': -0.27622770789651185, 'dE0': -0.001375375057480343, 'dn': 0.04340785439232466, 'dA_dEa': 6.925642454360545, 'dE0_dEa': 0.07045563853031368, 'dn_dEa': -0.9219544157984588, 'name': 'C=CC + Cl <=> C3H7Cl'}, {'dA': 0.4129538729956039, 'dE0': 0.0015269956110036491, 'dn': -0.04836726092016861, 'dA_dEa': -4.932068737554129, 'dE0_dEa': -0.0006812320033891484, 'dn_dEa': 0.6568701180211687, 'name': 'ClC(Cl)=C(Cl)Cl + [Cl][Cl] <=> C2Cl6'}, {'dA': 0.5630044880398709, 'dE0': 0.0021603691216205384, 'dn': -0.06834323205792062, 'dA_dEa': -12.10156248152261, 'dE0_dEa': -0.013854290797376082, 'dn_dEa': 1.6116760026780428, 'name': 'FC(F)=C(F)F + Cl <=> C2HClF4'}, {'dA': 0.5407207398056597, 'dE0': 0.002066452630505084, 'dn': -0.06537608068495265, 'dA_dEa': -11.693445775998024, 'dE0_dEa': -0.011930420923554357, 'dn_dEa': 1.5573372585311278, 'name': 'FC(F)=C(F)F + Br <=> C2HBrF4'}, {'dA': -0.29152463122009575, 'dE0': -0.0014397808286929247, 'dn': 0.04544492904251386, 'dA_dEa': 6.9415050801831955, 'dE0_dEa': 0.06845674855579748, 'dn_dEa': -0.9240451580920771, 'name': 'C=C + Cl <=> C2H5Cl'}, {'dA': -0.4195816139045867, 'dE0': -0.0019791133966615797, 'dn': 0.06249750449535257, 'dA_dEa': 10.310838976268746, 'dE0_dEa': 0.08443509805261333, 'dn_dEa': -1.3727158921163192, 'name': 'C=CCl + Cl <=> C2H4Cl2-2'}, {'dA': 0.22854909754513061, 'dE0': 0.0007513577343307918, 'dn': -0.023807307820797947, 'dA_dEa': -4.821223222471003, 'dE0_dEa': 0.01889925970538228, 'dn_dEa': 0.6422397247254114, 'name': 'C#C + Cl <=> C2H3Cl-3'}]
""",
)

entry(
    index = 2,
    label = "Root_1Br1sCl1sF1sH->Cl1s",
    kinetics = ArrheniusBM(A=(5.93272e-05,'m^3/(mol*s)'), n=2.63647, w0=(575000,'J/mol'), E0=(140198,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1Br1sCl1sF1sH->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_1Br1sCl1sF1sH->Cl1s
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.6399258658047055, 'dn_dEa': 0.0, 'name': 'ClC(Cl)=C(Cl)Cl + [Cl][Cl] <=> C2Cl6'}]
""",
)

entry(
    index = 3,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s",
    kinetics = ArrheniusBM(A=(2.10315,'m^3/(mol*s)'), n=1.61376, w0=(762016,'J/mol'), E0=(211241,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0789142276630321, var=3.378165150564068, Tref=1000.0, N=32, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s',), comment="""BM rule fitted to 32 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s
        Total Standard Deviation in ln(k): 3.8829370247759964"""),
    rank = 11,
    shortDesc = """BM rule fitted to 32 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 3.8829370247759964""",
    longDesc = 
"""
BM rule fitted to 32 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 3.8829370247759964
sensitivities = [{'dA': 0.14750932568798295, 'dE0': 0.0006117328779347515, 'dn': -0.015100887442293072, 'dA_dEa': 0.21284298499015933, 'dE0_dEa': 0.001135325267205404, 'dn_dEa': -0.02182043626347306, 'name': 'C=C + F <=> C2H5F'}, {'dA': 0.14877350069532586, 'dE0': 0.0006170335027423815, 'dn': -0.015230400460042006, 'dA_dEa': 0.17466272495705018, 'dE0_dEa': 0.0009480570174312845, 'dn_dEa': -0.01790904862093453, 'name': 'C=CF + F <=> C2H4F2'}, {'dA': 0.1519930303488682, 'dE0': 0.0006305326941933367, 'dn': -0.01556023732164926, 'dA_dEa': 0.1012515066336595, 'dE0_dEa': 0.0006181654292603608, 'dn_dEa': -0.010388267371912388, 'name': 'C=C(F)F + F <=> C2H3F3'}, {'dA': 0.1469950202013399, 'dE0': 0.0006095759986600073, 'dn': -0.015048198753552943, 'dA_dEa': 0.23871637536879006, 'dE0_dEa': 0.0012811314689316722, 'dn_dEa': -0.02447096444875293, 'name': 'C=CF + F <=> C2H4F2-2'}, {'dA': 0.14885329796411859, 'dE0': 0.0006173684846553784, 'dn': -0.015238574460000974, 'dA_dEa': 0.17594916838971902, 'dE0_dEa': 0.0009878194861779191, 'dn_dEa': -0.01804067747858336, 'name': 'FC=CF + F <=> C2H3F3-2'}, {'dA': 0.14743686601327813, 'dE0': 0.0006114108871519148, 'dn': -0.015093516400184316, 'dA_dEa': 0.22512931682608076, 'dE0_dEa': 0.0012183386351234929, 'dn_dEa': -0.023079036873724378, 'name': 'C=C(F)F + F <=> C2H3F3-3'}, {'dA': 0.15267451843438712, 'dE0': 0.0006333877166674307, 'dn': -0.015630061806459837, 'dA_dEa': 0.08646839490201572, 'dE0_dEa': 0.0005547617063183481, 'dn_dEa': -0.00887376745135974, 'name': 'FC=C(F)F + F <=> C2H2F4'}, {'dA': 0.15030328221412026, 'dE0': 0.0006234493655456867, 'dn': -0.015387120041002083, 'dA_dEa': 0.1363062666084475, 'dE0_dEa': 0.0007942409463787254, 'dn_dEa': -0.013979447848497481, 'name': 'FC=C(F)F + F <=> C2H2F4-2'}, {'dA': 0.15456509464241744, 'dE0': 0.0006413171652084832, 'dn': -0.015823742036149686, 'dA_dEa': 0.05601577675218911, 'dE0_dEa': 0.00040551724607449833, 'dn_dEa': -0.005754034146852113, 'name': 'FC(F)=C(F)F + F <=> C2HF5'}, {'dA': 0.14861910917753324, 'dE0': 0.0006164085317111299, 'dn': -0.015214518656172958, 'dA_dEa': 0.17003791408322852, 'dE0_dEa': 0.0008796190717029997, 'dn_dEa': -0.01743546291535249, 'name': 'C=C + Br <=> C2H5Br'}, {'dA': 0.7829985321868601, 'dE0': 0.003056162963275374, 'dn': -0.07486687371122425, 'dA_dEa': -17.523171432352644, 'dE0_dEa': -0.020117928195049043, 'dn_dEa': 1.7954734091822253, 'name': 'BrH + C3HF3 <=> C3H2BrF3'}, {'dA': 0.15147098323932687, 'dE0': 0.0006283261075221507, 'dn': -0.015506805449052887, 'dA_dEa': 0.08081370716706894, 'dE0_dEa': 0.0007250036545151613, 'dn_dEa': -0.008293586044086537, 'name': 'C#CC(F)(F)F + F <=> C3H2F4'}, {'dA': 0.15060055371264863, 'dE0': 0.0006246920763306186, 'dn': -0.015417586577222756, 'dA_dEa': 0.11581342600443133, 'dE0_dEa': 0.0008652439459181222, 'dn_dEa': -0.011879186542456763, 'name': 'C#CC(F)(F)F + F <=> C3H2F4-2'}, {'dA': 0.1466376691548083, 'dE0': 0.0006080811867986589, 'dn': -0.015011578542407889, 'dA_dEa': 0.2312925038201718, 'dE0_dEa': 0.0011966807994901617, 'dn_dEa': -0.023710652343774438, 'name': 'O=C(F)F + F <=> CF3OH'}, {'dA': -0.10234385319264366, 'dE0': -0.0006547329229886328, 'dn': 0.015838963098226248, 'dA_dEa': 7.799354353906078, 'dE0_dEa': 0.07684284449272626, 'dn_dEa': -0.7988327965770812, 'name': 'C=C + Cl <=> C2H5Cl'}, {'dA': -0.2347853748525789, 'dE0': -0.0012098385795701462, 'dn': 0.029408034684088414, 'dA_dEa': 11.746202105977726, 'dE0_dEa': 0.095906768469183, 'dn_dEa': -1.203167416470154, 'name': 'C=CCl + Cl <=> C2H4Cl2'}, {'dA': -0.26329952841844373, 'dE0': -0.0013294321345937567, 'dn': 0.032329170197501894, 'dA_dEa': 12.928571528875924, 'dE0_dEa': 0.10226198710617873, 'dn_dEa': -1.3242963516087365, 'name': 'C=C(Cl)Cl + Cl <=> C2H3Cl3'}, {'dA': -0.23591421495752596, 'dE0': -0.001214597127323247, 'dn': 0.02952361052410161, 'dA_dEa': 11.428498173689333, 'dE0_dEa': 0.09336456789740387, 'dn_dEa': -1.1706252941851294, 'name': 'C=CCl + Cl <=> C2H4Cl2-2'}, {'dA': -0.2917728435583344, 'dE0': -0.0014488146157220923, 'dn': 0.035246235565384254, 'dA_dEa': 14.064676703026574, 'dE0_dEa': 0.10854455268356887, 'dn_dEa': -1.4406664552535295, 'name': 'ClC=CCl + Cl <=> C2H3Cl3-2'}, {'dA': -0.2634293284571611, 'dE0': -0.0013299682397923732, 'dn': 0.032342492041224274, 'dA_dEa': 12.836233606377949, 'dE0_dEa': 0.1019602815534156, 'dn_dEa': -1.3148076388079764, 'name': 'C=C(Cl)Cl + Cl <=> C2H3Cl3-3'}, {'dA': -0.30191673310889783, 'dE0': -0.001491700965764352, 'dn': 0.03628445200537309, 'dA_dEa': 12.051322466883002, 'dE0_dEa': 0.09176438602701441, 'dn_dEa': -1.2344745636547665, 'name': 'ClC=C(Cl)Cl + Cl <=> C2H2Cl4'}, {'dA': -0.3841467894681184, 'dE0': -0.0018356930540018332, 'dn': 0.04471109220971892, 'dA_dEa': 17.181189325259478, 'dE0_dEa': 0.12294897996482591, 'dn_dEa': -1.7599613893431654, 'name': 'ClC(Cl)=C(Cl)Cl + Cl <=> C2HCl5'}, {'dA': 0.4397895026140782, 'dE0': 0.0016185364069242788, 'dn': -0.0397014932714636, 'dA_dEa': -6.4827625713797445, 'dE0_dEa': 0.023005457013257916, 'dn_dEa': 0.6643718469898025, 'name': 'C#C + Cl <=> C2H3Cl-3'}, {'dA': 0.8662688244044213, 'dE0': 0.0034067051779850307, 'dn': -0.0833938358529737, 'dA_dEa': -13.4955124582105, 'dE0_dEa': -0.020946784086580773, 'dn_dEa': 1.3827683705636644, 'name': 'C#CCl + Cl <=> C2H2Cl2-4'}, {'dA': 0.9512612582188655, 'dE0': 0.0037631225077652593, 'dn': -0.09210105530914876, 'dA_dEa': -14.62150246375088, 'dE0_dEa': -0.027117885002357893, 'dn_dEa': 1.4981136705263423, 'name': 'C#CCl + Cl <=> C2H2Cl2-5'}, {'dA': 1.3158479175935718, 'dE0': 0.005291776577054595, 'dn': -0.12945257925634873, 'dA_dEa': -21.807548090616095, 'dE0_dEa': -0.05758522576397002, 'dn_dEa': 2.2343067973065764, 'name': 'ClC#CCl + Cl <=> C2HCl3-2'}, {'dA': -0.08707676186015938, 'dE0': -0.0005905950500131957, 'dn': 0.014275218894627463, 'dA_dEa': 7.193108060814872, 'dE0_dEa': 0.0734021232289897, 'dn_dEa': -0.7367251746203749, 'name': 'C=CC + Cl <=> C3H7Cl'}, {'dA': 0.7884600638941899, 'dE0': 0.0030804835250214883, 'dn': -0.07542235325685936, 'dA_dEa': -13.043647814038655, 'dE0_dEa': -0.015793388202332316, 'dn_dEa': 1.336498664131743, 'name': 'FC(F)=C(F)F + Cl <=> C2HClF4'}, {'dA': 0.7649877710483598, 'dE0': 0.002982084610068779, 'dn': -0.07301759383436243, 'dA_dEa': -12.594743551237075, 'dE0_dEa': -0.013701168449167534, 'dn_dEa': 1.2905018063910079, 'name': 'FC(F)=C(F)F + Br <=> C2HBrF4'}, {'dA': -0.10121544223197225, 'dE0': -0.00065024735965528, 'dn': 0.015722671780602947, 'dA_dEa': 7.2560617767964075, 'dE0_dEa': 0.07149376037849885, 'dn_dEa': -0.7431812245484782, 'name': 'C=C + Cl <=> C2H5Cl'}, {'dA': -0.23587829324081366, 'dE0': -0.0012144568634861995, 'dn': 0.029519899966084097, 'dA_dEa': 10.851620322298002, 'dE0_dEa': 0.08843206895751454, 'dn_dEa': -1.1115699000391999, 'name': 'C=CCl + Cl <=> C2H4Cl2-2'}, {'dA': 0.43975649723342736, 'dE0': 0.001618408187856231, 'dn': -0.039698081314058276, 'dA_dEa': -5.296867294516756, 'dE0_dEa': 0.018866730328218874, 'dn_dEa': 0.5428498284990818, 'name': 'C#C + Cl <=> C2H3Cl-3'}]
""",
)

entry(
    index = 4,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(59029.4,'m^3/(mol*s)'), n=0.288781, w0=(866292,'J/mol'), E0=(240067,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.009670056152757593, var=11.544460769953993, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 12 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s
        Total Standard Deviation in ln(k): 6.835813163783375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 6.835813163783375""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 6.835813163783375
sensitivities = [{'dA': -0.302016141698258, 'dE0': -0.0014259320532084424, 'dn': 0.0745874349375382, 'dA_dEa': 16.285810968197385, 'dE0_dEa': 0.1293113085124071, 'dn_dEa': -3.1499976128677867, 'name': 'C=C + F <=> C2H5F'}, {'dA': 0.01273424200576441, 'dE0': -0.0002549151844988462, 'dn': 0.013697524294576206, 'dA_dEa': 6.634831134307915, 'dE0_dEa': 0.08588767124224075, 'dn_dEa': -1.2830435039427133, 'name': 'C=CF + F <=> C2H4F2'}, {'dA': 0.812075669367563, 'dE0': 0.002719762560521858, 'dn': -0.14093411065325548, 'dA_dEa': -11.856790259527434, 'dE0_dEa': 0.010956188053840134, 'dn_dEa': 2.29402527546605, 'name': 'C=C(F)F + F <=> C2H3F3'}, {'dA': -0.43051728131442724, 'dE0': -0.0019038875764999894, 'dn': 0.09944745585507204, 'dA_dEa': 22.873654797326136, 'dE0_dEa': 0.16413051898135098, 'dn_dEa': -4.42443234415329, 'name': 'C=CF + F <=> C2H4F2-2'}, {'dA': 0.03304849528263185, 'dE0': -0.00017934011479269485, 'dn': 0.0097676169984246, 'dA_dEa': 7.049736241298342, 'dE0_dEa': 0.09691253261922819, 'dn_dEa': -1.363367084724761, 'name': 'FC=CF + F <=> C2H3F3-2'}, {'dA': -0.3366448726885112, 'dE0': -0.0015550697633304241, 'dn': 0.08128466340599692, 'dA_dEa': 19.43000441261003, 'dE0_dEa': 0.14971095880302893, 'dn_dEa': -3.758252031760194, 'name': 'C=C(F)F + F <=> C2H3F3-3'}, {'dA': 0.9792688072752765, 'dE0': 0.003341891372760763, 'dn': -0.17327785118179248, 'dA_dEa': -15.590653897265602, 'dE0_dEa': -0.0033268089069957247, 'dn_dEa': 3.0163605094500294, 'name': 'FC=C(F)F + F <=> C2H2F4'}, {'dA': 0.3940562817863914, 'dE0': 0.0011640997787429896, 'dn': -0.060069037316953525, 'dA_dEa': -2.9413874885738562, 'dE0_dEa': 0.05216622652610078, 'dn_dEa': 0.5693377357536465, 'name': 'FC=C(F)F + F <=> C2H2F4-2'}, {'dA': 1.4528145123399663, 'dE0': 0.005103974141764032, 'dn': -0.26488582263039007, 'dA_dEa': -23.28951920874446, 'dE0_dEa': -0.03794765540076063, 'dn_dEa': 4.505593903703119, 'name': 'FC(F)=C(F)F + F <=> C2HF5'}, {'dA': 0.6751794298703506, 'dE0': 0.002208370999002233, 'dn': -0.11446349942327308, 'dA_dEa': -16.878399978971085, 'dE0_dEa': 0.04548542386306602, 'dn_dEa': 3.265721521306966, 'name': 'C#CC(F)(F)F + F <=> C3H2F4'}, {'dA': 0.4678713080066803, 'dE0': 0.0014386154957867082, 'dn': -0.0743491823291982, 'dA_dEa': -8.00000989397897, 'dE0_dEa': 0.07671290719273086, 'dn_dEa': 1.5481799469542863, 'name': 'C#CC(F)(F)F + F <=> C3H2F4-2'}, {'dA': -0.5072796421173312, 'dE0': -0.002191680418411001, 'dn': 0.11428362038870622, 'dA_dEa': 20.987829791413763, 'dE0_dEa': 0.14236866214956573, 'dn_dEa': -4.0597411121608795, 'name': 'O=C(F)F + F <=> CF3OH'}]
""",
)

entry(
    index = 5,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(1.74868,'m^3/(mol*s)'), n=1.63746, w0=(699450,'J/mol'), E0=(210999,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07982101879078687, var=3.3410847943152633, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 20 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s
        Total Standard Deviation in ln(k): 3.864937299850754"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 3.864937299850754""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 3.864937299850754
sensitivities = [{'dA': -0.8526863411627945, 'dE0': -0.003808322905771674, 'dn': 0.07622451667261716, 'dA_dEa': 20.0331623969595, 'dE0_dEa': 0.177929967751897, 'dn_dEa': -1.5578001908101218, 'name': 'C=CF + F <=> C2H4F2'}, {'dA': 0.4560115500026832, 'dE0': 0.0014110623652954031, 'dn': -0.025533271585203406, 'dA_dEa': -12.690212402889738, 'dE0_dEa': 0.037808892514257585, 'dn_dEa': 0.9870044260303065, 'name': 'C=C(F)F + F <=> C2H3F3'}, {'dA': -0.8363765413872215, 'dE0': -0.003739106960223314, 'dn': 0.07496595688373052, 'dA_dEa': 21.805508498567175, 'dE0_dEa': 0.20027527900187286, 'dn_dEa': -1.6954999129669797, 'name': 'FC=CF + F <=> C2H3F3-2'}, {'dA': 0.7433902102163533, 'dE0': 0.002553725231258154, 'dn': -0.04788638470199227, 'dA_dEa': -19.86838738035981, 'dE0_dEa': 0.008739455858352287, 'dn_dEa': 1.5455745823509148, 'name': 'FC=C(F)F + F <=> C2H2F4'}, {'dA': -0.16119954650069657, 'dE0': -0.001067180230142625, 'dn': 0.02241955730080207, 'dA_dEa': 4.01165290267613, 'dE0_dEa': 0.1171535637754722, 'dn_dEa': -0.3120155337090253, 'name': 'FC=C(F)F + F <=> C2H2F4-2'}, {'dA': 1.4704964446357558, 'dE0': 0.005465165807055188, 'dn': -0.10439583792639155, 'dA_dEa': -33.39864364768828, 'dE0_dEa': -0.05482625498518902, 'dn_dEa': 2.597504823162841, 'name': 'FC(F)=C(F)F + F <=> C2HF5'}, {'dA': 0.17876647675237636, 'dE0': 0.0002330115245323075, 'dn': -0.004142958171888958, 'dA_dEa': 1.434073155724849, 'dE0_dEa': 0.17649826282342132, 'dn_dEa': -0.11138487961490569, 'name': 'C#CC(F)(F)F + F <=> C3H2F4-2'}, {'dA': -1.512015943874817, 'dE0': -0.006488180034573789, 'dn': 0.12737471591390645, 'dA_dEa': 44.816758087819984, 'dE0_dEa': 0.28163963654908003, 'dn_dEa': -3.485049339413325, 'name': 'O=C(F)F + F <=> CF3OH'}]
""",
)

entry(
    index = 6,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.77089,'m^3/(mol*s)'), n=1.62248, w0=(871625,'J/mol'), E0=(221465,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05571320516261351, var=11.313190983790786, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R
        Total Standard Deviation in ln(k): 6.882926863784101"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 6.882926863784101""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 6.882926863784101
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.8588766402888115, 'dn_dEa': -0.0, 'name': 'C#CC(F)(F)F + F <=> C3H2F4-2'}]
""",
)

entry(
    index = 7,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.84221e+08,'m^3/(mol*s)'), n=-0.741075, w0=(854667,'J/mol'), E0=(275401,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07092136257417955, var=4.263901037659594, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
        Total Standard Deviation in ln(k): 4.317815056244463"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 4.317815056244463""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 4.317815056244463
sensitivities = [{'dA': 0.016419041157790946, 'dE0': -0.0005518046803989837, 'dn': 0.00552847492408977, 'dA_dEa': 27.68449436868486, 'dE0_dEa': 0.2434742910332887, 'dn_dEa': -1.2112336504773438, 'name': 'C=CF + F <=> C2H4F2'}, {'dA': 1.7997937206202004, 'dE0': 0.0072204472758263345, 'dn': -0.0725100668432996, 'dA_dEa': -16.707635378955096, 'dE0_dEa': 0.03776846479525287, 'dn_dEa': 0.7313157619881671, 'name': 'C=C(F)F + F <=> C2H3F3'}, {'dA': 0.061279724830505346, 'dE0': -0.00035620182749772475, 'dn': 0.0035655329004619573, 'dA_dEa': 30.289292278721685, 'dE0_dEa': 0.2739018958644132, 'dn_dEa': -1.3251777248268095, 'name': 'FC=CF + F <=> C2H3F3-2'}, {'dA': 2.171965388900316, 'dE0': 0.00884244914485204, 'dn': -0.08879587859585694, 'dA_dEa': -25.460075717169378, 'dE0_dEa': -0.001168523759195012, 'dn_dEa': 1.1143049701411603, 'name': 'FC=C(F)F + F <=> C2H2F4'}, {'dA': 0.8650552183909597, 'dE0': 0.0031473031316234146, 'dn': -0.031606212044877575, 'dA_dEa': 5.510886235815245, 'dE0_dEa': 0.15073381986814435, 'dn_dEa': -0.2409278696089058, 'name': 'FC=C(F)F + F <=> C2H2F4-2'}, {'dA': 3.22504131802539, 'dE0': 0.01343190692526448, 'dn': -0.13487737359221785, 'dA_dEa': -44.54357168624725, 'dE0_dEa': -0.09630007494638229, 'dn_dEa': 1.949359179536271, 'name': 'FC(F)=C(F)F + F <=> C2HF5'}, {'dA': -1.1606075477940294, 'dE0': -0.005681076703628757, 'dn': 0.05703437810367814, 'dA_dEa': 61.49254093926226, 'dE0_dEa': 0.39702812497000634, 'dn_dEa': -2.6906154809561516, 'name': 'O=C(F)F + F <=> CF3OH'}]
""",
)

entry(
    index = 8,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(3234.02,'m^3/(mol*s)'), n=0.841082, w0=(690500,'J/mol'), E0=(231106,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08953372930780412, var=8.7042697151113, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 6 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct
        Total Standard Deviation in ln(k): 6.13952889033091"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 6.13952889033091""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 6.13952889033091
sensitivities = [{'dA': 2.30185191417601, 'dE0': 0.010245885411599457, 'dn': -0.0524866213111052, 'dA_dEa': -7.645649695185728, 'dE0_dEa': 0.18359654697170422, 'dn_dEa': 0.19580778903473117, 'name': 'C=C(F)F + F <=> C2H3F3'}, {'dA': 3.293465737993636, 'dE0': 0.01520008281275212, 'dn': -0.07784889850846904, 'dA_dEa': -29.90124952209757, 'dE0_dEa': 0.07084400651519841, 'dn_dEa': 0.7650421704432782, 'name': 'FC=C(F)F + F <=> C2H2F4'}, {'dA': 6.101260317181063, 'dE0': 0.029222389867064942, 'dn': -0.14966670059072446, 'dA_dEa': -81.57800872327147, 'dE0_dEa': -0.21129075897295016, 'dn_dEa': 2.0867680056610194, 'name': 'FC(F)=C(F)F + F <=> C2HF5'}, {'dA': -5.6068437250515535, 'dE0': -0.029255368666884045, 'dn': 0.14979929690796492, 'dA_dEa': 204.6863733567127, 'dE0_dEa': 1.2811981822953118, 'dn_dEa': -5.235048509745848, 'name': 'O=C(F)F + F <=> CF3OH'}]
""",
)

entry(
    index = 9,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(3.873,'m^3/(mol*s)'), n=1.45743, w0=(703286,'J/mol'), E0=(205682,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.044056942611570095, var=2.2630917047093937, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 14 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct
        Total Standard Deviation in ln(k): 3.1265342294230076"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 3.1265342294230076""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 3.1265342294230076
sensitivities = [{'dA': -1.289593764013528, 'dE0': -0.007549720560661457, 'dn': 0.1862574340161294, 'dA_dEa': 32.62461399877208, 'dE0_dEa': 0.509946724050478, 'dn_dEa': -3.393437500902359, 'name': 'FC=C(F)F + F <=> C2H2F4'}, {'dA': 2.047131793118554, 'dE0': 0.0065400041146315745, 'dn': -0.1610389072653713, 'dA_dEa': -36.699709627233055, 'dE0_dEa': 0.1767175798037566, 'dn_dEa': 3.8219655970769475, 'name': 'FC(F)=C(F)F + F <=> C2HF5'}]
""",
)

entry(
    index = 10,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(1.56721e+32,'m^3/(mol*s)'), n=-7.40875, w0=(847000,'J/mol'), E0=(355628,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Ct
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.6921911050812886, 'dn_dEa': 0.0, 'name': 'FC(F)=C(F)F + F <=> C2HF5'}]
""",
)

entry(
    index = 11,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(1.35339e-05,'m^3/(mol*s)'), n=3.0724, w0=(875143,'J/mol'), E0=(200812,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08039416804036821, var=7.687635206276118, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 7 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct
        Total Standard Deviation in ln(k): 5.760441167260633"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 5.760441167260633""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 5.760441167260633
sensitivities = [{'dA': 0.9995003330836019, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.986870022472573, 'dn_dEa': 0.0, 'name': 'O=C(F)F + F <=> CF3OH'}]
""",
)

entry(
    index = 12,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(1.64483e+40,'m^3/(mol*s)'), n=-10.004, w0=(847000,'J/mol'), E0=(368699,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Ct
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.7463137652847429, 'dn_dEa': 0.0, 'name': 'C=C(F)F + F <=> C2H3F3'}]
""",
)

entry(
    index = 13,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(0.155486,'m^3/(mol*s)'), n=1.84406, w0=(858500,'J/mol'), E0=(243042,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0002592053915720451, var=0.023805321282912618, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct
        Total Standard Deviation in ln(k): 0.30996130688542933"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 0.30996130688542933""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 0.30996130688542933
sensitivities = [{'dA': -0.6883822680788446, 'dE0': -0.004578596484625732, 'dn': 0.06696500763656676, 'dA_dEa': 34.16914955793281, 'dE0_dEa': 0.5713304436345771, 'dn_dEa': -1.9245943628691842, 'name': 'FC=CF + F <=> C2H3F3-2'}, {'dA': 1.6738547630057066, 'dE0': 0.004530501949700769, 'dn': -0.06616401748300758, 'dA_dEa': -28.96982297643688, 'dE0_dEa': 0.28077956415290234, 'dn_dEa': 1.6335332752626954, 'name': 'FC=C(F)F + F <=> C2H2F4-2'}]
""",
)

entry(
    index = 14,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(4402.23,'m^3/(mol*s)'), n=0.832427, w0=(699500,'J/mol'), E0=(224340,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.007734243753195459, var=0.9741359578645888, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 5 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s
        Total Standard Deviation in ln(k): 1.9980727377529526"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 1.9980727377529526""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 1.9980727377529526
sensitivities = [{'dA': 0.9995003330835186, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.7962483572908988, 'dn_dEa': 0.0, 'name': 'FC=C(F)F + F <=> C2H2F4-2'}]
""",
)

entry(
    index = 15,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(645500,'J/mol'), E0=(275727,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': -1.1968178441926978, 'dE0': -0.0049307141875103095, 'dn': -0.447113856891604, 'dA_dEa': 45.89509980299916, 'dE0_dEa': 0.42598014233702625, 'dn_dEa': 13.393596322166523, 'name': 'C=CF + F <=> C2H4F2-2'}, {'dA': -0.872412834720489, 'dE0': -0.0038770017157143933, 'dn': -0.35240064342473093, 'dA_dEa': 35.18425207230212, 'dE0_dEa': 0.3854545985338373, 'dn_dEa': 10.267669987167295, 'name': 'C=C(F)F + F <=> C2H3F3-3'}, {'dA': 2.5980593279054194, 'dE0': 0.00740702498963477, 'dn': 0.6607154658832887, 'dA_dEa': -97.62303206250077, 'dE0_dEa': 0.061189886049240035, 'dn_dEa': -28.49644455831771, 'name': 'C#CC(F)(F)F + F <=> C3H2F4'}]
""",
)

entry(
    index = 16,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(103.798,'m^3/(mol*s)'), n=1.02893, w0=(711000,'J/mol'), E0=(207162,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0265270309925669, var=2.1852915220856866, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 12 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s
        Total Standard Deviation in ln(k): 3.030196880314295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 3.030196880314295""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 3.030196880314295
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.8503701961384889, 'dn_dEa': -0.0, 'name': 'C#CC(F)(F)F + F <=> C3H2F4'}]
""",
)

entry(
    index = 17,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.0660936,'m^3/(mol*s)'), n=2.05911, w0=(657000,'J/mol'), E0=(219798,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.724983558345639, var=68.1820070515672, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s
        Total Standard Deviation in ln(k): 30.937958818928855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 30.937958818928855""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 30.937958818928855
sensitivities = [{'dA': 0.21777293844585, 'dE0': -0.0010325880768243029, 'dn': 0.01692955712083687, 'dA_dEa': 8.717409329408525, 'dE0_dEa': 0.49912687570219977, 'dn_dEa': -0.5227640918081994, 'name': 'C=CF + F <=> C2H4F2-2'}, {'dA': 0.7686319460421267, 'dE0': 0.0009870330086973007, 'dn': -0.016138697877869528, 'dA_dEa': -8.885044538884037, 'dE0_dEa': 0.4250698789586928, 'dn_dEa': 0.533875829611803, 'name': 'C=C(F)F + F <=> C2H3F3-3'}]
""",
)

entry(
    index = 18,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(8.66807e-14,'m^3/(mol*s)'), n=5.44878, w0=(887625,'J/mol'), E0=(174247,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.2961558164851907, var=19.42048908477356, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R
        Total Standard Deviation in ln(k): 12.09127656637391"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.09127656637391""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.09127656637391
sensitivities = [{'dA': 0.9995003330834908, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.9086910262407434, 'dn_dEa': 0.0, 'name': 'C=C(F)F + F <=> C2H3F3-3'}]
""",
)

entry(
    index = 19,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R",
    kinetics = ArrheniusBM(A=(0.0965843,'m^3/(mol*s)'), n=2.00355, w0=(858500,'J/mol'), E0=(228419,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0012758229263045246, var=11.664448724158145, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R
        Total Standard Deviation in ln(k): 6.8500285488231"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 6.8500285488231""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 6.8500285488231
sensitivities = [{'dA': -0.0078061277797311915, 'dE0': -3.169679262805664e-05, 'dn': 0.000830418776138654, 'dA_dEa': 0.014074382834740492, 'dE0_dEa': 0.00023429822267483804, 'dn_dEa': -0.001428780090801084, 'name': 'C=C + Br <=> C2H5Br'}, {'dA': 0.6372878470322787, 'dE0': 0.0024561341415338597, 'dn': -0.05965670688221487, 'dA_dEa': -18.176199055743638, 'dE0_dEa': -0.022700806810998477, 'dn_dEa': 1.8549897698975104, 'name': 'BrH + C3HF3 <=> C3H2BrF3'}, {'dA': -0.26784194338616735, 'dE0': -0.0013426708324677126, 'dn': 0.032703872306131095, 'dA_dEa': 7.824945258139122, 'dE0_dEa': 0.07717997286546281, 'dn_dEa': -0.7982246809610793, 'name': 'C=C + Cl <=> C2H5Cl'}, {'dA': -0.40305434268188556, 'dE0': -0.0019102014654717083, 'dn': 0.04650097876917998, 'dA_dEa': 11.899132317962003, 'dE0_dEa': 0.09680092364866279, 'dn_dEa': -1.2139562951151062, 'name': 'C=CCl + Cl <=> C2H4Cl2'}, {'dA': -0.43263353384408776, 'dE0': -0.0020343194783138184, 'dn': 0.04951934977452107, 'dA_dEa': 13.141724090486422, 'dE0_dEa': 0.10341283006007075, 'dn_dEa': -1.3407676380374456, 'name': 'C=C(Cl)Cl + Cl <=> C2H3Cl3'}, {'dA': -0.4044879064020625, 'dE0': -0.0019161752541519237, 'dn': 0.046647384806302906, 'dA_dEa': 11.601314802999807, 'dE0_dEa': 0.09432921075922272, 'dn_dEa': -1.1835919142531908, 'name': 'C=CCl + Cl <=> C2H4Cl2-2'}, {'dA': -0.4617135732086173, 'dE0': -0.002156410418479828, 'dn': 0.05248659483117753, 'dA_dEa': 14.272821038794143, 'dE0_dEa': 0.1096950661484497, 'dn_dEa': -1.4561358436381884, 'name': 'ClC=CCl + Cl <=> C2H3Cl3-2'}, {'dA': -0.4332614217772901, 'dE0': -0.002036801996770545, 'dn': 0.049583867048520656, 'dA_dEa': 13.061823385558053, 'dE0_dEa': 0.10315959074882407, 'dn_dEa': -1.3325964796806267, 'name': 'C=C(Cl)Cl + Cl <=> C2H3Cl3-3'}, {'dA': -0.47095894653642245, 'dE0': -0.0021959420733220773, 'dn': 0.05342789402081791, 'dA_dEa': 12.176211332012086, 'dE0_dEa': 0.09252948964014726, 'dn_dEa': -1.2422488673193022, 'name': 'ClC=C(Cl)Cl + Cl <=> C2H2Cl4'}, {'dA': -0.5540618893729643, 'dE0': -0.0025442010973168914, 'dn': 0.061909349302460975, 'dA_dEa': 17.49764015265291, 'dE0_dEa': 0.12456659684215776, 'dn_dEa': -1.7852289500209007, 'name': 'ClC(Cl)=C(Cl)Cl + Cl <=> C2HCl5'}, {'dA': 0.2901540611835216, 'dE0': 0.0009992460423909717, 'dn': -0.024234710857990758, 'dA_dEa': -6.8384948152878415, 'dE0_dEa': 0.021704326276429056, 'dn_dEa': 0.6980570771012766, 'name': 'C#C + Cl <=> C2H3Cl-3'}, {'dA': 0.7283183597697998, 'dE0': 0.0028382595325794004, 'dn': -0.06894542629640366, 'dA_dEa': -14.037213378786042, 'dE0_dEa': -0.02311925536837992, 'dn_dEa': 1.4325672572975603, 'name': 'C#CCl + Cl <=> C2H2Cl2-4'}, {'dA': 0.8159852020011914, 'dE0': 0.003206168256283099, 'dn': -0.07789114033507603, 'dA_dEa': -15.171070911698676, 'dE0_dEa': -0.029340097464203758, 'dn_dEa': 1.5482388898800872, 'name': 'C#CCl + Cl <=> C2H2Cl2-5'}, {'dA': 1.1904785140110152, 'dE0': 0.00477791939094399, 'dn': -0.11610489215551481, 'dA_dEa': -22.57931531790529, 'dE0_dEa': -0.060763744165684884, 'dn_dEa': 2.304197408609568, 'name': 'ClC#CCl + Cl <=> C2HCl3-2'}, {'dA': -0.25179565023017436, 'dE0': -0.0012752812897009749, 'dn': 0.031066606326666836, 'dA_dEa': 7.228451399126886, 'dE0_dEa': 0.07376677118195439, 'dn_dEa': -0.7373802988401974, 'name': 'C=CC + Cl <=> C3H7Cl'}, {'dA': 0.6485402364414131, 'dE0': 0.0025033993881917716, 'dn': -0.06080485819569688, 'dA_dEa': -13.536516786349198, 'dE0_dEa': -0.017754869354071546, 'dn_dEa': 1.3814720583337357, 'name': 'FC(F)=C(F)F + Cl <=> C2HClF4'}, {'dA': 0.6242927204232606, 'dE0': 0.002401678242656017, 'dn': -0.0583304836652789, 'dA_dEa': -13.091959191968815, 'dE0_dEa': -0.015675086806323263, 'dn_dEa': 1.3361099818881217, 'name': 'FC(F)=C(F)F + Br <=> C2HBrF4'}, {'dA': -0.2706698001082884, 'dE0': -0.001353823817369794, 'dn': 0.03299448146787617, 'dA_dEa': 7.288001650762958, 'dE0_dEa': 0.07183768862616371, 'dn_dEa': -0.7434563240110683, 'name': 'C=C + Cl <=> C2H5Cl'}, {'dA': -0.4045074618606483, 'dE0': -0.0019162536125532956, 'dn': 0.046649390655706585, 'dA_dEa': 10.9614110367081, 'dE0_dEa': 0.08913124166170601, 'dn_dEa': -1.118306207719446, 'name': 'C=CCl + Cl <=> C2H4Cl2-2'}, {'dA': 0.29041061990134764, 'dE0': 0.001000260593654512, 'dn': -0.02426106760369071, 'dA_dEa': -5.620762385478437, 'dE0_dEa': 0.017666679156542256, 'dn_dEa': 0.5737712401166927, 'name': 'C#C + Cl <=> C2H3Cl-3'}]
""",
)

entry(
    index = 20,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(52.9173,'m^3/(mol*s)'), n=1.09798, w0=(858500,'J/mol'), E0=(249103,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3Cd-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3Cd-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.0895538209464518, 'dE0': -0.00030689824929378115, 'dn': 0.010028647595169462, 'dA_dEa': 1.3373575412593348, 'dE0_dEa': 0.1678224880889693, 'dn_dEa': -0.1726353790257852, 'name': 'BrH + C3HF3 <=> C3H2BrF3'}, {'dA': -0.9427333982109304, 'dE0': -0.004452464645248358, 'dn': 0.1442960190461928, 'dA_dEa': 31.145105797470638, 'dE0_dEa': 0.27792346804387, 'dn_dEa': -4.049627256016748, 'name': 'C#C + Cl <=> C2H3Cl-3'}, {'dA': 0.35520098003342687, 'dE0': 0.000761534460442036, 'dn': -0.024517573767620728, 'dA_dEa': -4.568115875186299, 'dE0_dEa': 0.09014882517824083, 'dn_dEa': 0.5950006998484297, 'name': 'C#CCl + Cl <=> C2H2Cl2-4'}, {'dA': 0.6156253914789257, 'dE0': 0.0018074251790463896, 'dn': -0.05839027411786618, 'dA_dEa': -9.45212127830801, 'dE0_dEa': 0.06612564334918132, 'dn_dEa': 1.2302202788794103, 'name': 'C#CCl + Cl <=> C2H2Cl2-5'}, {'dA': 1.7257725042407426, 'dE0': 0.006266987854054811, 'dn': -0.20277989968521246, 'dA_dEa': -31.344880980661472, 'dE0_dEa': -0.022839486177421094, 'dn_dEa': 4.077656348827435, 'name': 'ClC#CCl + Cl <=> C2HCl3-2'}, {'dA': -0.9415302640373084, 'dE0': -0.004447944312578883, 'dn': 0.1441383275196603, 'dA_dEa': 25.489617516812366, 'dE0_dEa': 0.22745225459057866, 'dn_dEa': -3.314271455999076, 'name': 'C#C + Cl <=> C2H3Cl-3'}]
""",
)

entry(
    index = 21,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.237624,'m^3/(mol*s)'), n=2.2618, w0=(699500,'J/mol'), E0=(218542,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.005716926918813203, var=0.8821332733001921, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
        Total Standard Deviation in ln(k): 1.8972504194064923"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 1.8972504194064923""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 1.8972504194064923
sensitivities = [{'dA': -1.2192088877701857, 'dE0': -0.00598861519321828, 'dn': 0.16237481975057091, 'dA_dEa': 40.6194407117955, 'dE0_dEa': 0.36404200684957677, 'dn_dEa': -4.646315853003219, 'name': 'C#C + Cl <=> C2H3Cl-3'}, {'dA': 0.44620184868021023, 'dE0': 0.0010398212091022316, 'dn': -0.028180516107436753, 'dA_dEa': -5.589650552822516, 'dE0_dEa': 0.11318927819486327, 'dn_dEa': 0.6405544259725254, 'name': 'C#CCl + Cl <=> C2H2Cl2-4'}, {'dA': 0.7807893371945845, 'dE0': 0.0024516442908506433, 'dn': -0.06646452109035073, 'dA_dEa': -11.8799069931099, 'dE0_dEa': 0.08108791964387668, 'dn_dEa': 1.3602547796070812, 'name': 'C#CCl + Cl <=> C2H2Cl2-5'}, {'dA': 2.2051214160268215, 'dE0': 0.008461823137109225, 'dn': -0.22943855104736985, 'dA_dEa': -40.117506354909494, 'dE0_dEa': -0.039355537955804924, 'dn_dEa': 4.591208168217071, 'name': 'ClC#CCl + Cl <=> C2HCl3-2'}, {'dA': -1.220090710099121, 'dE0': -0.005992251546565131, 'dn': 0.16247598470988475, 'dA_dEa': 33.248032089177144, 'dE0_dEa': 0.2979486218875677, 'dn_dEa': -3.8031298206668818, 'name': 'C#C + Cl <=> C2H3Cl-3'}]
""",
)

entry(
    index = 22,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3Ct-R",
    kinetics = ArrheniusBM(A=(2.10658,'m^3/(mol*s)'), n=1.73542, w0=(699500,'J/mol'), E0=(212290,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3Ct-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3Ct-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3Ct-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3Ct-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': -1.9859734678793173, 'dE0': -0.011218661590727248, 'dn': 0.11778873055173884, 'dA_dEa': 52.41422757255209, 'dE0_dEa': 0.602214657610969, 'dn_dEa': -2.4817899057763317, 'name': 'C#CCl + Cl <=> C2H2Cl2-4'}, {'dA': 2.9885228269351765, 'dE0': 0.011231598879693033, 'dn': -0.11793420309901842, 'dA_dEa': -48.69175657794148, 'dE0_dEa': 0.12764962339774444, 'dn_dEa': 2.3091728549674726, 'name': 'ClC#CCl + Cl <=> C2HCl3-2'}]
""",
)

entry(
    index = 23,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R",
    kinetics = ArrheniusBM(A=(0.861211,'m^3/(mol*s)'), n=1.62393, w0=(711000,'J/mol'), E0=(204231,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04415051193696195, var=3.3076813581525575, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R
        Total Standard Deviation in ln(k): 3.756949050610777"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 3.756949050610777""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 3.756949050610777
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.6804994449800477, 'dn_dEa': 0.0, 'name': 'ClC#CCl + Cl <=> C2HCl3-2'}]
""",
)

entry(
    index = 24,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(2.84999e+06,'m^3/(mol*s)'), n=-0.353558, w0=(711000,'J/mol'), E0=(213624,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0011176031788138253, var=0.766425788910674, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
        Total Standard Deviation in ln(k): 1.757868355229437"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 1.757868355229437""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 1.757868355229437
sensitivities = [{'dA': 0.9995003330834908, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.7024182582868447, 'dn_dEa': 0.0, 'name': 'C#CCl + Cl <=> C2H2Cl2-5'}]
""",
)

entry(
    index = 25,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s_Ext-3CdO2d-R",
    kinetics = ArrheniusBM(A=(0.882649,'m^3/(mol*s)'), n=1.68333, w0=(657000,'J/mol'), E0=(219941,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s_Ext-3CdO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s_Ext-3CdO2d-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.7871784499758653, 'dn_dEa': nan, 'name': 'BrH + C3HF3 <=> C3H2BrF3'}]
""",
)

entry(
    index = 26,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R",
    kinetics = ArrheniusBM(A=(4251.74,'m^3/(mol*s)'), n=0.489676, w0=(858500,'J/mol'), E0=(217340,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.012824852924355307, var=24.354166144100823, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R
        Total Standard Deviation in ln(k): 9.925578901029992"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 9.925578901029992""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 9.925578901029992
sensitivities = [{'dA': -0.01081878764708341, 'dE0': -4.875255580957364e-05, 'dn': 0.0016220556527032073, 'dA_dEa': -0.020731986258406616, 'dE0_dEa': 0.0001648191398767162, 'dn_dEa': 0.003006581520898586, 'name': 'C=C + Br <=> C2H5Br'}, {'dA': 0.01935262579255905, 'dE0': -0.00024365615493716168, 'dn': 0.008346082757494912, 'dA_dEa': 0.8512730633541792, 'dE0_dEa': 0.06858169156522372, 'dn_dEa': -0.12323291232712487, 'name': 'C=C + Cl <=> C2H5Cl'}, {'dA': -0.18226816806434573, 'dE0': -0.0010925915370986212, 'dn': 0.037632560996337334, 'dA_dEa': 6.178637904753051, 'dE0_dEa': 0.09471483191898543, 'dn_dEa': -0.8970354322514124, 'name': 'C=CCl + Cl <=> C2H4Cl2'}, {'dA': -0.22621364553734585, 'dE0': -0.0012776240995063162, 'dn': 0.044015878076407416, 'dA_dEa': 7.624598796892763, 'dE0_dEa': 0.10286121103887375, 'dn_dEa': -1.1070614259614087, 'name': 'C=C(Cl)Cl + Cl <=> C2H3Cl3'}, {'dA': -0.18407238258080022, 'dE0': -0.0011002116939969287, 'dn': 0.03789453668527242, 'dA_dEa': 5.997742566526071, 'dE0_dEa': 0.09217151069550186, 'dn_dEa': -0.8707719544983046, 'name': 'C=CCl + Cl <=> C2H4Cl2-2'}, {'dA': -0.2697752390865857, 'dE0': -0.0014610565468427194, 'dn': 0.050343368874687024, 'dA_dEa': 9.015380049190219, 'dE0_dEa': 0.11093971001417696, 'dn_dEa': -1.3090918464069639, 'name': 'ClC=CCl + Cl <=> C2H3Cl3-2'}, {'dA': -0.22712067670662975, 'dE0': -0.001281234232299919, 'dn': 0.04414849126586999, 'dA_dEa': 7.5363694046587915, 'dE0_dEa': 0.10259595763777087, 'dn_dEa': -1.0942669762391692, 'name': 'C=C(Cl)Cl + Cl <=> C2H3Cl3-3'}, {'dA': -0.2888257813600566, 'dE0': -0.0015409850034547444, 'dn': 0.0531116958588489, 'dA_dEa': 7.915280503930849, 'dE0_dEa': 0.09405161968220946, 'dn_dEa': -1.149358941205972, 'name': 'ClC=C(Cl)Cl + Cl <=> C2H2Cl4'}, {'dA': -0.40681846019379225, 'dE0': -0.0020386701304700708, 'dn': 0.07024714710098334, 'dA_dEa': 13.298849046552563, 'dE0_dEa': 0.13096444776286953, 'dn_dEa': -1.9312308514566285, 'name': 'ClC(Cl)=C(Cl)Cl + Cl <=> C2HCl5'}, {'dA': 0.044036351918746296, 'dE0': -0.00013982774718359345, 'dn': 0.004760223403033411, 'dA_dEa': 0.16458476731264363, 'dE0_dEa': 0.06436411409337947, 'dn_dEa': -0.02350327829479671, 'name': 'C=CC + Cl <=> C3H7Cl'}, {'dA': 1.3849280503290122, 'dE0': 0.005506136536783061, 'dn': -0.19001103267472547, 'dA_dEa': -29.15517868653305, 'dE0_dEa': -0.06549031953734398, 'dn_dEa': 4.2353138680098725, 'name': 'FC(F)=C(F)F + Cl <=> C2HClF4'}, {'dA': 1.3494026502673215, 'dE0': 0.005356483739408981, 'dn': -0.18485106982540547, 'dA_dEa': -28.544594790659996, 'dE0_dEa': -0.06260677871866836, 'dn_dEa': 4.146622533877654, 'name': 'FC(F)=C(F)F + Br <=> C2HBrF4'}, {'dA': 0.022609595451863744, 'dE0': -0.0002307439234474215, 'dn': 0.007869733399189852, 'dA_dEa': 0.7786329868598476, 'dE0_dEa': 0.06375326467568104, 'dn_dEa': -0.11269998115565057, 'name': 'C=C + Cl <=> C2H5Cl'}, {'dA': -0.18417090516822196, 'dE0': -0.0011006017913797394, 'dn': 0.037908948081148516, 'dA_dEa': 5.6911096534315195, 'dE0_dEa': 0.0871893985960116, 'dn_dEa': -0.826282942375017, 'name': 'C=CCl + Cl <=> C2H4Cl2-2'}]
""",
)

entry(
    index = 27,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3CdO2d->O2d",
    kinetics = ArrheniusBM(A=(0.109156,'m^3/(mol*s)'), n=1.86531, w0=(975000,'J/mol'), E0=(170750,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3CdO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3CdO2d->O2d
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3CdO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3CdO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.15686126311200205, 'dE0': 0.0003081151548043891, 'dn': -0.01124583348339382, 'dA_dEa': -1.8506948879519576, 'dE0_dEa': 0.0628020627030336, 'dn_dEa': 0.28307455866937464, 'name': 'C=C + Cl <=> C2H5Cl'}, {'dA': -0.06304545615077456, 'dE0': -0.0006201394856605956, 'dn': 0.022339760049690103, 'dA_dEa': 3.828398676409139, 'dE0_dEa': 0.09079088585179215, 'dn_dEa': -0.5842714050213095, 'name': 'C=CCl + Cl <=> C2H4Cl2'}, {'dA': -0.11098178062064591, 'dE0': -0.0008224744509935305, 'dn': 0.029660955260678818, 'dA_dEa': 5.305098479425093, 'dE0_dEa': 0.0992636568672266, 'dn_dEa': -0.8097806972270538, 'name': 'C=C(Cl)Cl + Cl <=> C2H3Cl3'}, {'dA': -0.0651417270427573, 'dE0': -0.000628977371568374, 'dn': 0.02265996418289241, 'dA_dEa': 3.6708776227345075, 'dE0_dEa': 0.08820064527340907, 'dn_dEa': -0.560181745037417, 'name': 'C=CCl + Cl <=> C2H4Cl2-2'}, {'dA': -0.15849976193928553, 'dE0': -0.0010230519691431601, 'dn': 0.03691822962639788, 'dA_dEa': 6.689418466494804, 'dE0_dEa': 0.10753198655464406, 'dn_dEa': -1.0211740405945977, 'name': 'ClC=CCl + Cl <=> C2H3Cl3-2'}, {'dA': -0.11198808484459545, 'dE0': -0.0008265156441134417, 'dn': 0.029815523856364882, 'dA_dEa': 5.176941366495173, 'dE0_dEa': 0.0988458326282221, 'dn_dEa': -0.7901982968179078, 'name': 'C=C(Cl)Cl + Cl <=> C2H3Cl3-3'}, {'dA': -0.17833470278196561, 'dE0': -0.0011066736580382824, 'dn': 0.0399479939961958, 'dA_dEa': 6.032162712596321, 'dE0_dEa': 0.09143847080365243, 'dn_dEa': -0.9208718646331698, 'name': 'ClC=C(Cl)Cl + Cl <=> C2H2Cl4'}, {'dA': -0.31119357766144035, 'dE0': -0.001667227495693727, 'dn': 0.060240241695942685, 'dA_dEa': 11.33540794768298, 'dE0_dEa': 0.12928988149081755, 'dn_dEa': -1.7307383484634276, 'name': 'ClC(Cl)=C(Cl)Cl + Cl <=> C2HCl5'}, {'dA': 0.1825524115810696, 'dE0': 0.00041675690095988423, 'dn': -0.01516871382977893, 'dA_dEa': -2.537928944201186, 'dE0_dEa': 0.058459816557765734, 'dn_dEa': 0.3880152630408754, 'name': 'C=CC + Cl <=> C3H7Cl'}, {'dA': 1.6445411290339642, 'dE0': 0.006588127267573377, 'dn': -0.23845268576050618, 'dA_dEa': -34.253231266086146, 'dE0_dEa': -0.08237956482512848, 'dn_dEa': 5.231711077789227, 'name': 'FC(F)=C(F)F + Cl <=> C2HClF4'}, {'dA': 0.154693677180812, 'dE0': 0.00029945090781986734, 'dn': -0.010912756658844305, 'dA_dEa': -1.7318735857252097, 'dE0_dEa': 0.05839006980295494, 'dn_dEa': 0.26490938749278825, 'name': 'C=C + Cl <=> C2H5Cl'}, {'dA': -0.06516556413239279, 'dE0': -0.0006290725697420046, 'dn': 0.022663627425598947, 'dA_dEa': 3.4762457258205535, 'dE0_dEa': 0.0833743274856902, 'dn_dEa': -0.5304890559841248, 'name': 'C=CCl + Cl <=> C2H4Cl2-2'}]
""",
)

entry(
    index = 28,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3CdO2d->O2d",
    kinetics = ArrheniusBM(A=(10.477,'m^3/(mol*s)'), n=1.29062, w0=(858500,'J/mol'), E0=(214595,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3CdO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3CdO2d->O2d
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3CdO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3CdO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': -0.1495349553182366, 'dE0': -0.0012384313542419176, 'dn': 0.035310548336767854, 'dA_dEa': 6.886504106855854, 'dE0_dEa': 0.1533570965104732, 'dn_dEa': -0.8318416434194562, 'name': 'C=CCl + Cl <=> C2H4Cl2-2'}, {'dA': -0.30840537097723897, 'dE0': -0.001907615664208982, 'dn': 0.054514242479514544, 'dA_dEa': 12.038925093746037, 'dE0_dEa': 0.18633996757577598, 'dn_dEa': -1.4545935609138847, 'name': 'ClC=CCl + Cl <=> C2H3Cl3-2'}, {'dA': -0.22603546974633562, 'dE0': -0.0015610880239490907, 'dn': 0.04455623140198119, 'dA_dEa': 9.45002265397725, 'dE0_dEa': 0.17149838950638027, 'dn_dEa': -1.1416813251860072, 'name': 'C=C(Cl)Cl + Cl <=> C2H3Cl3-3'}, {'dA': -0.34188754890611006, 'dE0': -0.0020485166277532632, 'dn': 0.05856190270654564, 'dA_dEa': 10.811584887612327, 'dE0_dEa': 0.15838598290977315, 'dn_dEa': -1.306348313927875, 'name': 'ClC=C(Cl)Cl + Cl <=> C2H2Cl4'}, {'dA': -0.5668082889034933, 'dE0': -0.0029958706692525426, 'dn': 0.08574965627292572, 'dA_dEa': 19.887676100889678, 'dE0_dEa': 0.22308327897859662, 'dn_dEa': -2.4032810719511986, 'name': 'ClC(Cl)=C(Cl)Cl + Cl <=> C2HCl5'}, {'dA': 2.759881146341707, 'dE0': 0.01101677130533826, 'dn': -0.31636823885981136, 'dA_dEa': -57.55962476709499, 'dE0_dEa': -0.13604415488012583, 'dn_dEa': 6.958046589187644, 'name': 'FC(F)=C(F)F + Cl <=> C2HClF4'}, {'dA': -0.14955164431464366, 'dE0': -0.0012384935624867833, 'dn': 0.03531259556979175, 'dA_dEa': 6.528459308667243, 'dE0_dEa': 0.14499671148488816, 'dn_dEa': -0.7886138277816034, 'name': 'C=CCl + Cl <=> C2H4Cl2-2'}]
""",
)

entry(
    index = 29,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R_Ext-3CdO2d-R",
    kinetics = ArrheniusBM(A=(4.14111,'m^3/(mol*s)'), n=1.29695, w0=(858500,'J/mol'), E0=(229024,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R_Ext-3CdO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R_Ext-3CdO2d-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.325002270999111, 'dE0': 0.0006725778262127921, 'dn': -0.01969329278903727, 'dA_dEa': -4.642202317442457, 'dE0_dEa': 0.12622911222737976, 'dn_dEa': 0.5779374152768993, 'name': 'C=CCl + Cl <=> C2H4Cl2-2'}, {'dA': 0.1356757631163646, 'dE0': -0.00012922514113578802, 'dn': 0.0038485854761584185, 'dA_dEa': 0.37791230453269875, 'dE0_dEa': 0.16071649705319807, 'dn_dEa': -0.0462485140384914, 'name': 'ClC=CCl + Cl <=> C2H3Cl3-2'}, {'dA': 0.23271517051484455, 'dE0': 0.00028148085753857294, 'dn': -0.008218720969666108, 'dA_dEa': -2.308961761793326, 'dE0_dEa': 0.14471832611639357, 'dn_dEa': 0.28781964138975386, 'name': 'C=C(Cl)Cl + Cl <=> C2H3Cl3-3'}, {'dA': 0.09893475774936912, 'dE0': -0.00028572815518922504, 'dn': 0.008413906072103237, 'dA_dEa': 1.2755685988540562, 'dE0_dEa': 0.13778800202437289, 'dn_dEa': -0.15800143159727623, 'name': 'ClC=C(Cl)Cl + Cl <=> C2H2Cl4'}, {'dA': -0.17067193772392844, 'dE0': -0.001426827751076959, 'dn': 0.04194076750009714, 'dA_dEa': 9.460408971215516, 'dE0_dEa': 0.2034868761229622, 'dn_dEa': -1.1756190277284877, 'name': 'ClC(Cl)=C(Cl)Cl + Cl <=> C2HCl5'}, {'dA': 0.3247499302277215, 'dE0': 0.0006715693638476014, 'dn': -0.01966170892047526, 'dA_dEa': -4.36181986905119, 'dE0_dEa': 0.11937755551061992, 'dn_dEa': 0.5430116822424139, 'name': 'C=CCl + Cl <=> C2H4Cl2-2'}]
""",
)

entry(
    index = 30,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-3Ct-R",
    kinetics = ArrheniusBM(A=(40.7026,'m^3/(mol*s)'), n=1.65435, w0=(699500,'J/mol'), E0=(223829,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-3Ct-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-3Ct-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-3Ct-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-3Ct-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.670450666060492, 'dE0': 0.0014391032073679656, 'dn': -0.04631401748363084, 'dA_dEa': -10.649142246943306, 'dE0_dEa': 0.2650716564490335, 'dn_dEa': 1.4641420687603546, 'name': 'C=C(Cl)Cl + Cl <=> C2H3Cl3-3'}, {'dA': 0.4134901404771363, 'dE0': 0.00034067431791956303, 'dn': -0.011038017882256798, 'dA_dEa': -2.5619695430159672, 'dE0_dEa': 0.25505158422345847, 'dn_dEa': 0.353073229281575, 'name': 'ClC=C(Cl)Cl + Cl <=> C2H2Cl4'}, {'dA': -0.13789598726755967, 'dE0': -0.0020007231256942938, 'dn': 0.0647169228978895, 'dA_dEa': 12.688096457309571, 'dE0_dEa': 0.3822817518010989, 'dn_dEa': -1.7414131204155583, 'name': 'ClC(Cl)=C(Cl)Cl + Cl <=> C2HCl5'}]
""",
)

entry(
    index = 31,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(863.231,'m^3/(mol*s)'), n=0.722812, w0=(711000,'J/mol'), E0=(207515,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.006812385391110879, var=3.4113384386473915, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl
        Total Standard Deviation in ln(k): 3.719823940287308"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.719823940287308""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.719823940287308
sensitivities = [{'dA': 1.2053838872520202, 'dE0': 0.0030131582666353845, 'dn': -0.0885142523932945, 'dA_dEa': -11.51988318798385, 'dE0_dEa': 0.3568824622700698, 'dn_dEa': 1.4437657186392339, 'name': 'ClC=C(Cl)Cl + Cl <=> C2H2Cl4'}, {'dA': 0.314506647625147, 'dE0': -0.0008335378330761694, 'dn': 0.02309297426482884, 'dA_dEa': 10.168190577258382, 'dE0_dEa': 0.5463467012019115, 'dn_dEa': -1.2714720362692882, 'name': 'ClC(Cl)=C(Cl)Cl + Cl <=> C2HCl5'}]
""",
)

entry(
    index = 32,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.18057,'m^3/(mol*s)'), n=1.62936, w0=(711000,'J/mol'), E0=(219824,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_N-5R!H->Cl
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.9451900642010095, 'dn_dEa': 0.0, 'name': 'ClC(Cl)=C(Cl)Cl + Cl <=> C2HCl5'}]
""",
)

entry(
    index = 33,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.25612e+07,'m^3/(mol*s)'), n=-0.637747, w0=(711000,'J/mol'), E0=(215085,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.9041823457180511, 'dn_dEa': -0.0, 'name': 'ClC=CCl + Cl <=> C2H3Cl3-2'}]
""",
)

entry(
    index = 34,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->C",
    kinetics = ArrheniusBM(A=(8.97967e+06,'m^3/(mol*s)'), n=-0.518739, w0=(711000,'J/mol'), E0=(212126,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330834908, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.7354502500279404, 'dn_dEa': 0.0, 'name': 'FC(F)=C(F)F + Cl <=> C2HClF4'}]
""",
)

entry(
    index = 35,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.6085e+08,'m^3/(mol*s)'), n=-0.88707, w0=(711000,'J/mol'), E0=(212590,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': -0.0477296576288974, 'dE0': -0.0015550193857336808, 'dn': -1.1742662252530058, 'dA_dEa': 7.113250528861032, 'dE0_dEa': 0.3247127744998559, 'dn_dEa': 21.839657398809628, 'name': 'C=CCl + Cl <=> C2H4Cl2'}, {'dA': -0.1088817628112202, 'dE0': -0.0018468001471142232, 'dn': -1.3590528873392258, 'dA_dEa': 12.673058657087186, 'dE0_dEa': 0.3567791942822353, 'dn_dEa': 38.932514274197885, 'name': 'C=C(Cl)Cl + Cl <=> C2H3Cl3'}, {'dA': 1.0556989401192594, 'dE0': 0.0030116283776568473, 'dn': 2.2220049970979368, 'dA_dEa': -17.495353791686135, 'dE0_dEa': 0.20042890759564222, 'dn_dEa': -53.82568456008296, 'name': 'C=CC + Cl <=> C3H7Cl'}]
""",
)

entry(
    index = 36,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R_Ext-3CdO2d-R",
    kinetics = ArrheniusBM(A=(26.4943,'m^3/(mol*s)'), n=1.22463, w0=(858500,'J/mol'), E0=(202816,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R_Ext-3CdO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R_Ext-3CdO2d-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.8930715902013446, 'dn_dEa': -0.0, 'name': 'C=C(Cl)Cl + Cl <=> C2H3Cl3'}]
""",
)

entry(
    index = 37,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R",
    kinetics = ArrheniusBM(A=(631.246,'m^3/(mol*s)'), n=0.744315, w0=(711000,'J/mol'), E0=(204988,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.007791397538652573, var=13.169458742624444, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R
        Total Standard Deviation in ln(k): 7.294709630031939"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 7.294709630031939""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 7.294709630031939
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.8429664860987649, 'dn_dEa': -0.0, 'name': 'C=CC + Cl <=> C3H7Cl'}]
""",
)

entry(
    index = 38,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(5.59096e+06,'m^3/(mol*s)'), n=-0.339093, w0=(711000,'J/mol'), E0=(220112,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.8826548532721864, 'dn_dEa': -0.0, 'name': 'C=CCl + Cl <=> C2H4Cl2'}]
""",
)

entry(
    index = 39,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(179.755,'m^3/(mol*s)'), n=0.928737, w0=(711000,'J/mol'), E0=(199420,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0015583992925483614, var=35.83408174955999, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R
        Total Standard Deviation in ln(k): 12.004575517732093"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.004575517732093""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.004575517732093
sensitivities = [{'dA': -0.07880352745693632, 'dE0': -0.0003476965268211674, 'dn': 0.005494771859024376, 'dA_dEa': 1.5059864332685462, 'dE0_dEa': 0.00950329129807375, 'dn_dEa': -0.09860643727667151, 'name': 'C=C + Br <=> C2H5Br'}, {'dA': 1.0721286050873262, 'dE0': 0.00032306813240187145, 'dn': -0.005088428769491093, 'dA_dEa': -1.5609055393819902, 'dE0_dEa': 0.7292220630655122, 'dn_dEa': 0.10555580949809021, 'name': 'FC(F)=C(F)F + Br <=> C2HBrF4'}]
""",
)

entry(
    index = 40,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.0823032,'m^3/(mol*s)'), n=1.92336, w0=(711000,'J/mol'), E0=(210237,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.7386763320225301, 'dn_dEa': 0.0, 'name': 'FC(F)=C(F)F + Br <=> C2HBrF4'}]
""",
)

