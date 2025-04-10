#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/groups"
shortDesc = u""
longDesc = u"""
The reaction site *3 should be a triplet, otherwise it will react via the 1+2_Cycloaddition family instead.
"""

template(reactants=["R_R", "YJ"], products=["RJ_R_Y"], ownReverse=False)

reverse = "Beta_Scission"
reversible = True

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 0,
    label = "R_R",
    group =
"""
1 *1 R!H u0 {2,[D,T,B]}
2 *2 R!H u0 {1,[D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "YJ",
    group = "OR{HJ, Y_1centerquadrad, Y_1centertrirad, Y_1centerbirad, CJ, OJ, SJ, NJ, LiJ}",
    kinetics = None,
)

entry(
    index = 2,
    label = "Cb_Cb",
    group =
"""
1 *1 [Cb,Cbf] u0 {2,B}
2 *2 [Cb,Cbf] u0 {1,B}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "Cb-R!H_Cb",
    group =
"""
1 *1 [Cb,Cbf] u0 {2,B} {3,[S,B]} {4,B}
2 *2 [Cb,Cbf] u0 {1,B}
3    R!H      u0 {1,[S,B]}
4    [Cb,Cbf] u0 {1,B}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "Cb-R!H_Cb-R!H",
    group =
"""
1 *1 [Cb,Cbf] u0 {2,B} {3,B} {5,[S,B]}
2 *2 [Cb,Cbf] u0 {1,B} {4,B} {6,[S,B]}
3    [Cb,Cbf] u0 {1,B}
4    [Cb,Cbf] u0 {2,B}
5    R!H      u0 {1,[S,B]}
6    R!H      u0 {2,[S,B]}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "Cb-indeneDe_Cb-indeneNde",
    group =
"""
1 *1 Cb       u0 {2,B} {3,S} {6,B}
2 *2 Cb       u0 {1,B} {4,S} {7,B}
3    Cd       u0 {1,S} {5,D}
4    C        u0 {2,S} {5,S}
5    Cd       u0 {3,D} {4,S}
6    [Cb,Cbf] u0 {1,B}
7    [Cb,Cbf] u0 {2,B}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "Cb-indeneNde_Cb-indene_De",
    group =
"""
1 *2 Cb       u0 {2,B} {3,S} {6,B}
2 *1 Cb       u0 {1,B} {4,S} {7,B}
3    Cd       u0 {1,S} {5,D}
4    C        u0 {2,S} {5,S}
5    Cd       u0 {3,D} {4,S}
6    [Cb,Cbf] u0 {1,B}
7    [Cb,Cbf] u0 {2,B}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "Cb-benzofuranNde_Cb-benzofuranDe",
    group =
"""
1 *1 Cb       u0 {2,B} {3,S} {6,B}
2 *2 Cb       u0 {1,B} {4,S} {7,B}
3    O        u0 {1,S} {5,S}
4    C        u0 {2,S} {5,D}
5    C        u0 {3,S} {4,D}
6    [Cb,Cbf] u0 {1,B}
7    [Cb,Cbf] u0 {2,B}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "Cb-R!H_Cb-H",
    group =
"""
1 *1 [Cb,Cbf] u0 {2,B} {3,[S,B]} {5,B}
2 *2 [Cb,Cbf] u0 {1,B} {4,S}
3    R!H      u0 {1,[S,B]}
4    H        u0 {2,S}
5    [Cb,Cbf] u0 {1,B}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "Cb-C-cyclic_Cb-H",
    group =
"""
1 *1 [Cb,Cbf] u0 {2,B} {3,B} {4,[S,B]}
2 *2 Cb       u0 {1,B} {8,S}
3    [Cb,Cbf] u0 {1,B} {7,[S,B]}
4    C        u0 {1,[S,B]} {5,[S,D,T,B]}
5    C        u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    C        u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    C        u0 {3,[S,B]} {6,[S,D,T,B]}
8    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "Cbf-Cb-cyclic_Cb-H",
    group =
"""
1 *1 Cbf      u0 {2,B} {3,B} {4,B}
2 *2 Cb       u0 {1,B} {8,S}
3    Cbf      u0 {1,B} {7,B}
4    [Cb,Cbf] u0 {1,B} {5,B}
5    [Cb,Cbf] u0 {4,B} {6,B}
6    [Cb,Cbf] u0 {5,B} {7,B}
7    [Cb,Cbf] u0 {3,B} {6,B}
8    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "Cb-Cd_Cb-H",
    group =
"""
1 *1 Cb u0 {2,B} {3,S} {5,B}
2 *2 Cb u0 {1,B} {4,S}
3    Cd u0 {1,S}
4    H  u0 {2,S}
5    Cb u0 {1,B}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "Cb-Cs_Cb-H",
    group =
"""
1 *1 Cb u0 {2,B} {3,S} {5,B}
2 *2 Cb u0 {1,B} {4,S}
3    Cs u0 {1,S}
4    H  u0 {2,S}
5    Cb u0 {1,B}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "Cb-H_Cb",
    group =
"""
1 *1 Cb       u0 {2,B} {3,S}
2 *2 [Cb,Cbf] u0 {1,B}
3    H        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "Cb-H_Cb-R!H",
    group =
"""
1 *1 Cb       u0 {2,B} {3,S}
2 *2 [Cb,Cbf] u0 {1,B} {4,[S,B]} {5,B}
3    H        u0 {1,S}
4    R!H      u0 {2,[S,B]}
5    [Cb,Cbf] u0 {2,B}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "Cb-H_Cb-indeneNde",
    group =
"""
1    Cb u0 {2,B} {4,S}
2 *2 Cb u0 {1,B} {3,B} {5,S}
3 *1 Cb u0 {2,B} {7,S}
4    Cd u0 {1,S} {6,D}
5    C  u0 {2,S} {6,S}
6    Cd u0 {4,D} {5,S}
7    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "Cb-H_Cbf-Cb",
    group =
"""
1 *1 Cb       u0 {2,B} {3,S}
2 *2 Cbf      u0 {1,B} {4,B} {5,B}
3    H        u0 {1,S}
4    [Cb,Cbf] u0 {2,B}
5    [Cb,Cbf] u0 {2,B}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "Cb-H-Ortho_Cb-C",
    group =
"""
1 *1 Cb       u0 {2,B} {3,S}
2 *2 Cb       u0 {1,B} {4,S} {5,B}
3    H        u0 {1,S}
4    C        u0 {2,S}
5    [Cb,Cbf] u0 {2,B}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "Cb-H_Cb-H",
    group =
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {4,S}
3    H  u0 {1,S}
4    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "Cb-H-Meta_Cb-H",
    group =
"""
1 *1 Cb       u0 {2,B} {6,S}
2 *2 Cb       u0 {1,B} {3,B} {5,S}
3    [Cb,Cbf] u0 {2,B} {4,S}
4    R!H      u0 {3,S}
5    H        u0 {2,S}
6    H        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "Cb-H-Para_Cb-H",
    group =
"""
1 *1 Cb       u0 {2,B} {7,S}
2 *2 Cb       u0 {1,B} {4,B} {6,S}
3    [Cb,Cbf] u0 {4,B} {5,S}
4    [Cb,Cbf] u0 {2,B} {3,B}
5    R!H      u0 {3,S}
6    H        u0 {2,S}
7    H        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "Cb-H_Cb-H_o_ketene",
    group =
"""
1 *1 Cb  u0 {2,B} {3,B} {4,S}
2 *2 Cb  u0 {1,B} {5,S}
3    Cb  u0 {1,B} {6,S}
4    H   u0 {1,S}
5    H   u0 {2,S}
6    Cd  u0 {3,S} {7,D}
7    Cdd u0 {6,D} {8,D}
8    O   u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "Cd_R",
    group =
"""
1 *1 C   u0 {2,D}
2 *2 R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "Cdd_Od",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 O2d u0 {1,D}
3    R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "CO2",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 O2d u0 {1,D}
3    O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "Ck_O",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 O2d u0 {1,D}
3    C   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "C=S_O",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 O2d u0 {1,D}
3    S   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "Cdd_Od-N3d",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 O2d u0 {1,D}
3    N3d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "CO_O",
    group =
"""
1 *1 CO  u0 {2,D}
2 *2 O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "CO-HH_O",
    group =
"""
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "CO-NdH_O",
    group =
"""
1 *1 CO           u0 {2,D} {3,S} {4,S}
2 *2 O2d          u0 {1,D}
3    H            u0 {1,S}
4    [Cs,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "CO-CsH_O",
    group =
"""
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3    H   u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "CO-DeH_O",
    group =
"""
1 *1 CO                        u0 {2,D} {3,S} {4,S}
2 *2 O2d                       u0 {1,D}
3    H                         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "CO-CdH_O",
    group =
"""
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3    H   u0 {1,S}
4    Cd  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "CO-CtH_O",
    group =
"""
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3    H   u0 {1,S}
4    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "CO-NdNd_O",
    group =
"""
1 *1 CO           u0 {2,D} {3,S} {4,S}
2 *2 O2d          u0 {1,D}
3    [Cs,O2s,S2s] u0 {1,S}
4    [Cs,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "CO-CsCs_O",
    group =
"""
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "CO-DeNd_O",
    group =
"""
1 *1 CO                        u0 {2,D} {3,S} {4,S}
2 *2 O2d                       u0 {1,D}
3    [Cs,O2s,S2s]              u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "CO-CdCs_O",
    group =
"""
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3    Cs  u0 {1,S}
4    Cd  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "CO-CtCs_O",
    group =
"""
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3    Cs  u0 {1,S}
4    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "CO-DeDe_O",
    group =
"""
1 *1 CO                        u0 {2,D} {3,S} {4,S}
2 *2 O2d                       u0 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "Cdd_Sd",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 S2d u0 p2 {1,D}
3    R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "Cdd-Sd_Sd",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 S2d u0 p2 {1,D}
3    S2d u0 p2 {1,D}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "Cds_Cdd",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    R   ux {1,S}
4    R   ux {1,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "Cds_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    R   ux {1,S}
4    R   ux {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "Cds-HH_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "Cds-CsH_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    Cs  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "Cds-CsCs_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "Cds-OneDeH_Ca",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cdd                       u0 {1,D} {5,D}
3    H                         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    C                         u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "Cds-CtH_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    Ct  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "Cds-CbH_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    Cb  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "Cds-COH_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    CO  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "Cds-CdH_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    H   u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "Cds-C=SH_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    CS  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "Cds-OneDeCs_Ca",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cdd                       u0 {1,D} {5,D}
3    Cs                        u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    C                         u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "Cds-CtCs_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cs  u0 {1,S}
4    Ct  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "Cds-CbCs_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cs  u0 {1,S}
4    Cb  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "Cds-COCs_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cs  u0 {1,S}
4    CO  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "Cds-CdCs_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cs  u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "Cds-C=SCs_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cs  u0 {1,S}
4    CS  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "Cds-TwoDe_Ca",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    C                         u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "Cds-CtCt_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "Cds-CtCb_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    Cb  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "Cds-CtCO_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    CO  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "Cds-CbCb_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cb  u0 {1,S}
4    Cb  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "Cds-CbCO_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cb  u0 {1,S}
4    CO  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "Cds-COCO_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    CO  u0 {1,S}
4    CO  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "Cds-CdCt_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Ct  u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "Cds-CdCb_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cb  u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "Cds-CdCO_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "Cds-CtC=S_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    CS  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "Cds-CbC=S_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cb  u0 {1,S}
4    CS  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "Cds-COC=S_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    CO  u0 {1,S}
4    CS  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "Cds-CdCd_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    C   u0 {2,D}
6    C   u0 {3,D}
7    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "Cds-CdC=S_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "Cds-C=SC=S_Ca",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    CS  u0 {1,S}
4    CS  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "Cds_Ck",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    R   ux {1,S}
4    R   ux {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "Cds-HH_Ck",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "Cds-CsH_Ck",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    Cs  u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "Cds-CsCs_Ck",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "Cds-OneDeH_Ck",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cdd                       u0 {1,D} {5,D}
3    H                         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    O2d                       u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "Cds-OneDeCs_Ck",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cdd                       u0 {1,D} {5,D}
3    Cs                        u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    O2d                       u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "Cds-TwoDe_Ck",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    O2d                       u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "Cdd_Cds",
    group =
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D}
3    R   u0 {1,S}
4    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "Ca_Cds",
    group =
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    R   u0 {1,S}
4    R   u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "Ca_Cds-HH",
    group =
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "Ca-Cdd_Cds-HH",
    group =
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    Cdd u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "Ca_Cds-CsH",
    group =
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "Ca_Cds-CsCs",
    group =
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "Ca_Cds-OneDeH",
    group =
"""
1 *2 Cd                        u0 {2,D} {3,S} {4,S}
2 *1 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    H                         u0 {1,S}
5    C                         u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 90,
    label = "Ca_Cds-CtH",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    Ct  u0 {2,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 91,
    label = "Ca_Cds-CbH",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    Cb  u0 {2,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 92,
    label = "Ca_Cds-COH",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    CO  u0 {2,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 93,
    label = "Ca_Cds-CdH",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    Cd  u0 {2,S} {6,D}
5    H   u0 {2,S}
6    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 94,
    label = "Ca_Cds-C=SH",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    CS  u0 {2,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 95,
    label = "Ca_Cds-OneDeCs",
    group =
"""
1 *2 Cd                        u0 {2,D} {3,S} {4,S}
2 *1 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cs                        u0 {1,S}
5    C                         u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "Ca_Cds-CtCs",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    Ct  u0 {2,S}
5    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "Ca_Cds-CbCs",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    Cb  u0 {2,S}
5    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 98,
    label = "Ca_Cds-COCs",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    CO  u0 {2,S}
5    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 99,
    label = "Ca_Cds-CdCs",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    Cd  u0 {2,S} {6,D}
5    Cs  u0 {2,S}
6    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 100,
    label = "Ca_Cds-C=SCs",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    CS  u0 {2,S}
5    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 101,
    label = "Ca_Cds-TwoDe",
    group =
"""
1 *2 Cd                        u0 {2,D} {3,S} {4,S}
2 *1 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    C                         u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 102,
    label = "Ca_Cds-CtCt",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    Ct  u0 {2,S}
5    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 103,
    label = "Ca_Cds-CtCb",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    Ct  u0 {2,S}
5    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "Ca_Cds-CtCO",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    Ct  u0 {2,S}
5    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 105,
    label = "Ca_Cds-CbCb",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    Cb  u0 {2,S}
5    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 106,
    label = "Ca_Cds-CbCO",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    Cb  u0 {2,S}
5    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 107,
    label = "Ca_Cds-COCO",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    CO  u0 {2,S}
5    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 108,
    label = "Ca_Cds-CdCt",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    Cd  u0 {2,S} {6,D}
5    Ct  u0 {2,S}
6    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 109,
    label = "Ca_Cds-CdCb",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    Cd  u0 {2,S} {6,D}
5    Cb  u0 {2,S}
6    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 110,
    label = "Ca_Cds-CdCO",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    Cd  u0 {2,S} {6,D}
5    CO  u0 {2,S}
6    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 111,
    label = "Ca_Cds-CtC=S",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    Ct  u0 {2,S}
5    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "Ca_Cds-CbC=S",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    Cb  u0 {2,S}
5    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "Ca_Cds-COC=S",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    CO  u0 {2,S}
5    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "Ca_Cds-CdCd",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    Cd  u0 {2,S} {6,D}
5    Cd  u0 {2,S} {7,D}
6    C   u0 {4,D}
7    C   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 115,
    label = "Ca_Cds-CdCdCdCdCd_cycle",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    Cd  u0 {2,S} {6,D}
5    Cd  u0 {2,S} {7,D} {9,S}
6    Cd  u0 {4,D} {8,S}
7    C   u0 {5,D}
8    Cd  u0 {6,S} {9,D}
9    Cd  u0 {5,S} {8,D}
""",
    kinetics = None,
)

entry(
    index = 116,
    label = "Ca_Cds-CdC=S",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    Cd  u0 {2,S} {6,D}
5    CS  u0 {2,S}
6    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 117,
    label = "Ca_Cds-C=SC=S",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    C   u0 {1,D}
4    CS  u0 {2,S}
5    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 118,
    label = "Ck_Cds",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    R   u0 {2,S}
5    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 119,
    label = "Ck_Cds-HH",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    H   u0 {2,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 120,
    label = "Ck_Cds-CsH",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    Cs  u0 {2,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 121,
    label = "Ck_Cds-CsCs",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    Cs  u0 {2,S}
5    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "Ck_Cds-OneDeH",
    group =
"""
1 *1 Cdd                       u0 {2,D} {3,D}
2 *2 Cd                        u0 {1,D} {4,S} {5,S}
3    O2d                       u0 {1,D}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
5    H                         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 123,
    label = "Ck_Cds-CtH",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    Ct  u0 {2,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 124,
    label = "Ck_Cds-CbH",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    Cb  u0 {2,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 125,
    label = "Ck_Cds-COH",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    CO  u0 {2,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 126,
    label = "Ck_Cds-CdH",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    Cd  u0 {2,S} {6,D}
5    H   u0 {2,S}
6    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 127,
    label = "Ck_Cds-C=SH",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    CS  u0 {2,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 128,
    label = "Ck_Cds-OneDeCs",
    group =
"""
1 *1 Cdd                       u0 {2,D} {3,D}
2 *2 Cd                        u0 {1,D} {4,S} {5,S}
3    O2d                       u0 {1,D}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
5    Cs                        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 129,
    label = "Ck_Cds-CtCs",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    Ct  u0 {2,S}
5    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 130,
    label = "Ck_Cds-CbCs",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    Cb  u0 {2,S}
5    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 131,
    label = "Ck_Cds-COCs",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    CO  u0 {2,S}
5    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 132,
    label = "Ck_Cds-CdCs",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    Cd  u0 {2,S} {6,D}
5    Cs  u0 {2,S}
6    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 133,
    label = "Ck_Cds-C=SCs",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    CS  u0 {2,S}
5    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 134,
    label = "Ck_Cds-TwoDe",
    group =
"""
1 *1 Cdd                       u0 {2,D} {3,D}
2 *2 Cd                        u0 {1,D} {4,S} {5,S}
3    O2d                       u0 {1,D}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 135,
    label = "Ck_Cds-CtCt",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    Ct  u0 {2,S}
5    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 136,
    label = "Ck_Cds-CtCb",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    Ct  u0 {2,S}
5    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 137,
    label = "Ck_Cds-CtCO",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    Ct  u0 {2,S}
5    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 138,
    label = "Ck_Cds-CbCb",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    Cb  u0 {2,S}
5    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 139,
    label = "Ck_Cds-CbCO",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    Cb  u0 {2,S}
5    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 140,
    label = "Ck_Cds-COCO",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    CO  u0 {2,S}
5    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 141,
    label = "Ck_Cds-CdCt",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    Cd  u0 {2,S} {6,D}
5    Ct  u0 {2,S}
6    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "Ck_Cds-CdCb",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    Cd  u0 {2,S} {6,D}
5    Cb  u0 {2,S}
6    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 143,
    label = "Ck_Cds-CdCO",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    Cd  u0 {2,S} {6,D}
5    CO  u0 {2,S}
6    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 144,
    label = "Ck_Cds-CtC=S",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    Ct  u0 {2,S}
5    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 145,
    label = "Ck_Cds-CbC=S",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    Cb  u0 {2,S}
5    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 146,
    label = "Ck_Cds-COC=S",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    CO  u0 {2,S}
5    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 147,
    label = "Ck_Cds-CdCd",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    Cd  u0 {2,S} {6,D}
5    Cd  u0 {2,S} {7,D}
6    C   u0 {4,D}
7    C   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 148,
    label = "Ck_Cds-CdC=S",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    Cd  u0 {2,S} {6,D}
5    CS  u0 {2,S}
6    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 149,
    label = "Ck_Cds-C=SC=S",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    O2d u0 {1,D}
4    CS  u0 {2,S}
5    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 150,
    label = "Cdd_Cdd",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cdd u0 {1,D} {4,D}
3    R!H u0 {1,D}
4    R!H u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 151,
    label = "Ca_Ca",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cdd u0 {1,D} {4,D}
3    C   u0 {1,D}
4    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 152,
    label = "Ca-Cb_Ca-Cb_cyc6",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cdd u0 {1,D} {4,D}
3    Cd  u0 {1,D} {5,S}
4    Cd  u0 {2,D} {6,S}
5    Cb  u0 {3,S} {6,B}
6    Cb  u0 {4,S} {5,B}
""",
    kinetics = None,
)

entry(
    index = 153,
    label = "Ck_Ck",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cdd u0 {1,D} {4,D}
3    O2d u0 {1,D}
4    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 154,
    label = "Ca_Ck",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cdd u0 {1,D} {4,D}
3    C   u0 {1,D}
4    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 155,
    label = "Ck_Ca",
    group =
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cdd u0 {1,D} {4,D}
3    O2d u0 {1,D}
4    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 156,
    label = "Cds_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    R   ux {1,S}
4    R   ux {1,S}
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "Cds-HH_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "Cds-CsH_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 159,
    label = "Cds-CsCs_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "Cds-OsH_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    O2s u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "Cds-OsCs_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    O2s u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 162,
    label = "Cds-SsH_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    S2s u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 163,
    label = "Cds-SsCs_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    S2s u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 164,
    label = "Cds-OneDeH_Sd",
    group =
"""
1 *1 CS                        u0 {2,D} {3,S} {4,S}
2 *2 S2d                       u0 p2 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    H                         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 165,
    label = "Cds-CtH_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 166,
    label = "Cds-CbH_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "Cds-COH_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    CO  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 168,
    label = "Cds-CdH_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cd  u0 {1,S} {5,D}
4    H   u0 {1,S}
5    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 169,
    label = "Cds-C=SH_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    CS  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 170,
    label = "Cds-OneDeCs_Sd",
    group =
"""
1 *1 CS                        u0 {2,D} {3,S} {4,S}
2 *2 S2d                       u0 p2 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cs                        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 171,
    label = "Cds-CtCs_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 172,
    label = "Cds-CbCs_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 173,
    label = "Cds-COCs_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    CO  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 174,
    label = "Cds-CdCs_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cd  u0 {1,S} {5,D}
4    Cs  u0 {1,S}
5    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 175,
    label = "Cds-C=SCs_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    CS  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 176,
    label = "Cds-TwoDe_Sd",
    group =
"""
1 *1 CS                        u0 {2,D} {3,S} {4,S}
2 *2 S2d                       u0 p2 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 177,
    label = "Cds-CtCt_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 178,
    label = "Cds-CtCb_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 179,
    label = "Cds-CtCO_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 180,
    label = "Cds-CbCb_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cb  u0 {1,S}
4    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 181,
    label = "Cds-CbCO_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cb  u0 {1,S}
4    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 182,
    label = "Cds-COCO_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    CO  u0 {1,S}
4    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 183,
    label = "Cds-CdCt_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cd  u0 {1,S} {5,D}
4    Ct  u0 {1,S}
5    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 184,
    label = "Cds-CdCb_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cd  u0 {1,S} {5,D}
4    Cb  u0 {1,S}
5    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 185,
    label = "Cds-CdCO_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cd  u0 {1,S} {5,D}
4    CO  u0 {1,S}
5    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 186,
    label = "Cds-CtC=S_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 187,
    label = "Cds-CbC=S_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cb  u0 {1,S}
4    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 188,
    label = "Cds-COC=S_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    CO  u0 {1,S}
4    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 189,
    label = "Cds-CdCd_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cd  u0 {1,S} {5,D}
4    Cd  u0 {1,S} {6,D}
5    C   u0 {3,D}
6    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 190,
    label = "Cds-CdC=S_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cd  u0 {1,S} {5,D}
4    CS  u0 {1,S}
5    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 191,
    label = "Cds-C=SC=S_Sd",
    group =
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    CS  u0 {1,S}
4    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 192,
    label = "Cds_Nd",
    group =
"""
1 *1 Cd u0 {2,D}
2 *2 N  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 193,
    label = "Cds_N3d",
    group =
"""
1 *1 Cd  u0 {2,D}
2 *2 N3d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 194,
    label = "Cds-HH_N3d",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 N3d u0 {1,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 195,
    label = "Cds-NonDeH_N3d",
    group =
"""
1 *1 Cd                    u0 {2,D} {3,S} {4,S}
2 *2 N3d                   u0 {1,D}
3    H                     u0 {1,S}
4    [Cs,O2s,N3s,N5sc,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 196,
    label = "Cds-NonDe2_N3d",
    group =
"""
1 *1 Cd                    u0 {2,D} {3,S} {4,S}
2 *2 N3d                   u0 {1,D}
3    [Cs,O2s,N3s,N5sc,S2s] u0 {1,S}
4    [Cs,O2s,N3s,N5sc,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 197,
    label = "Cds_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    R  ux {1,S}
4    R  ux {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 198,
    label = "Cds-HH_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 199,
    label = "Cds-HH_Cds-HH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 200,
    label = "Cds-HH_Cds-CsH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 201,
    label = "Cds-HH_Cds-Cs\O2s/H",
    group =
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S}
4    H   u0 {1,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    O2s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 202,
    label = "Cds-HH_Cds-Cs\H3/H",
    group =
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cd u0 {1,S} {3,D} {7,S}
3 *1 Cd u0 {2,D} {8,S} {9,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {3,S}
9    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 203,
    label = "Cds-HH_Cds-CsCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 204,
    label = "Cds-HH_Cds-OsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 205,
    label = "Cds-HH_Cds-OsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 206,
    label = "Cds-HH_Cds-OsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 207,
    label = "Cds-HH_Cds-SsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 208,
    label = "Cds-HH_Cds-SsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 209,
    label = "Cds-HH_Cds-SsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 210,
    label = "Cds-HH_Cds-SsSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 211,
    label = "Cds-HH_Cds-OneDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    H                         u0 {1,S}
5    [H,Cs,O2s,S2s]            u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 212,
    label = "Cds-HH_Cds-OneDeH",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    H                         u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 213,
    label = "Cds-HH_Cds-CtH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 214,
    label = "Cds-HH_Cds-CbH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 215,
    label = "Cds-HH_Cds-COH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 216,
    label = "Cds-HH_Cds-(Cd-Cd-Cb)H",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {5,S}
2 *1 Cd u0 {1,D} {6,S} {7,S}
3    Cd u0 {1,S} {4,D}
4    Cd u0 {3,D} {8,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    H  u0 {2,S}
8    Cb u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 217,
    label = "Cds-HH_Cds-CdH",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 218,
    label = "Cds-HH_Cds-C=SH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 219,
    label = "Cds-HH_Cds-OneDeCs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    H                         u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 220,
    label = "Cds-HH_Cds-CtCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 221,
    label = "Cds-HH_Cds-CbCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 222,
    label = "Cds-HH_Cds-COCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 223,
    label = "Cds-HH_Cds-CdCs",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 224,
    label = "Cds-HH_Cds-C=SCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 225,
    label = "Cds-HH_Cds-OneDeOs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    H                         u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 226,
    label = "Cds-HH_Cds-CtOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 227,
    label = "Cds-HH_Cds-CbOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 228,
    label = "Cds-HH_Cds-COOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 229,
    label = "Cds-HH_Cds-CdOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cd  u0 {2,S} {7,D}
7    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 230,
    label = "Cds-HH_Cds-C=SOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 231,
    label = "Cds-HH_Cds-OneDeSs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    H                         u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 232,
    label = "Cds-HH_Cds-CtSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 233,
    label = "Cds-HH_Cds-CbSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 234,
    label = "Cds-HH_Cds-COSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 235,
    label = "Cds-HH_Cds-CdSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cd  u0 {2,S} {7,D}
7    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 236,
    label = "Cds-HH_Cds-C=SSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 237,
    label = "Cds-HH_Cds-TwoDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    H                         u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 238,
    label = "Cds-HH_Cds-CtCt",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 239,
    label = "Cds-HH_Cds-CtCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 240,
    label = "Cds-HH_Cds-CtCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 241,
    label = "Cds-HH_Cds-CbCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 242,
    label = "Cds-HH_Cds-CbCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 243,
    label = "Cds-HH_Cds-COCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 244,
    label = "Cds-HH_Cds-CdCt",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 245,
    label = "Cds-HH_Cds-CdCb",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cb u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 246,
    label = "Cds-HH_Cds-CdCbCbCdCdCd_cycle",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cd u0 {2,S} {7,D}
6    Cb u0 {2,S} {8,B}
7    Cd u0 {5,D} {8,S}
8    Cb u0 {6,B} {7,S}
""",
    kinetics = None,
)

entry(
    index = 247,
    label = "Cds-HH_Cds-CdCO",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CO u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 248,
    label = "Cds-HH_Cds-CtC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 249,
    label = "Cds-HH_Cds-CbC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 250,
    label = "Cds-HH_Cds-COC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 251,
    label = "Cds-HH_Cds-CdCd",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 252,
    label = "Cds-HH_Cds-CdCd_cyc",
    group =
"""
1  *1 Cd u0 {2,D} {3,S} {4,S}
2  *2 Cd u0 {1,D} {5,S} {6,S}
3     H  u0 {1,S}
4     H  u0 {1,S}
5     Cd u0 {2,S} {7,D}
6     Cd u0 {2,S} {8,D}
7     Cd u0 {5,D} {9,S}
8     Cd u0 {6,D} {12,S}
9     Cd u0 {7,S} {10,D}
10    Cd u0 {9,D} {11,S}
11    Cd u0 {10,S} {12,D}
12    Cd u0 {8,S} {11,D}
""",
    kinetics = None,
)

entry(
    index = 253,
    label = "Cds-HH_Cds-CdC=S",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CS u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 254,
    label = "Cds-HH_Cds-C=SC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 255,
    label = "Cds-CsH_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 256,
    label = "Cds-CsH_Cds-HH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 257,
    label = "Cds-Cs\O2s/H_Cds-HH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S}
4    H   u0 {1,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    O2s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 258,
    label = "Cds-CsH_Cds-CsH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 259,
    label = "Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S} {8,S}
4    H  u0 {1,S}
5    Cs u0 {2,S} {7,S}
6    H  u0 {2,S}
7    Cd u0 {5,S} {8,D}
8    Cd u0 {3,S} {7,D}
""",
    kinetics = None,
)

entry(
    index = 260,
    label = "Cds-CsH_Cds-CsCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 261,
    label = "Cds-CsH_Cds-OsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 262,
    label = "Cds-CsH_Cds-OsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 263,
    label = "Cds-CsH_Cds-OsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 264,
    label = "Cds-CsH_Cds-SsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 265,
    label = "Cds-CsH_Cds-SsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 266,
    label = "Cds-CsH_Cds-SsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 267,
    label = "Cds-CsH_Cds-SsSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 268,
    label = "Cds-CsH_Cds-OneDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    H                         u0 {1,S}
5    [H,Cs,O2s,S2s]            u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 269,
    label = "Cds-CsH_Cds-OneDeH",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    H                         u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 270,
    label = "Cds-CsH_Cds-CtH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 271,
    label = "Cds-CsH_Cds-CbH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 272,
    label = "Cds-CsH_Cds-COH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 273,
    label = "Cds-CsH_Cds-(Cd-Cd-Cd-Cd-Cd)H",
    group =
"""
1  *2 Cd u0 {2,D} {3,S} {7,S}
2  *1 Cd u0 {1,D} {8,S} {9,S}
3     Cd u0 {1,S} {4,D}
4     Cd u0 {3,D} {5,S}
5     Cd u0 {4,S} {6,D}
6     Cd u0 {5,D} {10,S}
7     H  u0 {1,S}
8     Cs u0 {2,S}
9     H  u0 {2,S}
10    Cd u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 274,
    label = "Cds-CsH_Cds-(Cd-Cd-Cd)H",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {5,S}
2 *1 Cd u0 {1,D} {6,S} {7,S}
3    Cd u0 {1,S} {4,D}
4    Cd u0 {3,D} {8,S}
5    H  u0 {1,S}
6    Cs u0 {2,S}
7    H  u0 {2,S}
8    Cd u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 275,
    label = "Cds-CsH_Cds-Cd(Cd)H",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    Cd u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 276,
    label = "Cds-CsH_Cds-CdH",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 277,
    label = "Cds-CsH_Cds-(CdsH-Cds)_cyc5",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {6,S}
2 *2 Cd u0 {1,D} {4,S} {7,S}
3    Cs u0 {1,S} {5,S}
4    Cd u0 {2,S} {5,D}
5    Cd u0 {3,S} {4,D}
6    H  u0 {1,S}
7    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 278,
    label = "Cds-CsH_Cds-C=SH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 279,
    label = "Cds-CsH_Cds-OneDeCs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    H                         u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 280,
    label = "Cds-CsH_Cds-CtCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 281,
    label = "Cds-CsH_Cds-CbCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 282,
    label = "Cds-CsH_Cds-COCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 283,
    label = "Cds-CsH_Cds-CdCs",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 284,
    label = "Cds-CsH_Cds-C=SCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 285,
    label = "Cds-CsH_Cds-OneDeOs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    H                         u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 286,
    label = "Cds-CsH_Cds-CtOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 287,
    label = "Cds-CsH_Cds-CbOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 288,
    label = "Cds-CsH_Cds-COOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 289,
    label = "Cds-CsH_Cds-CdOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cd  u0 {2,S} {7,D}
7    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 290,
    label = "Cds-CsH_Cds-C=SOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 291,
    label = "Cds-CsH_Cds-OneDeSs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    H                         u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 292,
    label = "Cds-CsH_Cds-CtSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 293,
    label = "Cds-CsH_Cds-CbSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 294,
    label = "Cds-CsH_Cds-COSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 295,
    label = "Cds-CsH_Cds-CdSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cd  u0 {2,S} {7,D}
7    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 296,
    label = "Cds-CsH_Cds-C=SSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 297,
    label = "Cds-CsH_Cds-TwoDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    H                         u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 298,
    label = "Cds-CsH_Cds-CtCt",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 299,
    label = "Cds-CsH_Cds-CtCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 300,
    label = "Cds-CsH_Cds-CtCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 301,
    label = "Cds-CsH_Cds-CbCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 302,
    label = "Cds-CsH_Cds-CbCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 303,
    label = "Cds-CsH_Cds-COCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 304,
    label = "Cds-CsH_Cds-CdCt",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 305,
    label = "Cds-CsH_Cds-CdCb",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cb u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 306,
    label = "Cds-CsH_Cds-CdCO",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CO u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 307,
    label = "Cds-CsH_Cds-CtC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 308,
    label = "Cds-CsH_Cds-CbC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 309,
    label = "Cds-CsH_Cds-COC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 310,
    label = "Cds-CsH_Cds-CdCd",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 311,
    label = "Cds-CsH_Cds-CdC=S",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CS u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 312,
    label = "Cds-CsH_Cds-C=SC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 313,
    label = "Cds-CsCs_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 314,
    label = "Cds-CsCs_Cds-HH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 315,
    label = "Cds-CsCs_Cds-CsH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 316,
    label = "Cds-CsCs_Cds-CsCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 317,
    label = "Cds-CsCs_Cds-OsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 318,
    label = "Cds-CsCs_Cds-OsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 319,
    label = "Cds-CsCs_Cds-OsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 320,
    label = "Cds-CsCs_Cds-SsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 321,
    label = "Cds-CsCs_Cds-SsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 322,
    label = "Cds-CsCs_Cds-SsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 323,
    label = "Cds-CsCs_Cds-SsSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 324,
    label = "Cds-CsCs_Cds-OneDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    Cs                        u0 {1,S}
5    [H,Cs,O2s,S2s]            u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 325,
    label = "Cds-CsCs_Cds-OneDeH",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    Cs                        u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 326,
    label = "Cds-CsCs_Cds-CtH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 327,
    label = "Cds-CsCs_Cds-CbH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 328,
    label = "Cds-CsCs_Cds-COH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 329,
    label = "Cds-CsCs_Cds-CdH",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 330,
    label = "Cds-CsCs_Cds-C=SH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 331,
    label = "Cds-CsCs_Cds-OneDeCs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    Cs                        u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 332,
    label = "Cds-CsCs_Cds-CtCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 333,
    label = "Cds-CsCs_Cds-CbCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 334,
    label = "Cds-CsCs_Cds-COCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 335,
    label = "Cds-CsCs_Cds-CdCs",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 336,
    label = "Cds-CsCs_Cds-C=SCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 337,
    label = "Cds-CsCs_Cds-OneDeOs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    Cs                        u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 338,
    label = "Cds-CsCs_Cds-CtOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 339,
    label = "Cds-CsCs_Cds-CbOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 340,
    label = "Cds-CsCs_Cds-COOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 341,
    label = "Cds-CsCs_Cds-CdOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Cd  u0 {2,S} {7,D}
7    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 342,
    label = "Cds-CsCs_Cds-C=SOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 343,
    label = "Cds-CsCs_Cds-OneDeSs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    Cs                        u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 344,
    label = "Cds-CsCs_Cds-CtSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 345,
    label = "Cds-CsCs_Cds-CbSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 346,
    label = "Cds-CsCs_Cds-COSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 347,
    label = "Cds-CsCs_Cds-CdSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Cd  u0 {2,S} {7,D}
7    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 348,
    label = "Cds-CsCs_Cds-C=SSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 349,
    label = "Cds-CsCs_Cds-TwoDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    Cs                        u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 350,
    label = "Cds-CsCs_Cds-CtCt",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 351,
    label = "Cds-CsCs_Cds-CtCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 352,
    label = "Cds-CsCs_Cds-CtCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 353,
    label = "Cds-CsCs_Cds-CbCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 354,
    label = "Cds-CsCs_Cds-CbCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 355,
    label = "Cds-CsCs_Cds-COCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 356,
    label = "Cds-CsCs_Cds-CdCt",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 357,
    label = "Cds-CsCs_Cds-CdCb",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cb u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 358,
    label = "Cds-CsCs_Cds-CdCO",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CO u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 359,
    label = "Cds-CsCs_Cds-CtC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 360,
    label = "Cds-CsCs_Cds-CbC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 361,
    label = "Cds-CsCs_Cds-COC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 362,
    label = "Cds-CsCs_Cds-(Cd-Cd-Cd)Cd",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {5,S}
2 *1 Cd u0 {1,D} {6,S} {7,S}
3    Cd u0 {1,S} {4,D}
4    Cd u0 {3,D} {8,S}
5    Cd u0 {1,S}
6    Cs u0 {2,S}
7    Cs u0 {2,S}
8    Cd u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 363,
    label = "Cds-CsCs_Cds-CdCd",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 364,
    label = "Cds-CsCs_Cds-CdC=S",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CS u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 365,
    label = "Cds-CsCs_Cds-C=SC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 366,
    label = "Cds-SsH_Cds",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    S2s u0 {1,S}
4    H   u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 367,
    label = "Cds-SsCs_Cds",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    S2s u0 {1,S}
4    Cs  u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 368,
    label = "Cds-SsSs_Cds",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    S2s u0 {1,S}
4    S2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 369,
    label = "Cds-N3sH_Cds",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    N3s u0 {1,S}
4    H   u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 370,
    label = "Cds-OsH_Cds",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    O2s u0 {1,S}
4    H   u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 371,
    label = "Cds-OsH_Cds-CsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    O2s u0 {1,S}
4    H   u0 {1,S}
5    Cs  u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 372,
    label = "Cds-OsCs_Cds",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    O2s u0 {1,S}
4    Cs  u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 373,
    label = "Cds-OsOs_Cds",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    O2s u0 {1,S}
4    O2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 374,
    label = "Cds-OsSs_Cds",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    O2s u0 {1,S}
4    S2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 375,
    label = "Cds-OneDe_Cds",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [H,Cs,O2s,S2s]            u0 {1,S}
5    R                         u0 {2,S}
6    R                         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 376,
    label = "Cds-OneDeH_Cds",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    H                         u0 {1,S}
5    R                         u0 {2,S}
6    R                         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 377,
    label = "Cds-CtH_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 378,
    label = "Cds-CtH_Cds-HH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 379,
    label = "Cds-CtH_Cds-CsH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 380,
    label = "Cds-CtH_Cds-CsCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 381,
    label = "Cds-CtH_Cds-OsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 382,
    label = "Cds-CtH_Cds-OsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 383,
    label = "Cds-CtH_Cds-OsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 384,
    label = "Cds-CtH_Cds-SsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 385,
    label = "Cds-CtH_Cds-SsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 386,
    label = "Cds-CtH_Cds-SsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 387,
    label = "Cds-CtH_Cds-SsSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 388,
    label = "Cds-CtH_Cds-OneDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    H                         u0 {1,S}
5    [H,Cs,O2s,S2s]            u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 389,
    label = "Cds-CtH_Cds-OneDeH",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    H                         u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 390,
    label = "Cds-CtH_Cds-CtH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 391,
    label = "Cds-CtH_Cds-CbH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 392,
    label = "Cds-CtH_Cds-COH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 393,
    label = "Cds-CtH_Cds-CdH",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 394,
    label = "Cds-CtH_Cds-C=SH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 395,
    label = "Cds-CtH_Cds-OneDeCs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    H                         u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 396,
    label = "Cds-CtH_Cds-CtCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 397,
    label = "Cds-CtH_Cds-CbCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 398,
    label = "Cds-CtH_Cds-COCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 399,
    label = "Cds-CtH_Cds-CdCs",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 400,
    label = "Cds-CtH_Cds-C=SCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 401,
    label = "Cds-CtH_Cds-OneDeOs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    H                         u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 402,
    label = "Cds-CtH_Cds-CtOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 403,
    label = "Cds-CtH_Cds-CbOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 404,
    label = "Cds-CtH_Cds-COOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 405,
    label = "Cds-CtH_Cds-CdOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cd  u0 {2,S} {7,D}
7    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 406,
    label = "Cds-CtH_Cds-C=SOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 407,
    label = "Cds-CtH_Cds-OneDeSs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    H                         u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 408,
    label = "Cds-CtH_Cds-CtSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 409,
    label = "Cds-CtH_Cds-CbSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 410,
    label = "Cds-CtH_Cds-COSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 411,
    label = "Cds-CtH_Cds-CdSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cd  u0 {2,S} {7,D}
7    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 412,
    label = "Cds-CtH_Cds-C=SSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 413,
    label = "Cds-CtH_Cds-TwoDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    H                         u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 414,
    label = "Cds-CtH_Cds-CtCt",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 415,
    label = "Cds-CtH_Cds-CtCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 416,
    label = "Cds-CtH_Cds-CtCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 417,
    label = "Cds-CtH_Cds-CbCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 418,
    label = "Cds-CtH_Cds-CbCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 419,
    label = "Cds-CtH_Cds-COCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 420,
    label = "Cds-CtH_Cds-CdCt",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 421,
    label = "Cds-CtH_Cds-CdCb",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cb u0 {1,S}
5    Ct u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 422,
    label = "Cds-CtH_Cds-CdCO",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CO u0 {1,S}
5    Ct u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 423,
    label = "Cds-CtH_Cds-CtC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 424,
    label = "Cds-CtH_Cds-CbC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 425,
    label = "Cds-CtH_Cds-COC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 426,
    label = "Cds-CtH_Cds-CdCd",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Ct u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 427,
    label = "Cds-CtH_Cds-CdC=S",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CS u0 {1,S}
5    Ct u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 428,
    label = "Cds-CtH_Cds-C=SC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 429,
    label = "Cds-CbH_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 430,
    label = "Cds-CbH_Cds-HH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 431,
    label = "Cds-CbH_Cds-CsH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 432,
    label = "Cds-CbH_Cds-CsCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 433,
    label = "Cds-CbH_Cds-OsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 434,
    label = "Cds-CbH_Cds-OsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 435,
    label = "Cds-CbH_Cds-OsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 436,
    label = "Cds-CbH_Cds-SsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 437,
    label = "Cds-CbH_Cds-SsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 438,
    label = "Cds-CbH_Cds-SsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 439,
    label = "Cds-CbH_Cds-SsSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 440,
    label = "Cds-CbH_Cds-OneDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    H                         u0 {1,S}
5    [H,Cs,O2s,S2s]            u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 441,
    label = "Cds-CbH_Cds-OneDeH",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    H                         u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 442,
    label = "Cds-CbH_Cds-CtH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 443,
    label = "Cds-CbH_Cds-CbH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 444,
    label = "Cds-CbH_Cds-COH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 445,
    label = "Cds-CbH_Cds-CdH",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 446,
    label = "Cds-CbH_Cds-Cd(CdCb)H",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {5,S}
2 *1 Cd u0 {1,D} {6,S} {7,S}
3    Cd u0 {1,S} {4,D}
4    Cd u0 {3,D} {8,S}
5    H  u0 {1,S}
6    Cb u0 {2,S}
7    H  u0 {2,S}
8    Cb u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 447,
    label = "Cds-CbH_Cds-C=SH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 448,
    label = "Cds-CbH_Cds-OneDeCs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    H                         u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 449,
    label = "Cds-CbH_Cds-CtCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 450,
    label = "Cds-CbH_Cds-CbCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 451,
    label = "Cds-CbH_Cds-COCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 452,
    label = "Cds-CbH_Cds-CdCs",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 453,
    label = "Cds-CbH_Cds-C=SCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 454,
    label = "Cds-CbH_Cds-OneDeOs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    H                         u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 455,
    label = "Cds-CbH_Cds-CtOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 456,
    label = "Cds-CbH_Cds-CbOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 457,
    label = "Cds-CbH_Cds-COOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 458,
    label = "Cds-CbH_Cds-CdOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cd  u0 {2,S} {7,D}
7    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 459,
    label = "Cds-CbH_Cds-C=SOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 460,
    label = "Cds-CbH_Cds-OneDeSs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    H                         u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 461,
    label = "Cds-CbH_Cds-CtSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 462,
    label = "Cds-CbH_Cds-CbSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 463,
    label = "Cds-CbH_Cds-COSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 464,
    label = "Cds-CbH_Cds-CdSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cd  u0 {2,S} {7,D}
7    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 465,
    label = "Cds-CbH_Cds-C=SSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 466,
    label = "Cds-CbH_Cds-TwoDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    H                         u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 467,
    label = "Cds-CbH_Cds-CtCt",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 468,
    label = "Cds-CbH_Cds-CtCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 469,
    label = "Cds-CbH_Cds-CtCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 470,
    label = "Cds-CbH_Cds-CbCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 471,
    label = "Cds-CbH_Cds-CbCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 472,
    label = "Cds-CbH_Cds-COCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 473,
    label = "Cds-CbH_Cds-CdCt",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cb u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 474,
    label = "Cds-CbH_Cds-CdCb",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cb u0 {1,S}
5    Cb u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 475,
    label = "Cds-CbH_Cds-CdCO",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CO u0 {1,S}
5    Cb u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 476,
    label = "Cds-CbH_Cds-CtC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 477,
    label = "Cds-CbH_Cds-CbC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 478,
    label = "Cds-CbH_Cds-COC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 479,
    label = "Cds-CbH_Cds-CdCd",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cb u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 480,
    label = "Cds-CbH_Cds-CdC=S",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CS u0 {1,S}
5    Cb u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 481,
    label = "Cds-CbH_Cds-C=SC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 482,
    label = "Cds-COH_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    CO u0 {1,S}
4    H  u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 483,
    label = "Cds-CdH_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 484,
    label = "Cds-CdH_Cds-HH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 485,
    label = "Cds-CdH_Cds-CsH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 486,
    label = "Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {7,S}
2 *2 Cd u0 {1,D} {4,S} {8,S}
3    Cd u0 {1,S} {5,D}
4    Cs u0 {2,S} {6,S}
5    Cd u0 {3,D} {6,S}
6    Cs u0 {4,S} {5,S}
7    H  u0 {1,S}
8    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 487,
    label = "Cds-CdH_Cds-(CsH-Cds)_cyc5",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {6,S}
2 *2 Cd u0 {1,D} {4,S} {7,S}
3    Cd u0 {1,S} {5,D}
4    Cs u0 {2,S} {5,S}
5    C  u0 {3,D} {4,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 488,
    label = "Cds-CdH_Cds-CsCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 489,
    label = "Cds-CdH_Cds-OsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 490,
    label = "Cds-CdH_Cds-OsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 491,
    label = "Cds-CdH_Cds-OsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 492,
    label = "Cds-CdH_Cds-SsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 493,
    label = "Cds-CdH_Cds-SsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 494,
    label = "Cds-CdH_Cds-SsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 495,
    label = "Cds-CdH_Cds-SsSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 496,
    label = "Cds-CdH_Cds-OneDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    H                         u0 {1,S}
5    R                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 497,
    label = "Cds-CdH_Cds-OneDeH",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    H                         u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 498,
    label = "Cds-CdH_Cds-CtH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 499,
    label = "Cds-CdH_Cds-CbH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 500,
    label = "Cds(CdCb)-CdH_Cds-CbH_cycle",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {7,S}
2 *2 Cd u0 {1,D} {4,S} {8,S}
3    Cd u0 {1,S} {5,D}
4    Cb u0 {2,S} {6,B}
5    Cd u0 {3,D} {6,S}
6    Cb u0 {4,B} {5,S}
7    H  u0 {1,S}
8    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 501,
    label = "Cds-CdH_Cds-Cb(Cb)H_cycle",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {6,S}
2 *2 Cd u0 {1,D} {4,S} {7,S}
3    Cd u0 {1,S} {5,S} {8,D}
4    Cb u0 {2,S} {5,B}
5    Cb u0 {3,S} {4,B}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 502,
    label = "Cds-CdH_Cds-COH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 503,
    label = "Cds-CdH_Cds-CdH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 504,
    label = "Cds-CdH_Cds-CdH_cyc5_1",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {6,S}
2 *1 Cd u0 {1,D} {4,S} {7,S}
3    Cd u0 {1,S} {5,S} {8,D}
4    Cd u0 {2,S} {5,D}
5    Cd u0 {3,S} {4,D}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 505,
    label = "Cds-CdH_Cds-CdH_cyc5_2",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {6,S}
2 *2 Cd u0 {1,D} {4,S} {7,S}
3    Cd u0 {1,S} {5,S} {8,D}
4    Cd u0 {2,S} {5,D}
5    Cd u0 {3,S} {4,D}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 506,
    label = "Cds-CdH_Cds-C=SH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 507,
    label = "Cds-CdH_Cds-OneDeCs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    H                         u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 508,
    label = "Cds-CdH_Cds-CtCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 509,
    label = "Cds-CdH_Cds-CbCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 510,
    label = "Cds-CdH_Cds-COCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 511,
    label = "Cds-CdH_Cds-CdCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    H  u0 {1,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 512,
    label = "Cds-CdH_Cds-C=SCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 513,
    label = "Cds-CdH_Cds-OneDeOs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    H                         u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 514,
    label = "Cds-CdH_Cds-CtOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 515,
    label = "Cds-CdH_Cds-CbOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 516,
    label = "Cds-CdH_Cds-COOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 517,
    label = "Cds-CdH_Cds-CdOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cd  u0 {2,S} {8,D}
7    C   u0 {3,D}
8    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 518,
    label = "Cds-CdH_Cds-C=SOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 519,
    label = "Cds-CdH_Cds-OneDeSs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    H                         u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 520,
    label = "Cds-CdH_Cds-CtSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 521,
    label = "Cds-CdH_Cds-CbSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 522,
    label = "Cds-CdH_Cds-COSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 523,
    label = "Cds-CdH_Cds-CdSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cd  u0 {2,S} {8,D}
7    C   u0 {3,D}
8    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 524,
    label = "Cds-CdH_Cds-C=SSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 525,
    label = "Cds-CdH_Cds-TwoDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    H                         u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 526,
    label = "Cds-CdH_Cds-CtCt",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 527,
    label = "Cds-CdH_Cds-CtCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 528,
    label = "Cds-CdH_Cds-CtCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 529,
    label = "Cds-CdH_Cds-CbCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 530,
    label = "Cds-CdH_Cds-CbCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 531,
    label = "Cds-CdH_Cds-COCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 532,
    label = "Cds-CdH_Cds-CdCt",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    H  u0 {1,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 533,
    label = "Cds-CdH_Cds-CdCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    H  u0 {1,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 534,
    label = "Cds-CdH_Cds-CdCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    H  u0 {1,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 535,
    label = "Cds-CdH_Cds-CtC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 536,
    label = "Cds-CdH_Cds-CbC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 537,
    label = "Cds-CdH_Cds-COC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 538,
    label = "Cds-CdH_Cds-CdCd",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {8,D}
4    Cd u0 {1,S} {9,D}
5    Cd u0 {2,S} {7,D}
6    H  u0 {2,S}
7    C  u0 {5,D}
8    C  u0 {3,D}
9    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 539,
    label = "Cds-CdH_Cds-CdCd_cyc6",
    group =
"""
1  *2 Cd u0 {2,S} {3,D} {4,S}
2     Cd u0 {1,S} {5,S} {10,D}
3  *1 Cd u0 {1,D} {8,S} {9,S}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {2,S} {7,D}
6     Cd u0 {4,D} {7,S}
7     Cd u0 {5,D} {6,S}
8     Cd u0 {3,S} {11,D}
9     H  u0 {3,S}
10    C  u0 {2,D}
11    C  u0 {8,D}
""",
    kinetics = None,
)

entry(
    index = 540,
    label = "Cds-CdH_Cds-CdCd_cyc6_cyc5",
    group =
"""
1  *1 Cd u0 {2,D} {3,S} {4,S}
2  *2 Cd u0 {1,D} {5,S} {6,S}
3     Cd u0 {1,S} {7,D} {9,S}
4     H  u0 {1,S}
5     Cd u0 {2,S} {8,D}
6     Cd u0 {2,S} {9,D} {11,S}
7     C  u0 {3,D}
8     Cd u0 {5,D} {10,S}
9     C  u0 {3,S} {6,D}
10    Cd u0 {8,S} {11,D}
11    Cd u0 {6,S} {10,D}
""",
    kinetics = None,
)

entry(
    index = 541,
    label = "Cds-CdH_Cds-CdC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    H  u0 {1,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 542,
    label = "Cds-CdH_Cds-C=SC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 543,
    label = "Cds-C=SH_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 544,
    label = "Cds-OneDeCs_Cds",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cs                        u0 {1,S}
5    R                         u0 {2,S}
6    R                         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 545,
    label = "Cds-CtCs_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 546,
    label = "Cds-CtCs_Cds-HH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 547,
    label = "Cds-CtCs_Cds-CsH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 548,
    label = "Cds-CtCs_Cds-CsCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 549,
    label = "Cds-CtCs_Cds-OsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 550,
    label = "Cds-CtCs_Cds-OsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 551,
    label = "Cds-CtCs_Cds-OsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 552,
    label = "Cds-CtCs_Cds-SsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 553,
    label = "Cds-CtCs_Cds-SsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 554,
    label = "Cds-CtCs_Cds-SsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 555,
    label = "Cds-CtCs_Cds-SsSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 556,
    label = "Cds-CtCs_Cds-OneDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Cs                        u0 {1,S}
5    [H,Cs,O2s,S2s]            u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 557,
    label = "Cds-CtCs_Cds-OneDeH",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Cs                        u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 558,
    label = "Cds-CtCs_Cds-CtH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 559,
    label = "Cds-CtCs_Cds-CbH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 560,
    label = "Cds-CtCs_Cds-COH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 561,
    label = "Cds-CtCs_Cds-CdH",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 562,
    label = "Cds-CtCs_Cds-C=SH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 563,
    label = "Cds-CtCs_Cds-OneDeCs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Cs                        u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 564,
    label = "Cds-CtCs_Cds-CtCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 565,
    label = "Cds-CtCs_Cds-CbCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 566,
    label = "Cds-CtCs_Cds-COCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 567,
    label = "Cds-CtCs_Cds-CdCs",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 568,
    label = "Cds-CtCs_Cds-C=SCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 569,
    label = "Cds-CtCs_Cds-OneDeOs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Cs                        u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 570,
    label = "Cds-CtCs_Cds-CtOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 571,
    label = "Cds-CtCs_Cds-CbOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 572,
    label = "Cds-CtCs_Cds-COOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 573,
    label = "Cds-CtCs_Cds-CdOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Cd  u0 {2,S} {7,D}
7    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 574,
    label = "Cds-CtCs_Cds-C=SOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 575,
    label = "Cds-CtCs_Cds-OneDeSs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Cs                        u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 576,
    label = "Cds-CtCs_Cds-CtSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 577,
    label = "Cds-CtCs_Cds-CbSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 578,
    label = "Cds-CtCs_Cds-COSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 579,
    label = "Cds-CtCs_Cds-CdSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Cd  u0 {2,S} {7,D}
7    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 580,
    label = "Cds-CtCs_Cds-C=SSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 581,
    label = "Cds-CtCs_Cds-TwoDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Cs                        u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 582,
    label = "Cds-CtCs_Cds-CtCt",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 583,
    label = "Cds-CtCs_Cds-CtCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 584,
    label = "Cds-CtCs_Cds-CtCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 585,
    label = "Cds-CtCs_Cds-CbCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 586,
    label = "Cds-CtCs_Cds-CbCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 587,
    label = "Cds-CtCs_Cds-COCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 588,
    label = "Cds-CtCs_Cds-CdCt",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 589,
    label = "Cds-CtCs_Cds-CdCb",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cb u0 {1,S}
5    Ct u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 590,
    label = "Cds-CtCs_Cds-CdCO",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CO u0 {1,S}
5    Ct u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 591,
    label = "Cds-CtCs_Cds-CtC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 592,
    label = "Cds-CtCs_Cds-CbC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 593,
    label = "Cds-CtCs_Cds-COC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 594,
    label = "Cds-CtCs_Cds-CdCd",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Ct u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 595,
    label = "Cds-CtCs_Cds-CdC=S",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CS u0 {1,S}
5    Ct u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 596,
    label = "Cds-CtCs_Cds-C=SC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 597,
    label = "Cds-CbCs_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 598,
    label = "Cds-CbCs_Cds-HH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 599,
    label = "Cds-CbCs_Cds-CsH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 600,
    label = "Cds-CbCs_Cds-CsCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 601,
    label = "Cds-CbCs_Cds-OsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 602,
    label = "Cds-CbCs_Cds-OsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 603,
    label = "Cds-CbCs_Cds-OsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 604,
    label = "Cds-CbCs_Cds-SsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 605,
    label = "Cds-CbCs_Cds-SsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 606,
    label = "Cds-CbCs_Cds-SsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 607,
    label = "Cds-CbCs_Cds-SsSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 608,
    label = "Cds-CbCs_Cds-OneDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    Cs                        u0 {1,S}
5    [H,Cs,O2s,S2s]            u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 609,
    label = "Cds-CbCs_Cds-OneDeH",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    Cs                        u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 610,
    label = "Cds-CbCs_Cds-CtH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 611,
    label = "Cds-CbCs_Cds-CbH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 612,
    label = "Cds-CbCs_Cds-COH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 613,
    label = "Cds-CbCs_Cds-CdH",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 614,
    label = "Cds-CbCs_Cds-C=SH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 615,
    label = "Cds-CbCs_Cds-OneDeCs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    Cs                        u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 616,
    label = "Cds-CbCs_Cds-CtCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 617,
    label = "Cds-CbCs_Cds-CbCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 618,
    label = "Cds-CbCs_Cds-COCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 619,
    label = "Cds-CbCs_Cds-CdCs",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 620,
    label = "Cds-CbCs_Cds-C=SCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 621,
    label = "Cds-CbCs_Cds-OneDeOs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    Cs                        u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 622,
    label = "Cds-CbCs_Cds-CtOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 623,
    label = "Cds-CbCs_Cds-CbOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 624,
    label = "Cds-CbCs_Cds-COOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 625,
    label = "Cds-CbCs_Cds-CdOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Cd  u0 {2,S} {7,D}
7    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 626,
    label = "Cds-CbCs_Cds-C=SOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 627,
    label = "Cds-CbCs_Cds-OneDeSs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    Cs                        u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 628,
    label = "Cds-CbCs_Cds-CtSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 629,
    label = "Cds-CbCs_Cds-CbSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 630,
    label = "Cds-CbCs_Cds-COSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 631,
    label = "Cds-CbCs_Cds-CdSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Cd  u0 {2,S} {7,D}
7    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 632,
    label = "Cds-CbCs_Cds-C=SSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 633,
    label = "Cds-CbCs_Cds-TwoDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    Cs                        u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 634,
    label = "Cds-CbCs_Cds-CtCt",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 635,
    label = "Cds-CbCs_Cds-CtCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 636,
    label = "Cds-CbCs_Cds-CtCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 637,
    label = "Cds-CbCs_Cds-CbCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 638,
    label = "Cds-CbCs_Cds-CbCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 639,
    label = "Cds-CbCs_Cds-COCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 640,
    label = "Cds-CbCs_Cds-CdCt",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cb u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 641,
    label = "Cds-CbCs_Cds-CdCb",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cb u0 {1,S}
5    Cb u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 642,
    label = "Cds-CbCs_Cds-CdCO",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CO u0 {1,S}
5    Cb u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 643,
    label = "Cds-CbCs_Cds-CtC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 644,
    label = "Cds-CbCs_Cds-CbC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 645,
    label = "Cds-CbCs_Cds-COC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 646,
    label = "Cds-CbCs_Cds-CdCd",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cb u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 647,
    label = "Cds-CbCs_Cds-CdC=S",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CS u0 {1,S}
5    Cb u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 648,
    label = "Cds-CbCs_Cds-C=SC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 649,
    label = "Cds-COCs_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 650,
    label = "Cds-CdCs_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 651,
    label = "Cds-CdCs_Cds-HH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 652,
    label = "Cds-CdCs_Cds-CsH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 653,
    label = "Cds-CdCs_Cds-CsCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 654,
    label = "Cds-CdCs_Cds-OsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 655,
    label = "Cds-CdCs_Cds-OsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 656,
    label = "Cds-CdCs_Cds-OsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 657,
    label = "Cds-CdCs_Cds-SsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 658,
    label = "Cds-CdCs_Cds-SsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 659,
    label = "Cds-CdCs_Cds-SsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 660,
    label = "Cds-CdCs_Cds-SsSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 661,
    label = "Cds-CdCs_Cds-OneDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cs                        u0 {1,S}
5    R                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 662,
    label = "Cds-CdCs_Cds-OneDeH",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cs                        u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 663,
    label = "Cds-CdCs_Cds-CtH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 664,
    label = "Cds-CdCs_Cds-CbH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 665,
    label = "Cds-CdCs_Cds-COH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 666,
    label = "Cds-CdCs_Cds-(Cd-Cd-Cd)H",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {7,S}
2 *1 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {5,D}
4    Cd u0 {2,S} {8,D}
5    Cd u0 {3,D} {9,S}
6    Cs u0 {2,S}
7    H  u0 {1,S}
8    C  u0 {4,D}
9    Cd u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 667,
    label = "Cds-CdCs_Cds-CdH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Cs u0 {1,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 668,
    label = "Cds-CdCs_Cds-C=SH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 669,
    label = "Cds-CdCs_Cds-OneDeCs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cs                        u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 670,
    label = "Cds-CdCs_Cds-CtCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 671,
    label = "Cds-CdCs_Cds-CbCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 672,
    label = "Cds-CdCs_Cds-COCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 673,
    label = "Cds-CdCs_Cds-CdCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Cs u0 {1,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 674,
    label = "Cds-CdCs_Cds-C=SCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 675,
    label = "Cds-CdCs_Cds-OneDeOs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cs                        u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 676,
    label = "Cds-CdCs_Cds-CtOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 677,
    label = "Cds-CdCs_Cds-CbOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 678,
    label = "Cds-CdCs_Cds-COOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 679,
    label = "Cds-CdCs_Cds-CdOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Cd  u0 {2,S} {8,D}
7    C   u0 {3,D}
8    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 680,
    label = "Cds-CdCs_Cds-C=SOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 681,
    label = "Cds-CdCs_Cds-OneDeSs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cs                        u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 682,
    label = "Cds-CdCs_Cds-CtSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 683,
    label = "Cds-CdCs_Cds-CbSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 684,
    label = "Cds-CdCs_Cds-COSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 685,
    label = "Cds-CdCs_Cds-CdSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Cd  u0 {2,S} {8,D}
7    C   u0 {3,D}
8    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 686,
    label = "Cds-CdCs_Cds-C=SSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 687,
    label = "Cds-CdCs_Cds-TwoDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cs                        u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 688,
    label = "Cds-CdCs_Cds-CtCt",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 689,
    label = "Cds-CdCs_Cds-CtCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 690,
    label = "Cds-CdCs_Cds-CtCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 691,
    label = "Cds-CdCs_Cds-CbCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 692,
    label = "Cds-CdCs_Cds-CbCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 693,
    label = "Cds-CdCs_Cds-COCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 694,
    label = "Cds-CdCs_Cds-CdCt",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Cs u0 {1,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 695,
    label = "Cds-CdCs_Cds-CdCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Cs u0 {1,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 696,
    label = "Cds-CdCs_Cds-CdCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Cs u0 {1,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 697,
    label = "Cds-CdCs_Cds-CtC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 698,
    label = "Cds-CdCs_Cds-CbC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 699,
    label = "Cds-CdCs_Cds-COC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 700,
    label = "Cds-CdCs_Cds-CdCd",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {8,D}
4    Cd u0 {1,S} {9,D}
5    Cd u0 {2,S} {7,D}
6    Cs u0 {2,S}
7    C  u0 {5,D}
8    C  u0 {3,D}
9    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 701,
    label = "Cds-CdCs_Cds-CdC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Cs u0 {1,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 702,
    label = "Cds-CdCs_Cds-C=SC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 703,
    label = "Cds-C=SCs_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 704,
    label = "Cds-OneDeSs_Cds",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    S2s                       u0 {1,S}
5    R                         u0 {2,S}
6    R                         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 705,
    label = "Cds-CtSs_Cds",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    S2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 706,
    label = "Cds-CbSs_Cds",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    S2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 707,
    label = "Cds-COSs_Cds",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    CO  u0 {1,S}
4    S2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 708,
    label = "Cds-CdSs_Cds",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    S2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 709,
    label = "Cds-C=SSs_Cds",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    CS  u0 {1,S}
4    S2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 710,
    label = "Cds-OneDeOs_Cds",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    O2s                       u0 {1,S}
5    R                         u0 {2,S}
6    R                         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 711,
    label = "Cds-CtOs_Cds",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    O2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 712,
    label = "Cds-CbOs_Cds",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    O2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 713,
    label = "Cds-COOs_Cds",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    CO  u0 {1,S}
4    O2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 714,
    label = "Cds-CdOs_Cds",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    O2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 715,
    label = "Cds-C=SOs_Cds",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    CS  u0 {1,S}
4    O2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 716,
    label = "Cds-TwoDe_Cds",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    R                         u0 {2,S}
6    R                         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 717,
    label = "Cds-CtCt_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 718,
    label = "Cds-CtCt_Cds-HH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 719,
    label = "Cds-CtCt_Cds-CsH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 720,
    label = "Cds-CtCt_Cds-CsCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 721,
    label = "Cds-CtCt_Cds-OsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 722,
    label = "Cds-CtCt_Cds-OsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 723,
    label = "Cds-CtCt_Cds-OsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 724,
    label = "Cds-CtCt_Cds-SsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 725,
    label = "Cds-CtCt_Cds-SsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 726,
    label = "Cds-CtCt_Cds-SsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 727,
    label = "Cds-CtCt_Cds-SsSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 728,
    label = "Cds-CtCt_Cds-OneDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Ct                        u0 {1,S}
5    [H,Cs,O2s,S2s]            u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 729,
    label = "Cds-CtCt_Cds-OneDeH",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Ct                        u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 730,
    label = "Cds-CtCt_Cds-CtH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 731,
    label = "Cds-CtCt_Cds-CbH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 732,
    label = "Cds-CtCt_Cds-COH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 733,
    label = "Cds-CtCt_Cds-CdH",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 734,
    label = "Cds-CtCt_Cds-C=SH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 735,
    label = "Cds-CtCt_Cds-OneDeCs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Ct                        u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 736,
    label = "Cds-CtCt_Cds-CtCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 737,
    label = "Cds-CtCt_Cds-CbCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 738,
    label = "Cds-CtCt_Cds-COCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 739,
    label = "Cds-CtCt_Cds-CdCs",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 740,
    label = "Cds-CtCt_Cds-C=SCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 741,
    label = "Cds-CtCt_Cds-OneDeOs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Ct                        u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 742,
    label = "Cds-CtCt_Cds-CtOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 743,
    label = "Cds-CtCt_Cds-CbOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 744,
    label = "Cds-CtCt_Cds-COOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 745,
    label = "Cds-CtCt_Cds-CdOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    Cd  u0 {2,S} {7,D}
7    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 746,
    label = "Cds-CtCt_Cds-C=SOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 747,
    label = "Cds-CtCt_Cds-OneDeSs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Ct                        u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 748,
    label = "Cds-CtCt_Cds-CtSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 749,
    label = "Cds-CtCt_Cds-CbSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 750,
    label = "Cds-CtCt_Cds-COSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 751,
    label = "Cds-CtCt_Cds-CdSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    Cd  u0 {2,S} {7,D}
7    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 752,
    label = "Cds-CtCt_Cds-C=SSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 753,
    label = "Cds-CtCt_Cds-TwoDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Ct                        u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 754,
    label = "Cds-CtCt_Cds-CtCt",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 755,
    label = "Cds-CtCt_Cds-CtCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 756,
    label = "Cds-CtCt_Cds-CtCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 757,
    label = "Cds-CtCt_Cds-CbCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 758,
    label = "Cds-CtCt_Cds-CbCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 759,
    label = "Cds-CtCt_Cds-COCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 760,
    label = "Cds-CtCt_Cds-CdCt",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 761,
    label = "Cds-CtCt_Cds-CdCb",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cb u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 762,
    label = "Cds-CtCt_Cds-CdCO",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CO u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 763,
    label = "Cds-CtCt_Cds-CtC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 764,
    label = "Cds-CtCt_Cds-CbC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 765,
    label = "Cds-CtCt_Cds-COC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 766,
    label = "Cds-CtCt_Cds-CdCd",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 767,
    label = "Cds-CtCt_Cds-CdC=S",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CS u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 768,
    label = "Cds-CtCt_Cds-C=SC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 769,
    label = "Cds-CtCb_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 770,
    label = "Cds-CtCO_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    CO u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 771,
    label = "Cds-CbCb_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 772,
    label = "Cds-CbCO_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    CO u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 773,
    label = "Cds-COCO_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    CO u0 {1,S}
4    CO u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 774,
    label = "Cds-CdCt_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 775,
    label = "Cds-CdCt_Cds-HH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 776,
    label = "Cds-CdCt_Cds-CsH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 777,
    label = "Cds-CdCt_Cds-CsCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 778,
    label = "Cds-CdCt_Cds-OsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 779,
    label = "Cds-CdCt_Cds-OsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 780,
    label = "Cds-CdCt_Cds-OsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 781,
    label = "Cds-CdCt_Cds-SsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 782,
    label = "Cds-CdCt_Cds-SsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 783,
    label = "Cds-CdCt_Cds-SsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 784,
    label = "Cds-CdCt_Cds-SsSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 785,
    label = "Cds-CdCt_Cds-OneDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Ct                        u0 {1,S}
5    [H,Cs,O2s,S2s]            u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 786,
    label = "Cds-CdCt_Cds-OneDeH",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Ct                        u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 787,
    label = "Cds-CdCt_Cds-CtH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 788,
    label = "Cds-CdCt_Cds-CbH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 789,
    label = "Cds-CdCt_Cds-COH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 790,
    label = "Cds-CdCt_Cds-CdH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Ct u0 {1,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 791,
    label = "Cds-CdCt_Cds-C=SH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 792,
    label = "Cds-CdCt_Cds-OneDeCs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Ct                        u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 793,
    label = "Cds-CdCt_Cds-CtCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 794,
    label = "Cds-CdCt_Cds-CbCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 795,
    label = "Cds-CdCt_Cds-COCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 796,
    label = "Cds-CdCt_Cds-CdCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Ct u0 {1,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 797,
    label = "Cds-CdCt_Cds-C=SCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 798,
    label = "Cds-CdCt_Cds-OneDeOs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Ct                        u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 799,
    label = "Cds-CdCt_Cds-CtOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 800,
    label = "Cds-CdCt_Cds-CbOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 801,
    label = "Cds-CdCt_Cds-COOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 802,
    label = "Cds-CdCt_Cds-CdOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    Cd  u0 {2,S} {8,D}
7    C   u0 {3,D}
8    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 803,
    label = "Cds-CdCt_Cds-C=SOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 804,
    label = "Cds-CdCt_Cds-OneDeSs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Ct                        u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 805,
    label = "Cds-CdCt_Cds-CtSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 806,
    label = "Cds-CdCt_Cds-CbSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 807,
    label = "Cds-CdCt_Cds-COSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 808,
    label = "Cds-CdCt_Cds-CdSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    Cd  u0 {2,S} {8,D}
7    C   u0 {3,D}
8    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 809,
    label = "Cds-CdCt_Cds-C=SSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 810,
    label = "Cds-CdCt_Cds-TwoDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Ct                        u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 811,
    label = "Cds-CdCt_Cds-CtCt",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 812,
    label = "Cds-CdCt_Cds-CtCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 813,
    label = "Cds-CdCt_Cds-CtCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 814,
    label = "Cds-CdCt_Cds-CbCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 815,
    label = "Cds-CdCt_Cds-CbCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 816,
    label = "Cds-CdCt_Cds-COCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 817,
    label = "Cds-CdCt_Cds-CdCt",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Ct u0 {1,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 818,
    label = "Cds-CdCt_Cds-CdCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Ct u0 {1,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 819,
    label = "Cds-CdCt_Cds-CdCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Ct u0 {1,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 820,
    label = "Cds-CdCt_Cds-CtC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 821,
    label = "Cds-CdCt_Cds-CbC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 822,
    label = "Cds-CdCt_Cds-COC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 823,
    label = "Cds-CdCt_Cds-CdCd",
    group =
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {8,D}
4    Cd u0 {1,S} {9,D}
5    Cd u0 {2,S} {7,D}
6    Ct u0 {2,S}
7    C  u0 {5,D}
8    C  u0 {3,D}
9    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 824,
    label = "Cds-CdCt_Cds-CdC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Ct u0 {1,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 825,
    label = "Cds-CdCt_Cds-C=SC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 826,
    label = "Cds-CdCb_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cb u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 827,
    label = "Cds-CdCO_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CO u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 828,
    label = "Cds-CtC=S_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    CS u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 829,
    label = "Cds-CbC=S_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    CS u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 830,
    label = "Cds-COC=S_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    CO u0 {1,S}
4    CS u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 831,
    label = "Cds-CdCd_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    R  u0 {2,S}
6    R  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 832,
    label = "Cds-CdCd_Cds-HH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 833,
    label = "Cds-CdCd_Cds-CsH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 834,
    label = "Cds-CdCd_Cds-CsCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 835,
    label = "Cds-CdCd_Cds-OsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    O2s u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 836,
    label = "Cds-CdCd_Cds-OsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 837,
    label = "Cds-CdCd_Cds-OsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 838,
    label = "Cds-CdCd_Cds-SsH",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    S2s u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 839,
    label = "Cds-CdCd_Cds-SsCs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 840,
    label = "Cds-CdCd_Cds-SsOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 841,
    label = "Cds-CdCd_Cds-SsSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 842,
    label = "Cds-CdCd_Cds-OneDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cd                        u0 {1,S} {8,D}
5    [H,Cs,O2s,S2s]            u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
8    C                         u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 843,
    label = "Cds-CdCd_Cds-OneDeH",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cd                        u0 {1,S} {8,D}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
8    C                         u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 844,
    label = "Cds-CdCd_Cds-CtH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    H  u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 845,
    label = "Cds-CdCd_Cds-CbH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    H  u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 846,
    label = "Cds-CdCd_Cds-COH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    H  u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 847,
    label = "Cds-CdCd_Cds-CdH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cd u0 {2,S} {9,D}
6    H  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
9    C  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 848,
    label = "Cds-CdCd_Cds-C=SH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    H  u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 849,
    label = "Cds-CdCd_Cds-OneDeCs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cd                        u0 {1,S} {8,D}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
8    C                         u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 850,
    label = "Cds-CdCd_Cds-CtCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 851,
    label = "Cds-CdCd_Cds-CbCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 852,
    label = "Cds-CdCd_Cds-COCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cs u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 853,
    label = "Cds-CdCd_Cds-CdCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cd u0 {2,S} {9,D}
6    Cs u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
9    C  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 854,
    label = "Cds-CdCd_Cds-C=SCs",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cs u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 855,
    label = "Cds-CdCd_Cds-OneDeOs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cd                        u0 {1,S} {8,D}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
8    C                         u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 856,
    label = "Cds-CdCd_Cds-CtOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 857,
    label = "Cds-CdCd_Cds-CbOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 858,
    label = "Cds-CdCd_Cds-COOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 859,
    label = "Cds-CdCd_Cds-CdOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    O2s u0 {2,S}
6    Cd  u0 {2,S} {9,D}
7    C   u0 {3,D}
8    C   u0 {4,D}
9    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 860,
    label = "Cds-CdCd_Cds-C=SOs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 861,
    label = "Cds-CdCd_Cds-OneDeSs",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cd                        u0 {1,S} {8,D}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
8    C                         u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 862,
    label = "Cds-CdCd_Cds-CtSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 863,
    label = "Cds-CdCd_Cds-CbSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 864,
    label = "Cds-CdCd_Cds-COSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 865,
    label = "Cds-CdCd_Cds-CdSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    S2s u0 {2,S}
6    Cd  u0 {2,S} {9,D}
7    C   u0 {3,D}
8    C   u0 {4,D}
9    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 866,
    label = "Cds-CdCd_Cds-C=SSs",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 867,
    label = "Cds-CdCd_Cds-TwoDe",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cd                        u0 {1,S} {8,D}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
8    C                         u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 868,
    label = "Cds-CdCd_Cds-CtCt",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 869,
    label = "Cds-CdCd_Cds-CtCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 870,
    label = "Cds-CdCd_Cds-CtCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Ct u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 871,
    label = "Cds-CdCd_Cds-CbCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 872,
    label = "Cds-CdCd_Cds-CbCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cb u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 873,
    label = "Cds-CdCd_Cds-COCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    CO u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 874,
    label = "Cds-CdCd_Cds-CdCt",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cd u0 {2,S} {9,D}
6    Ct u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
9    C  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 875,
    label = "Cds-CdCd_Cds-CdCb",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cd u0 {2,S} {9,D}
6    Cb u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
9    C  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 876,
    label = "Cds-CdCd_Cds-CdCO",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cd u0 {2,S} {9,D}
6    CO u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
9    C  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 877,
    label = "Cds-CdCd_Cds-CtC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Ct u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 878,
    label = "Cds-CdCd_Cds-CbC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cb u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 879,
    label = "Cds-CdCd_Cds-COC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    CO u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 880,
    label = "Cds-CdCd_Cds-CdCd",
    group =
"""
1  *1 Cd u0 {2,D} {3,S} {4,S}
2  *2 Cd u0 {1,D} {5,S} {6,S}
3     Cd u0 {1,S} {7,D}
4     Cd u0 {1,S} {8,D}
5     Cd u0 {2,S} {9,D}
6     Cd u0 {2,S} {10,D}
7     C  u0 {3,D}
8     C  u0 {4,D}
9     C  u0 {5,D}
10    C  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 881,
    label = "Cds-CdCd_Cds-CdC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cd u0 {2,S} {9,D}
6    CS u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
9    C  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 882,
    label = "Cds-CdCd_Cds-C=SC=S",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    CS u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 883,
    label = "Cds-CdC=S_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CS u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 884,
    label = "Cds-C=SC=S_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    CS u0 {1,S}
4    CS u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 885,
    label = "Cds-OJH_Cds",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    O  u1 {1,S}
4    H  u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 886,
    label = "Cds-OJH_Cds-HH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    O  u1 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 887,
    label = "Cds-OJH_Cds-CsH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    O  u1 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 888,
    label = "Cds-OJNonDe_Cds",
    group =
"""
1 *1 Cd                    u0 {2,D} {3,S} {4,S}
2 *2 Cd                    u0 {1,D} {5,S} {6,S}
3    O                     u1 {1,S}
4    [Cs,O2s,S2s,N3s,N5sc] u0 {1,S}
5    R                     u0 {2,S}
6    R                     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 889,
    label = "Cds-OJCs_Cds-HH",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    O  u1 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 890,
    label = "Cds-OJDe_Cds",
    group =
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    O                         u1 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    R                         u0 {2,S}
6    R                         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 891,
    label = "Ct_R",
    group =
"""
1 *1 Ct  u0 {2,T}
2 *2 R!H u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 892,
    label = "Ct_Ct",
    group =
"""
1 *1 Ct u0 {2,T}
2 *2 Ct u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 893,
    label = "Ct-H_Ct-H",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    H  u0 {1,S}
4    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 894,
    label = "Ct-H_Ct-Cs",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    H  u0 {1,S}
4    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 895,
    label = "Ct-Cs_Ct-H",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cs u0 {1,S}
4    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 896,
    label = "Ct-Cs_Ct-Cs",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cs u0 {1,S}
4    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 897,
    label = "Ct-H_Ct-De",
    group =
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 Ct                        u0 {1,T} {4,S}
3    H                         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 898,
    label = "Ct-H_Ct-Ct",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    H  u0 {1,S}
4    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 899,
    label = "Ct-H_Ct-Cb",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    H  u0 {1,S}
4    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 900,
    label = "Ct-H_Ct-CO",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    H  u0 {1,S}
4    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 901,
    label = "Ct-H_Ct-Cd",
    group =
"""
1 *2 Ct u0 {2,T} {3,S}
2 *1 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S} {5,D}
4    H  u0 {2,S}
5    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 902,
    label = "Ct-H_Ct-Cd-C-Cb",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    H  u0 {1,S}
4    Cd u0 {2,S} {5,D}
5    C  u0 {4,D} {6,S}
6    Cb u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 903,
    label = "Ct-H_Ct-C=S",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    H  u0 {1,S}
4    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 904,
    label = "Ct-Cs_Ct-De",
    group =
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 Ct                        u0 {1,T} {4,S}
3    Cs                        u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 905,
    label = "Ct-Cs_Ct-Ct",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cs u0 {1,S}
4    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 906,
    label = "Ct-Cs_Ct-Cb",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cs u0 {1,S}
4    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 907,
    label = "Ct-Cs_Ct-CO",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cs u0 {1,S}
4    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 908,
    label = "Ct-Cs_Ct-Cd",
    group =
"""
1 *2 Ct u0 {2,T} {3,S}
2 *1 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S} {5,D}
4    Cs u0 {2,S}
5    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 909,
    label = "Ct-Cs_Ct-C=S",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cs u0 {1,S}
4    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 910,
    label = "Ct-De_Ct-H",
    group =
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 Ct                        u0 {1,T} {4,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    H                         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 911,
    label = "Ct-Cb_Ct-H",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cb u0 {1,S}
4    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 912,
    label = "Ct-CO_Ct-H",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    CO u0 {1,S}
4    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 913,
    label = "Ct-Cd_Ct-H",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S} {5,D}
4    H  u0 {2,S}
5    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 914,
    label = "Ct-Ct_Ct-H",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Ct u0 {1,S} {5,T}
4    H  u0 {2,S}
5    Ct u0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 915,
    label = "Ct-C=S_Ct-H",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    CS u0 {1,S}
4    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 916,
    label = "Ct-De_Ct-Cs",
    group =
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 Ct                        u0 {1,T} {4,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cs                        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 917,
    label = "Ct-Cb_Ct-Cs",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cb u0 {1,S}
4    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 918,
    label = "Ct-CO_Ct-Cs",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    CO u0 {1,S}
4    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 919,
    label = "Ct-Cd_Ct-Cs",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S}
4    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 920,
    label = "Ct-Ct_Ct-Cs",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Ct u0 {1,S} {5,T}
4    Cs u0 {2,S}
5    C  u0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 921,
    label = "Ct-CS_Ct-Cs",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    CS u0 {1,S}
4    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 922,
    label = "Ct-De_Ct-De",
    group =
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 Ct                        u0 {1,T} {4,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 923,
    label = "Ct-Ct_Ct-Ct",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Ct u0 {1,S}
4    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 924,
    label = "Ct-Cd_Ct-Ct",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S} {5,D}
4    Ct u0 {2,S}
5    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 925,
    label = "Ct-Ct_Ct-Cd",
    group =
"""
1 *2 Ct u0 {2,T} {3,S}
2 *1 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S} {5,D}
4    Ct u0 {2,S}
5    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 926,
    label = "Ct-Cd_Ct-Cd",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S} {5,D}
4    Cd u0 {2,S} {6,D}
5    C  u0 {3,D}
6    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 927,
    label = "Ct-Cd_Ct-Cd_cyc6",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S} {5,D}
4    Cd u0 {2,S} {6,D}
5    Cd u0 {3,D} {6,S}
6    Cd u0 {4,D} {5,S}
""",
    kinetics = None,
)

entry(
    index = 928,
    label = "Ct-De_Ct-Cb",
    group =
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 Ct                        u0 {1,T} {4,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cb                        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 929,
    label = "Ct-Cd_Ct-Cb",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S}
4    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 930,
    label = "Ct-CdCdCb_Ct-Cb_cyc6",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S} {5,D}
4    Cb u0 {2,S} {6,B}
5    Cd u0 {3,D} {6,S}
6    Cb u0 {4,B} {5,S}
""",
    kinetics = None,
)

entry(
    index = 931,
    label = "Ct-Cb_Ct-Cd",
    group =
"""
1 *1 Ct u0 {2,T} {4,S}
2 *2 Ct u0 {1,T} {3,S}
3    Cd u0 {2,S}
4    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 932,
    label = "Ct-Cb_Ct-CdCdCb_cyc6",
    group =
"""
1 *2 Ct u0 {2,T} {3,S}
2 *1 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S} {5,D}
4    Cb u0 {2,S} {6,B}
5    Cd u0 {3,D} {6,S}
6    Cb u0 {4,B} {5,S}
""",
    kinetics = None,
)

entry(
    index = 933,
    label = "Ct-Cb_Ct-CdCb_cyc5",
    group =
"""
1 *1 Ct u0 {2,T} {4,S}
2 *2 Ct u0 {1,T} {3,S}
3    Cd u0 {2,S} {5,S}
4    Cb u0 {1,S} {5,B}
5    Cb u0 {3,S} {4,B}
""",
    kinetics = None,
)

entry(
    index = 934,
    label = "Ct-O_Ct",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T}
3    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 935,
    label = "Ct-O_Ct-Cb",
    group =
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    O  u0 {1,S}
4    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 936,
    label = "Ct_Nt",
    group =
"""
1 *1 Ct         u0 {2,T}
2 *2 [N3t,N5tc] u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 937,
    label = "Ct_N3t",
    group =
"""
1 *1 Ct  u0 {2,T}
2 *2 N3t u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 938,
    label = "Ct-H_N3t",
    group =
"""
1 *1 Ct  u0 {2,T} {3,S}
2 *2 N3t u0 {1,T}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 939,
    label = "Ct-NonDe_N3t",
    group =
"""
1 *1 Ct                    u0 {2,T} {3,S}
2 *2 N3t                   u0 {1,T}
3    [Cs,N3s,N5sc,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 940,
    label = "Ct-OneDe_N3t",
    group =
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 N3t                       u0 {1,T}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 941,
    label = "Ct_N5t",
    group =
"""
1 *1 Ct   u0 {2,T}
2 *2 N5tc u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 942,
    label = "Od_R",
    group =
"""
1 *1 O2d u0 {2,D}
2 *2 R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 943,
    label = "Od_CO",
    group =
"""
1 *2 C   u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    R   u0 {1,S}
4    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 944,
    label = "Od_CO-HH",
    group =
"""
1 *2 CO  u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 945,
    label = "Od_CO-NdH",
    group =
"""
1 *2 CO           u0 {2,D} {3,S} {4,S}
2 *1 O2d          u0 {1,D}
3    [Cs,O2s,S2s] u0 {1,S}
4    H            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 946,
    label = "Od_CO-CsH",
    group =
"""
1 *2 CO  u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 947,
    label = "Od_CO-NdNd",
    group =
"""
1 *2 CO           u0 {2,D} {3,S} {4,S}
2 *1 O2d          u0 {1,D}
3    [Cs,O2s,S2s] u0 {1,S}
4    [Cs,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 948,
    label = "Od_CO-CsCs",
    group =
"""
1 *2 CO  u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 949,
    label = "Od_CO-DeH",
    group =
"""
1 *2 CO               u0 {2,D} {3,S} {4,S}
2 *1 O2d              u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 950,
    label = "Od_CO-CdH",
    group =
"""
1 *2 CO  u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    Cd  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 951,
    label = "Od_CO-CtH",
    group =
"""
1 *2 CO  u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 952,
    label = "Od_CO-DeNd",
    group =
"""
1 *2 CO               u0 {2,D} {3,S} {4,S}
2 *1 O2d              u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O2s,S2s]     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 953,
    label = "Od_CO-CdCs",
    group =
"""
1 *2 CO  u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    Cd  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 954,
    label = "Od_CO-CtCs",
    group =
"""
1 *2 CO  u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 955,
    label = "Od_Cdd",
    group =
"""
1 *2 C   u0 {2,D} {3,D}
2 *1 O2d u0 {1,D}
3    R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 956,
    label = "Od_Cdd-O2d",
    group =
"""
1 *1 O2d u0 {2,D}
2 *2 C   u0 {1,D} {3,D}
3    O   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 957,
    label = "Od_Nd",
    group =
"""
1 *1 O2d u0 {2,D}
2 *2 N   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 958,
    label = "Od_N3d",
    group =
"""
1 *1 O2d u0 {2,D}
2 *2 N3d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 959,
    label = "Od_N5dc",
    group =
"""
1 *1 O2d  u0 {2,D}
2 *2 N5dc u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 960,
    label = "Nd_R",
    group = "OR{N1dc_R, N3d_R}",
    kinetics = None,
)

entry(
    index = 961,
    label = "N1dc_R",
    group =
"""
1 *1 N1dc u0 p2 {2,D}
2 *2 R!H  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 962,
    label = "N3d_R",
    group =
"""
1 *1 N3d u0 {2,D}
2 *2 R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 963,
    label = "N3d_Cd",
    group =
"""
1 *1 N3d      u0 {2,D}
2 *2 [Cd,Cdd] u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 964,
    label = "N3d_Cds",
    group =
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 N3d u0 {1,D}
3    R   u0 {1,S}
4    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 965,
    label = "N3d-H_Cds",
    group =
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 N3d u0 {1,D} {5,S}
3    R   u0 {1,S}
4    R   u0 {1,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 966,
    label = "N3d-H_Cds-HH",
    group =
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 N3d u0 {1,D} {5,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 967,
    label = "N3d-H_Cds-NonDeH",
    group =
"""
1 *2 Cd                    u0 {2,D} {3,S} {4,S}
2 *1 N3d                   u0 {1,D} {5,S}
3    [Cs,O2s,S2s,N3s,N5sc] u0 {1,S}
4    H                     u0 {1,S}
5    H                     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 968,
    label = "N3d-H_Cds-NonDe2",
    group =
"""
1 *2 Cd                    u0 {2,D} {3,S} {4,S}
2 *1 N3d                   u0 {1,D} {5,S}
3    [Cs,O2s,S2s,N3s,N5sc] u0 {1,S}
4    [Cs,O2s,S2s,N3s,N5sc] u0 {1,S}
5    H                     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 969,
    label = "N3d-NonDe_Cds",
    group =
"""
1 *2 Cd                    u0 {2,D} {3,S} {4,S}
2 *1 N3d                   u0 {1,D} {5,S}
3    R!H                   u0 {1,S}
4    R!H                   u0 {1,S}
5    [Cs,N3s,N5sc,O2s,S2s] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 970,
    label = "N3d-OneDe_Cds",
    group =
"""
1 *2 Cd                        u0 {2,D} {3,S} {4,S}
2 *1 N3d                       u0 {1,D} {5,S}
3    R!H                       u0 {1,S}
4    R!H                       u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 971,
    label = "N3d_Cdd",
    group =
"""
1 *1 N3d u0 {2,D}
2 *2 Cdd u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 972,
    label = "N3d_Od",
    group =
"""
1 *1 N3d u0 {2,D}
2 *2 O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 973,
    label = "N3d-H_Od",
    group =
"""
1 *1 N3d u0 {2,D} {3,S}
2 *2 O2d u0 {1,D}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 974,
    label = "N3d-NonDe_Od",
    group =
"""
1 *1 N3d              u0 {2,D} {3,S}
2 *2 O2d              u0 {1,D}
3    [Cs,N3s,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 975,
    label = "N3d-OneDe_Od",
    group =
"""
1 *1 N3d                       u0 {2,D} {3,S}
2 *2 O2d                       u0 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 976,
    label = "N3d_Nd",
    group =
"""
1 *1 N3d u0 {2,D}
2 *2 N   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 977,
    label = "N3d_N3d",
    group =
"""
1 *1 N3d u0 {2,D}
2 *2 N3d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 978,
    label = "N3d-H_N3d",
    group =
"""
1 *1 N3d u0 {2,D} {3,S}
2 *2 N3d u0 {1,D}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 979,
    label = "N3d-H_N3d-H",
    group =
"""
1 *1 N3d u0 {2,D} {3,S}
2 *2 N3d u0 {1,D} {4,S}
3    H   u0 {1,S}
4    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 980,
    label = "N3d-H_N3d-NonDe",
    group =
"""
1 *1 N3d              u0 {2,D} {3,S}
2 *2 N3d              u0 {1,D} {4,S}
3    H                u0 {1,S}
4    [Cs,N3s,O2s,S2s] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 981,
    label = "N3d-H_N3d-OneDe",
    group =
"""
1 *1 N3d                       u0 {2,D} {3,S}
2 *2 N3d                       u0 {1,D} {4,S}
3    H                         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 982,
    label = "N3d-NonDe_N3d",
    group =
"""
1 *1 N3d              u0 {2,D} {3,S}
2 *2 N3d              u0 {1,D}
3    [Cs,N3s,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 983,
    label = "N3d-OneDe_N3d",
    group =
"""
1 *1 N3d                       u0 {2,D} {3,S}
2 *2 N3d                       u0 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 984,
    label = "N3d_N5dc",
    group =
"""
1 *1 N3d         u0 {2,D}
2 *2 [N5dc,N5tc] u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 985,
    label = "Nt_R",
    group = "OR{N3t_R, N5t_R}",
    kinetics = None,
)

entry(
    index = 986,
    label = "N3t_R",
    group =
"""
1 *1 N3t u0 {2,T}
2 *2 R!H u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 987,
    label = "N3t_Ct",
    group =
"""
1 *1 N3t u0 {2,T}
2 *2 Ct  u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 988,
    label = "N3t_Ct-H",
    group =
"""
1 *2 Ct  u0 {2,T} {3,S}
2 *1 N3t u0 {1,T}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 989,
    label = "N3t_Ct-NonDe",
    group =
"""
1 *2 Ct                    u0 {2,T} {3,S}
2 *1 N3t                   u0 {1,T}
3    [Cs,N3s,N5sc,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 990,
    label = "N3t_Ct-OneDe",
    group =
"""
1 *2 Ct                        u0 {2,T} {3,S}
2 *1 N3t                       u0 {1,T}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 991,
    label = "N3t_N3t",
    group =
"""
1 *1 N3t u0 {2,T}
2 *2 N3t u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 992,
    label = "N5t_R",
    group =
"""
1 *1 N5tc u0 {2,T}
2 *2 R!H  u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 993,
    label = "Sd_R",
    group =
"""
1 *1 S   u0 {2,D}
2 *2 R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 994,
    label = "Sd_Cdd",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2 *2 Cdd u0 {1,D} {3,D}
3    R!H u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 995,
    label = "Sd_Cdd-S2d",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2 *2 Cdd u0 {1,D} {3,D}
3    S2d u0 p2 {2,D}
""",
    kinetics = None,
)

entry(
    index = 996,
    label = "Sd_Cd",
    group =
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    R   u0 {1,S}
4    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 997,
    label = "Sd_Cds-HH",
    group =
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 998,
    label = "Sd_Cds-CsH",
    group =
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 999,
    label = "Sd_Cds-OsH",
    group =
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    O2s u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1000,
    label = "Sd_Cds-OsCs",
    group =
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    O2s u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1001,
    label = "Sd_Cds-CsCs",
    group =
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1002,
    label = "Sd_Cds-OneDeH",
    group =
"""
1 *2 CS                        u0 {2,D} {3,S} {4,S}
2 *1 S2d                       u0 p2 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    H                         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1003,
    label = "Sd_Cds-CtH",
    group =
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1004,
    label = "Sd_Cds-CbH",
    group =
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1005,
    label = "Sd_Cds-COH",
    group =
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    CO  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1006,
    label = "Sd_Cds-CdH",
    group =
"""
1 *2 CS  u0 {2,S} {3,D} {4,S}
2    Cd  u0 {1,S} {5,D}
3 *1 S2d u0 p2 {1,D}
4    H   u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1007,
    label = "Sd_Cds-C=SH",
    group =
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    CS  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1008,
    label = "Sd_Cds-OneDeCs",
    group =
"""
1 *2 CS                        u0 {2,D} {3,S} {4,S}
2 *1 S2d                       u0 p2 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cs                        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1009,
    label = "Sd_Cds-CtCs",
    group =
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1010,
    label = "Sd_Cds-CbCs",
    group =
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1011,
    label = "Sd_Cds-COCs",
    group =
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    CO  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1012,
    label = "Sd_Cds-CdCs",
    group =
"""
1 *2 CS  u0 {2,S} {3,D} {4,S}
2    Cd  u0 {1,S} {5,D}
3 *1 S2d u0 p2 {1,D}
4    Cs  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1013,
    label = "Sd_Cds-C=SCs",
    group =
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    CS  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1014,
    label = "Sd_Cds-TwoDe",
    group =
"""
1 *2 CS                        u0 {2,D} {3,S} {4,S}
2 *1 S2d                       u0 p2 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1015,
    label = "Sd_Cds-CtCt",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2 *2 CS  u0 {1,D} {3,S} {4,S}
3    Ct  u0 {2,S}
4    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1016,
    label = "Sd_Cds-CtCb",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2 *2 CS  u0 {1,D} {3,S} {4,S}
3    Ct  u0 {2,S}
4    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1017,
    label = "Sd_Cds-CtCO",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2 *2 CS  u0 {1,D} {3,S} {4,S}
3    Ct  u0 {2,S}
4    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1018,
    label = "Sd_Cds-CbCb",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2 *2 CS  u0 {1,D} {3,S} {4,S}
3    Cb  u0 {2,S}
4    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1019,
    label = "Sd_Cds-CbCO",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2 *2 CS  u0 {1,D} {3,S} {4,S}
3    Cb  u0 {2,S}
4    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1020,
    label = "Sd_Cds-COCO",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2 *2 CS  u0 {1,D} {3,S} {4,S}
3    CO  u0 {2,S}
4    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1021,
    label = "Sd_Cds-CdCt",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2 *2 CS  u0 {1,D} {3,S} {4,S}
3    Cd  u0 {2,S} {5,D}
4    Ct  u0 {2,S}
5    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1022,
    label = "Sd_Cds-CdCb",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2 *2 CS  u0 {1,D} {3,S} {4,S}
3    Cd  u0 {2,S} {5,D}
4    Cb  u0 {2,S}
5    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1023,
    label = "Sd_Cds-CdCO",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2 *2 CS  u0 {1,D} {3,S} {4,S}
3    Cd  u0 {2,S} {5,D}
4    CO  u0 {2,S}
5    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1024,
    label = "Sd_Cds-CtC=S",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2 *2 CS  u0 {1,D} {3,S} {4,S}
3    Ct  u0 {2,S}
4    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1025,
    label = "Sd_Cds-CbC=S",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2 *2 CS  u0 {1,D} {3,S} {4,S}
3    Cb  u0 {2,S}
4    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1026,
    label = "Sd_Cds-COC=S",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2 *2 CS  u0 {1,D} {3,S} {4,S}
3    CO  u0 {2,S}
4    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1027,
    label = "Sd_Cds-CdCd",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2 *2 CS  u0 {1,D} {3,S} {4,S}
3    Cd  u0 {2,S} {5,D}
4    Cd  u0 {2,S} {6,D}
5    C   u0 {3,D}
6    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1028,
    label = "Sd_Cds-CdC=S",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2 *2 CS  u0 {1,D} {3,S} {4,S}
3    Cd  u0 {2,S} {5,D}
4    CS  u0 {2,S}
5    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1029,
    label = "Sd_Cds-C=SC=S",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2 *2 CS  u0 {1,D} {3,S} {4,S}
3    CS  u0 {2,S}
4    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1030,
    label = "HJ",
    group =
"""
1 *3 H u1
""",
    kinetics = None,
)

entry(
    index = 1031,
    label = "Y_1centerquadrad",
    group = "OR{C_quintet, C_triplet}",
    kinetics = None,
)

entry(
    index = 1032,
    label = "C_quintet",
    group =
"""
1 *3 C u4 p0
""",
    kinetics = None,
)

entry(
    index = 1033,
    label = "C_triplet",
    group =
"""
1 *3 C u2 p1
""",
    kinetics = None,
)

entry(
    index = 1034,
    label = "Y_1centertrirad",
    group = "OR{N_atom_quartet, N_atom_doublet, CH_quartet, CH_doublet}",
    kinetics = None,
)

entry(
    index = 1035,
    label = "N_atom_quartet",
    group =
"""
1 *3 N u3 p1
""",
    kinetics = None,
)

entry(
    index = 1036,
    label = "N_atom_doublet",
    group =
"""
1 *3 N u1 p2
""",
    kinetics = None,
)

entry(
    index = 1037,
    label = "CH_quartet",
    group =
"""
1 *3 Cs u3 p0 {2,S}
2    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1038,
    label = "CH_doublet",
    group =
"""
1 *3 C u1 p1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1039,
    label = "Y_1centerbirad",
    group =
"""
1 *3 R!H u2
""",
    kinetics = None,
)

entry(
    index = 1040,
    label = "O_atom_triplet",
    group =
"""
1 *3 O u2
""",
    kinetics = None,
)

entry(
    index = 1041,
    label = "SJJ",
    group =
"""
1 *3 S u2
""",
    kinetics = None,
)

entry(
    index = 1042,
    label = "CH2_triplet",
    group =
"""
1 *3 C u2 {2,S} {3,S}
2    H u0 {1,S}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1043,
    label = "CO_birad",
    group =
"""
1 *3 C   u2 {2,D}
2    O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 1044,
    label = "NH_triplet",
    group =
"""
1 *3 N3s u2 {2,S}
2    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1045,
    label = "CJ",
    group =
"""
1 *3 C u1 p0
""",
    kinetics = None,
)

entry(
    index = 1046,
    label = "CbJ",
    group =
"""
1 *3 Cb u1 p0
""",
    kinetics = None,
)

entry(
    index = 1047,
    label = "CtJ",
    group =
"""
1 *3 Ct  u1 p0 {2,T}
2    R!H u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 1048,
    label = "CtJ_Ct",
    group =
"""
1 *3 Ct u1 p0 {2,T}
2    Ct u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 1049,
    label = "CtJ_N3t",
    group =
"""
1 *3 Ct  u1 p0 {2,T}
2    N3t u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 1050,
    label = "C2b",
    group =
"""
1 *3 C u1 p0 {2,T}
2    C u1 {1,T}
""",
    kinetics = None,
)

entry(
    index = 1051,
    label = "C=SJ",
    group =
"""
1 *3 CS u1 p0 {2,S}
2    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1052,
    label = "C=SJ-H",
    group =
"""
1 *3 CS u1 p0 {2,S}
2    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1053,
    label = "C=SJ-Cs",
    group =
"""
1 *3 CS u1 p0 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1054,
    label = "C=SJ-Ct",
    group =
"""
1 *3 CS u1 p0 {2,S}
2    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1055,
    label = "C=SJ-Cb",
    group =
"""
1 *3 CS u1 p0 {2,S}
2    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1056,
    label = "C=SJ-CO",
    group =
"""
1 *3 CS u1 p0 {2,S}
2    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1057,
    label = "C=SJ-O2s",
    group =
"""
1 *3 CS  u1 p0 {2,S}
2    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1058,
    label = "C=SJ-S2s",
    group =
"""
1 *3 CS  u1 p0 {2,S}
2    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1059,
    label = "C=SJ-Cd",
    group =
"""
1 *3 CS u1 p0 {2,S}
2    Cd u0 {1,S} {3,D}
3    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1060,
    label = "C=SJ-C=S",
    group =
"""
1 *3 CS u1 p0 {2,S}
2    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1061,
    label = "CO_rad",
    group =
"""
1 *3 C u1 p0 {2,D} {3,S}
2    O u0 {1,D}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1062,
    label = "CO_pri_rad",
    group =
"""
1 *3 C u1 p0 {2,D} {3,S}
2    O u0 {1,D}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1063,
    label = "CO_sec_rad",
    group =
"""
1 *3 C   u1 p0 {2,D} {3,S}
2    O   u0 {1,D}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1064,
    label = "CO_rad/NonDe",
    group =
"""
1 *3 C                     u1 p0 {2,D} {3,S}
2    O                     u0 {1,D}
3    [Cs,S2s,N3s,N5sc,O2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1065,
    label = "CO_rad/OneDe",
    group =
"""
1 *3 C                         u1 p0 {2,D} {3,S}
2    O                         u0 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1066,
    label = "CsJ",
    group =
"""
1 *3 C u1 p0 {2,S} {3,S} {4,S}
2    R u0 {1,S}
3    R u0 {1,S}
4    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1067,
    label = "CsJ-HHH",
    group =
"""
1 *3 C u1 p0 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1068,
    label = "CsJ-CsHH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1069,
    label = "CsJ-CsCsH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1070,
    label = "CsJ-CsCsCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1071,
    label = "CsJ-OsHH",
    group =
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1072,
    label = "CsJ-OsCsH",
    group =
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1073,
    label = "CsJ-OsCsCs",
    group =
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1074,
    label = "CsJ-OsOsH",
    group =
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    O2s u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1075,
    label = "CsJ-OsOsCs",
    group =
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    O2s u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1076,
    label = "CsJ-OsOsOs",
    group =
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    O2s u0 {1,S}
4    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1077,
    label = "CsJ-SsHH",
    group =
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1078,
    label = "CsJ-SsCsH",
    group =
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1079,
    label = "CsJ-SsCsCs",
    group =
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1080,
    label = "CsJ-SsSsH",
    group =
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    S2s u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1081,
    label = "CsJ-SsSsCs",
    group =
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    S2s u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1082,
    label = "CsJ-SsSsSs",
    group =
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    S2s u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1083,
    label = "CsJ-NsHH",
    group =
"""
1 *3 C          u1 p0 {2,S} {3,S} {4,S}
2    H          u0 {1,S}
3    H          u0 {1,S}
4    [N3s,N5sc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1084,
    label = "CsJ-NsCsH",
    group =
"""
1 *3 C          u1 p0 {2,S} {3,S} {4,S}
2    H          u0 {1,S}
3    [N3s,N5sc] u0 {1,S}
4    Cs         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1085,
    label = "CsJ-OneDe",
    group =
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    [H,Cs,O2s,S2s,N3s,N5sc]   u0 {1,S}
4    [H,Cs,O2s,S2s,N3s,N5sc]   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1086,
    label = "CsJ-OneDeHH",
    group =
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    H                         u0 {1,S}
4    H                         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1087,
    label = "CsJ-CtHH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1088,
    label = "CsJ-CbHH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1089,
    label = "CsJ-COHH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1090,
    label = "CsJ-CdHH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1091,
    label = "CsJ-(CdC)HH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
6    C  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1092,
    label = "CsJ-C=SHH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1093,
    label = "CsJ-OneDeCsH",
    group =
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    Cs                        u0 {1,S}
4    H                         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1094,
    label = "CsJ-CtCsH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1095,
    label = "CsJ-CbCsH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1096,
    label = "CsJ-COCsH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1097,
    label = "CsJ-CdCsH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1098,
    label = "CsJ-C=SCsH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1099,
    label = "CsJ-OneDeOsH",
    group =
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    O2s                       u0 {1,S}
4    H                         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1100,
    label = "CsJ-OneDeSsH",
    group =
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    S2s                       u0 {1,S}
4    H                         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1101,
    label = "CsJ-OneDeCsCs",
    group =
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    Cs                        u0 {1,S}
4    Cs                        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1102,
    label = "CsJ-CtCsCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1103,
    label = "CsJ-CbCsCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1104,
    label = "CsJ-COCsCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1105,
    label = "CsJ-CdCsCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1106,
    label = "CsJ-C=SCsCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1107,
    label = "CsJ-OneDeOsCs",
    group =
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    O2s                       u0 {1,S}
4    Cs                        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1108,
    label = "CsJ-OneDeSsCs",
    group =
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    S2s                       u0 {1,S}
4    Cs                        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1109,
    label = "CsJ-OneDeOsOs",
    group =
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    O2s                       u0 {1,S}
4    O2s                       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1110,
    label = "CsJ-OneDeOsSs",
    group =
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    O2s                       u0 {1,S}
4    S2s                       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1111,
    label = "CsJ-OneDeSsSs",
    group =
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    S2s                       u0 {1,S}
4    S2s                       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1112,
    label = "CsJ-OneDeNsH",
    group =
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    H                         u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [N3s,N5sc]                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1113,
    label = "CsJ-OneDeNsCs",
    group =
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    Cs                        u0 {1,S}
4    [N3s,N5sc]                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1114,
    label = "CsJ-TwoDe",
    group =
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [H,Cs,O2s,S2s]            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1115,
    label = "CsJ-TwoDeH",
    group =
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    H                         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1116,
    label = "CsJ-CtCtH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1117,
    label = "CsJ-CtCbH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1118,
    label = "CsJ-CtCOH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CO u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1119,
    label = "CsJ-CbCbH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1120,
    label = "CsJ-CbCOH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CO u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1121,
    label = "CsJ-COCOH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CO u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1122,
    label = "CsJ-CdCtH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1123,
    label = "CsJ-CdCbH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1124,
    label = "CsJ-CdCOH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CO u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1125,
    label = "CsJ-CtC=SH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1126,
    label = "CsJ-CbC=SH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1127,
    label = "CsJ-COC=SH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1128,
    label = "CsJ-CdCdH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cd u0 {1,S} {6,D}
4    H  u0 {1,S}
5    C  u0 {2,D}
6    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1129,
    label = "CsJ-CdC=SH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CS u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1130,
    label = "CsJ-C=SC=SH",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1131,
    label = "CsJ-TwoDeCs",
    group =
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cs                        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1132,
    label = "CsJ-CtCtCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1133,
    label = "CsJ-CtCbCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1134,
    label = "CsJ-CtCOCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1135,
    label = "CsJ-CbCbCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1136,
    label = "CsJ-CbCOCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1137,
    label = "CsJ-COCOCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1138,
    label = "CsJ-CdCtCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1139,
    label = "CsJ-CdCbCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1140,
    label = "CsJ-CdCOCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CO u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1141,
    label = "CsJ-CtC=SCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1142,
    label = "CsJ-CbC=SCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1143,
    label = "CsJ-COC=SCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1144,
    label = "CsJ-CdCdCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cd u0 {1,S} {6,D}
4    Cs u0 {1,S}
5    C  u0 {2,D}
6    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1145,
    label = "CsJ-CdC=SCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CS u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1146,
    label = "CsJ-C=SC=SCs",
    group =
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1147,
    label = "CsJ-TwoDeOs",
    group =
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    O2s                       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1148,
    label = "CsJ-TwoDeSs",
    group =
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    S2s                       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1149,
    label = "CsJ-ThreeDe",
    group =
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1150,
    label = "CdsJ=Cdd",
    group =
"""
1 *3 C   u1 p0 {2,D} {3,S}
2    C   u0 {1,D} {4,D}
3    R   u0 {1,S}
4    R!H u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1151,
    label = "CdsJ",
    group =
"""
1    C u0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 {1,D} {5,S}
3    R u0 {1,S}
4    R u0 {1,S}
5    R u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1152,
    label = "CdsJ-H",
    group =
"""
1    C u0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 {1,D} {5,S}
3    R u0 {1,S}
4    R u0 {1,S}
5    H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1153,
    label = "CdsJ-(CdCb)H",
    group =
"""
1 *3 Cd u1 p0 {2,D} {3,S}
2    Cd u0 {1,D} {4,S} {5,S}
3    H  u0 {1,S}
4    Cb u0 {2,S}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1154,
    label = "CdsJ-Cs",
    group =
"""
1    C  u0 {2,D} {3,S} {4,S}
2 *3 C  u1 p0 {1,D} {5,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
5    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1155,
    label = "CdsJ-Ct",
    group =
"""
1    C  u0 {2,D} {3,S} {4,S}
2 *3 C  u1 p0 {1,D} {5,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
5    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1156,
    label = "CdsJ-Cb",
    group =
"""
1    C  u0 {2,D} {3,S} {4,S}
2 *3 C  u1 p0 {1,D} {5,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
5    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1157,
    label = "CdsJ-CO",
    group =
"""
1    C  u0 {2,D} {3,S} {4,S}
2 *3 C  u1 p0 {1,D} {5,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
5    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1158,
    label = "CdsJ-O2s",
    group =
"""
1 *3 C   u1 p0 {2,D} {3,S}
2    C   u0 {1,D} {4,S} {5,S}
3    O2s u0 {1,S}
4    R   u0 {2,S}
5    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1159,
    label = "CdsJ-S2s",
    group =
"""
1 *3 C   u1 p0 {2,D} {3,S}
2    C   u0 {1,D} {4,S} {5,S}
3    S2s u0 {1,S}
4    R   u0 {2,S}
5    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1160,
    label = "CdsJ-Cd",
    group =
"""
1    C  u0 {2,D} {4,S} {5,S}
2 *3 C  u1 p0 {1,D} {3,S}
3    Cd u0 {2,S} {6,D}
4    R  u0 {1,S}
5    R  u0 {1,S}
6    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1161,
    label = "CdsJ-C=S",
    group =
"""
1    C  u0 {2,D} {3,S} {4,S}
2 *3 C  u1 p0 {1,D} {5,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
5    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1162,
    label = "OJ",
    group = "OR{OJ_pri, OJ_sec, O2b}",
    kinetics = None,
)

entry(
    index = 1163,
    label = "OJ_pri",
    group =
"""
1 *3 O u1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1164,
    label = "OJ_sec",
    group =
"""
1 *3 O   u1 {2,S}
2    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1165,
    label = "OJ-NonDe",
    group =
"""
1 *3 O                     u1 {2,S}
2    [Cs,O2s,S2s,N3s,N5sc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1166,
    label = "O_rad/NonDe",
    group =
"""
1 *3 O            u1 {2,S}
2    [Cs,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1167,
    label = "OJ-Cs",
    group =
"""
1 *3 O  u1 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1168,
    label = "OJ-O2s",
    group =
"""
1 *3 O   u1 {2,S}
2    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1169,
    label = "OJ-Ns",
    group =
"""
1 *3 O          u1 {2,S}
2    [N3s,N5sc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1170,
    label = "OJ-OneDe",
    group =
"""
1 *3 O                         u1 {2,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1171,
    label = "O_rad/OneDe",
    group =
"""
1 *3 O                u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1172,
    label = "OJ-OneDeN",
    group =
"""
1 *3 O          u1 {2,S}
2    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1173,
    label = "OJ-NO",
    group =
"""
1 *3 O          u1 {2,S}
2    [N3d,N5dc] u0 {1,S} {3,D}
3    O2d        u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1174,
    label = "O2b",
    group =
"""
1 *3 O u1 {2,S}
2    O u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1175,
    label = "SJ",
    group =
"""
1 *3 S u1
""",
    kinetics = None,
)

entry(
    index = 1176,
    label = "SsJ",
    group =
"""
1 *3 S2s u1 p2 {2,S}
2    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1177,
    label = "SsJ-H",
    group =
"""
1 *3 S2s u1 p2 {2,S}
2    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1178,
    label = "SsJ-Cs",
    group =
"""
1 *3 S2s u1 p2 {2,S}
2    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1179,
    label = "SsJ-S2s",
    group =
"""
1 *3 S2s u1 p2 {2,S}
2    S2s u0 p2 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1180,
    label = "SsJ-OneDe",
    group =
"""
1 *3 S2s                       u1 p2 {2,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1181,
    label = "SsJ-Ct",
    group =
"""
1 *3 S2s u1 p2 {2,S}
2    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1182,
    label = "SsJ-Cb",
    group =
"""
1 *3 S2s u1 p2 {2,S}
2    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1183,
    label = "SsJ-CO",
    group =
"""
1 *3 S2s u1 p2 {2,S}
2    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1184,
    label = "SsJ-Cd",
    group =
"""
1    Cd  u0 {2,S} {3,D}
2 *3 S2s u1 p2 {1,S}
3    C   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 1185,
    label = "SsJ-C=S",
    group =
"""
1 *3 S2s u1 p2 {2,S}
2    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1186,
    label = "NJ",
    group =
"""
1 *3 N u1
""",
    kinetics = None,
)

entry(
    index = 1187,
    label = "N3J",
    group =
"""
1 *3 [N3s,N3d] u1
""",
    kinetics = None,
)

entry(
    index = 1188,
    label = "N3sJ",
    group =
"""
1 *3 N3s u1
""",
    kinetics = None,
)

entry(
    index = 1189,
    label = "NH2J",
    group =
"""
1 *3 N3s u1 {2,S} {3,S}
2    H   u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1190,
    label = "N3sJ-NonDeH",
    group =
"""
1 *3 N3s                   u1 {2,S} {3,S}
2    [O2s,S2s,N3s,N5sc,Cs] u0 {1,S}
3    H                     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1191,
    label = "N3sJ-CsH",
    group =
"""
1 *3 N3s u1 {2,S} {3,S}
2    Cs  u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1192,
    label = "N3sJ-OsH",
    group =
"""
1 *3 N3s u1 {2,S} {3,S}
2    O2s u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1193,
    label = "N3sJ-NsH",
    group =
"""
1 *3 N3s        u1 {2,S} {3,S}
2    [N3s,N5sc] u0 {1,S}
3    H          u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1194,
    label = "N3sJ-NonDe2",
    group =
"""
1 *3 N3s                   u1 {2,S} {3,S}
2    [O2s,Cs,N3s,N5sc,S2s] u0 {1,S}
3    [O2s,Cs,N3s,N5sc,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1195,
    label = "N3sJ-OneDeH",
    group =
"""
1 *3 N3s                       u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    H                         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1196,
    label = "N3sJ-OneDeCs",
    group =
"""
1 *3 N3s                       u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    Cs                        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1197,
    label = "N3sJ-TwoDe",
    group =
"""
1 *3 N3s                       u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1198,
    label = "N3dJ",
    group =
"""
1 *3 N3d u1
""",
    kinetics = None,
)

entry(
    index = 1199,
    label = "N3dJ_C",
    group =
"""
1 *3 N3d u1 {2,D}
2    C   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 1200,
    label = "N3dJ_O",
    group =
"""
1 *3 N3d u1 {2,D}
2    O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 1201,
    label = "N3dJ_N",
    group =
"""
1 *3 N3d u1 {2,D}
2    N   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 1202,
    label = "Cb-naphthalene_Cb-naphthalene",
    group =
"""
1 *1 Cbf u0 {2,B} {3,B} {5,B}
2 *2 Cbf u0 {1,B} {4,B} {6,B}
3    [Cb,Cbf] u0 {1,B}
4    [Cb,Cbf] u0 {2,B}
5    [Cb,Cbf] u0 {1,B} {7,B}
6    [Cb,Cbf] u0 {2,B} {8,B}
7    [Cb,Cbf] u0 {5,B} {8,B}
8    [Cb,Cbf] u0 {6,B} {7,B}
""",
    kinetics = None,
)

entry(
    index = 1203,
    label = "Cb-indane_Cb-indane",
    group =
"""
1 *1 Cb u0 {2,B} {3,B} {5,[S,B]}
2 *2 Cb u0 {1,B} {4,B} {6,[S,B]}
3    [Cb,Cbf] u0 {1,B}
4    [Cb,Cbf] u0 {2,B}
5    C      u0 {1,[S,B]} {7,[S,D,T]}
6    C      u0 {2,[S,B]} {7,[S,D,T]}
7    C      u0 {5,[S,D,T]} {6,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 1204,
    label = "Cb-tetralin_Cb-tetralin",
    group =
"""
1 *1 [Cb,Cbf] u0 {2,B} {3,B} {5,[S,B]}
2 *2 [Cb,Cbf] u0 {1,B} {4,B} {6,[S,B]}
3    [Cb,Cbf] u0 {1,B}
4    [Cb,Cbf] u0 {2,B}
5    C      u0 {1,[S,B]} {7,[S,D,B]}
6    C      u0 {2,[S,B]} {8,[S,D,B]}
7    C      u0 {5,[S,D,B]} {8,[S,D,B]}
8    C      u0 {6,[S,D,B]} {7,[S,D,B]}
""",
    kinetics = None,
)

entry(
    index = 1205,
    label = "Cds-CsH_Cds-CbH-indene",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S} {7,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S} {7,B}
7    Cb u0 {3,S} {6,B}
""",
    kinetics = None,
)

entry(
    index = 1206,
    label = "Cds-CsH_Cds-CbH-dihydronaphthalene",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S} {8,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S} {7,B}
7    Cb u0 {6,B} {8,S}
8    Cs u0 {7,S} {3,S}
""",
    kinetics = None,
)


entry(
    index = 1207,
    label = "Cds-CsH_Cds-CbCs-dihydronaphthalene",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S} {8,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S} {7,B}
7    Cb u0 {6,B} {8,S}
8    Cs u0 {3,S} {7,S}
""",
    kinetics = None,
)

entry(
    index = 1208,
    label = "Cb-H-Ortho_Cb-C-fused",
    group =
"""
1 *1 Cb       u0 {2,B} {3,S}
2 *2 Cb       u0 {1,B} {4,S} {5,B}
3    H        u0 {1,S}
4    C        u0 {2,S}
5    Cbf      u0 {2,B}
""",
    kinetics = None,
)

entry(
    index = 1209,
    label = "Cb-H-Para_Cb-H-fused",
    group =
"""
1 *1 Cb       u0 {2,B} {7,S} {9,B}
2 *2 Cb       u0 {1,B} {4,B} {6,S}
3    Cb u0 {4,B} {5,S} {8,B}
4    Cb u0 {2,B} {3,B}
5    R!H      u0 {3,S}
6    H        u0 {2,S}
7    H        u0 {1,S}
8    Cbf      u0 {3,B} {9,B} {10,B}
9    Cbf      u0 {8,B} {1,B} {11,B}
10   Cb       u0 {8,B}
11   Cb       u0 {9,B}
""",
    kinetics = None,
)

entry(
    index = 1210,
    label = "Cb-H_Cb-CbfH",
    group =
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {4,S} {5,B}
3    H  u0 {1,S}
4    H  u0 {2,S}
5    Cbf u0 {2,B}
""",
    kinetics = None,
)

entry(
    index = 1211,
    label = "Cb-R!H_Cbf-R!H",
    group =
"""
1 *1 [Cb,Cbf] u0 {2,B} {3,B} {5,[S,B]}
2 *2 Cbf u0 {1,B} {4,B} {6,[S,B]}
3    [Cb,Cbf] u0 {1,B}
4    [Cb,Cbf] u0 {2,B}
5    R!H      u0 {1,[S,B]}
6    R!H      u0 {2,[S,B]}
""",
    kinetics = None,
)

entry(
    index = 1212,
    label = "LiJ",
    group =
"""
1 *3 Li u1
""",
    kinetics = None,
)

tree(
"""
L1: R_R
    L2: Cb_Cb
        L3: Cb-R!H_Cb
            L4: Cb-R!H_Cb-R!H
                L5: Cb-indane_Cb-indane
                    L6: Cb-indeneDe_Cb-indeneNde
                    L6: Cb-indeneNde_Cb-indene_De
                L5: Cb-benzofuranNde_Cb-benzofuranDe
                L5: Cb-tetralin_Cb-tetralin
                    L6: Cb-naphthalene_Cb-naphthalene
                L5: Cb-R!H_Cbf-R!H
            L4: Cb-R!H_Cb-H
                L5: Cb-C-cyclic_Cb-H
                    L6: Cbf-Cb-cyclic_Cb-H
                L5: Cb-Cd_Cb-H
                L5: Cb-Cs_Cb-H
        L3: Cb-H_Cb
            L4: Cb-H_Cb-R!H
                L5: Cb-H_Cb-indeneNde
                L5: Cb-H_Cbf-Cb
                L5: Cb-H-Ortho_Cb-C
                    L6: Cb-H-Ortho_Cb-C-fused
            L4: Cb-H_Cb-H
                L5: Cb-H-Meta_Cb-H
                L5: Cb-H-Para_Cb-H
                    L6: Cb-H-Para_Cb-H-fused
                L5: Cb-H_Cb-H_o_ketene
                L5: Cb-H_Cb-CbfH
    L2: Cd_R
        L3: Cdd_Od
            L4: CO2
            L4: Ck_O
            L4: C=S_O
            L4: Cdd_Od-N3d
        L3: CO_O
            L4: CO-HH_O
            L4: CO-NdH_O
                L5: CO-CsH_O
            L4: CO-DeH_O
                L5: CO-CdH_O
                L5: CO-CtH_O
            L4: CO-NdNd_O
                L5: CO-CsCs_O
            L4: CO-DeNd_O
                L5: CO-CdCs_O
                L5: CO-CtCs_O
            L4: CO-DeDe_O
        L3: Cdd_Sd
            L4: Cdd-Sd_Sd
        L3: Cds_Cdd
            L4: Cds_Ca
                L5: Cds-HH_Ca
                L5: Cds-CsH_Ca
                L5: Cds-CsCs_Ca
                L5: Cds-OneDeH_Ca
                    L6: Cds-CtH_Ca
                    L6: Cds-CbH_Ca
                    L6: Cds-COH_Ca
                    L6: Cds-CdH_Ca
                    L6: Cds-C=SH_Ca
                L5: Cds-OneDeCs_Ca
                    L6: Cds-CtCs_Ca
                    L6: Cds-CbCs_Ca
                    L6: Cds-COCs_Ca
                    L6: Cds-CdCs_Ca
                    L6: Cds-C=SCs_Ca
                L5: Cds-TwoDe_Ca
                    L6: Cds-CtCt_Ca
                    L6: Cds-CtCb_Ca
                    L6: Cds-CtCO_Ca
                    L6: Cds-CbCb_Ca
                    L6: Cds-CbCO_Ca
                    L6: Cds-COCO_Ca
                    L6: Cds-CdCt_Ca
                    L6: Cds-CdCb_Ca
                    L6: Cds-CdCO_Ca
                    L6: Cds-CtC=S_Ca
                    L6: Cds-CbC=S_Ca
                    L6: Cds-COC=S_Ca
                    L6: Cds-CdCd_Ca
                    L6: Cds-CdC=S_Ca
                    L6: Cds-C=SC=S_Ca
            L4: Cds_Ck
                L5: Cds-HH_Ck
                L5: Cds-CsH_Ck
                L5: Cds-CsCs_Ck
                L5: Cds-OneDeH_Ck
                L5: Cds-OneDeCs_Ck
                L5: Cds-TwoDe_Ck
        L3: Cdd_Cds
            L4: Ca_Cds
                L5: Ca_Cds-HH
                    L6: Ca-Cdd_Cds-HH
                L5: Ca_Cds-CsH
                L5: Ca_Cds-CsCs
                L5: Ca_Cds-OneDeH
                    L6: Ca_Cds-CtH
                    L6: Ca_Cds-CbH
                    L6: Ca_Cds-COH
                    L6: Ca_Cds-CdH
                    L6: Ca_Cds-C=SH
                L5: Ca_Cds-OneDeCs
                    L6: Ca_Cds-CtCs
                    L6: Ca_Cds-CbCs
                    L6: Ca_Cds-COCs
                    L6: Ca_Cds-CdCs
                    L6: Ca_Cds-C=SCs
                L5: Ca_Cds-TwoDe
                    L6: Ca_Cds-CtCt
                    L6: Ca_Cds-CtCb
                    L6: Ca_Cds-CtCO
                    L6: Ca_Cds-CbCb
                    L6: Ca_Cds-CbCO
                    L6: Ca_Cds-COCO
                    L6: Ca_Cds-CdCt
                    L6: Ca_Cds-CdCb
                    L6: Ca_Cds-CdCO
                    L6: Ca_Cds-CtC=S
                    L6: Ca_Cds-CbC=S
                    L6: Ca_Cds-COC=S
                    L6: Ca_Cds-CdCd
                        L7: Ca_Cds-CdCdCdCdCd_cycle
                    L6: Ca_Cds-CdC=S
                    L6: Ca_Cds-C=SC=S
            L4: Ck_Cds
                L5: Ck_Cds-HH
                L5: Ck_Cds-CsH
                L5: Ck_Cds-CsCs
                L5: Ck_Cds-OneDeH
                    L6: Ck_Cds-CtH
                    L6: Ck_Cds-CbH
                    L6: Ck_Cds-COH
                    L6: Ck_Cds-CdH
                    L6: Ck_Cds-C=SH
                L5: Ck_Cds-OneDeCs
                    L6: Ck_Cds-CtCs
                    L6: Ck_Cds-CbCs
                    L6: Ck_Cds-COCs
                    L6: Ck_Cds-CdCs
                    L6: Ck_Cds-C=SCs
                L5: Ck_Cds-TwoDe
                    L6: Ck_Cds-CtCt
                    L6: Ck_Cds-CtCb
                    L6: Ck_Cds-CtCO
                    L6: Ck_Cds-CbCb
                    L6: Ck_Cds-CbCO
                    L6: Ck_Cds-COCO
                    L6: Ck_Cds-CdCt
                    L6: Ck_Cds-CdCb
                    L6: Ck_Cds-CdCO
                    L6: Ck_Cds-CtC=S
                    L6: Ck_Cds-CbC=S
                    L6: Ck_Cds-COC=S
                    L6: Ck_Cds-CdCd
                    L6: Ck_Cds-CdC=S
                    L6: Ck_Cds-C=SC=S
        L3: Cdd_Cdd
            L4: Ca_Ca
                L5: Ca-Cb_Ca-Cb_cyc6
            L4: Ck_Ck
            L4: Ca_Ck
            L4: Ck_Ca
        L3: Cds_Sd
            L4: Cds-HH_Sd
            L4: Cds-CsH_Sd
            L4: Cds-CsCs_Sd
            L4: Cds-OsH_Sd
            L4: Cds-OsCs_Sd
            L4: Cds-SsH_Sd
            L4: Cds-SsCs_Sd
            L4: Cds-OneDeH_Sd
                L5: Cds-CtH_Sd
                L5: Cds-CbH_Sd
                L5: Cds-COH_Sd
                L5: Cds-CdH_Sd
                L5: Cds-C=SH_Sd
            L4: Cds-OneDeCs_Sd
                L5: Cds-CtCs_Sd
                L5: Cds-CbCs_Sd
                L5: Cds-COCs_Sd
                L5: Cds-CdCs_Sd
                L5: Cds-C=SCs_Sd
            L4: Cds-TwoDe_Sd
                L5: Cds-CtCt_Sd
                L5: Cds-CtCb_Sd
                L5: Cds-CtCO_Sd
                L5: Cds-CbCb_Sd
                L5: Cds-CbCO_Sd
                L5: Cds-COCO_Sd
                L5: Cds-CdCt_Sd
                L5: Cds-CdCb_Sd
                L5: Cds-CdCO_Sd
                L5: Cds-CtC=S_Sd
                L5: Cds-CbC=S_Sd
                L5: Cds-COC=S_Sd
                L5: Cds-CdCd_Sd
                L5: Cds-CdC=S_Sd
                L5: Cds-C=SC=S_Sd
        L3: Cds_Nd
            L4: Cds_N3d
                L5: Cds-HH_N3d
                L5: Cds-NonDeH_N3d
                L5: Cds-NonDe2_N3d
        L3: Cds_Cds
            L4: Cds-HH_Cds
                L5: Cds-HH_Cds-HH
                L5: Cds-HH_Cds-CsH
                    L6: Cds-HH_Cds-Cs\O2s/H
                    L6: Cds-HH_Cds-Cs\H3/H
                L5: Cds-HH_Cds-CsCs
                L5: Cds-HH_Cds-OsH
                L5: Cds-HH_Cds-OsCs
                L5: Cds-HH_Cds-OsOs
                L5: Cds-HH_Cds-SsH
                L5: Cds-HH_Cds-SsCs
                L5: Cds-HH_Cds-SsOs
                L5: Cds-HH_Cds-SsSs
                L5: Cds-HH_Cds-OneDe
                    L6: Cds-HH_Cds-OneDeH
                        L7: Cds-HH_Cds-CtH
                        L7: Cds-HH_Cds-CbH
                        L7: Cds-HH_Cds-COH
                        L7: Cds-HH_Cds-(Cd-Cd-Cb)H
                        L7: Cds-HH_Cds-CdH
                        L7: Cds-HH_Cds-C=SH
                    L6: Cds-HH_Cds-OneDeCs
                        L7: Cds-HH_Cds-CtCs
                        L7: Cds-HH_Cds-CbCs
                        L7: Cds-HH_Cds-COCs
                        L7: Cds-HH_Cds-CdCs
                        L7: Cds-HH_Cds-C=SCs
                    L6: Cds-HH_Cds-OneDeOs
                        L7: Cds-HH_Cds-CtOs
                        L7: Cds-HH_Cds-CbOs
                        L7: Cds-HH_Cds-COOs
                        L7: Cds-HH_Cds-CdOs
                        L7: Cds-HH_Cds-C=SOs
                    L6: Cds-HH_Cds-OneDeSs
                        L7: Cds-HH_Cds-CtSs
                        L7: Cds-HH_Cds-CbSs
                        L7: Cds-HH_Cds-COSs
                        L7: Cds-HH_Cds-CdSs
                        L7: Cds-HH_Cds-C=SSs
                L5: Cds-HH_Cds-TwoDe
                    L6: Cds-HH_Cds-CtCt
                    L6: Cds-HH_Cds-CtCb
                    L6: Cds-HH_Cds-CtCO
                    L6: Cds-HH_Cds-CbCb
                    L6: Cds-HH_Cds-CbCO
                    L6: Cds-HH_Cds-COCO
                    L6: Cds-HH_Cds-CdCt
                    L6: Cds-HH_Cds-CdCb
                        L7: Cds-HH_Cds-CdCbCbCdCdCd_cycle
                    L6: Cds-HH_Cds-CdCO
                    L6: Cds-HH_Cds-CtC=S
                    L6: Cds-HH_Cds-CbC=S
                    L6: Cds-HH_Cds-COC=S
                    L6: Cds-HH_Cds-CdCd
                        L7: Cds-HH_Cds-CdCd_cyc
                    L6: Cds-HH_Cds-CdC=S
                    L6: Cds-HH_Cds-C=SC=S
            L4: Cds-CsH_Cds
                L5: Cds-CsH_Cds-HH
                    L6: Cds-Cs\O2s/H_Cds-HH
                L5: Cds-CsH_Cds-CsH
                    L6: Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6
                L5: Cds-CsH_Cds-CsCs
                L5: Cds-CsH_Cds-OsH
                L5: Cds-CsH_Cds-OsCs
                L5: Cds-CsH_Cds-OsOs
                L5: Cds-CsH_Cds-SsH
                L5: Cds-CsH_Cds-SsCs
                L5: Cds-CsH_Cds-SsOs
                L5: Cds-CsH_Cds-SsSs
                L5: Cds-CsH_Cds-OneDe
                    L6: Cds-CsH_Cds-OneDeH
                        L7: Cds-CsH_Cds-CtH
                        L7: Cds-CsH_Cds-CbH
                            L8: Cds-CsH_Cds-CbH-indene
                            L8: Cds-CsH_Cds-CbH-dihydronaphthalene
                        L7: Cds-CsH_Cds-COH
                        L7: Cds-CsH_Cds-(Cd-Cd-Cd-Cd-Cd)H
                        L7: Cds-CsH_Cds-(Cd-Cd-Cd)H
                        L7: Cds-CsH_Cds-Cd(Cd)H
                        L7: Cds-CsH_Cds-CdH
                            L8: Cds-CsH_Cds-(CdsH-Cds)_cyc5
                        L7: Cds-CsH_Cds-C=SH
                    L6: Cds-CsH_Cds-OneDeCs
                        L7: Cds-CsH_Cds-CtCs
                        L7: Cds-CsH_Cds-CbCs
                            L8: Cds-CsH_Cds-CbCs-dihydronaphthalene
                        L7: Cds-CsH_Cds-COCs
                        L7: Cds-CsH_Cds-CdCs
                        L7: Cds-CsH_Cds-C=SCs
                    L6: Cds-CsH_Cds-OneDeOs
                        L7: Cds-CsH_Cds-CtOs
                        L7: Cds-CsH_Cds-CbOs
                        L7: Cds-CsH_Cds-COOs
                        L7: Cds-CsH_Cds-CdOs
                        L7: Cds-CsH_Cds-C=SOs
                    L6: Cds-CsH_Cds-OneDeSs
                        L7: Cds-CsH_Cds-CtSs
                        L7: Cds-CsH_Cds-CbSs
                        L7: Cds-CsH_Cds-COSs
                        L7: Cds-CsH_Cds-CdSs
                        L7: Cds-CsH_Cds-C=SSs
                L5: Cds-CsH_Cds-TwoDe
                    L6: Cds-CsH_Cds-CtCt
                    L6: Cds-CsH_Cds-CtCb
                    L6: Cds-CsH_Cds-CtCO
                    L6: Cds-CsH_Cds-CbCb
                    L6: Cds-CsH_Cds-CbCO
                    L6: Cds-CsH_Cds-COCO
                    L6: Cds-CsH_Cds-CdCt
                    L6: Cds-CsH_Cds-CdCb
                    L6: Cds-CsH_Cds-CdCO
                    L6: Cds-CsH_Cds-CtC=S
                    L6: Cds-CsH_Cds-CbC=S
                    L6: Cds-CsH_Cds-COC=S
                    L6: Cds-CsH_Cds-CdCd
                    L6: Cds-CsH_Cds-CdC=S
                    L6: Cds-CsH_Cds-C=SC=S
            L4: Cds-CsCs_Cds
                L5: Cds-CsCs_Cds-HH
                L5: Cds-CsCs_Cds-CsH
                L5: Cds-CsCs_Cds-CsCs
                L5: Cds-CsCs_Cds-OsH
                L5: Cds-CsCs_Cds-OsCs
                L5: Cds-CsCs_Cds-OsOs
                L5: Cds-CsCs_Cds-SsH
                L5: Cds-CsCs_Cds-SsCs
                L5: Cds-CsCs_Cds-SsOs
                L5: Cds-CsCs_Cds-SsSs
                L5: Cds-CsCs_Cds-OneDe
                    L6: Cds-CsCs_Cds-OneDeH
                        L7: Cds-CsCs_Cds-CtH
                        L7: Cds-CsCs_Cds-CbH
                        L7: Cds-CsCs_Cds-COH
                        L7: Cds-CsCs_Cds-CdH
                        L7: Cds-CsCs_Cds-C=SH
                    L6: Cds-CsCs_Cds-OneDeCs
                        L7: Cds-CsCs_Cds-CtCs
                        L7: Cds-CsCs_Cds-CbCs
                        L7: Cds-CsCs_Cds-COCs
                        L7: Cds-CsCs_Cds-CdCs
                        L7: Cds-CsCs_Cds-C=SCs
                    L6: Cds-CsCs_Cds-OneDeOs
                        L7: Cds-CsCs_Cds-CtOs
                        L7: Cds-CsCs_Cds-CbOs
                        L7: Cds-CsCs_Cds-COOs
                        L7: Cds-CsCs_Cds-CdOs
                        L7: Cds-CsCs_Cds-C=SOs
                    L6: Cds-CsCs_Cds-OneDeSs
                        L7: Cds-CsCs_Cds-CtSs
                        L7: Cds-CsCs_Cds-CbSs
                        L7: Cds-CsCs_Cds-COSs
                        L7: Cds-CsCs_Cds-CdSs
                        L7: Cds-CsCs_Cds-C=SSs
                L5: Cds-CsCs_Cds-TwoDe
                    L6: Cds-CsCs_Cds-CtCt
                    L6: Cds-CsCs_Cds-CtCb
                    L6: Cds-CsCs_Cds-CtCO
                    L6: Cds-CsCs_Cds-CbCb
                    L6: Cds-CsCs_Cds-CbCO
                    L6: Cds-CsCs_Cds-COCO
                    L6: Cds-CsCs_Cds-CdCt
                    L6: Cds-CsCs_Cds-CdCb
                    L6: Cds-CsCs_Cds-CdCO
                    L6: Cds-CsCs_Cds-CtC=S
                    L6: Cds-CsCs_Cds-CbC=S
                    L6: Cds-CsCs_Cds-COC=S
                    L6: Cds-CsCs_Cds-(Cd-Cd-Cd)Cd
                    L6: Cds-CsCs_Cds-CdCd
                    L6: Cds-CsCs_Cds-CdC=S
                    L6: Cds-CsCs_Cds-C=SC=S
            L4: Cds-SsH_Cds
            L4: Cds-SsCs_Cds
            L4: Cds-SsSs_Cds
            L4: Cds-N3sH_Cds
            L4: Cds-OsH_Cds
                L5: Cds-OsH_Cds-CsH
            L4: Cds-OsCs_Cds
            L4: Cds-OsOs_Cds
            L4: Cds-OsSs_Cds
            L4: Cds-OneDe_Cds
                L5: Cds-OneDeH_Cds
                    L6: Cds-CtH_Cds
                        L7: Cds-CtH_Cds-HH
                        L7: Cds-CtH_Cds-CsH
                        L7: Cds-CtH_Cds-CsCs
                        L7: Cds-CtH_Cds-OsH
                        L7: Cds-CtH_Cds-OsCs
                        L7: Cds-CtH_Cds-OsOs
                        L7: Cds-CtH_Cds-SsH
                        L7: Cds-CtH_Cds-SsCs
                        L7: Cds-CtH_Cds-SsOs
                        L7: Cds-CtH_Cds-SsSs
                        L7: Cds-CtH_Cds-OneDe
                            L8: Cds-CtH_Cds-OneDeH
                                L9: Cds-CtH_Cds-CtH
                                L9: Cds-CtH_Cds-CbH
                                L9: Cds-CtH_Cds-COH
                                L9: Cds-CtH_Cds-CdH
                                L9: Cds-CtH_Cds-C=SH
                            L8: Cds-CtH_Cds-OneDeCs
                                L9: Cds-CtH_Cds-CtCs
                                L9: Cds-CtH_Cds-CbCs
                                L9: Cds-CtH_Cds-COCs
                                L9: Cds-CtH_Cds-CdCs
                                L9: Cds-CtH_Cds-C=SCs
                            L8: Cds-CtH_Cds-OneDeOs
                                L9: Cds-CtH_Cds-CtOs
                                L9: Cds-CtH_Cds-CbOs
                                L9: Cds-CtH_Cds-COOs
                                L9: Cds-CtH_Cds-CdOs
                                L9: Cds-CtH_Cds-C=SOs
                            L8: Cds-CtH_Cds-OneDeSs
                                L9: Cds-CtH_Cds-CtSs
                                L9: Cds-CtH_Cds-CbSs
                                L9: Cds-CtH_Cds-COSs
                                L9: Cds-CtH_Cds-CdSs
                                L9: Cds-CtH_Cds-C=SSs
                        L7: Cds-CtH_Cds-TwoDe
                            L8: Cds-CtH_Cds-CtCt
                            L8: Cds-CtH_Cds-CtCb
                            L8: Cds-CtH_Cds-CtCO
                            L8: Cds-CtH_Cds-CbCb
                            L8: Cds-CtH_Cds-CbCO
                            L8: Cds-CtH_Cds-COCO
                            L8: Cds-CtH_Cds-CdCt
                            L8: Cds-CtH_Cds-CdCb
                            L8: Cds-CtH_Cds-CdCO
                            L8: Cds-CtH_Cds-CtC=S
                            L8: Cds-CtH_Cds-CbC=S
                            L8: Cds-CtH_Cds-COC=S
                            L8: Cds-CtH_Cds-CdCd
                            L8: Cds-CtH_Cds-CdC=S
                            L8: Cds-CtH_Cds-C=SC=S
                    L6: Cds-CbH_Cds
                        L7: Cds-CbH_Cds-HH
                        L7: Cds-CbH_Cds-CsH
                        L7: Cds-CbH_Cds-CsCs
                        L7: Cds-CbH_Cds-OsH
                        L7: Cds-CbH_Cds-OsCs
                        L7: Cds-CbH_Cds-OsOs
                        L7: Cds-CbH_Cds-SsH
                        L7: Cds-CbH_Cds-SsCs
                        L7: Cds-CbH_Cds-SsOs
                        L7: Cds-CbH_Cds-SsSs
                        L7: Cds-CbH_Cds-OneDe
                            L8: Cds-CbH_Cds-OneDeH
                                L9: Cds-CbH_Cds-CtH
                                L9: Cds-CbH_Cds-CbH
                                L9: Cds-CbH_Cds-COH
                                L9: Cds-CbH_Cds-CdH
                                    L10: Cds-CbH_Cds-Cd(CdCb)H
                                L9: Cds-CbH_Cds-C=SH
                            L8: Cds-CbH_Cds-OneDeCs
                                L9: Cds-CbH_Cds-CtCs
                                L9: Cds-CbH_Cds-CbCs
                                L9: Cds-CbH_Cds-COCs
                                L9: Cds-CbH_Cds-CdCs
                                L9: Cds-CbH_Cds-C=SCs
                            L8: Cds-CbH_Cds-OneDeOs
                                L9: Cds-CbH_Cds-CtOs
                                L9: Cds-CbH_Cds-CbOs
                                L9: Cds-CbH_Cds-COOs
                                L9: Cds-CbH_Cds-CdOs
                                L9: Cds-CbH_Cds-C=SOs
                            L8: Cds-CbH_Cds-OneDeSs
                                L9: Cds-CbH_Cds-CtSs
                                L9: Cds-CbH_Cds-CbSs
                                L9: Cds-CbH_Cds-COSs
                                L9: Cds-CbH_Cds-CdSs
                                L9: Cds-CbH_Cds-C=SSs
                        L7: Cds-CbH_Cds-TwoDe
                            L8: Cds-CbH_Cds-CtCt
                            L8: Cds-CbH_Cds-CtCb
                            L8: Cds-CbH_Cds-CtCO
                            L8: Cds-CbH_Cds-CbCb
                            L8: Cds-CbH_Cds-CbCO
                            L8: Cds-CbH_Cds-COCO
                            L8: Cds-CbH_Cds-CdCt
                            L8: Cds-CbH_Cds-CdCb
                            L8: Cds-CbH_Cds-CdCO
                            L8: Cds-CbH_Cds-CtC=S
                            L8: Cds-CbH_Cds-CbC=S
                            L8: Cds-CbH_Cds-COC=S
                            L8: Cds-CbH_Cds-CdCd
                            L8: Cds-CbH_Cds-CdC=S
                            L8: Cds-CbH_Cds-C=SC=S
                    L6: Cds-COH_Cds
                    L6: Cds-CdH_Cds
                        L7: Cds-CdH_Cds-HH
                        L7: Cds-CdH_Cds-CsH
                            L8: Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6
                            L8: Cds-CdH_Cds-(CsH-Cds)_cyc5
                        L7: Cds-CdH_Cds-CsCs
                        L7: Cds-CdH_Cds-OsH
                        L7: Cds-CdH_Cds-OsCs
                        L7: Cds-CdH_Cds-OsOs
                        L7: Cds-CdH_Cds-SsH
                        L7: Cds-CdH_Cds-SsCs
                        L7: Cds-CdH_Cds-SsOs
                        L7: Cds-CdH_Cds-SsSs
                        L7: Cds-CdH_Cds-OneDe
                            L8: Cds-CdH_Cds-OneDeH
                                L9: Cds-CdH_Cds-CtH
                                L9: Cds-CdH_Cds-CbH
                                    L10: Cds(CdCb)-CdH_Cds-CbH_cycle
                                    L10: Cds-CdH_Cds-Cb(Cb)H_cycle
                                L9: Cds-CdH_Cds-COH
                                L9: Cds-CdH_Cds-CdH
                                    L10: Cds-CdH_Cds-CdH_cyc5_1
                                    L10: Cds-CdH_Cds-CdH_cyc5_2
                                L9: Cds-CdH_Cds-C=SH
                            L8: Cds-CdH_Cds-OneDeCs
                                L9: Cds-CdH_Cds-CtCs
                                L9: Cds-CdH_Cds-CbCs
                                L9: Cds-CdH_Cds-COCs
                                L9: Cds-CdH_Cds-CdCs
                                L9: Cds-CdH_Cds-C=SCs
                            L8: Cds-CdH_Cds-OneDeOs
                                L9: Cds-CdH_Cds-CtOs
                                L9: Cds-CdH_Cds-CbOs
                                L9: Cds-CdH_Cds-COOs
                                L9: Cds-CdH_Cds-CdOs
                                L9: Cds-CdH_Cds-C=SOs
                            L8: Cds-CdH_Cds-OneDeSs
                                L9: Cds-CdH_Cds-CtSs
                                L9: Cds-CdH_Cds-CbSs
                                L9: Cds-CdH_Cds-COSs
                                L9: Cds-CdH_Cds-CdSs
                                L9: Cds-CdH_Cds-C=SSs
                            L8: Cds-CdH_Cds-TwoDe
                                L9: Cds-CdH_Cds-CtCt
                                L9: Cds-CdH_Cds-CtCb
                                L9: Cds-CdH_Cds-CtCO
                                L9: Cds-CdH_Cds-CbCb
                                L9: Cds-CdH_Cds-CbCO
                                L9: Cds-CdH_Cds-COCO
                                L9: Cds-CdH_Cds-CdCt
                                L9: Cds-CdH_Cds-CdCb
                                L9: Cds-CdH_Cds-CdCO
                                L9: Cds-CdH_Cds-CtC=S
                                L9: Cds-CdH_Cds-CbC=S
                                L9: Cds-CdH_Cds-COC=S
                                L9: Cds-CdH_Cds-CdCd
                                    L10: Cds-CdH_Cds-CdCd_cyc6
                                        L11: Cds-CdH_Cds-CdCd_cyc6_cyc5
                                L9: Cds-CdH_Cds-CdC=S
                                L9: Cds-CdH_Cds-C=SC=S
                    L6: Cds-C=SH_Cds
                L5: Cds-OneDeCs_Cds
                    L6: Cds-CtCs_Cds
                        L7: Cds-CtCs_Cds-HH
                        L7: Cds-CtCs_Cds-CsH
                        L7: Cds-CtCs_Cds-CsCs
                        L7: Cds-CtCs_Cds-OsH
                        L7: Cds-CtCs_Cds-OsCs
                        L7: Cds-CtCs_Cds-OsOs
                        L7: Cds-CtCs_Cds-SsH
                        L7: Cds-CtCs_Cds-SsCs
                        L7: Cds-CtCs_Cds-SsOs
                        L7: Cds-CtCs_Cds-SsSs
                        L7: Cds-CtCs_Cds-OneDe
                            L8: Cds-CtCs_Cds-OneDeH
                                L9: Cds-CtCs_Cds-CtH
                                L9: Cds-CtCs_Cds-CbH
                                L9: Cds-CtCs_Cds-COH
                                L9: Cds-CtCs_Cds-CdH
                                L9: Cds-CtCs_Cds-C=SH
                            L8: Cds-CtCs_Cds-OneDeCs
                                L9: Cds-CtCs_Cds-CtCs
                                L9: Cds-CtCs_Cds-CbCs
                                L9: Cds-CtCs_Cds-COCs
                                L9: Cds-CtCs_Cds-CdCs
                                L9: Cds-CtCs_Cds-C=SCs
                            L8: Cds-CtCs_Cds-OneDeOs
                                L9: Cds-CtCs_Cds-CtOs
                                L9: Cds-CtCs_Cds-CbOs
                                L9: Cds-CtCs_Cds-COOs
                                L9: Cds-CtCs_Cds-CdOs
                                L9: Cds-CtCs_Cds-C=SOs
                            L8: Cds-CtCs_Cds-OneDeSs
                                L9: Cds-CtCs_Cds-CtSs
                                L9: Cds-CtCs_Cds-CbSs
                                L9: Cds-CtCs_Cds-COSs
                                L9: Cds-CtCs_Cds-CdSs
                                L9: Cds-CtCs_Cds-C=SSs
                        L7: Cds-CtCs_Cds-TwoDe
                            L8: Cds-CtCs_Cds-CtCt
                            L8: Cds-CtCs_Cds-CtCb
                            L8: Cds-CtCs_Cds-CtCO
                            L8: Cds-CtCs_Cds-CbCb
                            L8: Cds-CtCs_Cds-CbCO
                            L8: Cds-CtCs_Cds-COCO
                            L8: Cds-CtCs_Cds-CdCt
                            L8: Cds-CtCs_Cds-CdCb
                            L8: Cds-CtCs_Cds-CdCO
                            L8: Cds-CtCs_Cds-CtC=S
                            L8: Cds-CtCs_Cds-CbC=S
                            L8: Cds-CtCs_Cds-COC=S
                            L8: Cds-CtCs_Cds-CdCd
                            L8: Cds-CtCs_Cds-CdC=S
                            L8: Cds-CtCs_Cds-C=SC=S
                    L6: Cds-CbCs_Cds
                        L7: Cds-CbCs_Cds-HH
                        L7: Cds-CbCs_Cds-CsH
                        L7: Cds-CbCs_Cds-CsCs
                        L7: Cds-CbCs_Cds-OsH
                        L7: Cds-CbCs_Cds-OsCs
                        L7: Cds-CbCs_Cds-OsOs
                        L7: Cds-CbCs_Cds-SsH
                        L7: Cds-CbCs_Cds-SsCs
                        L7: Cds-CbCs_Cds-SsOs
                        L7: Cds-CbCs_Cds-SsSs
                        L7: Cds-CbCs_Cds-OneDe
                            L8: Cds-CbCs_Cds-OneDeH
                                L9: Cds-CbCs_Cds-CtH
                                L9: Cds-CbCs_Cds-CbH
                                L9: Cds-CbCs_Cds-COH
                                L9: Cds-CbCs_Cds-CdH
                                L9: Cds-CbCs_Cds-C=SH
                            L8: Cds-CbCs_Cds-OneDeCs
                                L9: Cds-CbCs_Cds-CtCs
                                L9: Cds-CbCs_Cds-CbCs
                                L9: Cds-CbCs_Cds-COCs
                                L9: Cds-CbCs_Cds-CdCs
                                L9: Cds-CbCs_Cds-C=SCs
                            L8: Cds-CbCs_Cds-OneDeOs
                                L9: Cds-CbCs_Cds-CtOs
                                L9: Cds-CbCs_Cds-CbOs
                                L9: Cds-CbCs_Cds-COOs
                                L9: Cds-CbCs_Cds-CdOs
                                L9: Cds-CbCs_Cds-C=SOs
                            L8: Cds-CbCs_Cds-OneDeSs
                                L9: Cds-CbCs_Cds-CtSs
                                L9: Cds-CbCs_Cds-CbSs
                                L9: Cds-CbCs_Cds-COSs
                                L9: Cds-CbCs_Cds-CdSs
                                L9: Cds-CbCs_Cds-C=SSs
                        L7: Cds-CbCs_Cds-TwoDe
                            L8: Cds-CbCs_Cds-CtCt
                            L8: Cds-CbCs_Cds-CtCb
                            L8: Cds-CbCs_Cds-CtCO
                            L8: Cds-CbCs_Cds-CbCb
                            L8: Cds-CbCs_Cds-CbCO
                            L8: Cds-CbCs_Cds-COCO
                            L8: Cds-CbCs_Cds-CdCt
                            L8: Cds-CbCs_Cds-CdCb
                            L8: Cds-CbCs_Cds-CdCO
                            L8: Cds-CbCs_Cds-CtC=S
                            L8: Cds-CbCs_Cds-CbC=S
                            L8: Cds-CbCs_Cds-COC=S
                            L8: Cds-CbCs_Cds-CdCd
                            L8: Cds-CbCs_Cds-CdC=S
                            L8: Cds-CbCs_Cds-C=SC=S
                    L6: Cds-COCs_Cds
                    L6: Cds-CdCs_Cds
                        L7: Cds-CdCs_Cds-HH
                        L7: Cds-CdCs_Cds-CsH
                        L7: Cds-CdCs_Cds-CsCs
                        L7: Cds-CdCs_Cds-OsH
                        L7: Cds-CdCs_Cds-OsCs
                        L7: Cds-CdCs_Cds-OsOs
                        L7: Cds-CdCs_Cds-SsH
                        L7: Cds-CdCs_Cds-SsCs
                        L7: Cds-CdCs_Cds-SsOs
                        L7: Cds-CdCs_Cds-SsSs
                        L7: Cds-CdCs_Cds-OneDe
                            L8: Cds-CdCs_Cds-OneDeH
                                L9: Cds-CdCs_Cds-CtH
                                L9: Cds-CdCs_Cds-CbH
                                L9: Cds-CdCs_Cds-COH
                                L9: Cds-CdCs_Cds-(Cd-Cd-Cd)H
                                L9: Cds-CdCs_Cds-CdH
                                L9: Cds-CdCs_Cds-C=SH
                            L8: Cds-CdCs_Cds-OneDeCs
                                L9: Cds-CdCs_Cds-CtCs
                                L9: Cds-CdCs_Cds-CbCs
                                L9: Cds-CdCs_Cds-COCs
                                L9: Cds-CdCs_Cds-CdCs
                                L9: Cds-CdCs_Cds-C=SCs
                            L8: Cds-CdCs_Cds-OneDeOs
                                L9: Cds-CdCs_Cds-CtOs
                                L9: Cds-CdCs_Cds-CbOs
                                L9: Cds-CdCs_Cds-COOs
                                L9: Cds-CdCs_Cds-CdOs
                                L9: Cds-CdCs_Cds-C=SOs
                            L8: Cds-CdCs_Cds-OneDeSs
                                L9: Cds-CdCs_Cds-CtSs
                                L9: Cds-CdCs_Cds-CbSs
                                L9: Cds-CdCs_Cds-COSs
                                L9: Cds-CdCs_Cds-CdSs
                                L9: Cds-CdCs_Cds-C=SSs
                            L8: Cds-CdCs_Cds-TwoDe
                                L9: Cds-CdCs_Cds-CtCt
                                L9: Cds-CdCs_Cds-CtCb
                                L9: Cds-CdCs_Cds-CtCO
                                L9: Cds-CdCs_Cds-CbCb
                                L9: Cds-CdCs_Cds-CbCO
                                L9: Cds-CdCs_Cds-COCO
                                L9: Cds-CdCs_Cds-CdCt
                                L9: Cds-CdCs_Cds-CdCb
                                L9: Cds-CdCs_Cds-CdCO
                                L9: Cds-CdCs_Cds-CtC=S
                                L9: Cds-CdCs_Cds-CbC=S
                                L9: Cds-CdCs_Cds-COC=S
                                L9: Cds-CdCs_Cds-CdCd
                                L9: Cds-CdCs_Cds-CdC=S
                                L9: Cds-CdCs_Cds-C=SC=S
                    L6: Cds-C=SCs_Cds
                L5: Cds-OneDeSs_Cds
                    L6: Cds-CtSs_Cds
                    L6: Cds-CbSs_Cds
                    L6: Cds-COSs_Cds
                    L6: Cds-CdSs_Cds
                    L6: Cds-C=SSs_Cds
                L5: Cds-OneDeOs_Cds
                    L6: Cds-CtOs_Cds
                    L6: Cds-CbOs_Cds
                    L6: Cds-COOs_Cds
                    L6: Cds-CdOs_Cds
                    L6: Cds-C=SOs_Cds
            L4: Cds-TwoDe_Cds
                L5: Cds-CtCt_Cds
                    L6: Cds-CtCt_Cds-HH
                    L6: Cds-CtCt_Cds-CsH
                    L6: Cds-CtCt_Cds-CsCs
                    L6: Cds-CtCt_Cds-OsH
                    L6: Cds-CtCt_Cds-OsCs
                    L6: Cds-CtCt_Cds-OsOs
                    L6: Cds-CtCt_Cds-SsH
                    L6: Cds-CtCt_Cds-SsCs
                    L6: Cds-CtCt_Cds-SsOs
                    L6: Cds-CtCt_Cds-SsSs
                    L6: Cds-CtCt_Cds-OneDe
                        L7: Cds-CtCt_Cds-OneDeH
                            L8: Cds-CtCt_Cds-CtH
                            L8: Cds-CtCt_Cds-CbH
                            L8: Cds-CtCt_Cds-COH
                            L8: Cds-CtCt_Cds-CdH
                            L8: Cds-CtCt_Cds-C=SH
                        L7: Cds-CtCt_Cds-OneDeCs
                            L8: Cds-CtCt_Cds-CtCs
                            L8: Cds-CtCt_Cds-CbCs
                            L8: Cds-CtCt_Cds-COCs
                            L8: Cds-CtCt_Cds-CdCs
                            L8: Cds-CtCt_Cds-C=SCs
                        L7: Cds-CtCt_Cds-OneDeOs
                            L8: Cds-CtCt_Cds-CtOs
                            L8: Cds-CtCt_Cds-CbOs
                            L8: Cds-CtCt_Cds-COOs
                            L8: Cds-CtCt_Cds-CdOs
                            L8: Cds-CtCt_Cds-C=SOs
                        L7: Cds-CtCt_Cds-OneDeSs
                            L8: Cds-CtCt_Cds-CtSs
                            L8: Cds-CtCt_Cds-CbSs
                            L8: Cds-CtCt_Cds-COSs
                            L8: Cds-CtCt_Cds-CdSs
                            L8: Cds-CtCt_Cds-C=SSs
                    L6: Cds-CtCt_Cds-TwoDe
                        L7: Cds-CtCt_Cds-CtCt
                        L7: Cds-CtCt_Cds-CtCb
                        L7: Cds-CtCt_Cds-CtCO
                        L7: Cds-CtCt_Cds-CbCb
                        L7: Cds-CtCt_Cds-CbCO
                        L7: Cds-CtCt_Cds-COCO
                        L7: Cds-CtCt_Cds-CdCt
                        L7: Cds-CtCt_Cds-CdCb
                        L7: Cds-CtCt_Cds-CdCO
                        L7: Cds-CtCt_Cds-CtC=S
                        L7: Cds-CtCt_Cds-CbC=S
                        L7: Cds-CtCt_Cds-COC=S
                        L7: Cds-CtCt_Cds-CdCd
                        L7: Cds-CtCt_Cds-CdC=S
                        L7: Cds-CtCt_Cds-C=SC=S
                L5: Cds-CtCb_Cds
                L5: Cds-CtCO_Cds
                L5: Cds-CbCb_Cds
                L5: Cds-CbCO_Cds
                L5: Cds-COCO_Cds
                L5: Cds-CdCt_Cds
                    L6: Cds-CdCt_Cds-HH
                    L6: Cds-CdCt_Cds-CsH
                    L6: Cds-CdCt_Cds-CsCs
                    L6: Cds-CdCt_Cds-OsH
                    L6: Cds-CdCt_Cds-OsCs
                    L6: Cds-CdCt_Cds-OsOs
                    L6: Cds-CdCt_Cds-SsH
                    L6: Cds-CdCt_Cds-SsCs
                    L6: Cds-CdCt_Cds-SsOs
                    L6: Cds-CdCt_Cds-SsSs
                    L6: Cds-CdCt_Cds-OneDe
                        L7: Cds-CdCt_Cds-OneDeH
                            L8: Cds-CdCt_Cds-CtH
                            L8: Cds-CdCt_Cds-CbH
                            L8: Cds-CdCt_Cds-COH
                            L8: Cds-CdCt_Cds-CdH
                            L8: Cds-CdCt_Cds-C=SH
                        L7: Cds-CdCt_Cds-OneDeCs
                            L8: Cds-CdCt_Cds-CtCs
                            L8: Cds-CdCt_Cds-CbCs
                            L8: Cds-CdCt_Cds-COCs
                            L8: Cds-CdCt_Cds-CdCs
                            L8: Cds-CdCt_Cds-C=SCs
                        L7: Cds-CdCt_Cds-OneDeOs
                            L8: Cds-CdCt_Cds-CtOs
                            L8: Cds-CdCt_Cds-CbOs
                            L8: Cds-CdCt_Cds-COOs
                            L8: Cds-CdCt_Cds-CdOs
                            L8: Cds-CdCt_Cds-C=SOs
                        L7: Cds-CdCt_Cds-OneDeSs
                            L8: Cds-CdCt_Cds-CtSs
                            L8: Cds-CdCt_Cds-CbSs
                            L8: Cds-CdCt_Cds-COSs
                            L8: Cds-CdCt_Cds-CdSs
                            L8: Cds-CdCt_Cds-C=SSs
                    L6: Cds-CdCt_Cds-TwoDe
                        L7: Cds-CdCt_Cds-CtCt
                        L7: Cds-CdCt_Cds-CtCb
                        L7: Cds-CdCt_Cds-CtCO
                        L7: Cds-CdCt_Cds-CbCb
                        L7: Cds-CdCt_Cds-CbCO
                        L7: Cds-CdCt_Cds-COCO
                        L7: Cds-CdCt_Cds-CdCt
                        L7: Cds-CdCt_Cds-CdCb
                        L7: Cds-CdCt_Cds-CdCO
                        L7: Cds-CdCt_Cds-CtC=S
                        L7: Cds-CdCt_Cds-CbC=S
                        L7: Cds-CdCt_Cds-COC=S
                        L7: Cds-CdCt_Cds-CdCd
                        L7: Cds-CdCt_Cds-CdC=S
                        L7: Cds-CdCt_Cds-C=SC=S
                L5: Cds-CdCb_Cds
                L5: Cds-CdCO_Cds
                L5: Cds-CtC=S_Cds
                L5: Cds-CbC=S_Cds
                L5: Cds-COC=S_Cds
                L5: Cds-CdCd_Cds
                    L6: Cds-CdCd_Cds-HH
                    L6: Cds-CdCd_Cds-CsH
                    L6: Cds-CdCd_Cds-CsCs
                    L6: Cds-CdCd_Cds-OsH
                    L6: Cds-CdCd_Cds-OsCs
                    L6: Cds-CdCd_Cds-OsOs
                    L6: Cds-CdCd_Cds-SsH
                    L6: Cds-CdCd_Cds-SsCs
                    L6: Cds-CdCd_Cds-SsOs
                    L6: Cds-CdCd_Cds-SsSs
                    L6: Cds-CdCd_Cds-OneDe
                        L7: Cds-CdCd_Cds-OneDeH
                            L8: Cds-CdCd_Cds-CtH
                            L8: Cds-CdCd_Cds-CbH
                            L8: Cds-CdCd_Cds-COH
                            L8: Cds-CdCd_Cds-CdH
                            L8: Cds-CdCd_Cds-C=SH
                        L7: Cds-CdCd_Cds-OneDeCs
                            L8: Cds-CdCd_Cds-CtCs
                            L8: Cds-CdCd_Cds-CbCs
                            L8: Cds-CdCd_Cds-COCs
                            L8: Cds-CdCd_Cds-CdCs
                            L8: Cds-CdCd_Cds-C=SCs
                        L7: Cds-CdCd_Cds-OneDeOs
                            L8: Cds-CdCd_Cds-CtOs
                            L8: Cds-CdCd_Cds-CbOs
                            L8: Cds-CdCd_Cds-COOs
                            L8: Cds-CdCd_Cds-CdOs
                            L8: Cds-CdCd_Cds-C=SOs
                        L7: Cds-CdCd_Cds-OneDeSs
                            L8: Cds-CdCd_Cds-CtSs
                            L8: Cds-CdCd_Cds-CbSs
                            L8: Cds-CdCd_Cds-COSs
                            L8: Cds-CdCd_Cds-CdSs
                            L8: Cds-CdCd_Cds-C=SSs
                    L6: Cds-CdCd_Cds-TwoDe
                        L7: Cds-CdCd_Cds-CtCt
                        L7: Cds-CdCd_Cds-CtCb
                        L7: Cds-CdCd_Cds-CtCO
                        L7: Cds-CdCd_Cds-CbCb
                        L7: Cds-CdCd_Cds-CbCO
                        L7: Cds-CdCd_Cds-COCO
                        L7: Cds-CdCd_Cds-CdCt
                        L7: Cds-CdCd_Cds-CdCb
                        L7: Cds-CdCd_Cds-CdCO
                        L7: Cds-CdCd_Cds-CtC=S
                        L7: Cds-CdCd_Cds-CbC=S
                        L7: Cds-CdCd_Cds-COC=S
                        L7: Cds-CdCd_Cds-CdCd
                        L7: Cds-CdCd_Cds-CdC=S
                        L7: Cds-CdCd_Cds-C=SC=S
                L5: Cds-CdC=S_Cds
                L5: Cds-C=SC=S_Cds
            L4: Cds-OJH_Cds
                L5: Cds-OJH_Cds-HH
                L5: Cds-OJH_Cds-CsH
            L4: Cds-OJNonDe_Cds
                L5: Cds-OJCs_Cds-HH
            L4: Cds-OJDe_Cds
    L2: Ct_R
        L3: Ct_Ct
            L4: Ct-H_Ct-H
            L4: Ct-H_Ct-Cs
            L4: Ct-Cs_Ct-H
            L4: Ct-Cs_Ct-Cs
            L4: Ct-H_Ct-De
                L5: Ct-H_Ct-Ct
                L5: Ct-H_Ct-Cb
                L5: Ct-H_Ct-CO
                L5: Ct-H_Ct-Cd
                    L6: Ct-H_Ct-Cd-C-Cb
                L5: Ct-H_Ct-C=S
            L4: Ct-Cs_Ct-De
                L5: Ct-Cs_Ct-Ct
                L5: Ct-Cs_Ct-Cb
                L5: Ct-Cs_Ct-CO
                L5: Ct-Cs_Ct-Cd
                L5: Ct-Cs_Ct-C=S
            L4: Ct-De_Ct-H
                L5: Ct-Cb_Ct-H
                L5: Ct-CO_Ct-H
                L5: Ct-Cd_Ct-H
                L5: Ct-Ct_Ct-H
                L5: Ct-C=S_Ct-H
            L4: Ct-De_Ct-Cs
                L5: Ct-Cb_Ct-Cs
                L5: Ct-CO_Ct-Cs
                L5: Ct-Cd_Ct-Cs
                L5: Ct-Ct_Ct-Cs
                L5: Ct-CS_Ct-Cs
            L4: Ct-De_Ct-De
                L5: Ct-Ct_Ct-Ct
                L5: Ct-Cd_Ct-Ct
                L5: Ct-Ct_Ct-Cd
                L5: Ct-Cd_Ct-Cd
                    L6: Ct-Cd_Ct-Cd_cyc6
                L5: Ct-De_Ct-Cb
                    L6: Ct-Cd_Ct-Cb
                        L7: Ct-CdCdCb_Ct-Cb_cyc6
                L5: Ct-Cb_Ct-Cd
                    L6: Ct-Cb_Ct-CdCdCb_cyc6
                    L6: Ct-Cb_Ct-CdCb_cyc5
            L4: Ct-O_Ct
                L5: Ct-O_Ct-Cb
        L3: Ct_Nt
            L4: Ct_N3t
                L5: Ct-H_N3t
                L5: Ct-NonDe_N3t
                L5: Ct-OneDe_N3t
            L4: Ct_N5t
    L2: Od_R
        L3: Od_CO
            L4: Od_CO-HH
            L4: Od_CO-NdH
                L5: Od_CO-CsH
            L4: Od_CO-NdNd
                L5: Od_CO-CsCs
            L4: Od_CO-DeH
                L5: Od_CO-CdH
                L5: Od_CO-CtH
            L4: Od_CO-DeNd
                L5: Od_CO-CdCs
                L5: Od_CO-CtCs
        L3: Od_Cdd
            L4: Od_Cdd-O2d
        L3: Od_Nd
            L4: Od_N3d
            L4: Od_N5dc
    L2: Nd_R
        L3: N1dc_R
        L3: N3d_R
            L4: N3d_Cd
                L5: N3d_Cds
                    L6: N3d-H_Cds
                        L7: N3d-H_Cds-HH
                        L7: N3d-H_Cds-NonDeH
                        L7: N3d-H_Cds-NonDe2
                    L6: N3d-NonDe_Cds
                    L6: N3d-OneDe_Cds
                L5: N3d_Cdd
            L4: N3d_Od
                L5: N3d-H_Od
                L5: N3d-NonDe_Od
                L5: N3d-OneDe_Od
            L4: N3d_Nd
                L5: N3d_N3d
                    L6: N3d-H_N3d
                        L7: N3d-H_N3d-H
                        L7: N3d-H_N3d-NonDe
                        L7: N3d-H_N3d-OneDe
                    L6: N3d-NonDe_N3d
                    L6: N3d-OneDe_N3d
                L5: N3d_N5dc
    L2: Nt_R
        L3: N3t_R
            L4: N3t_Ct
                L5: N3t_Ct-H
                L5: N3t_Ct-NonDe
                L5: N3t_Ct-OneDe
            L4: N3t_N3t
        L3: N5t_R
    L2: Sd_R
        L3: Sd_Cdd
            L4: Sd_Cdd-S2d
        L3: Sd_Cd
            L4: Sd_Cds-HH
            L4: Sd_Cds-CsH
            L4: Sd_Cds-OsH
            L4: Sd_Cds-OsCs
            L4: Sd_Cds-CsCs
            L4: Sd_Cds-OneDeH
                L5: Sd_Cds-CtH
                L5: Sd_Cds-CbH
                L5: Sd_Cds-COH
                L5: Sd_Cds-CdH
                L5: Sd_Cds-C=SH
            L4: Sd_Cds-OneDeCs
                L5: Sd_Cds-CtCs
                L5: Sd_Cds-CbCs
                L5: Sd_Cds-COCs
                L5: Sd_Cds-CdCs
                L5: Sd_Cds-C=SCs
            L4: Sd_Cds-TwoDe
                L5: Sd_Cds-CtCt
                L5: Sd_Cds-CtCb
                L5: Sd_Cds-CtCO
                L5: Sd_Cds-CbCb
                L5: Sd_Cds-CbCO
                L5: Sd_Cds-COCO
                L5: Sd_Cds-CdCt
                L5: Sd_Cds-CdCb
                L5: Sd_Cds-CdCO
                L5: Sd_Cds-CtC=S
                L5: Sd_Cds-CbC=S
                L5: Sd_Cds-COC=S
                L5: Sd_Cds-CdCd
                L5: Sd_Cds-CdC=S
                L5: Sd_Cds-C=SC=S
L1: YJ
    L2: HJ
    L2: LiJ
    L2: Y_1centerquadrad
        L3: C_quintet
        L3: C_triplet
    L2: Y_1centertrirad
        L3: N_atom_quartet
        L3: N_atom_doublet
        L3: CH_quartet
        L3: CH_doublet
    L2: Y_1centerbirad
        L3: O_atom_triplet
        L3: SJJ
        L3: CH2_triplet
        L3: CO_birad
        L3: NH_triplet
    L2: CJ
        L3: CbJ
        L3: CtJ
            L4: CtJ_Ct
            L4: CtJ_N3t
        L3: C2b
        L3: C=SJ
            L4: C=SJ-H
            L4: C=SJ-Cs
            L4: C=SJ-Ct
            L4: C=SJ-Cb
            L4: C=SJ-CO
            L4: C=SJ-O2s
            L4: C=SJ-S2s
            L4: C=SJ-Cd
            L4: C=SJ-C=S
        L3: CO_rad
            L4: CO_pri_rad
            L4: CO_sec_rad
                L5: CO_rad/NonDe
                L5: CO_rad/OneDe
        L3: CsJ
            L4: CsJ-HHH
            L4: CsJ-CsHH
            L4: CsJ-CsCsH
            L4: CsJ-CsCsCs
            L4: CsJ-OsHH
            L4: CsJ-OsCsH
            L4: CsJ-OsCsCs
            L4: CsJ-OsOsH
            L4: CsJ-OsOsCs
            L4: CsJ-OsOsOs
            L4: CsJ-SsHH
            L4: CsJ-SsCsH
            L4: CsJ-SsCsCs
            L4: CsJ-SsSsH
            L4: CsJ-SsSsCs
            L4: CsJ-SsSsSs
            L4: CsJ-NsHH
            L4: CsJ-NsCsH
            L4: CsJ-OneDe
                L5: CsJ-OneDeHH
                    L6: CsJ-CtHH
                    L6: CsJ-CbHH
                    L6: CsJ-COHH
                    L6: CsJ-CdHH
                        L7: CsJ-(CdC)HH
                    L6: CsJ-C=SHH
                L5: CsJ-OneDeCsH
                    L6: CsJ-CtCsH
                    L6: CsJ-CbCsH
                    L6: CsJ-COCsH
                    L6: CsJ-CdCsH
                    L6: CsJ-C=SCsH
                L5: CsJ-OneDeOsH
                L5: CsJ-OneDeSsH
                L5: CsJ-OneDeCsCs
                    L6: CsJ-CtCsCs
                    L6: CsJ-CbCsCs
                    L6: CsJ-COCsCs
                    L6: CsJ-CdCsCs
                    L6: CsJ-C=SCsCs
                L5: CsJ-OneDeOsCs
                L5: CsJ-OneDeSsCs
                L5: CsJ-OneDeOsOs
                L5: CsJ-OneDeOsSs
                L5: CsJ-OneDeSsSs
                L5: CsJ-OneDeNsH
                L5: CsJ-OneDeNsCs
            L4: CsJ-TwoDe
                L5: CsJ-TwoDeH
                    L6: CsJ-CtCtH
                    L6: CsJ-CtCbH
                    L6: CsJ-CtCOH
                    L6: CsJ-CbCbH
                    L6: CsJ-CbCOH
                    L6: CsJ-COCOH
                    L6: CsJ-CdCtH
                    L6: CsJ-CdCbH
                    L6: CsJ-CdCOH
                    L6: CsJ-CtC=SH
                    L6: CsJ-CbC=SH
                    L6: CsJ-COC=SH
                    L6: CsJ-CdCdH
                    L6: CsJ-CdC=SH
                    L6: CsJ-C=SC=SH
                L5: CsJ-TwoDeCs
                    L6: CsJ-CtCtCs
                    L6: CsJ-CtCbCs
                    L6: CsJ-CtCOCs
                    L6: CsJ-CbCbCs
                    L6: CsJ-CbCOCs
                    L6: CsJ-COCOCs
                    L6: CsJ-CdCtCs
                    L6: CsJ-CdCbCs
                    L6: CsJ-CdCOCs
                    L6: CsJ-CtC=SCs
                    L6: CsJ-CbC=SCs
                    L6: CsJ-COC=SCs
                    L6: CsJ-CdCdCs
                    L6: CsJ-CdC=SCs
                    L6: CsJ-C=SC=SCs
                L5: CsJ-TwoDeOs
                L5: CsJ-TwoDeSs
            L4: CsJ-ThreeDe
        L3: CdsJ=Cdd
        L3: CdsJ
            L4: CdsJ-H
                L5: CdsJ-(CdCb)H
            L4: CdsJ-Cs
            L4: CdsJ-Ct
            L4: CdsJ-Cb
            L4: CdsJ-CO
            L4: CdsJ-O2s
            L4: CdsJ-S2s
            L4: CdsJ-Cd
            L4: CdsJ-C=S
    L2: OJ
        L3: OJ_pri
        L3: OJ_sec
            L4: OJ-NonDe
                L5: O_rad/NonDe
                    L6: OJ-Cs
                    L6: OJ-O2s
                L5: OJ-Ns
            L4: OJ-OneDe
                L5: O_rad/OneDe
                L5: OJ-OneDeN
                    L6: OJ-NO
        L3: O2b
    L2: SJ
        L3: SsJ
            L4: SsJ-H
            L4: SsJ-Cs
            L4: SsJ-S2s
            L4: SsJ-OneDe
                L5: SsJ-Ct
                L5: SsJ-Cb
                L5: SsJ-CO
                L5: SsJ-Cd
                L5: SsJ-C=S
    L2: NJ
        L3: N3J
            L4: N3sJ
                L5: NH2J
                L5: N3sJ-NonDeH
                    L6: N3sJ-CsH
                    L6: N3sJ-OsH
                    L6: N3sJ-NsH
                L5: N3sJ-NonDe2
                L5: N3sJ-OneDeH
                L5: N3sJ-OneDeCs
                L5: N3sJ-TwoDe
            L4: N3dJ
                L5: N3dJ_C
                L5: N3dJ_O
                L5: N3dJ_N
"""
)

forbidden(
    label = "O2d",
    group =
"""
1 *1 O u0 {2,D}
2 *2 O u0 {1,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

forbidden(
    label = "carbonaterad",
    group =
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2 O u0 {1,S}
3 O u0 {1,S}
4 O u0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

forbidden(
    label = "carbonatebreak",
    group =
"""
1 *3 C u0 {2,S} {3,S} {4,S} {5,S}
2 O u0 {1,S}
3 O u0 {1,S}
4 O u0 {1,S}
5 *1 R!H u0 {1,S} {6,[S,D]}
6 *2 R!H u1 {5,[S,D]}
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)