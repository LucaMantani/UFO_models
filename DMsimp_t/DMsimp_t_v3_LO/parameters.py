# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.2.0 for Mac OS X x86 (64-bit) (September 11, 2017)
# Date: Tue 12 Mar 2019 11:14:42



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
kg = Parameter(name = 'kg',
               nature = 'external',
               type = 'real',
               value = 0.,
               texname = '\\text{kg}',
               lhablock = 'ANOMCOUPINPUT',
               lhacode = [ 1 ])

gV3dR1x1 = Parameter(name = 'gV3dR1x1',
                     nature = 'external',
                     type = 'complex',
                     value = 1.1,
                     texname = '\\text{gV3dR1x1}',
                     lhablock = 'DMINPUTVDR',
                     lhacode = [ 1, 1 ])

gV3dR2x2 = Parameter(name = 'gV3dR2x2',
                     nature = 'external',
                     type = 'complex',
                     value = 1.1,
                     texname = '\\text{gV3dR2x2}',
                     lhablock = 'DMINPUTVDR',
                     lhacode = [ 2, 2 ])

gV3dR3x3 = Parameter(name = 'gV3dR3x3',
                     nature = 'external',
                     type = 'complex',
                     value = 1.1,
                     texname = '\\text{gV3dR3x3}',
                     lhablock = 'DMINPUTVDR',
                     lhacode = [ 3, 3 ])

gV3L1x1 = Parameter(name = 'gV3L1x1',
                    nature = 'external',
                    type = 'complex',
                    value = 1.1,
                    texname = '\\text{gV3L1x1}',
                    lhablock = 'DMINPUTVQL',
                    lhacode = [ 1, 1 ])

gV3L2x2 = Parameter(name = 'gV3L2x2',
                    nature = 'external',
                    type = 'complex',
                    value = 1.1,
                    texname = '\\text{gV3L2x2}',
                    lhablock = 'DMINPUTVQL',
                    lhacode = [ 2, 2 ])

gV3L3x3 = Parameter(name = 'gV3L3x3',
                    nature = 'external',
                    type = 'complex',
                    value = 1.1,
                    texname = '\\text{gV3L3x3}',
                    lhablock = 'DMINPUTVQL',
                    lhacode = [ 3, 3 ])

gV3uR1x1 = Parameter(name = 'gV3uR1x1',
                     nature = 'external',
                     type = 'complex',
                     value = 1.1,
                     texname = '\\text{gV3uR1x1}',
                     lhablock = 'DMINPUTVUR',
                     lhacode = [ 1, 1 ])

gV3uR2x2 = Parameter(name = 'gV3uR2x2',
                     nature = 'external',
                     type = 'complex',
                     value = 1.1,
                     texname = '\\text{gV3uR2x2}',
                     lhablock = 'DMINPUTVUR',
                     lhacode = [ 2, 2 ])

gV3uR3x3 = Parameter(name = 'gV3uR3x3',
                     nature = 'external',
                     type = 'complex',
                     value = 1.1,
                     texname = '\\text{gV3uR3x3}',
                     lhablock = 'DMINPUTVUR',
                     lhacode = [ 3, 3 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MXd = Parameter(name = 'MXd',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{MXd}',
                lhablock = 'MASS',
                lhacode = [ 52 ])

MXm = Parameter(name = 'MXm',
                nature = 'external',
                type = 'real',
                value = 100000.,
                texname = '\\text{MXm}',
                lhablock = 'MASS',
                lhacode = [ 522 ])

MV3uL1 = Parameter(name = 'MV3uL1',
                   nature = 'external',
                   type = 'real',
                   value = 1000.,
                   texname = '\\text{MV3uL1}',
                   lhablock = 'MASS',
                   lhacode = [ 3000002 ])

MV3uL2 = Parameter(name = 'MV3uL2',
                   nature = 'external',
                   type = 'real',
                   value = 1000.,
                   texname = '\\text{MV3uL2}',
                   lhablock = 'MASS',
                   lhacode = [ 3000004 ])

MV3uL3 = Parameter(name = 'MV3uL3',
                   nature = 'external',
                   type = 'real',
                   value = 1000.,
                   texname = '\\text{MV3uL3}',
                   lhablock = 'MASS',
                   lhacode = [ 3000006 ])

MV3dL1 = Parameter(name = 'MV3dL1',
                   nature = 'external',
                   type = 'real',
                   value = 1000.,
                   texname = '\\text{MV3dL1}',
                   lhablock = 'MASS',
                   lhacode = [ 3000001 ])

MV3dL2 = Parameter(name = 'MV3dL2',
                   nature = 'external',
                   type = 'real',
                   value = 1000.,
                   texname = '\\text{MV3dL2}',
                   lhablock = 'MASS',
                   lhacode = [ 3000003 ])

MV3dL3 = Parameter(name = 'MV3dL3',
                   nature = 'external',
                   type = 'real',
                   value = 1000.,
                   texname = '\\text{MV3dL3}',
                   lhablock = 'MASS',
                   lhacode = [ 3000005 ])

MV3uR1 = Parameter(name = 'MV3uR1',
                   nature = 'external',
                   type = 'real',
                   value = 1000.,
                   texname = '\\text{MV3uR1}',
                   lhablock = 'MASS',
                   lhacode = [ 4000002 ])

MV3uR2 = Parameter(name = 'MV3uR2',
                   nature = 'external',
                   type = 'real',
                   value = 1000.,
                   texname = '\\text{MV3uR2}',
                   lhablock = 'MASS',
                   lhacode = [ 4000004 ])

MV3uR3 = Parameter(name = 'MV3uR3',
                   nature = 'external',
                   type = 'real',
                   value = 1000.,
                   texname = '\\text{MV3uR3}',
                   lhablock = 'MASS',
                   lhacode = [ 4000006 ])

MV3dR1 = Parameter(name = 'MV3dR1',
                   nature = 'external',
                   type = 'real',
                   value = 1000.,
                   texname = '\\text{MV3dR1}',
                   lhablock = 'MASS',
                   lhacode = [ 4000001 ])

MV3dR2 = Parameter(name = 'MV3dR2',
                   nature = 'external',
                   type = 'real',
                   value = 1000.,
                   texname = '\\text{MV3dR2}',
                   lhablock = 'MASS',
                   lhacode = [ 4000003 ])

MV3dR3 = Parameter(name = 'MV3dR3',
                   nature = 'external',
                   type = 'real',
                   value = 1000.,
                   texname = '\\text{MV3dR3}',
                   lhablock = 'MASS',
                   lhacode = [ 4000005 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WV3uL1 = Parameter(name = 'WV3uL1',
                   nature = 'external',
                   type = 'real',
                   value = 10.,
                   texname = '\\text{WV3uL1}',
                   lhablock = 'DECAY',
                   lhacode = [ 3000002 ])

WV3uL2 = Parameter(name = 'WV3uL2',
                   nature = 'external',
                   type = 'real',
                   value = 10.,
                   texname = '\\text{WV3uL2}',
                   lhablock = 'DECAY',
                   lhacode = [ 3000004 ])

WV3uL3 = Parameter(name = 'WV3uL3',
                   nature = 'external',
                   type = 'real',
                   value = 10.,
                   texname = '\\text{WV3uL3}',
                   lhablock = 'DECAY',
                   lhacode = [ 3000006 ])

WV3dL1 = Parameter(name = 'WV3dL1',
                   nature = 'external',
                   type = 'real',
                   value = 10.,
                   texname = '\\text{WV3dL1}',
                   lhablock = 'DECAY',
                   lhacode = [ 3000001 ])

WV3dL2 = Parameter(name = 'WV3dL2',
                   nature = 'external',
                   type = 'real',
                   value = 10.,
                   texname = '\\text{WV3dL2}',
                   lhablock = 'DECAY',
                   lhacode = [ 3000003 ])

WV3dL3 = Parameter(name = 'WV3dL3',
                   nature = 'external',
                   type = 'real',
                   value = 10.,
                   texname = '\\text{WV3dL3}',
                   lhablock = 'DECAY',
                   lhacode = [ 3000005 ])

WV3uR1 = Parameter(name = 'WV3uR1',
                   nature = 'external',
                   type = 'real',
                   value = 10.,
                   texname = '\\text{WV3uR1}',
                   lhablock = 'DECAY',
                   lhacode = [ 4000002 ])

WV3uR2 = Parameter(name = 'WV3uR2',
                   nature = 'external',
                   type = 'real',
                   value = 10.,
                   texname = '\\text{WV3uR2}',
                   lhablock = 'DECAY',
                   lhacode = [ 4000004 ])

WV3uR3 = Parameter(name = 'WV3uR3',
                   nature = 'external',
                   type = 'real',
                   value = 10.,
                   texname = '\\text{WV3uR3}',
                   lhablock = 'DECAY',
                   lhacode = [ 4000006 ])

WV3dR1 = Parameter(name = 'WV3dR1',
                   nature = 'external',
                   type = 'real',
                   value = 10.,
                   texname = '\\text{WV3dR1}',
                   lhablock = 'DECAY',
                   lhacode = [ 4000001 ])

WV3dR2 = Parameter(name = 'WV3dR2',
                   nature = 'external',
                   type = 'real',
                   value = 10.,
                   texname = '\\text{WV3dR2}',
                   lhablock = 'DECAY',
                   lhacode = [ 4000003 ])

WV3dR3 = Parameter(name = 'WV3dR3',
                   nature = 'external',
                   type = 'real',
                   value = 10.,
                   texname = '\\text{WV3dR3}',
                   lhablock = 'DECAY',
                   lhacode = [ 4000005 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

