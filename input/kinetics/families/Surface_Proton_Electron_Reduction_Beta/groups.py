#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Proton_Electron_Reduction_Beta/groups"
shortDesc = u""
longDesc = u"""

   *1                        *1-*4H
   ||                        |
   *2  + *4H+ + *e-  ---->  *2
    |                       ||
  ~*3~                     ~*3~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m3) * 1
so k should be in (m3/mol/s).
"""

template(reactants=["Adsorbate", "Proton"], products=["Reduced"], ownReverse=False)

reverse = "Surface_Proton_Electron_Oxidation_Beta"

reactantNum = 2
productNum = 1
allowChargedSpecies = True
electrons = -1

recipe(actions=[
    ['LOSE_CHARGE', '*4', 1],
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['CHANGE_BOND', '*2', 1, '*3'],
    ['FORM_BOND', '*1', 1, '*4'],
])

entry(
    index = 1,
    label = "Adsorbate",
    group =
"""
1 *1 R!H u0 {2,[D,T]}
2 *2 R!H u0 {1,[D,T]} {3,[S,D]}
3 *3 X u0 {2,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Proton",
    group =
"""
1 *4 H+ u0 p0 c+1
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "CRX",
    group =
"""
1 *1 C u0 {2,[D,T]}
2 *2 R!H u0 {1,[D,T]} {3,[S,D]}
3 *3 X u0 {2,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "NRX",
    group =
"""
1 *1 N u0 {2,[D,T]}
2 *2 R!H u0 {1,[D,T]} {3,[S,D]}
3 *3 X u0 {2,[S,D]}
""",
    kinetics = None,
)


entry(
    index = 6,
    label = "ORX",
    group =
"""
1 *1 O u0 {2,D}
2 *2 R!H u0 {1,D} {3,[S,D]}
3 *3 X u0 {2,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "HN=N-X",
    group =
"""
1 *1 N u0 {2,D} {4,S}
2 *2 N u0 {1,D} {3,S}
3 *3 X u0 {2,S}
4    H u0 {1,S}
""",
    kinetics = None,
)


tree(
"""
L1: Adsorbate
    L2: CRX
    L2: ORX
    L2: NRX
        L3: HN=N-X

L1: Proton
"""
)
