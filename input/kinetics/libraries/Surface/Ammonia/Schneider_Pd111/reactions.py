#!/usr/bin/env python
# encoding: utf-8

name = "Schneider_Pd111"
shortDesc = u""
longDesc = u"""
Primarily based on:
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029
"""

entry(
    index = 1,
    label = "O2 + X + X <=> O_X + O_X",
    kinetics = StickingCoefficient(
        A = 0.9975,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""O2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

Scitcking coefficient from Schneider_Pt111

This is reaction (1) in Table S3
""",
	metal = "Pd",
    facet = "111",
)

entry(
    index = 2,
    label = "NH3 + X <=> NH3_X",
   kinetics = StickingCoefficient(
       A = 1,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

Scitcking coefficient from Schneider_Pt111

This is reaction (2) in Table S3
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 3,
    label = "NH3_X +O_X <=> NH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (2.05E22, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (69472.8, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd111
revised from 2.05E21 to 2.05E22 based on the ammonia model

Ea = 0.72eV = 69472.8J/mol

This is reaction (3) in Table S3
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 4,
    label = "NH2_X +O_X <=> NH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (2.17E22, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (85876.1, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd111
A factor revised from 2.17E21 to 2.17E22 based on the ammonia model

Ea = 0.89eV = 85876.1J/mol

This is reaction (4) in Table S3
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 5,
    label = "NH_X + O_X <=> N_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (3.08E20, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (133156.2, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd111
A factor revised from 3.08E21 to 3.08E20 based on the ammonia model
Ea = 1.38eV = 133156.2J/mol

This is reaction (5) in Table S3
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 6,
    label = "NH3_X + OH_X <=> NH2_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (1.93E22, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (44385.4, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_Single_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd111
Ea = 0.46eV = 44385.4J/mol

This is reaction (6) in Table S3
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 7,
    label = "NH2_X + OH_X <=> NH_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (5.92E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (7719.2, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd111
Ea = 0.08eV = 7719.2J/mol

This is reaction (7) in Table S3
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 8,
    label = "NH_X + OH_X <=> N_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (2.33E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (46315.2, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd111
A factor revised from 2.33E21 to 2.33E20 based on the ammonia model
Ea = 0.48eV = 46315.2J/mol

This is reaction (8) in Table S3
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 9,
    label = "OH_X + OH_X <=> O_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (1.22E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (0, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd111

This is reaction (9) in Table S3
""",
    metal = "Pd",
    facet = "111",
)



#Endothermic, Deutschmann's paper: A=4.5E8, n=0, Ea=41800J/mol
# entry(
#     index = 10,
#     label = "H2O_X <=> H2O + X",
#     kinetics = SurfaceArrhenius(
#         A = (5.9E15, '1/s'),
#         n = 0.0,
#         Ea = (20262.9, 'J/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_vdW""",
#     longDesc = u"""
# "DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
# Hanyu Ma, and William F.Schneider
# Journal of Catalysis 383 (2020) 322–330
# https://doi.org/10.1016/j.jcat.2020.01.029
# Ea = 0.21eV = 20262.9J/mol
#
# This is reaction (10) in Table S3
# """,
#       metal = "Pd",
#       facet = "111",
# )

entry(
    index = 11,
    label = "N_X + N_X <=> N2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (3.63E21, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (208418.4, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd111

Ea = 2.16eV = 208418.4J/mol

This is reaction (11) in Table S3
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 12,
    label = "N_X + O_X <=> NO_X + X",
    kinetics = SurfaceArrhenius(
        A = (3.28E22, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (187190.6, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd111
A factor revised from 3.28E21 to 3.28E22 based on the ammonia model

Ea = 1.94eV = 187190.6J/mol

This is reaction (12) in Table S3
""",
    metal = "Pd",
    facet = "111",
)


entry(
    index = 13,
    label = "NO_X <=> NO + X",
    kinetics = SurfaceArrhenius(
        A = (2.6E12, '1/s'), #revise A=2.6E17 to A=2.6E12 and match the coverage plot 
        n = 0.0,
        Ea = (221927, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

Ea = 2.3eV = 221927J/mol

This is reaction (13) in Table S3
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 14,
    label = "N_X + NO_X <=> N2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (1.7E19, 'cm^2/(mol*s)'),   
        n = 0.0,
        Ea = (186225.7, 'J/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd111
A factor revised from 1.7E21 to 1.7E19 based on the ammonia model

Ea = 1.93eV = 186225.7J/mol

This is reaction (14) in Table S3
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 15,
    label = "N2O_X <=> N2O + X",
    kinetics = SurfaceArrhenius(
        A = (1.4E10, '1/s'),
        n = 0.0,
        Ea = (11578.8, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd111
A factor revised from 1.4E16 to A=1.4E10 based on the ammonia model,
this value is close to the value of Deutschmann's Nitrogen library and better match the models

Ea = 0.12eV = 11578.8J/mol

This is reaction (15) in Table S3
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 16,
    label = "NH3_X + X <=> NH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (3.74E20, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (104209.2, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd111

Ea = 1.08eV = 104209.2J/mol

This is reaction (1) in Table S5
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 17,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (3.38E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (85876.1, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd111

Ea = 0.89eV = 85876.1J/mol

This is reaction (2) in Table S5
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 18,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (3.56E20, 'cm^2/(mol*s)'), #revised from 3.56E21 to 3.56E20 based on the models
        n = 0.0,
        Ea = (113858.2, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd111

Ea = 1.18eV = 113858.2J/mol

This is reaction (3) in Table S5
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 19,
    label = "H_X + O_X <=> OH_X + X",
    kinetics = SurfaceArrhenius(
        A = (1.25E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (97454.9, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd111

Ea = 1.01eV = 97454.9J/mol

This is reaction (4) in Table S5
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 20,
    label = "H_X + OH_X <=> H2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (2E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (64648.3, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd111

Ea = 0.67eV = 64648.3J/mol

This is reaction (5) in Table S5
""",
    metal = "Pd",
    facet = "111",
)