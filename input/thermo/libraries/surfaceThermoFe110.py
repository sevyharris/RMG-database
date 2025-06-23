#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "X",
    molecule = 
"""
1 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.00710141,-4.25621e-05,8.98538e-08,-7.80198e-11,2.32467e-14,-0.876103,-0.0311212], Tmin=(100,'K'), Tmax=(1554.8,'K')),
            NASAPolynomial(coeffs=[0.160299,-0.000252235,1.14181e-07,-1.21471e-11,3.85783e-16,-70.8098,-0.909524], Tmin=(1554.8,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
    label = "HX",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.377311,0.00523441,3.53289e-06,-1.07921e-08,5.09304e-12,-8958.65,1.01668], Tmin=(100,'K'), Tmax=(949.78,'K')),
            NASAPolynomial(coeffs=[2.87901,-0.000691033,5.90484e-07,-9.28848e-11,4.20289e-15,-9928.51,-16.3748], Tmin=(949.78,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
    label = "CX",
    molecule = 
"""
1 C u0 p0 c0 {2,Q}
2 X u0 p0 c0 {1,Q}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.631598,0.0107879,-1.25133e-05,6.3409e-09,-1.16277e-12,-2167.09,1.60885], Tmin=(100,'K'), Tmax=(1556.41,'K')),
            NASAPolynomial(coeffs=[3.13608,-0.000888722,6.6154e-07,-1.25347e-10,8.07607e-15,-3098.43,-17.459], Tmin=(1556.41,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 3,
    label = "NX",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 X u0 p0 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.632147,0.0144792,-2.35036e-05,1.7426e-08,-4.89051e-12,3328.63,1.33806], Tmin=(100,'K'), Tmax=(887.32,'K')),
            NASAPolynomial(coeffs=[2.39559,0.000830679,-4.31476e-07,9.18212e-11,-6.76576e-15,2791.3,-12.9071], Tmin=(887.32,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 4,
    label = "OX",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 X u0 p0 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.712491,0.0171469,-3.227e-05,2.75916e-08,-8.84466e-12,-41010.8,1.59429], Tmin=(100,'K'), Tmax=(873.71,'K')),
            NASAPolynomial(coeffs=[2.13663,0.00147253,-8.43505e-07,1.66114e-10,-1.11725e-14,-41408.3,-11.1918], Tmin=(873.71,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 5,
    label = "NH3X",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.34551,0.0338516,-5.98228e-05,5.41831e-08,-1.8411e-11,-13346.9,5.02702], Tmin=(100,'K'), Tmax=(894.18,'K')),
            NASAPolynomial(coeffs=[1.5623,0.0109743,-4.8892e-06,8.82814e-10,-5.78148e-14,-13472.4,-6.46994], Tmin=(894.18,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
    label = "OCX",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 X u0 p0 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.26997,0.0329366,-6.79007e-05,6.38176e-08,-2.20528e-11,-36236.9,3.62111], Tmin=(100,'K'), Tmax=(883.23,'K')),
            NASAPolynomial(coeffs=[2.03676,0.00654307,-3.68515e-06,7.11035e-10,-4.75858e-14,-36375.6,-9.40017], Tmin=(883.23,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 7,
    label = "HCXNX",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {5,D}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 H u0 p0 c0 {2,S}
4 X u0 p0 c0 {2,D}
5 X u0 p0 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.41578,0.0341897,-5.98766e-05,5.1847e-08,-1.71997e-11,-14098.5,4.51457], Tmin=(100,'K'), Tmax=(842.93,'K')),
            NASAPolynomial(coeffs=[3.23135,0.00737868,-3.69822e-06,7.18798e-10,-4.95759e-14,-14712.9,-16.1083], Tmin=(842.93,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 8,
    label = "N2X",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
3 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.23367,0.0362427,-8.82867e-05,9.03689e-08,-3.26017e-11,-7937.03,11.5849], Tmin=(100,'K'), Tmax=(900.69,'K')),
            NASAPolynomial(coeffs=[-0.1516,0.00886303,-5.09416e-06,9.65486e-10,-6.28455e-14,-7216.29,11.5609], Tmin=(900.69,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 9,
    label = "ONX",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.35348,0.0355015,-7.4893e-05,7.11154e-08,-2.47096e-11,-22834.5,4.45381], Tmin=(100,'K'), Tmax=(884.84,'K')),
            NASAPolynomial(coeffs=[2.03099,0.00694443,-4.00835e-06,7.75732e-10,-5.18506e-14,-22914.5,-8.5276], Tmin=(884.84,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 10,
    label = "HCX",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,T}
2 H u0 p0 c0 {1,S}
3 X u0 p0 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.919835,0.0168946,-1.92149e-05,1.01244e-08,-1.976e-12,-3559.65,2.34071], Tmin=(100,'K'), Tmax=(1412.83,'K')),
            NASAPolynomial(coeffs=[4.1668,0.000505265,2.96501e-07,-7.83441e-11,5.62335e-15,-4798.54,-23.255], Tmin=(1412.83,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 11,
    label = "H2CX",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 X u0 p0 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.01997,0.0205597,-2.2179e-05,1.19754e-08,-2.49767e-12,-3486.54,3.22263], Tmin=(100,'K'), Tmax=(1183.51,'K')),
            NASAPolynomial(coeffs=[3.851,0.0040968,-1.31361e-06,2.21976e-10,-1.49072e-14,-4639.5,-21.0976], Tmin=(1183.51,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 12,
    label = "H3CX",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.15127,0.0270831,-3.76716e-05,3.01429e-08,-9.74501e-12,-7276.6,4.52419], Tmin=(100,'K'), Tmax=(809.83,'K')),
            NASAPolynomial(coeffs=[1.89867,0.0106406,-4.66402e-06,8.69432e-10,-5.95245e-14,-7725.41,-9.26769], Tmin=(809.83,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 13,
    label = "HNX",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 X u0 p0 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.923132,0.017312,-2.04683e-05,1.11797e-08,-2.26059e-12,-17757,2.32484], Tmin=(100,'K'), Tmax=(1357.84,'K')),
            NASAPolynomial(coeffs=[4.18171,0.000356553,3.80398e-07,-9.64164e-11,6.98522e-15,-18966.6,-23.2138], Tmin=(1357.84,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 14,
    label = "H2NX",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.05406,0.0227286,-2.88319e-05,1.83239e-08,-4.4894e-12,-13259.8,2.93579], Tmin=(100,'K'), Tmax=(1010.66,'K')),
            NASAPolynomial(coeffs=[3.6145,0.00425225,-1.41117e-06,2.37181e-10,-1.5647e-14,-14203.5,-19.6371], Tmin=(1010.66,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 15,
    label = "HOX",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.32358,0.0348667,-7.48151e-05,7.00816e-08,-2.37155e-11,-40373.9,8.47224], Tmin=(100,'K'), Tmax=(913.91,'K')),
            NASAPolynomial(coeffs=[2.23377,0.0051092,-2.68809e-06,4.80934e-10,-2.95675e-14,-40431.6,-5.12814], Tmin=(913.91,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 16,
    label = "CXNX",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {4,S}
2 C u0 p0 c0 {1,D} {3,D}
3 X u0 p0 c0 {2,D}
4 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82402,-0.0108695,2.97555e-05,-3.43936e-08,1.38585e-11,-19229.7,-32.6856], Tmin=(100,'K'), Tmax=(848.76,'K')),
            NASAPolynomial(coeffs=[4.76973,-0.00577267,3.86379e-06,-7.94848e-10,5.58692e-14,-19734.4,-39.1202], Tmin=(848.76,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 17,
    label = "HOCX",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 C u0 p0 c0 {1,S} {4,T}
3 H u0 p0 c0 {1,S}
4 X u0 p0 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.50128,0.0358676,-6.26479e-05,5.28904e-08,-1.70176e-11,-383.761,4.71815], Tmin=(100,'K'), Tmax=(864.35,'K')),
            NASAPolynomial(coeffs=[3.84,0.00636561,-3.14818e-06,5.95702e-10,-4.01426e-14,-1128.41,-19.2381], Tmin=(864.35,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 18,
    label = "HCOX",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 H u0 p0 c0 {2,S}
4 X u0 p0 c0 {2,D}
5 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.45831,0.0356844,-6.43502e-05,5.69975e-08,-1.92301e-11,-30963.4,6.91245], Tmin=(100,'K'), Tmax=(847.84,'K')),
            NASAPolynomial(coeffs=[3.06427,0.00799572,-4.12569e-06,8.06096e-10,-5.56076e-14,-31502,-12.8135], Tmin=(847.84,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 19,
    label = "HONX",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {4,D}
3 H u0 p0 c0 {1,S}
4 X u0 p0 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.61256,0.0393154,-7.24185e-05,6.29448e-08,-2.05519e-11,-19962.7,4.908], Tmin=(100,'K'), Tmax=(884.3,'K')),
            NASAPolynomial(coeffs=[3.85944,0.00656809,-3.30805e-06,6.18208e-10,-4.08456e-14,-20617.9,-19.0508], Tmin=(884.3,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 20,
    label = "HNXOX",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 N u0 p1 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 X u0 p0 c0 {2,S}
5 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.36453,-0.0484608,0.000151007,-1.57368e-07,5.4814e-11,-36509.9,-47.3829], Tmin=(100,'K'), Tmax=(959.59,'K')),
            NASAPolynomial(coeffs=[5.73831,-0.00117619,7.43604e-07,6.81996e-11,-2.17954e-14,-38830.4,-60.888], Tmin=(959.59,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

