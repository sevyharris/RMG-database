#!/usr/bin/env python
# encoding: utf-8

name = "1,3_sigmatropic_rearrangement/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(5.36025e-75,'s^-1'), n=26.0114, w0=(735278,'J/mol'), E0=(-18847.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0014814239980872, var=102.87700592211432, Tref=1000.0, N=72, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 72 training reactions at node Root
        Total Standard Deviation in ln(k): 22.849972614810042"""),
    rank = 11,
    shortDesc = """BM rule fitted to 72 training reactions at node Root
Total Standard Deviation in ln(k): 22.849972614810042""",
    longDesc = 
"""
BM rule fitted to 72 training reactions at node Root
Total Standard Deviation in ln(k): 22.849972614810042
sensitivities = [{'dA': 0.0, 'dE0': -0.0, 'dn': 0.0, 'dA_dEa': -0.047795158593549596, 'dE0_dEa': -0.0, 'dn_dEa': 0.00023613758326873003, 'name': 'C2H4O <=> C2H4O-2'}, {'dA': 0.00026023420218737695, 'dE0': -0.0, 'dn': -3.1942147165948204e-07, 'dA_dEa': -0.046646343605521584, 'dE0_dEa': -0.0, 'dn_dEa': 0.00023046071978996067, 'name': 'C4H8O <=> C4H8O-2'}, {'dA': 0.00026035806399707465, 'dE0': -0.0, 'dn': -3.201066562293291e-07, 'dA_dEa': -0.04664641349450507, 'dE0_dEa': -0.0, 'dn_dEa': 0.00023046110547991723, 'name': 'C2H4O <=> C2H4O-2'}, {'dA': 0.0032996040317815637, 'dE0': -0.0, 'dn': -3.2171331006393667e-07, 'dA_dEa': -0.30573817772964235, 'dE0_dEa': -0.0, 'dn_dEa': 0.0015107205143045038, 'name': 'CH2OS <=> CH2OS-2'}, {'dA': 0.0032999849679530594, 'dE0': -0.0, 'dn': -3.238149714412173e-07, 'dA_dEa': -0.3002261450433583, 'dE0_dEa': -0.0, 'dn_dEa': 0.0014834841620893335, 'name': 'C2H4OS <=> C2H4OS-2'}, {'dA': 0.003297487666032247, 'dE0': -0.0, 'dn': -3.1000743517835795e-07, 'dA_dEa': -0.30022612529027026, 'dE0_dEa': -0.0, 'dn_dEa': 0.0014834840552344715, 'name': 'C3H6OS <=> C3H6OS-2'}, {'dA': 0.00025732205699571857, 'dE0': -0.0, 'dn': -3.0333468424864287e-07, 'dA_dEa': -0.08033468543545472, 'dE0_dEa': -0.0, 'dn_dEa': 0.00039692629010115916, 'name': 'C3H6O <=> C3H6O-2'}, {'dA': 0.01770383519783731, 'dE0': -0.0, 'dn': -3.0709225394238906e-07, 'dA_dEa': -1.8832144887428313, 'dE0_dEa': -0.0, 'dn_dEa': 0.009305557401657668, 'name': 'C2H4N2O2 <=> C2H4N2O2-2'}, {'dA': 0.01770535266132551, 'dE0': -0.0, 'dn': -3.153601659942781e-07, 'dA_dEa': -1.4243100119701215, 'dE0_dEa': -0.0, 'dn_dEa': 0.0070379620221158665, 'name': 'C2H4N2O2-3 <=> C2H4N2O2-4'}, {'dA': 0.01770492693253995, 'dE0': -0.0, 'dn': -3.129959508650932e-07, 'dA_dEa': -1.6097617384788871, 'dE0_dEa': -0.0, 'dn_dEa': 0.007954340487837627, 'name': 'C2H4N2O2-5 <=> C2H4N2O2-6'}, {'dA': 0.01770575775595002, 'dE0': -0.0, 'dn': -3.1757648085988377e-07, 'dA_dEa': -1.4060765147691383, 'dE0_dEa': -0.0, 'dn_dEa': 0.006947863352981968, 'name': 'C2H4N2O2-7 <=> C2H4N2O2-8'}, {'dA': 0.017734821739170136, 'dE0': -0.0, 'dn': -4.78029796412637e-07, 'dA_dEa': -6.4046780082954005, 'dE0_dEa': -0.0, 'dn_dEa': 0.03164762876442068, 'name': 'C2H2N2O <=> C2H2N2O-2'}, {'dA': 0.01770719575233865, 'dE0': -0.0, 'dn': -3.255358683101344e-07, 'dA_dEa': -1.4719329262222147, 'dE0_dEa': -0.0, 'dn_dEa': 0.00727328068354061, 'name': 'C3H3NO <=> C3H3NO-2'}, {'dA': 0.017707807273838756, 'dE0': -0.0, 'dn': -3.289137680395583e-07, 'dA_dEa': -1.4744995078503311, 'dE0_dEa': -0.0, 'dn_dEa': 0.007285963122386176, 'name': 'C3H6N2O <=> C3H6N2O-2'}, {'dA': 0.017702787459940868, 'dE0': -0.0, 'dn': -3.011631088707249e-07, 'dA_dEa': -1.3544800264925598, 'dE0_dEa': -0.0, 'dn_dEa': 0.00669290852370701, 'name': 'C2H5N3O <=> C2H5N3O-2'}, {'dA': 0.017705631194077927, 'dE0': -0.0, 'dn': -3.168506613425038e-07, 'dA_dEa': -1.437871805393501, 'dE0_dEa': -0.0, 'dn_dEa': 0.007104972069213209, 'name': 'C2H3NO2 <=> C2H3NO2-2'}, {'dA': 0.017706968662880303, 'dE0': -0.0, 'dn': -3.2427509039257427e-07, 'dA_dEa': -1.4962983201771123, 'dE0_dEa': -0.0, 'dn_dEa': 0.007393679548328698, 'name': 'C2H4N2O2-9 <=> C2H4N2O2-10'}, {'dA': 0.017705615675824578, 'dE0': -0.0, 'dn': -3.1680414322074904e-07, 'dA_dEa': -1.456196621831101, 'dE0_dEa': -0.0, 'dn_dEa': 0.007195524111076266, 'name': 'C2H4N2O <=> C2H4N2O-2'}, {'dA': 0.01770508958998302, 'dE0': -0.0, 'dn': -3.138551679375053e-07, 'dA_dEa': -1.3728534571841158, 'dE0_dEa': -0.0, 'dn_dEa': 0.006783691856955065, 'name': 'CH4N2O <=> CH4N2O-2'}, {'dA': 0.017708526456774183, 'dE0': -0.0, 'dn': -3.3291364242044493e-07, 'dA_dEa': -2.586054134411882, 'dE0_dEa': -0.0, 'dn_dEa': 0.012778531206127713, 'name': 'C2H4N2O2-11 <=> C2H4N2O2-12'}, {'dA': 0.017705427296734473, 'dE0': -0.0, 'dn': -3.158000358808712e-07, 'dA_dEa': -1.786922335498017, 'dE0_dEa': -0.0, 'dn_dEa': 0.008829746078961942, 'name': 'C2H4N2O2-13 <=> C2H4N2O2-14'}, {'dA': 0.01770604470152843, 'dE0': -0.0, 'dn': -3.191702738020061e-07, 'dA_dEa': -2.064474568669766, 'dE0_dEa': -0.0, 'dn_dEa': 0.010201229831436067, 'name': 'C2H3NO2-3 <=> C2H3NO2-4'}, {'dA': 0.017736754927002173, 'dE0': -0.0, 'dn': -4.891012462082834e-07, 'dA_dEa': -4.838172619429848, 'dE0_dEa': -0.0, 'dn_dEa': 0.023907010539330868, 'name': 'C2H2N2O-3 <=> C2H2N2O-4'}, {'dA': 0.017701796053872516, 'dE0': -0.0, 'dn': -2.9569038866427844e-07, 'dA_dEa': -1.9862869635292013, 'dE0_dEa': -0.0, 'dn_dEa': 0.009814880411280964, 'name': 'C2H3NO2-3 <=> C2H3NO2-4'}, {'dA': 0.017715026984889977, 'dE0': -0.0, 'dn': -3.686481794624528e-07, 'dA_dEa': -3.160153393082858, 'dE0_dEa': -0.0, 'dn_dEa': 0.015615347557900425, 'name': 'C2H4N2O-3 <=> C2H4N2O-4'}, {'dA': 0.017702513162023155, 'dE0': -0.0, 'dn': -2.996468917375289e-07, 'dA_dEa': -7.171118142509493, 'dE0_dEa': -0.0, 'dn_dEa': 0.035434876038040394, 'name': 'C3H3NO-3 <=> C3H3NO-4'}, {'dA': 0.017730154496577732, 'dE0': -0.0, 'dn': -4.518094466315312e-07, 'dA_dEa': -7.580729668945576, 'dE0_dEa': -0.0, 'dn_dEa': 0.0374589018452477, 'name': 'C4H4N2O <=> C4H4N2O-2'}, {'dA': 0.017700502382924373, 'dE0': -0.0, 'dn': -2.885126424775135e-07, 'dA_dEa': -8.10173565622652, 'dE0_dEa': -0.0, 'dn_dEa': 0.04003337243735259, 'name': 'C2H3N3 <=> C2H3N3-2'}, {'dA': 0.017716684197923445, 'dE0': -0.0, 'dn': -3.7801131964565695e-07, 'dA_dEa': -8.758822819232646, 'dE0_dEa': -0.0, 'dn_dEa': 0.043280257939117536, 'name': 'C3H4N2 <=> C3H4N2-2'}, {'dA': 0.017705862177310468, 'dE0': -0.0, 'dn': -3.1817410190642774e-07, 'dA_dEa': -2.282243488821474, 'dE0_dEa': -0.0, 'dn_dEa': 0.011277299330373917, 'name': 'C2H5N3O-3 <=> C2H5N3O-4'}, {'dA': 0.017709314846572073, 'dE0': -0.0, 'dn': -3.3723845956358924e-07, 'dA_dEa': -1.945717011381235, 'dE0_dEa': -0.0, 'dn_dEa': 0.00961440883825136, 'name': 'C2H4N2O-5 <=> C2H4N2O-6'}, {'dA': 0.017722580849978974, 'dE0': -0.0, 'dn': -4.1034976016355443e-07, 'dA_dEa': -4.7105918864934395, 'dE0_dEa': -0.0, 'dn_dEa': 0.023276605304817736, 'name': 'C3H3N3O <=> C3H3N3O-2'}, {'dA': 0.01770422343838813, 'dE0': -0.0, 'dn': -3.0896666061309695e-07, 'dA_dEa': -8.897053980093531, 'dE0_dEa': -0.0, 'dn_dEa': 0.04396330830528801, 'name': 'C4H3N3 <=> C4H3N3-2'}, {'dA': 0.017689754713503265, 'dE0': -0.0, 'dn': -2.2919519633989154e-07, 'dA_dEa': -5.976703491314287, 'dE0_dEa': -0.0, 'dn_dEa': 0.02953286982002868, 'name': 'C4H4N2O-3 <=> C4H4N2O-4'}, {'dA': 0.006412262678168896, 'dE0': -0.0, 'dn': -3.259866836371404e-07, 'dA_dEa': -1.533606521945954, 'dE0_dEa': -0.0, 'dn_dEa': 0.007578032397067791, 'name': 'C6H6O <=> C6H6O-2'}, {'dA': 0.006388818462711036, 'dE0': -0.0, 'dn': -1.968828880609798e-07, 'dA_dEa': -3.154286530446263, 'dE0_dEa': -0.0, 'dn_dEa': 0.01558634410359736, 'name': 'C6H6O-3 <=> C6H6O-4'}, {'dA': 0.0, 'dE0': -0.0, 'dn': 0.0, 'dA_dEa': -0.04995175100930833, 'dE0_dEa': -0.0, 'dn_dEa': 0.0002467938745617855, 'name': 'CC=O <=> C=CO'}, {'dA': 0.0002600836239708146, 'dE0': -0.0, 'dn': -3.1858934455209184e-07, 'dA_dEa': -0.052351615323692695, 'dE0_dEa': -0.0, 'dn_dEa': 0.00025865243765703404, 'name': 'CCC(C)=O <=> C=C(O)CC'}, {'dA': 0.0, 'dE0': -0.0, 'dn': 0.0, 'dA_dEa': -0.048803153958948235, 'dE0_dEa': -0.0, 'dn_dEa': 0.0002411182143973715, 'name': 'CC=O <=> C=CO'}, {'dA': 0.003299049296856901, 'dE0': -0.0, 'dn': -3.1864297721011505e-07, 'dA_dEa': -0.33839885131218667, 'dE0_dEa': -0.0, 'dn_dEa': 0.0016721079672379333, 'name': 'SC=O <=> OC=S'}, {'dA': 0.0032997020298356798, 'dE0': -0.0, 'dn': -3.2226810707486517e-07, 'dA_dEa': -0.3293052256765712, 'dE0_dEa': -0.0, 'dn_dEa': 0.001627172990564009, 'name': 'CC(=O)S <=> CC(=S)O'}, {'dA': 0.0032983086555308542, 'dE0': -0.0, 'dn': -3.14545962045564e-07, 'dA_dEa': -0.3339838879128733, 'dE0_dEa': -0.0, 'dn_dEa': 0.0016502925099370347, 'name': 'CCC(=O)S <=> CCC(=S)O'}, {'dA': 0.0, 'dE0': -0.0, 'dn': 0.0, 'dA_dEa': -0.09223601864506342, 'dE0_dEa': -0.0, 'dn_dEa': 0.00045573490419441255, 'name': 'CCC=O <=> C=COC'}, {'dA': 0.01770369095766195, 'dE0': -0.0, 'dn': -3.0603957621067907e-07, 'dA_dEa': -3.4788918583789576, 'dE0_dEa': -0.0, 'dn_dEa': 0.017190332930880448, 'name': 'O=CNC(=O)N <=> NC(=NC=O)O'}, {'dA': 0.01769588786260296, 'dE0': -0.0, 'dn': -2.63009903133478e-07, 'dA_dEa': -2.683500442344962, 'dE0_dEa': -0.0, 'dn_dEa': 0.013260042891068233, 'name': 'O=CNC(=O)N <=> OC(=N)NC=O'}, {'dA': 0.017700268188038666, 'dE0': -0.0, 'dn': -2.872556954640979e-07, 'dA_dEa': -2.3640964741676145, 'dE0_dEa': -0.0, 'dn_dEa': 0.011681765057235288, 'name': 'O=CNC(=O)N <=> NC(=O)N=CO'}, {'dA': 0.01771047055854264, 'dE0': -0.0, 'dn': -3.436247135904968e-07, 'dA_dEa': -2.4993730674228143, 'dE0_dEa': -0.0, 'dn_dEa': 0.01235020591061931, 'name': 'NC(=O)OC=N <=> N=COC(=N)O'}, {'dA': 0.017695119623797058, 'dE0': -0.0, 'dn': -2.5902932009131913e-07, 'dA_dEa': -2.0800012623853963, 'dE0_dEa': -0.0, 'dn_dEa': 0.010277945737284556, 'name': 'O=CN1C=N1 <=> o1cnnc1'}, {'dA': 0.017706968918675688, 'dE0': -0.0, 'dn': -3.243072426237871e-07, 'dA_dEa': -2.429466833405326, 'dE0_dEa': -0.0, 'dn_dEa': 0.012004778922725877, 'name': 'NC(=O)C#C <=> OC(=N)C#C'}, {'dA': 0.01770516041688292, 'dE0': -0.0, 'dn': -3.1420555884872303e-07, 'dA_dEa': -2.786559211728297, 'dE0_dEa': -0.0, 'dn_dEa': 0.01376929555188327, 'name': 'NC(=O)N1CC1 <=> OC(=N)N1CC1'}, {'dA': 0.01771706473619101, 'dE0': -0.0, 'dn': -3.799249930838461e-07, 'dA_dEa': -2.7013618560832375, 'dE0_dEa': -0.0, 'dn_dEa': 0.013348302659171944, 'name': 'NC(=O)NC=N <=> N=CNC(=N)O'}, {'dA': 0.01769989174249726, 'dE0': -0.0, 'dn': -2.851778404197153e-07, 'dA_dEa': -2.590085823954099, 'dE0_dEa': -0.0, 'dn_dEa': 0.01279845429364837, 'name': 'O=CNC=O <=> OC=NC=O'}, {'dA': 0.017704241997764388, 'dE0': -0.0, 'dn': -3.0922743573093415e-07, 'dA_dEa': -2.4142586806592976, 'dE0_dEa': -0.0, 'dn_dEa': 0.011929631976941121, 'name': 'NC(=O)C(=O)N <=> OC(=N)C(=O)N'}, {'dA': 0.017707230654197832, 'dE0': -0.0, 'dn': -3.257071644525961e-07, 'dA_dEa': -2.0968988353333806, 'dE0_dEa': -0.0, 'dn_dEa': 0.0103614483660606, 'name': 'N=CNC=O <=> OC=NC=N'}, {'dA': 0.017715495488348228, 'dE0': -0.0, 'dn': -3.713666164069999e-07, 'dA_dEa': -3.0720668514451264, 'dE0_dEa': -0.0, 'dn_dEa': 0.015180082925410156, 'name': 'NC(=O)N <=> NC(=N)O'}, {'dA': 0.017711082222151293, 'dE0': -0.0, 'dn': -3.470068546780808e-07, 'dA_dEa': -3.816750427717318, 'dE0_dEa': -0.0, 'dn_dEa': 0.018859812796903557, 'name': 'O=CNC(=O)N <=> NC(=O)OC=N'}, {'dA': 0.017698097138920406, 'dE0': -0.0, 'dn': -2.7503812123921647e-07, 'dA_dEa': -3.207860424169338, 'dE0_dEa': -0.0, 'dn_dEa': 0.015851078105004256, 'name': 'O=CNC(=O)N <=> NC(=N)OC=O'}, {'dA': 0.01769637245274875, 'dE0': -0.0, 'dn': -2.656837374083426e-07, 'dA_dEa': -3.144616731049501, 'dE0_dEa': -0.0, 'dn_dEa': 0.015538584244886784, 'name': 'O=CNC=O <=> N=COC=O'}, {'dA': 0.017663895448551684, 'dE0': -0.0, 'dn': -8.596781490894931e-08, 'dA_dEa': -1.464487953285404, 'dE0_dEa': -0.0, 'dn_dEa': 0.007236498558259866, 'name': 'O=CN1C=N1 <=> c1ncno1'}, {'dA': 0.017711693544699432, 'dE0': -0.0, 'dn': -3.502037441866765e-07, 'dA_dEa': -3.066413511789161, 'dE0_dEa': -0.0, 'dn_dEa': 0.01515214858752212, 'name': 'O=CNC=O <=> N=COC=O'}, {'dA': 0.017704875830306395, 'dE0': -0.0, 'dn': -3.1270097124596573e-07, 'dA_dEa': -4.531190266363227, 'dE0_dEa': -0.0, 'dn_dEa': 0.02239010307337712, 'name': 'N=CNC=O <=> N=COC=N'}, {'dA': 0.017707628273912764, 'dE0': -0.0, 'dn': -3.279084293376341e-07, 'dA_dEa': -3.416324992059948, 'dE0_dEa': -0.0, 'dn_dEa': 0.0168811786747223, 'name': 'O=CN1C=C1 <=> c1ncco1'}, {'dA': 0.01773507904090561, 'dE0': -0.0, 'dn': -4.795609267083955e-07, 'dA_dEa': -8.486167744394859, 'dE0_dEa': -0.0, 'dn_dEa': 0.04193296024997934, 'name': 'O=c1cncc[nH]1 <=> N=c1cncco1'}, {'dA': 0.01770454269945016, 'dE0': -0.0, 'dn': -3.108728090610023e-07, 'dA_dEa': -3.372507138977115, 'dE0_dEa': -0.0, 'dn_dEa': 0.016664659881638493, 'name': 'N=CN1C=N1 <=> [nH]1cnnc1'}, {'dA': 0.017716609193032258, 'dE0': -0.0, 'dn': -3.776124951606121e-07, 'dA_dEa': -4.673956739282463, 'dE0_dEa': -0.0, 'dn_dEa': 0.023095554522376435, 'name': 'N=CN1C=C1 <=> c1ncc[nH]1'}, {'dA': 0.01770586959537663, 'dE0': -0.0, 'dn': -3.182018759614754e-07, 'dA_dEa': -2.2208669658996487, 'dE0_dEa': -0.0, 'dn_dEa': 0.010974016872704658, 'name': 'NC(=O)NC=N <=> NC=NC(=O)N'}, {'dA': 0.017706198093494226, 'dE0': -0.0, 'dn': -3.2003619495667116e-07, 'dA_dEa': -2.2822044677471025, 'dE0_dEa': -0.0, 'dn_dEa': 0.011277106424922086, 'name': 'N=CNC=O <=> NC=NC=O'}, {'dA': 0.01768735864971144, 'dE0': -0.0, 'dn': -2.1574885961065766e-07, 'dA_dEa': -9.71830033077588, 'dE0_dEa': -0.0, 'dn_dEa': 0.04802134261203769, 'name': '[O-]c1nncc[nH+]1 <=> [O-]C1=[N+]=CC=NN1'}, {'dA': 0.017703939874993142, 'dE0': -0.0, 'dn': -3.074359407713539e-07, 'dA_dEa': -4.8121386326164, 'dE0_dEa': -0.0, 'dn_dEa': 0.023778367908132442, 'name': 'N#CC(=N)N1C=C1 <=> N#Cc1ncc[nH]1'}, {'dA': 0.01774027387569017, 'dE0': -0.0, 'dn': -5.091428948763112e-07, 'dA_dEa': -6.362259804718197, 'dE0_dEa': -0.0, 'dn_dEa': 0.03143805099706338, 'name': 'O=c1ccnc[nH]1 <=> O=c1cc[nH]cn1'}, {'dA': 0.006411919372340686, 'dE0': -0.0, 'dn': -3.240128102766803e-07, 'dA_dEa': -2.193892901573477, 'dE0_dEa': -0.0, 'dn_dEa': 0.010840729124383018, 'name': 'OC1=CC=CC=C1 <=> O=C1C=CC=CC1'}, {'dA': 0.006430393455048742, 'dE0': -0.0, 'dn': -4.263332499804969e-07, 'dA_dEa': -3.0621886666327742, 'dE0_dEa': -0.0, 'dn_dEa': 0.015131231589297058, 'name': 'O=C1C=CCC=C1 <=> O=C1C=CC=CC1'}]
""",
)

entry(
    index = 2,
    label = "Root_1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.37447e+24,'s^-1'), n=-2.86863, w0=(682344,'J/mol'), E0=(346122,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.24783434109764116, var=169.16650822293855, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R!H-inRing',), comment="""BM rule fitted to 16 training reactions at node Root_1R!H-inRing
        Total Standard Deviation in ln(k): 26.697090843880112"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 26.697090843880112""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 26.697090843880112
sensitivities = [{'dA': -3.6169405440209066, 'dE0': -0.009678712071719374, 'dn': -0.1651243170041691, 'dA_dEa': -48.93930102983119, 'dE0_dEa': -0.05756047263099981, 'dn_dEa': -2.189088467760141, 'name': 'C2H2N2O <=> C2H2N2O-2'}, {'dA': -4.623386148388929, 'dE0': -0.012313856487759714, 'dn': -0.21015371466001517, 'dA_dEa': -8.367315881877813, 'dE0_dEa': 0.03147313220490846, 'dn_dEa': -0.3741205778537704, 'name': 'C2H2N2O-3 <=> C2H2N2O-4'}, {'dA': -4.278736523702281, 'dE0': -0.011413975882941529, 'dn': -0.19472859778972773, 'dA_dEa': -24.99135500643055, 'dE0_dEa': 0.01366029072382037, 'dn_dEa': -1.11772481635831, 'name': 'C3H3NO-3 <=> C3H3NO-4'}, {'dA': -5.9811185406395335, 'dE0': -0.015874238147050787, 'dn': -0.27088865754179603, 'dA_dEa': 53.16671915744439, 'dE0_dEa': 0.22304699735345565, 'dn_dEa': 2.3786908371072193, 'name': 'C4H4N2O <=> C4H4N2O-2'}, {'dA': -3.293304744254407, 'dE0': -0.008831219842107782, 'dn': -0.150644837760388, 'dA_dEa': -77.77207094826512, 'dE0_dEa': -0.114346561466121, 'dn_dEa': -3.478972192608641, 'name': 'C2H3N3 <=> C2H3N3-2'}, {'dA': -4.025553174230811, 'dE0': -0.0107499995676595, 'dn': -0.18340311883857238, 'dA_dEa': -44.01795465531451, 'dE0_dEa': -0.018658220254614832, 'dn_dEa': -1.9688739366930432, 'name': 'C3H4N2 <=> C3H4N2-2'}, {'dA': -3.032561652830502, 'dE0': -0.008150816581230532, 'dn': -0.1389742923468978, 'dA_dEa': -53.95256892948791, 'dE0_dEa': -0.08941174090336006, 'dn_dEa': -2.413402534912645, 'name': 'C3H3N3O <=> C3H3N3O-2'}, {'dA': -4.025566803826041, 'dE0': -0.010750032764486413, 'dn': -0.18340373380885597, 'dA_dEa': -44.589468107785216, 'dE0_dEa': -0.01864523676016518, 'dn_dEa': -1.9944050737212502, 'name': 'C4H3N3 <=> C4H3N3-2'}, {'dA': -6.086716467643032, 'dE0': -0.01615131051435528, 'dn': -0.2756119919779662, 'dA_dEa': 45.05349876931815, 'dE0_dEa': 0.18404430077186737, 'dn_dEa': 2.0157466388443344, 'name': 'C4H4N2O-3 <=> C4H4N2O-4'}, {'dA': -5.093744068681467, 'dE0': -0.013424373295068275, 'dn': -0.2290610499489094, 'dA_dEa': 6.428956283308904, 'dE0_dEa': 0.03377643902017314, 'dn_dEa': 0.2876676288018494, 'name': 'C6H6O <=> C6H6O-2'}, {'dA': -5.226444024395114, 'dE0': -0.013771478750361488, 'dn': -0.2349988797605256, 'dA_dEa': 22.027379603047887, 'dE0_dEa': 0.09253704982071771, 'dn_dEa': 0.985557740817427, 'name': 'C6H6O-3 <=> C6H6O-4'}, {'dA': -5.9843950537448105, 'dE0': -0.015882230625484522, 'dn': -0.27103644345691374, 'dA_dEa': 60.194439756201724, 'dE0_dEa': 0.2514321397875238, 'dn_dEa': 2.693173851088148, 'name': 'O=c1cncc[nH]1 <=> N=c1cncco1'}, {'dA': -3.0615656945304255, 'dE0': -0.008221429586080103, 'dn': -0.14028282442353454, 'dA_dEa': -107.19262068766015, 'dE0_dEa': -0.17360762788892828, 'dn_dEa': -4.795058902911286, 'name': '[O-]c1nncc[nH+]1 <=> [O-]C1=[N+]=CC=NN1'}, {'dA': -6.086699285327017, 'dE0': -0.01615126883581384, 'dn': -0.2756112163788343, 'dA_dEa': 48.1824385603584, 'dE0_dEa': 0.19650231353898864, 'dn_dEa': 2.155732969316519, 'name': 'O=c1ccnc[nH]1 <=> O=c1cc[nH]cn1'}, {'dA': -5.093275124750669, 'dE0': -0.013423242163629974, 'dn': -0.22903987040618973, 'dA_dEa': 11.233914057535616, 'dE0_dEa': 0.053659118454070336, 'dn_dEa': 0.5026441384563991, 'name': 'OC1=CC=CC=C1 <=> O=C1C=CC=CC1'}, {'dA': -5.2212392503540235, 'dE0': -0.013758919941336547, 'dn': -0.2347637987138681, 'dA_dEa': 21.13954041160559, 'dE0_dEa': 0.08920940402481316, 'dn_dEa': 0.9458045118824289, 'name': 'O=C1C=CCC=C1 <=> O=C1C=CC=CC1'}]
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(3.50759e-62,'s^-1'), n=22.1275, w0=(750402,'J/mol'), E0=(-20429.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8800459367924431, var=31.676078103554833, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_N-1R!H-inRing',), comment="""BM rule fitted to 56 training reactions at node Root_N-1R!H-inRing
        Total Standard Deviation in ln(k): 13.494121433083981"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 13.494121433083981""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 13.494121433083981
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 2.015830949985777, 'dn_dEa': 0.0, 'name': 'C2H2N2O-3 <=> C2H2N2O-4'}]
""",
)

entry(
    index = 4,
    label = "Root_1R!H-inRing_4R->N",
    kinetics = ArrheniusBM(A=(4.0435e+11,'s^-1'), n=1.01704, w0=(559500,'J/mol'), E0=(135903,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_4R->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->N
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->N
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': -2.2447050593188664, 'dE0': -0.00585329344817339, 'dn': -0.11399120601751939, 'dA_dEa': -49.532307230384504, 'dE0_dEa': -0.05156097990855953, 'dn_dEa': -2.4267854664793536, 'name': 'C2H2N2O <=> C2H2N2O-2'}, {'dA': -2.9659590129898987, 'dE0': -0.007671626154945403, 'dn': -0.14934647713715601, 'dA_dEa': -24.804664385587106, 'dE0_dEa': 0.019854407291015418, 'dn_dEa': -1.2152145146310465, 'name': 'C3H3NO-3 <=> C3H3NO-4'}, {'dA': -4.716235912568387, 'dE0': -0.012098471447363174, 'dn': -0.23511014308719308, 'dA_dEa': 56.89877335023313, 'dE0_dEa': 0.2312264474471428, 'dn_dEa': 2.788251247340658, 'name': 'C4H4N2O <=> C4H4N2O-2'}, {'dA': -1.9483145755148015, 'dE0': -0.005097602919550797, 'dn': -0.09948220596507468, 'dA_dEa': -79.77017616298266, 'dE0_dEa': -0.108437767140638, 'dn_dEa': -3.9085240142222393, 'name': 'C2H3N3 <=> C2H3N3-2'}, {'dA': -2.702675235802885, 'dE0': -0.007005603623327581, 'dn': -0.13644581696023664, 'dA_dEa': -44.37335245279206, 'dE0_dEa': -0.011398745999999143, 'dn_dEa': -2.173928453227851, 'name': 'C3H4N2 <=> C3H4N2-2'}, {'dA': -1.68725097006491, 'dE0': -0.004438736556095347, 'dn': -0.08668674998616649, 'dA_dEa': -54.962017232375985, 'dE0_dEa': -0.08477799605106069, 'dn_dEa': -2.69295649003937, 'name': 'C3H3N3O <=> C3H3N3O-2'}, {'dA': -2.702712391297566, 'dE0': -0.007005666624777618, 'dn': -0.13644771290282517, 'dA_dEa': -45.415399944536034, 'dE0_dEa': -0.012373369244049758, 'dn_dEa': -2.2251451533325963, 'name': 'C4H3N3 <=> C4H3N3-2'}, {'dA': -4.825616089995853, 'dE0': -0.012375291637881182, 'dn': -0.2404693844095825, 'dA_dEa': 48.1049461068874, 'dE0_dEa': 0.19053865486984833, 'dn_dEa': 2.35724136923294, 'name': 'C4H4N2O-3 <=> C4H4N2O-4'}, {'dA': -3.8065327847580406, 'dE0': -0.009667678698124918, 'dn': -0.18801474474989488, 'dA_dEa': 8.016393759896262, 'dE0_dEa': 0.03797124195108734, 'dn_dEa': 0.39277385055016745, 'name': 'C6H6O <=> C6H6O-2'}, {'dA': -3.9400301696024163, 'dE0': -0.010005363715606869, 'dn': -0.19455601613897813, 'dA_dEa': 24.38607406961337, 'dE0_dEa': 0.09799304542066571, 'dn_dEa': 1.1950460702075716, 'name': 'C6H6O-3 <=> C6H6O-4'}, {'dA': -4.715431922854472, 'dE0': -0.012096619730681312, 'dn': -0.23507033249582895, 'dA_dEa': 63.86127835092019, 'dE0_dEa': 0.259297015793244, 'dn_dEa': 3.1293657214366766, 'name': 'O=c1cncc[nH]1 <=> N=c1cncco1'}, {'dA': -1.6813717078038768, 'dE0': -0.0044248145454723956, 'dn': -0.08639647626638798, 'dA_dEa': -110.20817527204733, 'dE0_dEa': -0.16686688442333392, 'dn_dEa': -5.399792977303168, 'name': '[O-]c1nncc[nH+]1 <=> [O-]C1=[N+]=CC=NN1'}, {'dA': -4.825572985141056, 'dE0': -0.012375180451720357, 'dn': -0.2404672779328058, 'dA_dEa': 51.56619768793859, 'dE0_dEa': 0.20370605351128007, 'dn_dEa': 2.526917306294175, 'name': 'O=c1ccnc[nH]1 <=> O=c1cc[nH]cn1'}, {'dA': -3.8060441042379907, 'dE0': -0.009666528490033651, 'dn': -0.1879906029967281, 'dA_dEa': 10.904732538024355, 'dE0_dEa': 0.052839936814612395, 'dn_dEa': 0.5344179815028565, 'name': 'OC1=CC=CC=C1 <=> O=C1C=CC=CC1'}, {'dA': -3.9392484195563857, 'dE0': -0.010003513354913252, 'dn': -0.19451741194405103, 'dA_dEa': 23.37126660706703, 'dE0_dEa': 0.09440385389876174, 'dn_dEa': 1.1452302840224537, 'name': 'O=C1C=CCC=C1 <=> O=C1C=CC=CC1'}]
""",
)

entry(
    index = 5,
    label = "Root_1R!H-inRing_N-4R->N",
    kinetics = ArrheniusBM(A=(1.68103e+23,'s^-1'), n=-2.61902, w0=(690533,'J/mol'), E0=(358178,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.24185951672063075, var=131.1729658832691, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N',), comment="""BM rule fitted to 15 training reactions at node Root_1R!H-inRing_N-4R->N
        Total Standard Deviation in ln(k): 23.56807183139528"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R!H-inRing_N-4R->N
Total Standard Deviation in ln(k): 23.56807183139528""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R!H-inRing_N-4R->N
Total Standard Deviation in ln(k): 23.56807183139528
sensitivities = [{'dA': -5.909970509521341, 'dE0': -0.01369069599796727, 'dn': -0.047468936351938405, 'dA_dEa': -155.07433097069455, 'dE0_dEa': -0.10398658237598134, 'dn_dEa': -1.1856400393356603, 'name': 'C2H2N2O <=> C2H2N2O-2'}, {'dA': -8.072239382443946, 'dE0': -0.018462887321404314, 'dn': -0.0640026659085765, 'dA_dEa': -96.32910495987441, 'dE0_dEa': 0.05418244793092699, 'dn_dEa': -0.7364321795678626, 'name': 'C3H3NO-3 <=> C3H3NO-4'}, {'dA': -13.55945066032554, 'dE0': -0.030571142201149686, 'dn': -0.10596139230549198, 'dA_dEa': 105.6141250524095, 'dE0_dEa': 0.5150979560248862, 'dn_dEa': 0.8077363496065076, 'name': 'C4H4N2O <=> C4H4N2O-2'}, {'dA': -10.900707279746548, 'dE0': -0.024285142182963057, 'dn': -0.08417476217978101, 'dA_dEa': 16.691891015826304, 'dE0_dEa': 0.11845563654384476, 'dn_dEa': 0.12768019688794532, 'name': 'OC1=CC=CC=C1 <=> O=C1C=CC=CC1'}]
""",
)

entry(
    index = 6,
    label = "Root_N-1R!H-inRing_2R!H->C",
    kinetics = ArrheniusBM(A=(0.00280882,'s^-1'), n=4.73143, w0=(762750,'J/mol'), E0=(254186,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0682640946252418, var=221.53427713373026, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_2R!H->C
        Total Standard Deviation in ln(k): 30.01005001707717"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_2R!H->C
Total Standard Deviation in ln(k): 30.01005001707717""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_2R!H->C
Total Standard Deviation in ln(k): 30.01005001707717
sensitivities = [{'dA': 8.924115385185432, 'dE0': 0.02704440067591848, 'dn': 0.15256620911074004, 'dA_dEa': -178.4693558351106, 'dE0_dEa': -0.07879949637227825, 'dn_dEa': -3.2022037564917967, 'name': 'C2H2N2O <=> C2H2N2O-2'}, {'dA': 4.262110658686894, 'dE0': 0.012211814327981846, 'dn': 0.06889428288475938, 'dA_dEa': -16.636265858681, 'dE0_dEa': 0.49454759602739884, 'dn_dEa': -0.297541964564497, 'name': 'C3H3NO-3 <=> C3H3NO-4'}, {'dA': 0.5856136618689979, 'dE0': 0.0013778958501637745, 'dn': 0.007774058340797025, 'dA_dEa': 122.40018931652158, 'dE0_dEa': 0.5569010261927789, 'dn_dEa': 2.1971209508305694, 'name': 'OC1=CC=CC=C1 <=> O=C1C=CC=CC1'}]
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H-inRing_N-2R!H->C",
    kinetics = ArrheniusBM(A=(2.69879e-62,'s^-1'), n=22.1571, w0=(749452,'J/mol'), E0=(-20749.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9531070000081657, var=31.327014816049115, Tref=1000.0, N=52, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C',), comment="""BM rule fitted to 52 training reactions at node Root_N-1R!H-inRing_N-2R!H->C
        Total Standard Deviation in ln(k): 13.615351929384866"""),
    rank = 11,
    shortDesc = """BM rule fitted to 52 training reactions at node Root_N-1R!H-inRing_N-2R!H->C
Total Standard Deviation in ln(k): 13.615351929384866""",
    longDesc = 
"""
BM rule fitted to 52 training reactions at node Root_N-1R!H-inRing_N-2R!H->C
Total Standard Deviation in ln(k): 13.615351929384866
sensitivities = [{'dA': 6.837490569581249, 'dE0': 0.01971573877447082, 'dn': 0.27827244062659817, 'dA_dEa': -249.1408662763125, 'dE0_dEa': 0.15992697537355785, 'dn_dEa': -11.357471143233212, 'name': 'C3H3NO-3 <=> C3H3NO-4'}, {'dA': -2.094899708027018, 'dE0': -0.007621962934036525, 'dn': -0.10759190609074988, 'dA_dEa': 171.08262648674818, 'dE0_dEa': 0.8480813740840104, 'dn_dEa': 7.801889532266613, 'name': 'OC1=CC=CC=C1 <=> O=C1C=CC=CC1'}]
""",
)

entry(
    index = 8,
    label = "Root_1R!H-inRing_N-4R->N_2R!H->O",
    kinetics = ArrheniusBM(A=(3.40031e+71,'s^-1'), n=-16.7831, w0=(726125,'J/mol'), E0=(408378,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.8901812474716291, var=376.0091735555458, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_2R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O
        Total Standard Deviation in ln(k): 41.1103659239092"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O
Total Standard Deviation in ln(k): 41.1103659239092""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O
Total Standard Deviation in ln(k): 41.1103659239092
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.1879526364859516, 'dn_dEa': 0.0, 'name': 'OC1=CC=CC=C1 <=> O=C1C=CC=CC1'}]
""",
)

entry(
    index = 9,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O",
    kinetics = ArrheniusBM(A=(863.216,'s^-1'), n=3.33558, w0=(677591,'J/mol'), E0=(334456,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08380078001030873, var=94.54296239857095, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O',), comment="""BM rule fitted to 11 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O
        Total Standard Deviation in ln(k): 19.703236486659"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O
Total Standard Deviation in ln(k): 19.703236486659""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O
Total Standard Deviation in ln(k): 19.703236486659
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.9588580866664256, 'dn_dEa': 0.0, 'name': 'C2H2N2O <=> C2H2N2O-2'}]
""",
)

entry(
    index = 10,
    label = "Root_N-1R!H-inRing_2R!H->C_4R->C",
    kinetics = ArrheniusBM(A=(0.00257114,'s^-1'), n=4.34785, w0=(700500,'J/mol'), E0=(369438,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->C_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C_4R->C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.9398480759987256, 'dn_dEa': 0.0, 'name': 'C4H4N2O <=> C4H4N2O-2'}]
""",
)

entry(
    index = 11,
    label = "Root_N-1R!H-inRing_2R!H->C_N-4R->C",
    kinetics = ArrheniusBM(A=(256.099,'s^-1'), n=3.36485, w0=(783500,'J/mol'), E0=(223926,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.005508982678508988, var=4.333596933699633, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->C_N-4R->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->C_N-4R->C
        Total Standard Deviation in ln(k): 4.187157440959891"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->C_N-4R->C
Total Standard Deviation in ln(k): 4.187157440959891""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->C_N-4R->C
Total Standard Deviation in ln(k): 4.187157440959891
sensitivities = [{'dA': 2.4465933776068236, 'dE0': 0.006335109005386853, 'dn': -0.08991304064508847, 'dA_dEa': -118.92839589011639, 'dE0_dEa': -0.1858052919756558, 'dn_dEa': 4.575241423558726, 'name': 'C2H3N3 <=> C2H3N3-2'}, {'dA': 1.3604861126942758, 'dE0': 0.003379090163377184, 'dn': -0.04813626923291673, 'dA_dEa': -59.68639585164173, 'dE0_dEa': -0.013721460936279607, 'dn_dEa': 2.2960180502782315, 'name': 'C3H4N2 <=> C3H4N2-2'}, {'dA': 2.875082258673484, 'dE0': 0.007490412332846372, 'dn': -0.10641273657127202, 'dA_dEa': -81.69956753227947, 'dE0_dEa': -0.14210576894516755, 'dn_dEa': 3.14309808178504, 'name': 'C3H3N3O <=> C3H3N3O-2'}, {'dA': 1.34713120121092, 'dE0': 0.0033451396253050257, 'dn': -0.047618575072720756, 'dA_dEa': -60.67797507572739, 'dE0_dEa': -0.014063187112571181, 'dn_dEa': 2.3341789419693075, 'name': 'C4H3N3 <=> C4H3N3-2'}, {'dA': -1.808276423641985, 'dE0': -0.0052275206028701395, 'dn': 0.07377845424079735, 'dA_dEa': 92.76895483263958, 'dE0_dEa': 0.3532786920613963, 'dn_dEa': -3.5693327250826137, 'name': 'C4H4N2O-3 <=> C4H4N2O-4'}, {'dA': -0.24466579890794402, 'dE0': -0.0007904804489358019, 'dn': 0.01090777637144783, 'dA_dEa': 17.965317824222485, 'dE0_dEa': 0.07479865537671783, 'dn_dEa': -0.6912238071789677, 'name': 'C6H6O <=> C6H6O-2'}, {'dA': -0.49088136153146855, 'dE0': -0.001451324412717713, 'dn': 0.020393797088163163, 'dA_dEa': 49.369939652249, 'dE0_dEa': 0.1875622621815331, 'dn_dEa': -1.8995324680586725, 'name': 'C6H6O-3 <=> C6H6O-4'}, {'dA': -1.6495279996464203, 'dE0': -0.004795304677375153, 'dn': 0.06767250958001987, 'dA_dEa': 121.9346129894393, 'dE0_dEa': 0.4750468170409333, 'dn_dEa': -4.691487114305869, 'name': 'O=c1cncc[nH]1 <=> N=c1cncco1'}, {'dA': 2.8632266578195553, 'dE0': 0.007460143988817021, 'dn': -0.10595341594290758, 'dA_dEa': -168.481775678928, 'dE0_dEa': -0.29304199853964286, 'dn_dEa': 6.4816342756442005, 'name': '[O-]c1nncc[nH+]1 <=> [O-]C1=[N+]=CC=NN1'}, {'dA': -1.796174723280173, 'dE0': -0.00519672267696874, 'dn': 0.07330940023793212, 'dA_dEa': 98.68113188932192, 'dE0_dEa': 0.3758855996144095, 'dn_dEa': -3.7967834885187357, 'name': 'O=c1ccnc[nH]1 <=> O=c1cc[nH]cn1'}, {'dA': -0.4449908072814914, 'dE0': -0.0013344659954714977, 'dn': 0.018615266218388243, 'dA_dEa': 47.856158452481644, 'dE0_dEa': 0.18190204405650764, 'dn_dEa': -1.841269897495439, 'name': 'O=C1C=CCC=C1 <=> O=C1C=CC=CC1'}]
""",
)

entry(
    index = 12,
    label = "Root_N-1R!H-inRing_N-2R!H->C_3R!H->C",
    kinetics = ArrheniusBM(A=(0.0954007,'s^-1'), n=3.97882, w0=(762750,'J/mol'), E0=(250868,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05104117971660031, var=160.05464641490252, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_3R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C
        Total Standard Deviation in ln(k): 25.490690006267023"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C
Total Standard Deviation in ln(k): 25.490690006267023""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C
Total Standard Deviation in ln(k): 25.490690006267023
sensitivities = [{'dA': 4.366249947850545, 'dE0': 0.14804654465314213, 'dn': -0.012429996253136653, 'dA_dEa': -113.15291017684895, 'dE0_dEa': -2.154139584138863, 'dn_dEa': 0.3373842405655265, 'name': 'C3H3N3O <=> C3H3N3O-2'}, {'dA': 0.3615931849481456, 'dE0': 0.005785197803046545, 'dn': -0.0004920868081141751, 'dA_dEa': -8.883886037893786, 'dE0_dEa': 2.051175153340332, 'dn_dEa': 0.026575405422191094, 'name': 'C4H4N2O-3 <=> C4H4N2O-4'}, {'dA': 1.6496975164843204, 'dE0': 0.056016915112672684, 'dn': -0.0047073080560694576, 'dA_dEa': -10.585239001956126, 'dE0_dEa': 0.23151115528228047, 'dn_dEa': 0.03158024147198709, 'name': 'C6H6O <=> C6H6O-2'}, {'dA': 1.2794669851247409, 'dE0': 0.042863217192720494, 'dn': -0.003603664147597353, 'dA_dEa': -3.5523326175170316, 'dE0_dEa': 1.1230438383662977, 'dn_dEa': 0.010639244791671583, 'name': 'C6H6O-3 <=> C6H6O-4'}, {'dA': 4.366190014252905, 'dE0': 0.1480461808291028, 'dn': -0.01242979970891143, 'dA_dEa': -231.81485722275562, 'dE0_dEa': -4.386899254988812, 'dn_dEa': 0.6911933490613243, 'name': '[O-]c1nncc[nH+]1 <=> [O-]C1=[N+]=CC=NN1'}, {'dA': 0.3616672287876498, 'dE0': 0.005789186510598587, 'dn': -0.0004922938970898182, 'dA_dEa': -9.540001710207575, 'dE0_dEa': 2.180609416852659, 'dn_dEa': 0.028538130053572, 'name': 'O=c1ccnc[nH]1 <=> O=c1cc[nH]cn1'}, {'dA': 1.2791553965031697, 'dE0': 0.0428536908832026, 'dn': -0.0036027204432204024, 'dA_dEa': -3.3990520667547677, 'dE0_dEa': 1.0920488183508812, 'dn_dEa': 0.010181017663872402, 'name': 'O=C1C=CCC=C1 <=> O=C1C=CC=CC1'}]
""",
)

entry(
    index = 13,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C",
    kinetics = ArrheniusBM(A=(1.19221e-62,'s^-1'), n=22.2718, w0=(748344,'J/mol'), E0=(-21081.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9949489040724094, var=31.03257203316843, Tref=1000.0, N=48, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C',), comment="""BM rule fitted to 48 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C
        Total Standard Deviation in ln(k): 13.66762655979622"""),
    rank = 11,
    shortDesc = """BM rule fitted to 48 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C
Total Standard Deviation in ln(k): 13.66762655979622""",
    longDesc = 
"""
BM rule fitted to 48 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C
Total Standard Deviation in ln(k): 13.66762655979622
sensitivities = [{'dA': 3.531054010011692, 'dE0': 0.07802728725515928, 'dn': -0.010046226204302604, 'dA_dEa': -222.98136423810502, 'dE0_dEa': -3.7348869917424814, 'dn_dEa': 0.6819345760427984, 'name': 'C3H3N3O <=> C3H3N3O-2'}, {'dA': -4.3305906144160184, 'dE0': -0.1082627248184822, 'dn': 0.013994479283532138, 'dA_dEa': -13.113439988275411, 'dE0_dEa': 1.6550998893056397, 'dn_dEa': 0.0401844630106965, 'name': 'C4H4N2O-3 <=> C4H4N2O-4'}, {'dA': -2.674836520782559, 'dE0': -0.06531333374732211, 'dn': 0.00845177356521384, 'dA_dEa': -17.553993246339928, 'dE0_dEa': 0.08864885878348945, 'dn_dEa': 0.05370352062554979, 'name': 'C6H6O <=> C6H6O-2'}, {'dA': -3.1913892648848434, 'dE0': -0.07755139563880052, 'dn': 0.010031412855454518, 'dA_dEa': -8.117693770089756, 'dE0_dEa': 0.8187042571633018, 'dn_dEa': 0.02446019038995066, 'name': 'C6H6O-3 <=> C6H6O-4'}, {'dA': -4.330645324501369, 'dE0': -0.10826473561830796, 'dn': 0.013994635129388582, 'dA_dEa': -13.802556422548761, 'dE0_dEa': 1.7656845169764275, 'dn_dEa': 0.04229896140630681, 'name': 'O=c1ccnc[nH]1 <=> O=c1cc[nH]cn1'}, {'dA': -3.190875573182335, 'dE0': -0.07754264176419896, 'dn': 0.010029789467553667, 'dA_dEa': -7.9103463374971925, 'dE0_dEa': 0.7934254912046643, 'dn_dEa': 0.023826150724667986, 'name': 'O=C1C=CCC=C1 <=> O=C1C=CC=CC1'}]
""",
)

entry(
    index = 14,
    label = "Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing",
    kinetics = ArrheniusBM(A=(2.70002e+39,'s^-1'), n=-7.1515, w0=(732500,'J/mol'), E0=(288782,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24763149641243207, var=87.79679561687634, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing
        Total Standard Deviation in ln(k): 19.40654619814221"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing
Total Standard Deviation in ln(k): 19.40654619814221""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing
Total Standard Deviation in ln(k): 19.40654619814221
sensitivities = [{'dA': 0.4992857639579124, 'dE0': -1.1051750506325491e-06, 'dn': 3.989304333512819e-05, 'dA_dEa': 0.006834890793783941, 'dE0_dEa': 0.5074960276555704, 'dn_dEa': -0.0005077896083967209, 'name': 'C6H6O-3 <=> C6H6O-4'}, {'dA': 0.499285655280401, 'dE0': -1.1050905477702614e-06, 'dn': 3.9904221016273604e-05, 'dA_dEa': 0.006994879878875142, 'dE0_dEa': 0.4926863856079571, 'dn_dEa': -0.0005248129131170938, 'name': 'O=C1C=CCC=C1 <=> O=C1C=CC=CC1'}]
""",
)

entry(
    index = 15,
    label = "Root_1R!H-inRing_N-4R->N_2R!H->O_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(2.1761e+10,'s^-1'), n=0.996245, w0=(707000,'J/mol'), E0=(405481,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_2R!H->O_N-3R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_N-3R!H-inRing
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_N-3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_N-3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.0110274257747558, 'dn_dEa': 0.0, 'name': 'C6H6O-3 <=> C6H6O-4'}]
""",
)

entry(
    index = 16,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R",
    kinetics = ArrheniusBM(A=(6.42898e-133,'s^-1'), n=43.0224, w0=(700214,'J/mol'), E0=(42887.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.3589376793601295, var=69.21003957276957, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R
        Total Standard Deviation in ln(k): 22.604885725751753"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R
Total Standard Deviation in ln(k): 22.604885725751753""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R
Total Standard Deviation in ln(k): 22.604885725751753
sensitivities = [{'dA': 0.2980220867243916, 'dE0': -0.0, 'dn': -1.7878528240390847e-06, 'dA_dEa': -79.39842608232958, 'dE0_dEa': -0.0, 'dn_dEa': 0.2344808823884186, 'name': 'C3H3N3O <=> C3H3N3O-2'}, {'dA': 0.2980249042821343, 'dE0': -0.0, 'dn': -1.7971419097295552e-06, 'dA_dEa': -100.73964467143215, 'dE0_dEa': -0.0, 'dn_dEa': 0.29750618046333555, 'name': 'C4H4N2O-3 <=> C4H4N2O-4'}, {'dA': 0.10761639271096377, 'dE0': -0.0, 'dn': -1.7062943245962708e-06, 'dA_dEa': -25.84988161447939, 'dE0_dEa': -0.0, 'dn_dEa': 0.07634025270753336, 'name': 'C6H6O <=> C6H6O-2'}, {'dA': 0.2980192738846527, 'dE0': -0.0, 'dn': -1.7785665185327114e-06, 'dA_dEa': -107.23789037082314, 'dE0_dEa': -0.0, 'dn_dEa': 0.3166969642011079, 'name': 'O=c1ccnc[nH]1 <=> O=c1cc[nH]cn1'}]
""",
)

entry(
    index = 17,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C",
    kinetics = ArrheniusBM(A=(3.18179e+39,'s^-1'), n=-7.17225, w0=(645667,'J/mol'), E0=(415609,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.42262730356938655, var=78.72060767182978, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C
        Total Standard Deviation in ln(k): 18.84881634829919"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C
Total Standard Deviation in ln(k): 18.84881634829919""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C
Total Standard Deviation in ln(k): 18.84881634829919
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.843952995869635, 'dn_dEa': 0.0, 'name': 'C6H6O <=> C6H6O-2'}]
""",
)

entry(
    index = 18,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(6.1544e+10,'s^-1'), n=1.34775, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_N-5R!H->C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.3356495514595196, 'dE0': -0.0, 'dn': -8.124738339367253e-06, 'dA_dEa': -88.92770656815243, 'dE0_dEa': -0.0, 'dn_dEa': 0.2597687935824369, 'name': 'C3H3N3O <=> C3H3N3O-2'}, {'dA': 0.33561058273793665, 'dE0': -0.0, 'dn': -7.997248363549294e-06, 'dA_dEa': -112.82665943549651, 'dE0_dEa': -0.0, 'dn_dEa': 0.32957934825767, 'name': 'C4H4N2O-3 <=> C4H4N2O-4'}, {'dA': 0.3356474746283681, 'dE0': -0.0, 'dn': -8.118015646531023e-06, 'dA_dEa': -120.11205049726827, 'dE0_dEa': -0.0, 'dn_dEa': 0.3508634703106322, 'name': 'O=c1ccnc[nH]1 <=> O=c1cc[nH]cn1'}]
""",
)

entry(
    index = 19,
    label = "Root_N-1R!H-inRing_2R!H->C_N-4R->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(28.6641,'s^-1'), n=3.55793, w0=(783500,'J/mol'), E0=(211066,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->C_N-4R->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C_N-4R->C_Ext-1R!H-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C_N-4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C_N-4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.9738250554978112, 'dn_dEa': 0.0, 'name': 'C4H4N2O-3 <=> C4H4N2O-4'}]
""",
)

entry(
    index = 20,
    label = "Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_4R->C",
    kinetics = ArrheniusBM(A=(7040,'s^-1'), n=2.66, w0=(700500,'J/mol'), E0=(384026,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_4R->C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.7072523494053203, 'dn_dEa': 0.0, 'name': 'C3H3N3O <=> C3H3N3O-2'}]
""",
)

entry(
    index = 21,
    label = "Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_N-4R->C",
    kinetics = ArrheniusBM(A=(635.413,'s^-1'), n=2.83859, w0=(783500,'J/mol'), E0=(219488,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0012207818220425905, var=12.527101437509526, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_N-4R->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_N-4R->C
        Total Standard Deviation in ln(k): 7.098555561663242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_N-4R->C
Total Standard Deviation in ln(k): 7.098555561663242""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_N-4R->C
Total Standard Deviation in ln(k): 7.098555561663242
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.4853469186556836, 'dn_dEa': 0.0, 'name': '[O-]c1nncc[nH+]1 <=> [O-]C1=[N+]=CC=NN1'}]
""",
)

entry(
    index = 22,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N",
    kinetics = ArrheniusBM(A=(3.76721e-56,'s^-1'), n=20.4354, w0=(727519,'J/mol'), E0=(-33116.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.8731427039737816, var=23.68673873026742, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N',), comment="""BM rule fitted to 26 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N
        Total Standard Deviation in ln(k): 19.488364241519903"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N
Total Standard Deviation in ln(k): 19.488364241519903""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N
Total Standard Deviation in ln(k): 19.488364241519903
sensitivities = [{'dA': 0.17968637151002145, 'dE0': -0.0003326234103498262, 'dn': -0.0027475511857952555, 'dA_dEa': -168.48379798191084, 'dE0_dEa': -0.006834974192518923, 'dn_dEa': -3.014136562080861, 'name': 'C3H4N2 <=> C3H4N2-2'}, {'dA': 0.17922430706109635, 'dE0': -0.00033360450530269057, 'dn': -0.0027558378211315223, 'dA_dEa': -171.2087854465711, 'dE0_dEa': -0.007069619196503407, 'dn_dEa': -3.062903022445808, 'name': 'C4H3N3 <=> C4H3N3-2'}, {'dA': -7.7831664743266105, 'dE0': -0.017668231631963006, 'dn': -0.14521627180065533, 'dA_dEa': 266.2464956190016, 'dE0_dEa': 0.9283142413156709, 'dn_dEa': 4.763976382458178, 'name': 'O=c1cncc[nH]1 <=> N=c1cncco1'}]
""",
)

entry(
    index = 23,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N",
    kinetics = ArrheniusBM(A=(1.90425e-05,'s^-1'), n=5.18692, w0=(772955,'J/mol'), E0=(109729,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013830948589540256, var=7.224049258643255, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N
        Total Standard Deviation in ln(k): 5.422996178518286"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N
Total Standard Deviation in ln(k): 5.422996178518286""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N
Total Standard Deviation in ln(k): 5.422996178518286
sensitivities = [{'dA': 3.6942151546388207, 'dE0': 0.0067070916751061195, 'dn': 0.057882718795524944, 'dA_dEa': -348.45347790880083, 'dE0_dEa': -0.2024526883761982, 'dn_dEa': -6.314161580210696, 'name': 'C4H3N3 <=> C4H3N3-2'}, {'dA': -7.595307041484871, 'dE0': -0.01697524245218517, 'dn': -0.14670199582812785, 'dA_dEa': 278.06303860295367, 'dE0_dEa': 1.0873486030458341, 'dn_dEa': 5.039379343377773, 'name': 'O=c1cncc[nH]1 <=> N=c1cncco1'}]
""",
)

entry(
    index = 24,
    label = "Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.32322e+24,'s^-1'), n=-2.81453, w0=(745250,'J/mol'), E0=(282167,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.4915944114598476, var=57.075019008093854, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_5R!H->C
        Total Standard Deviation in ln(k): 21.40566214731623"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_5R!H->C
Total Standard Deviation in ln(k): 21.40566214731623""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_5R!H->C
Total Standard Deviation in ln(k): 21.40566214731623
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.0665208181448242, 'dn_dEa': 0.0, 'name': 'O=c1cncc[nH]1 <=> N=c1cncco1'}]
""",
)

entry(
    index = 25,
    label = "Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.23584e+11,'s^-1'), n=1.27308, w0=(707000,'J/mol'), E0=(183610,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_N-5R!H->C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.404892745179493, 'dn_dEa': 0.0, 'name': 'C4H3N3 <=> C4H3N3-2'}]
""",
)

entry(
    index = 26,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN",
    kinetics = ArrheniusBM(A=(3.35262e-129,'s^-1'), n=41.9454, w0=(700917,'J/mol'), E0=(51012.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.36255197685948554, var=131.25054790841853, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN
        Total Standard Deviation in ln(k): 23.8781081550003"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN
Total Standard Deviation in ln(k): 23.8781081550003""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN
Total Standard Deviation in ln(k): 23.8781081550003
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H3N3 <=> C2H3N3-2'}]
""",
)

entry(
    index = 27,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_N-Sp-5R!H-2CN",
    kinetics = ArrheniusBM(A=(8.16507e-20,'s^-1'), n=9.4016, w0=(696000,'J/mol'), E0=(345895,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_N-Sp-5R!H-2CN',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_N-Sp-5R!H-2CN
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_N-Sp-5R!H-2CN
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_N-Sp-5R!H-2CN
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': -8.982374311018328e-05, 'dE0': -0.0, 'dn': 1.9770579195631876e-06, 'dA_dEa': -0.06309610409972051, 'dE0_dEa': -0.0, 'dn_dEa': 0.00036581137336034065, 'name': 'C2H4O <=> C2H4O-2'}, {'dA': -8.947711194197003e-05, 'dE0': -0.0, 'dn': 1.9748061369378467e-06, 'dA_dEa': -0.061591307598980585, 'dE0_dEa': -0.0, 'dn_dEa': 0.0003570857511723099, 'name': 'C4H8O <=> C4H8O-2'}, {'dA': 0.0, 'dE0': -0.0, 'dn': 0.0, 'dA_dEa': -0.06159034219877636, 'dE0_dEa': -0.0, 'dn_dEa': 0.0003570794813771049, 'name': 'C2H4O <=> C2H4O-2'}, {'dA': 0.003895163700918121, 'dE0': -0.0, 'dn': 1.9741670828271183e-06, 'dA_dEa': -0.4013002775309802, 'dE0_dEa': -0.0, 'dn_dEa': 0.0023270693062445672, 'name': 'CH2OS <=> CH2OS-2'}, {'dA': 0.003895819503441518, 'dE0': -0.0, 'dn': 1.969911432035473e-06, 'dA_dEa': -0.3940728575458231, 'dE0_dEa': -0.0, 'dn_dEa': 0.002285157757106144, 'name': 'C2H4OS <=> C2H4OS-2'}, {'dA': 0.003894282002648171, 'dE0': -0.0, 'dn': 1.979894806002472e-06, 'dA_dEa': -0.3940731782563923, 'dE0_dEa': -0.0, 'dn_dEa': 0.0022851598406152243, 'name': 'C3H6OS <=> C3H6OS-2'}, {'dA': 0.0, 'dE0': -0.0, 'dn': 0.0, 'dA_dEa': -0.10576125845319694, 'dE0_dEa': -0.0, 'dn_dEa': 0.0006132285582208641, 'name': 'C3H6O <=> C3H6O-2'}, {'dA': 0.02280140759580969, 'dE0': -0.0, 'dn': 1.8667873665270239e-06, 'dA_dEa': -2.4696181289416916, 'dE0_dEa': -0.0, 'dn_dEa': 0.014321311609054376, 'name': 'C2H4N2O2 <=> C2H4N2O2-2'}, {'dA': 0.022788110356944124, 'dE0': -0.0, 'dn': 1.9529846869855e-06, 'dA_dEa': -1.8679188980004038, 'dE0_dEa': -0.0, 'dn_dEa': 0.01083204280039272, 'name': 'C2H4N2O2-3 <=> C2H4N2O2-4'}, {'dA': 0.02278028404134853, 'dE0': -0.0, 'dn': 2.0037875619921046e-06, 'dA_dEa': -2.111081465244757, 'dE0_dEa': -0.0, 'dn_dEa': 0.012242154226503392, 'name': 'C2H4N2O2-5 <=> C2H4N2O2-6'}, {'dA': 0.022798192418352084, 'dE0': -0.0, 'dn': 1.8875646534436754e-06, 'dA_dEa': -1.8440103464174384, 'dE0_dEa': -0.0, 'dn_dEa': 0.010693393922875511, 'name': 'C2H4N2O2-7 <=> C2H4N2O2-8'}, {'dA': 0.022774724499188558, 'dE0': -0.0, 'dn': 2.0398761358160054e-06, 'dA_dEa': -1.9303646423909264, 'dE0_dEa': -0.0, 'dn_dEa': 0.011194167766351501, 'name': 'C3H3NO <=> C3H3NO-2'}, {'dA': 0.022780414013825755, 'dE0': -0.0, 'dn': 2.0030131504403354e-06, 'dA_dEa': -1.9337285304745675, 'dE0_dEa': -0.0, 'dn_dEa': 0.011213674293526703, 'name': 'C3H6N2O <=> C3H6N2O-2'}, {'dA': 0.022782746611940418, 'dE0': -0.0, 'dn': 1.9877116580810142e-06, 'dA_dEa': -1.7763641264141052, 'dE0_dEa': -0.0, 'dn_dEa': 0.010301115604890006, 'name': 'C2H5N3O <=> C2H5N3O-2'}, {'dA': 0.022794002859430076, 'dE0': -0.0, 'dn': 1.9146855960906443e-06, 'dA_dEa': -1.8857084662331347, 'dE0_dEa': -0.0, 'dn_dEa': 0.010935205544731503, 'name': 'C2H3NO2 <=> C2H3NO2-2'}, {'dA': 0.022787277032423624, 'dE0': -0.0, 'dn': 1.958352099250182e-06, 'dA_dEa': -1.9623138931594781, 'dE0_dEa': -0.0, 'dn_dEa': 0.011379446209242439, 'name': 'C2H4N2O2-9 <=> C2H4N2O2-10'}, {'dA': 0.022787976433849288, 'dE0': -0.0, 'dn': 1.953861058175539e-06, 'dA_dEa': -1.909728414148259, 'dE0_dEa': -0.0, 'dn_dEa': 0.011074497984259983, 'name': 'C2H4N2O <=> C2H4N2O-2'}, {'dA': 0.022784913852549615, 'dE0': -0.0, 'dn': 1.973723598542236e-06, 'dA_dEa': -1.8004658194288077, 'dE0_dEa': -0.0, 'dn_dEa': 0.010440880835917566, 'name': 'CH4N2O <=> CH4N2O-2'}, {'dA': 0.02278700586089395, 'dE0': -0.0, 'dn': 1.9601645723159866e-06, 'dA_dEa': -3.391161970910535, 'dE0_dEa': -0.0, 'dn_dEa': 0.019665395071438493, 'name': 'C2H4N2O2-11 <=> C2H4N2O2-12'}, {'dA': 0.022781135442076227, 'dE0': -0.0, 'dn': 1.998269377915872e-06, 'dA_dEa': -2.3433740782652728, 'dE0_dEa': -0.0, 'dn_dEa': 0.013589225613614492, 'name': 'C2H4N2O2-13 <=> C2H4N2O2-14'}, {'dA': 0.022778748046905783, 'dE0': -0.0, 'dn': 2.0137760740826077e-06, 'dA_dEa': -2.707282028410716, 'dE0_dEa': -0.0, 'dn_dEa': 0.015699543600393745, 'name': 'C2H3NO2-3 <=> C2H3NO2-4'}, {'dA': 0.022785742203270964, 'dE0': -0.0, 'dn': 1.9683486396586585e-06, 'dA_dEa': -2.604752267132258, 'dE0_dEa': -0.0, 'dn_dEa': 0.015104963300569978, 'name': 'C2H3NO2-3 <=> C2H3NO2-4'}, {'dA': 0.022836010401763602, 'dE0': -0.0, 'dn': 1.6415172600353056e-06, 'dA_dEa': -4.143872099121383, 'dE0_dEa': -0.0, 'dn_dEa': 0.024030368938117844, 'name': 'C2H4N2O-3 <=> C2H4N2O-4'}, {'dA': 0.022790932632690563, 'dE0': -0.0, 'dn': 1.9346223181154205e-06, 'dA_dEa': -2.992802530684787, 'dE0_dEa': -0.0, 'dn_dEa': 0.01735528115512186, 'name': 'C2H5N3O-3 <=> C2H5N3O-4'}, {'dA': 0.022780998818918995, 'dE0': -0.0, 'dn': 1.999132261531715e-06, 'dA_dEa': -2.551565277997551, 'dE0_dEa': -0.0, 'dn_dEa': 0.014796531845967053, 'name': 'C2H4N2O-5 <=> C2H4N2O-6'}, {'dA': -8.936368089963327e-05, 'dE0': -0.0, 'dn': 1.9740710641441493e-06, 'dA_dEa': -0.0659244541338994, 'dE0_dEa': -0.0, 'dn_dEa': 0.00038221332926194584, 'name': 'CC=O <=> C=CO'}, {'dA': -8.918294724936532e-05, 'dE0': -0.0, 'dn': 1.9728941127291645e-06, 'dA_dEa': -0.06907140516433025, 'dE0_dEa': -0.0, 'dn_dEa': 0.00040046289833769446, 'name': 'CCC(C)=O <=> C=C(O)CC'}, {'dA': -8.938772566581139e-05, 'dE0': -0.0, 'dn': 1.974223923318374e-06, 'dA_dEa': -0.06441896309184612, 'dE0_dEa': -0.0, 'dn_dEa': 0.0003734831962831782, 'name': 'CC=O <=> C=CO'}, {'dA': 0.0038948919893759663, 'dE0': -0.0, 'dn': 1.975925926728857e-06, 'dA_dEa': -0.44412427982370334, 'dE0_dEa': -0.0, 'dn_dEa': 0.002575407857966613, 'name': 'SC=O <=> OC=S'}, {'dA': 0.0038952814236385817, 'dE0': -0.0, 'dn': 1.973402305256917e-06, 'dA_dEa': -0.4322010928774965, 'dE0_dEa': -0.0, 'dn_dEa': 0.002506264393953194, 'name': 'CC(=O)S <=> CC(=S)O'}, {'dA': 0.0038950028908861637, 'dE0': -0.0, 'dn': 1.9752115669955326e-06, 'dA_dEa': -0.43833463357150604, 'dE0_dEa': -0.0, 'dn_dEa': 0.0025418334060271263, 'name': 'CCC(=O)S <=> CCC(=S)O'}, {'dA': -8.798753015072239e-05, 'dE0': -0.0, 'dn': 1.965129605283813e-06, 'dA_dEa': -0.12136494353855114, 'dE0_dEa': -0.0, 'dn_dEa': 0.0007037145118885852, 'name': 'CCC=O <=> C=COC'}, {'dA': 0.02280179623426444, 'dE0': -0.0, 'dn': 1.8636731819849185e-06, 'dA_dEa': -4.561806863904897, 'dE0_dEa': -0.0, 'dn_dEa': 0.026453987269506516, 'name': 'O=CNC(=O)N <=> NC(=NC=O)O'}, {'dA': 0.02278695097857304, 'dE0': -0.0, 'dn': 1.960506257528959e-06, 'dA_dEa': -3.51892194891018, 'dE0_dEa': -0.0, 'dn_dEa': 0.020406269181654085, 'name': 'O=CNC(=O)N <=> OC(=N)NC=O'}, {'dA': 0.02278577127867971, 'dE0': -0.0, 'dn': 1.9682381700033367e-06, 'dA_dEa': -3.1001250459613634, 'dE0_dEa': -0.0, 'dn_dEa': 0.01797765270995936, 'name': 'O=CNC(=O)N <=> NC(=O)N=CO'}, {'dA': 0.022777363227535496, 'dE0': -0.0, 'dn': 2.0227123948194413e-06, 'dA_dEa': -3.277506558362481, 'dE0_dEa': -0.0, 'dn_dEa': 0.019006293372912646, 'name': 'NC(=O)OC=N <=> N=COC(=N)O'}, {'dA': 0.022799831413069807, 'dE0': -0.0, 'dn': 1.8769253658982022e-06, 'dA_dEa': -2.727634838976501, 'dE0_dEa': -0.0, 'dn_dEa': 0.015817556399473482, 'name': 'O=CN1C=N1 <=> o1cnnc1'}, {'dA': 0.02278521796484052, 'dE0': -0.0, 'dn': 1.97175714233769e-06, 'dA_dEa': -3.185839976140765, 'dE0_dEa': -0.0, 'dn_dEa': 0.01847471467876408, 'name': 'NC(=O)C#C <=> OC(=N)C#C'}, {'dA': 0.02278504229025453, 'dE0': -0.0, 'dn': 1.9728917042337724e-06, 'dA_dEa': -3.654038904841575, 'dE0_dEa': -0.0, 'dn_dEa': 0.02118981794435287, 'name': 'NC(=O)N1CC1 <=> OC(=N)N1CC1'}, {'dA': 0.02279271274119561, 'dE0': -0.0, 'dn': 1.9231445530407452e-06, 'dA_dEa': -3.542330107535853, 'dE0_dEa': -0.0, 'dn_dEa': 0.020542007175404105, 'name': 'NC(=O)NC=N <=> N=CNC(=N)O'}, {'dA': 0.022788901759443213, 'dE0': -0.0, 'dn': 1.947854912932848e-06, 'dA_dEa': -3.3964312147819884, 'dE0_dEa': -0.0, 'dn_dEa': 0.019695941577421883, 'name': 'O=CNC=O <=> OC=NC=O'}, {'dA': 0.0227858875803147, 'dE0': -0.0, 'dn': 1.9673953571824284e-06, 'dA_dEa': -3.165896009307183, 'dE0_dEa': -0.0, 'dn_dEa': 0.01835905887646749, 'name': 'NC(=O)C(=O)N <=> OC(=N)C(=O)N'}, {'dA': 0.022785149468520793, 'dE0': -0.0, 'dn': 1.972189386977409e-06, 'dA_dEa': -2.7497922146440787, 'dE0_dEa': -0.0, 'dn_dEa': 0.01594605840600702, 'name': 'N=CNC=O <=> OC=NC=N'}, {'dA': 0.02279399262761468, 'dE0': -0.0, 'dn': 1.914710483876364e-06, 'dA_dEa': -4.028378314246073, 'dE0_dEa': -0.0, 'dn_dEa': 0.023360618694753636, 'name': 'NC(=O)N <=> NC(=N)O'}, {'dA': 0.022786632172258358, 'dE0': -0.0, 'dn': 1.9625931385031146e-06, 'dA_dEa': -5.004789410805285, 'dE0_dEa': -0.0, 'dn_dEa': 0.029022867993366668, 'name': 'O=CNC(=O)N <=> NC(=O)OC=N'}, {'dA': 0.0227831986308072, 'dE0': -0.0, 'dn': 1.9847036079025245e-06, 'dA_dEa': -4.206449085643735, 'dE0_dEa': -0.0, 'dn_dEa': 0.024393263909526928, 'name': 'O=CNC(=O)N <=> NC(=N)OC=O'}, {'dA': 0.02278142224554609, 'dE0': -0.0, 'dn': 1.99640343625236e-06, 'dA_dEa': -4.12349117530698, 'dE0_dEa': -0.0, 'dn_dEa': 0.02391218620459495, 'name': 'O=CNC=O <=> N=COC=O'}, {'dA': 0.02277584809462747, 'dE0': -0.0, 'dn': 2.032654824364773e-06, 'dA_dEa': -1.9206161260287742, 'dE0_dEa': -0.0, 'dn_dEa': 0.011137653403997548, 'name': 'O=CN1C=N1 <=> c1ncno1'}, {'dA': 0.022763214246881724, 'dE0': -0.0, 'dn': 2.114438015034797e-06, 'dA_dEa': -4.020975969638573, 'dE0_dEa': -0.0, 'dn_dEa': 0.023317700272029146, 'name': 'O=CNC=O <=> N=COC=O'}, {'dA': 0.0227881600096705, 'dE0': -0.0, 'dn': 1.9526377030826643e-06, 'dA_dEa': -5.941515263487617, 'dE0_dEa': -0.0, 'dn_dEa': 0.03445496723583121, 'name': 'N=CNC=O <=> N=COC=N'}, {'dA': 0.02278314127579757, 'dE0': -0.0, 'dn': 1.985215654022905e-06, 'dA_dEa': -4.479761521111452, 'dE0_dEa': -0.0, 'dn_dEa': 0.025978211483908553, 'name': 'O=CN1C=C1 <=> c1ncco1'}, {'dA': 0.022781461922252454, 'dE0': -0.0, 'dn': 1.9961381806265e-06, 'dA_dEa': -4.42231295261357, 'dE0_dEa': -0.0, 'dn_dEa': 0.025645067511080522, 'name': 'N=CN1C=N1 <=> [nH]1cnnc1'}, {'dA': 0.022793641534238088, 'dE0': -0.0, 'dn': 1.917138728930773e-06, 'dA_dEa': -6.128710480084685, 'dE0_dEa': -0.0, 'dn_dEa': 0.03554051424697486, 'name': 'N=CN1C=C1 <=> c1ncc[nH]1'}, {'dA': 0.022784010781154173, 'dE0': -0.0, 'dn': 1.979594386343886e-06, 'dA_dEa': -2.9123310945070466, 'dE0_dEa': -0.0, 'dn_dEa': 0.016888625745391243, 'name': 'NC(=O)NC=N <=> NC=NC(=O)N'}, {'dA': 0.02278607075823198, 'dE0': -0.0, 'dn': 1.9662066844232014e-06, 'dA_dEa': -2.992755201831062, 'dE0_dEa': -0.0, 'dn_dEa': 0.017355009239524544, 'name': 'N=CNC=O <=> NC=NC=O'}, {'dA': 0.0227549116687012, 'dE0': -0.0, 'dn': 2.168533945507968e-06, 'dA_dEa': -6.309895989262044, 'dE0_dEa': -0.0, 'dn_dEa': 0.036591236245043325, 'name': 'N#CC(=N)N1C=C1 <=> N#Cc1ncc[nH]1'}]
""",
)

entry(
    index = 28,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.15835e+39,'s^-1'), n=-7.08112, w0=(661000,'J/mol'), E0=(428856,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10039660117628249, var=202.96872295848286, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R
        Total Standard Deviation in ln(k): 28.81313043246121"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 28.81313043246121""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 28.81313043246121
sensitivities = [{'dA': 1.262736237924639, 'dE0': 0.0036647045991987453, 'dn': -0.02570973351148321, 'dA_dEa': 14.86952485454815, 'dE0_dEa': 0.27703199734106565, 'dn_dEa': -0.37756675689732705, 'name': 'CC=O <=> C=CO'}, {'dA': 1.378807462517325, 'dE0': 0.004093541056616838, 'dn': -0.02864869846791915, 'dA_dEa': 10.168909215214637, 'dE0_dEa': 0.27071201039695836, 'dn_dEa': -0.25827645555844414, 'name': 'CCC(C)=O <=> C=C(O)CC'}, {'dA': 1.2465086837833135, 'dE0': 0.003609358537779153, 'dn': -0.025295053494006615, 'dA_dEa': 14.556918223449783, 'dE0_dEa': 0.2707721736746316, 'dn_dEa': -0.3696305154450016, 'name': 'CC=O <=> C=CO'}, {'dA': 2.2618655428525973, 'dE0': 0.007254941698651373, 'dn': -0.05109124017491928, 'dA_dEa': -25.146800929502717, 'dE0_dEa': 0.3209051375370613, 'dn_dEa': 0.6379965502235262, 'name': 'CCC=O <=> C=COC'}]
""",
)

entry(
    index = 29,
    label = "Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_N-4R->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(205000,'s^-1'), n=2.37, w0=(783500,'J/mol'), E0=(221387,'J/mol'), Tmin=(600,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_N-4R->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_N-4R->C_Ext-1R!H-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_N-4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_N-4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.092640560837302, 'dn_dEa': 0.0, 'name': 'CCC=O <=> C=COC'}]
""",
)

entry(
    index = 30,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_4R->N",
    kinetics = ArrheniusBM(A=(3.81632e+14,'s^-1'), n=-0.222789, w0=(559500,'J/mol'), E0=(147442,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_4R->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_4R->N
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_4R->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_4R->N
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.23565448928588958, 'dE0': -0.00039626256096155567, 'dn': 0.004078443448463792, 'dA_dEa': 2.316751259582339, 'dE0_dEa': 0.3446403027970917, 'dn_dEa': -0.09712975279808873, 'name': 'CC=O <=> C=CO'}, {'dA': 0.49002059658237296, 'dE0': 0.0006400286138569833, 'dn': -0.006557253405331839, 'dA_dEa': -5.6764213353612405, 'dE0_dEa': 0.3281482131923072, 'dn_dEa': 0.23705654965107195, 'name': 'CCC(C)=O <=> C=C(O)CC'}, {'dA': 0.23591034943850997, 'dE0': -0.0003959376021856139, 'dn': 0.00406687617316808, 'dA_dEa': 2.277880062969724, 'dE0_dEa': 0.336780237912412, 'dn_dEa': -0.095502728180929, 'name': 'CC=O <=> C=CO'}]
""",
)

entry(
    index = 31,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N",
    kinetics = ArrheniusBM(A=(1.64685e-57,'s^-1'), n=20.836, w0=(734240,'J/mol'), E0=(-47104.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.7709993395862518, var=15.19742260456597, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N
        Total Standard Deviation in ln(k): 17.29010623737784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N
Total Standard Deviation in ln(k): 17.29010623737784""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N
Total Standard Deviation in ln(k): 17.29010623737784
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.0876440940023262, 'dn_dEa': 0.0, 'name': 'CCC(C)=O <=> C=C(O)CC'}]
""",
)

entry(
    index = 32,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S",
    kinetics = ArrheniusBM(A=(2628.85,'s^-1'), n=2.78353, w0=(782000,'J/mol'), E0=(89057.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004857179637508415, var=0.25064116944332687, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S
        Total Standard Deviation in ln(k): 1.0158560594211685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S
Total Standard Deviation in ln(k): 1.0158560594211685""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S
Total Standard Deviation in ln(k): 1.0158560594211685
sensitivities = [{'dA': 0.00029900186859780313, 'dE0': -0.0, 'dn': 1.0890856141053178e-07, 'dA_dEa': -0.06277534410515509, 'dE0_dEa': -0.0, 'dn_dEa': 0.0003653464261124791, 'name': 'C2H4O <=> C2H4O-2'}, {'dA': 0.00029852779448450394, 'dE0': -0.0, 'dn': 1.1198774250289095e-07, 'dA_dEa': -0.06126888126801297, 'dE0_dEa': -0.0, 'dn_dEa': 0.000356586873371301, 'name': 'C4H8O <=> C4H8O-2'}, {'dA': 0.0002987720790770583, 'dE0': -0.0, 'dn': 1.1039807742629286e-07, 'dA_dEa': -0.061268656480713085, 'dE0_dEa': -0.0, 'dn_dEa': 0.00035658540897305613, 'name': 'C2H4O <=> C2H4O-2'}, {'dA': 0.004287908581091432, 'dE0': -0.0, 'dn': 1.0809384397028199e-07, 'dA_dEa': -0.40133992300188637, 'dE0_dEa': -0.0, 'dn_dEa': 0.0023341358915895845, 'name': 'CH2OS <=> CH2OS-2'}, {'dA': 0.004287731229624586, 'dE0': -0.0, 'dn': 1.0923992277259388e-07, 'dA_dEa': -0.3941049536138487, 'dE0_dEa': -0.0, 'dn_dEa': 0.0022920644054569214, 'name': 'C2H4OS <=> C2H4OS-2'}, {'dA': 0.004287072272291442, 'dE0': -0.0, 'dn': 1.1352958720799612e-07, 'dA_dEa': -0.3941038855828517, 'dE0_dEa': -0.0, 'dn_dEa': 0.002292057448800454, 'name': 'C3H6OS <=> C3H6OS-2'}, {'dA': 0.0002975540951411277, 'dE0': -0.0, 'dn': 1.183301406627487e-07, 'dA_dEa': -0.10548247854559374, 'dE0_dEa': -0.0, 'dn_dEa': 0.0006136910785614366, 'name': 'C3H6O <=> C3H6O-2'}, {'dA': 0.02319571413522936, 'dE0': -0.0, 'dn': 1.2095929502674854e-07, 'dA_dEa': -2.471863819210102, 'dE0_dEa': -0.0, 'dn_dEa': 0.01437445032781897, 'name': 'C2H4N2O2 <=> C2H4N2O2-2'}, {'dA': 0.023196381164327984, 'dE0': -0.0, 'dn': 1.1664177562748002e-07, 'dA_dEa': -1.8695191543544991, 'dE0_dEa': -0.0, 'dn_dEa': 0.010871755055405037, 'name': 'C2H4N2O2-3 <=> C2H4N2O2-4'}, {'dA': 0.02319601358635992, 'dE0': -0.0, 'dn': 1.1894311087915798e-07, 'dA_dEa': -2.1129373011208425, 'dE0_dEa': -0.0, 'dn_dEa': 0.012287258446098452, 'name': 'C2H4N2O2-5 <=> C2H4N2O2-6'}, {'dA': 0.023204890766239997, 'dE0': -0.0, 'dn': 6.132197840046258e-08, 'dA_dEa': -1.8455923713818023, 'dE0_dEa': -0.0, 'dn_dEa': 0.01073262098221486, 'name': 'C2H4N2O2-7 <=> C2H4N2O2-8'}, {'dA': 0.023201072366421438, 'dE0': -0.0, 'dn': 8.604301731473027e-08, 'dA_dEa': -1.9320218030431842, 'dE0_dEa': -0.0, 'dn_dEa': 0.011235207994460473, 'name': 'C3H3NO <=> C3H3NO-2'}, {'dA': 0.02319311803944657, 'dE0': -0.0, 'dn': 1.37739254068858e-07, 'dA_dEa': -1.935399642519755, 'dE0_dEa': -0.0, 'dn_dEa': 0.011254856777289062, 'name': 'C3H6N2O <=> C3H6N2O-2'}, {'dA': 0.02320847730175302, 'dE0': -0.0, 'dn': 3.786890388184058e-08, 'dA_dEa': -1.7778558409704286, 'dE0_dEa': -0.0, 'dn_dEa': 0.01033871768031504, 'name': 'C2H5N3O <=> C2H5N3O-2'}, {'dA': 0.023197138460775757, 'dE0': -0.0, 'dn': 1.1171048095504309e-07, 'dA_dEa': -1.8873330620296915, 'dE0_dEa': -0.0, 'dn_dEa': 0.010975348961198929, 'name': 'C2H3NO2 <=> C2H3NO2-2'}, {'dA': 0.023203977121968648, 'dE0': -0.0, 'dn': 6.728664392893177e-08, 'dA_dEa': -1.9640109053968788, 'dE0_dEa': -0.0, 'dn_dEa': 0.011421235649107837, 'name': 'C2H4N2O2-9 <=> C2H4N2O2-10'}, {'dA': 0.023199413760724208, 'dE0': -0.0, 'dn': 9.692561357343466e-08, 'dA_dEa': -1.911373470221844, 'dE0_dEa': -0.0, 'dn_dEa': 0.011115142853112488, 'name': 'C2H4N2O <=> C2H4N2O-2'}, {'dA': 0.023197093213414344, 'dE0': -0.0, 'dn': 1.1198307317368794e-07, 'dA_dEa': -1.8019973716152147, 'dE0_dEa': -0.0, 'dn_dEa': 0.010479111637546171, 'name': 'CH4N2O <=> CH4N2O-2'}, {'dA': 0.023189550205418352, 'dE0': -0.0, 'dn': 1.61091213458532e-07, 'dA_dEa': -3.394373425891591, 'dE0_dEa': -0.0, 'dn_dEa': 0.019738950354233207, 'name': 'C2H4N2O2-11 <=> C2H4N2O2-12'}, {'dA': 0.02319280872598284, 'dE0': -0.0, 'dn': 1.398984162968718e-07, 'dA_dEa': -2.3454705360566406, 'dE0_dEa': -0.0, 'dn_dEa': 0.01363945776791453, 'name': 'C2H4N2O2-13 <=> C2H4N2O2-14'}, {'dA': 0.02320181994264459, 'dE0': -0.0, 'dn': 8.120559226040906e-08, 'dA_dEa': -2.7097664269322905, 'dE0_dEa': -0.0, 'dn_dEa': 0.015757880594225004, 'name': 'C2H3NO2-3 <=> C2H3NO2-4'}, {'dA': 0.023191345775333327, 'dE0': -0.0, 'dn': 1.493187074582741e-07, 'dA_dEa': -2.6071408256316917, 'dE0_dEa': -0.0, 'dn_dEa': 0.015161104459860571, 'name': 'C2H3NO2-3 <=> C2H3NO2-4'}, {'dA': 0.023212142508557746, 'dE0': -0.0, 'dn': 1.4616932541651792e-08, 'dA_dEa': -4.147896385604101, 'dE0_dEa': -0.0, 'dn_dEa': 0.024120756889585503, 'name': 'C2H4N2O-3 <=> C2H4N2O-4'}, {'dA': 0.02320391567423286, 'dE0': -0.0, 'dn': 6.760834460988417e-08, 'dA_dEa': -2.9955999603433727, 'dE0_dEa': -0.0, 'dn_dEa': 0.017420033667485443, 'name': 'C2H5N3O-3 <=> C2H5N3O-4'}, {'dA': 0.023191947150283165, 'dE0': -0.0, 'dn': 1.4543366455001569e-07, 'dA_dEa': -2.5538900499103048, 'dE0_dEa': -0.0, 'dn_dEa': 0.014851442220595772, 'name': 'C2H4N2O-5 <=> C2H4N2O-6'}, {'dA': 0.004287609044695745, 'dE0': -0.0, 'dn': 1.1005174200851078e-07, 'dA_dEa': -0.4442091255896719, 'dE0_dEa': -0.0, 'dn_dEa': 0.0025834252929584378, 'name': 'SC=O <=> OC=S'}, {'dA': 0.00428699402732538, 'dE0': -0.0, 'dn': 1.1404981488575247e-07, 'dA_dEa': -0.432274063570096, 'dE0_dEa': -0.0, 'dn_dEa': 0.00251402171218952, 'name': 'CC(=O)S <=> CC(=S)O'}, {'dA': 0.0042874613654935445, 'dE0': -0.0, 'dn': 1.1100154797294429e-07, 'dA_dEa': -0.4384134309134907, 'dE0_dEa': -0.0, 'dn_dEa': 0.0025497226853261378, 'name': 'CCC(=O)S <=> CCC(=S)O'}, {'dA': 0.023171955888304008, 'dE0': -0.0, 'dn': 2.756422566825251e-07, 'dA_dEa': -4.566273532106427, 'dE0_dEa': -0.0, 'dn_dEa': 0.026553662952870913, 'name': 'O=CNC(=O)N <=> NC(=NC=O)O'}, {'dA': 0.023199702440026893, 'dE0': -0.0, 'dn': 9.501424781588419e-08, 'dA_dEa': -3.5222807623544456, 'dE0_dEa': -0.0, 'dn_dEa': 0.020482742634219755, 'name': 'O=CNC(=O)N <=> OC(=N)NC=O'}, {'dA': 0.023201119802254477, 'dE0': -0.0, 'dn': 8.579473781021145e-08, 'dA_dEa': -3.1030292426240758, 'dE0_dEa': -0.0, 'dn_dEa': 0.018044745673920417, 'name': 'O=CNC(=O)N <=> NC(=O)N=CO'}, {'dA': 0.023193926153910804, 'dE0': -0.0, 'dn': 1.3261522880828292e-07, 'dA_dEa': -3.280603715410641, 'dE0_dEa': -0.0, 'dn_dEa': 0.019077362181303632, 'name': 'NC(=O)OC=N <=> N=COC(=N)O'}, {'dA': 0.02321033548469387, 'dE0': -0.0, 'dn': 2.5929912143792505e-08, 'dA_dEa': -2.730148165625524, 'dE0_dEa': -0.0, 'dn_dEa': 0.0158763938915799, 'name': 'O=CN1C=N1 <=> o1cnnc1'}, {'dA': 0.023196853760512393, 'dE0': -0.0, 'dn': 1.1355486599023312e-07, 'dA_dEa': -3.1888428557355257, 'dE0_dEa': -0.0, 'dn_dEa': 0.01854376425614102, 'name': 'NC(=O)C#C <=> OC(=N)C#C'}, {'dA': 0.023195392287791772, 'dE0': -0.0, 'dn': 1.2308689902980405e-07, 'dA_dEa': -3.6575409626497666, 'dE0_dEa': -0.0, 'dn_dEa': 0.021269295559516947, 'name': 'NC(=O)N1CC1 <=> OC(=N)N1CC1'}, {'dA': 0.023197174868985537, 'dE0': -0.0, 'dn': 1.1147057404081933e-07, 'dA_dEa': -3.545719184814224, 'dE0_dEa': -0.0, 'dn_dEa': 0.02061903650677248, 'name': 'NC(=O)NC=N <=> N=CNC(=N)O'}, {'dA': 0.02319550722518471, 'dE0': -0.0, 'dn': 1.2224255550081788e-07, 'dA_dEa': -3.399659061642898, 'dE0_dEa': -0.0, 'dn_dEa': 0.019769684437756826, 'name': 'O=CNC=O <=> OC=NC=O'}, {'dA': 0.023198105594704255, 'dE0': -0.0, 'dn': 1.0540125113366192e-07, 'dA_dEa': -3.168876683190896, 'dE0_dEa': -0.0, 'dn_dEa': 0.01842765813758712, 'name': 'NC(=O)C(=O)N <=> OC(=N)C(=O)N'}, {'dA': 0.023197583573167146, 'dE0': -0.0, 'dn': 1.0883240304111713e-07, 'dA_dEa': -2.752329576310634, 'dE0_dEa': -0.0, 'dn_dEa': 0.01600539204142726, 'name': 'N=CNC=O <=> OC=NC=N'}, {'dA': 0.023204337423979097, 'dE0': -0.0, 'dn': 6.480626405402104e-08, 'dA_dEa': -4.032275871424407, 'dE0_dEa': -0.0, 'dn_dEa': 0.023448410416813528, 'name': 'NC(=O)N <=> NC(=N)O'}, {'dA': 0.023197963230361718, 'dE0': -0.0, 'dn': 1.0638084419818363e-07, 'dA_dEa': -5.009730104405304, 'dE0_dEa': -0.0, 'dn_dEa': 0.02913242075940126, 'name': 'O=CNC(=O)N <=> NC(=O)OC=N'}, {'dA': 0.023201805532837908, 'dE0': -0.0, 'dn': 8.123425228103445e-08, 'dA_dEa': -4.21055074213019, 'dE0_dEa': -0.0, 'dn_dEa': 0.0244851144016863, 'name': 'O=CNC(=O)N <=> NC(=N)OC=O'}, {'dA': 0.023203920420658334, 'dE0': -0.0, 'dn': 6.772845907834787e-08, 'dA_dEa': -4.127487028171572, 'dE0_dEa': -0.0, 'dn_dEa': 0.02400207600163292, 'name': 'O=CNC=O <=> N=COC=O'}, {'dA': 0.023196237322056557, 'dE0': -0.0, 'dn': 1.1735086962093064e-07, 'dA_dEa': -1.9222433087693231, 'dE0_dEa': -0.0, 'dn_dEa': 0.011178348443260752, 'name': 'O=CN1C=N1 <=> c1ncno1'}, {'dA': 0.023188384830066577, 'dE0': -0.0, 'dn': 1.6880961463111204e-07, 'dA_dEa': -4.024857469091091, 'dE0_dEa': -0.0, 'dn_dEa': 0.023405274016251906, 'name': 'O=CNC=O <=> N=COC=O'}, {'dA': 0.023196600039912307, 'dE0': -0.0, 'dn': 1.1524435810496459e-07, 'dA_dEa': -5.946284178975902, 'dE0_dEa': -0.0, 'dn_dEa': 0.034577757959307176, 'name': 'N=CNC=O <=> N=COC=N'}, {'dA': 0.02319475512990976, 'dE0': -0.0, 'dn': 1.2722811099882084e-07, 'dA_dEa': -4.484143265216783, 'dE0_dEa': -0.0, 'dn_dEa': 0.026076075779711896, 'name': 'O=CN1C=C1 <=> c1ncco1'}, {'dA': 0.023196923876869557, 'dE0': -0.0, 'dn': 1.1312754186248154e-07, 'dA_dEa': -4.426629361490119, 'dE0_dEa': -0.0, 'dn_dEa': 0.02574162574526029, 'name': 'N=CN1C=N1 <=> [nH]1cnnc1'}, {'dA': 0.023186437772440338, 'dE0': -0.0, 'dn': 1.8156348482076175e-07, 'dA_dEa': -6.1348515907873145, 'dE0_dEa': -0.0, 'dn_dEa': 0.03567511393760027, 'name': 'N=CN1C=C1 <=> c1ncc[nH]1'}, {'dA': 0.023196207450839945, 'dE0': -0.0, 'dn': 1.1779606600873514e-07, 'dA_dEa': -2.9150476322857712, 'dE0_dEa': -0.0, 'dn_dEa': 0.016951617852116206, 'name': 'NC(=O)NC=N <=> NC=NC(=O)N'}, {'dA': 0.023198779587121687, 'dE0': -0.0, 'dn': 1.0105780890674911e-07, 'dA_dEa': -2.9955522781793777, 'dE0_dEa': -0.0, 'dn_dEa': 0.01741975868730744, 'name': 'N=CNC=O <=> NC=NC=O'}, {'dA': 0.023194646757931703, 'dE0': -0.0, 'dn': 1.2770937392943483e-07, 'dA_dEa': -6.316201995844735, 'dE0_dEa': -0.0, 'dn_dEa': 0.03672968692349518, 'name': 'N#CC(=N)N1C=C1 <=> N#Cc1ncc[nH]1'}]
""",
)

entry(
    index = 33,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S",
    kinetics = ArrheniusBM(A=(0.000221028,'s^-1'), n=4.87215, w0=(771526,'J/mol'), E0=(113206,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0013507450818510233, var=6.7138360241038875, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S
        Total Standard Deviation in ln(k): 5.19787713242361"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S
Total Standard Deviation in ln(k): 5.19787713242361""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S
Total Standard Deviation in ln(k): 5.19787713242361
sensitivities = [{'dA': 1.450688367761348, 'dE0': 0.0044018374065574, 'dn': -0.03152431428516015, 'dA_dEa': 14.74453614168765, 'dE0_dEa': 0.2749549818680921, 'dn_dEa': -0.3864816258257646, 'name': 'C2H4O <=> C2H4O-2'}, {'dA': 1.5970065643442037, 'dE0': 0.004951292260107011, 'dn': -0.035354688531553484, 'dA_dEa': 9.433263095913675, 'dE0_dEa': 0.24985463044460182, 'dn_dEa': -0.2473348329909889, 'name': 'C4H8O <=> C4H8O-2'}, {'dA': 1.442879491204411, 'dE0': 0.004374642035515156, 'dn': -0.03131811596848877, 'dA_dEa': 14.622850636783204, 'dE0_dEa': 0.26917838303410024, 'dn_dEa': -0.3833251363951261, 'name': 'C2H4O <=> C2H4O-2'}, {'dA': 2.3184472810558243, 'dE0': 0.007646586961493269, 'dn': -0.05425206454129993, 'dA_dEa': -23.55970988286142, 'dE0_dEa': 0.28179499630611216, 'dn_dEa': 0.6170476239108643, 'name': 'C3H6O <=> C3H6O-2'}]
""",
)

entry(
    index = 34,
    label = "Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6.5268e+11,'s^-1'), n=0.396329, w0=(783500,'J/mol'), E0=(259654,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_5R!H->C_Ext-1R!H-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.920203198450264, 'dn_dEa': 0.0, 'name': 'C3H6O <=> C3H6O-2'}]
""",
)

entry(
    index = 35,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_3R!H->C",
    kinetics = ArrheniusBM(A=(7.49767e+07,'s^-1'), n=1.48437, w0=(667000,'J/mol'), E0=(433271,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.470728631562516e-15, var=0.07135570365739116, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_3R!H->C
        Total Standard Deviation in ln(k): 0.5355146250198273"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_3R!H->C
Total Standard Deviation in ln(k): 0.5355146250198273""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_3R!H->C
Total Standard Deviation in ln(k): 0.5355146250198273
sensitivities = [{'dA': 0.234812332791127, 'dE0': -0.0004171041375469523, 'dn': 0.004142061286956999, 'dA_dEa': 2.325774923599234, 'dE0_dEa': 0.3429960298752944, 'dn_dEa': -0.09822850217948224, 'name': 'C2H4O <=> C2H4O-2'}, {'dA': 0.503520938423263, 'dE0': 0.0007216392926842707, 'dn': -0.007175093605122859, 'dA_dEa': -5.4013876307627395, 'dE0_dEa': 0.3022778622909712, 'dn_dEa': 0.2272499681600849, 'name': 'C4H8O <=> C4H8O-2'}, {'dA': 0.2334864132463012, 'dE0': -0.0004222109053649869, 'dn': 0.004198507114756047, 'dA_dEa': 2.309806197392993, 'dE0_dEa': 0.3349232982300535, 'dn_dEa': -0.09756030226059899, 'name': 'C2H4O <=> C2H4O-2'}]
""",
)

entry(
    index = 36,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C",
    kinetics = ArrheniusBM(A=(3.70867e-134,'s^-1'), n=43.4476, w0=(717875,'J/mol'), E0=(-5808.39,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.620428518091382, var=89.65743457902248, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C
        Total Standard Deviation in ln(k): 25.56634853630231"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C
Total Standard Deviation in ln(k): 25.56634853630231""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C
Total Standard Deviation in ln(k): 25.56634853630231
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.9239154299556949, 'dn_dEa': 0.0, 'name': 'C4H8O <=> C4H8O-2'}]
""",
)

entry(
    index = 37,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R_3R!H->O",
    kinetics = ArrheniusBM(A=(1.37586e+09,'s^-1'), n=1.6158, w0=(707000,'J/mol'), E0=(400010,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R_3R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R_3R!H->O
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R_3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R_3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.0069118592307412085, 'dE0': -0.0, 'dn': -1.618036976327165e-05, 'dA_dEa': -0.399148914283431, 'dE0_dEa': -0.0, 'dn_dEa': 0.002298561859093338, 'name': 'CH2OS <=> CH2OS-2'}, {'dA': 0.00690991009833018, 'dE0': -0.0, 'dn': -1.616780080215839e-05, 'dA_dEa': -0.39190522412018025, 'dE0_dEa': -0.0, 'dn_dEa': 0.0022568315462953366, 'name': 'C2H4OS <=> C2H4OS-2'}, {'dA': 0.006911736250004503, 'dE0': -0.0, 'dn': -1.6179580504548747e-05, 'dA_dEa': -0.3919051681294127, 'dE0_dEa': -0.0, 'dn_dEa': 0.0022568311797398505, 'name': 'C3H6OS <=> C3H6OS-2'}, {'dA': 0.025849893859233936, 'dE0': -0.0, 'dn': -1.623248604166665e-05, 'dA_dEa': -2.471871887678662, 'dE0_dEa': -0.0, 'dn_dEa': 0.014239319518624546, 'name': 'C2H4N2O2 <=> C2H4N2O2-2'}, {'dA': 0.025837619858751285, 'dE0': -0.0, 'dn': -1.61535668688241e-05, 'dA_dEa': -1.8688968798132704, 'dE0_dEa': -0.0, 'dn_dEa': 0.010765647109181436, 'name': 'C2H4N2O2-3 <=> C2H4N2O2-4'}, {'dA': 0.025843102491765538, 'dE0': -0.0, 'dn': -1.618883323913632e-05, 'dA_dEa': -2.1125703145801307, 'dE0_dEa': -0.0, 'dn_dEa': 0.012169425350321589, 'name': 'C2H4N2O2-5 <=> C2H4N2O2-6'}, {'dA': 0.02584175470588264, 'dE0': -0.0, 'dn': -1.618022732025638e-05, 'dA_dEa': -1.8449279765777404, 'dE0_dEa': -0.0, 'dn_dEa': 0.010627555705538019, 'name': 'C2H4N2O2-7 <=> C2H4N2O2-8'}, {'dA': 0.025841139034812957, 'dE0': -0.0, 'dn': -1.6176139381179882e-05, 'dA_dEa': -1.9314659871556468, 'dE0_dEa': -0.0, 'dn_dEa': 0.011126095232326508, 'name': 'C3H3NO <=> C3H3NO-2'}, {'dA': 0.025839855680945337, 'dE0': -0.0, 'dn': -1.616786859418693e-05, 'dA_dEa': -1.9348523547366625, 'dE0_dEa': -0.0, 'dn_dEa': 0.011145613571353394, 'name': 'C3H6N2O <=> C3H6N2O-2'}, {'dA': 0.025848046846024892, 'dE0': -0.0, 'dn': -1.6220734732172954e-05, 'dA_dEa': -1.7771354312119139, 'dE0_dEa': -0.0, 'dn_dEa': 0.010237012135672163, 'name': 'C2H5N3O <=> C2H5N3O-2'}, {'dA': 0.025837662860797653, 'dE0': -0.0, 'dn': -1.6153693998816452e-05, 'dA_dEa': -1.8867169065688163, 'dE0_dEa': -0.0, 'dn_dEa': 0.01086830192661862, 'name': 'C2H3NO2 <=> C2H3NO2-2'}, {'dA': 0.02583918544019355, 'dE0': -0.0, 'dn': -1.6163534051637194e-05, 'dA_dEa': -1.9634812886126727, 'dE0_dEa': -0.0, 'dn_dEa': 0.011310534647295633, 'name': 'C2H4N2O2-9 <=> C2H4N2O2-10'}, {'dA': 0.025840540331503806, 'dE0': -0.0, 'dn': -1.617230937083316e-05, 'dA_dEa': -1.9107876803163721, 'dE0_dEa': -0.0, 'dn_dEa': 0.011006971119807186, 'name': 'C2H4N2O <=> C2H4N2O-2'}, {'dA': 0.025839542843189636, 'dE0': -0.0, 'dn': -1.616589369276247e-05, 'dA_dEa': -1.8012972838052683, 'dE0_dEa': -0.0, 'dn_dEa': 0.010376211032642722, 'name': 'CH4N2O <=> CH4N2O-2'}, {'dA': 0.02585244752140455, 'dE0': -0.0, 'dn': -1.624912842638677e-05, 'dA_dEa': -3.3953500449403338, 'dE0_dEa': -0.0, 'dn_dEa': 0.01955938980451342, 'name': 'C2H4N2O2-11 <=> C2H4N2O2-12'}, {'dA': 0.02584110549719583, 'dE0': -0.0, 'dn': -1.6175928986625416e-05, 'dA_dEa': -2.3453564083129406, 'dE0_dEa': -0.0, 'dn_dEa': 0.013510481811678623, 'name': 'C2H4N2O2-13 <=> C2H4N2O2-14'}, {'dA': 0.02584210196232846, 'dE0': -0.0, 'dn': -1.6182387094530443e-05, 'dA_dEa': -2.7100414902466383, 'dE0_dEa': -0.0, 'dn_dEa': 0.015611402925542982, 'name': 'C2H3NO2-3 <=> C2H3NO2-4'}, {'dA': 0.025844461475801953, 'dE0': -0.0, 'dn': -1.6197617490928992e-05, 'dA_dEa': -2.607300257949706, 'dE0_dEa': -0.0, 'dn_dEa': 0.01501951844703877, 'name': 'C2H3NO2-3 <=> C2H3NO2-4'}, {'dA': 0.025814094186674196, 'dE0': -0.0, 'dn': -1.600153295637821e-05, 'dA_dEa': -4.149704512258725, 'dE0_dEa': -0.0, 'dn_dEa': 0.023905165695003058, 'name': 'C2H4N2O-3 <=> C2H4N2O-4'}, {'dA': 0.02583897176578205, 'dE0': -0.0, 'dn': -1.6162222236007214e-05, 'dA_dEa': -2.9961773807375383, 'dE0_dEa': -0.0, 'dn_dEa': 0.01725980427446382, 'name': 'C2H5N3O-3 <=> C2H5N3O-4'}, {'dA': 0.025845547071415356, 'dE0': -0.0, 'dn': -1.6204595125038648e-05, 'dA_dEa': -2.5539901261313926, 'dE0_dEa': -0.0, 'dn_dEa': 0.014712398746888105, 'name': 'C2H4N2O-5 <=> C2H4N2O-6'}, {'dA': 0.006911422758549486, 'dE0': -0.0, 'dn': -1.6177554878735873e-05, 'dA_dEa': -0.4420620728638401, 'dE0_dEa': -0.0, 'dn_dEa': 0.0025457798106079616, 'name': 'SC=O <=> OC=S'}, {'dA': 0.006911783117403354, 'dE0': -0.0, 'dn': -1.6179884850879243e-05, 'dA_dEa': -0.43011507727901704, 'dE0_dEa': -0.0, 'dn_dEa': 0.002476954888840228, 'name': 'CC(=O)S <=> CC(=S)O'}, {'dA': 0.006911797441944907, 'dE0': -0.0, 'dn': -1.6179982790421658e-05, 'dA_dEa': -0.43626040880444894, 'dE0_dEa': -0.0, 'dn_dEa': 0.00251235707593558, 'name': 'CCC(=O)S <=> CCC(=S)O'}, {'dA': 0.025829370173372015, 'dE0': -0.0, 'dn': -1.6100102246859032e-05, 'dA_dEa': -4.568552108935868, 'dE0_dEa': -0.0, 'dn_dEa': 0.0263181230765994, 'name': 'O=CNC(=O)N <=> NC(=NC=O)O'}, {'dA': 0.025846127925890985, 'dE0': -0.0, 'dn': -1.62082708885816e-05, 'dA_dEa': -3.523414414502601, 'dE0_dEa': -0.0, 'dn_dEa': 0.020297168522189095, 'name': 'O=CNC(=O)N <=> OC(=N)NC=O'}, {'dA': 0.025839123139806477, 'dE0': -0.0, 'dn': -1.6163198281707586e-05, 'dA_dEa': -3.103719094412214, 'dE0_dEa': -0.0, 'dn_dEa': 0.017879339985695027, 'name': 'O=CNC(=O)N <=> NC(=O)N=CO'}, {'dA': 0.025838109934286993, 'dE0': -0.0, 'dn': -1.6156693437180523e-05, 'dA_dEa': -3.281483799270652, 'dE0_dEa': -0.0, 'dn_dEa': 0.018903428722854675, 'name': 'NC(=O)OC=N <=> N=COC(=N)O'}, {'dA': 0.025857070710347336, 'dE0': -0.0, 'dn': -1.6278980845544185e-05, 'dA_dEa': -2.730417579101941, 'dE0_dEa': -0.0, 'dn_dEa': 0.015728759855720087, 'name': 'O=CN1C=N1 <=> o1cnnc1'}, {'dA': 0.025841738562351682, 'dE0': -0.0, 'dn': -1.6180041490342843e-05, 'dA_dEa': -3.1896200438271864, 'dE0_dEa': -0.0, 'dn_dEa': 0.0183742078737266, 'name': 'NC(=O)C#C <=> OC(=N)C#C'}, {'dA': 0.0258332046314564, 'dE0': -0.0, 'dn': -1.6125032964744194e-05, 'dA_dEa': -3.658817448809207, 'dE0_dEa': -0.0, 'dn_dEa': 0.021077212413583762, 'name': 'NC(=O)N1CC1 <=> OC(=N)N1CC1'}, {'dA': 0.025838220693688643, 'dE0': -0.0, 'dn': -1.6157386351467564e-05, 'dA_dEa': -3.5468829585174078, 'dE0_dEa': -0.0, 'dn_dEa': 0.020432369124273937, 'name': 'NC(=O)NC=N <=> N=CNC(=N)O'}, {'dA': 0.02584872115108113, 'dE0': -0.0, 'dn': -1.622502014544083e-05, 'dA_dEa': -3.400656246214259, 'dE0_dEa': -0.0, 'dn_dEa': 0.019589966221639783, 'name': 'O=CNC=O <=> OC=NC=O'}, {'dA': 0.025841267245144198, 'dE0': -0.0, 'dn': -1.617699675095264e-05, 'dA_dEa': -3.1696333935830205, 'dE0_dEa': -0.0, 'dn_dEa': 0.01825906649535003, 'name': 'NC(=O)C(=O)N <=> OC(=N)C(=O)N'}, {'dA': 0.025841682969488036, 'dE0': -0.0, 'dn': -1.6179705401391923e-05, 'dA_dEa': -2.7526438866235217, 'dE0_dEa': -0.0, 'dn_dEa': 0.01585682925066451, 'name': 'N=CNC=O <=> OC=NC=N'}, {'dA': 0.02583499389175188, 'dE0': -0.0, 'dn': -1.6136537192232686e-05, 'dA_dEa': -4.033962626124765, 'dE0_dEa': -0.0, 'dn_dEa': 0.023238388127212305, 'name': 'NC(=O)N <=> NC(=N)O'}, {'dA': 0.02584095520319636, 'dE0': -0.0, 'dn': -1.61749885118012e-05, 'dA_dEa': -5.012443423169641, 'dE0_dEa': -0.0, 'dn_dEa': 0.02887532473765102, 'name': 'O=CNC(=O)N <=> NC(=O)OC=N'}, {'dA': 0.02584230753655277, 'dE0': -0.0, 'dn': -1.6183512920736233e-05, 'dA_dEa': -4.212397282600941, 'dE0_dEa': -0.0, 'dn_dEa': 0.024266329441807667, 'name': 'O=CNC(=O)N <=> NC(=N)OC=O'}, {'dA': 0.025834991703280255, 'dE0': -0.0, 'dn': -1.613661311930465e-05, 'dA_dEa': -4.129269346976116, 'dE0_dEa': -0.0, 'dn_dEa': 0.023787439703746475, 'name': 'O=CNC=O <=> N=COC=O'}, {'dA': 0.02585739875371758, 'dE0': -0.0, 'dn': -1.628098270426941e-05, 'dA_dEa': -1.9216657060498916, 'dE0_dEa': -0.0, 'dn_dEa': 0.011069632765189791, 'name': 'O=CN1C=N1 <=> c1ncno1'}, {'dA': 0.025858736364628505, 'dE0': -0.0, 'dn': -1.628971192488597e-05, 'dA_dEa': -4.026536611093422, 'dE0_dEa': -0.0, 'dn_dEa': 0.023195609991311667, 'name': 'O=CNC=O <=> N=COC=O'}, {'dA': 0.025841229955861425, 'dE0': -0.0, 'dn': -1.61767458406917e-05, 'dA_dEa': -5.951181280978036, 'dE0_dEa': -0.0, 'dn_dEa': 0.03428331069704096, 'name': 'N=CNC=O <=> N=COC=N'}, {'dA': 0.025841258349149146, 'dE0': -0.0, 'dn': -1.617693294669048e-05, 'dA_dEa': -4.4862974261553, 'dE0_dEa': -0.0, 'dn_dEa': 0.02584424551521126, 'name': 'O=CN1C=C1 <=> c1ncco1'}, {'dA': 0.025841027422760024, 'dE0': -0.0, 'dn': -1.6175454761446924e-05, 'dA_dEa': -4.428729983317713, 'dE0_dEa': -0.0, 'dn_dEa': 0.025512609611932743, 'name': 'N=CN1C=N1 <=> [nH]1cnnc1'}, {'dA': 0.025890233104067316, 'dE0': -0.0, 'dn': -1.649288654855846e-05, 'dA_dEa': -6.1387442626432795, 'dE0_dEa': -0.0, 'dn_dEa': 0.03536381781323021, 'name': 'N=CN1C=C1 <=> c1ncc[nH]1'}, {'dA': 0.025839886774295454, 'dE0': -0.0, 'dn': -1.616811838787328e-05, 'dA_dEa': -2.915531186460251, 'dE0_dEa': -0.0, 'dn_dEa': 0.0167952079900214, 'name': 'NC(=O)NC=N <=> NC=NC(=O)N'}, {'dA': 0.02584037500242005, 'dE0': -0.0, 'dn': -1.617124240405922e-05, 'dA_dEa': -2.996122236482154, 'dE0_dEa': -0.0, 'dn_dEa': 0.017259483804477255, 'name': 'N=CNC=O <=> NC=NC=O'}, {'dA': 0.02584046271181535, 'dE0': -0.0, 'dn': -1.617188220129801e-05, 'dA_dEa': -6.32028898715545, 'dE0_dEa': -0.0, 'dn_dEa': 0.0364096822601258, 'name': 'N#CC(=N)N1C=C1 <=> N#Cc1ncc[nH]1'}]
""",
)

entry(
    index = 38,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R_N-3R!H->O",
    kinetics = ArrheniusBM(A=(1.04679e+11,'s^-1'), n=1.26667, w0=(615000,'J/mol'), E0=(331277,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R_N-3R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R_N-3R!H->O
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R_N-3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R_N-3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.03764345174773057, 'dE0': -0.0, 'dn': 5.6213881300831964e-06, 'dA_dEa': -4.972182832759679, 'dE0_dEa': -0.0, 'dn_dEa': 0.031220127738970854, 'name': 'C2H5N3O-3 <=> C2H5N3O-4'}, {'dA': 0.03766066232913505, 'dE0': -0.0, 'dn': 5.500422091648361e-06, 'dA_dEa': -4.2391280730816, 'dE0_dEa': -0.0, 'dn_dEa': 0.026617381082316243, 'name': 'C2H4N2O-5 <=> C2H4N2O-6'}, {'dA': 0.03759960353022921, 'dE0': -0.0, 'dn': 5.930178351032537e-06, 'dA_dEa': -7.578764105262206, 'dE0_dEa': -0.0, 'dn_dEa': 0.04758640163212059, 'name': 'O=CNC(=O)N <=> NC(=NC=O)O'}, {'dA': 0.037628980479102715, 'dE0': -0.0, 'dn': 5.7233256290703025e-06, 'dA_dEa': -5.846216352339373, 'dE0_dEa': -0.0, 'dn_dEa': 0.03670803633950647, 'name': 'O=CNC(=O)N <=> OC(=N)NC=O'}, {'dA': 0.03763058813888579, 'dE0': -0.0, 'dn': 5.711939242300375e-06, 'dA_dEa': -5.150465402537065, 'dE0_dEa': -0.0, 'dn_dEa': 0.03233953274579048, 'name': 'O=CNC(=O)N <=> NC(=O)N=CO'}, {'dA': 0.037631853814450146, 'dE0': -0.0, 'dn': 5.703030583360739e-06, 'dA_dEa': -5.444467333689462, 'dE0_dEa': -0.0, 'dn_dEa': 0.03418500423618406, 'name': 'NC(=O)OC=N <=> N=COC(=N)O'}, {'dA': 0.03763421827330108, 'dE0': -0.0, 'dn': 5.686087911055016e-06, 'dA_dEa': -4.531646246804188, 'dE0_dEa': -0.0, 'dn_dEa': 0.028454047276327762, 'name': 'O=CN1C=N1 <=> o1cnnc1'}, {'dA': 0.03763410143165361, 'dE0': -0.0, 'dn': 5.687283659863376e-06, 'dA_dEa': -5.292866490393649, 'dE0_dEa': -0.0, 'dn_dEa': 0.03323364412228945, 'name': 'NC(=O)C#C <=> OC(=N)C#C'}, {'dA': 0.03763122882105977, 'dE0': -0.0, 'dn': 5.707434756748671e-06, 'dA_dEa': -6.070684060916379, 'dE0_dEa': -0.0, 'dn_dEa': 0.03811743124495434, 'name': 'NC(=O)N1CC1 <=> OC(=N)N1CC1'}, {'dA': 0.037636307723691566, 'dE0': -0.0, 'dn': 5.671807770444559e-06, 'dA_dEa': -5.8851173304936655, 'dE0_dEa': -0.0, 'dn_dEa': 0.03695228665673245, 'name': 'NC(=O)NC=N <=> N=CNC(=N)O'}, {'dA': 0.03762963432052816, 'dE0': -0.0, 'dn': 5.718625908579403e-06, 'dA_dEa': -5.64253541169597, 'dE0_dEa': -0.0, 'dn_dEa': 0.03542901574111949, 'name': 'O=CNC=O <=> OC=NC=O'}, {'dA': 0.03763142353819108, 'dE0': -0.0, 'dn': 5.70607697858739e-06, 'dA_dEa': -5.2597333905032535, 'dE0_dEa': -0.0, 'dn_dEa': 0.033025606721322515, 'name': 'NC(=O)C(=O)N <=> OC(=N)C(=O)N'}, {'dA': 0.03763175274685141, 'dE0': -0.0, 'dn': 5.703766669498367e-06, 'dA_dEa': -4.56845981240456, 'dE0_dEa': -0.0, 'dn_dEa': 0.02868521580847709, 'name': 'N=CNC=O <=> OC=NC=N'}, {'dA': 0.037628178077402076, 'dE0': -0.0, 'dn': 5.728911643167632e-06, 'dA_dEa': -6.692590222727572, 'dE0_dEa': -0.0, 'dn_dEa': 0.04202227593247804, 'name': 'NC(=O)N <=> NC(=N)O'}, {'dA': 0.03763274372659412, 'dE0': -0.0, 'dn': 5.696795930298015e-06, 'dA_dEa': -8.314688782875585, 'dE0_dEa': -0.0, 'dn_dEa': 0.05220716305558918, 'name': 'O=CNC(=O)N <=> NC(=O)OC=N'}, {'dA': 0.03760578375989058, 'dE0': -0.0, 'dn': 5.886538213510782e-06, 'dA_dEa': -6.988480394512268, 'dE0_dEa': -0.0, 'dn_dEa': 0.04388017812550374, 'name': 'O=CNC(=O)N <=> NC(=N)OC=O'}, {'dA': 0.03763638338228207, 'dE0': -0.0, 'dn': 5.671162086950193e-06, 'dA_dEa': -6.851135463919222, 'dE0_dEa': -0.0, 'dn_dEa': 0.04301816411187632, 'name': 'O=CNC=O <=> N=COC=O'}, {'dA': 0.037635765409053924, 'dE0': -0.0, 'dn': 5.675814519904617e-06, 'dA_dEa': -3.1909195212737234, 'dE0_dEa': -0.0, 'dn_dEa': 0.020035878352414317, 'name': 'O=CN1C=N1 <=> c1ncno1'}, {'dA': 0.037630550210114556, 'dE0': -0.0, 'dn': 5.7121137889423635e-06, 'dA_dEa': -6.68027643867293, 'dE0_dEa': -0.0, 'dn_dEa': 0.04194496193168214, 'name': 'O=CNC=O <=> N=COC=O'}, {'dA': 0.03761721350770545, 'dE0': -0.0, 'dn': 5.805906531325388e-06, 'dA_dEa': -9.870886016586788, 'dE0_dEa': -0.0, 'dn_dEa': 0.06197826261440551, 'name': 'N=CNC=O <=> N=COC=N'}, {'dA': 0.0376200745364527, 'dE0': -0.0, 'dn': 5.7857620407871e-06, 'dA_dEa': -7.44246438912992, 'dE0_dEa': -0.0, 'dn_dEa': 0.04673061332795287, 'name': 'O=CN1C=C1 <=> c1ncco1'}, {'dA': 0.037634847430471886, 'dE0': -0.0, 'dn': 5.682320380897125e-06, 'dA_dEa': -7.347025644421833, 'dE0_dEa': -0.0, 'dn_dEa': 0.04613137449962629, 'name': 'N=CN1C=N1 <=> [nH]1cnnc1'}, {'dA': 0.037656846586746326, 'dE0': -0.0, 'dn': 5.5263714749914095e-06, 'dA_dEa': -10.182649467681115, 'dE0_dEa': -0.0, 'dn_dEa': 0.06393634961474104, 'name': 'N=CN1C=C1 <=> c1ncc[nH]1'}, {'dA': 0.03763812138402459, 'dE0': -0.0, 'dn': 5.658963467200814e-06, 'dA_dEa': -4.83848869355139, 'dE0_dEa': -0.0, 'dn_dEa': 0.030380681737939425, 'name': 'NC(=O)NC=N <=> NC=NC(=O)N'}, {'dA': 0.037625242057974496, 'dE0': -0.0, 'dn': 5.749478418360689e-06, 'dA_dEa': -4.972099754852459, 'dE0_dEa': -0.0, 'dn_dEa': 0.031219607235321214, 'name': 'N=CNC=O <=> NC=NC=O'}, {'dA': 0.03763441806370752, 'dE0': -0.0, 'dn': 5.685500120022584e-06, 'dA_dEa': -10.483263868438275, 'dE0_dEa': -0.0, 'dn_dEa': 0.06582359963822075, 'name': 'N#CC(=N)N1C=C1 <=> N#Cc1ncc[nH]1'}]
""",
)

entry(
    index = 39,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C",
    kinetics = ArrheniusBM(A=(8.63142e-63,'s^-1'), n=22.5022, w0=(679400,'J/mol'), E0=(-40826.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2635762441282121, var=50.24514974463436, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C
        Total Standard Deviation in ln(k): 14.87257854479527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C
Total Standard Deviation in ln(k): 14.87257854479527""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C
Total Standard Deviation in ln(k): 14.87257854479527
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.5531458183380386, 'dn_dEa': -0.0, 'name': 'O=CN1C=N1 <=> c1ncno1'}]
""",
)

entry(
    index = 40,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C",
    kinetics = ArrheniusBM(A=(4.13471e-05,'s^-1'), n=5.26861, w0=(770800,'J/mol'), E0=(119544,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12046792272150078, var=8.981422953803811, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C
        Total Standard Deviation in ln(k): 6.310678239436273"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C
Total Standard Deviation in ln(k): 6.310678239436273""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C
Total Standard Deviation in ln(k): 6.310678239436273
sensitivities = [{'dA': 0.04112590318073215, 'dE0': -0.0, 'dn': -7.904064880922238e-06, 'dA_dEa': -5.16907275067581, 'dE0_dEa': -0.0, 'dn_dEa': 0.03183084430104733, 'name': 'C2H5N3O-3 <=> C2H5N3O-4'}, {'dA': 0.04111926619998938, 'dE0': -0.0, 'dn': -7.858436989824172e-06, 'dA_dEa': -4.406759232040743, 'dE0_dEa': -0.0, 'dn_dEa': 0.027136466088066753, 'name': 'C2H4N2O-5 <=> C2H4N2O-6'}, {'dA': 0.04118377077589229, 'dE0': -0.0, 'dn': -8.30229538316783e-06, 'dA_dEa': -7.879903364256237, 'dE0_dEa': -0.0, 'dn_dEa': 0.04852439787443121, 'name': 'O=CNC(=O)N <=> NC(=NC=O)O'}, {'dA': 0.04112915357268774, 'dE0': -0.0, 'dn': -7.926545738211376e-06, 'dA_dEa': -6.078073458326786, 'dE0_dEa': -0.0, 'dn_dEa': 0.03742856819403901, 'name': 'O=CNC(=O)N <=> OC(=N)NC=O'}, {'dA': 0.041135305167476856, 'dE0': -0.0, 'dn': -7.9688630372162e-06, 'dA_dEa': -5.354483448514337, 'dE0_dEa': -0.0, 'dn_dEa': 0.03297261916531282, 'name': 'O=CNC(=O)N <=> NC(=O)N=CO'}, {'dA': 0.041135046672029586, 'dE0': -0.0, 'dn': -7.967079007288735e-06, 'dA_dEa': -5.660958728129286, 'dE0_dEa': -0.0, 'dn_dEa': 0.0348599270555386, 'name': 'NC(=O)OC=N <=> N=COC(=N)O'}, {'dA': 0.04114699521551755, 'dE0': -0.0, 'dn': -8.049271924273699e-06, 'dA_dEa': -4.710932203039938, 'dE0_dEa': -0.0, 'dn_dEa': 0.02900955547563435, 'name': 'O=CN1C=N1 <=> o1cnnc1'}, {'dA': 0.04113521620752634, 'dE0': -0.0, 'dn': -7.968287571192574e-06, 'dA_dEa': -5.5025817432869335, 'dE0_dEa': -0.0, 'dn_dEa': 0.03388462341266012, 'name': 'NC(=O)C#C <=> OC(=N)C#C'}, {'dA': 0.04113509822901049, 'dE0': -0.0, 'dn': -7.967434687918449e-06, 'dA_dEa': -6.3115115352168365, 'dE0_dEa': -0.0, 'dn_dEa': 0.038866097878415426, 'name': 'NC(=O)N1CC1 <=> OC(=N)N1CC1'}, {'dA': 0.04113483632295809, 'dE0': -0.0, 'dn': -7.965591662066787e-06, 'dA_dEa': -6.118520838527494, 'dE0_dEa': -0.0, 'dn_dEa': 0.037677637915578675, 'name': 'NC(=O)NC=N <=> N=CNC(=N)O'}, {'dA': 0.041132235537593244, 'dE0': -0.0, 'dn': -7.947759547197829e-06, 'dA_dEa': -5.866433151368901, 'dE0_dEa': -0.0, 'dn_dEa': 0.03612526123164424, 'name': 'O=CNC=O <=> OC=NC=O'}, {'dA': 0.04113570355457794, 'dE0': -0.0, 'dn': -7.971610610402773e-06, 'dA_dEa': -5.469339647590379, 'dE0_dEa': -0.0, 'dn_dEa': 0.033680813945195176, 'name': 'NC(=O)C(=O)N <=> OC(=N)C(=O)N'}, {'dA': 0.04113534879480083, 'dE0': -0.0, 'dn': -7.969162450056936e-06, 'dA_dEa': -4.74919868969489, 'dE0_dEa': -0.0, 'dn_dEa': 0.029245212063563862, 'name': 'N=CNC=O <=> OC=NC=N'}, {'dA': 0.04113127678806903, 'dE0': -0.0, 'dn': -7.941070330139215e-06, 'dA_dEa': -6.958570131360687, 'dE0_dEa': -0.0, 'dn_dEa': 0.04285095620337816, 'name': 'NC(=O)N <=> NC(=N)O'}, {'dA': 0.04112988389693326, 'dE0': -0.0, 'dn': -7.93149952025119e-06, 'dA_dEa': -8.645284721923005, 'dE0_dEa': -0.0, 'dn_dEa': 0.05323772420908189, 'name': 'O=CNC(=O)N <=> NC(=O)OC=N'}, {'dA': 0.04117261278225213, 'dE0': -0.0, 'dn': -8.225865651841688e-06, 'dA_dEa': -7.267313404981569, 'dE0_dEa': -0.0, 'dn_dEa': 0.04475304211548282, 'name': 'O=CNC(=O)N <=> NC(=N)OC=O'}, {'dA': 0.04113091688396251, 'dE0': -0.0, 'dn': -7.938449956257416e-06, 'dA_dEa': -7.122622857139834, 'dE0_dEa': -0.0, 'dn_dEa': 0.04386101233559011, 'name': 'O=CNC=O <=> N=COC=O'}, {'dA': 0.041134865597318805, 'dE0': -0.0, 'dn': -7.965626616299333e-06, 'dA_dEa': -6.945494524217875, 'dE0_dEa': -0.0, 'dn_dEa': 0.04277023862713813, 'name': 'O=CNC=O <=> N=COC=O'}, {'dA': 0.04114513592413003, 'dE0': -0.0, 'dn': -8.036448324657469e-06, 'dA_dEa': -10.263739665135738, 'dE0_dEa': -0.0, 'dn_dEa': 0.06320434339946203, 'name': 'N=CNC=O <=> N=COC=N'}, {'dA': 0.041134452885676166, 'dE0': -0.0, 'dn': -7.963136169857536e-06, 'dA_dEa': -7.740788398764096, 'dE0_dEa': -0.0, 'dn_dEa': 0.04766967994249798, 'name': 'O=CN1C=C1 <=> c1ncco1'}, {'dA': 0.04112282243796015, 'dE0': -0.0, 'dn': -7.88275013093253e-06, 'dA_dEa': -7.640362941573062, 'dE0_dEa': -0.0, 'dn_dEa': 0.0470503888052773, 'name': 'N=CN1C=N1 <=> [nH]1cnnc1'}, {'dA': 0.04113053623200811, 'dE0': -0.0, 'dn': -7.936089948780974e-06, 'dA_dEa': -10.587166808052217, 'dE0_dEa': -0.0, 'dn_dEa': 0.06519603276831444, 'name': 'N=CN1C=C1 <=> c1ncc[nH]1'}, {'dA': 0.04112728723271628, 'dE0': -0.0, 'dn': -7.913756240285436e-06, 'dA_dEa': -5.030203277215705, 'dE0_dEa': -0.0, 'dn_dEa': 0.030975794117709683, 'name': 'NC(=O)NC=N <=> NC=NC(=O)N'}, {'dA': 0.041139521158588634, 'dE0': -0.0, 'dn': -7.997893806159121e-06, 'dA_dEa': -5.168979259338472, 'dE0_dEa': -0.0, 'dn_dEa': 0.03183026483745306, 'name': 'N=CNC=O <=> NC=NC=O'}, {'dA': 0.04103616336692991, 'dE0': -0.0, 'dn': -7.285604639740365e-06, 'dA_dEa': -10.9012703998713, 'dE0_dEa': -0.0, 'dn_dEa': 0.06713113766113825, 'name': 'N#CC(=N)N1C=C1 <=> N#Cc1ncc[nH]1'}]
""",
)

entry(
    index = 41,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(4909.53,'s^-1'), n=2.71698, w0=(782000,'J/mol'), E0=(88826.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1408662726283667e-06, var=3.5438674360202764e-06, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S_Ext-1R!H-R
        Total Standard Deviation in ln(k): 0.003776812860711284"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.003776812860711284""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.003776812860711284
sensitivities = [{'dA': 0.10112935979124109, 'dE0': -0.0, 'dn': -7.5329870091913815e-06, 'dA_dEa': -11.77912388180987, 'dE0_dEa': -0.0, 'dn_dEa': 0.06716530912134408, 'name': 'O=CN1C=N1 <=> o1cnnc1'}, {'dA': 0.1010994104433505, 'dE0': -0.0, 'dn': -7.342024019632895e-06, 'dA_dEa': -21.614933720288825, 'dE0_dEa': -0.0, 'dn_dEa': 0.12325033885333504, 'name': 'O=CNC(=O)N <=> NC(=O)OC=N'}, {'dA': 0.10114953457219804, 'dE0': -0.0, 'dn': -7.661049508326709e-06, 'dA_dEa': -18.16794468340022, 'dE0_dEa': -0.0, 'dn_dEa': 0.10359609316348664, 'name': 'O=CNC(=O)N <=> NC(=N)OC=O'}, {'dA': 0.10107380555269832, 'dE0': -0.0, 'dn': -7.178455493900404e-06, 'dA_dEa': -17.808260931163574, 'dE0_dEa': -0.0, 'dn_dEa': 0.10154419040618466, 'name': 'O=CNC=O <=> N=COC=O'}, {'dA': 0.10108109478325081, 'dE0': -0.0, 'dn': -7.225884382591313e-06, 'dA_dEa': -17.36546994152568, 'dE0_dEa': -0.0, 'dn_dEa': 0.09901936200185109, 'name': 'O=CNC=O <=> N=COC=O'}, {'dA': 0.10112497525939239, 'dE0': -0.0, 'dn': -7.504793025076673e-06, 'dA_dEa': -25.662743181132427, 'dE0_dEa': -0.0, 'dn_dEa': 0.1463326203804563, 'name': 'N=CNC=O <=> N=COC=N'}, {'dA': 0.10109267438452865, 'dE0': -0.0, 'dn': -7.298893341909583e-06, 'dA_dEa': -19.347152028390013, 'dE0_dEa': -0.0, 'dn_dEa': 0.11031916341662085, 'name': 'O=CN1C=C1 <=> c1ncco1'}, {'dA': 0.1010852345757596, 'dE0': -0.0, 'dn': -7.25153897406707e-06, 'dA_dEa': -19.101908883927592, 'dE0_dEa': -0.0, 'dn_dEa': 0.10892275657197636, 'name': 'N=CN1C=N1 <=> [nH]1cnnc1'}, {'dA': 0.10116162454211212, 'dE0': -0.0, 'dn': -7.739774469329923e-06, 'dA_dEa': -26.46960609297658, 'dE0_dEa': -0.0, 'dn_dEa': 0.15093226859062428, 'name': 'N=CN1C=C1 <=> c1ncc[nH]1'}, {'dA': 0.10117484748662924, 'dE0': -0.0, 'dn': -7.822734014389924e-06, 'dA_dEa': -27.252102635859092, 'dE0_dEa': -0.0, 'dn_dEa': 0.15539417588010515, 'name': 'N#CC(=N)N1C=C1 <=> N#Cc1ncc[nH]1'}]
""",
)

entry(
    index = 42,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O",
    kinetics = ArrheniusBM(A=(0.00132983,'s^-1'), n=4.6492, w0=(769562,'J/mol'), E0=(116133,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.011878464585718973, var=6.628325949021129, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O
        Total Standard Deviation in ln(k): 5.1911431859520585"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O
Total Standard Deviation in ln(k): 5.1911431859520585""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O
Total Standard Deviation in ln(k): 5.1911431859520585
sensitivities = [{'dA': 0.15961554309386708, 'dE0': -0.0006101111186904814, 'dn': 0.007646603022453894, 'dA_dEa': 1.3054455689528783, 'dE0_dEa': 0.3745280599355184, 'dn_dEa': -0.11256366948024693, 'name': 'O=CNC(=O)N <=> NC(=O)OC=N'}, {'dA': 1.3531127827663239, 'dE0': 0.007466187412305487, 'dn': -0.0934508489565661, 'dA_dEa': -24.683325553065902, 'dE0_dEa': 0.1403228874981549, 'dn_dEa': 2.08917402925822, 'name': 'O=CNC(=O)N <=> NC(=N)OC=O'}, {'dA': -0.2533584261499579, 'dE0': -0.0034047631030659224, 'dn': 0.04262823976097555, 'dA_dEa': 11.099450941509104, 'dE0_dEa': 0.37639889571977575, 'dn_dEa': -0.9418406133024116, 'name': 'O=CNC=O <=> N=COC=O'}, {'dA': -0.2526977500707795, 'dE0': -0.0034005963558825327, 'dn': 0.04257181981305493, 'dA_dEa': 10.80992890916951, 'dE0_dEa': 0.3669552595763449, 'dn_dEa': -0.9172648906038292, 'name': 'O=CNC=O <=> N=COC=O'}]
""",
)

entry(
    index = 43,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O",
    kinetics = ArrheniusBM(A=(1.85399,'s^-1'), n=3.49715, w0=(782000,'J/mol'), E0=(83909.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.004050044991505004, var=0.10935763999388207, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O
        Total Standard Deviation in ln(k): 0.6731271817713865"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O
Total Standard Deviation in ln(k): 0.6731271817713865""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O
Total Standard Deviation in ln(k): 0.6731271817713865
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.246096497544664, 'dn_dEa': 0.0, 'name': 'O=CNC(=O)N <=> NC(=O)OC=N'}]
""",
)

entry(
    index = 44,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_3R!H->C_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.885e+08,'s^-1'), n=1.289, w0=(667000,'J/mol'), E0=(434967,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_3R!H->C_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_3R!H->C_Ext-5R!H-R_Ext-5R!H-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_3R!H->C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_3R!H->C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.399894756260111, 'dn_dEa': 0.0, 'name': 'O=CNC(=O)N <=> NC(=N)OC=O'}]
""",
)

entry(
    index = 45,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_2CN->C",
    kinetics = ArrheniusBM(A=(3.62e+09,'s^-1'), n=0.863, w0=(783500,'J/mol'), E0=(255551,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_2CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_2CN->C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 7.587648053290988, 'dE0': 0.03143674718159078, 'dn': -0.15705776935842375, 'dA_dEa': -32.594198857657055, 'dE0_dEa': -0.05490426435349367, 'dn_dEa': 0.6896224310835283, 'name': 'O=CN1C=N1 <=> o1cnnc1'}, {'dA': -1.696913332569681, 'dE0': -0.007905687501077334, 'dn': 0.03943207607979339, 'dA_dEa': 309.7716737848625, 'dE0_dEa': 1.493719095954532, 'dn_dEa': -6.556128917078367, 'name': 'N=CNC=O <=> N=COC=N'}, {'dA': 4.839406718828521, 'dE0': 0.019789956393120568, 'dn': -0.09889733366462017, 'dA_dEa': 24.435265648874907, 'dE0_dEa': 0.24017395660551172, 'dn_dEa': -0.5174258066703469, 'name': 'O=CN1C=C1 <=> c1ncco1'}, {'dA': 8.899362820337856, 'dE0': 0.03699318670072339, 'dn': -0.18481872542719976, 'dA_dEa': -97.33872093799617, 'dE0_dEa': -0.277596882047495, 'dn_dEa': 2.059682489551639, 'name': 'N=CN1C=N1 <=> [nH]1cnnc1'}, {'dA': 5.89830298559833, 'dE0': 0.02427724153920469, 'dn': -0.12130663499960118, 'dA_dEa': -14.029453682180328, 'dE0_dEa': 0.12749716972622105, 'dn_dEa': 0.29650305452480546, 'name': 'N=CN1C=C1 <=> c1ncc[nH]1'}, {'dA': 5.909694718478005, 'dE0': 0.02432205311397908, 'dn': -0.12154976301755355, 'dA_dEa': -14.663713989895138, 'dE0_dEa': 0.13034688145909776, 'dn_dEa': 0.30992072041967217, 'name': 'N#CC(=N)N1C=C1 <=> N#Cc1ncc[nH]1'}]
""",
)

entry(
    index = 46,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C",
    kinetics = ArrheniusBM(A=(1.11641e-135,'s^-1'), n=43.925, w0=(696000,'J/mol'), E0=(-144.585,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.08213559833397, var=88.30888828234897, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C
        Total Standard Deviation in ln(k): 26.583117941329068"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C
Total Standard Deviation in ln(k): 26.583117941329068""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C
Total Standard Deviation in ln(k): 26.583117941329068
sensitivities = [{'dA': -0.3846604026449964, 'dE0': -0.0018639714166379894, 'dn': -0.12658280097387317, 'dA_dEa': -14.063896575686513, 'dE0_dEa': 0.0311537535558783, 'dn_dEa': -3.0339533520980284, 'name': 'O=CN1C=N1 <=> o1cnnc1'}, {'dA': -2.8405423836875627, 'dE0': -0.009919552094240634, 'dn': -0.6566059188609967, 'dA_dEa': 33.4483902321915, 'dE0_dEa': 0.23648394335422174, 'dn_dEa': 7.222178347583166, 'name': 'O=CN1C=C1 <=> c1ncco1'}, {'dA': 0.7874873018139695, 'dE0': 0.0019799043418491555, 'dn': 0.12639516209568197, 'dA_dEa': -49.9906732684023, 'dE0_dEa': -0.03856358006257543, 'dn_dEa': -10.787616868968323, 'name': 'N=CN1C=N1 <=> [nH]1cnnc1'}, {'dA': -1.916640274224546, 'dE0': -0.006884885149041422, 'dn': -0.4572440057805654, 'dA_dEa': 15.52895636108247, 'dE0_dEa': 0.22447445833488666, 'dn_dEa': 3.3553035864836773, 'name': 'N=CN1C=C1 <=> c1ncc[nH]1'}, {'dA': -1.926572524965521, 'dE0': -0.006915497760028994, 'dn': -0.4594031086302368, 'dA_dEa': 15.946600608183184, 'dE0_dEa': 0.23099102867061386, 'dn_dEa': 3.4454204017858006, 'name': 'N#CC(=N)N1C=C1 <=> N#Cc1ncc[nH]1'}]
""",
)

entry(
    index = 47,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O",
    kinetics = ArrheniusBM(A=(8.23714e+08,'s^-1'), n=1.51542, w0=(707000,'J/mol'), E0=(132752,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.014265471420943657, var=4.066288247412202, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O
        Total Standard Deviation in ln(k): 4.078399128613921"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O
Total Standard Deviation in ln(k): 4.078399128613921""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O
Total Standard Deviation in ln(k): 4.078399128613921
sensitivities = [{'dA': 1.795403457009768, 'dE0': 0.004946103295641604, 'dn': 0.05922572910020395, 'dA_dEa': -55.743551002293145, 'dE0_dEa': 0.012057985875797896, 'dn_dEa': -2.5471059392827784, 'name': 'O=CN1C=N1 <=> o1cnnc1'}, {'dA': -4.381133289790767, 'dE0': -0.018607044601178555, 'dn': -0.2231480615216395, 'dA_dEa': 54.73520108065236, 'dE0_dEa': 0.5774990450292994, 'dn_dEa': 2.504730814693942, 'name': 'O=CN1C=C1 <=> c1ncco1'}]
""",
)

entry(
    index = 48,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(2.2591e-07,'s^-1'), n=6.06556, w0=(661000,'J/mol'), E0=(221850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8641639367273353, var=85.7131359414688, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O
        Total Standard Deviation in ln(k): 20.731381982288035"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O
Total Standard Deviation in ln(k): 20.731381982288035""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O
Total Standard Deviation in ln(k): 20.731381982288035
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.6913260387203447, 'dn_dEa': -0.0, 'name': 'O=CN1C=C1 <=> c1ncco1'}]
""",
)

entry(
    index = 49,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R",
    kinetics = ArrheniusBM(A=(25.6378,'s^-1'), n=3.66551, w0=(764000,'J/mol'), E0=(129088,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15106182521201603, var=19.940213171909487, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R
        Total Standard Deviation in ln(k): 9.331589722744125"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R
Total Standard Deviation in ln(k): 9.331589722744125""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R
Total Standard Deviation in ln(k): 9.331589722744125
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.570897319473596, 'dn_dEa': -0.0, 'name': 'O=CN1C=N1 <=> o1cnnc1'}]
""",
)

entry(
    index = 50,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.10704e-11,'s^-1'), n=7.19062, w0=(798000,'J/mol'), E0=(103605,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.026122774708554834, var=1.7134819836096122, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R
        Total Standard Deviation in ln(k): 2.6898340818415187"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.6898340818415187""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.6898340818415187
sensitivities = [{'dA': 2.9823571257882, 'dE0': 0.007530520828791702, 'dn': 0.23502908243439713, 'dA_dEa': -63.49846722076779, 'dE0_dEa': 0.0004909101775891614, 'dn_dEa': -5.6328362944716295, 'name': 'N=CN1C=N1 <=> [nH]1cnnc1'}, {'dA': -0.8000629460625845, 'dE0': -0.0032181565006892195, 'dn': -0.10054879723116601, 'dA_dEa': 35.92818012910866, 'dE0_dEa': 0.3525473769559412, 'dn_dEa': 3.1897952361401773, 'name': 'N=CN1C=C1 <=> c1ncc[nH]1'}, {'dA': -0.9498159120867535, 'dE0': -0.0036271127235241586, 'dn': -0.11389719589021065, 'dA_dEa': 37.031737826464266, 'dE0_dEa': 0.363077680137569, 'dn_dEa': 3.287802782805799, 'name': 'N#CC(=N)N1C=C1 <=> N#Cc1ncc[nH]1'}]
""",
)

entry(
    index = 51,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-3NOS-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.0652e-17,'s^-1'), n=8.61669, w0=(696000,'J/mol'), E0=(114142,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-3NOS-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-3NOS-R_Ext-5R!H-R_Ext-5R!H-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-3NOS-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-3NOS-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.49962533882214005, 'dE0': -2.6440832797654994e-07, 'dn': 1.8366526274490648e-05, 'dA_dEa': -0.4225896801771011, 'dE0_dEa': 0.3694245735401409, 'dn_dEa': 0.05656681700771681, 'name': 'N=CN1C=C1 <=> c1ncc[nH]1'}, {'dA': 0.49965139940871767, 'dE0': -1.9955924140980028e-07, 'dn': 1.4588082835055401e-05, 'dA_dEa': -0.43467575221005983, 'dE0_dEa': 0.38034584775551283, 'dn_dEa': 0.058180870148075325, 'name': 'N#CC(=N)N1C=C1 <=> N#Cc1ncc[nH]1'}]
""",
)

entry(
    index = 52,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S_Ext-1R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(87.5,'s^-1'), n=3.23, w0=(782000,'J/mol'), E0=(84839.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S_Ext-1R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S_Ext-1R!H-R_Ext-5R!H-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.7428409838058692, 'dn_dEa': 0.0, 'name': 'N#CC(=N)N1C=C1 <=> N#Cc1ncc[nH]1'}]
""",
)

entry(
    index = 53,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(0.000164309,'s^-1'), n=4.97161, w0=(787889,'J/mol'), E0=(112114,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.051526042577798054, var=4.08971979394378, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R
        Total Standard Deviation in ln(k): 4.183649319777569"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 4.183649319777569""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 4.183649319777569
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'N=CN1C=N1 <=> [nH]1cnnc1'}]
""",
)

entry(
    index = 54,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R",
    kinetics = ArrheniusBM(A=(4.74194e-14,'s^-1'), n=7.69802, w0=(798000,'J/mol'), E0=(92033.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.012749512289493472, var=0.8377613591004845, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R
        Total Standard Deviation in ln(k): 1.8669540248408663"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R
Total Standard Deviation in ln(k): 1.8669540248408663""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R
Total Standard Deviation in ln(k): 1.8669540248408663
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.2229155959344098, 'dn_dEa': 0.0, 'name': 'N=CNC=O <=> N=COC=N'}]
""",
)

entry(
    index = 55,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_5R!H->O",
    kinetics = ArrheniusBM(A=(1.50087e+11,'s^-1'), n=0.45162, w0=(707000,'J/mol'), E0=(137659,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008012511677798886, var=3.4768369970791304, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_5R!H->O
        Total Standard Deviation in ln(k): 3.7582167842883063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_5R!H->O
Total Standard Deviation in ln(k): 3.7582167842883063""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_5R!H->O
Total Standard Deviation in ln(k): 3.7582167842883063
sensitivities = [{'dA': 1.1569469900171323, 'dE0': 0.008183976566463764, 'dn': -0.026555983785730063, 'dA_dEa': 7.530965885284621, 'dE0_dEa': 0.12117506367971168, 'dn_dEa': -0.1834609555394028, 'name': 'C2H5N3O-3 <=> C2H5N3O-4'}, {'dA': 1.254901415169623, 'dE0': 0.008919548062033914, 'dn': -0.028941669643621788, 'dA_dEa': 5.6468497937742335, 'dE0_dEa': 0.0975023782842365, 'dn_dEa': -0.1375650940950967, 'name': 'C2H4N2O-5 <=> C2H4N2O-6'}, {'dA': 2.869996320651641, 'dE0': 0.021039628069499147, 'dn': -0.06828053071569379, 'dA_dEa': -19.982380370148856, 'dE0_dEa': -0.05138635633516462, 'dn_dEa': 0.48666691502408754, 'name': 'O=CNC(=O)N <=> NC(=NC=O)O'}, {'dA': 2.151805186921389, 'dE0': 0.015649329766730145, 'dn': -0.05078785735762701, 'dA_dEa': -5.256382819871643, 'dE0_dEa': 0.03658773393196781, 'dn_dEa': 0.1279966326170146, 'name': 'O=CNC(=O)N <=> OC(=N)NC=O'}, {'dA': 1.5848117532152952, 'dE0': 0.011394580053582772, 'dn': -0.03697755991602554, 'dA_dEa': 2.621108955301499, 'dE0_dEa': 0.08665152953379358, 'dn_dEa': -0.06387179238839313, 'name': 'O=CNC(=O)N <=> NC(=O)N=CO'}, {'dA': 2.0090909209005128, 'dE0': 0.01457834752411233, 'dn': -0.04731177397167566, 'dA_dEa': -2.206147252900935, 'dE0_dEa': 0.054003374761989964, 'dn_dEa': 0.05360509590947259, 'name': 'NC(=O)OC=N <=> N=COC(=N)O'}, {'dA': 1.8146821481599185, 'dE0': 0.013119224315353686, 'dn': -0.04257664927947287, 'dA_dEa': -0.2199176128883338, 'dE0_dEa': 0.06718732102582047, 'dn_dEa': 0.005327453967758806, 'name': 'NC(=O)C#C <=> OC(=N)C#C'}, {'dA': 2.166063002427404, 'dE0': 0.015756309797188447, 'dn': -0.05113514012481414, 'dA_dEa': -5.825522513709133, 'dE0_dEa': 0.035228580813115654, 'dn_dEa': 0.1418548441655358, 'name': 'NC(=O)N1CC1 <=> OC(=N)N1CC1'}, {'dA': 2.3570841299032463, 'dE0': 0.017189794667162688, 'dn': -0.05578783486023328, 'dA_dEa': -8.096724356584598, 'dE0_dEa': 0.015788777084991695, 'dn_dEa': 0.19718230638830517, 'name': 'NC(=O)NC=N <=> N=CNC(=N)O'}, {'dA': 2.1260356248478227, 'dE0': 0.015456026576643096, 'dn': -0.05016015832958802, 'dA_dEa': -4.431515525608765, 'dE0_dEa': 0.040126560777573476, 'dn_dEa': 0.10790484431990004, 'name': 'O=CNC=O <=> OC=NC=O'}, {'dA': 1.7264190663121806, 'dE0': 0.012457091821294904, 'dn': -0.04042674354713366, 'dA_dEa': 0.8376483791537693, 'dE0_dEa': 0.07469143302964597, 'dn_dEa': -0.020431872073192532, 'name': 'NC(=O)C(=O)N <=> OC(=N)C(=O)N'}, {'dA': 1.5034452235502251, 'dE0': 0.010783844085615977, 'dn': -0.03499577001312323, 'dA_dEa': 3.3889533816665995, 'dE0_dEa': 0.0848427406644828, 'dn_dEa': -0.08257111118649138, 'name': 'N=CNC=O <=> OC=NC=N'}, {'dA': 3.044523240641419, 'dE0': 0.02234846841705306, 'dn': -0.0725317999945933, 'dA_dEa': -20.28125391765069, 'dE0_dEa': -0.06515420878191039, 'dn_dEa': 0.4939522972592612, 'name': 'NC(=O)N <=> NC(=N)O'}, {'dA': 1.1577143994047243, 'dE0': 0.008189358916148602, 'dn': -0.02657481983382417, 'dA_dEa': 7.363167739872368, 'dE0_dEa': 0.11817845271759184, 'dn_dEa': -0.17937259143505244, 'name': 'NC(=O)NC=N <=> NC=NC(=O)N'}, {'dA': 1.2573570973800905, 'dE0': 0.008936871114725175, 'dn': -0.02900190442925733, 'dA_dEa': 6.400369613509577, 'dE0_dEa': 0.11268440401779113, 'dn_dEa': -0.1559250862477337, 'name': 'N=CNC=O <=> NC=NC=O'}]
""",
)

entry(
    index = 56,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(4.85602e+09,'s^-1'), n=0.739985, w0=(707000,'J/mol'), E0=(193742,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_N-5R!H->O
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': -2.6080451472501696, 'dE0': -0.01920023615133262, 'dn': 0.09714279505158496, 'dA_dEa': -54.03942144268843, 'dE0_dEa': -0.1467266690055021, 'dn_dEa': 1.8917720746953084, 'name': 'O=CNC(=O)N <=> NC(=NC=O)O'}, {'dA': -5.50599138186952, 'dE0': -0.039207714636548985, 'dn': 0.1986303787399154, 'dA_dEa': -3.595214646656194, 'dE0_dEa': 0.12813359833445997, 'dn_dEa': 0.12489173210270302, 'name': 'O=CNC(=O)N <=> NC(=O)N=CO'}, {'dA': -4.3397108592828975, 'dE0': -0.031135114300545937, 'dn': 0.15779885807892394, 'dA_dEa': -21.278930982323043, 'dE0_dEa': 0.021956842258017025, 'dn_dEa': 0.7448659918199704, 'name': 'O=CNC=O <=> OC=NC=O'}, {'dA': -5.68004293928022, 'dE0': -0.04041326238618116, 'dn': 0.20472344018496275, 'dA_dEa': -3.7086684995499475, 'dE0_dEa': 0.11090434982672401, 'dn_dEa': 0.12948525040655143, 'name': 'N=CNC=O <=> OC=NC=N'}, {'dA': -6.407030046984547, 'dE0': -0.04545267817085939, 'dn': 0.23017083896416524, 'dA_dEa': 2.709722812311931, 'dE0_dEa': 0.16387392942591184, 'dn_dEa': -0.09496149681624382, 'name': 'NC(=O)NC=N <=> NC=NC(=O)N'}, {'dA': -6.225695542504425, 'dE0': -0.044184510677244354, 'dn': 0.22383005468577738, 'dA_dEa': 0.6449796770132288, 'dE0_dEa': 0.1535990038239299, 'dn_dEa': -0.022672184579271903, 'name': 'N=CNC=O <=> NC=NC=O'}]
""",
)

entry(
    index = 57,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.82438,'s^-1'), n=3.5005, w0=(782000,'J/mol'), E0=(83092.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.0095089610383627e-06, var=0.12475859351858236, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O_Ext-1R!H-R
        Total Standard Deviation in ln(k): 0.7081011849094191"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.7081011849094191""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.7081011849094191
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.3997355157835554, 'dn_dEa': 0.0, 'name': 'O=CNC(=O)N <=> NC(=NC=O)O'}]
""",
)

entry(
    index = 58,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(3.13351e+10,'s^-1'), n=1.04551, w0=(696000,'J/mol'), E0=(308088,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 1.1399092899396923, 'dE0': 0.005041860398176728, 'dn': -0.011464737245687504, 'dA_dEa': -34.093587574940386, 'dE0_dEa': 0.2587945203224261, 'dn_dEa': 0.6104578391786899, 'name': 'O=CNC(=O)N <=> NC(=O)N=CO'}, {'dA': -2.0812443675135643, 'dE0': -0.020340272010169424, 'dn': 0.046220136658981295, 'dA_dEa': 16.657859615337557, 'dE0_dEa': 0.6266730489933883, 'dn_dEa': -0.29842211264059587, 'name': 'NC(=O)NC=N <=> NC=NC(=O)N'}]
""",
)

entry(
    index = 59,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.30649e-17,'s^-1'), n=8.88181, w0=(696000,'J/mol'), E0=(351768,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C_Ext-1R!H-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.2464499943308092, 'dn_dEa': 0.0, 'name': 'O=CNC(=O)N <=> NC(=O)N=CO'}]
""",
)

entry(
    index = 60,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O_Ext-4C-R",
    kinetics = ArrheniusBM(A=(7.46723e+09,'s^-1'), n=1.26362, w0=(707000,'J/mol'), E0=(155669,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O_Ext-4C-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.9964477934020363, 'dn_dEa': 0.0, 'name': 'NC(=O)NC=N <=> NC=NC(=O)N'}]
""",
)

entry(
    index = 61,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(7.10378e+09,'s^-1'), n=1.08011, w0=(707000,'J/mol'), E0=(118314,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O_Ext-1R!H-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 3.5729362056930496, 'dE0': 0.028308668156030573, 'dn': -0.053451563089857206, 'dA_dEa': -64.00145465210721, 'dE0_dEa': 0.08607989201147674, 'dn_dEa': 1.1126569646939295, 'name': 'O=CNC=O <=> OC=NC=O'}, {'dA': -2.793973888774867, 'dE0': -0.030347189233721813, 'dn': 0.057285773966361794, 'dA_dEa': 41.463567227695414, 'dE0_dEa': 0.9290723703351166, 'dn_dEa': -0.721549797716556, 'name': 'N=CNC=O <=> OC=NC=N'}]
""",
)

entry(
    index = 62,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing",
    kinetics = ArrheniusBM(A=(1.31843e+16,'s^-1'), n=-0.594645, w0=(651800,'J/mol'), E0=(283810,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06834214918355454, var=83.03772135212918, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing
        Total Standard Deviation in ln(k): 18.439869496605795"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing
Total Standard Deviation in ln(k): 18.439869496605795""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing
Total Standard Deviation in ln(k): 18.439869496605795
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.2503072566559845, 'dn_dEa': 0.0, 'name': 'N=CNC=O <=> OC=NC=N'}]
""",
)

entry(
    index = 63,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_N-2N-inRing",
    kinetics = ArrheniusBM(A=(6.3785e+07,'s^-1'), n=1.39836, w0=(707000,'J/mol'), E0=(187989,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_N-2N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_N-2N-inRing
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_N-2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_N-2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.4012695221723326, 'dn_dEa': 0.0, 'name': 'O=CNC=O <=> OC=NC=O'}]
""",
)

entry(
    index = 64,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.08866e+12,'s^-1'), n=0.904623, w0=(798000,'J/mol'), E0=(128315,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-1R!H-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.104003559924187, 'dn_dEa': 0.0, 'name': 'N=CNC=O <=> NC=NC=O'}]
""",
)

entry(
    index = 65,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.8372e-11,'s^-1'), n=7.16536, w0=(747000,'J/mol'), E0=(112893,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008977972048432677, var=25.44819571736246, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R
        Total Standard Deviation in ln(k): 10.135685333227709"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 10.135685333227709""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 10.135685333227709
sensitivities = [{'dA': -0.08646579658134598, 'dE0': -0.0020065173280944407, 'dn': 0.004091849641008489, 'dA_dEa': -1.0101950695152742, 'dE0_dEa': 0.18128799261861778, 'dn_dEa': 0.017954927773363178, 'name': 'O=CNC(=O)N <=> OC(=N)NC=O'}, {'dA': -0.45223535965282485, 'dE0': -0.005212108629466024, 'dn': 0.01061934793844857, 'dA_dEa': 6.282386867547255, 'dE0_dEa': 0.23210653483292332, 'dn_dEa': -0.1121943731081159, 'name': 'NC(=O)OC=N <=> N=COC(=N)O'}, {'dA': -0.9613397853876997, 'dE0': -0.009675259600106388, 'dn': 0.01970444740315939, 'dA_dEa': 14.709254461090126, 'dE0_dEa': 0.3009535419733655, 'dn_dEa': -0.2625902496497489, 'name': 'NC(=O)C#C <=> OC(=N)C#C'}, {'dA': -0.043954273976969785, 'dE0': -0.0016343960759285076, 'dn': 0.003333082144679257, 'dA_dEa': -2.21155111126261, 'dE0_dEa': 0.17806582218639733, 'dn_dEa': 0.03939261846444114, 'name': 'NC(=O)N1CC1 <=> OC(=N)N1CC1'}, {'dA': 0.45443981748155016, 'dE0': 0.002730783328970262, 'dn': -0.005561885026671341, 'dA_dEa': -10.82231616112969, 'dE0_dEa': 0.0966244524633211, 'dn_dEa': 0.19307632253046178, 'name': 'NC(=O)NC=N <=> N=CNC(=N)O'}, {'dA': -1.2004296047793062, 'dE0': -0.011761761281762644, 'dn': 0.023973399724025467, 'dA_dEa': 18.266651964806492, 'dE0_dEa': 0.33102461473078965, 'dn_dEa': -0.3260816275860893, 'name': 'NC(=O)C(=O)N <=> OC(=N)C(=O)N'}, {'dA': 2.262329859704231, 'dE0': 0.018560724220849596, 'dn': -0.03782885785887137, 'dA_dEa': -50.84578737912642, 'dE0_dEa': -0.22761243422309782, 'dn_dEa': 0.907386267082346, 'name': 'NC(=O)N <=> NC(=N)O'}]
""",
)

entry(
    index = 66,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O",
    kinetics = ArrheniusBM(A=(2.61055e-12,'s^-1'), n=7.38016, w0=(798000,'J/mol'), E0=(97626.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.012281183960210522, var=4.719030378538201, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O
        Total Standard Deviation in ln(k): 4.385809279805604"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O
Total Standard Deviation in ln(k): 4.385809279805604""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O
Total Standard Deviation in ln(k): 4.385809279805604
sensitivities = [{'dA': 0.496348509678112, 'dE0': 0.0029404610760523846, 'dn': -0.00572355961951516, 'dA_dEa': -9.15651276524899, 'dE0_dEa': 0.14438019659441445, 'dn_dEa': 0.158823896112897, 'name': 'O=CNC(=O)N <=> OC(=N)NC=O'}, {'dA': 0.035551066769560796, 'dE0': -0.0011772468756384733, 'dn': 0.00227219537232086, 'dA_dEa': 0.4830288327220521, 'dE0_dEa': 0.21492246584608052, 'dn_dEa': -0.008455051628429343, 'name': 'NC(=O)OC=N <=> N=COC(=N)O'}, {'dA': -0.6091200576073379, 'dE0': -0.006925132184000729, 'dn': 0.013461540495069728, 'dA_dEa': 11.181742698508922, 'dE0_dEa': 0.30454330958425163, 'dn_dEa': -0.1941183474756536, 'name': 'NC(=O)C#C <=> OC(=N)C#C'}, {'dA': 0.5401320922403015, 'dE0': 0.003333284291050299, 'dn': -0.006482927624129475, 'dA_dEa': -10.967343459033927, 'dE0_dEa': 0.13690369856802437, 'dn_dEa': 0.19024748523225454, 'name': 'NC(=O)N1CC1 <=> OC(=N)N1CC1'}, {'dA': 1.1688922174003702, 'dE0': 0.008941793090597457, 'dn': -0.017395529189561332, 'dA_dEa': -21.42357967144784, 'dE0_dEa': 0.03637364612128742, 'dn_dEa': 0.37170643863989167, 'name': 'NC(=O)NC=N <=> N=CNC(=N)O'}, {'dA': -0.8934141719266637, 'dE0': -0.009464933241829473, 'dn': 0.018394764394197988, 'dA_dEa': 15.651034716368475, 'dE0_dEa': 0.3431592027249584, 'dn_dEa': -0.27167827963164626, 'name': 'NC(=O)C(=O)N <=> OC(=N)C(=O)N'}]
""",
)

entry(
    index = 67,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_N-3NOS->O",
    kinetics = ArrheniusBM(A=(5.99955e-18,'s^-1'), n=8.92667, w0=(696000,'J/mol'), E0=(104007,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_N-3NOS->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_N-3NOS->O
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_N-3NOS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_N-3NOS->O
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.5991679053779058, 'dE0': 0.003588117544512839, 'dn': -0.006934809371153042, 'dA_dEa': -6.908312557233438, 'dE0_dEa': 0.2110236177507334, 'dn_dEa': 0.1199171376332933, 'name': 'O=CNC(=O)N <=> OC(=N)NC=O'}, {'dA': 0.015008814106211564, 'dE0': -0.001657388688638441, 'dn': 0.0032123175042405175, 'dA_dEa': 4.7818884098061725, 'dE0_dEa': 0.29731189913125144, 'dn_dEa': -0.08312969220510787, 'name': 'NC(=O)OC=N <=> N=COC(=N)O'}, {'dA': 0.6560033232113239, 'dE0': 0.004098461088010592, 'dn': -0.007922071987190624, 'dA_dEa': -8.981244377584398, 'dE0_dEa': 0.20288415351029843, 'dn_dEa': 0.1559191731664933, 'name': 'NC(=O)N1CC1 <=> OC(=N)N1CC1'}, {'dA': 1.43104177795921, 'dE0': 0.011062409771430618, 'dn': -0.02138383876232929, 'dA_dEa': -22.129260178931126, 'dE0_dEa': 0.07609189388506589, 'dn_dEa': 0.38429507942626767, 'name': 'NC(=O)NC=N <=> N=CNC(=N)O'}, {'dA': -1.1287347741168041, 'dE0': -0.01193615890907241, 'dn': 0.023077745021115842, 'dA_dEa': 23.50471807541769, 'dE0_dEa': 0.45685912664721345, 'dn_dEa': -0.408331201654742, 'name': 'NC(=O)C(=O)N <=> OC(=N)C(=O)N'}]
""",
)

entry(
    index = 68,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.83426e-12,'s^-1'), n=7.39498, w0=(798000,'J/mol'), E0=(101379,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01931713628791539, var=2.0216086590715365, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R
        Total Standard Deviation in ln(k): 2.89893371093887"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.89893371093887""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.89893371093887
sensitivities = [{'dA': 2.8160712745804775, 'dE0': 0.02069728439539886, 'dn': -0.03861013349776915, 'dA_dEa': -48.20296146028189, 'dE0_dEa': 0.2743896554427599, 'dn_dEa': 0.8034137309840813, 'name': 'NC(=O)N1CC1 <=> OC(=N)N1CC1'}, {'dA': -1.6353786656646132, 'dE0': -0.019080904261479955, 'dn': 0.035589302702262994, 'dA_dEa': 36.33001085806287, 'dE0_dEa': 0.9355727407833181, 'dn_dEa': -0.6056198702722363, 'name': 'NC(=O)C(=O)N <=> OC(=N)C(=O)N'}]
""",
)

entry(
    index = 69,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_Ext-3NO-R",
    kinetics = ArrheniusBM(A=(8.00067e+12,'s^-1'), n=0.391729, w0=(798000,'J/mol'), E0=(133048,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_Ext-3NO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_Ext-3NO-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_Ext-3NO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_Ext-3NO-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.2897268020713002, 'dn_dEa': 0.0, 'name': 'NC(=O)C(=O)N <=> OC(=N)C(=O)N'}]
""",
)

entry(
    index = 70,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N",
    kinetics = ArrheniusBM(A=(6.91728e-07,'s^-1'), n=5.62342, w0=(779800,'J/mol'), E0=(106545,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006515153720890275, var=0.8806591803136841, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N
        Total Standard Deviation in ln(k): 1.897682153588295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N
Total Standard Deviation in ln(k): 1.897682153588295""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N
Total Standard Deviation in ln(k): 1.897682153588295
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.3665211011827767, 'dn_dEa': 0.0, 'name': 'NC(=O)N1CC1 <=> OC(=N)N1CC1'}]
""",
)

entry(
    index = 71,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N",
    kinetics = ArrheniusBM(A=(8.46061e-15,'s^-1'), n=7.98481, w0=(798000,'J/mol'), E0=(96853.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00263383782615601, var=0.4396759609029318, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N
        Total Standard Deviation in ln(k): 1.335918740070374"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 1.335918740070374""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 1.335918740070374
sensitivities = [{'dA': -1.4293898611087894, 'dE0': -0.017907462318431263, 'dn': 0.03197152362491392, 'dA_dEa': 33.19381867854798, 'dE0_dEa': 0.9650930592404571, 'dn_dEa': -0.5504854585206524, 'name': 'NC(=O)OC=N <=> N=COC(=N)O'}, {'dA': 2.4327778956954496, 'dE0': 0.017943997459984238, 'dn': -0.03203585382918463, 'dA_dEa': -38.58423260531366, 'dE0_dEa': 0.3519177058714769, 'dn_dEa': 0.6390575909468955, 'name': 'NC(=O)NC=N <=> N=CNC(=N)O'}]
""",
)

entry(
    index = 72,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.20077e-11,'s^-1'), n=7.05311, w0=(798000,'J/mol'), E0=(100604,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_Ext-5R!H-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.3800277797985767, 'dn_dEa': 0.0, 'name': 'NC(=O)OC=N <=> N=COC(=N)O'}]
""",
)

entry(
    index = 73,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_6R!H->N",
    kinetics = ArrheniusBM(A=(7.35011e-13,'s^-1'), n=7.36802, w0=(798000,'J/mol'), E0=(90879,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_6R!H->N
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.4503691120385525, 'dn_dEa': 0.0, 'name': 'NC(=O)NC=N <=> N=CNC(=N)O'}]
""",
)

entry(
    index = 74,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_N-6R!H->N",
    kinetics = ArrheniusBM(A=(1.29627e-12,'s^-1'), n=7.28519, w0=(798000,'J/mol'), E0=(101095,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_N-6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_N-6R!H->N
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.3867765266572771, 'dn_dEa': 0.0, 'name': 'O=CNC(=O)N <=> OC(=N)NC=O'}]
""",
)

entry(
    index = 75,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_5R!H->O_Ext-4R-R",
    kinetics = ArrheniusBM(A=(1.88124e+11,'s^-1'), n=0.620515, w0=(707000,'J/mol'), E0=(161496,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_5R!H->O_Ext-4R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_5R!H->O_Ext-4R-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_5R!H->O_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_5R!H->O_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.3226964833232273, 'dn_dEa': 0.0, 'name': 'NC(=O)C#C <=> OC(=N)C#C'}]
""",
)

entry(
    index = 76,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O_Ext-1R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(181.401,'s^-1'), n=2.92819, w0=(782000,'J/mol'), E0=(87394.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O_Ext-1R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O_Ext-1R!H-R_Ext-5R!H-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.003494431998648, 'dn_dEa': 0.0, 'name': 'C2H5N3O-3 <=> C2H5N3O-4'}]
""",
)

entry(
    index = 77,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O",
    kinetics = ArrheniusBM(A=(1.07004e+24,'s^-1'), n=-2.80801, w0=(707000,'J/mol'), E0=(245324,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06960442888511502, var=70.04500144656065, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O
        Total Standard Deviation in ln(k): 16.95309309986816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O
Total Standard Deviation in ln(k): 16.95309309986816""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O
Total Standard Deviation in ln(k): 16.95309309986816
sensitivities = [{'dA': 1.021387356415217, 'dE0': 0.008311781312072495, 'dn': -0.025106381671284338, 'dA_dEa': 3.260945436141331, 'dE0_dEa': 0.03511770163982938, 'dn_dEa': -0.08102279678346426, 'name': 'CH2OS <=> CH2OS-2'}, {'dA': 1.0199159463405452, 'dE0': 0.008299893213008195, 'dn': -0.025069753951193496, 'dA_dEa': 3.2343090340617673, 'dE0_dEa': 0.03474922042774957, 'dn_dEa': -0.08036076083362079, 'name': 'C2H4OS <=> C2H4OS-2'}, {'dA': 1.0189027592543154, 'dE0': 0.008292020296303867, 'dn': -0.025044420298393287, 'dA_dEa': 3.234328090004369, 'dE0_dEa': 0.03474934295995913, 'dn_dEa': -0.08036124589884665, 'name': 'C3H6OS <=> C3H6OS-2'}, {'dA': 2.030084186305682, 'dE0': 0.016206464439214974, 'dn': -0.04898222271957221, 'dA_dEa': -9.34256224986388, 'dE0_dEa': -0.025518863622475147, 'dn_dEa': 0.23206835760718078, 'name': 'C2H4N2O2 <=> C2H4N2O2-2'}, {'dA': 1.281460604209669, 'dE0': 0.010056548804426786, 'dn': -0.030382540343846832, 'dA_dEa': 1.0695322144799246, 'dE0_dEa': 0.04753074753510767, 'dn_dEa': -0.026610477086807433, 'name': 'C2H4N2O2-3 <=> C2H4N2O2-4'}, {'dA': 0.6919776370396187, 'dE0': 0.005213798408282611, 'dn': -0.015736795139010266, 'dA_dEa': 8.236793445459709, 'dE0_dEa': 0.11146129745716457, 'dn_dEa': -0.20468463638191645, 'name': 'C2H4N2O2-5 <=> C2H4N2O2-6'}, {'dA': 1.1329884789291893, 'dE0': 0.008836824612123146, 'dn': -0.02669373596416009, 'dA_dEa': 2.774515012502782, 'dE0_dEa': 0.06105046931872723, 'dn_dEa': -0.06896725604645439, 'name': 'C2H4N2O2-7 <=> C2H4N2O2-8'}, {'dA': 0.9302282517254982, 'dE0': 0.007171098980899154, 'dn': -0.021656143901572614, 'dA_dEa': 5.058624796932977, 'dE0_dEa': 0.0816034116656109, 'dn_dEa': -0.12571894425863414, 'name': 'C3H3NO <=> C3H3NO-2'}, {'dA': 1.2961863359583254, 'dE0': 0.01017755434189128, 'dn': -0.030748391502925514, 'dA_dEa': 0.7790923154172594, 'dE0_dEa': 0.04652247095078022, 'dn_dEa': -0.01939135171060391, 'name': 'C3H6N2O <=> C3H6N2O-2'}, {'dA': 1.4948969569223405, 'dE0': 0.011809981371124123, 'dn': -0.035685381562633865, 'dA_dEa': -0.9962618048310321, 'dE0_dEa': 0.028658767421609478, 'dn_dEa': 0.024715627804435373, 'name': 'C2H5N3O <=> C2H5N3O-2'}, {'dA': 1.254947771695352, 'dE0': 0.00983868396217862, 'dn': -0.029723846989069613, 'dA_dEa': 1.5372921635014607, 'dE0_dEa': 0.05175280241255357, 'dn_dEa': -0.03822873624263363, 'name': 'C2H3NO2 <=> C2H3NO2-2'}, {'dA': 0.8389682502213205, 'dE0': 0.0064213582855778715, 'dn': -0.019388788866378022, 'dA_dEa': 6.08577385720888, 'dE0_dEa': 0.0907008834832247, 'dn_dEa': -0.15124043132356282, 'name': 'C2H4N2O2-9 <=> C2H4N2O2-10'}, {'dA': 0.6069703530063422, 'dE0': 0.00451544869679195, 'dn': -0.013624781007268933, 'dA_dEa': 8.53372725517781, 'dE0_dEa': 0.10972147501239742, 'dn_dEa': -0.21205856665354345, 'name': 'C2H4N2O <=> C2H4N2O-2'}, {'dA': 2.209253236033847, 'dE0': 0.01767858276472832, 'dn': -0.05343361803858045, 'dA_dEa': -8.319210117698567, 'dE0_dEa': -0.030993662219769964, 'dn_dEa': 0.20665691092402777, 'name': 'CH4N2O <=> CH4N2O-2'}, {'dA': 1.3890432136617756, 'dE0': 0.01094054515185883, 'dn': -0.03305537411891425, 'dA_dEa': -0.8031034540768364, 'dE0_dEa': 0.06375833554503568, 'dn_dEa': 0.019888187942479544, 'name': 'C2H4N2O2-11 <=> C2H4N2O2-12'}, {'dA': 1.7839762255784397, 'dE0': 0.014184913303081552, 'dn': -0.04286755015330703, 'dA_dEa': -5.255635739564692, 'dE0_dEa': 0.005440826117611433, 'dn_dEa': 0.13053231510229707, 'name': 'C2H4N2O2-13 <=> C2H4N2O2-14'}, {'dA': 1.2523646762404852, 'dE0': 0.009817582127388131, 'dn': -0.02965962695776465, 'dA_dEa': 1.917983651354971, 'dE0_dEa': 0.0719398332966282, 'dn_dEa': -0.04769829038940688, 'name': 'C2H3NO2-3 <=> C2H3NO2-4'}, {'dA': 1.252502017607209, 'dE0': 0.009818624188214383, 'dn': -0.02966307036389192, 'dA_dEa': 1.8805555997511842, 'dE0_dEa': 0.06951234581839426, 'dn_dEa': -0.04676383919449642, 'name': 'C2H3NO2-3 <=> C2H3NO2-4'}, {'dA': 1.6368886235158113, 'dE0': 0.012979772866409852, 'dn': -0.03921200319252937, 'dA_dEa': -7.192725799900838, 'dE0_dEa': 0.026882615852334563, 'dn_dEa': 0.17862356717284927, 'name': 'C2H4N2O-3 <=> C2H4N2O-4'}, {'dA': 1.0212650635069724, 'dE0': 0.00831082207456755, 'dn': -0.025103327730444203, 'dA_dEa': 3.481863434191041, 'dE0_dEa': 0.03782115531812949, 'dn_dEa': -0.08651233835529462, 'name': 'SC=O <=> OC=S'}, {'dA': 1.019925167327186, 'dE0': 0.008299945568773852, 'dn': -0.025069991412117302, 'dA_dEa': 3.4327446397103727, 'dE0_dEa': 0.03717028474865641, 'dn_dEa': -0.08529173714796885, 'name': 'CC(=O)S <=> CC(=S)O'}, {'dA': 1.0201273434021787, 'dE0': 0.00830146753544754, 'dn': -0.025075063855827945, 'dA_dEa': 3.4643590139559683, 'dE0_dEa': 0.03755731695784208, 'dn_dEa': -0.08607729567100686, 'name': 'CCC(=O)S <=> CCC(=S)O'}]
""",
)

entry(
    index = 78,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O",
    kinetics = ArrheniusBM(A=(5.30991e+18,'s^-1'), n=-1.44644, w0=(615000,'J/mol'), E0=(326412,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10690871308720216, var=25.722674424570492, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O
        Total Standard Deviation in ln(k): 10.436135195906743"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O
Total Standard Deviation in ln(k): 10.436135195906743""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O
Total Standard Deviation in ln(k): 10.436135195906743
sensitivities = [{'dA': 0.3669034841467371, 'dE0': 0.00033554402701342325, 'dn': -0.0015621734963998427, 'dA_dEa': -0.31238881653198436, 'dE0_dEa': 0.30851109792786996, 'dn_dEa': 0.014476767783002465, 'name': 'CH2OS <=> CH2OS-2'}, {'dA': 0.3301462695822019, 'dE0': -3.4620908780633615e-05, 'dn': 0.0001373588228076864, 'dA_dEa': 0.21944495520023397, 'dE0_dEa': 0.3081569276657736, 'dn_dEa': -0.010163751988873178, 'name': 'C2H4OS <=> C2H4OS-2'}, {'dA': 0.3183775105615534, 'dE0': -0.00014821066842956828, 'dn': 0.0006841902796406431, 'dA_dEa': 0.21725692677068315, 'dE0_dEa': 0.3081427656253842, 'dn_dEa': -0.010058174552773731, 'name': 'C3H6OS <=> C3H6OS-2'}]
""",
)

entry(
    index = 79,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R_3NOS->O",
    kinetics = ArrheniusBM(A=(1.80649e-12,'s^-1'), n=7.52975, w0=(798000,'J/mol'), E0=(96352.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R_3NOS->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R_3NOS->O
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R_3NOS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R_3NOS->O
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.504342504672961, 'dE0': 4.575187033029025e-05, 'dn': -0.0002158391754186415, 'dA_dEa': 0.04191012563659519, 'dE0_dEa': 0.4615107656917947, 'dn_dEa': -0.0019493670533066425, 'name': 'C2H4OS <=> C2H4OS-2'}, {'dA': 0.49521298157101284, 'dE0': -4.515412514514593e-05, 'dn': 0.00021327392322313476, 'dA_dEa': 0.03513906874275495, 'dE0_dEa': 0.4614434484903782, 'dn_dEa': -0.0016310092028784685, 'name': 'C3H6OS <=> C3H6OS-2'}]
""",
)

entry(
    index = 80,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R_N-3NOS->O",
    kinetics = ArrheniusBM(A=(3.03331e-17,'s^-1'), n=8.87366, w0=(696000,'J/mol'), E0=(111857,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R_N-3NOS->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R_N-3NOS->O
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R_N-3NOS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R_N-3NOS->O
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330828247, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.9654120915248895, 'dn_dEa': 0.0, 'name': 'C3H6OS <=> C3H6OS-2'}]
""",
)

entry(
    index = 81,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O_Ext-5R!H-R_6R!H->N",
    kinetics = ArrheniusBM(A=(3.31385e-15,'s^-1'), n=8.01833, w0=(798000,'J/mol'), E0=(85225.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O_Ext-5R!H-R_6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O_Ext-5R!H-R_6R!H->N
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.7899033709702667, 'dE0': 0.0058138210064712535, 'dn': -0.019282550743373157, 'dA_dEa': -9.74463358492202, 'dE0_dEa': -0.026273361790591858, 'dn_dEa': 0.2575505703419435, 'name': 'C2H4N2O2 <=> C2H4N2O2-2'}, {'dA': 0.05884365375941707, 'dE0': -6.102481187071669e-06, 'dn': 4.329904105846421e-05, 'dA_dEa': -0.09843868334870028, 'dE0_dEa': 0.03803041617654264, 'dn_dEa': 0.0025672773995054224, 'name': 'C2H4N2O2-3 <=> C2H4N2O2-4'}, {'dA': -0.5160263046591353, 'dE0': -0.0045831043268672825, 'dn': 0.015240016820884193, 'dA_dEa': 6.628940543641113, 'dE0_dEa': 0.09663407192996798, 'dn_dEa': -0.17528049041377902, 'name': 'C2H4N2O2-5 <=> C2H4N2O2-6'}, {'dA': -0.08602037867611993, 'dE0': -0.0011594488176598966, 'dn': 0.0038728001034909225, 'dA_dEa': 1.5381145704138095, 'dE0_dEa': 0.05054959824282695, 'dn_dEa': -0.04070002572902893, 'name': 'C2H4N2O2-7 <=> C2H4N2O2-8'}, {'dA': -0.2837479241879805, 'dE0': -0.0027337114609185817, 'dn': 0.009099740315879672, 'dA_dEa': 3.640848892196803, 'dE0_dEa': 0.0690959637949198, 'dn_dEa': -0.0962835404348031, 'name': 'C3H3NO <=> C3H3NO-2'}, {'dA': 0.07324709137713466, 'dE0': 0.00010858391639675615, 'dn': -0.0003374530392276111, 'dA_dEa': -0.3174782911657198, 'dE0_dEa': 0.037643343489172296, 'dn_dEa': 0.008352253399450475, 'name': 'C3H6N2O <=> C3H6N2O-2'}, {'dA': 0.2670011796617483, 'dE0': 0.0016512147241695484, 'dn': -0.00545935314453947, 'dA_dEa': -1.98838077646912, 'dE0_dEa': 0.021061075778678846, 'dn_dEa': 0.05252228680620144, 'name': 'C2H5N3O <=> C2H5N3O-2'}, {'dA': 0.03276082276571307, 'dE0': -0.0002137176703784115, 'dn': 0.0007328198432884583, 'dA_dEa': 0.3618383743991104, 'dE0_dEa': 0.04206226956618286, 'dn_dEa': -0.009601418571035867, 'name': 'C2H3NO2 <=> C2H3NO2-2'}, {'dA': -0.37272396945379976, 'dE0': -0.00344214477989218, 'dn': 0.01145181771480037, 'dA_dEa': 4.6269311391609715, 'dE0_dEa': 0.07759382965756326, 'dn_dEa': -0.12235790464586682, 'name': 'C2H4N2O2-9 <=> C2H4N2O2-10'}, {'dA': -0.5988838485038832, 'dE0': -0.005242808377726127, 'dn': 0.017430357145355267, 'dA_dEa': 6.892502137055039, 'dE0_dEa': 0.09454476726363083, 'dn_dEa': -0.18224522160178772, 'name': 'C2H4N2O <=> C2H4N2O-2'}, {'dA': 0.9638371482837367, 'dE0': 0.007199283287496804, 'dn': -0.02388024989644508, 'dA_dEa': -8.820424945443412, 'dE0_dEa': -0.03282336040708579, 'dn_dEa': 0.23313121367785697, 'name': 'CH4N2O <=> CH4N2O-2'}, {'dA': 0.16461937228664106, 'dE0': 0.0008358373099246267, 'dn': -0.0027529755956753567, 'dA_dEa': -1.7127631794766285, 'dE0_dEa': 0.056822757639508135, 'dn_dEa': 0.045208831149792045, 'name': 'C2H4N2O2-11 <=> C2H4N2O2-12'}, {'dA': 0.5491375361562129, 'dE0': 0.003897528022996645, 'dn': -0.012917643055594128, 'dA_dEa': -5.926598287991012, 'dE0_dEa': 0.0014980385621668208, 'dn_dEa': 0.15662176524782428, 'name': 'C2H4N2O2-13 <=> C2H4N2O2-14'}, {'dA': 0.03038426956436859, 'dE0': -0.00023259764608513428, 'dn': 0.0007956608637523268, 'dA_dEa': 0.8014209678305123, 'dE0_dEa': 0.0626359243723941, 'dn_dEa': -0.02123760750792562, 'name': 'C2H3NO2-3 <=> C2H3NO2-4'}, {'dA': 0.030272427293812635, 'dE0': -0.00023345058858814123, 'dn': 0.0007986318020878438, 'dA_dEa': 0.8391589605950358, 'dE0_dEa': 0.06077089405280879, 'dn_dEa': -0.022246881307981275, 'name': 'C2H3NO2-3 <=> C2H3NO2-4'}, {'dA': 0.4262030714290902, 'dE0': 0.0029120294861389264, 'dn': -0.009670488024556176, 'dA_dEa': -7.617382865130424, 'dE0_dEa': 0.025449256878063195, 'dn_dEa': 0.20128109841501107, 'name': 'C2H4N2O-3 <=> C2H4N2O-4'}, {'dA': -0.17141476322992344, 'dE0': -0.001446956007875286, 'dn': 0.004826989374537879, 'dA_dEa': 2.3101164535666343, 'dE0_dEa': 0.027619596315914485, 'dn_dEa': -0.061074795659083754, 'name': 'SC=O <=> OC=S'}, {'dA': -0.1732070218594308, 'dE0': -0.0014608506999066535, 'dn': 0.0048745143409343345, 'dA_dEa': 2.259487424407318, 'dE0_dEa': 0.0269691139152647, 'dn_dEa': -0.05973603395065078, 'name': 'CC(=O)S <=> CC(=S)O'}, {'dA': -0.17325825868932074, 'dE0': -0.001461297396963517, 'dn': 0.004875853050811647, 'dA_dEa': 2.291409722076562, 'dE0_dEa': 0.027350729939788244, 'dn_dEa': -0.060580019339714776, 'name': 'CCC(=O)S <=> CCC(=S)O'}]
""",
)

entry(
    index = 82,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O_Ext-5R!H-R_N-6R!H->N",
    kinetics = ArrheniusBM(A=(9.90794e-14,'s^-1'), n=7.92259, w0=(798000,'J/mol'), E0=(95420.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O_Ext-5R!H-R_N-6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O_Ext-5R!H-R_N-6R!H->N
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.6234659889772918, 'dE0': 0.0043632598976801025, 'dn': -0.015484864559787934, 'dA_dEa': -9.220125974298682, 'dE0_dEa': -0.01983301773492127, 'dn_dEa': 0.2544835773583859, 'name': 'C2H4N2O2 <=> C2H4N2O2-2'}, {'dA': -0.09968526386218134, 'dE0': -0.0012532160742916955, 'dn': 0.004479127358931462, 'dA_dEa': -0.03168415499743909, 'dE0_dEa': 0.038931779745765574, 'dn_dEa': 0.0008400340652665546, 'name': 'C2H4N2O2-3 <=> C2H4N2O2-4'}, {'dA': -0.6678974148136189, 'dE0': -0.005666905393388442, 'dn': 0.0201654844126924, 'dA_dEa': 6.456711500724844, 'dE0_dEa': 0.09441792922186071, 'dn_dEa': -0.17829249715300527, 'name': 'C2H4N2O2-5 <=> C2H4N2O2-6'}, {'dA': -0.2426203158379093, 'dE0': -0.002363576716326203, 'dn': 0.008425029588830275, 'dA_dEa': 1.5181748107819255, 'dE0_dEa': 0.05046274384650988, 'dn_dEa': -0.04194834684558806, 'name': 'C2H4N2O2-7 <=> C2H4N2O2-8'}, {'dA': -0.43819034452324096, 'dE0': -0.003882635379785785, 'dn': 0.013824064230696698, 'dA_dEa': 3.5996423964780946, 'dE0_dEa': 0.06842871916607872, 'dn_dEa': -0.09941775079001297, 'name': 'C3H3NO <=> C3H3NO-2'}, {'dA': -0.08540717331230016, 'dE0': -0.0011423191973313847, 'dn': 0.004084954563420886, 'dA_dEa': -0.22006635676688127, 'dE0_dEa': 0.0388268516208781, 'dn_dEa': 0.006030069729834215, 'name': 'C3H6N2O <=> C3H6N2O-2'}, {'dA': 0.10613212929301344, 'dE0': 0.0003454916234878033, 'dn': -0.001202780065471516, 'dA_dEa': -1.8756155175465428, 'dE0_dEa': 0.022678027104811444, 'dn_dEa': 0.05174208506556531, 'name': 'C2H5N3O <=> C2H5N3O-2'}, {'dA': -0.1252476101036986, 'dE0': -0.0014518242229261413, 'dn': 0.0051847946637594055, 'dA_dEa': 0.42664949559428045, 'dE0_dEa': 0.04285396983022799, 'dn_dEa': -0.011817972346388492, 'name': 'C2H3NO2 <=> C2H3NO2-2'}, {'dA': -0.5262546531419912, 'dE0': -0.004566662937381648, 'dn': 0.016255224362573248, 'dA_dEa': 4.501900523935339, 'dE0_dEa': 0.07611111108891874, 'dn_dEa': -0.12432496527308166, 'name': 'C2H4N2O2-9 <=> C2H4N2O2-10'}, {'dA': -0.7500252738364681, 'dE0': -0.006304748042103155, 'dn': 0.022432790056386827, 'dA_dEa': 6.6691807824311296, 'dE0_dEa': 0.09185287167434118, 'dn_dEa': -0.1841507617082282, 'name': 'C2H4N2O <=> C2H4N2O-2'}, {'dA': 0.7950880659742575, 'dE0': 0.005697062035504185, 'dn': -0.02022245966030681, 'dA_dEa': -8.41792651541255, 'dE0_dEa': -0.027633984524970855, 'dn_dEa': 0.2323523847632653, 'name': 'CH4N2O <=> CH4N2O-2'}, {'dA': 0.0038740212575665116, 'dE0': -0.0004485798317046075, 'dn': 0.0016203082345519052, 'dA_dEa': -1.4051846326791788, 'dE0_dEa': 0.06019005065391327, 'dn_dEa': 0.038717989923891055, 'name': 'C2H4N2O2-11 <=> C2H4N2O2-12'}, {'dA': 0.3856279879608662, 'dE0': 0.0025162496964110594, 'dn': -0.00891880221148563, 'dA_dEa': -5.570925658457685, 'dE0_dEa': 0.005865790261622982, 'dn_dEa': 0.15374488920715362, 'name': 'C2H4N2O2-13 <=> C2H4N2O2-14'}, {'dA': -0.1275203184692016, 'dE0': -0.001469496983186951, 'dn': 0.005247527911267094, 'dA_dEa': 0.9528064142126863, 'dE0_dEa': 0.06416050674087777, 'dn_dEa': -0.02636500817865798, 'name': 'C2H3NO2-3 <=> C2H3NO2-4'}, {'dA': -0.12748892194471023, 'dE0': -0.0014692539937184283, 'dn': 0.00524666159012304, 'dA_dEa': 0.8940961320949999, 'dE0_dEa': 0.06156618010440775, 'dn_dEa': -0.024737114395281045, 'name': 'C2H3NO2-3 <=> C2H3NO2-4'}, {'dA': 0.2545794488426903, 'dE0': 0.0014964959271605534, 'dn': -0.005301760808649293, 'dA_dEa': -7.005875122729205, 'dE0_dEa': 0.03247735845144943, 'dn_dEa': 0.19331986730979328, 'name': 'C2H4N2O-3 <=> C2H4N2O-4'}]
""",
)

entry(
    index = 83,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(2.63375e-12,'s^-1'), n=7.38822, w0=(798000,'J/mol'), E0=(100901,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01164948583439061, var=1.058298597701629, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
        Total Standard Deviation in ln(k): 2.091614027963185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 2.091614027963185""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 2.091614027963185
sensitivities = [{'dA': 0.25338157867518823, 'dE0': 0.0011526553068443432, 'dn': -0.0036731922426666546, 'dA_dEa': -14.784123993029604, 'dE0_dEa': -0.02370927718687114, 'dn_dEa': 0.381575259946664, 'name': 'C2H4N2O2 <=> C2H4N2O2-2'}, {'dA': -1.1174979486680123, 'dE0': -0.00992948445028474, 'dn': 0.03171489702435736, 'dA_dEa': 0.707026665429289, 'dE0_dEa': 0.0781280738133442, 'dn_dEa': -0.018317416123357907, 'name': 'C2H4N2O2-3 <=> C2H4N2O2-4'}, {'dA': -1.3901330134837164, 'dE0': -0.012133146955404413, 'dn': 0.03875285489017997, 'dA_dEa': 3.2675537214149886, 'dE0_dEa': 0.09792824992897557, 'dn_dEa': -0.08440394486255054, 'name': 'C2H4N2O2-7 <=> C2H4N2O2-8'}, {'dA': -1.7624243889662048, 'dE0': -0.01514229736384821, 'dn': 0.0483634049227512, 'dA_dEa': 6.852457453915806, 'dE0_dEa': 0.13025207869824654, 'dn_dEa': -0.17694989265774053, 'name': 'C3H3NO <=> C3H3NO-2'}, {'dA': -1.0901510332958033, 'dE0': -0.009708536051155736, 'dn': 0.031008913546852476, 'dA_dEa': 0.2703925625553736, 'dE0_dEa': 0.07719315426046358, 'dn_dEa': -0.007032263290976499, 'name': 'C3H6N2O <=> C3H6N2O-2'}, {'dA': -0.7255383529081971, 'dE0': -0.00676134146102321, 'dn': 0.021596627159224106, 'dA_dEa': -2.6460932139332343, 'dE0_dEa': 0.047514187863960576, 'dn_dEa': 0.06825975620682768, 'name': 'C2H5N3O <=> C2H5N3O-2'}, {'dA': -1.9301982920547538, 'dE0': -0.01649830683702464, 'dn': 0.05269444634516291, 'dA_dEa': 8.440909679094096, 'dE0_dEa': 0.1443365685965179, 'dn_dEa': -0.21795364656850552, 'name': 'C2H4N2O2-9 <=> C2H4N2O2-10'}, {'dA': 0.5867925040750712, 'dE0': 0.0038458653664008836, 'dn': -0.012280687395451545, 'dA_dEa': -13.839535587955002, 'dE0_dEa': -0.042041045750551044, 'dn_dEa': 0.35720712471902033, 'name': 'CH4N2O <=> CH4N2O-2'}, {'dA': -0.19425741068170774, 'dE0': -0.0024671331218381275, 'dn': 0.007881818371799972, 'dA_dEa': -8.60380052599036, 'dE0_dEa': 0.021346352323842487, 'dn_dEa': 0.22203606351443153, 'name': 'C2H4N2O2-13 <=> C2H4N2O2-14'}]
""",
)

entry(
    index = 84,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(8.72733e-17,'s^-1'), n=8.43216, w0=(798000,'J/mol'), E0=(93995.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.7293818489377198, 'dn_dEa': 0.0, 'name': 'C2H4N2O2 <=> C2H4N2O2-2'}]
""",
)

entry(
    index = 85,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_4R->C",
    kinetics = ArrheniusBM(A=(1.93892e+11,'s^-1'), n=0.308436, w0=(707000,'J/mol'), E0=(125262,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_4R->C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': -1.0254105239867493, 'dE0': -0.010485642479777926, 'dn': 0.02796558198338567, 'dA_dEa': 11.692236366561426, 'dE0_dEa': 0.23817848166964442, 'dn_dEa': -0.26693424222362383, 'name': 'C2H4N2O2-3 <=> C2H4N2O2-4'}, {'dA': -0.9685891587488628, 'dE0': -0.01000018773750578, 'dn': 0.02666847602378035, 'dA_dEa': 11.196368638166543, 'dE0_dEa': 0.23880378112526068, 'dn_dEa': -0.25561928412521046, 'name': 'C3H6N2O <=> C3H6N2O-2'}, {'dA': -0.23677140132252583, 'dE0': -0.0037364319374501498, 'dn': 0.009966396092608172, 'dA_dEa': 3.951058763798523, 'dE0_dEa': 0.16515080828649603, 'dn_dEa': -0.09025518398485484, 'name': 'C2H5N3O <=> C2H5N3O-2'}, {'dA': 2.379956102338361, 'dE0': 0.018667799666760562, 'dn': -0.04975221594262035, 'dA_dEa': -21.06834840788584, 'dE0_dEa': -0.047227803489975635, 'dn_dEa': 0.4807498587942944, 'name': 'CH4N2O <=> CH4N2O-2'}, {'dA': 0.8237131356026791, 'dE0': 0.005341165719290586, 'dn': -0.01423653276686728, 'dA_dEa': -6.8689904568149736, 'dE0_dEa': 0.11446182549924767, 'dn_dEa': 0.15665929305648005, 'name': 'C2H4N2O2-13 <=> C2H4N2O2-14'}]
""",
)

entry(
    index = 86,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C",
    kinetics = ArrheniusBM(A=(7.72033e-12,'s^-1'), n=7.13865, w0=(798000,'J/mol'), E0=(101332,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0009406278385854534, var=0.10603351746797161, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C
        Total Standard Deviation in ln(k): 0.6551610235432553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C
Total Standard Deviation in ln(k): 0.6551610235432553""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C
Total Standard Deviation in ln(k): 0.6551610235432553
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.7343954752954083, 'dn_dEa': 0.0, 'name': 'C2H4N2O2-13 <=> C2H4N2O2-14'}]
""",
)

entry(
    index = 87,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_Ext-5CO-R_Ext-5CO-R",
    kinetics = ArrheniusBM(A=(2.24517e-15,'s^-1'), n=8.2595, w0=(798000,'J/mol'), E0=(97485.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_Ext-5CO-R_Ext-5CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_Ext-5CO-R_Ext-5CO-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_Ext-5CO-R_Ext-5CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_Ext-5CO-R_Ext-5CO-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': -1.2301935244850815, 'dE0': -0.013361613850405848, 'dn': 0.02660600003126634, 'dA_dEa': 14.710765140636028, 'dE0_dEa': 0.314856472457785, 'dn_dEa': -0.2644886038732889, 'name': 'C2H4N2O2-3 <=> C2H4N2O2-4'}, {'dA': -1.1564368732061179, 'dE0': -0.01269537274802092, 'dn': 0.0252802289834162, 'dA_dEa': 13.973300339779488, 'dE0_dEa': 0.31461530681075134, 'dn_dEa': -0.2512331404537548, 'name': 'C3H6N2O <=> C3H6N2O-2'}, {'dA': -0.13697479888465214, 'dE0': -0.0034920086628069916, 'dn': 0.006954173243886364, 'dA_dEa': 4.000898567202867, 'dE0_dEa': 0.2092491143847037, 'dn_dEa': -0.07196338291878411, 'name': 'C2H5N3O <=> C2H5N3O-2'}, {'dA': 3.5257990133498724, 'dE0': 0.02957352333932179, 'dn': -0.05888876079616534, 'dA_dEa': -30.94983933868519, 'dE0_dEa': -0.10391944249067118, 'dn_dEa': 0.5563185366877481, 'name': 'CH4N2O <=> CH4N2O-2'}]
""",
)

entry(
    index = 88,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_5CO->O",
    kinetics = ArrheniusBM(A=(3.21561e-15,'s^-1'), n=8.08717, w0=(798000,'J/mol'), E0=(97688.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_5CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_5CO->O
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_5CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_5CO->O
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': -0.1965741478287203, 'dE0': -0.004787399035899944, 'dn': 0.009729180447496323, 'dA_dEa': 4.976478977227409, 'dE0_dEa': 0.2879181074206394, 'dn_dEa': -0.09142231419668158, 'name': 'C2H4N2O2-3 <=> C2H4N2O2-4'}, {'dA': -0.09700689070869475, 'dE0': -0.0038854070046715266, 'dn': 0.007901068745368283, 'dA_dEa': 3.4892084716173177, 'dE0_dEa': 0.2830412123701959, 'dn_dEa': -0.0641074434274055, 'name': 'C3H6N2O <=> C3H6N2O-2'}, {'dA': 1.256367054480872, 'dE0': 0.00834124758862152, 'dn': -0.01695589064866848, 'dA_dEa': -8.516666761072372, 'dE0_dEa': 0.15409140400103163, 'dn_dEa': 0.15639853151538233, 'name': 'C2H5N3O <=> C2H5N3O-2'}]
""",
)

entry(
    index = 89,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_N-5CO->O",
    kinetics = ArrheniusBM(A=(7.48602e-15,'s^-1'), n=8.00071, w0=(798000,'J/mol'), E0=(97935.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_N-5CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_N-5CO->O
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_N-5CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_N-5CO->O
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.7031533281968485, 'dn_dEa': 0.0, 'name': 'C2H5N3O <=> C2H5N3O-2'}]
""",
)

entry(
    index = 90,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O_5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(9.16767e+14,'s^-1'), n=-0.000952816, w0=(707000,'J/mol'), E0=(259509,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O_5BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O_5BrCClFINPSSi->C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.4220055926609699, 'dE0': -0.000692038198256115, 'dn': 0.0014087792583852366, 'dA_dEa': 1.2179163575966276, 'dE0_dEa': 0.3710810900763254, 'dn_dEa': -0.02203308403404953, 'name': 'C2H4N2O2-3 <=> C2H4N2O2-4'}, {'dA': 0.5720608465900686, 'dE0': 0.0006473050242019112, 'dn': -0.0013094265444449633, 'dA_dEa': -1.206418921953078, 'dE0_dEa': 0.3621238774204019, 'dn_dEa': 0.02188109130038771, 'name': 'C3H6N2O <=> C3H6N2O-2'}]
""",
)

entry(
    index = 91,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O_N-5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(3.03918e+16,'s^-1'), n=-0.601612, w0=(707000,'J/mol'), E0=(201180,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O_N-5BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O_N-5BrCClFINPSSi->C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.7333188331401207, 'dn_dEa': 0.0, 'name': 'C3H6N2O <=> C3H6N2O-2'}]
""",
)

entry(
    index = 92,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(9.05172e+10,'s^-1'), n=0.89767, w0=(615000,'J/mol'), E0=(329307,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0565073687571566e-14, var=1.80566058771988, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_5BrCClFINPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_5BrCClFINPSSi->C
        Total Standard Deviation in ln(k): 2.6938601682420895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 2.6938601682420895""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 2.6938601682420895
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.7282105395068024, 'dn_dEa': 0.0, 'name': 'C2H4N2O2-3 <=> C2H4N2O2-4'}]
""",
)

entry(
    index = 93,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_N-5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(8.78669e+12,'s^-1'), n=0.204119, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_N-5BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_N-5BrCClFINPSSi->C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 1.5741985778065584, 'dE0': 0.01154394701655871, 'dn': -0.019949302268833475, 'dA_dEa': -11.497837643902487, 'dE0_dEa': 0.13997830769848452, 'dn_dEa': 0.1846821799435517, 'name': 'C2H4N2O2-7 <=> C2H4N2O2-8'}, {'dA': 0.05481333183610708, 'dE0': -0.002587536866361141, 'dn': 0.004474815409204325, 'dA_dEa': 3.4317406668481936, 'dE0_dEa': 0.2904280813277785, 'dn_dEa': -0.055311543360800776, 'name': 'C3H3NO <=> C3H3NO-2'}, {'dA': -0.6273945554654128, 'dE0': -0.008934305138178663, 'dn': 0.015440956747053829, 'dA_dEa': 10.189223011026328, 'dE0_dEa': 0.35756902252318973, 'dn_dEa': -0.16393777011516222, 'name': 'C2H4N2O2-9 <=> C2H4N2O2-10'}]
""",
)

entry(
    index = 94,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.69578e-13,'s^-1'), n=7.6981, w0=(798000,'J/mol'), E0=(101157,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.006581694381035067, var=2.055466972897255, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R
        Total Standard Deviation in ln(k): 2.890705523459266"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.890705523459266""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.890705523459266
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.7823801830247007, 'dn_dEa': 0.0, 'name': 'C2H4N2O2-9 <=> C2H4N2O2-10'}]
""",
)

entry(
    index = 95,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N",
    kinetics = ArrheniusBM(A=(1.65175e-13,'s^-1'), n=7.74458, w0=(798000,'J/mol'), E0=(97939.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.002146257399877121, var=0.23553441622036883, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N
        Total Standard Deviation in ln(k): 0.9783283909230072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N
Total Standard Deviation in ln(k): 0.9783283909230072""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N
Total Standard Deviation in ln(k): 0.9783283909230072
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.7395669245138405, 'dn_dEa': 0.0, 'name': 'C2H4N2O2-7 <=> C2H4N2O2-8'}]
""",
)

entry(
    index = 96,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-7R!H->N",
    kinetics = ArrheniusBM(A=(1.797e-10,'s^-1'), n=6.92374, w0=(798000,'J/mol'), E0=(99729.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-7R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-7R!H->N
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330872656, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.7679914205682004, 'dn_dEa': 0.0, 'name': 'C3H3NO <=> C3H3NO-2'}]
""",
)

entry(
    index = 97,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R",
    kinetics = ArrheniusBM(A=(2.19963e-11,'s^-1'), n=6.98648, w0=(798000,'J/mol'), E0=(100797,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006099207969903697, var=0.16754745053310063, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R
        Total Standard Deviation in ln(k): 0.8359140406399651"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R
Total Standard Deviation in ln(k): 0.8359140406399651""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R
Total Standard Deviation in ln(k): 0.8359140406399651
sensitivities = [{'dA': -1.014922021244869, 'dE0': -0.013169733176401726, 'dn': 0.022479156360588996, 'dA_dEa': 16.918593534418576, 'dE0_dEa': 0.4623026146958053, 'dn_dEa': -0.28229551909839273, 'name': 'C2H4N2O2-5 <=> C2H4N2O2-6'}, {'dA': 3.820738038222226, 'dE0': 0.0340842010647071, 'dn': -0.058151913191115755, 'dA_dEa': -32.77771721222328, 'dE0_dEa': -0.05503719039972661, 'dn_dEa': 0.5463735757552579, 'name': 'C2H3NO2 <=> C2H3NO2-2'}, {'dA': -1.7470772145921891, 'dE0': -0.02032271249392431, 'dn': 0.03468763788034994, 'dA_dEa': 22.988705767818065, 'dE0_dEa': 0.49329331437340496, 'dn_dEa': -0.3834911845500477, 'name': 'C2H4N2O <=> C2H4N2O-2'}]
""",
)

entry(
    index = 98,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_5BrCClFINPSSi->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.54394e+12,'s^-1'), n=0.452411, w0=(615000,'J/mol'), E0=(338565,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_5BrCClFINPSSi->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_5BrCClFINPSSi->C_Ext-1R!H-R
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_5BrCClFINPSSi->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_5BrCClFINPSSi->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.8120762167453791, 'dn_dEa': 0.0, 'name': 'C2H4N2O2-5 <=> C2H4N2O2-6'}]
""",
)

entry(
    index = 99,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.835e-16,'s^-1'), n=8.51386, w0=(798000,'J/mol'), E0=(95477.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_5R!H->C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.8130647994034734, 'dn_dEa': 0.0, 'name': 'C2H4N2O <=> C2H4N2O-2'}]
""",
)

entry(
    index = 100,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.77636e-11,'s^-1'), n=7.04941, w0=(798000,'J/mol'), E0=(104855,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_N-5R!H->C
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.7320349450823946, 'dn_dEa': 0.0, 'name': 'C2H3NO2 <=> C2H3NO2-2'}]
""",
)

entry(
    index = 101,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N_5R!H->O",
    kinetics = ArrheniusBM(A=(2.33438e-16,'s^-1'), n=8.59067, w0=(798000,'J/mol'), E0=(93265.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N_5R!H->O
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.6691705271251918, 'dE0': 0.002194242009432829, 'dn': -0.09546316379772571, 'dA_dEa': -6.314336419351448, 'dE0_dEa': 0.2767358020231782, 'dn_dEa': 1.7894474481998126, 'name': 'C2H4N2O2-11 <=> C2H4N2O2-12'}, {'dA': 0.14573815434461507, 'dE0': -0.0012089572121722488, 'dn': 0.053329690463788354, 'dA_dEa': 3.358392205339215, 'dE0_dEa': 0.2755699337374497, 'dn_dEa': -0.9588508278157174, 'name': 'C2H3NO2-3 <=> C2H3NO2-4'}, {'dA': 0.14623924295166735, 'dE0': -0.001205894154888275, 'dn': 0.0531862411501068, 'dA_dEa': 3.2152372477089117, 'dE0_dEa': 0.2650372871736591, 'dn_dEa': -0.9179575140381342, 'name': 'C2H3NO2-3 <=> C2H3NO2-4'}]
""",
)

entry(
    index = 102,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1.28848e-11,'s^-1'), n=7.11818, w0=(798000,'J/mol'), E0=(96726.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N_N-5R!H->O
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.8131668459690816, 'dn_dEa': 0.0, 'name': 'C2H4N2O2-11 <=> C2H4N2O2-12'}]
""",
)

entry(
    index = 103,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_7R!H->N",
    kinetics = ArrheniusBM(A=(9.61654e-11,'s^-1'), n=6.78703, w0=(798000,'J/mol'), E0=(99834.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_7R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_7R!H->N
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.8271044239052772, 'dn_dEa': 0.0, 'name': 'C2H4N2O-3 <=> C2H4N2O-4'}]
""",
)

entry(
    index = 104,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N",
    kinetics = ArrheniusBM(A=(1.1358e-11,'s^-1'), n=7.08342, w0=(798000,'J/mol'), E0=(101820,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.774397504036697e-05, var=0.31280538790524537, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N
        Total Standard Deviation in ln(k): 1.1213232657408565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N
Total Standard Deviation in ln(k): 1.1213232657408565""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N
Total Standard Deviation in ln(k): 1.1213232657408565
sensitivities = [{'dA': 0.36963738996646694, 'dE0': 0.0003849821412775104, 'dn': -0.001340881513320648, 'dA_dEa': -0.38844714583723244, 'dE0_dEa': 0.3625942487434335, 'dn_dEa': 0.014284842474758988, 'name': 'SC=O <=> OC=S'}, {'dA': 0.3419160947119403, 'dE0': 7.677178937555413e-05, 'dn': -0.00032808961790811703, 'dA_dEa': 0.2525734106182676, 'dE0_dEa': 0.3595149139086027, 'dn_dEa': -0.009280645294607119, 'name': 'CC(=O)S <=> CC(=S)O'}, {'dA': 0.33518011306980316, 'dE0': 5.730956582023945e-06, 'dn': -8.040754498242154e-05, 'dA_dEa': 0.24802769644147138, 'dE0_dEa': 0.3645365820999571, 'dn_dEa': -0.009112707271440614, 'name': 'CCC(=O)S <=> CCC(=S)O'}]
""",
)

entry(
    index = 105,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing",
    kinetics = ArrheniusBM(A=(4.38421e-12,'s^-1'), n=7.22006, w0=(798000,'J/mol'), E0=(103463,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.509581867285503, 'dE0': 0.00010122814468046166, 'dn': -0.0003671475571198058, 'dA_dEa': 0.05678645022356225, 'dE0_dEa': 0.5402278925715959, 'dn_dEa': -0.0020939850072065882, 'name': 'CC(=O)S <=> CC(=S)O'}, {'dA': 0.499331924580348, 'dE0': -7.762374380259881e-06, 'dn': 1.4191712570140346e-05, 'dA_dEa': 0.048958806585624855, 'dE0_dEa': 0.5478083236357922, 'dn_dEa': -0.0018024741586004126, 'name': 'CCC(=O)S <=> CCC(=S)O'}]
""",
)

entry(
    index = 106,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing",
    kinetics = ArrheniusBM(A=(7.07407e-11,'s^-1'), n=6.82872, w0=(798000,'J/mol'), E0=(100753,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing
        Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.0345588349785892, 'dn_dEa': 0.0, 'name': 'CCC(=O)S <=> CCC(=S)O'}]
""",
)

