#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "CH2O + C2H4 <=> C3H6O",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.66e+06,'cm^3/(mol*s)','*|/',5), n=1.65, Ea=(226.564,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 11,
    longDesc = 
"""
Converted to training reaction from rate rule: db_2H;mb_OC
""",
)

entry(
    index = 1,
    label = "CH2O + C2H3O <=> C3H5O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.2319,'cm^3/(mol*s)','*|/',5), n=3.416, Ea=(322.616,'kJ/mol'), T0=(1,'K'), Tmin=(600,'K'), Tmax=(2000,'K')),
    rank = 11,
    shortDesc = """MRH CBS-QB3 calculations with 1d h.r. corrections""",
    longDesc = 
"""
MRH CBS-QB3 calculations for the reverse of the reaction sequence *CH2-cycle(CH-CH2-O-O) => *CH2-O-O-CH=CH2 ==> CH2O + CH2CHO

Previous RMG estimate for this reaction was an "Average of average" estimate, in addition to RMG needing
to increase the estimated Ea by ~20 kcal/mol because the barrier was not greater than the endothermicity.
This reaction was of interest to MRH/MHS because the butanol model was sensitive to allyl+O2 => CH2O+CH2CHO.
The high-p limit kinetics were necessary to estimate a k(T,P) for this PES.

The kinetics correspond to the reaction CH2O+CH2CHO => *CH2-cycle(CH-CH2-O-O)

Reactant: 0 hindered rotors
TS: 0 hindered rotors were considered (the only low-frequency torisonal mode corresponded to
	a hindered rotation within the cycle; MRH did not think treating this as a 1-d separable
	hindered rotor was accurate)
Product: 1 hindered rotor was considered (the *CH2 torsion)

All external symmetry numbers were set equal to one, except for CH2O which was set to two.
MRH could not find a stable geometry for *CH2-O-O-CH=CH2 at the B3LYP/6-31G(d) level (the method/basis
used in the CBS-QB3 method), it would always optimize to CH2O + CH2CHO.  Furthermore, MRH did not run an
IRC for the TS, to confirm the TS would fall apart to CH2O + CH2CHO (instead of CH2-OO-CH=CH2), hence the lowest
ranking of "5" assigned to this rate coefficient.

The k(T) was calculated from 600 - 2000 K, in 200 K intervals, and the fitted Arrhenius expression from CanTherm was:
k(T) = 2.319e-01 * (T/1K)^3.416 * exp(-77.107 kcal/mol / RT) cm3/mol/s.

Converted to training reaction from rate rule: CH2CHO;mb_CO_2H
""",
)

entry(
    index = 2,
    label = "CH2O + C2H4<=> C3H6O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.05605e+06,'cm^3/(mol*s)'), n=1.86, Ea=(232.9,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 11,
    shortDesc = """Converted to training reaction from rate rule: db;doublebond""",
    longDesc = 
"""
Kinetics fitted from reverse direction using rate of 

C3H6O <=> C2H4 + CH2O, low or high pressure extrapolation with thermal excitation technique, taken from 

Zalotai, L. et al, Kinetics of gas phase decomposition of oxetan and oxetan-2,2-d2, Int. J. Chem. Kinet., 15, 505, 1983
http://kinetics.nist.gov/kinetics/Detail?id=1983ZAL/HUN505:1
""",
)

entry(
    index = 3,
    label = "CH2S + C2H4 <=> C3H6S",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.92e+10,'cm^3/(mol*s)'), n=0, Ea=(43.72,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 11,
    shortDesc = """Converted to training reaction from rate rule: CS;doublebond""",
)

entry(
    index = 4,
    label = "CH2O + C2H4 <=> C3H6O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.92e+10,'cm^3/(mol*s)'), n=0, Ea=(43.72,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 11,
    shortDesc = """Converted to training reaction from rate rule: CO;doublebond""",
)

entry(
    index = 5,
    label = "C2H2O + C2H4 <=> C4H6O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.92e+10,'cm^3/(mol*s)'), n=0, Ea=(43.72,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 11,
    shortDesc = """Converted to training reaction from rate rule: CCO;doublebond""",
)

