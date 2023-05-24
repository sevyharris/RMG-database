#!/usr/bin/env python
# encoding: utf-8

name = "Rebrov_Pt111"
shortDesc = u""
longDesc = u"""
This library is built to import training reactions, based on:
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2
"""

entry(
    index = 1,
    label = "NH3 + X <=> NH3_X",
    kinetics = StickingCoefficient(
        A = 0.79731,  
        n = 0.0,
        Ea = (0, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = ((2e8 /atm)/(101325 Pa/atm)/s)*(2.483e-9(mol/cm^2))*sqrt(2*pi*(17(g/mol))*the molar gas constant*(298 kelvin))

This is R1 in Table 3 
""",
    metal = "Pt",
    facet = "111",
)

# entry(
#     index = 2,
#     label = "NH3_X <=> NH3 + X",
#     kinetics = SurfaceArrhenius(
#         A = (1.9E13, '1/s'),  
#         n = 0.0,
#         Ea = (96000, 'J/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_vdW""",
#     longDesc = u"""
# "Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
# Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
# https://doi.org/10.1016/S1385-8947(02)00068-2

# This is R2 in Table 3 
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 3,
    label = "O2 + X + X <=> O_X + O_X",
    kinetics = StickingCoefficient(
        A = 0.0235189884,   
        n = 0.0,
        Ea = (0, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""O2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = ((4.3e6 /atm)/(101325 Pa/atm)/s)*(2.483e-9(mol/cm^2))*sqrt(2*pi*(32(g/mol))*the molar gas constant*(298 kelvin))

This is R3 in Table 3 
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 4,
#     label = "O_X + O_X <=> O2 + X + X",
#     kinetics = SurfaceArrhenius(
#         A = (4.03E21, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (213200, 'J/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""O2 Surface_Adsorption_Dissociative""",
#     longDesc = u"""
# "Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
# Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
# https://doi.org/10.1016/S1385-8947(02)00068-2

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 1E13(1/s)/2.483E-9(mol/cm^2) = 4.03E21 cm^2/(mol*s)

# This is R4 in Table 3 
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 5,
    label = "NH3_X + O_X <=> NH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (6.85E23, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (157000, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.7E15(1/s)/2.483E-9(mol/cm^2) = 6.85E23 cm^2/(mol*s)

This is R5 in Table 1 
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 6,
    label = "NH2_X + O_X <=> NH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (4.03E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (96490, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1E13(1/s)/2.483E-9(mol/cm^2) = 4.03E21 cm^2/(mol*s)

This is R6 in Table 1 
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 7,
    label = "NH_X + O_X <=> N_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (4.03E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (58500, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1E13(1/s)/2.483E-9(mol/cm^2) = 4.03E21 cm^2/(mol*s)

This is R7 in Table 1 
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 8,
    label = "N_X + O_X <=> NO_X + X",
    kinetics = SurfaceArrhenius(
        A = (8.46E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (131000, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 2.1E13(1/s)/2.483E-9(mol/cm^2) = 8.46E21 cm^2/(mol*s)

This is L10 in Table 3 
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 9,
    label = "NH_X + O_X <=> NHO_X + X",
    kinetics = SurfaceArrhenius(
        A = (4.03E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (73000, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_Double_vdW""",
    longDesc = u"""
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1E13(1/s)/2.483E-9(mol/cm^2) = 4.03E21 cm^2/(mol*s)

This is R9 in Table 1 
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 10,
    label = "NHO_X + O_X <=> NO_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (8.05E23, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (118000, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 2E15(1/s)/2.483E-9(mol/cm^2) = 8.05E23 cm^2/(mol*s)

This is R10 in Table 1, it's from ref[52] where metal = Pt100.  
""",
    metal = "Pt",
    facet = "111",
)

#Reverse of index = 8
# entry(
#     index = 11,
#     label = "NO_X + X <=> N_X + O_X",
#     kinetics = SurfaceArrhenius(
#         A = (4.03E21, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (118000, 'J/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Nitrogen/51""",
#     longDesc = u"""
# "Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
# Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
# https://doi.org/10.1016/S1385-8947(02)00068-2

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 1E13(1/s)/2.483E-9(mol/cm^2) = 4.03E21 cm^2/(mol*s)

# This is L8 in Table 3 
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 12,
    label = "N_X + N_X <=> N2 + X + X",
    kinetics = SurfaceArrhenius( 
        A = (3.22E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (124000, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 8E12(1/s)/2.483E-9(mol/cm^2) = 3.22E21 cm^2/(mol*s)

This is L6 in Table 3 
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 13,
    label = "N_X + NO_X <=> N2O + X + X",
    kinetics = SurfaceArrhenius(
        A = (1.01E19, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (98900, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""doesn't match a family""",
    longDesc = u"""
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 2.5E10(1/s)/2.483E-9(mol/cm^2) = 1.01E19 cm^2/(mol*s)

This is L7 in Table 3
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 14,
    label = "N2O + X <=> N2 + O_X",
    kinetics = StickingCoefficient(
        A = 0.0160339874,
        n = 0,
        Ea = (72200, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = ((2.5e6/atm)/s)*(2.483e-9(mol/cm2))*sqrt(2*pi*(44(g/mol))*the molar gas constant*(298 kelvin))

This is L13 in Table 3 
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 15,
    label = "NO_X <=> NO + X",
    kinetics = SurfaceArrhenius(
        A = (1.5E13, '1/s'),  
        n = 0.0,
        Ea = (143000, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This is L12 in Table 3 
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 16,
    label = "NH_X + OH_X <=> N_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (4.03E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (46000, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1E13(1/s)/2.483E-9(mol/cm^2) = 4.03E21 cm^2/(mol*s)

This is R16 in Table 1 
""",
    metal = "Pt",
    facet = "111",
)

#reverse reaction of R18
entry(
    index = 17,
    label = "OH_X + OH_X <=> O_X + H2O + X",
    kinetics = SurfaceArrhenius(
        A = (4.03E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (113000, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1E13(1/s)/2.483E-9(mol/cm^2) = 4.03E21 cm^2/(mol*s)

This is L9 in Table 3 
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 18,
    label = "O_X + H2O_X <=> OH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (4.03E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (52700, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2
This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1E11(1/s)/2.483E-9(mol/cm^2) = 4.03E19 cm^2/(mol*s)
This is R18 in Table 1 
""",
    metal = "Pt",
    facet = "111",
)

#endothermic, and Deutschmann's paper: A=4.5E8, n=0, Ea=41800J/mol
# entry(
#    index = 19,
#    label = "H2O_X <=> H2O + X",
#    kinetics = SurfaceArrhenius(
#        A = (1E13, '1/s'),  
#        n = 0.0,
#        Ea = (40300, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Surface_Adsorption_vdW""",
#     longDesc = u"""
# "Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
# Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
# https://doi.org/10.1016/S1385-8947(02)00068-2

# This is R19 in Table 1 
# """,
# 	metal = "Pt",
#    facet = "111",
# )
