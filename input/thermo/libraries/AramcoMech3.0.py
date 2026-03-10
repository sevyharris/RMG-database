#!/usr/bin/env python
# encoding: utf-8

name = "AramcoMech3.0"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "AR",
    molecule = 
"""
1 Ar u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.37967], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.37967], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53101,-0.000123661,-5.02999e-07,2.43531e-09,-1.40881e-12,-1046.98,2.96747], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.95258,0.0013969,-4.92632e-07,7.8601e-11,-4.60755e-15,-923.949,5.87189], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
    label = "HE",
    molecule = 
"""
1 He u0 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,0.928724], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,0.928724], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 3,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.34433,0.00798052,-1.94782e-05,2.01572e-08,-7.37612e-12,-917.935,0.68301], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.93287,0.000826608,-1.46402e-07,1.541e-11,-6.88805e-16,-813.066,-1.02433], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 4,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,25473.7,-0.446683], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,25473.7,-0.446683], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 5,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78246,-0.00299673,9.8473e-06,-9.6813e-09,3.24373e-12,-1063.94,3.65768], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.66096,0.000656366,-1.4115e-07,2.05798e-11,-1.29913e-15,-1215.98,3.41536], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
    label = "O",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16827,-0.00327932,6.64306e-06,-6.12807e-09,2.11266e-12,29122.3,2.05193], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.54364,-2.73162e-05,-4.1903e-09,4.95482e-12,-4.79554e-16,29226,4.92229], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 7,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.19864,-0.0020364,6.52034e-06,-5.48793e-09,1.77197e-12,-30293.7,-0.849009], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.67704,0.00297318,-7.73769e-07,9.44335e-11,-4.269e-15,-29885.9,6.88255], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 8,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99198,-0.00240107,4.61664e-06,-3.87916e-09,1.3632e-12,3368.9,-0.103998], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.83853,0.00110741,-2.94e-07,4.20699e-11,-2.4229e-15,3697.81,5.84495], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 9,
    label = "H2O2",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.31515,-0.000847391,1.76404e-05,-2.26763e-08,9.0895e-12,-17706.7,3.27373], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.57977,0.00405326,-1.29845e-06,1.98211e-10,-1.13969e-14,-18007.2,0.664971], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 10,
    label = "HO2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.3018,-0.00474912,2.11583e-05,-2.42764e-08,9.29225e-12,264.018,3.71666], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.17229,0.00188118,-3.46277e-07,1.94658e-11,1.76257e-16,31.0207,2.95768], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 11,
    label = "CO",
    molecule = 
"""
1 O u0 p1 c+1 {2,T}
2 C u0 p1 c-1 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57953,-0.000610354,1.01681e-06,9.07006e-10,-9.04424e-13,-14344.1,3.50841], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.04849,0.00135173,-4.85794e-07,7.88536e-11,-4.69807e-15,-14266.1,6.0171], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 12,
    label = "CO2",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35681,0.00898413,-7.12206e-06,2.4573e-09,-1.42885e-13,-48372,9.9009], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.63651,0.00274146,-9.95898e-07,1.60387e-10,-9.16199e-15,-49024.9,-1.9349], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 13,
    label = "HOCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 C u1 p0 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.92208,0.00762454,3.29884e-06,-1.07135e-08,5.11587e-12,-23028.2,11.2926], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.39206,0.00411221,-1.48195e-06,2.39875e-10,-1.43903e-14,-23860.7,-2.23529], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 14,
    label = "CH4",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.14911,-0.0136622,4.91454e-05,-4.84247e-08,1.66603e-11,-10246.6,-4.63849], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.65326,0.0100263,-3.31661e-06,5.36483e-10,-3.14697e-14,-10009.6,9.90506], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 15,
    label = "CH3",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65718,0.0021266,5.45839e-06,-6.6181e-09,2.46571e-12,16422.7,1.67354], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.97812,0.00579785,-1.97558e-06,3.07298e-10,-1.79174e-14,16509.5,4.72248], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 16,
    label = "CH2",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71758,0.00127391,2.17347e-06,-3.48858e-09,1.65209e-12,45872.4,1.75298], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.14632,0.00303671,-9.96474e-07,1.50484e-10,-8.57336e-15,46041.3,4.72342], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 17,
    label = "C",
    molecule = 
"""
multiplicity 3
1 C u2 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.55424,-0.000321538,7.33792e-07,-7.32235e-10,2.66521e-13,85442.7,4.53131], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.60558,-0.000195934,1.06737e-07,-1.64239e-11,8.18706e-16,85411.7,4.19239], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 18,
    label = "CH",
    molecule = 
"""
multiplicity 2
1 C u1 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48976,0.000324322,-1.68998e-06,3.16284e-09,-1.40618e-12,70612.6,2.08428], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.52094,0.00176536,-4.61477e-07,5.92897e-11,-3.34745e-15,70946.8,7.40518], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 19,
    label = "CH3O2H",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {7,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.90541,0.0174995,5.28244e-06,-2.52827e-08,1.34368e-11,-16889.5,11.3742], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.76538,0.008615,-2.98007e-06,4.68638e-10,-2.75339e-14,-18298,-14.3993], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 20,
    label = "CH3O2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.97339,0.0153542,-6.37315e-06,3.19931e-10,2.82194e-13,254.279,16.9194], Tmin=(300,'K'), Tmax=(1374,'K')),
            NASAPolynomial(coeffs=[6.4797,0.00744401,-2.52349e-06,3.89577e-10,-2.25182e-14,-1562.85,-8.19477], Tmin=(1374,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 21,
    label = "CH2O2H",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.88976,0.0209466,-1.75191e-05,7.2782e-09,-1.18912e-12,6123.91,12.3802], Tmin=(300,'K'), Tmax=(1410,'K')),
            NASAPolynomial(coeffs=[9.24698,0.00460846,-1.53501e-06,2.34435e-10,-1.34573e-14,4115.3,-21.1503], Tmin=(1410,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 22,
    label = "CH3OH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.65851,-0.0162983,6.91938e-05,-7.58373e-08,2.80428e-11,-25612,-0.897331], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.52727,0.0103179,-3.62893e-06,5.77448e-10,-3.42183e-14,-26002.9,5.16759], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 23,
    label = "CH3O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71181,-0.00280463,3.76551e-05,-4.73072e-08,1.86588e-11,1295.7,6.57241], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.75779,0.00744142,-2.69705e-06,4.38091e-10,-2.63537e-14,378.112,-1.9668], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 24,
    label = "CH2OH",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.47834,-0.0013507,2.78485e-05,-3.64869e-08,1.47907e-11,-3500.73,3.30913], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.09314,0.00594761,-2.06497e-06,3.23008e-10,-1.88126e-14,-4034.1,-1.84691], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 25,
    label = "CH2O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.79372,-0.00990833,3.7322e-05,-3.79285e-08,1.31773e-11,-14379.2,0.602798], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.16953,0.00619321,-2.25056e-06,3.65976e-10,-2.20149e-14,-14548.7,6.04208], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 26,
    label = "HCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.23755,-0.00332075,1.4003e-05,-1.3424e-08,4.37416e-12,3872.41,3.30835], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.92002,0.00252279,-6.71004e-07,1.05616e-10,-7.43798e-15,3653.43,3.58077], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 27,
    label = "HCOH",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {4,S}
2 C u2 p0 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.82157,0.0357332,-3.80862e-05,1.86206e-08,-3.45958e-12,11295.7,34.8488], Tmin=(300,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[9.18749,0.00152011,-6.27604e-07,1.09728e-10,-6.89655e-15,7813.65,-27.3434], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 28,
    label = "HO2CHO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {3,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.42465,0.0219706,-1.68706e-05,6.25612e-09,-9.11646e-13,-35482.8,17.5028], Tmin=(300,'K'), Tmax=(1378,'K')),
            NASAPolynomial(coeffs=[9.87504,0.00464664,-1.67231e-06,2.68624e-10,-1.59595e-14,-38050.2,-22.4939], Tmin=(1378,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 29,
    label = "HOCH2O2H",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,S} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.53519,0.0373267,-3.153e-05,1.30353e-08,-2.11473e-12,-38660.9,27.1776], Tmin=(300,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[12.4532,0.00718221,-2.4703e-06,3.85612e-10,-2.24774e-14,-42486.3,-35.8745], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 30,
    label = "HOCH2O2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.82069,0.0247857,-1.66186e-05,4.79633e-09,-4.28088e-13,-22207.7,17.06], Tmin=(300,'K'), Tmax=(1377,'K')),
            NASAPolynomial(coeffs=[11.6406,0.00572826,-2.05362e-06,3.29071e-10,-1.95188e-14,-25350.6,-30.7332], Tmin=(1377,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 31,
    label = "OCH2O2H",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {7,S}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.446349,0.036305,-3.26131e-05,1.37051e-08,-2.20873e-12,-14197.3,27.296], Tmin=(300,'K'), Tmax=(1418,'K')),
            NASAPolynomial(coeffs=[12.9622,0.00421949,-1.54275e-06,2.50413e-10,-1.49856e-14,-18132.6,-38.7016], Tmin=(1418,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 32,
    label = "HOCH2O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u1 p2 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.11183,0.00753851,3.77337e-06,-5.38746e-09,1.45616e-12,-22802.3,7.46807], Tmin=(300,'K'), Tmax=(1452,'K')),
            NASAPolynomial(coeffs=[6.39522,0.00743673,-2.50422e-06,3.8488e-10,-2.21779e-14,-24110.9,-6.63866], Tmin=(1452,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 33,
    label = "O2CHO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,D}
3 O u1 p2 c0 {1,S}
4 C u0 p0 c0 {1,S} {2,D} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96059,0.0106002,-5.25713e-06,1.01717e-09,-2.87488e-14,-17359.9,11.7807], Tmin=(300,'K'), Tmax=(1368,'K')),
            NASAPolynomial(coeffs=[7.24075,0.00463313,-1.63694e-06,2.59707e-10,-1.52965e-14,-18702.8,-6.49547], Tmin=(1368,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 34,
    label = "HOCHO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89836,-0.00355878,3.55205e-05,-4.385e-08,1.71078e-11,-46770.6,7.34954], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.61383,0.00644964,-2.29083e-06,3.6716e-10,-2.18737e-14,-47514.8,0.847884], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 35,
    label = "OCHO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 O u1 p2 c0 {1,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.68826,-0.00414872,2.55066e-05,-2.84474e-08,1.04423e-11,-16986.7,4.28426], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.14394,0.00559739,-1.99794e-06,3.16179e-10,-1.85614e-14,-17246,5.07779], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 36,
    label = "C2H6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.29143,-0.00550155,5.99438e-05,-7.08466e-08,2.68686e-11,-11522.2,2.66679], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.04666,0.0153539,-5.47039e-06,8.77827e-10,-5.23168e-14,-12447.3,-0.968698], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 37,
    label = "C2H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.3273,0.0176657,-6.14927e-06,-3.01143e-10,4.38618e-13,13428.4,17.1789], Tmin=(300,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[5.88784,0.0103077,-3.46844e-06,5.32499e-10,-3.06513e-14,11506.5,-8.49652], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 38,
    label = "C2H5O2H",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  O u0 p2 c0 {1,S} {4,S}
4  O u0 p2 c0 {3,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.83755,0.0338054,-2.37548e-05,9.31975e-09,-1.58003e-12,-21581.4,18.0978], Tmin=(300,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[10.4824,0.013478,-4.62179e-06,7.18619e-10,-4.17307e-14,-24657.8,-28.4294], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 39,
    label = "C2H5O2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 O u0 p2 c0 {1,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 O u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90352,0.0222599,-1.0161e-05,1.7171e-09,1.88167e-14,-5096.54,8.98723], Tmin=(300,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[9.50283,0.012043,-4.09492e-06,6.33049e-10,-3.66134e-14,-7370.69,-22.1717], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 40,
    label = "C2H4",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.481118,0.0183778,-9.99634e-06,2.73211e-09,-3.01837e-13,5443.87,18.5867], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[5.07061,0.00911141,-3.10507e-06,4.80734e-10,-2.78321e-14,3663.91,-6.64501], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 41,
    label = "C2H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u1 p0 c0 {1,D} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.25545,0.0157482,-1.12218e-05,4.50916e-09,-7.74862e-13,34743.6,16.9664], Tmin=(300,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[4.99675,0.00655838,-2.20922e-06,3.393e-10,-1.95317e-14,33460.4,-3.01451], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 42,
    label = "CHOCHO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {4,D}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 C u0 p0 c0 {2,D} {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.88105,0.0236386,-1.83443e-05,6.84843e-09,-9.92734e-13,-26928,15.9155], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[9.75439,0.00497646,-1.7441e-06,2.75587e-10,-1.6197e-14,-29583.3,-26.1878], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 43,
    label = "C2H3OOH",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {3,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.35644,0.0337002,-2.75989e-05,1.14223e-08,-1.89489e-12,-5499.97,19.8354], Tmin=(300,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[11.575,0.00809909,-2.81809e-06,4.42698e-10,-2.58998e-14,-8848.53,-34.3859], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 44,
    label = "C2H3OO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 O u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.09785,0.0295333,-2.27744e-05,7.20559e-09,-3.07929e-13,11399.6,21.3564], Tmin=(298.15,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.04484,0.0145511,-7.50975e-06,1.83488e-09,-1.6669e-13,10169.9,-3.71145], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298.15,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 45,
    label = "CHCHO",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u1 p0 c0 {2,D} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33257,0.0162953,-9.72052e-06,5.15124e-10,1.03837e-12,29658.5,13.9905], Tmin=(298.15,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.92633,0.00971712,-5.54856e-06,1.53069e-09,-1.64742e-13,28949.9,0.527875], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298.15,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 46,
    label = "C2H2",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.80868,0.0233616,-3.55172e-05,2.80153e-08,-8.50075e-12,26429,13.9397], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.65878,0.00488397,-1.60829e-06,2.46975e-10,-1.38606e-14,25759.4,-3.99838], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 47,
    label = "C2H",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {3,S}
2 C u1 p0 c0 {1,T}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.89868,0.0132988,-2.80733e-05,2.89485e-08,-1.07502e-11,67061.6,6.18548], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.6627,0.00382492,-1.36633e-06,2.13455e-10,-1.23217e-14,67168.4,3.92206], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 48,
    label = "H2CC",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u2 p0 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28155,0.00697648,-2.38552e-06,-1.21044e-09,9.81895e-13,48621.8,5.92039], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.27803,0.00475628,-1.6301e-06,2.54628e-10,-1.48864e-14,48316.7,0.640237], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 49,
    label = "C2H5OH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 O u0 p2 c0 {1,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.215806,0.0295228,-1.68271e-05,4.49485e-09,-4.02452e-13,-29485.2,24.5725], Tmin=(300,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[8.14484,0.0128314,-4.29053e-06,6.55972e-10,-3.76507e-14,-32400.6,-18.6241], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 50,
    label = "C2H5O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.90354,0.0177257,-2.69625e-06,-3.45831e-09,1.25225e-12,-3289.3,11.3546], Tmin=(300,'K'), Tmax=(1467,'K')),
            NASAPolynomial(coeffs=[8.19121,0.0110392,-3.75271e-06,5.80276e-10,-3.35735e-14,-5668.47,-19.0131], Tmin=(1467,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 51,
    label = "PC2H4OH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5948,0.0227101,-1.39474e-05,4.70096e-09,-6.90044e-13,-4914.87,14.3241], Tmin=(300,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[8.0675,0.0106144,-3.57999e-06,5.50364e-10,-3.17052e-14,-6927.48,-15.3833], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 52,
    label = "SC2H4OH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {7,S}
3 O u0 p2 c0 {2,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.46281,0.0239194,-1.30667e-05,3.10615e-09,-1.85896e-13,-8007.9,19.2547], Tmin=(300,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[8.15007,0.0102549,-3.40138e-06,5.1751e-10,-2.96129e-14,-10501.4,-17.3135], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 53,
    label = "O2C2H4OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  O u0 p2 c0 {1,S} {9,S}
4  O u0 p2 c0 {2,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u1 p2 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.0401,0.0159564,2.21097e-06,-7.05197e-09,2.08266e-12,-22452.4,-1.75362], Tmin=(300,'K'), Tmax=(1506,'K')),
            NASAPolynomial(coeffs=[12.7504,0.0111514,-3.83474e-06,5.98156e-10,-3.48372e-14,-25277.1,-35.4318], Tmin=(1506,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 54,
    label = "C2H4O2H",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {7,S} {8,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {3,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.75788,0.0288272,-2.08302e-05,8.47401e-09,-1.48618e-12,3001.54,15.9922], Tmin=(300,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[10.0591,0.0113379,-3.89403e-06,6.06091e-10,-3.52212e-14,424.049,-23.2087], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 55,
    label = "C2H4O1-2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75905,-0.00944122,8.03097e-05,-1.00808e-07,4.00399e-11,-7560.81,7.84975], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.48876,0.0120462,-4.33369e-06,7.00283e-10,-4.19491e-14,-9180.43,-7.07996], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 56,
    label = "C2H3O1-2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {3,S} {6,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58349,-0.00602276,6.32427e-05,-8.18541e-08,3.30445e-11,18568.1,9.59726], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.60158,0.00917614,-3.28029e-06,5.27904e-10,-3.15362e-14,17144.6,-5.47229], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 57,
    label = "CH3CHO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.72946,-0.00319329,4.75349e-05,-5.74586e-08,2.19311e-11,-21572.9,4.10302], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.40411,0.0117231,-4.22631e-06,6.83725e-10,-4.09849e-14,-22593.1,-3.48079], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 58,
    label = "CH3CO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03587,0.000877295,3.071e-05,-3.92476e-08,1.52969e-11,-2682.07,7.86177], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.31372,0.00917378,-3.32204e-06,5.39475e-10,-3.24524e-14,-3645.04,-1.67576], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 59,
    label = "CH2CHO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.79503,0.0101099,1.61751e-05,-3.10303e-08,1.39436e-11,162.945,12.3647], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.53928,0.00780239,-2.76414e-06,4.42099e-10,-2.62954e-14,-1188.59,-8.72091], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 60,
    label = "O2CH2CHO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
8 O u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.29466,0.0444936,-4.26577e-05,2.07392e-08,-3.96829e-12,-11827.6,36.0779], Tmin=(300,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[11.1808,0.00914479,-3.1509e-06,4.91944e-10,-2.86639e-14,-15579,-28.7893], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 61,
    label = "HO2CH2CO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {4,S}
3 C u1 p0 c0 {1,S} {7,D}
4 O u0 p2 c0 {2,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {3,D}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.22682,0.0356781,-3.26402e-05,1.47652e-08,-2.64794e-12,-11873.5,19.1581], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[10.4146,0.011268,-5.17495e-06,1.00333e-09,-6.68166e-14,-14095.6,-22.7894], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 62,
    label = "C2H3OH",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.127972,0.0338506,-3.30645e-05,1.64859e-08,-3.19935e-12,-15991.5,23.0439], Tmin=(300,'K'), Tmax=(1410,'K')),
            NASAPolynomial(coeffs=[8.32598,0.00803387,-2.63928e-06,3.98411e-10,-2.26551e-14,-18322.1,-20.208], Tmin=(1410,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 63,
    label = "C2H2OH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 O u0 p2 c0 {1,S} {6,S}
3 C u1 p0 c0 {1,D} {5,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.641643,0.0261904,-2.30385e-05,1.02805e-08,-1.81971e-12,14827.7,20.6751], Tmin=(300,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[8.20268,0.00592989,-1.99194e-06,3.05794e-10,-1.76115e-14,12488.1,-18.967], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 64,
    label = "CH2CO",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35724,0.0162213,-1.34812e-05,6.1194e-09,-1.13613e-12,-7113.93,11.299], Tmin=(300,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[6.32897,0.00544013,-1.82688e-06,2.80011e-10,-1.60964e-14,-8365.26,-9.53529], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 65,
    label = "HCCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 C u1 p0 c0 {3,D} {4,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87608,0.0221205,-3.58869e-05,3.05403e-08,-1.01281e-11,20163.4,13.6968], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.91479,0.00371409,-1.30137e-06,2.06473e-10,-1.21477e-14,19359.6,-5.50567], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 66,
    label = "HCCOH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,T}
2 O u0 p2 c0 {1,S} {5,S}
3 C u0 p0 c0 {1,T} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.05541,0.0252003,-3.80822e-05,3.09891e-08,-9.898e-12,9768.72,12.2272], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.3751,0.00549429,-1.88137e-06,2.93804e-10,-1.71772e-14,8932.78,-8.24498], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 67,
    label = "CH3CO3H",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {8,D}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 O u0 p2 c0 {2,D}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.24136,0.0337964,-2.53887e-05,9.67584e-09,-1.49266e-12,-42467.8,17.0668], Tmin=(300,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[12.506,0.0094779,-3.30402e-06,5.19631e-10,-3.04234e-14,-45985.7,-37.9196], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 68,
    label = "CH3CO3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 O u0 p2 c0 {2,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 O u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60373,0.027008,-2.08293e-05,8.50541e-09,-1.43846e-12,-23420.5,11.2015], Tmin=(300,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[11.2522,0.00833653,-2.89015e-06,4.52782e-10,-2.64354e-14,-26023.9,-29.637], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 69,
    label = "CH3CO2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
7 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.37441,0.0249116,-1.74309e-05,6.248e-09,-9.09517e-13,-27233,18.1405], Tmin=(300,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[8.5406,0.00832951,-2.84722e-06,4.41927e-10,-2.56373e-14,-29729.1,-20.3884], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 70,
    label = "CH3OCH3",
    molecule = 
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7548,0.00994331,2.04659e-05,-2.65049e-08,9.20398e-12,-23817.5,7.12147], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.13852,0.0258203,-1.29426e-05,3.14819e-09,-3.01295e-13,-23515.7,18.5133], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 71,
    label = "CH3OCH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {3,S} {7,S} {8,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93734,0.00990764,1.63346e-05,-2.34569e-08,8.57705e-12,-1325.48,7.99274], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.743,0.020653,-1.03926e-05,2.54086e-09,-2.44516e-13,-1329.87,12.4007], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 72,
    label = "CH3OCH2O2H",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {3,S} {4,S}
3  O u0 p2 c0 {2,S} {11,S}
4  C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
5  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.05787,0.0436787,-3.46384e-05,1.44809e-08,-2.46101e-12,-36885.1,24.3392], Tmin=(300,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[12.8159,0.0134818,-4.50398e-06,6.88229e-10,-3.94884e-14,-40674.6,-37.8048], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 73,
    label = "CH3OCH2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  O u0 p2 c0 {1,S} {2,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39931,0.030946,-1.92548e-05,5.76034e-09,-6.16082e-13,-20443.3,13.943], Tmin=(300,'K'), Tmax=(1441,'K')),
            NASAPolynomial(coeffs=[11.9179,0.0119413,-3.93526e-06,5.95756e-10,-3.39598e-14,-23423.2,-32.0097], Tmin=(1441,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 74,
    label = "CH2OCH2O2H",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u1 p0 c0 {3,S} {8,S} {9,S}
3  O u0 p2 c0 {1,S} {2,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.162245,0.0476101,-4.52047e-05,2.18379e-08,-4.11296e-12,-14649.8,29.8253], Tmin=(300,'K'), Tmax=(1418,'K')),
            NASAPolynomial(coeffs=[12.3893,0.0111759,-3.59249e-06,5.34196e-10,-3.00537e-14,-18055.2,-32.9577], Tmin=(1418,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 75,
    label = "O2CH2OCH2O2H",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,S} {7,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {5,S} {7,S}
4  O u0 p2 c0 {2,S} {12,S}
5  O u1 p2 c0 {3,S}
6  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
7  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
8  H u0 p0 c0 {7,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.39978,0.0539882,-4.8797e-05,2.19792e-08,-3.86107e-12,-33782.5,23.0683], Tmin=(300,'K'), Tmax=(1433,'K')),
            NASAPolynomial(coeffs=[17.7378,0.011359,-3.67383e-06,5.49256e-10,-3.10406e-14,-38290.3,-56.661], Tmin=(1433,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 76,
    label = "HO2CH2OCHO",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {6,S}
2  O u0 p2 c0 {3,S} {5,S}
3  O u0 p2 c0 {2,S} {10,S}
4  O u0 p2 c0 {6,D}
5  C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
6  C u0 p0 c0 {1,S} {4,D} {9,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2191,0.0428858,-3.17634e-05,1.11543e-08,-1.49753e-12,-57928.8,24.9759], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[15.7136,0.0096443,-3.44136e-06,5.49722e-10,-3.2536e-14,-62940.9,-52.9505], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 77,
    label = "OCH2OCHO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,D} {8,S}
3 O u0 p2 c0 {1,S} {2,S}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.8954,0.0274119,-1.36476e-05,1.26326e-09,5.1797e-13,-42787.9,20.2333], Tmin=(300,'K'), Tmax=(1523,'K')),
            NASAPolynomial(coeffs=[12.4013,0.00783738,-2.82993e-06,4.55559e-10,-2.71061e-14,-46845.3,-37.8085], Tmin=(1523,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 78,
    label = "HOCH2OCO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,S} {7,S}
4 C u1 p0 c0 {2,S} {8,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.95255,0.00842196,1.36742e-05,-1.46786e-08,3.84144e-12,-44447,2.85657], Tmin=(300,'K'), Tmax=(1443,'K')),
            NASAPolynomial(coeffs=[11.1498,0.00934737,-3.35542e-06,5.38037e-10,-3.1926e-14,-47501.2,-29.5984], Tmin=(1443,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 79,
    label = "CH3OCH2OH",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  O u0 p2 c0 {1,S} {2,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.15852,0.0244326,-8.66985e-06,-5.93319e-11,4.364e-13,-45448.9,13.0511], Tmin=(300,'K'), Tmax=(2014,'K')),
            NASAPolynomial(coeffs=[8.70982,0.0153602,-5.41004e-06,8.60573e-10,-5.0882e-14,-47660.7,-18.0227], Tmin=(2014,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 80,
    label = "CH3OCH2O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3 O u0 p2 c0 {1,S} {2,S}
4 O u1 p2 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.63414,0.0089283,1.37226e-05,-1.40497e-08,3.54626e-12,-22282.5,1.93589], Tmin=(300,'K'), Tmax=(1523,'K')),
            NASAPolynomial(coeffs=[9.81289,0.0121313,-4.30286e-06,6.84443e-10,-4.03863e-14,-25076.1,-25.1866], Tmin=(1523,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 81,
    label = "CH3OCHO",
    molecule = 
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,D} {8,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95243,0.00627937,3.21013e-05,-3.93941e-08,1.36186e-11,-44789.9,9.26882], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.55822,0.0263651,-1.49022e-05,3.93578e-09,-3.99334e-13,-44799.6,18.2846], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 82,
    label = "CH3OCO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u1 p0 c0 {2,S} {7,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.20427,0.00877415,1.5202e-05,-2.17224e-08,7.77728e-12,-20687.6,8.45258], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.36304,0.0187671,-1.03048e-05,2.67955e-09,-2.69525e-13,-20831.7,10.9018], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 83,
    label = "CH2OCHO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {3,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {4,D} {7,S}
3 O u0 p2 c0 {1,S} {2,S}
4 O u0 p2 c0 {2,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.19932,0.0193736,-1.21521e-06,-1.11559e-08,5.18761e-12,-20553.9,11.4662], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.66298,0.017398,-1.01218e-05,2.73226e-09,-2.81907e-13,-21438.9,-2.38514], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 84,
    label = "C3H8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.240878,0.0339549,-1.60931e-05,2.83481e-09,2.78195e-14,-14036.3,21.6501], Tmin=(300,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[9.15541,0.0172574,-5.85615e-06,9.0419e-10,-5.22524e-14,-17576.2,-27.7419], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 85,
    label = "IC3H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.897467,0.0415744,-4.94778e-05,4.56494e-08,-1.79085e-11,9939.5,29.2642], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.70776,0.0174048,-6.07616e-06,9.60084e-10,-5.65656e-14,7553.78,-10.3687], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 86,
    label = "NC3H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.20121,0.0529642,-7.23641e-05,6.36997e-08,-2.29333e-11,11513.1,34.3669], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.48614,0.0165769,-5.74876e-06,9.04104e-10,-5.30867e-14,8937.1,-14.2595], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 87,
    label = "NC3H7O2H",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.35816,0.0456684,-2.91646e-05,9.41701e-09,-1.22337e-12,-24152.8,22.3323], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[14.2246,0.0174341,-5.97064e-06,9.27754e-10,-5.38585e-14,-28816,-47.4358], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 88,
    label = "NC3H7O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.13312,0.0396692,-2.3757e-05,6.9602e-09,-7.82577e-13,-7466.87,19.2445], Tmin=(300,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[13.2753,0.0161303,-5.52348e-06,8.58197e-10,-4.98173e-14,-11603.3,-41.5091], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 89,
    label = "IC3H7O2H",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.77385,0.0475813,-3.43745e-05,1.31405e-08,-2.06923e-12,-26345.9,17.767], Tmin=(300,'K'), Tmax=(1405,'K')),
            NASAPolynomial(coeffs=[14.4896,0.0168268,-5.67601e-06,8.72851e-10,-5.02994e-14,-30647.8,-50.1352], Tmin=(1405,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 90,
    label = "IC3H7O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.58518,0.0416107,-2.92194e-05,1.08615e-08,-1.66312e-12,-9670.13,14.4731], Tmin=(300,'K'), Tmax=(1407,'K')),
            NASAPolynomial(coeffs=[13.5268,0.0154307,-5.17464e-06,7.92549e-10,-4.55415e-14,-13394.6,-44.0461], Tmin=(1407,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 91,
    label = "C3H6OOH1-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {2,S} {11,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.83631,0.038823,-2.47944e-05,7.85645e-09,-9.58634e-13,-1260.03,17.255], Tmin=(300,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[13.8089,0.0143846,-4.74441e-06,7.19308e-10,-4.10654e-14,-5143.53,-42.0211], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 92,
    label = "C3H6OOH1-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.74271,0.0453734,-3.5758e-05,1.4854e-08,-2.49982e-12,232.581,22.0973], Tmin=(300,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[13.9131,0.0140218,-4.55921e-06,6.84182e-10,-3.87696e-14,-3656.51,-42.1533], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 93,
    label = "C3H6OOH2-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.38466,0.0442929,-3.50977e-05,1.53695e-08,-2.81168e-12,-1809.8,16.9923], Tmin=(300,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[13.6645,0.015433,-5.29286e-06,8.23001e-10,-4.77931e-14,-5582.96,-42.8758], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 94,
    label = "C3H6OOH1-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {2,S} {6,S}
5  O u0 p2 c0 {1,S} {13,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99085,0.0531865,-4.28598e-05,1.77187e-08,-2.92769e-12,-20214.4,13.4151], Tmin=(300,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[19.1045,0.0144076,-4.72128e-06,7.12632e-10,-4.05578e-14,-25027.1,-66.3748], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 95,
    label = "C3H6OOH1-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  O u0 p2 c0 {2,S} {6,S}
5  O u0 p2 c0 {3,S} {13,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.56933,0.0468523,-3.58918e-05,1.43315e-08,-2.29776e-12,-18606.6,7.18655], Tmin=(300,'K'), Tmax=(1416,'K')),
            NASAPolynomial(coeffs=[18.1662,0.0147645,-4.74843e-06,7.06972e-10,-3.98306e-14,-22625.6,-59.3719], Tmin=(1416,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 96,
    label = "C3H6OOH2-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {6,S}
5  O u0 p2 c0 {2,S} {13,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99085,0.0531865,-4.28598e-05,1.77187e-08,-2.92769e-12,-20214.4,13.4151], Tmin=(300,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[19.1045,0.0144076,-4.72128e-06,7.12632e-10,-4.05578e-14,-25027.1,-66.3748], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 97,
    label = "C3KET12",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,D} {11,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.03883,0.053418,-4.47684e-05,1.94652e-08,-3.45055e-12,-37030.9,25.6511], Tmin=(300,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[17.0188,0.0132097,-4.67055e-06,7.41412e-10,-4.3687e-14,-42357.3,-59.2616], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 98,
    label = "C3KET13",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,D} {11,S}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.74957,0.0314081,-6.83838e-06,-5.67124e-09,2.27687e-12,-35192.5,9.83754], Tmin=(300,'K'), Tmax=(1508,'K')),
            NASAPolynomial(coeffs=[17.3613,0.0132331,-4.75332e-06,7.62529e-10,-4.52614e-14,-40624.8,-61.7768], Tmin=(1508,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 99,
    label = "C3H51-2,3OOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {7,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {13,S}
7  O u0 p2 c0 {4,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5562,0.0613504,-5.23205e-05,2.28208e-08,-4.02232e-12,-13135.3,22.1044], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[21.2378,0.013952,-4.94539e-06,7.86381e-10,-4.63926e-14,-19286.5,-76.9637], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 100,
    label = "C3H52-1,3OOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {2,S} {12,S}
4  O u0 p2 c0 {1,S} {6,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {4,S} {13,S}
7  O u0 p2 c0 {5,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12254,0.0519554,-3.83734e-05,1.45852e-08,-2.29821e-12,-12275.9,14.8367], Tmin=(300,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[20.2818,0.0148155,-5.25503e-06,8.35963e-10,-4.93309e-14,-18008.5,-72.2688], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 101,
    label = "C3H5O1-2OOH-3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  O u0 p2 c0 {1,S} {2,S}
5  O u0 p2 c0 {3,S} {6,S}
6  O u0 p2 c0 {5,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.25001,0.0665787,-6.1886e-05,2.84639e-08,-5.08512e-12,-22237.1,43.0381], Tmin=(300,'K'), Tmax=(1432,'K')),
            NASAPolynomial(coeffs=[15.7042,0.0130256,-4.23544e-06,6.35556e-10,-3.6011e-14,-27726.9,-55.1895], Tmin=(1432,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 102,
    label = "C3H5O1-3OOH-2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {3,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.43959,0.0716533,-7.15032e-05,3.51738e-08,-6.63683e-12,-22725,45.6394], Tmin=(300,'K'), Tmax=(1434,'K')),
            NASAPolynomial(coeffs=[14.4493,0.0136373,-4.25837e-06,6.20006e-10,-3.43452e-14,-27737.2,-50.6099], Tmin=(1434,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 103,
    label = "C3H6O1-2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {2,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42807,0.00625177,6.13196e-05,-8.60387e-08,3.51371e-11,-12844.7,10.4245], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.01491,0.017392,-6.26028e-06,1.01188e-09,-6.06239e-14,-15198.1,-18.828], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 104,
    label = "C3H6O1-3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
4  O u0 p2 c0 {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.15284,-0.0186402,0.000129981,-1.5863e-07,6.20669e-11,-11324.4,4.73561], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.80717,0.0188825,-6.79082e-06,1.09714e-09,-6.57155e-14,-13654.8,-13.5382], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 105,
    label = "C3H5-SOOH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0060548,0.0572963,-7.65094e-05,6.36301e-08,-2.20627e-11,-8822.38,26.8572], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.7367,0.0150781,-5.22874e-06,8.2257e-10,-4.83199e-14,-11905.2,-32.165], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 106,
    label = "C3H6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.54607,0.0436553,-5.61392e-05,4.98422e-08,-1.84799e-11,2070.56,29.9232], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.59032,0.0152593,-5.30369e-06,8.35511e-10,-4.91216e-14,-247.481,-11.5748], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 107,
    label = "C3H5-A",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.32899,0.0538423,-7.65501e-05,6.35512e-08,-2.14283e-11,20342.1,36.8038], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.37604,0.012345,-4.26464e-06,6.69046e-10,-3.92203e-14,17733.3,-16.1758], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 108,
    label = "C3H5-S",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u1 p0 c0 {2,D} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.61793,0.0244804,-1.41857e-05,4.16402e-09,-4.90905e-13,30429.1,16.6341], Tmin=(300,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[7.95954,0.0111163,-3.75198e-06,5.77246e-10,-3.32769e-14,28056.8,-17.98], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 109,
    label = "C3H5-T",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.29257,0.0198528,-6.42636e-06,-5.90016e-10,5.05491e-13,28577.3,13.9407], Tmin=(300,'K'), Tmax=(1376,'K')),
            NASAPolynomial(coeffs=[7.69949,0.0117804,-4.07792e-06,6.38119e-10,-3.7223e-14,26174.7,-16.8306], Tmin=(1376,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 110,
    label = "CC3H6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.83279,-0.00521029,9.29583e-05,-1.22753e-07,4.99191e-11,5195.2,10.8306], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.21663,0.0165394,-5.90076e-06,9.48095e-10,-5.65662e-14,2959.37,-13.6041], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 111,
    label = "CH3CHCHO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {8,D} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 O u0 p2 c0 {3,D}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.47167,0.0269252,-1.00248e-05,-1.13421e-09,1.03417e-12,-4041.42,18.8722], Tmin=(300,'K'), Tmax=(1424,'K')),
            NASAPolynomial(coeffs=[10.6781,0.0112806,-3.89011e-06,6.07617e-10,-3.54121e-14,-7732.34,-32.4971], Tmin=(1424,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 112,
    label = "CH3CHCO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.4838,0.0322203,-2.7025e-05,1.20499e-08,-2.18366e-12,-11527.7,17.1552], Tmin=(300,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[10.0219,0.00956966,-3.26222e-06,5.05232e-10,-2.92593e-14,-14248.3,-27.783], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 113,
    label = "C3H5O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.824069,0.034675,-2.51787e-05,9.56782e-09,-1.48085e-12,10420.4,22.8283], Tmin=(300,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[10.2638,0.011761,-3.89838e-06,5.92651e-10,-3.38867e-14,7259.38,-27.5109], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 114,
    label = "CH2CHOCH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u1 p0 c0 {4,S} {8,S} {9,S}
4 O u0 p2 c0 {1,S} {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.1535,0.0351254,-2.50072e-05,9.00716e-09,-1.32377e-12,10830.1,21.0607], Tmin=(300,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[12.0077,0.0105055,-3.69921e-06,5.8563e-10,-3.44432e-14,6973.12,-37.519], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 115,
    label = "AC4H7OOH",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {12,S}
4  C u0 p0 c0 {3,D} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.33471,0.0527831,-3.58861e-05,1.32495e-08,-2.06619e-12,-8878.92,24.3857], Tmin=(300,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[14.7661,0.0212235,-7.09403e-06,1.08424e-09,-6.22146e-14,-13561.7,-47.7449], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 116,
    label = "AC3H5OOH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.18125,0.0435233,-5.16277e-05,4.32011e-08,-1.57715e-11,-7635.22,12.1726], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.0839,0.0147947,-5.13213e-06,8.07505e-10,-4.74395e-14,-10218.4,-33.6435], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 117,
    label = "C3H4-P",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.68039,0.0157997,2.50706e-06,-1.36576e-08,6.61543e-12,20802.4,9.87694], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.02524,0.0113365,-4.02234e-06,6.43761e-10,-3.82996e-14,19620.9,-8.60438], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 118,
    label = "C3H4-A",
    molecule = 
"""
1 C u0 p0 c0 {3,D} {4,S} {5,S}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.61304,0.0121226,1.85399e-05,-3.45251e-08,1.53351e-11,21541.6,10.2261], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.31687,0.0111337,-3.96294e-06,6.35642e-10,-3.78755e-14,20117.5,-10.9958], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 119,
    label = "C3H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u1 p0 c0 {2,D} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.35111,0.0327411,-4.73827e-05,3.7631e-08,-1.18541e-11,40768,15.2059], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.14222,0.00761902,-2.6746e-06,4.24915e-10,-2.51475e-14,39571,-12.5849], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 120,
    label = "CC3H4",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {1,S} {2,D} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.024621,0.0231972,-1.84744e-06,-1.59276e-08,8.68462e-12,32334.1,22.7298], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.69999,0.0103574,-3.45512e-06,5.06529e-10,-2.66823e-14,30199.1,-13.3788], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 121,
    label = "C3H2",
    molecule = 
"""
multiplicity 3
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {5,T}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 C u1 p0 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.43417,0.0173013,-1.18294e-05,1.02756e-09,1.62626e-12,76907.5,12.1012], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.67325,0.00557729,-1.9918e-06,3.20289e-10,-1.91216e-14,75757.1,-9.72894], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 122,
    label = "C3H2(S)",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 C u2 p0 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.29765,0.0169875,-2.42665e-05,1.86537e-08,-5.5763e-12,67240.5,-3.754], Tmin=(200,'K'), Tmax=(900,'K')),
            NASAPolynomial(coeffs=[7.76426,0.00471128,-1.61706e-06,2.54724e-10,-1.50386e-14,66849.7,-15.0985], Tmin=(900,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 123,
    label = "C3H2C",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {3,S} {5,S}
3 C u2 p0 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.12959,0.0172874,-1.13668e-05,3.45693e-09,-3.6616e-13,58419.1,17.3314], Tmin=(200,'K'), Tmax=(1500,'K')),
            NASAPolynomial(coeffs=[6.56327,0.00523633,-1.75448e-06,2.68661e-10,-1.54285e-14,56514.6,-12.0006], Tmin=(1500,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 124,
    label = "PC3H4OH-1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {8,S}
3 C u1 p0 c0 {2,D} {4,S}
4 O u0 p2 c0 {3,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.0715,0.0350017,-3.01922e-05,1.38468e-08,-2.5538e-12,6819.14,15.1917], Tmin=(300,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[10.9469,0.0104015,-3.44082e-06,5.22106e-10,-2.98049e-14,4115.31,-31.1162], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 125,
    label = "PC3H4OH-2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {3,D} {4,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 O u0 p2 c0 {2,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.42757,0.0364826,-3.18007e-05,1.46915e-08,-2.72331e-12,7803.43,18.589], Tmin=(300,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[10.7164,0.0106066,-3.51374e-06,5.33714e-10,-3.04902e-14,4984.87,-29.8329], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 126,
    label = "PC3H4OH-3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {4,S} {6,S}
3 C u1 p0 c0 {1,S} {7,S} {8,S}
4 O u0 p2 c0 {2,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.406368,0.0370231,-2.72203e-05,1.05783e-08,-1.73633e-12,527.161,23.4782], Tmin=(300,'K'), Tmax=(1378,'K')),
            NASAPolynomial(coeffs=[11.5298,0.0114381,-4.04415e-06,6.41949e-10,-3.78242e-14,-3454.86,-36.5385], Tmin=(1378,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 127,
    label = "SC3H4OH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 O u0 p2 c0 {1,S} {9,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.72871,0.0441016,-4.72014e-05,2.52074e-08,-5.13376e-12,2227.21,14.3928], Tmin=(300,'K'), Tmax=(1407,'K')),
            NASAPolynomial(coeffs=[12.0968,0.00943977,-3.10774e-06,4.69609e-10,-2.67166e-14,-385.855,-37.6796], Tmin=(1407,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 128,
    label = "C3H3O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {7,S}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.875024,0.0351184,-3.89901e-05,2.40256e-08,-6.10884e-12,32042.8,20.4717], Tmin=(298.15,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.19356,0.0195625,-1.22336e-05,3.90615e-09,-5.08539e-13,31493.2,5.03216], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298.15,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 129,
    label = "C3H3O2H",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2 O u0 p2 c0 {1,S} {4,S}
3 C u0 p0 c0 {1,S} {5,T}
4 O u0 p2 c0 {2,S} {9,S}
5 C u0 p0 c0 {3,T} {8,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.09787,0.0422718,-3.83969e-05,1.77405e-08,-3.27674e-12,10359.2,23.0652], Tmin=(300,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[13.8152,0.00862175,-3.0671e-06,4.88874e-10,-2.88888e-14,6291.83,-43.9151], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 130,
    label = "C2HCHO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,D} {5,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {6,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.20777,0.0134383,-5.15442e-06,-2.24571e-11,2.74111e-13,10211.7,5.43872], Tmin=(300,'K'), Tmax=(2012,'K')),
            NASAPolynomial(coeffs=[7.99952,0.00707825,-2.63087e-06,4.33073e-10,-2.62003e-14,8718.63,-15.7226], Tmin=(2012,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 131,
    label = "NC3H7OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0570007,0.0417376,-2.49234e-05,7.16029e-09,-7.2507e-13,-32430.7,27.029], Tmin=(300,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[11.2834,0.0171532,-5.56084e-06,8.32707e-10,-4.71119e-14,-36417.4,-33.718], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 132,
    label = "C3H6OH1-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {4,S} {10,S}
4  O u0 p2 c0 {3,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.13615,0.0368851,-2.24074e-05,6.62399e-09,-7.32206e-13,-10927.3,22.4919], Tmin=(300,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[11.4795,0.0145881,-4.88359e-06,7.47607e-10,-4.29608e-14,-14683.2,-33.6826], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 133,
    label = "C3H6OH1-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  O u0 p2 c0 {1,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.505208,0.036387,-2.15531e-05,6.45585e-09,-7.71267e-13,-9269.81,27.9804], Tmin=(300,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[10.0338,0.0160227,-5.41658e-06,8.34191e-10,-4.81216e-14,-12791.2,-23.9034], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 134,
    label = "C3H6OH1-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  O u0 p2 c0 {2,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.53523,0.0342021,-2.1191e-05,6.89185e-09,-9.29272e-13,-7899.7,15.5563], Tmin=(300,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[11.2537,0.0148843,-5.00125e-06,7.67004e-10,-4.41141e-14,-11052.2,-31.6714], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 135,
    label = "NC3H7O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  O u1 p2 c0 {3,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.57487,0.0307101,-1.20049e-05,3.40807e-12,7.25275e-13,-6209.13,14.5966], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[11.5279,0.0153776,-5.23946e-06,8.11383e-10,-4.69928e-14,-9851,-35.4233], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 136,
    label = "C3H5OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.15012,0.0128538,4.28438e-05,-6.67819e-08,2.80408e-11,-16641.4,13.5066], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.72477,0.0163943,-5.90853e-06,9.53262e-10,-5.70318e-14,-19049.7,-19.7199], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 137,
    label = "SC3H5OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  O u0 p2 c0 {3,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0353977,0.0434969,-3.7448e-05,1.70906e-08,-3.13775e-12,-20250.3,24.1528], Tmin=(300,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[11.1222,0.0127745,-4.25316e-06,6.48216e-10,-3.71191e-14,-23669.1,-34.1335], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 138,
    label = "CH2CCH2OH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 O u0 p2 c0 {1,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.88423,0.0242428,-1.14152e-05,1.71775e-09,1.42177e-13,11793.6,15.2102], Tmin=(300,'K'), Tmax=(1372,'K')),
            NASAPolynomial(coeffs=[9.70702,0.0113973,-3.77994e-06,5.75209e-10,-3.29229e-14,9132.13,-22.5013], Tmin=(1372,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 139,
    label = "HOC3H6O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {13,S}
2  O u0 p2 c0 {3,S} {5,S}
3  O u1 p2 c0 {2,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
6  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.8496,0.0477245,-3.60393e-05,1.4348e-08,-2.33508e-12,-28210.6,17.6479], Tmin=(300,'K'), Tmax=(1407,'K')),
            NASAPolynomial(coeffs=[15.6948,0.0157704,-5.30502e-06,8.14308e-10,-4.68666e-14,-32454.1,-50.6084], Tmin=(1407,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 140,
    label = "IC3H7OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.253082,0.0417886,-2.38155e-05,5.85131e-09,-3.55869e-13,-34527,24.2125], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[12.5041,0.0162138,-5.3502e-06,8.11484e-10,-4.63435e-14,-38997.6,-42.5159], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 141,
    label = "C3H6OH2-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0967,0.0380728,-2.75022e-05,1.07477e-08,-1.74896e-12,-14076.4,22.2476], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[11.2222,0.0136444,-4.51407e-06,7.10523e-10,-4.2269e-14,-17535,-31.8912], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 142,
    label = "TC3H6OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {2,S} {4,S}
4  O u0 p2 c0 {3,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0967,0.0380728,-2.75022e-05,1.07477e-08,-1.74896e-12,-14076.4,22.2476], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[11.2222,0.0136444,-4.51407e-06,7.10523e-10,-4.2269e-14,-17535,-31.8912], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 143,
    label = "IC3H7O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u1 p2 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.36108,0.034565,-1.9458e-05,4.71537e-09,-2.64705e-13,-8287.91,13.3112], Tmin=(300,'K'), Tmax=(1527,'K')),
            NASAPolynomial(coeffs=[11.9648,0.0142944,-4.71413e-06,7.14027e-10,-4.07161e-14,-11751.9,-38.8861], Tmin=(1527,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 144,
    label = "IC3H5OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {2,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.58376,0.0316215,-1.73665e-05,4.18928e-09,-2.799e-13,-21264.3,18.8314], Tmin=(300,'K'), Tmax=(1374,'K')),
            NASAPolynomial(coeffs=[10.7381,0.0131698,-4.4153e-06,6.7701e-10,-3.89609e-14,-24729.8,-31.3634], Tmin=(1374,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 145,
    label = "CH3COCH3",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.20008,0.027402,-1.31342e-05,2.5715e-09,-6.21509e-14,-27993.4,15.5884], Tmin=(300,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[8.87619,0.01457,-4.84823e-06,7.38615e-10,-4.22831e-14,-30604.6,-21.273], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 146,
    label = "CH3COCH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u1 p2 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.13382,0.0325095,-2.10425e-05,6.64421e-09,-8.12619e-13,-6048.68,21.7159], Tmin=(300,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[10.9524,0.0111459,-3.86263e-06,6.05089e-10,-3.53293e-14,-9608.34,-31.5623], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 147,
    label = "CH3COCH2O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {6,D}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {2,D} {4,S} {5,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.19378,0.0498027,-4.18e-05,1.74528e-08,-2.88199e-12,-19324.4,26.7877], Tmin=(300,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[16.5756,0.0106465,-3.61369e-06,5.59054e-10,-3.23832e-14,-24254.1,-54.5305], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 148,
    label = "CH3COCH2O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  O u1 p2 c0 {2,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.8596,0.0178955,7.41506e-07,-5.40033e-09,1.47393e-12,-19071.5,2.70988], Tmin=(300,'K'), Tmax=(2002,'K')),
            NASAPolynomial(coeffs=[9.84062,0.0159181,-5.85165e-06,9.5616e-10,-5.75477e-14,-21121.5,-21.2331], Tmin=(2002,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 149,
    label = "C3KET21",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,D}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.874353,0.0612501,-5.51475e-05,2.48491e-08,-4.42613e-12,-35806.1,35.9306], Tmin=(300,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[17.5768,0.0120312,-4.11634e-06,6.40149e-10,-3.72128e-14,-41550.2,-60.9097], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 150,
    label = "C2H3CHO",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {5,D} {8,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {3,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.733844,0.0317483,-2.29599e-05,8.42104e-09,-1.23613e-12,-9384.74,21.0309], Tmin=(300,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[9.99155,0.00982348,-3.31203e-06,5.09524e-10,-2.93822e-14,-12530.4,-28.5169], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 151,
    label = "C2H3CO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 C u1 p0 c0 {1,S} {7,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.65335,0.0257403,-1.8901e-05,7.29175e-09,-1.16083e-12,10202.1,17.8706], Tmin=(300,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[8.86033,0.00848985,-2.9035e-06,4.50764e-10,-2.61524e-14,7734.89,-20.6979], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 152,
    label = "C2H5CHO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.18896,0.025829,-6.0417e-06,-3.70703e-09,1.57131e-12,-24267.1,16.1496], Tmin=(300,'K'), Tmax=(1449,'K')),
            NASAPolynomial(coeffs=[10.6224,0.0135569,-4.60755e-06,7.12755e-10,-4.12632e-14,-27869.2,-31.6629], Tmin=(1449,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 153,
    label = "C2H5CO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {9,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.25722,-0.00917612,7.6119e-05,-9.05515e-08,3.46198e-11,-5916.16,2.23331], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.52325,0.0154212,-5.50898e-06,8.8589e-10,-5.28846e-14,-7196.32,-5.19862], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 154,
    label = "CH2CH2CHO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {6,D} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {3,D}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.55799,0.0223392,-4.89741e-06,-3.58874e-09,1.47175e-12,453.128,16.7016], Tmin=(300,'K'), Tmax=(1437,'K')),
            NASAPolynomial(coeffs=[10.0673,0.0114971,-3.90138e-06,6.03029e-10,-3.48958e-14,-2750.81,-25.8818], Tmin=(1437,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 155,
    label = "C4H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0920862,0.0469704,-2.54762e-05,6.35895e-09,-5.16006e-13,-16955.7,24.9102], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[12.4924,0.0215952,-7.34278e-06,1.1353e-09,-6.5673e-14,-21759.9,-44.1547], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 156,
    label = "PC4H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.409645,0.0429511,-2.36583e-05,6.15745e-09,-5.64301e-13,7743.19,25.5313], Tmin=(300,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[11.8548,0.0196962,-6.71054e-06,1.03891e-09,-6.01514e-14,3381.82,-37.2343], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 157,
    label = "SC4H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.942662,0.0377415,-1.58912e-05,1.75489e-09,2.89726e-13,6205.43,24.2127], Tmin=(300,'K'), Tmax=(1682,'K')),
            NASAPolynomial(coeffs=[9.25139,0.0224301,-7.82649e-06,1.23559e-09,-7.2625e-14,3111.49,-21.608], Tmin=(1682,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 158,
    label = "PC4H9O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {9,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u1 p2 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.84659,0.0461054,-2.44857e-05,5.11293e-09,-1.07538e-13,-9092.07,19.5237], Tmin=(300,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[15.3372,0.019279,-6.56857e-06,1.01724e-09,-5.89183e-14,-14195.9,-54.5072], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 159,
    label = "SC4H9O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u1 p2 c0 {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.01773,0.0470084,-2.74727e-05,7.3629e-09,-6.30414e-13,-11189.2,17.4372], Tmin=(300,'K'), Tmax=(1411,'K')),
            NASAPolynomial(coeffs=[15.213,0.019003,-6.39005e-06,9.80774e-10,-5.64494e-14,-15988.9,-54.3195], Tmin=(1411,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 160,
    label = "PC4H9O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {15,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.80541,0.0526493,-3.3087e-05,1.04593e-08,-1.32306e-12,-10386.7,22.483], Tmin=(300,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[16.612,0.0204752,-7.01415e-06,1.09011e-09,-6.32914e-14,-15790.2,-57.9272], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 161,
    label = "SC4H9O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.27751,0.0544335,-3.82988e-05,1.42448e-08,-2.18865e-12,-12590.9,18.3237], Tmin=(300,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[16.8209,0.0198834,-6.71756e-06,1.03412e-09,-5.96371e-14,-17581.5,-59.5731], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 162,
    label = "PC4H9O2H",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {6,S}
6  O u0 p2 c0 {5,S} {16,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.04178,0.0585997,-3.84212e-05,1.28728e-08,-1.75491e-12,-27074.4,25.518], Tmin=(300,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[17.5611,0.0217833,-7.46366e-06,1.16012e-09,-6.7363e-14,-33003.6,-63.8547], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 163,
    label = "SC4H9O2H",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.44011,0.06053,-4.36263e-05,1.66226e-08,-2.61557e-12,-29263.1,21.7354], Tmin=(300,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[17.8076,0.0212546,-7.2096e-06,1.11291e-09,-6.4306e-14,-34845.6,-65.8011], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 164,
    label = "C4H8OOH1-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {2,S} {14,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.91878,0.0486144,-2.81342e-05,7.64456e-09,-7.32889e-13,-3944.65,18.9326], Tmin=(300,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[16.781,0.0199678,-6.85257e-06,1.06629e-09,-6.19616e-14,-9147.63,-56.8668], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 165,
    label = "C4H8OOH1-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.46293,0.0470131,-2.42145e-05,4.65408e-09,1.62199e-14,-3957.88,22.457], Tmin=(300,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[16.1248,0.0202421,-6.88631e-06,1.06535e-09,-6.166e-14,-9168.02,-52.6575], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 166,
    label = "C4H8OOH1-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.35984,0.0552812,-3.75641e-05,1.32624e-08,-1.93623e-12,-2344.56,26.3198], Tmin=(300,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[16.9218,0.0199306,-6.85728e-06,1.06879e-09,-6.21775e-14,-7879.21,-57.663], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 167,
    label = "C4H8OOH2-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.32205,0.0555032,-3.97238e-05,1.47354e-08,-2.22482e-12,-4673.32,19.8332], Tmin=(300,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[17.7648,0.0187777,-6.3641e-06,9.81958e-10,-5.67252e-14,-9938.52,-62.817], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 168,
    label = "C4H8OOH2-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3029,0.0508232,-3.39615e-05,1.17622e-08,-1.66013e-12,-6136.71,15.1726], Tmin=(300,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[17.0354,0.019273,-6.50685e-06,1.00126e-09,-5.77271e-14,-10943.7,-58.7403], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 169,
    label = "C4H8OOH2-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.82673,0.0569912,-4.24389e-05,1.67119e-08,-2.70636e-12,-4546.3,22.2052], Tmin=(300,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[17.2354,0.0191946,-6.49947e-06,1.00211e-09,-5.7856e-14,-9711.58,-59.8986], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 170,
    label = "C4H8O1-2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.29657,0.0675907,-5.89614e-05,2.59401e-08,-4.45927e-12,-14880,44.7756], Tmin=(300,'K'), Tmax=(1463,'K')),
            NASAPolynomial(coeffs=[14.1886,0.0163163,-5.16581e-06,7.60174e-10,-4.24548e-14,-20283.9,-51.2818], Tmin=(1463,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 171,
    label = "C4H8O1-3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.37284,0.0662224,-5.35318e-05,2.19452e-08,-3.5448e-12,-15414.5,49.8345], Tmin=(300,'K'), Tmax=(1447,'K')),
            NASAPolynomial(coeffs=[13.2077,0.0177468,-5.69934e-06,8.47771e-10,-4.77346e-14,-21171.8,-47.8386], Tmin=(1447,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 172,
    label = "C4H8O1-4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.78118,0.0698405,-5.45316e-05,2.1303e-08,-3.24667e-12,-22899.6,61.7621], Tmin=(300,'K'), Tmax=(1484,'K')),
            NASAPolynomial(coeffs=[12.2763,0.0189106,-6.09114e-06,9.08066e-10,-5.1215e-14,-29226.1,-44.1236], Tmin=(1484,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 173,
    label = "C4H8O2-3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.48183,0.0689313,-6.15372e-05,2.73744e-08,-4.85891e-12,-16892.4,43.8883], Tmin=(300,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[10.6342,0.0241442,-1.13124e-05,2.25481e-09,-1.54043e-13,-21038.3,-33.6764], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 174,
    label = "C4H8OOH1-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.02241,0.0653863,-4.89646e-05,1.90438e-08,-3.02309e-12,-22580.6,20.5729], Tmin=(300,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[21.5735,0.0204529,-6.99498e-06,1.08598e-09,-6.30071e-14,-28842.8,-78.4561], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 175,
    label = "C4H8OOH1-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.02241,0.0653863,-4.89646e-05,1.90438e-08,-3.02309e-12,-22580.6,20.5729], Tmin=(300,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[21.5735,0.0204529,-6.99498e-06,1.08598e-09,-6.30071e-14,-28842.8,-78.4561], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 176,
    label = "C4H8OOH1-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {4,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.91974,0.0634948,-4.29699e-05,1.42283e-08,-1.84506e-12,-20486.7,22.6279], Tmin=(300,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[22.6393,0.0198017,-6.9235e-06,1.091e-09,-6.39618e-14,-27544.2,-84.0748], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 177,
    label = "C4H8OOH2-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.02241,0.0653863,-4.89646e-05,1.90438e-08,-3.02309e-12,-22580.6,20.5729], Tmin=(300,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[21.5735,0.0204529,-6.99498e-06,1.08598e-09,-6.30071e-14,-28842.8,-78.4561], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 178,
    label = "C4H8OOH2-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.34684,0.0667468,-5.25089e-05,2.14288e-08,-3.53382e-12,-24734.1,17.3189], Tmin=(300,'K'), Tmax=(1408,'K')),
            NASAPolynomial(coeffs=[21.9463,0.0197308,-6.65765e-06,1.02425e-09,-5.90486e-14,-30777.2,-81.2054], Tmin=(1408,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 179,
    label = "C4H8OOH2-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.02241,0.0653863,-4.89646e-05,1.90438e-08,-3.02309e-12,-22580.6,20.5729], Tmin=(300,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[21.5735,0.0204529,-6.99498e-06,1.08598e-09,-6.30071e-14,-28842.8,-78.4561], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 180,
    label = "C4H71-2,4OOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {3,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  O u0 p2 c0 {5,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.99387,0.0652914,-4.87959e-05,1.88108e-08,-2.95257e-12,-14602.1,22.7764], Tmin=(300,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[21.863,0.0199359,-6.85104e-06,1.06712e-09,-6.20562e-14,-21004.3,-78.0707], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 181,
    label = "C4H72-1,3OOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {2,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  O u0 p2 c0 {5,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85542,0.0605524,-4.18122e-05,1.4668e-08,-2.07882e-12,-16035.9,18.7735], Tmin=(300,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[21.4626,0.0202946,-6.97889e-06,1.08751e-09,-6.32605e-14,-22219.7,-76.0672], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 182,
    label = "C4H72-1,4OOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {3,S} {15,S}
5  O u0 p2 c0 {2,S} {8,S}
6  O u0 p2 c0 {3,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  O u0 p2 c0 {5,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41715,0.0589886,-3.76843e-05,1.1845e-08,-1.46347e-12,-13843.8,22.7095], Tmin=(300,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[21.0229,0.0210128,-7.3035e-06,1.14623e-09,-6.70076e-14,-20290.8,-72.9927], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 183,
    label = "C4H71-2,3OOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {2,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  O u0 p2 c0 {5,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.30791,0.0666513,-5.21745e-05,2.10434e-08,-3.42495e-12,-16753.7,19.5807], Tmin=(300,'K'), Tmax=(1406,'K')),
            NASAPolynomial(coeffs=[22.2829,0.0192254,-6.52861e-06,1.00882e-09,-5.83408e-14,-22972,-81.1232], Tmin=(1406,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 184,
    label = "C4H7O1-3OOH-4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {4,S} {7,S}
7  O u0 p2 c0 {6,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.4095,0.0805103,-6.64646e-05,2.73712e-08,-4.44857e-12,-25300.5,55.6327], Tmin=(300,'K'), Tmax=(1418,'K')),
            NASAPolynomial(coeffs=[18.725,0.0188463,-6.40166e-06,9.89755e-10,-5.72728e-14,-32982.6,-71.8225], Tmin=(1418,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 185,
    label = "C4H7O1-3OOH-2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.68244,0.080342,-6.67265e-05,2.74081e-08,-4.41624e-12,-27530.7,50.4193], Tmin=(300,'K'), Tmax=(1425,'K')),
            NASAPolynomial(coeffs=[19.711,0.017906,-6.05725e-06,9.3411e-10,-5.39628e-14,-35253.3,-78.3129], Tmin=(1425,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 186,
    label = "C4H7O1-2OOH-4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {4,S} {7,S}
7  O u0 p2 c0 {6,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.06057,0.0752777,-6.16382e-05,2.51521e-08,-4.05109e-12,-24931,44.8871], Tmin=(300,'K'), Tmax=(1417,'K')),
            NASAPolynomial(coeffs=[19.6187,0.0177382,-6.03564e-06,9.34268e-10,-5.41073e-14,-32191.8,-75.0296], Tmin=(1417,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 187,
    label = "C4H7O1-4OOH-2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
5  O u0 p2 c0 {3,S} {4,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.17427,0.0789226,-6.62654e-05,2.77699e-08,-4.54378e-12,-35378.1,53.5508], Tmin=(300,'K'), Tmax=(1470,'K')),
            NASAPolynomial(coeffs=[17.4906,0.0187795,-6.05492e-06,9.03186e-10,-5.09572e-14,-42271.7,-65.186], Tmin=(1470,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 188,
    label = "C4H7O1-2OOH-3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {15,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.944964,0.0731027,-6.71228e-05,3.12252e-08,-5.67207e-12,-27451.1,32.5427], Tmin=(300,'K'), Tmax=(1435,'K')),
            NASAPolynomial(coeffs=[18.3476,0.0172628,-5.5344e-06,8.21396e-10,-4.6148e-14,-32922.4,-66.992], Tmin=(1435,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 189,
    label = "C4H7O2-3OOH-1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {3,S} {7,S}
7  O u0 p2 c0 {6,S} {15,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.04171,0.0775255,-6.55777e-05,2.74944e-08,-4.52477e-12,-27034.3,43.3137], Tmin=(300,'K'), Tmax=(1424,'K')),
            NASAPolynomial(coeffs=[20.3028,0.0169332,-5.71129e-06,8.79006e-10,-5.07088e-14,-34345.1,-79.5919], Tmin=(1424,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 190,
    label = "C4H72-1OOH",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {13,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.29755,0.0559252,-4.0889e-05,1.54881e-08,-2.42412e-12,-11604.7,24.3621], Tmin=(300,'K'), Tmax=(1381,'K')),
            NASAPolynomial(coeffs=[18.0123,0.0170341,-5.89884e-06,9.23962e-10,-5.3954e-14,-17458.5,-65.521], Tmin=(1381,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 191,
    label = "NC4KET12",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.724232,0.0726649,-6.04779e-05,2.54349e-08,-4.30153e-12,-37293.7,35.6277], Tmin=(300,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[21.7577,0.0164473,-5.79962e-06,9.1915e-10,-5.41037e-14,-44711.5,-83.7725], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 192,
    label = "NC4KET13",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.31776,0.0528482,-3.43212e-05,1.04563e-08,-1.12797e-12,-39486.8,15.8443], Tmin=(300,'K'), Tmax=(1411,'K')),
            NASAPolynomial(coeffs=[19.3085,0.0173455,-5.85047e-06,9.00298e-10,-5.19275e-14,-45102.4,-70.487], Tmin=(1411,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 193,
    label = "NC4KET14",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,D} {14,S}
5  O u0 p2 c0 {3,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.92379,0.0507578,-2.88361e-05,6.6465e-09,-2.83907e-13,-37294.6,19.6328], Tmin=(300,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[18.9232,0.018227,-6.27434e-06,9.78729e-10,-5.69844e-14,-43250.9,-67.8717], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 194,
    label = "NC4KET21",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {2,S} {14,D}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.388449,0.0692735,-5.58731e-05,2.25791e-08,-3.639e-12,-38687.6,35.2948], Tmin=(300,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[21.0786,0.0161788,-5.53076e-06,8.59641e-10,-4.99535e-14,-45756.4,-78.8015], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 195,
    label = "NC4KET23",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56927,0.0520286,-3.64134e-05,1.32008e-08,-1.93577e-12,-43065.1,14.8669], Tmin=(300,'K'), Tmax=(1411,'K')),
            NASAPolynomial(coeffs=[17.6878,0.018482,-6.18385e-06,9.45792e-10,-5.42982e-14,-47859.4,-60.6682], Tmin=(1411,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 196,
    label = "NC4KET24",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.12063,0.0501344,-3.10195e-05,9.36512e-09,-1.07549e-12,-40864.4,19.6072], Tmin=(300,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[17.4146,0.0192744,-6.57971e-06,1.02024e-09,-5.91418e-14,-46066.3,-58.0321], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 197,
    label = "C4H71-3OOH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.50977,0.0685369,-5.75194e-05,2.43179e-08,-4.09788e-12,-11801.9,35.042], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[19.2985,0.0154534,-5.2546e-06,8.13772e-10,-4.7169e-14,-18500.3,-74.9927], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 198,
    label = "C4H71-4OOH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.31653,0.0516546,-3.47311e-05,1.20406e-08,-1.71651e-12,-11775.5,24.6385], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[15.9871,0.0186028,-6.40003e-06,9.97532e-10,-5.80334e-14,-17015.2,-54.6227], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 199,
    label = "C4H71-3,4OOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u1 p0 c0 {2,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {3,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  O u0 p2 c0 {5,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5689,0.0671962,-5.17e-05,2.0577e-08,-3.32914e-12,-14512.6,24.6333], Tmin=(300,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[21.8395,0.0198803,-6.81505e-06,1.05975e-09,-6.1556e-14,-20946.9,-77.9985], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 200,
    label = "C4H72-3,4OOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {3,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  O u0 p2 c0 {5,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85542,0.0605524,-4.18122e-05,1.4668e-08,-2.07882e-12,-16035.9,18.7735], Tmin=(300,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[21.4626,0.0202946,-6.97889e-06,1.08751e-09,-6.32605e-14,-22219.7,-76.0672], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 201,
    label = "HO2CH2CHO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {7,D} {8,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {3,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.32769,0.0521619,-4.97328e-05,2.31272e-08,-4.20788e-12,-29060.9,36.186], Tmin=(300,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[15.1555,0.0075724,-2.72693e-06,4.38217e-10,-2.60434e-14,-34142,-50.1255], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 202,
    label = "C4H71-O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.10873,0.022875,3.92794e-06,-1.04316e-08,2.89511e-12,3533.02,-0.349512], Tmin=(300,'K'), Tmax=(1369,'K')),
            NASAPolynomial(coeffs=[15.6997,0.0161015,-6.49437e-06,1.11549e-09,-6.91568e-14,-1624.98,-57.8468], Tmin=(1369,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 203,
    label = "IC4H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.07414,0.0524618,-3.42408e-05,1.18818e-08,-1.73238e-12,-17921.9,27.4852], Tmin=(300,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[12.6423,0.0214134,-7.26712e-06,1.12207e-09,-6.48434e-14,-22829.4,-46.606], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 204,
    label = "IC4H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.120802,0.0473187,-3.1644e-05,1.1423e-08,-1.74785e-12,6840.33,24.4291], Tmin=(300,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[12.3262,0.0192058,-6.52064e-06,1.00704e-09,-5.82039e-14,2509.96,-41.3479], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 205,
    label = "TC4H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.05842,0.0341134,-9.03157e-06,-2.95313e-09,1.41437e-12,4226.99,22.3965], Tmin=(300,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[10.2683,0.0209965,-7.14946e-06,1.10648e-09,-6.40498e-14,157.543,-30.0961], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 206,
    label = "TC4H9O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.77057,0.0268033,4.12718e-05,-7.22055e-08,3.02642e-11,-12707.9,12.1533], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.7372,0.0233707,-8.50517e-06,1.3852e-09,-8.34398e-14,-16694,-45.3156], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 207,
    label = "IC4H9O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  O u1 p2 c0 {4,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80297,0.0156874,6.81105e-05,-9.83347e-08,3.95262e-11,-10083.2,9.78963], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.631,0.0247982,-9.01551e-06,1.46715e-09,-8.83215e-14,-13785.5,-38.1956], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 208,
    label = "IC3H7CHO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,D} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.273021,0.0489696,-3.1277e-05,1.00053e-08,-1.27512e-12,-27605.5,28.3451], Tmin=(300,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[13.7502,0.0183127,-6.28573e-06,9.78251e-10,-5.68539e-14,-32693.7,-47.7271], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 209,
    label = "SC4H7OH-I",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,S} {12,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.70103,0.041795,-2.67861e-05,9.38191e-09,-1.41171e-12,-27356.1,13.5316], Tmin=(300,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[13.0299,0.0183782,-6.1853e-06,9.49578e-10,-5.46526e-14,-31072.3,-42.2892], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 210,
    label = "IC4H6OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {5,S} {9,S}
4  C u1 p0 c0 {2,S} {10,S} {11,S}
5  O u0 p2 c0 {3,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.46664,0.0603352,-5.43113e-05,2.493e-08,-4.52282e-12,-6950.12,32.0768], Tmin=(300,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[15.3491,0.0138857,-4.56428e-06,6.90419e-10,-3.9354e-14,-12016.5,-55.5976], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 211,
    label = "IC3H7CO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.503453,0.0441608,-2.82139e-05,8.93549e-09,-1.11327e-12,-9077.55,26.1991], Tmin=(300,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[13.3306,0.0161874,-5.56711e-06,8.67576e-10,-5.04697e-14,-13730.7,-43.3959], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 212,
    label = "IC3H6CHO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {9,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {4,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.521482,0.0443114,-2.86617e-05,9.3032e-09,-1.20762e-12,-2996.77,26.8182], Tmin=(300,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[13.3102,0.0162098,-5.57576e-06,8.69004e-10,-5.05554e-14,-7621.78,-42.5051], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 213,
    label = "TC3H6CHO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {2,S} {4,S}
4  C u0 p0 c0 {3,S} {11,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87053,0.041487,-2.66816e-05,9.01532e-09,-1.27871e-12,-8977.31,16.6174], Tmin=(300,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[13.1013,0.0166392,-5.68458e-06,8.81808e-10,-5.1129e-14,-13063.9,-44.2706], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 214,
    label = "IC3H5CHO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {8,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {4,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.09373,0.0443315,-3.41918e-05,1.3937e-08,-2.33791e-12,-15674.6,19.4458], Tmin=(300,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[13.3892,0.0139115,-4.75821e-06,7.38737e-10,-4.28607e-14,-19791.7,-46.0146], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 215,
    label = "IC3H6CO",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.28039,0.0417017,-3.2509e-05,1.37243e-08,-2.40573e-12,-16394,13.8188], Tmin=(300,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[13.2548,0.0140143,-4.7891e-06,7.42924e-10,-4.30738e-14,-20053,-44.481], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 216,
    label = "IC3H5CO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  C u1 p0 c0 {2,S} {10,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87307,0.0395189,-3.11404e-05,1.28844e-08,-2.18165e-12,2852.71,16.8774], Tmin=(300,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[12.9634,0.0117955,-4.04361e-06,6.28772e-10,-3.6521e-14,-826.519,-42.0563], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 217,
    label = "IC3H4CHO-A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {4,S}
2  C u1 p0 c0 {1,S} {6,S} {7,S}
3  C u0 p0 c0 {1,D} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {5,D} {10,S}
5  O u0 p2 c0 {4,D}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.764345,0.0445242,-3.61034e-05,1.48295e-08,-2.43809e-12,2447.33,20.8542], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[14.1737,0.0109162,-3.69021e-06,5.69228e-10,-3.29023e-14,-1928.68,-50.2664], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 218,
    label = "IC4H8O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.02574,0.0751341,-6.88669e-05,3.12223e-08,-5.60129e-12,-30748.1,29.6284], Tmin=(300,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[14.0434,0.0205734,-9.09519e-06,1.73417e-09,-1.14909e-13,-36227.5,-69.001], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 219,
    label = "TC3H6O2CHO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,D} {13,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
14 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.17883,0.0541596,-3.83436e-05,1.38308e-08,-2.0419e-12,-22739.4,20.0751], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[18.5534,0.0168774,-5.90753e-06,9.31518e-10,-5.46345e-14,-28544.7,-68.2487], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 220,
    label = "IC3H5O2HCHO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {10,D} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.05985,0.0582332,-4.37672e-05,1.6325e-08,-2.43462e-12,-16349.6,21.3688], Tmin=(300,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[20.6289,0.0148626,-5.25305e-06,8.33773e-10,-4.91277e-14,-22758.9,-78.2963], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 221,
    label = "TC3H6O2HCO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {6,S}
5  C u1 p0 c0 {1,S} {13,D}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {5,D}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.03864,0.0580421,-4.32124e-05,1.58792e-08,-2.3221e-12,-22428.5,20.3681], Tmin=(300,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[20.6473,0.0148527,-5.25105e-06,8.33619e-10,-4.91256e-14,-28872,-79.5951], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 222,
    label = "TC3H6OCHO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,D} {13,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.37083,0.0538476,-3.82478e-05,1.32882e-08,-1.79229e-12,-21839.1,25.8142], Tmin=(300,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[17.0371,0.0154401,-5.28333e-06,8.21085e-10,-4.76898e-14,-27587.2,-63.7271], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 223,
    label = "IC4H9O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.7722,0.0534033,-3.31042e-05,9.24466e-09,-8.01707e-13,-11776.9,20.9581], Tmin=(300,'K'), Tmax=(1432,'K')),
            NASAPolynomial(coeffs=[17.8794,0.0182475,-6.01252e-06,9.11107e-10,-5.20019e-14,-17457,-66.1553], Tmin=(1432,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 224,
    label = "TC4H9O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {15,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.63892,0.0544717,-3.75505e-05,1.40479e-08,-2.27969e-12,-14759.9,14.0326], Tmin=(300,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[18.0863,0.0199283,-6.98287e-06,1.10172e-09,-6.46381e-14,-20442.1,-69.7533], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 225,
    label = "IC4H8O2H-I",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.186433,0.062643,-4.83691e-05,1.88657e-08,-2.91189e-12,-3590.87,29.7635], Tmin=(300,'K'), Tmax=(1414,'K')),
            NASAPolynomial(coeffs=[18.3915,0.0173043,-5.66841e-06,8.55414e-10,-4.86782e-14,-9485.7,-66.7673], Tmin=(1414,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 226,
    label = "IC4H8O2H-T",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84375,0.0436801,-2.076e-05,2.51709e-09,5.41307e-13,-6507.66,13.4245], Tmin=(300,'K'), Tmax=(1413,'K')),
            NASAPolynomial(coeffs=[16.9754,0.0185198,-6.09075e-06,9.21674e-10,-5.25503e-14,-11481.3,-58.8259], Tmin=(1413,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 227,
    label = "TC4H8O2H-I",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54378,0.0525201,-3.69898e-05,1.44635e-08,-2.47536e-12,-6981.83,12.7624], Tmin=(300,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[18.1415,0.0194699,-6.8275e-06,1.07773e-09,-6.32519e-14,-12357.1,-66.3492], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 228,
    label = "CC4H8O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {2,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.56747,0.0787299,-7.33065e-05,3.40603e-08,-6.15675e-12,-27158.3,38.0876], Tmin=(300,'K'), Tmax=(1431,'K')),
            NASAPolynomial(coeffs=[15.1842,0.0164657,-5.33483e-06,7.9815e-10,-4.5116e-14,-33392.3,-74.3747], Tmin=(1431,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 229,
    label = "IC4H8OOH-IO2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.23355,0.0563089,-3.15673e-05,7.79537e-09,-6.21665e-13,-22278.3,15.2623], Tmin=(300,'K'), Tmax=(1367,'K')),
            NASAPolynomial(coeffs=[22.4665,0.0209351,-7.44324e-06,1.18589e-09,-7.00547e-14,-29449.5,-85.4241], Tmin=(1367,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 230,
    label = "IC4H8OOH-TO2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.36414,0.0693743,-5.70416e-05,2.4604e-08,-4.32849e-12,-25113.8,16.5767], Tmin=(300,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[23.2465,0.0188385,-6.40938e-06,9.92649e-10,-5.75276e-14,-31653.3,-88.8302], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 231,
    label = "TC4H8OOH-IO2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.36414,0.0693743,-5.70416e-05,2.4604e-08,-4.32849e-12,-25113.8,16.5767], Tmin=(300,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[23.2465,0.0188385,-6.40938e-06,9.92649e-10,-5.75276e-14,-31653.3,-88.8302], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 232,
    label = "IC4KETII",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,D} {14,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.15502,0.0610622,-4.49711e-05,1.70515e-08,-2.65949e-12,-38274.8,26.9612], Tmin=(300,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[19.5143,0.0182377,-6.38909e-06,1.00802e-09,-5.9144e-14,-44688.5,-71.7168], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 233,
    label = "IC4KETIT",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.14244,0.0633841,-4.73085e-05,1.77145e-08,-2.67265e-12,-40936.7,23.4845], Tmin=(300,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[20.937,0.0171091,-6.01892e-06,9.52354e-10,-5.59926e-14,-47782,-82.7718], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 234,
    label = "TIC4H7Q2-I",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  O u0 p2 c0 {5,S} {17,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.48426,0.0661225,-5.27349e-05,2.18216e-08,-3.66789e-12,-19890.7,12.672], Tmin=(300,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[23.3849,0.018707,-6.44022e-06,1.00428e-09,-5.84468e-14,-26118.1,-87.661], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 235,
    label = "IIC4H7Q2-I",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {3,S} {8,S}
7  O u0 p2 c0 {5,S} {16,S}
8  O u0 p2 c0 {6,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.93056,0.0605819,-4.23666e-05,1.49122e-08,-2.10979e-12,-16841.5,13.6228], Tmin=(300,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[23.05,0.0192149,-6.66623e-06,1.04496e-09,-6.10371e-14,-23208.7,-83.995], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 236,
    label = "IIC4H7Q2-T",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {5,S} {16,S}
8  O u0 p2 c0 {6,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.16274,0.0434463,-1.76972e-05,4.88791e-10,9.03915e-13,-19650.2,0.262067], Tmin=(300,'K'), Tmax=(1377,'K')),
            NASAPolynomial(coeffs=[21.507,0.020536,-7.12383e-06,1.11655e-09,-6.52112e-14,-25111.8,-74.338], Tmin=(1377,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 237,
    label = "IC4H7OOH",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.131852,0.0619561,-4.99344e-05,2.09628e-08,-3.59718e-12,-12140,29.3906], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[18.2897,0.0167816,-5.80668e-06,9.08949e-10,-5.30513e-14,-18204.7,-67.2111], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 238,
    label = "IC4H9O2H",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.547969,0.0657429,-4.70123e-05,1.65991e-08,-2.27331e-12,-28218,31.2961], Tmin=(300,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[19.1652,0.0193679,-6.41984e-06,9.76948e-10,-5.593e-14,-34879.1,-74.2064], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 239,
    label = "TC4H9O2H",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {16,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.445574,0.0666154,-5.20932e-05,2.22302e-08,-4.0019e-12,-31226.1,23.7278], Tmin=(300,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[19.0927,0.0212698,-7.46253e-06,1.17841e-09,-6.91795e-14,-37727.8,-76.1321], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 240,
    label = "IC4H8",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0572478,0.0417769,-2.49096e-05,7.54294e-09,-9.23202e-13,-3721.66,23.5699], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[11.1444,0.0181609,-6.17791e-06,9.55482e-10,-5.52826e-14,-7840.25,-36.8509], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 241,
    label = "IC4H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u1 p0 c0 {2,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.229579,0.0417843,-2.66886e-05,8.42206e-09,-1.03175e-12,14394.7,25.4798], Tmin=(300,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[11.8999,0.015157,-5.09995e-06,7.83722e-10,-4.5166e-14,10036.4,-40.2287], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 242,
    label = "IC4H7-I1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u1 p0 c0 {3,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.912465,0.0388654,-2.57576e-05,9.0776e-09,-1.33947e-12,25563.6,20.8635], Tmin=(300,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[11.1159,0.0155127,-5.23769e-06,8.05998e-10,-4.64703e-14,21948.8,-34.144], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 243,
    label = "IC4H7O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.43532,0.0489027,-3.63601e-05,1.41906e-08,-2.24558e-12,3092.85,24.132], Tmin=(300,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[14.5792,0.0162136,-5.26957e-06,7.90454e-10,-4.47755e-14,-1208.48,-45.6459], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 244,
    label = "IC4H6OOH-I",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u1 p0 c0 {2,S} {9,S} {10,S}
4  C u0 p0 c0 {2,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.06669,0.039495,-2.52722e-05,7.84486e-09,-8.98877e-13,2874.48,-0.378377], Tmin=(300,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[17.3601,0.0142046,-4.65348e-06,7.0221e-10,-3.99553e-14,-1075.09,-61.2822], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 245,
    label = "CCYCCOOC-T1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.29768,0.0665082,-4.67054e-05,1.5103e-08,-1.74322e-12,3979.36,51.6412], Tmin=(300,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[16.827,0.0164472,-5.63767e-06,8.78002e-10,-5.1096e-14,-3657.11,-67.4097], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 246,
    label = "C2CYCOOC-I1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.04718,0.0726608,-6.8296e-05,3.27506e-08,-6.23802e-12,-371.476,19.2056], Tmin=(300,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[18.9745,0.0150114,-5.30728e-06,8.42455e-10,-4.96393e-14,-6931.11,-90.8581], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 247,
    label = "CCYCCOOC-I2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {6,S} {13,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {4,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.55773,0.0710221,-6.05228e-05,2.61774e-08,-4.51391e-12,13292.2,46.0829], Tmin=(300,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[16.3389,0.0165879,-5.61829e-06,8.67331e-10,-5.01477e-14,6669.47,-64.0322], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 248,
    label = "IC3H5OOCH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {10,S} {11,S}
4  C u1 p0 c0 {6,S} {12,S} {13,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {4,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.26548,-0.00361338,7.31804e-05,-5.49846e-08,1.20447e-11,13310.9,53.3429], Tmin=(300,'K'), Tmax=(1410,'K')),
            NASAPolynomial(coeffs=[5.05336,0.0362904,-1.54013e-05,2.74342e-09,-1.74719e-13,4083.26,-2.5539], Tmin=(1410,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 249,
    label = "CHOIC3H6O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,D} {13,S}
5  H u0 p0 c0 {1,S}
6  O u1 p2 c0 {3,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.255559,0.0522086,-3.72284e-05,1.36714e-08,-2.05639e-12,-19728.5,29.921], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[15.5512,0.016736,-5.73573e-06,8.92095e-10,-5.18352e-14,-25067.4,-52.3216], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 250,
    label = "CVCYCCOC",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.45567,0.0488377,-3.46186e-05,1.26591e-08,-1.88738e-12,-643.461,35.8434], Tmin=(300,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[11.4364,0.0163251,-5.57146e-06,8.63796e-10,-5.00702e-14,-5446.53,-38.7179], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 251,
    label = "CCYC2OCO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {8,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  O u1 p2 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.97381,0.0675615,-5.79902e-05,2.55213e-08,-4.49992e-12,-9936.07,42.5128], Tmin=(300,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[16.4353,0.0165843,-5.71791e-06,8.92587e-10,-5.19865e-14,-16093.8,-59.6946], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 252,
    label = "CCYCCO-T1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 C u1 p0 c0 {1,S} {2,S} {4,S}
4 O u0 p2 c0 {1,S} {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.39311,0.0381789,-2.62316e-05,8.74877e-09,-1.11297e-12,11253.5,34.1877], Tmin=(300,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[10.3395,0.011518,-3.87497e-06,5.95744e-10,-3.4354e-14,7176.59,-28.9688], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 253,
    label = "IC4H7O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u1 p2 c0 {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.74701,0.0407783,-2.4475e-05,7.06503e-09,-7.51571e-13,4869.79,19.4536], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[13.3458,0.0161219,-5.44376e-06,8.38199e-10,-4.83608e-14,611.444,-43.6819], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 254,
    label = "IC3H5OCH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  C u1 p0 c0 {5,S} {11,S} {12,S}
5  O u0 p2 c0 {2,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.14799,0.0700226,-8.21595e-05,5.2259e-08,-1.34177e-11,3264.75,35.5146], Tmin=(298.15,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.64732,0.0308191,-1.73209e-05,5.011e-09,-6.00089e-13,1706.8,-5.91215], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298.15,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 255,
    label = "IC4H7OOCH3",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {2,S} {5,D}
5  C u0 p0 c0 {4,D} {16,S} {17,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {3,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.26784,0.0682442,-5.30808e-05,2.27496e-08,-4.11475e-12,-11676.8,24.4901], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[19.5897,0.0231057,-8.02911e-06,1.2597e-09,-7.36169e-14,-18006.9,-73.4192], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 256,
    label = "IC4H7OOIC4H7",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {4,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {8,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {3,S} {5,S} {9,D}
8  C u0 p0 c0 {4,S} {6,S} {10,D}
9  C u0 p0 c0 {7,D} {21,S} {22,S}
10 C u0 p0 c0 {8,D} {23,S} {24,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.207882,0.104076,-8.33973e-05,3.60898e-08,-6.47907e-12,-7790.63,35.0447], Tmin=(300,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[28.0447,0.0327505,-1.1322e-05,1.77028e-09,-1.03212e-13,-17268.3,-115.135], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 257,
    label = "C4H8-1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.1626,0.0401053,-2.18039e-05,5.47071e-09,-4.54073e-13,-1654.03,24.8169], Tmin=(300,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[11.0189,0.0182714,-6.21802e-06,9.62039e-10,-5.56791e-14,-5809.99,-34.7942], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 258,
    label = "C4H71-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u1 p0 c0 {3,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.73187,0.0350027,-1.85648e-05,2.75749e-09,7.71262e-13,27650.8,17.8656], Tmin=(298.15,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.93165,0.0262974,-1.16478e-05,2.24009e-09,-1.22866e-13,26806.2,1.40496], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298.15,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 259,
    label = "C4H71-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,D} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {3,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.82637,0.03225,-1.22967e-05,-2.55681e-09,2.3621e-12,25973.3,18.3257], Tmin=(298.15,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.57643,0.0264291,-1.13346e-05,1.98119e-09,-6.72515e-14,25164.3,3.76341], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298.15,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 260,
    label = "C4H71-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.279155,0.0380224,-1.87607e-05,5.39087e-10,1.86579e-12,14348,24.1411], Tmin=(298.15,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.46811,0.0274302,-1.2118e-05,2.27424e-09,-1.08909e-13,13202,2.39089], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298.15,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 261,
    label = "C4H71-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.436416,0.0387311,-2.31537e-05,5.31946e-09,2.40685e-13,22970.4,25.8119], Tmin=(298.15,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.56422,0.026712,-1.18633e-05,2.2846e-09,-1.2363e-13,21920.2,4.77459], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298.15,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 262,
    label = "C4H6-1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,T}
4  C u0 p0 c0 {3,T} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.129199,0.0422021,-3.66747e-05,1.86446e-08,-4.10014e-12,18465.3,24.3146], Tmin=(298.15,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.94366,0.0261885,-1.30711e-05,3.18676e-09,-3.05127e-13,17636.9,4.59598], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298.15,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 263,
    label = "SC3H5CHO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {10,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.09373,0.0443315,-3.41918e-05,1.3937e-08,-2.33791e-12,-15674.6,19.4458], Tmin=(300,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[13.3892,0.0139115,-4.75821e-06,7.38737e-10,-4.28607e-14,-19791.7,-46.0146], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 264,
    label = "SC3H5CO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u1 p0 c0 {3,S} {10,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.776401,0.0426828,-3.37881e-05,1.39128e-08,-2.33332e-12,1299.03,19.8102], Tmin=(300,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[12.9926,0.0122141,-4.19305e-06,6.52698e-10,-3.79407e-14,-2747.82,-45.1092], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 265,
    label = "AC3H5OCH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  C u1 p0 c0 {1,S} {11,S} {12,S}
5  O u0 p2 c0 {2,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.20089,0.0424761,-2.94115e-05,1.11825e-08,-1.8131e-12,7267.92,24.3629], Tmin=(300,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[11.988,0.0170264,-5.78617e-06,8.9415e-10,-5.16995e-14,3483.67,-33.5861], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 266,
    label = "C4H7O1-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  O u1 p2 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.44895,0.0369424,-1.77511e-05,2.64538e-09,2.43666e-13,6163.86,17.3175], Tmin=(300,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[13.3251,0.0165058,-5.65236e-06,8.7832e-10,-5.09915e-14,1912.81,-42.8181], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 267,
    label = "C4H7O2-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  O u1 p2 c0 {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.16435,0.0253428,-1.39669e-06,-6.00714e-09,1.76697e-12,5032.11,4.37441], Tmin=(300,'K'), Tmax=(1684,'K')),
            NASAPolynomial(coeffs=[11.2686,0.0201725,-7.41926e-06,1.21276e-09,-7.30115e-14,2138.76,-31.5208], Tmin=(1684,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 268,
    label = "SC3H5OCH2-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {5,S} {10,S}
4  C u1 p0 c0 {5,S} {11,S} {12,S}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.235694,0.0467368,-3.04881e-05,9.75216e-09,-1.23281e-12,7116.68,28.1379], Tmin=(300,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[14.7022,0.0155342,-5.45701e-06,8.62545e-10,-5.06734e-14,1812.95,-50.512], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 269,
    label = "C4H71-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {5,S} {12,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.02223,0.0485578,-3.30294e-05,1.13407e-08,-1.57078e-12,4041.44,20.6107], Tmin=(300,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[16.3739,0.0162685,-5.62192e-06,8.78983e-10,-5.12511e-14,-1063.18,-56.9006], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 270,
    label = "C4H71-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {3,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.4246,0.0520548,-3.89441e-05,1.51726e-08,-2.42612e-12,1688.54,22.3231], Tmin=(300,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[16.3566,0.0161768,-5.5661e-06,8.67701e-10,-5.04886e-14,-3402.45,-57.5261], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 271,
    label = "C4H71-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {2,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.09043,0.045713,-2.94816e-05,9.69605e-09,-1.30061e-12,4889.33,21.5456], Tmin=(300,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[15.024,0.0172861,-5.94297e-06,9.25861e-10,-5.38462e-14,192.461,-48.5941], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 272,
    label = "C4H61-3OOH4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.987401,0.0518591,-3.67576e-05,1.30999e-08,-1.88471e-12,6326.45,25.643], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[16.8745,0.0156489,-5.46062e-06,8.59386e-10,-5.03397e-14,726.846,-59.9892], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 273,
    label = "C4H6O1-3OOH4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {14,S}
7  O u1 p2 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83046,0.0507388,-3.42226e-05,1.13486e-08,-1.48529e-12,-5617.86,15.151], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[19.5456,0.0160359,-5.61769e-06,8.86342e-10,-5.20073e-14,-11267.9,-69.949], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 274,
    label = "C4H6O2-1OOH4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {13,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u1 p2 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.38345,0.044709,-2.4363e-05,5.07835e-09,-1.20806e-13,-3407.11,8.84731], Tmin=(300,'K'), Tmax=(1364,'K')),
            NASAPolynomial(coeffs=[20.5165,0.0155728,-5.54197e-06,8.83593e-10,-5.22242e-14,-9300.31,-74.6631], Tmin=(1364,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 275,
    label = "C4H71-3OOCH3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {7,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {5,D} {15,S}
5  C u0 p0 c0 {4,D} {16,S} {17,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {3,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.542405,0.0751511,-6.00685e-05,2.49701e-08,-4.2232e-12,-11306.1,30.2982], Tmin=(300,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[21.2299,0.0207004,-6.99464e-06,1.07837e-09,-6.23e-14,-18500.6,-85.35], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 276,
    label = "C4H72-1OOCH3",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {5,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {5,D} {17,S}
5  C u0 p0 c0 {2,S} {4,D} {16,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {3,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.44675,0.062143,-4.39326e-05,1.72567e-08,-2.94951e-12,-11143.2,19.4029], Tmin=(300,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[19.2915,0.0234475,-8.16714e-06,1.28338e-09,-7.50838e-14,-17268.9,-71.651], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 277,
    label = "C4H8-2",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.30796,0.0353137,-1.51866e-05,1.64112e-09,3.44258e-13,-3197.68,18.1595], Tmin=(300,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[10.8652,0.0184123,-6.26887e-06,9.70206e-10,-5.61639e-14,-7096.26,-35.1547], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 278,
    label = "C4H72-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u1 p0 c0 {2,S} {3,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87261,0.0194663,1.17651e-05,-2.15467e-08,7.83625e-12,24611.4,9.12813], Tmin=(298.15,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.37426,0.0257363,-1.00547e-05,1.2764e-09,6.13336e-14,24097.3,4.63882], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298.15,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 279,
    label = "C4H72-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  O u0 p2 c0 {3,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.49537,0.0475681,-3.26453e-05,1.1407e-08,-1.61495e-12,176.384,16.7027], Tmin=(300,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[16.3301,0.0160699,-5.50238e-06,8.55099e-10,-4.96517e-14,-4700.4,-57.8736], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 280,
    label = "SC4H8OH-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.78283,0.0518872,-3.89601e-05,1.57819e-08,-2.64134e-12,-12830.5,20.0308], Tmin=(300,'K'), Tmax=(1405,'K')),
            NASAPolynomial(coeffs=[15.0517,0.0184749,-6.15328e-06,9.38017e-10,-5.37214e-14,-17197.4,-50.3734], Tmin=(1405,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 281,
    label = "SC4H8OH-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {5,S}
5  O u0 p2 c0 {4,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.96361,0.0477674,-3.11652e-05,1.07499e-08,-1.54834e-12,-16500,19.7287], Tmin=(300,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[14.5515,0.0192722,-6.50955e-06,1.002e-09,-5.77831e-14,-20991,-48.2454], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 282,
    label = "SC4H8OH-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.93186,0.0479506,-3.23719e-05,1.16233e-08,-1.72499e-12,-13943.1,20.3995], Tmin=(300,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[14.2454,0.0189491,-6.27404e-06,9.52693e-10,-5.44158e-14,-18180.4,-45.6206], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 283,
    label = "SC4H8OH-1O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {16,S}
6  O u0 p2 c0 {3,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {6,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.47038,0.0638295,-4.92334e-05,1.99705e-08,-3.30499e-12,-30860.2,26.3463], Tmin=(300,'K'), Tmax=(1405,'K')),
            NASAPolynomial(coeffs=[18.8547,0.0202218,-6.82329e-06,1.04962e-09,-6.05033e-14,-36572.1,-65.9105], Tmin=(1405,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 284,
    label = "SC4H8OH-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {16,S}
6  O u0 p2 c0 {2,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {6,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.78918,0.0662988,-5.52281e-05,2.40248e-08,-4.18762e-12,-33042.8,22.8886], Tmin=(300,'K'), Tmax=(1417,'K')),
            NASAPolynomial(coeffs=[19.3083,0.0192157,-6.34251e-06,9.60913e-10,-5.4794e-14,-38437.1,-68.8888], Tmin=(1417,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 285,
    label = "PQC4H8OS",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {6,S}
6  O u0 p2 c0 {5,S} {16,S}
7  O u1 p2 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.6898,0.0610664,-4.46911e-05,1.68939e-08,-2.59692e-12,-21246.1,19.4272], Tmin=(300,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[19.9994,0.0196391,-6.70756e-06,1.04036e-09,-6.03188e-14,-27125.8,-73.1285], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 286,
    label = "PQC4H7OHS-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14059,0.0594343,-4.55415e-05,1.85507e-08,-3.10109e-12,-24076.5,19.9412], Tmin=(300,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[18.9704,0.0196512,-6.61523e-06,1.01591e-09,-5.8489e-14,-29287.6,-64.0683], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 287,
    label = "SQC4H7OHS-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37953,0.0650949,-5.5911e-05,2.49644e-08,-4.44897e-12,-25150.2,15.8597], Tmin=(300,'K'), Tmax=(1414,'K')),
            NASAPolynomial(coeffs=[20.6664,0.0178772,-5.93194e-06,9.02006e-10,-5.15692e-14,-30413.2,-74.4595], Tmin=(1414,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 288,
    label = "SQC4H8OS",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {16,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45579,0.061042,-4.64107e-05,1.80687e-08,-2.81124e-12,-23483.6,13.9992], Tmin=(300,'K'), Tmax=(1424,'K')),
            NASAPolynomial(coeffs=[20.5364,0.0185262,-6.18258e-06,9.44045e-10,-5.4139e-14,-29045.4,-76.6224], Tmin=(1424,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 289,
    label = "NC4KET12OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,D} {13,S}
5  O u0 p2 c0 {2,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.52027,0.0540317,-3.57074e-05,1.18022e-08,-1.57486e-12,-46778.1,28.9999], Tmin=(300,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[16.8651,0.0183319,-6.4139e-06,1.01105e-09,-5.92859e-14,-52735.3,-59.7188], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 290,
    label = "NC4KET23OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {13,D}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.64761,0.0474122,-2.72509e-05,7.25756e-09,-6.68683e-13,-50494.6,23.78], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[15.4636,0.019212,-6.64681e-06,1.03989e-09,-6.06553e-14,-55729.3,-51.9147], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 291,
    label = "CH3COCOHCH3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  O u0 p2 c0 {3,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 O u1 p2 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.65608,0.060841,-4.85215e-05,1.97794e-08,-3.26305e-12,-30515.8,35.8912], Tmin=(300,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[16.5625,0.0159037,-5.54554e-06,8.72275e-10,-5.10735e-14,-36588.5,-61.0834], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 292,
    label = "CH3COHCO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 O u0 p2 c0 {2,S} {9,S}
4 C u0 p0 c0 {2,D} {8,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 O u0 p2 c0 {4,D}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.825855,0.0522217,-5.66992e-05,2.94816e-08,-5.81715e-12,-35015.7,17.8489], Tmin=(300,'K'), Tmax=(1410,'K')),
            NASAPolynomial(coeffs=[15.0111,0.00726697,-2.42872e-06,3.71247e-10,-2.13069e-14,-38735.5,-54.1006], Tmin=(1410,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 293,
    label = "CH2COHCHO",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {5,D} {8,S}
4 O u0 p2 c0 {1,S} {9,S}
5 O u0 p2 c0 {3,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.057664,0.051659,-5.49774e-05,2.83487e-08,-5.57464e-12,-33959.5,22.9757], Tmin=(300,'K'), Tmax=(1406,'K')),
            NASAPolynomial(coeffs=[14.02,0.00795093,-2.63245e-06,3.99896e-10,-2.28538e-14,-37680.8,-48.0458], Tmin=(1406,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 294,
    label = "C4H71-3OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0716708,0.0504773,-3.50357e-05,1.30539e-08,-2.07783e-12,-21698.4,28.2073], Tmin=(300,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[14.2402,0.0183039,-6.37213e-06,1.001e-09,-5.85511e-14,-26818.4,-48.395], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 295,
    label = "C4H72-2OH",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  O u0 p2 c0 {3,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.184034,0.0590105,-5.22507e-05,2.44136e-08,-4.56519e-12,-26671.8,23.6075], Tmin=(300,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[14.9412,0.016629,-5.55628e-06,8.48899e-10,-4.86949e-14,-31249.7,-55.1731], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 296,
    label = "C4H63,1-3OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u1 p0 c0 {3,S} {10,S} {11,S}
5  O u0 p2 c0 {2,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.596155,0.0435893,-2.65985e-05,8.1425e-09,-1.02316e-12,-5056.31,24.3924], Tmin=(300,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[13.3633,0.0170223,-5.95245e-06,9.37896e-10,-5.49767e-14,-9901.13,-45.4753], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 297,
    label = "CCY(COCC)OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {2,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.13261,0.0775376,-6.73066e-05,2.82842e-08,-4.6547e-12,-35782.5,55.3089], Tmin=(300,'K'), Tmax=(1328,'K')),
            NASAPolynomial(coeffs=[10.3817,0.0253053,-1.00512e-05,1.68205e-09,-9.58093e-14,-39434.9,-27.3523], Tmin=(1328,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 298,
    label = "SQC4H7OHS-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {10,S}
3  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {2,S} {17,S}
7  O u0 p2 c0 {3,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.90987,0.0776596,-6.68514e-05,2.93628e-08,-5.12008e-12,-43155.2,22.9131], Tmin=(300,'K'), Tmax=(1414,'K')),
            NASAPolynomial(coeffs=[24.6608,0.0192948,-6.45434e-06,9.87246e-10,-5.6689e-14,-49846.7,-91.0425], Tmin=(1414,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 299,
    label = "C4H7O2-1,3OOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {8,S}
7  O u0 p2 c0 {5,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {1,S}
10 O u1 p2 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.88339,0.0718219,-5.86792e-05,2.42824e-08,-3.98539e-12,-33657.6,12.4696], Tmin=(300,'K'), Tmax=(1425,'K')),
            NASAPolynomial(coeffs=[25.4691,0.0186441,-6.23826e-06,9.54423e-10,-5.48154e-14,-40153.2,-96.039], Tmin=(1425,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 300,
    label = "NC4KET13OH-2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.13332,0.0669841,-5.19672e-05,2.03864e-08,-3.22075e-12,-59096.3,24.0965], Tmin=(300,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[22.5434,0.0176377,-6.14926e-06,9.67201e-10,-5.66322e-14,-65972.4,-84.8523], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 301,
    label = "C4H6OHOOH1-2-3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {14,S}
7  O u0 p2 c0 {5,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.88476,0.0916099,-9.37152e-05,4.66407e-08,-8.92736e-12,-35290,39.2852], Tmin=(300,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[23.2793,0.0138281,-4.61331e-06,7.0532e-10,-4.05175e-14,-42634.8,-95.198], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 302,
    label = "SC2H2OH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u1 p0 c0 {1,D} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.63792,0.0264969,-2.74821e-05,1.43111e-08,-2.85795e-12,11146.7,15.8715], Tmin=(300,'K'), Tmax=(1410,'K')),
            NASAPolynomial(coeffs=[7.99235,0.00583109,-1.89243e-06,2.83129e-10,-1.59933e-14,9512.37,-16.2058], Tmin=(1410,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 303,
    label = "CH2COHCO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 O u0 p2 c0 {1,S} {8,S}
4 C u1 p0 c0 {1,S} {7,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 O u0 p2 c0 {4,D}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.24341,0.0471485,-5.442e-05,2.9597e-08,-6.01447e-12,-16555.5,16.8301], Tmin=(300,'K'), Tmax=(1411,'K')),
            NASAPolynomial(coeffs=[13.1285,0.00617949,-1.93388e-06,2.81893e-10,-1.56244e-14,-19350.8,-42.2958], Tmin=(1411,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 304,
    label = "PC4H8OH-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {5,S} {13,S}
5  O u0 p2 c0 {4,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.772567,0.0500429,-3.20164e-05,1.02913e-08,-1.30709e-12,-13842.2,25.8928], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[14.7813,0.0189693,-6.38671e-06,9.81341e-10,-5.65332e-14,-18848.7,-49.8892], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 305,
    label = "PC4H8OH-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u1 p0 c0 {1,S} {2,S} {13,S}
5  O u0 p2 c0 {2,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.89477,0.0487803,-3.26703e-05,1.1712e-08,-1.771e-12,-10745.5,20.6226], Tmin=(300,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[14.7199,0.0193692,-6.59357e-06,1.02019e-09,-5.90411e-14,-15302.3,-48.5296], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 306,
    label = "PC4H8OH-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  O u0 p2 c0 {2,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.21685,0.047134,-3.04255e-05,1.03165e-08,-1.45044e-12,-10820.9,18.3498], Tmin=(300,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[14.5945,0.0192223,-6.48869e-06,9.98309e-10,-5.75489e-14,-15239.3,-48.5128], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 307,
    label = "PC4H8OH-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0695635,0.0520263,-3.44849e-05,1.17704e-08,-1.63047e-12,-10605.4,31.591], Tmin=(300,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[14.152,0.019644,-6.64538e-06,1.02403e-09,-5.91002e-14,-15614.1,-45.0604], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 308,
    label = "PC4H8OH-2O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {15,S}
6  O u0 p2 c0 {3,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.97781,0.0625692,-4.7673e-05,1.90562e-08,-3.10597e-12,-30962.5,23.588], Tmin=(300,'K'), Tmax=(1407,'K')),
            NASAPolynomial(coeffs=[19.0514,0.0200624,-6.7697e-06,1.04137e-09,-6.00272e-14,-36596.7,-67.1202], Tmin=(1407,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 309,
    label = "SQC4H8OP",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u1 p2 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92966,0.0567741,-3.88078e-05,1.31554e-08,-1.72823e-12,-21464.9,13.2313], Tmin=(300,'K'), Tmax=(1421,'K')),
            NASAPolynomial(coeffs=[20.2482,0.0190403,-6.41819e-06,9.86792e-10,-5.68666e-14,-27068.6,-74.3735], Tmin=(1421,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 310,
    label = "SQC4H7OHP-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.44518,0.0652944,-5.1038e-05,2.05239e-08,-3.32051e-12,-22906,27.8546], Tmin=(300,'K'), Tmax=(1410,'K')),
            NASAPolynomial(coeffs=[19.9207,0.0189423,-6.39488e-06,9.84231e-10,-5.67606e-14,-28925.1,-70.1061], Tmin=(1410,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 311,
    label = "CY(CCCO)COH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {4,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.9759,0.0798393,-7.11132e-05,3.16612e-08,-5.61324e-12,-33577.8,61.2093], Tmin=(300,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[13.4636,0.0228746,-9.9362e-06,1.89605e-09,-1.26467e-13,-39639.7,-45.1064], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 312,
    label = "NC4KET21OH",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {2,S} {13,D}
5  O u0 p2 c0 {2,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.46677,0.030112,-2.59549e-06,-7.61701e-09,2.55573e-12,-48990.9,6.33308], Tmin=(300,'K'), Tmax=(1507,'K')),
            NASAPolynomial(coeffs=[15.2253,0.0186615,-6.30659e-06,9.72356e-10,-5.6177e-14,-53476,-50.0397], Tmin=(1507,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 313,
    label = "C2H5CHOHCO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {5,S} {11,S}
4  C u0 p0 c0 {5,S} {12,D} {13,S}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.44749,0.0646308,-5.10458e-05,1.99851e-08,-3.12214e-12,-26667,39.5567], Tmin=(300,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[18.2917,0.0148007,-5.24975e-06,8.3522e-10,-4.92942e-14,-33670.4,-71.2364], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 314,
    label = "C2H4COCH2OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u1 p2 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.98874,0.0141152,1.863e-05,-1.99223e-08,5.12984e-12,-29870.6,-1.87192], Tmin=(300,'K'), Tmax=(1462,'K')),
            NASAPolynomial(coeffs=[14.0828,0.0176833,-6.09759e-06,9.52795e-10,-5.55572e-14,-33751.8,-40.8944], Tmin=(1462,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 315,
    label = "CH3COCHO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 C u0 p0 c0 {2,S} {8,D} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 O u0 p2 c0 {3,D}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.08731,0.0309032,-1.98794e-05,6.26175e-09,-7.69946e-13,-34398.9,18.284], Tmin=(300,'K'), Tmax=(1381,'K')),
            NASAPolynomial(coeffs=[11.4371,0.0106774,-3.68968e-06,5.77007e-10,-3.36532e-14,-37807.9,-32.5054], Tmin=(1381,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 316,
    label = "C4H71-1OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {5,S} {12,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.465981,0.0556573,-4.50578e-05,1.93726e-08,-3.38968e-12,-23100.8,27.9745], Tmin=(300,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[14.2587,0.0171933,-5.74956e-06,8.7909e-10,-5.04586e-14,-27805.1,-49.6582], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 317,
    label = "C4H71-4OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {2,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.212276,0.0486358,-3.17242e-05,1.04987e-08,-1.39007e-12,-20036.5,30.4092], Tmin=(300,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[13.3437,0.0182064,-6.15151e-06,9.47319e-10,-5.46543e-14,-24847.9,-42.7999], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 318,
    label = "C4H72-1OH",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {12,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.94638,0.0345853,-1.10025e-05,-1.33281e-09,9.54964e-13,-21224.2,15.5037], Tmin=(300,'K'), Tmax=(1367,'K')),
            NASAPolynomial(coeffs=[13.2893,0.0193844,-6.80733e-06,1.0756e-09,-6.31699e-14,-25862.8,-43.4782], Tmin=(1367,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 319,
    label = "C4H71-2OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {3,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.28561,0.0635758,-5.85328e-05,2.80453e-08,-5.32187e-12,-25153.9,29.3803], Tmin=(300,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[15.0658,0.0165276,-5.52198e-06,8.43592e-10,-4.83871e-14,-29973.8,-55.3405], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 320,
    label = "C4H63,1-2OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,D} {4,S} {5,S}
3  C u0 p0 c0 {1,S} {2,D} {9,S}
4  C u1 p0 c0 {2,S} {10,S} {11,S}
5  O u0 p2 c0 {2,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.58904,0.0617723,-5.78264e-05,2.7809e-08,-5.2678e-12,-8179.77,29.6999], Tmin=(300,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[14.69,0.0148008,-4.94484e-06,7.55543e-10,-4.33462e-14,-12944.8,-54.5653], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 321,
    label = "C4H64,2-1OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.757728,0.0498662,-3.52717e-05,1.24304e-08,-1.72238e-12,-1883.79,32.4006], Tmin=(300,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[14.1573,0.0151593,-5.06195e-06,7.74219e-10,-4.44825e-14,-6994.11,-47.6128], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 322,
    label = "C4H63,1-1OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {5,S} {11,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.596641,0.0531885,-4.34792e-05,1.86514e-08,-3.23781e-12,-6155.44,27.4734], Tmin=(300,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[13.8675,0.0154796,-5.1772e-06,7.91828e-10,-4.54657e-14,-10765.5,-48.7821], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 323,
    label = "C4H5OH-13",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {5,S} {8,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  O u0 p2 c0 {3,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.60023,0.0612386,-6.18934e-05,3.14927e-08,-6.20397e-12,-9774.35,30.8328], Tmin=(300,'K'), Tmax=(1405,'K')),
            NASAPolynomial(coeffs=[14.0975,0.0129827,-4.36357e-06,6.6926e-10,-3.8492e-14,-14109.9,-49.4341], Tmin=(1405,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 324,
    label = "SQC4H7OHP-4O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {4,S} {16,S}
7  O u0 p2 c0 {3,S} {17,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.62618,0.0726813,-5.64957e-05,2.25892e-08,-3.65247e-12,-40900,26.5615], Tmin=(300,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[23.5936,0.0208588,-7.13602e-06,1.10821e-09,-6.43133e-14,-47845.2,-84.9506], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 325,
    label = "PQC4H7OHS-3O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {8,S}
6  O u0 p2 c0 {2,S} {16,S}
7  O u0 p2 c0 {1,S} {17,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.90987,0.0776596,-6.68514e-05,2.93628e-08,-5.12008e-12,-43155.2,22.9131], Tmin=(300,'K'), Tmax=(1414,'K')),
            NASAPolynomial(coeffs=[24.6608,0.0192948,-6.45434e-06,9.87246e-10,-5.6689e-14,-49846.7,-91.0425], Tmin=(1414,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 326,
    label = "NC4KET24OH-1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {3,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.17383,0.0372831,-7.3e-06,-5.42424e-09,1.94299e-12,-59147,3.98041], Tmin=(300,'K'), Tmax=(1672,'K')),
            NASAPolynomial(coeffs=[17.664,0.0238922,-8.87612e-06,1.46065e-09,-8.83477e-14,-63656.1,-56.0405], Tmin=(1672,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 327,
    label = "NC4KET24OH-3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.6098,0.061153,-4.50409e-05,1.73313e-08,-2.75574e-12,-60770.8,24.4892], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[20.2237,0.0194541,-6.73928e-06,1.05529e-09,-6.15931e-14,-66865.1,-69.9677], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 328,
    label = "C4H6OHOOH1-4-3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {14,S}
7  O u0 p2 c0 {5,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.90016,0.0772727,-6.79668e-05,2.98158e-08,-5.16343e-12,-30165,40.681], Tmin=(300,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[21.5164,0.0155812,-5.2757e-06,8.14811e-10,-4.71425e-14,-37482.6,-82.4101], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 329,
    label = "C4H6OHOOH2-2-1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {2,S} {3,D} {13,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {14,S}
7  O u0 p2 c0 {5,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0472577,0.0785787,-7.68006e-05,3.79206e-08,-7.33204e-12,-35114,28.0065], Tmin=(300,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[21.6656,0.0159965,-5.52215e-06,8.6274e-10,-5.02768e-14,-41487.5,-83.9378], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 330,
    label = "HOCH2COCH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  O u1 p2 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.98635,0.0251767,-1.10893e-05,1.12011e-09,2.89491e-13,-24004.8,6.38259], Tmin=(300,'K'), Tmax=(1363,'K')),
            NASAPolynomial(coeffs=[12.7107,0.0115514,-3.95952e-06,6.16237e-10,-3.58328e-14,-27153.8,-36.7129], Tmin=(1363,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 331,
    label = "HOCH2CHO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.35084,0.0150413,-5.95083e-07,-3.75736e-09,1.09354e-12,-39165.5,8.0961], Tmin=(300,'K'), Tmax=(1680,'K')),
            NASAPolynomial(coeffs=[7.99599,0.0120664,-4.43693e-06,7.25167e-10,-4.36535e-14,-40902.1,-13.3754], Tmin=(1680,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 332,
    label = "HOCH2CO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {7,S}
3 C u1 p0 c0 {1,S} {6,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {3,D}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.12917,0.00907173,6.49228e-06,-8.56592e-09,2.31071e-12,-20615.2,5.73008], Tmin=(300,'K'), Tmax=(1487,'K')),
            NASAPolynomial(coeffs=[9.43497,0.00768897,-2.74959e-06,4.39772e-10,-2.60488e-14,-22970,-20.4619], Tmin=(1487,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 333,
    label = "HOCHCHO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {5,D} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.542856,0.0295296,-2.08315e-05,6.72777e-09,-8.06116e-13,-18937.8,23.1681], Tmin=(300,'K'), Tmax=(1680,'K')),
            NASAPolynomial(coeffs=[9.99252,0.00777561,-2.94239e-06,4.90136e-10,-2.9898e-14,-22044.1,-27.3957], Tmin=(1680,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 334,
    label = "CH3COCHOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  O u0 p2 c0 {3,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.11184,0.0332521,-1.96834e-05,5.40737e-09,-5.32451e-13,-25854.5,17.7643], Tmin=(300,'K'), Tmax=(1378,'K')),
            NASAPolynomial(coeffs=[12.3885,0.01231,-4.32264e-06,6.83044e-10,-4.01193e-14,-29760.9,-38.5683], Tmin=(1378,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 335,
    label = "IC4H8OH-TI",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33169,0.0513017,-4.02699e-05,1.7515e-08,-3.16002e-12,-14831.9,15.5368], Tmin=(300,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[14.6324,0.0188896,-6.30561e-06,9.62474e-10,-5.5164e-14,-18797.6,-49.3219], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 336,
    label = "TQJC4H8OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {15,S}
6  O u0 p2 c0 {2,S} {16,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.64342,0.0849132,-8.17211e-05,3.9098e-08,-7.27093e-12,-34237.6,28.4394], Tmin=(300,'K'), Tmax=(1415,'K')),
            NASAPolynomial(coeffs=[22.9682,0.0165163,-5.50247e-06,8.39335e-10,-4.81031e-14,-41005.1,-93.4898], Tmin=(1415,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 337,
    label = "TQC4H7OHI",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {6,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {4,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.55844,0.0637086,-4.9717e-05,1.99225e-08,-3.21373e-12,-27752.7,19.5001], Tmin=(300,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[20.8281,0.0181675,-6.12943e-06,9.43194e-10,-5.43937e-14,-33738.7,-77.4824], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 338,
    label = "IQJC4H8OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {16,S}
6  O u0 p2 c0 {2,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {6,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.81449,0.0747453,-7.10895e-05,3.44974e-08,-6.54647e-12,-34402.4,17.738], Tmin=(300,'K'), Tmax=(1410,'K')),
            NASAPolynomial(coeffs=[21.1752,0.0175144,-5.73227e-06,8.63387e-10,-4.90282e-14,-39888.2,-81.9187], Tmin=(1410,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 339,
    label = "TQC4H8OI",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {16,S}
7  O u1 p2 c0 {4,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0745748,0.07465,-6.42255e-05,2.80909e-08,-4.87692e-12,-24718.3,29.4512], Tmin=(300,'K'), Tmax=(1411,'K')),
            NASAPolynomial(coeffs=[21.3201,0.018049,-6.06124e-06,9.29741e-10,-5.34977e-14,-31296.7,-82.0047], Tmin=(1411,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 340,
    label = "QC4H7OHP",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.27864,0.0894493,-8.78565e-05,4.22111e-08,-7.83451e-12,-25897.5,35.3964], Tmin=(300,'K'), Tmax=(1416,'K')),
            NASAPolynomial(coeffs=[24.3481,0.0150316,-5.01788e-06,7.66774e-10,-4.40093e-14,-33192.2,-96.8211], Tmin=(1416,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 341,
    label = "IQC4H8OT",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {16,S}
7  O u1 p2 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72212,0.0642865,-5.52809e-05,2.50037e-08,-4.53472e-12,-24311.1,12.1981], Tmin=(300,'K'), Tmax=(1405,'K')),
            NASAPolynomial(coeffs=[20.4824,0.0182967,-6.04413e-06,9.16381e-10,-5.22867e-14,-29428.7,-75.3563], Tmin=(1405,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 342,
    label = "IQC4H7OHT",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.589,0.0725591,-7.1408e-05,3.55251e-08,-6.84992e-12,-25724.1,12.3767], Tmin=(300,'K'), Tmax=(1413,'K')),
            NASAPolynomial(coeffs=[21.9946,0.0162011,-5.23758e-06,7.81898e-10,-4.41126e-14,-30738.4,-81.6614], Tmin=(1413,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 343,
    label = "IC4H7OH",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.04124,0.0414387,-2.55229e-05,8.28133e-09,-1.10654e-12,-22271,18.8699], Tmin=(300,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[12.3304,0.0183885,-6.06722e-06,9.19055e-10,-5.24036e-14,-25945.2,-36.7418], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 344,
    label = "IC4H8OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29613,0.034765,-1.02506e-05,-2.04642e-09,1.18879e-12,-14562.7,15.8606], Tmin=(300,'K'), Tmax=(1376,'K')),
            NASAPolynomial(coeffs=[12.5606,0.0210637,-7.1502e-06,1.10439e-09,-6.38429e-14,-18620.3,-36.7889], Tmin=(1376,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 345,
    label = "CCY(CCOC)OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {2,S} {3,S}
6  O u0 p2 c0 {1,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.84915,0.0623737,-4.70327e-05,1.84908e-08,-2.94976e-12,-37425.7,38.3164], Tmin=(300,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[14.3405,0.0198312,-6.60658e-06,1.0078e-09,-5.77614e-14,-43095.9,-53.0535], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 346,
    label = "CCY(CCO)COH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {3,S} {14,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.10049,0.0953372,-9.78702e-05,4.90006e-08,-9.41686e-12,-39898.7,56.0925], Tmin=(300,'K'), Tmax=(1412,'K')),
            NASAPolynomial(coeffs=[19.1885,0.0156256,-5.2257e-06,7.99171e-10,-4.58832e-14,-47112,-78.4579], Tmin=(1412,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 347,
    label = "C2CY(COC)OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {2,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.592324,0.0552429,-4.02419e-05,1.57152e-08,-2.57388e-12,-35824.1,22.3378], Tmin=(300,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[15.683,0.0192911,-6.63718e-06,1.03441e-09,-6.01715e-14,-41059.8,-58.5686], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 348,
    label = "IC3H6OHCHO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,D} {13,S}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.84081,0.0529601,-3.94262e-05,1.59063e-08,-2.69565e-12,-50143.7,17.5483], Tmin=(300,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[16.0254,0.0185402,-6.36974e-06,9.91733e-10,-5.76473e-14,-55019.9,-58.3075], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 349,
    label = "CH2COHCH2OOH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {6,S}
5  O u0 p2 c0 {2,S} {11,S}
6  O u0 p2 c0 {4,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.389823,0.0701531,-7.42037e-05,3.84181e-08,-7.63556e-12,-30788,28.6874], Tmin=(300,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[18.7971,0.0112783,-3.90789e-06,6.12065e-10,-3.57305e-14,-36115.5,-69.4914], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 350,
    label = "TQC4H7OHIO2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {2,S} {17,S}
7  O u0 p2 c0 {2,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.17336,0.0794006,-6.51166e-05,2.62036e-08,-4.13406e-12,-48494.3,17.7867], Tmin=(300,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[28.2565,0.016697,-5.67315e-06,8.7835e-10,-5.0909e-14,-56601.7,-115.148], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 351,
    label = "TQC4H7OHTO2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {8,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {2,S} {17,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.17336,0.0794006,-6.51166e-05,2.62036e-08,-4.13406e-12,-48494.3,17.7867], Tmin=(300,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[28.2565,0.016697,-5.67315e-06,8.7835e-10,-5.0909e-14,-56601.7,-115.148], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 352,
    label = "TQC4H7OHIQ-I",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {5,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  O u1 p2 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.09882,0.0693745,-5.12049e-05,1.81276e-08,-2.4633e-12,-39139.4,2.93863], Tmin=(300,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[28.8467,0.016629,-5.74302e-06,8.98791e-10,-5.24795e-14,-46924.9,-119.118], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 353,
    label = "TQC4H7OHIQ-P",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {2,S} {9,S}
7  O u0 p2 c0 {2,S} {16,S}
8  O u0 p2 c0 {5,S} {17,S}
9  O u0 p2 c0 {6,S} {18,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.36948,0.0796855,-6.74366e-05,2.82233e-08,-4.65271e-12,-40556.8,19.2726], Tmin=(300,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[28.1439,0.0163525,-5.54998e-06,8.58604e-10,-4.97359e-14,-48450.3,-111.573], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 354,
    label = "IQC4H7OHTO2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {8,S}
6  O u0 p2 c0 {1,S} {17,S}
7  O u0 p2 c0 {3,S} {16,S}
8  O u0 p2 c0 {5,S} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83287,0.0690926,-5.15031e-05,1.99236e-08,-3.17457e-12,-43444.3,19.4649], Tmin=(300,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[24.172,0.0209397,-7.29061e-06,1.14554e-09,-6.70218e-14,-50477.2,-89.5997], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 355,
    label = "IQC4H8OTQ-I",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {3,S} {8,S}
7  O u0 p2 c0 {5,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  O u1 p2 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.9022,0.0626952,-4.17352e-05,1.35422e-08,-1.7117e-12,-33962,7.8929], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[25.3249,0.0200635,-7.0125e-06,1.10475e-09,-6.47562e-14,-40961.1,-97.3593], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 356,
    label = "IQC4H7OHTQ-P",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {8,S}
6  O u0 p2 c0 {3,S} {9,S}
7  O u0 p2 c0 {1,S} {16,S}
8  O u0 p2 c0 {5,S} {17,S}
9  O u0 p2 c0 {6,S} {18,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45243,0.0714541,-5.54617e-05,2.22755e-08,-3.66067e-12,-35413.3,22.3024], Tmin=(300,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[24.577,0.0201889,-7.03585e-06,1.10623e-09,-6.47523e-14,-42578.3,-90.5053], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 357,
    label = "CH2CQCOHQ",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {7,S}
5  O u0 p2 c0 {2,S} {8,S}
6  O u0 p2 c0 {1,S} {12,S}
7  O u0 p2 c0 {4,S} {14,S}
8  O u0 p2 c0 {5,S} {13,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-16.1172,0.178866,-0.000216751,1.1545e-07,-2.27163e-11,-52116.5,114.441], Tmin=(300,'K'), Tmax=(1418,'K')),
            NASAPolynomial(coeffs=[38.6574,0.000483815,-2.10414e-07,3.81491e-11,-2.46188e-15,-65639.2,-161.084], Tmin=(1418,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 358,
    label = "IC3H5COHQ",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {1,S} {14,S}
7  O u0 p2 c0 {5,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.64361,0.0572485,-3.95908e-05,1.27776e-08,-1.47241e-12,-38010,17.7322], Tmin=(300,'K'), Tmax=(1504,'K')),
            NASAPolynomial(coeffs=[20.7388,0.0158361,-5.27614e-06,8.05932e-10,-4.62682e-14,-44182.1,-79.424], Tmin=(1504,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 359,
    label = "IC3H5Q",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.32903,0.0449171,-3.51235e-05,1.41982e-08,-2.33335e-12,-12189.8,20.2697], Tmin=(300,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[14.3424,0.0128054,-4.40585e-06,6.86848e-10,-3.99675e-14,-16526.1,-48.9935], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 360,
    label = "COHQCYC(COC)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {2,S} {15,S}
8  O u0 p2 c0 {6,S} {16,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.40688,0.059518,-3.16914e-05,4.23695e-09,8.42033e-13,-51969.5,18.8941], Tmin=(300,'K'), Tmax=(1319,'K')),
            NASAPolynomial(coeffs=[24.4599,0.0164188,-5.74024e-06,9.0571e-10,-5.31829e-14,-60181.1,-102.05], Tmin=(1319,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 361,
    label = "QCYC(CCOC)OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {3,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {2,S} {15,S}
8  O u0 p2 c0 {6,S} {16,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.091,0.0802657,-6.69756e-05,2.79282e-08,-4.60982e-12,-51252.9,41.1897], Tmin=(300,'K'), Tmax=(1411,'K')),
            NASAPolynomial(coeffs=[22.086,0.0183744,-6.29479e-06,9.78788e-10,-5.68621e-14,-58965.2,-86.4964], Tmin=(1411,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 362,
    label = "HOCOCQ(CH3)2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {6,S} {14,D}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {4,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.56326,0.0677166,-5.146e-05,1.99185e-08,-3.16007e-12,-73094.3,23.7255], Tmin=(300,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[22.8935,0.0178628,-6.34628e-06,1.01069e-09,-5.96886e-14,-80540.1,-90.8954], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 363,
    label = "CHOC(CH3)OHCH2Q",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,D} {14,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {1,S} {15,S}
7  O u0 p2 c0 {5,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.40934,0.0613326,-4.03875e-05,1.22738e-08,-1.32997e-12,-58305,22.9871], Tmin=(300,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[22.4481,0.0178754,-6.26905e-06,9.90084e-10,-5.81417e-14,-65509.3,-85.6747], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 364,
    label = "CO(CH2OOH)2",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,D}
4  O u0 p2 c0 {1,S} {6,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {4,S} {13,S}
7  O u0 p2 c0 {5,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.47627,0.0893737,-9.25891e-05,4.63168e-08,-8.933e-12,-43892.4,48.4479], Tmin=(300,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[24.3376,0.0114074,-4.08932e-06,6.55183e-10,-3.88571e-14,-51686.3,-90.1518], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 365,
    label = "C4H6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {7,S} {8,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.37272,0.05767,-5.76208e-05,2.99837e-08,-6.17539e-12,12321.2,37.8455], Tmin=(298.15,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.48731,0.022021,-9.83379e-06,1.91676e-09,-1.06428e-13,10159.7,-10.6712], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298.15,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 366,
    label = "C4H5-I",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {4,D} {8,S} {9,S}
4 C u1 p0 c0 {1,S} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.420623,0.0438861,-4.32708e-05,2.43849e-08,-5.85727e-12,36906.7,26.089], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.25595,0.0219966,-1.09137e-05,2.63404e-09,-2.50557e-13,35705.5,-1.56386], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 367,
    label = "C4H5-N",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,D} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 C u1 p0 c0 {2,D} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.1836,0.0581814,-6.38642e-05,3.5745e-08,-7.89218e-12,42374,37.7564], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.29521,0.0191513,-9.57154e-06,2.33661e-09,-2.25148e-13,40131.4,-13.5255], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 368,
    label = "C4H5-2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2 C u1 p0 c0 {4,S} {8,S} {9,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {2,S} {3,T}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.31011,0.0283747,-1.63837e-05,4.46252e-09,-4.30511e-13,35584.3,14.9106], Tmin=(300,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[10.3231,0.0117626,-4.00005e-06,6.18728e-10,-3.58084e-14,32586.1,-28.8794], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 369,
    label = "C4H4",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {3,T} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.91525,0.0527509,-7.16559e-05,5.50724e-08,-1.72862e-11,32978.5,31.42], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.65071,0.0161294,-7.19389e-06,1.49818e-09,-1.18641e-13,31196,-9.79521], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 370,
    label = "C4H3-I",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.08304,0.0408343,-6.21597e-05,5.16794e-08,-1.70292e-11,58005.1,13.6175], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.09782,0.00922071,-3.38784e-06,4.91605e-10,-1.45298e-14,56600.6,-19.8026], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 371,
    label = "C4H3-N",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,T}
3 C u1 p0 c0 {1,D} {6,S}
4 C u0 p0 c0 {2,T} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.316841,0.0469121,-6.80938e-05,5.31799e-08,-1.6523e-11,62476.2,24.6226], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.43283,0.016861,-9.43131e-06,2.57039e-09,-2.74563e-13,61600.7,-1.5674], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 372,
    label = "C4H2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,T}
2 C u0 p0 c0 {1,S} {4,T}
3 C u0 p0 c0 {1,T} {5,S}
4 C u0 p0 c0 {2,T} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0544,0.041627,-6.58718e-05,5.32571e-08,-1.66832e-11,54185.2,14.8666], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.15763,0.00554305,-1.35916e-06,1.87801e-11,2.31895e-14,52588,-23.7115], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 373,
    label = "CHCC(CH2)CHCH2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,D} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {6,T}
6  C u0 p0 c0 {5,T} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0974937,0.0525465,-4.13131e-05,1.72824e-08,-3.0075e-12,37789.3,26.2209], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[15.026,0.0156364,-5.48047e-06,8.64877e-10,-5.07522e-14,32600.4,-54.6019], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 374,
    label = "CH2CHCHCHCCH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,D} {5,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {6,T}
6  C u0 p0 c0 {5,T} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.63758,0.0658049,-6.19478e-05,2.95389e-08,-5.56039e-12,39106.8,31.3986], Tmin=(300,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[17.1156,0.0135874,-4.71348e-06,7.38927e-10,-4.31679e-14,33400.1,-66.395], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 375,
    label = "CH2CHCHCHO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {5,S}
2  C u0 p0 c0 {1,D} {4,S} {6,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {7,D} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  O u0 p2 c0 {4,D}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.49321,0.052655,-5.1516e-05,2.5741e-08,-5.03442e-12,8263.68,26.1133], Tmin=(300,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[13.2552,0.0119067,-4.06548e-06,6.30313e-10,-3.65301e-14,4288.22,-44.7691], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 376,
    label = "NC4H5O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {5,S} {8,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  O u0 p2 c0 {3,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.612413,0.0552513,-5.12448e-05,2.41307e-08,-4.50077e-12,17411.5,24.0737], Tmin=(300,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[16.4522,0.0116957,-4.08e-06,6.41912e-10,-3.75907e-14,12538.1,-58.7191], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 377,
    label = "C3H3CH2OOH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {4,D} {10,S} {11,S}
4  C u0 p0 c0 {2,D} {3,D}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.64825,0.0528806,-4.39834e-05,1.88141e-08,-3.26453e-12,9504.1,22.1989], Tmin=(300,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[17.6338,0.012758,-4.44137e-06,6.98376e-10,-4.08987e-14,4207.46,-62.7098], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 378,
    label = "C3H3CH2O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {4,D} {9,S} {10,S}
4  C u0 p0 c0 {2,D} {3,D}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.53697,0.0218275,-3.15174e-06,-3.93257e-09,1.2873e-12,26145.8,2.17742], Tmin=(300,'K'), Tmax=(1676,'K')),
            NASAPolynomial(coeffs=[11.4428,0.0150893,-5.59322e-06,9.19033e-10,-5.55291e-14,23524,-31.911], Tmin=(1676,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 379,
    label = "C3H3CHO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,D} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 C u0 p0 c0 {4,D} {8,S} {9,S}
4 C u0 p0 c0 {1,D} {3,D}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.1417,0.0405129,-3.49446e-05,1.55825e-08,-2.79825e-12,5133.66,19.7622], Tmin=(300,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[12.7527,0.0100632,-3.49309e-06,5.47747e-10,-3.20021e-14,1415.29,-41.4481], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 380,
    label = "C2H3CHOHCH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.30466,0.0441216,-3.23936e-05,1.315e-08,-2.29928e-12,2897.44,18.6658], Tmin=(300,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[14.4788,0.0156398,-5.4724e-06,8.62564e-10,-5.05719e-14,-1476.14,-46.9554], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 381,
    label = "C2H3CHOHCH2OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {14,S}
6  O u0 p2 c0 {2,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {6,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.85133,0.0568751,-4.37973e-05,1.7701e-08,-2.95625e-12,-15117.1,24.8996], Tmin=(300,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[18.353,0.0169515,-5.91054e-06,9.29544e-10,-5.44176e-14,-20762.1,-63.3249], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 382,
    label = "C2H3CHOHCH2O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  O u1 p2 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.45139,0.0476174,-3.17417e-05,1.07287e-08,-1.48713e-12,-13895.9,20.1151], Tmin=(300,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[16.7238,0.0162893,-5.69978e-06,8.98524e-10,-5.26886e-14,-19097.6,-57.3256], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 383,
    label = "C4H51,3OH2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {9,S} {10,S}
4  C u0 p0 c0 {2,D} {7,S} {8,S}
5  O u0 p2 c0 {1,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.532203,0.0347944,9.07363e-06,-4.2689e-08,2.13649e-11,-9761.03,24.626], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.7569,0.0162958,-5.86746e-06,9.47794e-10,-5.68012e-14,-13380.9,-36.1323], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 384,
    label = "C2H3CHOHCHO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,S} {8,D} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.983,0.0357503,-8.68563e-06,-5.68946e-09,2.40247e-12,-28454.7,22.2891], Tmin=(300,'K'), Tmax=(1519,'K')),
            NASAPolynomial(coeffs=[16.261,0.0146912,-5.27967e-06,8.4724e-10,-5.03008e-14,-34559.8,-58.6215], Tmin=(1519,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 385,
    label = "C4H5OH1-4OOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {10,S}
3  C u0 p0 c0 {2,D} {5,S} {6,S}
4  C u1 p0 c0 {1,S} {11,S} {12,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {3,S} {13,S}
7  O u0 p2 c0 {5,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.30966,0.056653,-4.39894e-05,1.77261e-08,-2.93544e-12,-4326.26,23.9531], Tmin=(300,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[19.1838,0.0159285,-5.58252e-06,8.81017e-10,-5.17029e-14,-10093.5,-66.2735], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 386,
    label = "C4H5OH1-4OOH-2OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {7,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {2,S} {8,S}
6  O u0 p2 c0 {2,S} {14,S}
7  O u0 p2 c0 {3,S} {15,S}
8  O u0 p2 c0 {5,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 O u1 p2 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.31183,0.0747918,-6.6049e-05,2.9522e-08,-5.26743e-12,-28433,26.3335], Tmin=(300,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[24.7663,0.0159484,-5.61098e-06,8.87849e-10,-5.22018e-14,-35592.9,-91.9981], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 387,
    label = "C3H3OHCHO1-2OOH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {5,S}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  C u0 p0 c0 {2,D} {11,S} {12,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {1,S} {13,S}
7  O u0 p2 c0 {5,S} {14,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.79128,0.0572788,-3.75143e-05,1.08389e-08,-1.07752e-12,-41687.4,25.9258], Tmin=(300,'K'), Tmax=(1671,'K')),
            NASAPolynomial(coeffs=[20.1194,0.0168369,-6.36173e-06,1.05867e-09,-6.45336e-14,-47879.2,-72.7687], Tmin=(1671,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 388,
    label = "C4H5OH1-2,4OOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
3  C u1 p0 c0 {1,S} {2,S} {5,S}
4  C u0 p0 c0 {1,S} {6,S} {14,D}
5  O u0 p2 c0 {3,S} {8,S}
6  O u0 p2 c0 {4,S} {7,S}
7  O u0 p2 c0 {6,S} {15,S}
8  O u0 p2 c0 {5,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64256,0.0668211,-5.5264e-05,2.34597e-08,-4.03884e-12,-23159.3,22.8638], Tmin=(300,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[23.7938,0.0163847,-5.76911e-06,9.13314e-10,-5.37158e-14,-29847.7,-84.2153], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 389,
    label = "C4H5OJ1-2,4OOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {6,S} {12,D}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {8,S}
7  O u0 p2 c0 {5,S} {16,S}
8  O u0 p2 c0 {6,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.33801,0.0685025,-5.62798e-05,2.30601e-08,-3.77375e-12,-18942.5,15.6652], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[25.961,0.0150318,-5.31796e-06,8.44638e-10,-4.97917e-14,-26096.5,-99.317], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 390,
    label = "C3H3OH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {4,T}
3 O u0 p2 c0 {1,S} {7,S}
4 C u0 p0 c0 {2,T} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.664863,0.0390791,-3.85723e-05,1.92354e-08,-3.72429e-12,800.157,20.1988], Tmin=(300,'K'), Tmax=(1409,'K')),
            NASAPolynomial(coeffs=[10.7171,0.00856985,-2.82907e-06,4.28606e-10,-2.44382e-14,-1984.68,-31.2883], Tmin=(1409,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 391,
    label = "CDY(COCC)OH",
    molecule = 
"""
1  C u0 p0 c0 {3,D} {5,S} {6,S}
2  C u0 p0 c0 {4,D} {5,S} {7,S}
3  C u0 p0 c0 {1,D} {10,S} {11,S}
4  C u0 p0 c0 {2,D} {8,S} {9,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.28738,0.0685314,-6.01513e-05,2.6562e-08,-4.65128e-12,-20144.2,47.0823], Tmin=(300,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[15.9913,0.0148926,-5.14765e-06,8.05057e-10,-4.69531e-14,-26493.9,-59.493], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 392,
    label = "C3H2OHCH2Q",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {7,T}
4  O u0 p2 c0 {2,S} {6,S}
5  O u0 p2 c0 {1,S} {11,S}
6  O u0 p2 c0 {4,S} {13,S}
7  C u0 p0 c0 {3,T} {12,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.69903,0.0454113,-3.24594e-05,1.20346e-08,-1.84997e-12,-12888.8,9.19558], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[18.1132,0.0145656,-5.07825e-06,7.9865e-10,-4.67561e-14,-17633.2,-63.0842], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 393,
    label = "C3H4OCH2OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {2,S} {13,S}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68557,0.0371955,-1.57928e-05,1.29415e-09,4.50053e-13,-19963.1,14.1319], Tmin=(300,'K'), Tmax=(1678,'K')),
            NASAPolynomial(coeffs=[13.5768,0.0193824,-6.93534e-06,1.11509e-09,-6.64284e-14,-23703.3,-40.5883], Tmin=(1678,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 394,
    label = "C2H3COCH2Q",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,D}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.68972,0.0727108,-6.82565e-05,3.19924e-08,-5.91997e-12,-25169.8,39.9767], Tmin=(300,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[20.313,0.013062,-4.6443e-06,7.40055e-10,-4.37242e-14,-32007.8,-75.306], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 395,
    label = "C2H3CHOHCH2OOH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {2,S} {7,S}
6  O u0 p2 c0 {1,S} {14,S}
7  O u0 p2 c0 {5,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.944278,0.0634331,-4.99456e-05,2.05721e-08,-3.48144e-12,-31782.7,29.2924], Tmin=(300,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[19.3445,0.0182186,-6.34492e-06,9.97098e-10,-5.8342e-14,-37995.2,-68.8145], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 396,
    label = "C2H3OCHCH2OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {5,S} {9,S}
3  C u0 p0 c0 {4,D} {5,S} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {2,S} {3,S}
6  O u0 p2 c0 {1,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.35772,0.0664956,-5.97594e-05,2.74521e-08,-5.00267e-12,-11358.8,43.9224], Tmin=(300,'K'), Tmax=(1406,'K')),
            NASAPolynomial(coeffs=[16.1335,0.015703,-5.34936e-06,8.28273e-10,-4.79652e-14,-16996.8,-52.6511], Tmin=(1406,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 397,
    label = "CH2CH2COCH2OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  C u1 p0 c0 {1,S} {11,S} {12,S}
5  O u0 p2 c0 {2,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.86369,0.026555,-1.46596e-06,-7.41455e-09,2.42515e-12,-24276,6.7462], Tmin=(300,'K'), Tmax=(1498,'K')),
            NASAPolynomial(coeffs=[14.5573,0.0167758,-5.67488e-06,8.75537e-10,-5.06066e-14,-28311.8,-43.6209], Tmin=(1498,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 398,
    label = "C2H3COCH2OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52504,0.0370498,-2.04867e-05,5.38095e-09,-5.47927e-13,-35189.4,14.1522], Tmin=(300,'K'), Tmax=(1374,'K')),
            NASAPolynomial(coeffs=[14.501,0.0157294,-5.52878e-06,8.74136e-10,-5.13616e-14,-39549.2,-46.5252], Tmin=(1374,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 399,
    label = "C3H4CH2OH-1OOH",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {12,S}
4  C u0 p0 c0 {1,S} {3,D} {13,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {14,S}
7  O u0 p2 c0 {5,S} {15,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.62447,0.0566513,-3.85853e-05,1.3114e-08,-1.80854e-12,-29587.5,22.4313], Tmin=(300,'K'), Tmax=(1373,'K')),
            NASAPolynomial(coeffs=[20.5562,0.0173435,-6.08616e-06,9.61896e-10,-5.65239e-14,-36110.1,-74.8563], Tmin=(1373,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 400,
    label = "C3H4CH2OH-1O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {12,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.65239,0.023952,8.126e-06,-1.51386e-08,4.29644e-12,-12956,1.89176], Tmin=(300,'K'), Tmax=(1502,'K')),
            NASAPolynomial(coeffs=[17.1974,0.0164461,-5.88477e-06,9.41603e-10,-5.57897e-14,-18308.9,-60.7873], Tmin=(1502,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 401,
    label = "CH2OC3H4OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {5,S} {12,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.88678,0.042867,-2.48859e-05,6.91429e-09,-7.31773e-13,-11311.3,20.0968], Tmin=(300,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[15.5247,0.0172696,-6.02881e-06,9.48884e-10,-5.55788e-14,-16165.1,-49.2916], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 402,
    label = "CHOC3H4OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {10,D} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.11996,0.0443238,-2.97127e-05,1.00484e-08,-1.39027e-12,-33959.2,19.977], Tmin=(300,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[15.6484,0.0146898,-5.15632e-06,8.146e-10,-4.784e-14,-38894.5,-53.4469], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 403,
    label = "C4H71-OO3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.697499,0.0624503,-5.21065e-05,2.1934e-08,-3.68635e-12,4876.66,31.0774], Tmin=(300,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[18.2801,0.0142613,-4.85634e-06,7.52828e-10,-4.36658e-14,-1260.8,-69.3661], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 404,
    label = "C4H61-4OOH3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  C u0 p0 c0 {2,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.585216,0.0635552,-5.46197e-05,2.35378e-08,-4.02918e-12,12780,32.2245], Tmin=(300,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[18.8084,0.0134575,-4.59376e-06,7.13321e-10,-4.14239e-14,6598.98,-70.1086], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 405,
    label = "C4H61-OOH3-OO4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {14,S}
7  O u0 p2 c0 {5,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 O u1 p2 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.283626,0.0747135,-6.59702e-05,2.89688e-08,-5.0278e-12,-5217.59,32.3978], Tmin=(300,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[23.3277,0.0144238,-4.95806e-06,7.73526e-10,-4.50683e-14,-12482.2,-88.9215], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 406,
    label = "C4H61-2OOH34",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,D} {12,S}
4  O u0 p2 c0 {1,S} {8,S}
5  O u0 p2 c0 {2,S} {7,S}
6  C u1 p0 c0 {3,D} {13,S}
7  O u0 p2 c0 {5,S} {14,S}
8  O u0 p2 c0 {4,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.807372,0.0742391,-6.59005e-05,2.89288e-08,-5.01114e-12,5562.75,30.4532], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[24.0462,0.0135992,-4.71883e-06,7.40795e-10,-4.33462e-14,-1777.3,-91.9449], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 407,
    label = "C4H61-OOH34",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {12,S}
4  C u0 p0 c0 {3,D} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {8,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {15,S}
8  O u0 p2 c0 {5,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.55039,0.080898,-7.14917e-05,3.14215e-08,-5.45705e-12,-21893.2,35.7719], Tmin=(300,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[24.3682,0.0156263,-5.36622e-06,8.36673e-10,-4.87261e-14,-29739.5,-95.3858], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 408,
    label = "C4H61-OOH34-OO2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,S} {7,S}
2  O u0 p2 c0 {4,S} {8,S}
3  O u0 p2 c0 {6,S} {9,S}
4  O u0 p2 c0 {2,S} {16,S}
5  O u0 p2 c0 {1,S} {17,S}
6  O u1 p2 c0 {3,S}
7  C u0 p0 c0 {1,S} {8,S} {9,S} {11,S}
8  C u0 p0 c0 {2,S} {7,S} {12,S} {13,S}
9  C u0 p0 c0 {3,S} {7,S} {10,D}
10 C u0 p0 c0 {9,D} {14,S} {15,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {10,S}
15 H u0 p0 c0 {10,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.732401,0.0927972,-8.86482e-05,4.11652e-08,-7.44083e-12,-18534.4,33.175], Tmin=(300,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[29.6189,0.0136225,-4.74693e-06,7.4738e-10,-4.3822e-14,-27265.2,-117.599], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 409,
    label = "C4H412-OOH34",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {4,D} {11,S} {12,S}
4  C u0 p0 c0 {2,D} {3,D}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {5,S} {13,S}
8  O u0 p2 c0 {6,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.25297,0.0703406,-6.59547e-05,3.07772e-08,-5.66773e-12,-3837.24,22.2442], Tmin=(300,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[23.7714,0.0122692,-4.37586e-06,6.98707e-10,-4.134e-14,-10541.9,-90.5796], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 410,
    label = "C3H3CHO-OOH23",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,S} {10,D} {11,S}
4  C u0 p0 c0 {2,D} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {5,S} {15,S}
8  O u0 p2 c0 {6,S} {14,S}
9  H u0 p0 c0 {1,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.21287,0.0732715,-5.85847e-05,2.18421e-08,-3.09399e-12,-33253.1,30.2888], Tmin=(300,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[27.0409,0.0119362,-4.33841e-06,7.01449e-10,-4.18637e-14,-41900.6,-107.702], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 411,
    label = "C4H4O-OOH24",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,D} {5,S}
3  C u0 p0 c0 {1,S} {6,S} {11,D}
4  C u0 p0 c0 {2,D} {12,S} {13,S}
5  O u0 p2 c0 {2,S} {8,S}
6  O u0 p2 c0 {3,S} {7,S}
7  O u0 p2 c0 {6,S} {14,S}
8  O u0 p2 c0 {5,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.959576,0.0765314,-6.90785e-05,3.08837e-08,-5.46998e-12,-30830.8,33.7582], Tmin=(300,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[25.2106,0.0133312,-4.78042e-06,7.66052e-10,-4.54376e-14,-38567.3,-94.1154], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 412,
    label = "CH2CCO",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {6,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60552,0.0145152,-6.96191e-06,7.31584e-10,3.52253e-13,13552.4,8.43859], Tmin=(298.15,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.40003,0.0125785,-5.91888e-06,1.27759e-09,-9.45875e-14,13331.4,4.29517], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298.15,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 413,
    label = "C4H62-OOH14",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,D} {13,S}
4  C u0 p0 c0 {2,S} {3,D} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {5,S} {15,S}
8  O u0 p2 c0 {6,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.533887,0.0775331,-6.82133e-05,3.07799e-08,-5.6016e-12,-19819.7,33.2306], Tmin=(300,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[24.0028,0.0169212,-6.02148e-06,9.59977e-10,-5.67353e-14,-27486.7,-90.9248], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 414,
    label = "C4H512-OO4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {4,D} {9,S} {10,S}
4  C u0 p0 c0 {2,D} {3,D}
5  O u0 p2 c0 {1,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.52191,0.0471699,-4.032e-05,1.80913e-08,-3.27484e-12,25099.3,22.5475], Tmin=(300,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[14.2836,0.0130647,-4.4462e-06,6.87917e-10,-3.98144e-14,21077.9,-44.499], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 415,
    label = "C4H513-OO2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {9,S} {10,S}
4  C u0 p0 c0 {2,D} {7,S} {8,S}
5  O u0 p2 c0 {1,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.753229,0.0571867,-5.24258e-05,2.41573e-08,-4.38384e-12,18231.2,29.6637], Tmin=(300,'K'), Tmax=(1405,'K')),
            NASAPolynomial(coeffs=[15.6905,0.0119261,-4.06874e-06,6.30816e-10,-3.65703e-14,13253.5,-56.1395], Tmin=(1405,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 416,
    label = "CYCCCOO-3J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.47557,0.0602141,-5.37659e-05,2.4386e-08,-4.38846e-12,14343.7,36.4074], Tmin=(300,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[14.7511,0.0136106,-4.65773e-06,7.23551e-10,-4.20015e-14,9030.33,-53.7988], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 417,
    label = "C2H3COOCH2",
    molecule = 
"""
multiplicity 4
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {6,S}
3  C u0 p0 c0 {4,D} {6,S} {7,S}
4  C u0 p0 c0 {3,D} {8,S} {9,S}
5  C u1 p0 c0 {1,S} {10,S} {11,S}
6  C u2 p0 c0 {2,S} {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.00791,0.0451756,-3.38733e-05,1.27342e-08,-1.94378e-12,-16020.5,17.7256], Tmin=(300,'K'), Tmax=(1378,'K')),
            NASAPolynomial(coeffs=[16.5803,0.011544,-4.11632e-06,6.57144e-10,-3.8875e-14,-21131,-60.7009], Tmin=(1378,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 418,
    label = "CYCOOC-CH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.266211,0.0557788,-5.16416e-05,2.44394e-08,-4.56853e-12,27451.7,26.6023], Tmin=(300,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[14.9632,0.0128725,-4.37192e-06,6.75553e-10,-3.90654e-14,22893.4,-52.5926], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 419,
    label = "C4H6O25",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {1,S} {3,D} {11,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.67053,0.00492586,8.86967e-05,-1.26219e-07,5.23991e-11,-14657.2,14.5722], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.60658,0.020831,-8.42229e-06,1.56718e-09,-1.09391e-13,-17617.7,-23.2465], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 420,
    label = "C2H3CHOCH2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.59388,0.0579063,-4.97163e-05,2.15819e-08,-3.69199e-12,858.853,42.8475], Tmin=(300,'K'), Tmax=(1431,'K')),
            NASAPolynomial(coeffs=[12.6763,0.014082,-4.63474e-06,7.01091e-10,-3.99438e-14,-4080.65,-42.2516], Tmin=(1431,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 421,
    label = "C4H4O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {6,S}
2 C u0 p0 c0 {1,S} {4,D} {7,S}
3 C u0 p0 c0 {1,D} {5,S} {8,S}
4 C u0 p0 c0 {2,D} {5,S} {9,S}
5 O u0 p2 c0 {3,S} {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.847469,0.0131774,5.99736e-05,-9.71563e-08,4.22734e-11,-5367.85,21.4945], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.38935,0.0140291,-5.07755e-06,8.24137e-10,-4.9532e-14,-8682.42,-27.9163], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 422,
    label = "C4H6O23",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {5,S} {11,S}
5  O u0 p2 c0 {2,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.67053,0.00492586,8.86967e-05,-1.26219e-07,5.23991e-11,-10278.8,14.5722], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.60658,0.020831,-8.42229e-06,1.56718e-09,-1.09391e-13,-13239.3,-23.2465], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 423,
    label = "CYHEXDN13",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {6,S} {13,S}
6  C u0 p0 c0 {4,D} {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.82039,0.0670224,-4.73488e-05,1.69646e-08,-2.45944e-12,11421,45.531], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[15.0998,0.021208,-7.33544e-06,1.1476e-09,-6.69434e-14,4449.01,-61.6788], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 424,
    label = "CYHEXDN14",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,D} {11,S}
4  C u0 p0 c0 {1,S} {3,D} {12,S}
5  C u0 p0 c0 {1,S} {6,D} {13,S}
6  C u0 p0 c0 {2,S} {5,D} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.02044,0.0610389,-3.86838e-05,1.17506e-08,-1.35179e-12,11264.7,35.5809], Tmin=(300,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[15.7263,0.0209983,-7.33475e-06,1.15498e-09,-6.7677e-14,4379.85,-66.4318], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 425,
    label = "C6H8",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {8,S}
2  C u0 p0 c0 {1,D} {4,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {7,S}
4  C u0 p0 c0 {2,S} {6,D} {10,S}
5  C u0 p0 c0 {3,D} {11,S} {12,S}
6  C u0 p0 c0 {4,D} {13,S} {14,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.80217,0.0745729,-6.92666e-05,3.34618e-08,-6.42278e-12,17918.8,36.4469], Tmin=(300,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[16.9511,0.0186093,-6.39484e-06,9.95781e-10,-5.78882e-14,11935.9,-66.3328], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 426,
    label = "CYHEXEN-4J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  C u0 p0 c0 {2,S} {6,D} {15,S}
6  C u0 p0 c0 {3,S} {5,D} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.84381,0.0599346,-3.11377e-05,5.82015e-09,8.64222e-14,21106,45.3885], Tmin=(300,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[14.5727,0.0241688,-8.34934e-06,1.30512e-09,-7.60858e-14,14040.7,-55.9995], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 427,
    label = "CYPENTN-4MJ",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {5,D} {12,S}
5  C u0 p0 c0 {3,S} {4,D} {13,S}
6  C u1 p0 c0 {1,S} {14,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9447,0.00344172,0.000164472,-3.0151e-07,1.79534e-10,25170.2,12.4235], Tmin=(10,'K'), Tmax=(433.34,'K')),
            NASAPolynomial(coeffs=[-2.41048,0.0621592,-3.89685e-05,1.17649e-08,-1.36839e-12,25720.5,37.7632], Tmin=(433.34,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 428,
    label = "CYPENTN-4M4J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  C u0 p0 c0 {1,S} {6,D} {14,S}
6  C u0 p0 c0 {2,S} {5,D} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00036,-0.000625728,0.000158764,-2.60855e-07,1.387e-10,21064.3,11.8802], Tmin=(10,'K'), Tmax=(528.91,'K')),
            NASAPolynomial(coeffs=[-3.37192,0.0618953,-3.77368e-05,1.10139e-08,-1.23709e-12,21749.5,41.8568], Tmin=(528.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 429,
    label = "CYPENTN-4M3J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {6,S} {13,S}
5  C u0 p0 c0 {2,S} {6,D} {14,S}
6  C u0 p0 c0 {4,S} {5,D} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94633,0.00328517,0.000164956,-2.94963e-07,1.70105e-10,16801.1,11.8896], Tmin=(10,'K'), Tmax=(451.07,'K')),
            NASAPolynomial(coeffs=[-3.01889,0.0653666,-4.25402e-05,1.32584e-08,-1.58143e-12,17426.2,39.9119], Tmin=(451.07,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 430,
    label = "CYPENTN-4MTHNE",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {6,D}
4  C u0 p0 c0 {1,S} {5,D} {11,S}
5  C u0 p0 c0 {2,S} {4,D} {12,S}
6  C u0 p0 c0 {3,D} {13,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03826,-0.00404316,0.000173911,-2.84647e-07,1.48353e-10,14991.8,11.6115], Tmin=(10,'K'), Tmax=(592.29,'K')),
            NASAPolynomial(coeffs=[-2.10239,0.0581366,-3.60082e-05,1.06656e-08,-1.21248e-12,15355.9,34.954], Tmin=(592.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 431,
    label = "C4H612",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {4,D} {9,S} {10,S}
4  C u0 p0 c0 {2,D} {3,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.26299,0.0321839,-1.60587e-05,1.38632e-09,1.08752e-12,17741.1,18.9778], Tmin=(298.15,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.03555,0.0250965,-1.14319e-05,2.30462e-09,-1.42765e-13,16986.5,4.60107], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298.15,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 432,
    label = "C4H6-2",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,T}
4  C u0 p0 c0 {2,S} {3,T}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.65653,0.023044,1.57228e-07,-1.06199e-08,4.35705e-12,15723.7,12.0348], Tmin=(298.15,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.28493,0.0256209,-1.13438e-05,2.13795e-09,-1.05016e-13,15343.5,7.73048], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298.15,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 433,
    label = "H2C4O",
    molecule = 
"""
1 O u0 p2 c0 {5,D}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {3,D} {5,D}
5 C u0 p0 c0 {1,D} {4,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.81097,0.01314,9.86507e-07,-6.12072e-09,1.64e-12,25458,2.11342], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.2689,0.00489616,-4.88508e-07,-2.70857e-10,5.10701e-14,23469,-28.1598], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (4000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 434,
    label = "NC3H7CHO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,D} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.24209,0.0421278,-2.13832e-05,4.22615e-09,-1.03711e-13,-27104.9,22.1567], Tmin=(300,'K'), Tmax=(1679,'K')),
            NASAPolynomial(coeffs=[11.9789,0.0204894,-7.24832e-06,1.15562e-09,-6.8412e-14,-30927.2,-36.393], Tmin=(1679,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 435,
    label = "NC3H7CO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.63538,0.0340369,-1.24119e-05,-1.17887e-09,1.16488e-12,-8659.2,16.8408], Tmin=(300,'K'), Tmax=(1496,'K')),
            NASAPolynomial(coeffs=[13.487,0.0158627,-5.41699e-06,8.40509e-10,-4.8757e-14,-13072.5,-43.8634], Tmin=(1496,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 436,
    label = "C3H6CHO-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {9,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {4,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.21483,0.0354113,-1.44083e-05,5.27606e-11,8.95003e-13,-2464.83,20.0076], Tmin=(300,'K'), Tmax=(1538,'K')),
            NASAPolynomial(coeffs=[13.3449,0.0159347,-5.43144e-06,8.41706e-10,-4.87847e-14,-6912.82,-41.9662], Tmin=(1538,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 437,
    label = "C3H6CHO-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  C u0 p0 c0 {1,S} {11,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01373,0.0233174,5.72464e-06,-1.27183e-08,3.69913e-12,-4167.66,13.0546], Tmin=(300,'K'), Tmax=(1439,'K')),
            NASAPolynomial(coeffs=[12.7129,0.0168633,-5.8378e-06,9.1406e-10,-5.33576e-14,-8501.66,-38.462], Tmin=(1439,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 438,
    label = "C3H6CHO-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {11,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.529001,0.0430707,-2.49474e-05,6.40935e-09,-5.2777e-13,-6876.67,24.8856], Tmin=(300,'K'), Tmax=(1678,'K')),
            NASAPolynomial(coeffs=[12.173,0.0180057,-6.43783e-06,1.03362e-09,-6.1485e-14,-10864.2,-38.0322], Tmin=(1678,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 439,
    label = "C2H5COCH3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {13,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.57048,0.0351447,-1.2385e-05,-1.21281e-09,1.16164e-12,-31019.4,16.1395], Tmin=(300,'K'), Tmax=(1454,'K')),
            NASAPolynomial(coeffs=[12.8183,0.0179874,-5.94195e-06,9.01636e-10,-5.14994e-14,-35171.2,-41.1609], Tmin=(1454,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 440,
    label = "C2H5COCH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {10,D}
4  C u1 p0 c0 {3,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.96643,0.0410271,-2.56194e-05,7.86244e-09,-9.26826e-13,-8801.49,18.4804], Tmin=(300,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[13.5979,0.0157188,-5.35201e-06,8.28428e-10,-4.79646e-14,-13011.2,-44.6216], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 441,
    label = "CH2CH2COCH3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  C u1 p0 c0 {1,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.36192,0.0350401,-1.70487e-05,3.0907e-09,2.80365e-14,-6027.54,19.5185], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[11.7916,0.0170296,-5.75444e-06,8.86035e-10,-5.11071e-14,-9706.83,-32.5533], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 442,
    label = "CH3CHCOCH3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {4,S} {12,S}
4  C u0 p0 c0 {2,S} {3,S} {11,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.31082,0.0283712,-5.64604e-06,-4.62626e-09,1.82954e-12,-11460.2,16.2217], Tmin=(300,'K'), Tmax=(1438,'K')),
            NASAPolynomial(coeffs=[11.9651,0.0163142,-5.3988e-06,8.20455e-10,-4.69198e-14,-15199.1,-33.0143], Tmin=(1438,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 443,
    label = "C2H3COCH3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.655911,0.0419405,-3.0027e-05,1.16578e-08,-1.92101e-12,-17221.7,23.8412], Tmin=(300,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[11.999,0.0152616,-5.26019e-06,8.20774e-10,-4.77835e-14,-21217.1,-37.1384], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 444,
    label = "CH3CHOOCOCH3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {13,D}
5  O u0 p2 c0 {1,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.30172,0.0462274,-3.12564e-05,1.08628e-08,-1.51478e-12,-26373.2,11.9724], Tmin=(300,'K'), Tmax=(1411,'K')),
            NASAPolynomial(coeffs=[16.8056,0.0170791,-5.69439e-06,8.68879e-10,-4.98008e-14,-30671.9,-55.1179], Tmin=(1411,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 445,
    label = "CH2CHOOHCOCH3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,D}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.45962,0.04672,-3.15879e-05,1.06246e-08,-1.38857e-12,-18472.1,12.9656], Tmin=(300,'K'), Tmax=(1413,'K')),
            NASAPolynomial(coeffs=[17.8031,0.0160286,-5.38152e-06,8.25242e-10,-4.74719e-14,-23076.8,-58.737], Tmin=(1413,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 446,
    label = "C2H5CHCO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-22.8307,0.170978,-0.000353394,2.78222e-07,-6.77325e-11,-10412.5,131.233], Tmin=(300,'K'), Tmax=(1550,'K')),
            NASAPolynomial(coeffs=[-204.041,0.293467,-0.000115885,1.95254e-08,-1.19031e-12,82738,1212.33], Tmin=(1550,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 447,
    label = "NC5CYCPER24",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {7,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,D} {16,S}
6  O u0 p2 c0 {1,S} {17,S}
7  O u0 p2 c0 {3,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u0 p2 c0 {5,D}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.2587,0.0926924,-7.79864e-05,3.34971e-08,-5.74391e-12,-47690.2,46.2164], Tmin=(300,'K'), Tmax=(1408,'K')),
            NASAPolynomial(coeffs=[22.2821,0.023331,-7.91636e-06,1.22269e-09,-7.06907e-14,-56069.8,-93.5419], Tmin=(1408,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 448,
    label = "NC5CYCPER31",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {7,S} {16,D}
6  O u0 p2 c0 {1,S} {17,S}
7  O u0 p2 c0 {5,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u0 p2 c0 {5,D}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.01648,0.0890856,-7.09557e-05,2.89247e-08,-4.75384e-12,-45627.4,46.5939], Tmin=(300,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[22.0861,0.0239837,-8.24799e-06,1.28547e-09,-7.47886e-14,-54216.2,-92.0233], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 449,
    label = "IC4H6Q2-II",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {5,S} {15,S}
8  O u0 p2 c0 {6,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.216408,0.0825572,-7.6454e-05,3.58212e-08,-6.67719e-12,-20569.5,33.6943], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[25.0361,0.016023,-5.70705e-06,9.10412e-10,-5.38295e-14,-28419.6,-96.7186], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 450,
    label = "C5H10-1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.165024,0.0530727,-3.10862e-05,8.92413e-09,-9.8162e-13,-4573.63,28.057], Tmin=(300,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[14.3625,0.0226076,-7.70501e-06,1.1933e-09,-6.91126e-14,-9999.16,-51.2512], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 451,
    label = "C5H10-2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {5,D} {15,S}
5  C u0 p0 c0 {3,S} {4,D} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.590529,0.0485275,-2.43232e-05,4.86096e-09,-1.13099e-13,-5997.78,24.1816], Tmin=(300,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[13.9426,0.0228735,-7.778e-06,1.20285e-09,-6.95972e-14,-11216.6,-49.538], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 452,
    label = "C5H81-3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.54882,0.0415043,-2.1436e-05,4.71146e-09,-2.42143e-13,9056.36,19.5666], Tmin=(300,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[12.9945,0.0192678,-6.58967e-06,1.02296e-09,-5.93441e-14,4590.4,-43.569], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 453,
    label = "C5H91-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.46816,0.0513473,-3.05649e-05,8.8281e-09,-9.61458e-13,12378.1,28.3588], Tmin=(300,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[13.9594,0.020918,-7.14307e-06,1.10781e-09,-6.42268e-14,7026.51,-50.3104], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 454,
    label = "C5H91-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {2,S} {11,S}
4  C u0 p0 c0 {1,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.58798,0.0401577,-1.50063e-05,-3.94608e-10,1.02064e-12,18468.4,23.4273], Tmin=(300,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[12.923,0.0210932,-7.14227e-06,1.10138e-09,-6.35984e-14,13819.2,-40.0293], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 455,
    label = "C5H91-5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u1 p0 c0 {2,S} {11,S} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.207677,0.0496049,-3.00622e-05,9.19962e-09,-1.13246e-12,20125.2,28.5856], Tmin=(300,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[13.7335,0.0207003,-7.06963e-06,1.09639e-09,-6.35591e-14,15117.6,-45.0795], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 456,
    label = "C5H92-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {5,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {3,S} {4,D} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.255028,0.0469861,-2.40448e-05,4.89007e-09,-1.15558e-13,10977.5,24.6227], Tmin=(300,'K'), Tmax=(1384,'K')),
            NASAPolynomial(coeffs=[13.5638,0.0211621,-7.20826e-06,1.11611e-09,-6.4637e-14,5822.59,-48.7324], Tmin=(1384,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 457,
    label = "C5H92-5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  C u1 p0 c0 {1,S} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.996364,0.0449149,-2.30951e-05,5.01699e-09,-2.38646e-13,18716.2,24.5616], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[13.2989,0.0209846,-7.14999e-06,1.10717e-09,-6.41184e-14,13927,-43.2759], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 458,
    label = "C5H9O1-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.49666,0.0520326,-3.09828e-05,9.02567e-09,-1.04311e-12,1547.59,17.0868], Tmin=(300,'K'), Tmax=(1379,'K')),
            NASAPolynomial(coeffs=[17.886,0.0204837,-7.16613e-06,1.12949e-09,-6.62221e-14,-4331.4,-67.2851], Tmin=(1379,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 459,
    label = "C5H9O2-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {5,D} {15,S}
5  C u0 p0 c0 {3,S} {4,D} {14,S}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.389,0.0471705,-2.4039e-05,4.99167e-09,-2.03243e-13,115.233,12.5184], Tmin=(300,'K'), Tmax=(1376,'K')),
            NASAPolynomial(coeffs=[17.3707,0.0209045,-7.30724e-06,1.15107e-09,-6.74601e-14,-5480.2,-65.0109], Tmin=(1376,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 460,
    label = "BC5H10",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {2,S} {5,D}
5  C u0 p0 c0 {3,S} {4,D} {15,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.604883,0.0496635,-2.66571e-05,6.47312e-09,-4.84018e-13,-8063.12,22.3818], Tmin=(300,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[14.0426,0.0227915,-7.74903e-06,1.19815e-09,-6.93127e-14,-13216,-51.447], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 461,
    label = "CC5H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.964397,0.0568483,-3.66324e-05,1.23009e-08,-1.71393e-12,-5935.02,30.2998], Tmin=(300,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[14.4243,0.0226455,-7.73646e-06,1.2e-09,-6.95711e-14,-11498.1,-53.0391], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 462,
    label = "CC5H9-A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u1 p0 c0 {1,S} {11,S} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.67891,0.0537496,-3.61117e-05,1.28563e-08,-1.92156e-12,18797.4,31.2403], Tmin=(300,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[13.8636,0.0206363,-7.05717e-06,1.0954e-09,-6.35382e-14,13610.4,-47.2507], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 463,
    label = "CC5H9-B",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.691502,0.0509805,-2.96448e-05,8.28273e-09,-8.57575e-13,10747.8,27.6712], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[13.525,0.0214364,-7.35304e-06,1.14369e-09,-6.64364e-14,5413.82,-50.0302], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 464,
    label = "AC5H9O-C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {5,D}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.04951,0.0536585,-3.35087e-05,1.06174e-08,-1.39224e-12,-385.113,19.1077], Tmin=(300,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[17.679,0.0205915,-7.18764e-06,1.13116e-09,-6.62505e-14,-6251.47,-66.2132], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 465,
    label = "CC5H9O-B",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.75615,0.0520514,-3.10967e-05,8.25895e-09,-6.59917e-13,-1351.63,14.099], Tmin=(300,'K'), Tmax=(1377,'K')),
            NASAPolynomial(coeffs=[18.6974,0.0184543,-6.18683e-06,9.48851e-10,-5.46204e-14,-7158.98,-72.654], Tmin=(1377,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 466,
    label = "AC5H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {5,D}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.539429,0.054449,-3.32708e-05,1.03048e-08,-1.28363e-12,-6539.67,29.035], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[14.1931,0.0226551,-7.70009e-06,1.19031e-09,-6.8849e-14,-11949.1,-51.0689], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 467,
    label = "AC5H9-A2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {5,D}
4  C u1 p0 c0 {3,S} {11,S} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.954048,0.0550153,-3.58308e-05,1.16444e-08,-1.49087e-12,11596,30.8477], Tmin=(300,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[15.002,0.0195965,-6.60206e-06,1.01536e-09,-5.85455e-14,5900.81,-55.4529], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 468,
    label = "AC5H9-C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {5,D}
4  C u1 p0 c0 {2,S} {3,S} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.841373,0.0527157,-3.27335e-05,1.01974e-08,-1.26085e-12,10432.1,29.3317], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[13.7918,0.0209645,-7.13793e-06,1.10481e-09,-6.39628e-14,5095.56,-50.1391], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 469,
    label = "AC5H9-D",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  C u1 p0 c0 {1,S} {11,S} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.167398,0.0509877,-3.22616e-05,1.05912e-08,-1.43705e-12,18179.3,29.5711], Tmin=(300,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[13.5608,0.0207515,-7.06609e-06,1.09362e-09,-6.33083e-14,13189.7,-44.8719], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 470,
    label = "B2E2M1OJ",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {2,S} {5,D}
5  C u0 p0 c0 {3,S} {4,D} {15,S}
6  O u1 p2 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.64763,0.034361,-5.6065e-06,-5.19111e-09,1.73155e-12,-6.65738,3.13825], Tmin=(300,'K'), Tmax=(2003,'K')),
            NASAPolynomial(coeffs=[13.5666,0.0256548,-9.37226e-06,1.52518e-09,-9.15379e-14,-3587.67,-42.7273], Tmin=(2003,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 471,
    label = "B13DE2M",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {12,S} {13,S}
5  C u0 p0 c0 {3,D} {10,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.47217,0.0559413,-4.50459e-05,1.96181e-08,-3.5201e-12,7149.6,25.6277], Tmin=(300,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[14.0758,0.0182376,-6.20748e-06,9.60351e-10,-5.55742e-14,2400.34,-51.2988], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 472,
    label = "B13DE2MJ",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,D}
2  C u0 p0 c0 {1,S} {5,D} {6,S}
3  C u1 p0 c0 {1,S} {7,S} {8,S}
4  C u0 p0 c0 {1,D} {9,S} {10,S}
5  C u0 p0 c0 {2,D} {11,S} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.898037,0.0565174,-4.76108e-05,2.09672e-08,-3.73076e-12,25288.2,27.4967], Tmin=(300,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[14.8413,0.0152426,-5.1356e-06,7.89787e-10,-4.55353e-14,20266.2,-55.4475], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 473,
    label = "B12DE3M",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  C u0 p0 c0 {5,D} {12,S} {13,S}
5  C u0 p0 c0 {3,D} {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2786,0.0454917,-2.82334e-05,8.98449e-09,-1.1722e-12,13163.7,18.7039], Tmin=(300,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[13.7093,0.0185727,-6.33116e-06,9.80719e-10,-5.681e-14,8595.19,-48.875], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 474,
    label = "B2E3M1OJ",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {2,S} {5,D}
5  C u0 p0 c0 {3,S} {4,D} {15,S}
6  O u1 p2 c0 {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.64763,0.034361,-5.6065e-06,-5.19111e-09,1.73155e-12,-6.65738,3.13825], Tmin=(300,'K'), Tmax=(2003,'K')),
            NASAPolynomial(coeffs=[13.5666,0.0256548,-9.37226e-06,1.52518e-09,-9.15379e-14,-3587.67,-42.7273], Tmin=(2003,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 475,
    label = "TC4H8CHO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {12,D} {15,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.958078,0.0642003,-4.70777e-05,1.75738e-08,-2.64896e-12,-6865.83,33.3781], Tmin=(300,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[17.9664,0.0194207,-6.67409e-06,1.03969e-09,-6.04703e-14,-13336.9,-67.9819], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 476,
    label = "O2C4H8CHO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,D} {16,S}
6  O u0 p2 c0 {2,S} {17,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u0 p2 c0 {5,D}
16 H u0 p0 c0 {5,S}
17 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.91848,0.0667246,-4.80871e-05,1.78589e-08,-2.71164e-12,-24983.8,23.8578], Tmin=(300,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[21.263,0.0214072,-7.38343e-06,1.15282e-09,-6.71508e-14,-31685.5,-79.9829], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 477,
    label = "O2HC4H8CO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {7,S}
6  C u1 p0 c0 {1,S} {16,D}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u0 p2 c0 {6,D}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.82607,0.0693466,-4.93125e-05,1.69848e-08,-2.26118e-12,-24657.8,24.1168], Tmin=(300,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[23.822,0.0191411,-6.67919e-06,1.05127e-09,-6.15877e-14,-32309.4,-94.2581], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 478,
    label = "C6H10D24",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,D} {13,S}
4  C u0 p0 c0 {2,S} {6,D} {14,S}
5  C u0 p0 c0 {3,D} {6,S} {15,S}
6  C u0 p0 c0 {4,D} {5,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.363783,0.0636719,-4.5309e-05,1.73368e-08,-2.79133e-12,3040.87,27.5469], Tmin=(300,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[16.7663,0.023211,-7.93355e-06,1.23102e-09,-7.13893e-14,-2933.25,-64.4104], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 479,
    label = "C6H101-5",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  C u0 p0 c0 {4,D} {15,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.01375,0.0638243,-4.40654e-05,1.58295e-08,-2.30831e-12,7940.34,32.5056], Tmin=(300,'K'), Tmax=(1413,'K')),
            NASAPolynomial(coeffs=[16.0456,0.0234774,-7.85798e-06,1.20201e-09,-6.901e-14,2118.99,-58.8452], Tmin=(1413,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 480,
    label = "C6H9-A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {4,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,S} {6,D} {11,S}
5  C u0 p0 c0 {3,D} {14,S} {15,S}
6  C u0 p0 c0 {4,D} {12,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.724108,0.0600319,-3.9664e-05,1.30604e-08,-1.70076e-12,25915.4,32.2515], Tmin=(300,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[17.0377,0.0205549,-6.96492e-06,1.07547e-09,-6.21899e-14,19575.3,-63.8078], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 481,
    label = "C5D2Y1-1R",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 O u1 p2 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.767164,0.0523889,-3.85651e-05,1.48264e-08,-2.35264e-12,-236.669,25.0746], Tmin=(300,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[15.8396,0.0166572,-5.74156e-06,8.96152e-10,-5.21898e-14,-5439.55,-55.7244], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 482,
    label = "C3Y1-3OR",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {2,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.64167,0.0294284,-1.29128e-05,3.88758e-10,7.42969e-13,-24111.5,18.933], Tmin=(300,'K'), Tmax=(1409,'K')),
            NASAPolynomial(coeffs=[12.4459,0.0115136,-3.89008e-06,5.99668e-10,-3.46407e-14,-27899.7,-35.2984], Tmin=(1409,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 483,
    label = "C4Y1-3OR",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94684,0.0365985,-1.24268e-05,-2.56059e-09,1.66288e-12,-21350.7,11.8427], Tmin=(300,'K'), Tmax=(1417,'K')),
            NASAPolynomial(coeffs=[16.4998,0.015839,-5.41016e-06,8.39905e-10,-4.87506e-14,-26423.3,-58.3737], Tmin=(1417,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 484,
    label = "C6D2Y1",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {17,S}
2  C u0 p0 c0 {3,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {6,S} {8,S}
4  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {3,S} {7,D} {15,S}
7  C u0 p0 c0 {5,S} {6,D} {16,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.269585,0.06981,-5.04217e-05,1.90983e-08,-2.99717e-12,-21692.3,30.5709], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[19.5305,0.0232321,-7.99722e-06,1.24699e-09,-7.25687e-14,-28572,-75.7136], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 485,
    label = "C6D2Y1-1R",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,S} {16,S}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {3,S} {7,D}
6  C u1 p0 c0 {4,S} {7,S} {14,S}
7  C u0 p0 c0 {5,D} {6,S} {15,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.50366,0.065019,-4.73913e-05,1.80513e-08,-2.8408e-12,-3164,28.0316], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[19.1108,0.0211064,-7.27838e-06,1.13628e-09,-6.61819e-14,-9608.87,-71.7888], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 486,
    label = "H15DE25DM",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {3,S} {7,D}
6  C u0 p0 c0 {2,S} {4,S} {8,D}
7  C u0 p0 c0 {5,D} {19,S} {20,S}
8  C u0 p0 c0 {6,D} {21,S} {22,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.71853,0.0882614,-6.03141e-05,2.15862e-08,-3.19691e-12,-1952.56,38.6049], Tmin=(300,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[22.5356,0.0323956,-1.10271e-05,1.70641e-09,-9.87758e-14,-10480.9,-91.9785], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 487,
    label = "H15DE25DM-S",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {2,S} {7,D}
5  C u0 p0 c0 {3,S} {6,D} {8,S}
6  C u0 p0 c0 {1,S} {5,D} {17,S}
7  C u0 p0 c0 {4,D} {20,S} {21,S}
8  C u1 p0 c0 {5,S} {18,S} {19,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.04236,0.0866262,-5.99111e-05,2.15552e-08,-3.18977e-12,15022.4,39.6918], Tmin=(300,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[22.1423,0.0306966,-1.04617e-05,1.62038e-09,-9.38579e-14,6560.46,-90.406], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 488,
    label = "H15DE25DM-A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {3,S} {6,D}
5  C u0 p0 c0 {2,S} {7,S} {8,D}
6  C u0 p0 c0 {4,D} {20,S} {21,S}
7  C u1 p0 c0 {5,S} {16,S} {17,S}
8  C u0 p0 c0 {5,D} {18,S} {19,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.21863,0.0891653,-6.33361e-05,2.32007e-08,-3.4633e-12,16197.1,41.5117], Tmin=(300,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[23.3283,0.0293694,-9.94259e-06,1.53368e-09,-8.8603e-14,7373.19,-95.5902], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 489,
    label = "H15DE25DM-AO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {6,S} {13,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {3,S} {7,D}
6  C u0 p0 c0 {2,S} {4,S} {8,D}
7  C u0 p0 c0 {5,D} {19,S} {20,S}
8  C u0 p0 c0 {6,D} {21,S} {22,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u1 p2 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.03692,0.075064,-4.1778e-05,1.07916e-08,-9.97734e-13,6116.5,20.4746], Tmin=(300,'K'), Tmax=(1378,'K')),
            NASAPolynomial(coeffs=[25.0986,0.0315086,-1.10077e-05,1.73332e-09,-1.01557e-13,-2494.65,-101.098], Tmin=(1378,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 490,
    label = "H15DE25DM-SO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {12,S}
3  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {3,S} {7,D}
6  C u0 p0 c0 {2,S} {4,S} {8,D}
7  C u0 p0 c0 {5,D} {19,S} {20,S}
8  C u0 p0 c0 {6,D} {21,S} {22,S}
9  O u1 p2 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.930464,0.087167,-5.99583e-05,2.15026e-08,-3.21688e-12,4193.1,29.0925], Tmin=(300,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[26.0152,0.0304296,-1.05677e-05,1.65747e-09,-9.6847e-14,-4795.69,-106.442], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 491,
    label = "H15DE2M-T",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {3,S} {5,D}
5  C u0 p0 c0 {4,D} {15,S} {16,S}
6  C u0 p0 c0 {7,D} {17,S} {18,S}
7  C u1 p0 c0 {2,S} {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.388856,0.0670216,-4.29671e-05,1.4249e-08,-1.96106e-12,30362.7,29.5444], Tmin=(300,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[19.0145,0.0261932,-9.01184e-06,1.40456e-09,-8.17075e-14,23555.1,-71.5569], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 492,
    label = "IC4H7CHO",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  C u0 p0 c0 {1,S} {11,D} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.20983,0.0592603,-4.2696e-05,1.60356e-08,-2.49348e-12,-15620.5,35.3137], Tmin=(300,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[15.9172,0.0193357,-6.70858e-06,1.05155e-09,-6.14176e-14,-21614.1,-56.7617], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 493,
    label = "C8H141-5,3-4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {7,D} {17,S}
6  C u0 p0 c0 {2,S} {8,D} {18,S}
7  C u0 p0 c0 {5,D} {19,S} {20,S}
8  C u0 p0 c0 {6,D} {21,S} {22,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.52713,0.0928838,-6.67177e-05,2.53684e-08,-4.01213e-12,-45.5966,42.3181], Tmin=(300,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[23.0691,0.0323154,-1.10796e-05,1.72276e-09,-1.00053e-13,-8912.4,-94.9656], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 494,
    label = "C8H131-5,3-4,TA",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u1 p0 c0 {1,S} {3,S} {6,S}
5  C u0 p0 c0 {1,S} {7,D} {16,S}
6  C u0 p0 c0 {4,S} {8,D} {17,S}
7  C u0 p0 c0 {5,D} {20,S} {21,S}
8  C u0 p0 c0 {6,D} {18,S} {19,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.23997,0.0913495,-6.60037e-05,2.51706e-08,-3.99031e-12,16434.5,44.9499], Tmin=(300,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[22.2823,0.0310652,-1.06941e-05,1.6674e-09,-9.70243e-14,7576.81,-91.9859], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 495,
    label = "C6H101-3,3",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {2,S} {3,D} {13,S}
5  C u0 p0 c0 {3,S} {6,D} {14,S}
6  C u0 p0 c0 {5,D} {15,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.030131,0.0643105,-4.75083e-05,1.89878e-08,-3.17681e-12,2823.67,24.9255], Tmin=(300,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[16.9678,0.0228868,-7.78758e-06,1.20465e-09,-6.97081e-14,-2972.77,-65.8633], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 496,
    label = "C8H131-5,3-4,TAO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {7,D} {17,S}
6  C u0 p0 c0 {2,S} {8,D} {18,S}
7  C u0 p0 c0 {5,D} {19,S} {20,S}
8  C u0 p0 c0 {6,D} {21,S} {22,S}
9  O u1 p2 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0068,0.0890191,-6.27964e-05,2.24162e-08,-3.20587e-12,4564.23,27.6547], Tmin=(300,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[27.0579,0.0284727,-9.66435e-06,1.49337e-09,-8.63788e-14,-4431.11,-112.228], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 497,
    label = "C8H141-5,3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {8,D} {18,S}
6  C u0 p0 c0 {2,S} {7,D} {19,S}
7  C u0 p0 c0 {4,S} {6,D} {20,S}
8  C u0 p0 c0 {5,D} {21,S} {22,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.02072,0.0847809,-5.47568e-05,1.81792e-08,-2.47336e-12,-453.249,36.4247], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[22.5174,0.0326749,-1.11808e-05,1.7363e-09,-1.00752e-13,-8960.63,-91.0858], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 498,
    label = "C8H131-5,3,TA",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
4  C u1 p0 c0 {1,S} {2,S} {7,S}
5  C u0 p0 c0 {1,S} {6,D} {17,S}
6  C u0 p0 c0 {3,S} {5,D} {18,S}
7  C u0 p0 c0 {4,S} {8,D} {19,S}
8  C u0 p0 c0 {7,D} {20,S} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.503201,0.0778854,-4.63156e-05,1.32834e-08,-1.42623e-12,15838.9,32.6514], Tmin=(300,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[21.6162,0.0314327,-1.07786e-05,1.67633e-09,-9.73755e-14,7608.97,-88.0384], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 499,
    label = "C8H131-5,3,SA",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
4  C u1 p0 c0 {1,S} {7,S} {17,S}
5  C u0 p0 c0 {1,S} {8,D} {16,S}
6  C u0 p0 c0 {3,S} {7,D} {18,S}
7  C u0 p0 c0 {4,S} {6,D} {19,S}
8  C u0 p0 c0 {5,D} {20,S} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.32186,0.0830474,-5.42213e-05,1.80737e-08,-2.45105e-12,16518.3,36.717], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[22.1142,0.0309871,-1.06198e-05,1.651e-09,-9.58788e-14,8085.1,-90.1448], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 500,
    label = "C8H131-5,3,PA",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {7,D} {16,S}
5  C u0 p0 c0 {2,S} {6,D} {15,S}
6  C u0 p0 c0 {5,D} {8,S} {17,S}
7  C u0 p0 c0 {4,D} {20,S} {21,S}
8  C u1 p0 c0 {6,S} {18,S} {19,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.57063,0.0860081,-5.83884e-05,2.02048e-08,-2.83116e-12,17701.5,39.5476], Tmin=(300,'K'), Tmax=(1389,'K')),
            NASAPolynomial(coeffs=[23.2086,0.0297529,-1.01334e-05,1.56926e-09,-9.09001e-14,8953.39,-94.0778], Tmin=(1389,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 501,
    label = "C8H131-5,3,TAO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {8,D} {18,S}
6  C u0 p0 c0 {2,S} {7,D} {19,S}
7  C u0 p0 c0 {4,S} {6,D} {20,S}
8  C u0 p0 c0 {5,D} {21,S} {22,S}
9  O u1 p2 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.46772,0.0767801,-5.6319e-05,2.2269e-08,-3.64814e-12,1174.76,14.562], Tmin=(300,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[21.6639,0.0277253,-9.69376e-06,1.67582e-09,-1.08059e-13,-5703.01,-93.3238], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 502,
    label = "C8H131-5,3,SAO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {8,D} {18,S}
6  C u0 p0 c0 {2,S} {7,D} {19,S}
7  C u0 p0 c0 {4,S} {6,D} {20,S}
8  C u0 p0 c0 {5,D} {21,S} {22,S}
9  H u0 p0 c0 {1,S}
10 O u1 p2 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.60954,0.0839739,-5.49469e-05,1.84255e-08,-2.5604e-12,5337.13,26.2654], Tmin=(300,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[26.1024,0.0305037,-1.06268e-05,1.67027e-09,-9.77389e-14,-3647.44,-106.781], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 503,
    label = "C8H131-5,3,PAO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {8,D} {18,S}
6  C u0 p0 c0 {2,S} {7,D} {19,S}
7  C u0 p0 c0 {4,S} {6,D} {20,S}
8  C u0 p0 c0 {5,D} {21,S} {22,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u1 p2 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91532,0.071032,-3.55624e-05,6.98595e-09,-1.83466e-13,7229.12,16.7146], Tmin=(300,'K'), Tmax=(1374,'K')),
            NASAPolynomial(coeffs=[25.1903,0.031563,-1.10568e-05,1.74424e-09,-1.02327e-13,-1344.02,-101.448], Tmin=(1374,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 504,
    label = "C7H111-5,3,6P",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {6,D} {14,S}
5  C u0 p0 c0 {2,S} {7,D} {15,S}
6  C u0 p0 c0 {4,D} {16,S} {17,S}
7  C u1 p0 c0 {5,D} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.676849,0.0738083,-5.35945e-05,2.06294e-08,-3.29701e-12,32816,34.0518], Tmin=(300,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[19.5787,0.0254214,-8.68127e-06,1.3463e-09,-7.80465e-14,25853.8,-74.4112], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 505,
    label = "C8H142-6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {8,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {7,D} {20,S}
6  C u0 p0 c0 {2,S} {8,D} {21,S}
7  C u0 p0 c0 {3,S} {5,D} {19,S}
8  C u0 p0 c0 {4,S} {6,D} {22,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.343525,0.0772359,-4.34861e-05,1.12949e-08,-9.77995e-13,-837.798,29.8241], Tmin=(300,'K'), Tmax=(1386,'K')),
            NASAPolynomial(coeffs=[22.0961,0.0327887,-1.117e-05,1.7297e-09,-1.00179e-13,-9049.52,-89.2943], Tmin=(1386,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 506,
    label = "C8H132-6,SA",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {6,D} {19,S}
5  C u1 p0 c0 {1,S} {8,S} {18,S}
6  C u0 p0 c0 {3,S} {4,D} {20,S}
7  C u0 p0 c0 {2,S} {8,D} {17,S}
8  C u0 p0 c0 {5,S} {7,D} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.220018,0.0748621,-4.2124e-05,1.07414e-08,-8.6656e-13,16102.8,29.9517], Tmin=(300,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[21.6167,0.0312261,-1.0664e-05,1.6541e-09,-9.59112e-14,8033.85,-87.2194], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 507,
    label = "C8H132-6,PA",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {6,D} {17,S}
5  C u0 p0 c0 {1,S} {7,D} {16,S}
6  C u0 p0 c0 {3,S} {4,D} {18,S}
7  C u0 p0 c0 {5,D} {8,S} {19,S}
8  C u1 p0 c0 {7,S} {20,S} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.10512,0.077015,-4.48891e-05,1.19517e-08,-1.04378e-12,17271.3,32.2059], Tmin=(300,'K'), Tmax=(1378,'K')),
            NASAPolynomial(coeffs=[22.9294,0.0297187,-1.00712e-05,1.55505e-09,-8.9913e-14,8779.76,-92.4517], Tmin=(1378,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 508,
    label = "C8H132-6,SAO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {12,S}
3  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {8,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {7,D} {20,S}
6  C u0 p0 c0 {2,S} {8,D} {21,S}
7  C u0 p0 c0 {3,S} {5,D} {19,S}
8  C u0 p0 c0 {4,S} {6,D} {22,S}
9  O u1 p2 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.34169,0.0749918,-4.18383e-05,1.06108e-08,-8.96488e-13,5244.58,18.6128], Tmin=(300,'K'), Tmax=(1381,'K')),
            NASAPolynomial(coeffs=[25.4268,0.0310422,-1.08046e-05,1.69717e-09,-9.92702e-14,-3286.42,-102.873], Tmin=(1381,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 509,
    label = "C8H132-6,PAO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {7,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {8,S} {13,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {7,D} {20,S}
6  C u0 p0 c0 {2,S} {8,D} {21,S}
7  C u0 p0 c0 {3,S} {5,D} {19,S}
8  C u0 p0 c0 {4,S} {6,D} {22,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u1 p2 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.30808,0.0580374,-1.75638e-05,-2.70888e-09,1.61702e-12,7078.39,6.29345], Tmin=(300,'K'), Tmax=(2014,'K')),
            NASAPolynomial(coeffs=[19.9392,0.0379082,-1.37893e-05,2.23771e-09,-1.34044e-13,1429.81,-70.7923], Tmin=(2014,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 510,
    label = "C7H111-5,1P",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {5,D} {15,S}
5  C u0 p0 c0 {3,S} {4,D} {16,S}
6  C u0 p0 c0 {2,S} {7,D} {17,S}
7  C u1 p0 c0 {6,D} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.816832,0.0656745,-4.14491e-05,1.32235e-08,-1.6929e-12,32764.6,27.5443], Tmin=(300,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[19.1916,0.0255013,-8.65882e-06,1.33797e-09,-7.73785e-14,26094.6,-72.1388], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 511,
    label = "L-C6H4",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,T}
4  C u0 p0 c0 {3,T} {5,S}
5  C u0 p0 c0 {4,S} {6,T}
6  C u0 p0 c0 {5,T} {10,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.295902,0.0580533,-6.77668e-05,4.33768e-08,-1.14189e-11,60001.4,22.319], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.7152,0.0138397,-4.37654e-06,3.15416e-10,4.6619e-14,57031.1,-39.4646], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 512,
    label = "C-C6H4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,D} {6,S} {9,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {6,T}
6  C u0 p0 c0 {3,S} {5,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.09913,0.0540306,-4.0839e-05,1.07388e-08,9.80785e-13,52205.7,37.4152], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.8492,0.00788079,1.82438e-06,-2.11692e-09,3.746e-13,47446.3,-50.405], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 513,
    label = "C6H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,D} {7,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {5,S}
4 C u1 p0 c0 {1,D} {8,S}
5 C u0 p0 c0 {3,S} {6,T}
6 C u0 p0 c0 {5,T} {9,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.17906,0.0555474,-7.30762e-05,5.20767e-08,-1.5047e-11,85647.3,19.1792], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.81883,0.0279334,-1.78254e-05,5.37025e-09,-6.17076e-13,85188.2,-0.921478], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 514,
    label = "C6H2",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 C u0 p0 c0 {1,S} {5,T}
4 C u0 p0 c0 {2,S} {6,T}
5 C u0 p0 c0 {3,T} {7,S}
6 C u0 p0 c0 {4,T} {8,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.59326,0.0805301,-0.000148006,1.33e-07,-4.53323e-11,83273.2,27.9809], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.2263,0.00739043,-2.27154e-06,2.58752e-10,-5.53567e-15,80565.3,-41.2012], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 515,
    label = "C6H6",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {6,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {8,S}
3  C u0 p0 c0 {2,B} {4,B} {9,S}
4  C u0 p0 c0 {3,B} {5,B} {10,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {1,B} {5,B} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.504819,0.0185021,7.38346e-05,-1.18136e-07,5.0721e-11,8552.48,21.6413], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.081,0.0207177,-7.52146e-06,1.22321e-09,-7.36091e-14,4306.41,-40.0413], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 516,
    label = "FULVENE",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,D}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,D} {5,S} {8,S}
5  C u0 p0 c0 {3,D} {4,S} {9,S}
6  C u0 p0 c0 {1,D} {11,S} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.718132,0.0379343,1.13988e-05,-4.13335e-08,1.80559e-11,24223.8,27.8557], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.1035,0.0206007,-7.53022e-06,1.23887e-09,-7.5416e-14,20361.8,-36.6652], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 517,
    label = "C6H5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {8,S}
2  C u0 p0 c0 {1,B} {4,B} {7,S}
3  C u0 p0 c0 {1,B} {5,B} {9,S}
4  C u0 p0 c0 {2,B} {6,B} {10,S}
5  C u0 p0 c0 {3,B} {6,B} {11,S}
6  C u1 p0 c0 {4,B} {5,B}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.210307,0.0204746,5.89743e-05,-1.01534e-07,4.47106e-11,39546.9,25.291], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.8445,0.0173212,-6.29233e-06,1.0237e-09,-6.16217e-14,35559.8,-35.3735], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 518,
    label = "C6H5OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {8,S}
3  C u0 p0 c0 {1,B} {6,B} {12,S}
4  C u0 p0 c0 {2,B} {5,B} {9,S}
5  C u0 p0 c0 {4,B} {6,B} {10,S}
6  C u0 p0 c0 {3,B} {5,B} {11,S}
7  O u0 p2 c0 {1,S} {13,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.99165,0.0703857,-6.34401e-05,2.91549e-08,-5.30707e-12,14132,42.0143], Tmin=(300,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[16.7078,0.0162326,-5.4797e-06,8.4351e-10,-4.86562e-14,8142.43,-60.8347], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 519,
    label = "C6H5OOH",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {14,S}
3  C u0 p0 c0 {1,S} {4,B} {5,B}
4  C u0 p0 c0 {3,B} {6,B} {9,S}
5  C u0 p0 c0 {3,B} {8,B} {13,S}
6  C u0 p0 c0 {4,B} {7,B} {10,S}
7  C u0 p0 c0 {6,B} {8,B} {11,S}
8  C u0 p0 c0 {5,B} {7,B} {12,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.03106,0.0796102,-7.21655e-05,3.27611e-08,-5.85584e-12,-3109.73,45.4325], Tmin=(300,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[19.2317,0.0163155,-5.53449e-06,8.5506e-10,-4.94584e-14,-10197.1,-76.1674], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 520,
    label = "C6H5OH",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {13,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {8,S}
4  C u0 p0 c0 {2,B} {7,B} {12,S}
5  C u0 p0 c0 {3,B} {6,B} {9,S}
6  C u0 p0 c0 {5,B} {7,B} {10,S}
7  C u0 p0 c0 {4,B} {6,B} {11,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.69565,0.0522713,-7.20241e-06,-3.58596e-08,2.04491e-11,-13284.1,32.5422], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.9121,0.0183781,-6.19831e-06,9.19832e-10,-4.92096e-14,-18375.2,-55.9241], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 521,
    label = "C6H5O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {6,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {8,S}
3  C u0 p0 c0 {2,B} {4,B} {9,S}
4  C u0 p0 c0 {3,B} {5,B} {10,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {1,B} {5,B} {12,S}
7  O u1 p2 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.466204,0.0413444,1.32413e-05,-5.72873e-08,2.89764e-11,4778.58,27.699], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.7222,0.0174689,-6.35505e-06,1.03492e-09,-6.23411e-14,287.275,-48.8182], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 522,
    label = "C6H4OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {4,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {9,S}
3  C u0 p0 c0 {2,B} {5,B} {8,S}
4  C u0 p0 c0 {1,B} {6,B} {10,S}
5  C u0 p0 c0 {3,B} {6,B} {11,S}
6  C u1 p0 c0 {4,B} {5,B}
7  O u0 p2 c0 {1,S} {12,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.99875,0.0859063,-9.12526e-05,4.72276e-08,-9.35577e-12,17862.2,49.9931], Tmin=(300,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[17.3188,0.0136367,-4.68316e-06,7.29071e-10,-4.23805e-14,11499,-68.9987], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 523,
    label = "OC6H4OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {6,B} {11,S}
3  C u0 p0 c0 {1,B} {4,B} {12,S}
4  C u0 p0 c0 {3,B} {5,B} {8,S}
5  C u0 p0 c0 {4,B} {6,B} {9,S}
6  C u0 p0 c0 {2,B} {5,B} {10,S}
7  O u0 p2 c0 {1,S} {13,S}
8  O u1 p2 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.02206,0.109403,-0.000123489,6.56287e-08,-1.31528e-11,-15594.9,57.2175], Tmin=(300,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[22.2718,0.0121039,-4.1843e-06,6.54475e-10,-3.81747e-14,-23482.8,-96.1035], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 524,
    label = "O-C6H4O2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,D}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {6,S} {12,S}
6  C u0 p0 c0 {1,S} {5,S} {8,D}
7  O u0 p2 c0 {1,D}
8  O u0 p2 c0 {6,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.3618,0.0686058,-6.3913e-05,3.06903e-08,-5.97358e-12,-12670.4,35.3724], Tmin=(270,'K'), Tmax=(1370,'K')),
            NASAPolynomial(coeffs=[12.3614,0.0240491,-1.16529e-05,2.71333e-09,-2.47593e-13,-16708,-40.0311], Tmin=(1370,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (270,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 525,
    label = "P-C6H4O2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,D}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {8,D}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  C u0 p0 c0 {1,S} {5,D} {12,S}
7  O u0 p2 c0 {1,D}
8  O u0 p2 c0 {4,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.4317,0.0687938,-6.41383e-05,3.08127e-08,-5.99832e-12,-16569.7,34.8309], Tmin=(270,'K'), Tmax=(1370,'K')),
            NASAPolynomial(coeffs=[12.3424,0.0240613,-1.16565e-05,2.71394e-09,-2.47643e-13,-20618.5,-40.8244], Tmin=(1370,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (270,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 526,
    label = "O-OC6H5OJ",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {9,D}
4  C u0 p0 c0 {2,D} {6,S} {11,S}
5  C u0 p0 c0 {3,S} {6,D} {13,S}
6  C u0 p0 c0 {4,S} {5,D} {12,S}
7  O u1 p2 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.65459,0.0717179,-6.31552e-05,2.81133e-08,-4.97463e-12,6452.83,38.1123], Tmin=(300,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[18.4626,0.0157607,-5.44671e-06,8.51766e-10,-4.9676e-14,-172.77,-72.8742], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 527,
    label = "P-OC6H5OJ",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,D} {6,S} {12,S}
5  C u0 p0 c0 {3,D} {6,S} {13,S}
6  C u0 p0 c0 {4,S} {5,S} {11,D}
7  O u1 p2 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {6,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.29683,0.0727366,-6.36158e-05,2.80684e-08,-4.92279e-12,6734.02,40.935], Tmin=(300,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[18.28,0.0159281,-5.50765e-06,8.6165e-10,-5.02678e-14,-62.5908,-72.5809], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 528,
    label = "P-C6H3O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,D}
2  O u0 p2 c0 {6,D}
3  C u0 p0 c0 {4,S} {5,D} {9,S}
4  C u0 p0 c0 {1,D} {3,S} {7,S}
5  C u0 p0 c0 {3,D} {6,S} {10,S}
6  C u0 p0 c0 {2,D} {5,S} {8,S}
7  C u0 p0 c0 {4,S} {8,D} {11,S}
8  C u1 p0 c0 {6,S} {7,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.57852,0.0655376,-6.50309e-05,3.32027e-08,-6.86666e-12,15175,33.1519], Tmin=(270,'K'), Tmax=(1290,'K')),
            NASAPolynomial(coeffs=[12.2964,0.0215055,-1.07516e-05,2.57528e-09,-2.41024e-13,11542.9,-37.2584], Tmin=(1290,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (270,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 529,
    label = "C5H6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  C u0 p0 c0 {3,D} {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.86109,0.014804,7.21089e-05,-1.13381e-07,4.869e-11,14801.8,21.3535], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.97578,0.0189055,-6.84115e-06,1.10993e-09,-6.66802e-14,11081.7,-32.2095], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 530,
    label = "C5H5",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {1,S} {4,D} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.97555,0.0741371,-0.000111803,9.04629e-08,-2.81e-11,30176.9,36.7154], Tmin=(298.15,'K'), Tmax=(969.35,'K')),
            NASAPolynomial(coeffs=[1.33676,0.0324794,-1.67588e-05,4.03514e-09,-3.70739e-13,30073.1,16.0316], Tmin=(969.35,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (298.15,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 531,
    label = "C5H6-L",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,T}
5  C u0 p0 c0 {4,T} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58448,0.032446,-1.70151e-05,4.22716e-09,-4.18453e-13,27651.5,9.60644], Tmin=(300,'K'), Tmax=(1372,'K')),
            NASAPolynomial(coeffs=[12.9601,0.0148954,-5.23623e-06,8.27916e-10,-4.86465e-14,23818.1,-42.5312], Tmin=(1372,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 532,
    label = "C#CCVCCJ",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {6,S}
2  C u0 p0 c0 {1,D} {4,S} {7,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {5,T}
5  C u0 p0 c0 {4,T} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.616144,0.0506467,-4.48562e-05,2.02459e-08,-3.64542e-12,47153.2,27.1623], Tmin=(300,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[14.1231,0.0114233,-3.95851e-06,6.20129e-10,-3.62098e-14,42515.8,-50.2943], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 533,
    label = "C5H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u1 p0 c0 {2,S} {5,S} {10,S}
4  C u0 p0 c0 {1,S} {5,D} {11,S}
5  C u0 p0 c0 {3,S} {4,D} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.75118,0.0606462,-4.0126e-05,1.22052e-08,-1.3346e-12,20136.5,56.2695], Tmin=(300,'K'), Tmax=(1377,'K')),
            NASAPolynomial(coeffs=[13.663,0.0168061,-5.98747e-06,9.55341e-10,-5.64952e-14,12723.9,-54.6331], Tmin=(1377,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 534,
    label = "CVCCJCVC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {4,S} {6,S}
3  C u0 p0 c0 {1,S} {5,D} {8,S}
4  C u1 p0 c0 {2,S} {9,S} {10,S}
5  C u0 p0 c0 {3,D} {11,S} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.94596,0.0568784,-4.31336e-05,1.6817e-08,-2.67926e-12,23515.7,39.8189], Tmin=(300,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[14.0879,0.0162399,-5.64769e-06,8.86858e-10,-5.18699e-14,17679.9,-51.3735], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 535,
    label = "CVCCJCVCOH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {1,D} {5,S} {7,S}
4  C u0 p0 c0 {2,D} {6,S} {10,S}
5  C u1 p0 c0 {3,S} {11,S} {12,S}
6  O u0 p2 c0 {4,S} {13,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.91175,0.0669362,-5.71603e-05,2.48754e-08,-4.33244e-12,1964.42,41.7454], Tmin=(300,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[16.7466,0.0158357,-5.44955e-06,8.49881e-10,-4.94743e-14,-4309.73,-61.9379], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 536,
    label = "CVCCVCCOH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {12,S} {13,S}
6  O u0 p2 c0 {1,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.531488,0.0606984,-4.815e-05,2.00308e-08,-3.38987e-12,-10330.1,30.7961], Tmin=(300,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[16.308,0.0179958,-6.03116e-06,9.23992e-10,-5.31254e-14,-15820.5,-58.4137], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 537,
    label = "C5H5OH",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3  C u0 p0 c0 {2,S} {5,D} {8,S}
4  C u0 p0 c0 {2,S} {6,D} {9,S}
5  C u0 p0 c0 {3,D} {6,S} {10,S}
6  C u0 p0 c0 {4,D} {5,S} {11,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.26822,0.0662447,-5.68494e-05,2.46859e-08,-4.26821e-12,-5755.81,44.7963], Tmin=(300,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[15.3433,0.0150754,-5.13554e-06,7.95808e-10,-4.61312e-14,-11964.5,-58.5204], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 538,
    label = "C5H5O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  C u0 p0 c0 {3,D} {4,S} {11,S}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.83113,0.0567277,-4.44757e-05,1.74924e-08,-2.76005e-12,20499.2,36.9634], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[14.8323,0.0140483,-4.92302e-06,7.77041e-10,-4.56104e-14,14552.4,-57.3228], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 539,
    label = "C5H4OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {6,S}
2  C u1 p0 c0 {1,S} {5,S} {10,S}
3  C u0 p0 c0 {1,D} {4,S} {7,S}
4  C u0 p0 c0 {3,S} {5,D} {8,S}
5  C u0 p0 c0 {2,S} {4,D} {9,S}
6  O u0 p2 c0 {1,S} {11,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.28398,0.0490299,-1.35844e-05,-2.92984e-08,1.90821e-11,6373.65,30.8074], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.3741,0.0151996,-5.45685e-06,8.80945e-10,-5.27493e-14,2203.58,-45.9569], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 540,
    label = "C5H4O",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {6,S}
3  C u0 p0 c0 {2,S} {4,D} {7,S}
4  C u0 p0 c0 {3,D} {5,S} {8,S}
5  C u0 p0 c0 {4,S} {6,D} {9,S}
6  C u0 p0 c0 {2,S} {5,D} {10,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.264576,0.0334874,1.67738e-06,-2.96207e-08,1.54431e-11,5111.59,23.541], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.0807,0.0161143,-5.83315e-06,9.46759e-10,-5.68972e-14,1943.65,-29.4522], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 541,
    label = "C5H3O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,D} {5,S} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {8,S}
4 C u0 p0 c0 {1,D} {3,S} {6,S}
5 C u0 p0 c0 {2,S} {6,D} {9,S}
6 C u1 p0 c0 {4,S} {5,D}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.03243,0.0543937,-4.95018e-05,2.25524e-08,-4.10728e-12,33564.4,37.8375], Tmin=(300,'K'), Tmax=(1500,'K')),
            NASAPolynomial(coeffs=[11.9962,0.0134287,-5.90045e-06,1.22554e-09,-9.86115e-14,28959.2,-40.7548], Tmin=(1500,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 542,
    label = "CJVCCVCCVO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {6,S}
2  C u0 p0 c0 {1,D} {4,S} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {8,S}
4  C u0 p0 c0 {2,S} {9,D} {10,S}
5  C u1 p0 c0 {3,D} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  O u0 p2 c0 {4,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.506629,0.0604672,-5.97397e-05,2.96804e-08,-5.7624e-12,24276.6,28.2994], Tmin=(300,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[16.2361,0.0118297,-4.11454e-06,6.46027e-10,-3.77768e-14,19350,-58.3499], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 543,
    label = "CVCCVCCJVO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {5,S} {8,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  C u1 p0 c0 {3,S} {11,D}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.218492,0.05921,-5.89241e-05,2.97412e-08,-5.85245e-12,12060.1,25.5969], Tmin=(300,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[15.3178,0.0127353,-4.35883e-06,6.76913e-10,-3.92771e-14,7605.83,-54.36], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 544,
    label = "CJVCCVO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u0 p0 c0 {1,S} {5,D} {6,S}
3 C u1 p0 c0 {1,D} {7,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.46654,0.032339,-3.05588e-05,1.44082e-08,-2.65601e-12,17885,18.085], Tmin=(300,'K'), Tmax=(1402,'K')),
            NASAPolynomial(coeffs=[10.7483,0.00619823,-2.06131e-06,3.14419e-10,-1.8031e-14,15141,-30.1266], Tmin=(1402,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 545,
    label = "HOCVCCVO",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {4,S} {6,S}
3 C u0 p0 c0 {1,S} {7,D} {8,S}
4 O u0 p2 c0 {2,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 O u0 p2 c0 {3,D}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.01837,0.062654,-6.73359e-05,3.3943e-08,-6.48918e-12,-33136.8,31.8163], Tmin=(300,'K'), Tmax=(1413,'K')),
            NASAPolynomial(coeffs=[16.6505,0.00611745,-2.09081e-06,3.24986e-10,-1.88875e-14,-38218,-63.6795], Tmin=(1413,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 546,
    label = "HOCVCCJVO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 O u0 p2 c0 {2,S} {8,S}
4 C u1 p0 c0 {1,S} {7,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 O u0 p2 c0 {4,D}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.60727,0.0496011,-5.32301e-05,2.68393e-08,-5.13095e-12,-15881.5,19.4817], Tmin=(300,'K'), Tmax=(1414,'K')),
            NASAPolynomial(coeffs=[15.2721,0.00502586,-1.68409e-06,2.58391e-10,-1.48849e-14,-19850.7,-55.4642], Tmin=(1414,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 547,
    label = "OC5H7O",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,D}
2  O u0 p2 c0 {7,D}
3  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
5  C u1 p0 c0 {3,S} {7,S} {12,S}
6  C u0 p0 c0 {1,D} {4,S} {13,S}
7  C u0 p0 c0 {2,D} {5,S} {14,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.88395,0.0403401,-1.97774e-05,3.68904e-09,-3.40202e-14,-23529.6,9.9707], Tmin=(300,'K'), Tmax=(1375,'K')),
            NASAPolynomial(coeffs=[16.5417,0.0186678,-6.44836e-06,1.00788e-09,-5.87522e-14,-28201.7,-54.7258], Tmin=(1375,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 548,
    label = "OC4H6O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,D} {11,S}
4  C u0 p0 c0 {2,S} {10,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.21629,0.0357423,-2.04226e-05,5.63821e-09,-5.88889e-13,-37205.6,10.2815], Tmin=(300,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[14.1895,0.0153346,-5.24595e-06,8.14655e-10,-4.72759e-14,-41000.2,-44.3772], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 549,
    label = "OC4H5O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  C u1 p0 c0 {2,S} {11,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.60551,0.0330499,-2.13102e-05,7.37021e-09,-1.08289e-12,-18546.1,10.1599], Tmin=(300,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[13.2139,0.0137339,-4.6264e-06,7.10941e-10,-4.09538e-14,-21653.5,-36.4185], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 550,
    label = "O2CCHOOJ",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {5,S} {7,S}
2 O u0 p2 c0 {5,D}
3 O u1 p2 c0 {6,S}
4 O u0 p2 c0 {6,D}
5 C u0 p0 c0 {1,S} {2,D} {6,S}
6 C u0 p0 c0 {3,S} {4,D} {5,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.91498,0.00860572,5.24417e-07,-2.79301e-09,7.62963e-13,-34086.8,-8.72978], Tmin=(300,'K'), Tmax=(1682,'K')),
            NASAPolynomial(coeffs=[10.9911,0.00746986,-2.75568e-06,4.51353e-10,-2.72109e-14,-35133.5,-21.1652], Tmin=(1682,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 551,
    label = "C7H6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,D}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,D} {5,S} {9,S}
5  C u0 p0 c0 {3,D} {4,S} {10,S}
6  C u0 p0 c0 {7,D} {12,S} {13,S}
7  C u0 p0 c0 {1,D} {6,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.96407,0.074075,-6.68009e-05,3.06822e-08,-5.59259e-12,40857.5,41.6089], Tmin=(300,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[17.0565,0.0167767,-5.75638e-06,8.95749e-10,-5.20575e-14,34393,-68.351], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 552,
    label = "C7H5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {6,S}
2  C u1 p0 c0 {1,S} {5,S} {11,S}
3  C u0 p0 c0 {1,D} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {2,S} {4,D} {10,S}
6  C u0 p0 c0 {1,S} {7,T}
7  C u0 p0 c0 {6,T} {12,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.77568,0.069721,-6.63891e-05,3.18329e-08,-5.98041e-12,55326.1,37.3111], Tmin=(300,'K'), Tmax=(1404,'K')),
            NASAPolynomial(coeffs=[16.5644,0.0144569,-4.91369e-06,7.5974e-10,-4.39557e-14,49636.5,-62.9487], Tmin=(1404,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 553,
    label = "O-O2C6H4CH3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {5,B} {6,B}
5  C u0 p0 c0 {1,S} {4,B} {7,B}
6  C u0 p0 c0 {4,B} {8,B} {13,S}
7  C u0 p0 c0 {5,B} {9,B} {16,S}
8  C u0 p0 c0 {6,B} {9,B} {14,S}
9  C u0 p0 c0 {7,B} {8,B} {15,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.17635,0.0932723,-8.64518e-05,4.02042e-08,-7.33446e-12,11069.9,51.5569], Tmin=(300,'K'), Tmax=(1408,'K')),
            NASAPolynomial(coeffs=[21.2862,0.0193021,-6.48485e-06,9.95147e-10,-5.72828e-14,3198.65,-86.0791], Tmin=(1408,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 554,
    label = "OC6H4CH2",
    molecule = 
"""
multiplicity 3
1  O u1 p2 c0 {4,S}
2  C u0 p0 c0 {3,B} {4,B} {8,S}
3  C u0 p0 c0 {2,B} {5,B} {9,S}
4  C u0 p0 c0 {1,S} {2,B} {7,B}
5  C u0 p0 c0 {3,B} {6,B} {10,S}
6  C u0 p0 c0 {5,B} {7,B} {11,S}
7  C u0 p0 c0 {4,B} {6,B} {12,S}
8  C u1 p0 c0 {2,S} {13,S} {14,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.62198,0.0514918,-6.11682e-06,-2.88887e-08,1.4512e-11,4442.41,28.8225], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.4205,0.0270172,-1.09477e-05,2.02706e-09,-1.40757e-13,449.159,-41.0236], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 555,
    label = "C6H5CHOOCH3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {9,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,B} {5,B}
4  C u0 p0 c0 {3,B} {6,B} {15,S}
5  C u0 p0 c0 {3,B} {8,B} {19,S}
6  C u0 p0 c0 {4,B} {7,B} {16,S}
7  C u0 p0 c0 {6,B} {8,B} {17,S}
8  C u0 p0 c0 {5,B} {7,B} {18,S}
9  O u0 p2 c0 {1,S} {2,S}
10 O u1 p2 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.15081,0.0963086,-7.90362e-05,3.37294e-08,-5.86581e-12,6403.62,50.7485], Tmin=(300,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[23.9389,0.0255802,-8.93645e-06,1.40728e-09,-8.24626e-14,-2904.83,-98.4084], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 556,
    label = "C6H5CH2CH2OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {4,B} {5,B}
4  C u0 p0 c0 {3,B} {6,B} {14,S}
5  C u0 p0 c0 {3,B} {8,B} {18,S}
6  C u0 p0 c0 {4,B} {7,B} {15,S}
7  C u0 p0 c0 {6,B} {8,B} {16,S}
8  C u0 p0 c0 {5,B} {7,B} {17,S}
9  O u0 p2 c0 {2,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.97718,0.0909239,-7.22332e-05,3.00778e-08,-5.14216e-12,7870.41,45.31], Tmin=(300,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[23.2196,0.0260544,-9.06849e-06,1.42451e-09,-8.33255e-14,-930.561,-94.1996], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 557,
    label = "C14H12O",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {7,B} {8,B}
4  C u0 p0 c0 {6,S} {9,B} {10,B}
5  C u0 p0 c0 {6,S} {11,B} {12,B}
6  C u0 p0 c0 {1,D} {4,S} {5,S}
7  C u0 p0 c0 {3,B} {9,B} {19,S}
8  C u0 p0 c0 {3,B} {10,B} {22,S}
9  C u0 p0 c0 {4,B} {7,B} {20,S}
10 C u0 p0 c0 {4,B} {8,B} {21,S}
11 C u0 p0 c0 {5,B} {13,B} {23,S}
12 C u0 p0 c0 {5,B} {15,B} {27,S}
13 C u0 p0 c0 {11,B} {14,B} {24,S}
14 C u0 p0 c0 {13,B} {15,B} {25,S}
15 C u0 p0 c0 {12,B} {14,B} {26,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {13,S}
25 H u0 p0 c0 {14,S}
26 H u0 p0 c0 {15,S}
27 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.56374,0.144801,-0.000113795,4.50883e-08,-7.17649e-12,-2005.6,74.6679], Tmin=(300,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[34.8141,0.0367954,-1.28283e-05,2.01784e-09,-1.18159e-13,-16866.9,-161.938], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 558,
    label = "IND",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,B} {6,B}
3  C u0 p0 c0 {2,B} {5,S} {7,B}
4  C u0 p0 c0 {1,S} {5,D} {12,S}
5  C u0 p0 c0 {3,S} {4,D} {13,S}
6  C u0 p0 c0 {2,B} {9,B} {17,S}
7  C u0 p0 c0 {3,B} {8,B} {14,S}
8  C u0 p0 c0 {7,B} {9,B} {15,S}
9  C u0 p0 c0 {6,B} {8,B} {16,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.28231,0.0911988,-6.98829e-05,2.68064e-08,-4.09653e-12,18457.6,59.0251], Tmin=(300,'K'), Tmax=(1398,'K')),
            NASAPolynomial(coeffs=[20.565,0.0240328,-8.27638e-06,1.29145e-09,-7.52115e-14,9123.66,-89.5736], Tmin=(1398,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 559,
    label = "C10H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u1 p0 c0 {1,S} {5,S} {6,S}
3  C u0 p0 c0 {1,S} {7,D} {12,S}
4  C u0 p0 c0 {1,S} {8,D} {13,S}
5  C u0 p0 c0 {2,S} {9,D} {15,S}
6  C u0 p0 c0 {2,S} {10,D} {16,S}
7  C u0 p0 c0 {3,D} {10,S} {18,S}
8  C u0 p0 c0 {4,D} {9,S} {19,S}
9  C u0 p0 c0 {5,D} {8,S} {14,S}
10 C u0 p0 c0 {6,D} {7,S} {17,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.42912,0.0879983,-5.68391e-05,1.22282e-08,8.4745e-13,27623,22.5328], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[24.2294,0.023703,-7.09346e-06,1.03581e-09,-6.01752e-14,19509.9,-118.237], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 560,
    label = "C10H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {7,D} {13,S}
4  C u0 p0 c0 {1,S} {8,D} {14,S}
5  C u0 p0 c0 {2,S} {9,D} {15,S}
6  C u0 p0 c0 {2,S} {10,D} {16,S}
7  C u0 p0 c0 {3,D} {10,S} {17,S}
8  C u0 p0 c0 {4,D} {9,S} {18,S}
9  C u0 p0 c0 {5,D} {8,S} {19,S}
10 C u0 p0 c0 {6,D} {7,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.29108,0.0981011,-6.98931e-05,2.36468e-08,-3.00135e-12,12524,30.0159], Tmin=(300,'K'), Tmax=(1388,'K')),
            NASAPolynomial(coeffs=[27.5025,0.0253421,-8.65099e-06,1.34349e-09,-7.80291e-14,1576.19,-140.867], Tmin=(1388,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 561,
    label = "C5H5CH3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {1,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {6,S} {13,S}
6  C u0 p0 c0 {4,D} {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.05214,0.0763737,-6.3462e-05,2.72515e-08,-4.72539e-12,10514.3,51.3368], Tmin=(300,'K'), Tmax=(1399,'K')),
            NASAPolynomial(coeffs=[15.846,0.0200903,-6.93497e-06,1.0834e-09,-6.31319e-14,3428.21,-64.4405], Tmin=(1399,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 562,
    label = "C9H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {4,S} {5,B}
2  C u0 p0 c0 {1,B} {3,S} {6,B}
3  C u1 p0 c0 {2,S} {7,S} {10,S}
4  C u0 p0 c0 {1,S} {7,D} {12,S}
5  C u0 p0 c0 {1,B} {8,B} {13,S}
6  C u0 p0 c0 {2,B} {9,B} {16,S}
7  C u0 p0 c0 {3,S} {4,D} {11,S}
8  C u0 p0 c0 {5,B} {9,B} {14,S}
9  C u0 p0 c0 {6,B} {8,B} {15,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.73685,0.103422,-9.23423e-05,3.75623e-08,-4.40605e-12,33164.1,62.8218], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.65598,0.0574808,-3.42871e-05,9.70279e-09,-1.05386e-12,30684.3,2.5768], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 563,
    label = "C9H6O",
    molecule = 
"""
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {3,B} {5,S} {6,B}
3  C u0 p0 c0 {2,B} {4,S} {7,B}
4  C u0 p0 c0 {1,D} {3,S} {8,S}
5  C u0 p0 c0 {2,S} {8,D} {12,S}
6  C u0 p0 c0 {2,B} {9,B} {13,S}
7  C u0 p0 c0 {3,B} {10,B} {16,S}
8  C u0 p0 c0 {4,S} {5,D} {11,S}
9  C u0 p0 c0 {6,B} {10,B} {14,S}
10 C u0 p0 c0 {7,B} {9,B} {15,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {10,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.53929,0.0969323,-8.17699e-05,2.96699e-08,-2.24993e-12,6888.84,54.0946], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.65659,0.0570056,-3.43174e-05,9.76177e-09,-1.06334e-12,4578.57,-0.703868], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 564,
    label = "NAPH",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {4,B}
2  C u0 p0 c0 {1,B} {5,B} {6,B}
3  C u0 p0 c0 {1,B} {8,B} {13,S}
4  C u0 p0 c0 {1,B} {9,B} {14,S}
5  C u0 p0 c0 {2,B} {10,B} {17,S}
6  C u0 p0 c0 {2,B} {7,B} {18,S}
7  C u0 p0 c0 {6,B} {8,B} {11,S}
8  C u0 p0 c0 {3,B} {7,B} {12,S}
9  C u0 p0 c0 {4,B} {10,B} {15,S}
10 C u0 p0 c0 {5,B} {9,B} {16,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.8412,0.109328,-9.50844e-05,4.1832e-08,-7.33414e-12,16816.4,58.6792], Tmin=(300,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[23.5898,0.0243824,-8.4757e-06,1.33051e-09,-7.77993e-14,6534.23,-112.134], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 565,
    label = "NAPH-",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {4,B}
2  C u0 p0 c0 {1,B} {5,B} {10,B}
3  C u0 p0 c0 {1,B} {8,B} {12,S}
4  C u0 p0 c0 {1,B} {6,B} {13,S}
5  C u0 p0 c0 {2,B} {7,B} {16,S}
6  C u0 p0 c0 {4,B} {7,B} {14,S}
7  C u0 p0 c0 {5,B} {6,B} {15,S}
8  C u0 p0 c0 {3,B} {9,B} {11,S}
9  C u0 p0 c0 {8,B} {10,B} {17,S}
10 C u1 p0 c0 {2,B} {9,B}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.02718,0.102925,-8.34272e-05,2.72135e-08,-7.2456e-13,50136.3,60.8902], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.22892,0.0631264,-3.80582e-05,1.08454e-08,-1.18343e-12,47840.1,5.82017], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 566,
    label = "NAPHV",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {5,B}
2  C u0 p0 c0 {1,B} {4,B} {8,B}
3  C u0 p0 c0 {1,B} {6,B} {12,S}
4  C u0 p0 c0 {2,B} {7,B} {15,S}
5  C u0 p0 c0 {1,B} {9,B} {11,S}
6  C u0 p0 c0 {3,B} {7,B} {13,S}
7  C u0 p0 c0 {4,B} {6,B} {14,S}
8  C u0 p0 c0 {2,B} {10,B} {17,S}
9  C u0 p0 c0 {5,B} {10,B} {16,S}
10 C u1 p0 c0 {8,B} {9,B}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.00769,0.103041,-8.38191e-05,2.76492e-08,-8.88842e-13,49974.1,60.7299], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.29951,0.0630133,-3.7976e-05,1.08181e-08,-1.18008e-12,47665.8,5.41216], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 567,
    label = "NAPHO",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {4,S}
2  C u0 p0 c0 {3,B} {5,B} {6,B}
3  C u0 p0 c0 {2,B} {4,B} {7,B}
4  C u0 p0 c0 {1,S} {3,B} {8,B}
5  C u0 p0 c0 {2,B} {9,B} {14,S}
6  C u0 p0 c0 {2,B} {10,B} {15,S}
7  C u0 p0 c0 {3,B} {11,B} {18,S}
8  C u0 p0 c0 {4,B} {9,B} {12,S}
9  C u0 p0 c0 {5,B} {8,B} {13,S}
10 C u0 p0 c0 {6,B} {11,B} {16,S}
11 C u0 p0 c0 {7,B} {10,B} {17,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.15176,0.0611355,3.20151e-05,-9.94285e-08,4.7999e-11,11405.9,32.5585], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[21.0591,0.0282563,-1.03329e-05,1.68867e-09,-1.01975e-13,4091.44,-88.4963], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 568,
    label = "FLUORENE",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {4,B} {6,B}
3  C u0 p0 c0 {1,S} {5,B} {7,B}
4  C u0 p0 c0 {2,B} {5,S} {8,B}
5  C u0 p0 c0 {3,B} {4,S} {9,B}
6  C u0 p0 c0 {2,B} {10,B} {19,S}
7  C u0 p0 c0 {3,B} {12,B} {20,S}
8  C u0 p0 c0 {4,B} {11,B} {18,S}
9  C u0 p0 c0 {5,B} {13,B} {23,S}
10 C u0 p0 c0 {6,B} {11,B} {16,S}
11 C u0 p0 c0 {8,B} {10,B} {17,S}
12 C u0 p0 c0 {7,B} {13,B} {21,S}
13 C u0 p0 c0 {9,B} {12,B} {22,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {12,S}
22 H u0 p0 c0 {13,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-11.2093,0.129848,-9.07013e-05,2.32288e-08,0,21942.7,74.8524], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[23.1613,0.0392129,-1.25432e-05,1.33504e-09,0,12310.3,-103.717], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 569,
    label = "C14H10",
    molecule = 
"""
1  C u0 p0 c0 {4,B} {5,B} {7,B}
2  C u0 p0 c0 {3,B} {5,B} {8,B}
3  C u0 p0 c0 {2,B} {6,B} {9,B}
4  C u0 p0 c0 {1,B} {6,B} {10,B}
5  C u0 p0 c0 {1,B} {2,B} {18,S}
6  C u0 p0 c0 {3,B} {4,B} {23,S}
7  C u0 p0 c0 {1,B} {12,B} {17,S}
8  C u0 p0 c0 {2,B} {13,B} {19,S}
9  C u0 p0 c0 {3,B} {14,B} {22,S}
10 C u0 p0 c0 {4,B} {11,B} {24,S}
11 C u0 p0 c0 {10,B} {12,B} {15,S}
12 C u0 p0 c0 {7,B} {11,B} {16,S}
13 C u0 p0 c0 {8,B} {14,B} {20,S}
14 C u0 p0 c0 {9,B} {13,B} {21,S}
15 H u0 p0 c0 {11,S}
16 H u0 p0 c0 {12,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {13,S}
21 H u0 p0 c0 {14,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.67061,0.130752,-0.000100533,3.78085e-08,-5.59154e-12,44756.3,69.8276], Tmin=(300,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[33.5906,0.0304,-1.0587e-05,1.66528e-09,-9.75499e-14,30467.7,-156.193], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 570,
    label = "C16H10",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {6,B}
2  C u0 p0 c0 {1,B} {4,B} {5,B}
3  C u0 p0 c0 {1,B} {7,B} {8,B}
4  C u0 p0 c0 {2,B} {9,B} {10,B}
5  C u0 p0 c0 {2,B} {11,B} {12,B}
6  C u0 p0 c0 {1,B} {13,B} {14,B}
7  C u0 p0 c0 {3,B} {15,B} {18,S}
8  C u0 p0 c0 {3,B} {9,B} {19,S}
9  C u0 p0 c0 {4,B} {8,B} {20,S}
10 C u0 p0 c0 {4,B} {16,B} {21,S}
11 C u0 p0 c0 {5,B} {16,B} {23,S}
12 C u0 p0 c0 {5,B} {13,B} {24,S}
13 C u0 p0 c0 {6,B} {12,B} {25,S}
14 C u0 p0 c0 {6,B} {15,B} {26,S}
15 C u0 p0 c0 {7,B} {14,B} {17,S}
16 C u0 p0 c0 {10,B} {11,B} {22,S}
17 H u0 p0 c0 {15,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {16,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {13,S}
26 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-10.6811,0.146535,-0.000103944,2.70645e-08,0,25271.5,69.9617], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[29.0747,0.0412338,-1.26077e-05,1.27454e-09,0,14168.7,-136.431], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

