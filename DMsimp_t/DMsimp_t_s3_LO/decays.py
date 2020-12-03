# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.2.0 for Mac OS X x86 (64-bit) (September 11, 2017)
# Date: Tue 12 Mar 2019 11:10:19


from object_library import all_decays, Decay
import particles as P


Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.S3dL3,P.Xd):'((3*gS3L3x3*MB**2*complexconjugate(gS3L3x3) - 3*gS3L3x3*MS3dL3**2*complexconjugate(gS3L3x3) + 3*gS3L3x3*MXd**2*complexconjugate(gS3L3x3))*cmath.sqrt(MB**4 - 2*MB**2*MS3dL3**2 + MS3dL3**4 - 2*MB**2*MXd**2 - 2*MS3dL3**2*MXd**2 + MXd**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.S3dL3,P.Xm):'((3*gS3L3x3*MB**2*complexconjugate(gS3L3x3) - 3*gS3L3x3*MS3dL3**2*complexconjugate(gS3L3x3) + 3*gS3L3x3*MXm**2*complexconjugate(gS3L3x3))*cmath.sqrt(MB**4 - 2*MB**2*MS3dL3**2 + MS3dL3**4 - 2*MB**2*MXm**2 - 2*MS3dL3**2*MXm**2 + MXm**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.S3dR3,P.Xd):'((3*gS3dR3x3*MB**2*complexconjugate(gS3dR3x3) - 3*gS3dR3x3*MS3dR3**2*complexconjugate(gS3dR3x3) + 3*gS3dR3x3*MXd**2*complexconjugate(gS3dR3x3))*cmath.sqrt(MB**4 - 2*MB**2*MS3dR3**2 + MS3dR3**4 - 2*MB**2*MXd**2 - 2*MS3dR3**2*MXd**2 + MXd**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.S3dR3,P.Xm):'((3*gS3dR3x3*MB**2*complexconjugate(gS3dR3x3) - 3*gS3dR3x3*MS3dR3**2*complexconjugate(gS3dR3x3) + 3*gS3dR3x3*MXm**2*complexconjugate(gS3dR3x3))*cmath.sqrt(MB**4 - 2*MB**2*MS3dR3**2 + MS3dR3**4 - 2*MB**2*MXm**2 - 2*MS3dR3**2*MXm**2 + MXm**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.W__minus__,P.t):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.b,P.b__tilde__):'((-12*MB**2*yb**2 + 3*MH**2*yb**2)*cmath.sqrt(-4*MB**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_S3dL1 = Decay(name = 'Decay_S3dL1',
                    particle = P.S3dL1,
                    partial_widths = {(P.d,P.Xd__tilde__):'((MS3dL1**2 - MXd**2)*(3*gS3L1x1*MS3dL1**2*complexconjugate(gS3L1x1) - 3*gS3L1x1*MXd**2*complexconjugate(gS3L1x1)))/(48.*cmath.pi*abs(MS3dL1)**3)',
                                      (P.d,P.Xm):'((MS3dL1**2 - MXm**2)*(3*gS3L1x1*MS3dL1**2*complexconjugate(gS3L1x1) - 3*gS3L1x1*MXm**2*complexconjugate(gS3L1x1)))/(48.*cmath.pi*abs(MS3dL1)**3)',
                                      (P.S3uL1,P.W__minus__):'(((-3*ee**2*MS3dL1**2)/sw**2 - (3*ee**2*MS3uL1**2)/sw**2 + (3*ee**2*MS3dL1**4)/(2.*MW**2*sw**2) - (3*ee**2*MS3dL1**2*MS3uL1**2)/(MW**2*sw**2) + (3*ee**2*MS3uL1**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/(2.*sw**2))*cmath.sqrt(MS3dL1**4 - 2*MS3dL1**2*MS3uL1**2 + MS3uL1**4 - 2*MS3dL1**2*MW**2 - 2*MS3uL1**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MS3dL1)**3)'})

Decay_S3dL2 = Decay(name = 'Decay_S3dL2',
                    particle = P.S3dL2,
                    partial_widths = {(P.s,P.Xd__tilde__):'((MS3dL2**2 - MXd**2)*(3*gS3L2x2*MS3dL2**2*complexconjugate(gS3L2x2) - 3*gS3L2x2*MXd**2*complexconjugate(gS3L2x2)))/(48.*cmath.pi*abs(MS3dL2)**3)',
                                      (P.s,P.Xm):'((MS3dL2**2 - MXm**2)*(3*gS3L2x2*MS3dL2**2*complexconjugate(gS3L2x2) - 3*gS3L2x2*MXm**2*complexconjugate(gS3L2x2)))/(48.*cmath.pi*abs(MS3dL2)**3)',
                                      (P.S3uL2,P.W__minus__):'(((-3*ee**2*MS3dL2**2)/sw**2 - (3*ee**2*MS3uL2**2)/sw**2 + (3*ee**2*MS3dL2**4)/(2.*MW**2*sw**2) - (3*ee**2*MS3dL2**2*MS3uL2**2)/(MW**2*sw**2) + (3*ee**2*MS3uL2**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/(2.*sw**2))*cmath.sqrt(MS3dL2**4 - 2*MS3dL2**2*MS3uL2**2 + MS3uL2**4 - 2*MS3dL2**2*MW**2 - 2*MS3uL2**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MS3dL2)**3)'})

Decay_S3dL3 = Decay(name = 'Decay_S3dL3',
                    particle = P.S3dL3,
                    partial_widths = {(P.b,P.Xd__tilde__):'((-3*gS3L3x3*MB**2*complexconjugate(gS3L3x3) + 3*gS3L3x3*MS3dL3**2*complexconjugate(gS3L3x3) - 3*gS3L3x3*MXd**2*complexconjugate(gS3L3x3))*cmath.sqrt(MB**4 - 2*MB**2*MS3dL3**2 + MS3dL3**4 - 2*MB**2*MXd**2 - 2*MS3dL3**2*MXd**2 + MXd**4))/(48.*cmath.pi*abs(MS3dL3)**3)',
                                      (P.b,P.Xm):'((-3*gS3L3x3*MB**2*complexconjugate(gS3L3x3) + 3*gS3L3x3*MS3dL3**2*complexconjugate(gS3L3x3) - 3*gS3L3x3*MXm**2*complexconjugate(gS3L3x3))*cmath.sqrt(MB**4 - 2*MB**2*MS3dL3**2 + MS3dL3**4 - 2*MB**2*MXm**2 - 2*MS3dL3**2*MXm**2 + MXm**4))/(48.*cmath.pi*abs(MS3dL3)**3)',
                                      (P.S3uL3,P.W__minus__):'(((-3*ee**2*MS3dL3**2)/sw**2 - (3*ee**2*MS3uL3**2)/sw**2 + (3*ee**2*MS3dL3**4)/(2.*MW**2*sw**2) - (3*ee**2*MS3dL3**2*MS3uL3**2)/(MW**2*sw**2) + (3*ee**2*MS3uL3**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/(2.*sw**2))*cmath.sqrt(MS3dL3**4 - 2*MS3dL3**2*MS3uL3**2 + MS3uL3**4 - 2*MS3dL3**2*MW**2 - 2*MS3uL3**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MS3dL3)**3)'})

Decay_S3dR1 = Decay(name = 'Decay_S3dR1',
                    particle = P.S3dR1,
                    partial_widths = {(P.d,P.Xd__tilde__):'((MS3dR1**2 - MXd**2)*(3*gS3dR1x1*MS3dR1**2*complexconjugate(gS3dR1x1) - 3*gS3dR1x1*MXd**2*complexconjugate(gS3dR1x1)))/(48.*cmath.pi*abs(MS3dR1)**3)',
                                      (P.d,P.Xm):'((MS3dR1**2 - MXm**2)*(3*gS3dR1x1*MS3dR1**2*complexconjugate(gS3dR1x1) - 3*gS3dR1x1*MXm**2*complexconjugate(gS3dR1x1)))/(48.*cmath.pi*abs(MS3dR1)**3)'})

Decay_S3dR2 = Decay(name = 'Decay_S3dR2',
                    particle = P.S3dR2,
                    partial_widths = {(P.s,P.Xd__tilde__):'((MS3dR2**2 - MXd**2)*(3*gS3dR2x2*MS3dR2**2*complexconjugate(gS3dR2x2) - 3*gS3dR2x2*MXd**2*complexconjugate(gS3dR2x2)))/(48.*cmath.pi*abs(MS3dR2)**3)',
                                      (P.s,P.Xm):'((MS3dR2**2 - MXm**2)*(3*gS3dR2x2*MS3dR2**2*complexconjugate(gS3dR2x2) - 3*gS3dR2x2*MXm**2*complexconjugate(gS3dR2x2)))/(48.*cmath.pi*abs(MS3dR2)**3)'})

Decay_S3dR3 = Decay(name = 'Decay_S3dR3',
                    particle = P.S3dR3,
                    partial_widths = {(P.b,P.Xd__tilde__):'((-3*gS3dR3x3*MB**2*complexconjugate(gS3dR3x3) + 3*gS3dR3x3*MS3dR3**2*complexconjugate(gS3dR3x3) - 3*gS3dR3x3*MXd**2*complexconjugate(gS3dR3x3))*cmath.sqrt(MB**4 - 2*MB**2*MS3dR3**2 + MS3dR3**4 - 2*MB**2*MXd**2 - 2*MS3dR3**2*MXd**2 + MXd**4))/(48.*cmath.pi*abs(MS3dR3)**3)',
                                      (P.b,P.Xm):'((-3*gS3dR3x3*MB**2*complexconjugate(gS3dR3x3) + 3*gS3dR3x3*MS3dR3**2*complexconjugate(gS3dR3x3) - 3*gS3dR3x3*MXm**2*complexconjugate(gS3dR3x3))*cmath.sqrt(MB**4 - 2*MB**2*MS3dR3**2 + MS3dR3**4 - 2*MB**2*MXm**2 - 2*MS3dR3**2*MXm**2 + MXm**4))/(48.*cmath.pi*abs(MS3dR3)**3)'})

Decay_S3uL1 = Decay(name = 'Decay_S3uL1',
                    particle = P.S3uL1,
                    partial_widths = {(P.S3dL1,P.W__plus__):'(((-3*ee**2*MS3dL1**2)/sw**2 - (3*ee**2*MS3uL1**2)/sw**2 + (3*ee**2*MS3dL1**4)/(2.*MW**2*sw**2) - (3*ee**2*MS3dL1**2*MS3uL1**2)/(MW**2*sw**2) + (3*ee**2*MS3uL1**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/(2.*sw**2))*cmath.sqrt(MS3dL1**4 - 2*MS3dL1**2*MS3uL1**2 + MS3uL1**4 - 2*MS3dL1**2*MW**2 - 2*MS3uL1**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MS3uL1)**3)',
                                      (P.u,P.Xd__tilde__):'((MS3uL1**2 - MXd**2)*(3*gS3L1x1*MS3uL1**2*complexconjugate(gS3L1x1) - 3*gS3L1x1*MXd**2*complexconjugate(gS3L1x1)))/(48.*cmath.pi*abs(MS3uL1)**3)',
                                      (P.u,P.Xm):'((MS3uL1**2 - MXm**2)*(3*gS3L1x1*MS3uL1**2*complexconjugate(gS3L1x1) - 3*gS3L1x1*MXm**2*complexconjugate(gS3L1x1)))/(48.*cmath.pi*abs(MS3uL1)**3)'})

Decay_S3uL2 = Decay(name = 'Decay_S3uL2',
                    particle = P.S3uL2,
                    partial_widths = {(P.c,P.Xd__tilde__):'((MS3uL2**2 - MXd**2)*(3*gS3L2x2*MS3uL2**2*complexconjugate(gS3L2x2) - 3*gS3L2x2*MXd**2*complexconjugate(gS3L2x2)))/(48.*cmath.pi*abs(MS3uL2)**3)',
                                      (P.c,P.Xm):'((MS3uL2**2 - MXm**2)*(3*gS3L2x2*MS3uL2**2*complexconjugate(gS3L2x2) - 3*gS3L2x2*MXm**2*complexconjugate(gS3L2x2)))/(48.*cmath.pi*abs(MS3uL2)**3)',
                                      (P.S3dL2,P.W__plus__):'(((-3*ee**2*MS3dL2**2)/sw**2 - (3*ee**2*MS3uL2**2)/sw**2 + (3*ee**2*MS3dL2**4)/(2.*MW**2*sw**2) - (3*ee**2*MS3dL2**2*MS3uL2**2)/(MW**2*sw**2) + (3*ee**2*MS3uL2**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/(2.*sw**2))*cmath.sqrt(MS3dL2**4 - 2*MS3dL2**2*MS3uL2**2 + MS3uL2**4 - 2*MS3dL2**2*MW**2 - 2*MS3uL2**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MS3uL2)**3)'})

Decay_S3uL3 = Decay(name = 'Decay_S3uL3',
                    particle = P.S3uL3,
                    partial_widths = {(P.S3dL3,P.W__plus__):'(((-3*ee**2*MS3dL3**2)/sw**2 - (3*ee**2*MS3uL3**2)/sw**2 + (3*ee**2*MS3dL3**4)/(2.*MW**2*sw**2) - (3*ee**2*MS3dL3**2*MS3uL3**2)/(MW**2*sw**2) + (3*ee**2*MS3uL3**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/(2.*sw**2))*cmath.sqrt(MS3dL3**4 - 2*MS3dL3**2*MS3uL3**2 + MS3uL3**4 - 2*MS3dL3**2*MW**2 - 2*MS3uL3**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MS3uL3)**3)',
                                      (P.t,P.Xd__tilde__):'((3*gS3L3x3*MS3uL3**2*complexconjugate(gS3L3x3) - 3*gS3L3x3*MT**2*complexconjugate(gS3L3x3) - 3*gS3L3x3*MXd**2*complexconjugate(gS3L3x3))*cmath.sqrt(MS3uL3**4 - 2*MS3uL3**2*MT**2 + MT**4 - 2*MS3uL3**2*MXd**2 - 2*MT**2*MXd**2 + MXd**4))/(48.*cmath.pi*abs(MS3uL3)**3)',
                                      (P.t,P.Xm):'((3*gS3L3x3*MS3uL3**2*complexconjugate(gS3L3x3) - 3*gS3L3x3*MT**2*complexconjugate(gS3L3x3) - 3*gS3L3x3*MXm**2*complexconjugate(gS3L3x3))*cmath.sqrt(MS3uL3**4 - 2*MS3uL3**2*MT**2 + MT**4 - 2*MS3uL3**2*MXm**2 - 2*MT**2*MXm**2 + MXm**4))/(48.*cmath.pi*abs(MS3uL3)**3)'})

Decay_S3uR1 = Decay(name = 'Decay_S3uR1',
                    particle = P.S3uR1,
                    partial_widths = {(P.u,P.Xd__tilde__):'((MS3uR1**2 - MXd**2)*(3*gS3uR1x1*MS3uR1**2*complexconjugate(gS3uR1x1) - 3*gS3uR1x1*MXd**2*complexconjugate(gS3uR1x1)))/(48.*cmath.pi*abs(MS3uR1)**3)',
                                      (P.u,P.Xm):'((MS3uR1**2 - MXm**2)*(3*gS3uR1x1*MS3uR1**2*complexconjugate(gS3uR1x1) - 3*gS3uR1x1*MXm**2*complexconjugate(gS3uR1x1)))/(48.*cmath.pi*abs(MS3uR1)**3)'})

Decay_S3uR2 = Decay(name = 'Decay_S3uR2',
                    particle = P.S3uR2,
                    partial_widths = {(P.c,P.Xd__tilde__):'((MS3uR2**2 - MXd**2)*(3*gS3uR2x2*MS3uR2**2*complexconjugate(gS3uR2x2) - 3*gS3uR2x2*MXd**2*complexconjugate(gS3uR2x2)))/(48.*cmath.pi*abs(MS3uR2)**3)',
                                      (P.c,P.Xm):'((MS3uR2**2 - MXm**2)*(3*gS3uR2x2*MS3uR2**2*complexconjugate(gS3uR2x2) - 3*gS3uR2x2*MXm**2*complexconjugate(gS3uR2x2)))/(48.*cmath.pi*abs(MS3uR2)**3)'})

Decay_S3uR3 = Decay(name = 'Decay_S3uR3',
                    particle = P.S3uR3,
                    partial_widths = {(P.t,P.Xd__tilde__):'((3*gS3uR3x3*MS3uR3**2*complexconjugate(gS3uR3x3) - 3*gS3uR3x3*MT**2*complexconjugate(gS3uR3x3) - 3*gS3uR3x3*MXd**2*complexconjugate(gS3uR3x3))*cmath.sqrt(MS3uR3**4 - 2*MS3uR3**2*MT**2 + MT**4 - 2*MS3uR3**2*MXd**2 - 2*MT**2*MXd**2 + MXd**4))/(48.*cmath.pi*abs(MS3uR3)**3)',
                                      (P.t,P.Xm):'((3*gS3uR3x3*MS3uR3**2*complexconjugate(gS3uR3x3) - 3*gS3uR3x3*MT**2*complexconjugate(gS3uR3x3) - 3*gS3uR3x3*MXm**2*complexconjugate(gS3uR3x3))*cmath.sqrt(MS3uR3**4 - 2*MS3uR3**2*MT**2 + MT**4 - 2*MS3uR3**2*MXm**2 - 2*MT**2*MXm**2 + MXm**4))/(48.*cmath.pi*abs(MS3uR3)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.S3uL3,P.Xd):'((-3*gS3L3x3*MS3uL3**2*complexconjugate(gS3L3x3) + 3*gS3L3x3*MT**2*complexconjugate(gS3L3x3) + 3*gS3L3x3*MXd**2*complexconjugate(gS3L3x3))*cmath.sqrt(MS3uL3**4 - 2*MS3uL3**2*MT**2 + MT**4 - 2*MS3uL3**2*MXd**2 - 2*MT**2*MXd**2 + MXd**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.S3uL3,P.Xm):'((-3*gS3L3x3*MS3uL3**2*complexconjugate(gS3L3x3) + 3*gS3L3x3*MT**2*complexconjugate(gS3L3x3) + 3*gS3L3x3*MXm**2*complexconjugate(gS3L3x3))*cmath.sqrt(MS3uL3**4 - 2*MS3uL3**2*MT**2 + MT**4 - 2*MS3uL3**2*MXm**2 - 2*MT**2*MXm**2 + MXm**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.S3uR3,P.Xd):'((-3*gS3uR3x3*MS3uR3**2*complexconjugate(gS3uR3x3) + 3*gS3uR3x3*MT**2*complexconjugate(gS3uR3x3) + 3*gS3uR3x3*MXd**2*complexconjugate(gS3uR3x3))*cmath.sqrt(MS3uR3**4 - 2*MS3uR3**2*MT**2 + MT**4 - 2*MS3uR3**2*MXd**2 - 2*MT**2*MXd**2 + MXd**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.S3uR3,P.Xm):'((-3*gS3uR3x3*MS3uR3**2*complexconjugate(gS3uR3x3) + 3*gS3uR3x3*MT**2*complexconjugate(gS3uR3x3) + 3*gS3uR3x3*MXm**2*complexconjugate(gS3uR3x3))*cmath.sqrt(MS3uR3**4 - 2*MS3uR3**2*MT**2 + MT**4 - 2*MS3uR3**2*MXm**2 - 2*MT**2*MXm**2 + MXm**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.W__plus__,P.b):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.s__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.S3dL1__tilde__,P.S3uL1):'(((-3*ee**2*MS3dL1**2)/sw**2 - (3*ee**2*MS3uL1**2)/sw**2 + (3*ee**2*MS3dL1**4)/(2.*MW**2*sw**2) - (3*ee**2*MS3dL1**2*MS3uL1**2)/(MW**2*sw**2) + (3*ee**2*MS3uL1**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/(2.*sw**2))*cmath.sqrt(MS3dL1**4 - 2*MS3dL1**2*MS3uL1**2 + MS3uL1**4 - 2*MS3dL1**2*MW**2 - 2*MS3uL1**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.S3dL2__tilde__,P.S3uL2):'(((-3*ee**2*MS3dL2**2)/sw**2 - (3*ee**2*MS3uL2**2)/sw**2 + (3*ee**2*MS3dL2**4)/(2.*MW**2*sw**2) - (3*ee**2*MS3dL2**2*MS3uL2**2)/(MW**2*sw**2) + (3*ee**2*MS3uL2**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/(2.*sw**2))*cmath.sqrt(MS3dL2**4 - 2*MS3dL2**2*MS3uL2**2 + MS3uL2**4 - 2*MS3dL2**2*MW**2 - 2*MS3uL2**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.S3dL3__tilde__,P.S3uL3):'(((-3*ee**2*MS3dL3**2)/sw**2 - (3*ee**2*MS3uL3**2)/sw**2 + (3*ee**2*MS3dL3**4)/(2.*MW**2*sw**2) - (3*ee**2*MS3dL3**2*MS3uL3**2)/(MW**2*sw**2) + (3*ee**2*MS3uL3**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/(2.*sw**2))*cmath.sqrt(MS3dL3**4 - 2*MS3dL3**2*MS3uL3**2 + MS3uL3**4 - 2*MS3dL3**2*MW**2 - 2*MS3uL3**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*ee**2*MB**2)/(2.*sw**2) - (3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MB**4)/(2.*MW**2*sw**2) + (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-(ee**2*MTA**2)/(2.*sw**2) - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Xd = Decay(name = 'Decay_Xd',
                 particle = P.Xd,
                 partial_widths = {(P.S3dL1__tilde__,P.d):'((-MS3dL1**2 + MXd**2)*(-3*gS3L1x1*MS3dL1**2*complexconjugate(gS3L1x1) + 3*gS3L1x1*MXd**2*complexconjugate(gS3L1x1)))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.S3dL2__tilde__,P.s):'((-MS3dL2**2 + MXd**2)*(-3*gS3L2x2*MS3dL2**2*complexconjugate(gS3L2x2) + 3*gS3L2x2*MXd**2*complexconjugate(gS3L2x2)))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.S3dL3__tilde__,P.b):'((3*gS3L3x3*MB**2*complexconjugate(gS3L3x3) - 3*gS3L3x3*MS3dL3**2*complexconjugate(gS3L3x3) + 3*gS3L3x3*MXd**2*complexconjugate(gS3L3x3))*cmath.sqrt(MB**4 - 2*MB**2*MS3dL3**2 + MS3dL3**4 - 2*MB**2*MXd**2 - 2*MS3dL3**2*MXd**2 + MXd**4))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.S3dR1__tilde__,P.d):'((-MS3dR1**2 + MXd**2)*(-3*gS3dR1x1*MS3dR1**2*complexconjugate(gS3dR1x1) + 3*gS3dR1x1*MXd**2*complexconjugate(gS3dR1x1)))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.S3dR2__tilde__,P.s):'((-MS3dR2**2 + MXd**2)*(-3*gS3dR2x2*MS3dR2**2*complexconjugate(gS3dR2x2) + 3*gS3dR2x2*MXd**2*complexconjugate(gS3dR2x2)))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.S3dR3__tilde__,P.b):'((3*gS3dR3x3*MB**2*complexconjugate(gS3dR3x3) - 3*gS3dR3x3*MS3dR3**2*complexconjugate(gS3dR3x3) + 3*gS3dR3x3*MXd**2*complexconjugate(gS3dR3x3))*cmath.sqrt(MB**4 - 2*MB**2*MS3dR3**2 + MS3dR3**4 - 2*MB**2*MXd**2 - 2*MS3dR3**2*MXd**2 + MXd**4))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.S3uL1__tilde__,P.u):'((-MS3uL1**2 + MXd**2)*(-3*gS3L1x1*MS3uL1**2*complexconjugate(gS3L1x1) + 3*gS3L1x1*MXd**2*complexconjugate(gS3L1x1)))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.S3uL2__tilde__,P.c):'((-MS3uL2**2 + MXd**2)*(-3*gS3L2x2*MS3uL2**2*complexconjugate(gS3L2x2) + 3*gS3L2x2*MXd**2*complexconjugate(gS3L2x2)))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.S3uL3__tilde__,P.t):'((-3*gS3L3x3*MS3uL3**2*complexconjugate(gS3L3x3) + 3*gS3L3x3*MT**2*complexconjugate(gS3L3x3) + 3*gS3L3x3*MXd**2*complexconjugate(gS3L3x3))*cmath.sqrt(MS3uL3**4 - 2*MS3uL3**2*MT**2 + MT**4 - 2*MS3uL3**2*MXd**2 - 2*MT**2*MXd**2 + MXd**4))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.S3uR1__tilde__,P.u):'((-MS3uR1**2 + MXd**2)*(-3*gS3uR1x1*MS3uR1**2*complexconjugate(gS3uR1x1) + 3*gS3uR1x1*MXd**2*complexconjugate(gS3uR1x1)))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.S3uR2__tilde__,P.c):'((-MS3uR2**2 + MXd**2)*(-3*gS3uR2x2*MS3uR2**2*complexconjugate(gS3uR2x2) + 3*gS3uR2x2*MXd**2*complexconjugate(gS3uR2x2)))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.S3uR3__tilde__,P.t):'((-3*gS3uR3x3*MS3uR3**2*complexconjugate(gS3uR3x3) + 3*gS3uR3x3*MT**2*complexconjugate(gS3uR3x3) + 3*gS3uR3x3*MXd**2*complexconjugate(gS3uR3x3))*cmath.sqrt(MS3uR3**4 - 2*MS3uR3**2*MT**2 + MT**4 - 2*MS3uR3**2*MXd**2 - 2*MT**2*MXd**2 + MXd**4))/(32.*cmath.pi*abs(MXd)**3)'})

Decay_Xm = Decay(name = 'Decay_Xm',
                 particle = P.Xm,
                 partial_widths = {(P.S3dL1,P.d__tilde__):'((-MS3dL1**2 + MXm**2)*(-3*gS3L1x1*MS3dL1**2*complexconjugate(gS3L1x1) + 3*gS3L1x1*MXm**2*complexconjugate(gS3L1x1)))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3dL1__tilde__,P.d):'((-MS3dL1**2 + MXm**2)*(-3*gS3L1x1*MS3dL1**2*complexconjugate(gS3L1x1) + 3*gS3L1x1*MXm**2*complexconjugate(gS3L1x1)))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3dL2,P.s__tilde__):'((-MS3dL2**2 + MXm**2)*(-3*gS3L2x2*MS3dL2**2*complexconjugate(gS3L2x2) + 3*gS3L2x2*MXm**2*complexconjugate(gS3L2x2)))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3dL2__tilde__,P.s):'((-MS3dL2**2 + MXm**2)*(-3*gS3L2x2*MS3dL2**2*complexconjugate(gS3L2x2) + 3*gS3L2x2*MXm**2*complexconjugate(gS3L2x2)))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3dL3,P.b__tilde__):'((3*gS3L3x3*MB**2*complexconjugate(gS3L3x3) - 3*gS3L3x3*MS3dL3**2*complexconjugate(gS3L3x3) + 3*gS3L3x3*MXm**2*complexconjugate(gS3L3x3))*cmath.sqrt(MB**4 - 2*MB**2*MS3dL3**2 + MS3dL3**4 - 2*MB**2*MXm**2 - 2*MS3dL3**2*MXm**2 + MXm**4))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3dL3__tilde__,P.b):'((3*gS3L3x3*MB**2*complexconjugate(gS3L3x3) - 3*gS3L3x3*MS3dL3**2*complexconjugate(gS3L3x3) + 3*gS3L3x3*MXm**2*complexconjugate(gS3L3x3))*cmath.sqrt(MB**4 - 2*MB**2*MS3dL3**2 + MS3dL3**4 - 2*MB**2*MXm**2 - 2*MS3dL3**2*MXm**2 + MXm**4))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3dR1,P.d__tilde__):'((-MS3dR1**2 + MXm**2)*(-3*gS3dR1x1*MS3dR1**2*complexconjugate(gS3dR1x1) + 3*gS3dR1x1*MXm**2*complexconjugate(gS3dR1x1)))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3dR1__tilde__,P.d):'((-MS3dR1**2 + MXm**2)*(-3*gS3dR1x1*MS3dR1**2*complexconjugate(gS3dR1x1) + 3*gS3dR1x1*MXm**2*complexconjugate(gS3dR1x1)))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3dR2,P.s__tilde__):'((-MS3dR2**2 + MXm**2)*(-3*gS3dR2x2*MS3dR2**2*complexconjugate(gS3dR2x2) + 3*gS3dR2x2*MXm**2*complexconjugate(gS3dR2x2)))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3dR2__tilde__,P.s):'((-MS3dR2**2 + MXm**2)*(-3*gS3dR2x2*MS3dR2**2*complexconjugate(gS3dR2x2) + 3*gS3dR2x2*MXm**2*complexconjugate(gS3dR2x2)))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3dR3,P.b__tilde__):'((3*gS3dR3x3*MB**2*complexconjugate(gS3dR3x3) - 3*gS3dR3x3*MS3dR3**2*complexconjugate(gS3dR3x3) + 3*gS3dR3x3*MXm**2*complexconjugate(gS3dR3x3))*cmath.sqrt(MB**4 - 2*MB**2*MS3dR3**2 + MS3dR3**4 - 2*MB**2*MXm**2 - 2*MS3dR3**2*MXm**2 + MXm**4))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3dR3__tilde__,P.b):'((3*gS3dR3x3*MB**2*complexconjugate(gS3dR3x3) - 3*gS3dR3x3*MS3dR3**2*complexconjugate(gS3dR3x3) + 3*gS3dR3x3*MXm**2*complexconjugate(gS3dR3x3))*cmath.sqrt(MB**4 - 2*MB**2*MS3dR3**2 + MS3dR3**4 - 2*MB**2*MXm**2 - 2*MS3dR3**2*MXm**2 + MXm**4))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3uL1,P.u__tilde__):'((-MS3uL1**2 + MXm**2)*(-3*gS3L1x1*MS3uL1**2*complexconjugate(gS3L1x1) + 3*gS3L1x1*MXm**2*complexconjugate(gS3L1x1)))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3uL1__tilde__,P.u):'((-MS3uL1**2 + MXm**2)*(-3*gS3L1x1*MS3uL1**2*complexconjugate(gS3L1x1) + 3*gS3L1x1*MXm**2*complexconjugate(gS3L1x1)))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3uL2,P.c__tilde__):'((-MS3uL2**2 + MXm**2)*(-3*gS3L2x2*MS3uL2**2*complexconjugate(gS3L2x2) + 3*gS3L2x2*MXm**2*complexconjugate(gS3L2x2)))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3uL2__tilde__,P.c):'((-MS3uL2**2 + MXm**2)*(-3*gS3L2x2*MS3uL2**2*complexconjugate(gS3L2x2) + 3*gS3L2x2*MXm**2*complexconjugate(gS3L2x2)))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3uL3,P.t__tilde__):'((-3*gS3L3x3*MS3uL3**2*complexconjugate(gS3L3x3) + 3*gS3L3x3*MT**2*complexconjugate(gS3L3x3) + 3*gS3L3x3*MXm**2*complexconjugate(gS3L3x3))*cmath.sqrt(MS3uL3**4 - 2*MS3uL3**2*MT**2 + MT**4 - 2*MS3uL3**2*MXm**2 - 2*MT**2*MXm**2 + MXm**4))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3uL3__tilde__,P.t):'((-3*gS3L3x3*MS3uL3**2*complexconjugate(gS3L3x3) + 3*gS3L3x3*MT**2*complexconjugate(gS3L3x3) + 3*gS3L3x3*MXm**2*complexconjugate(gS3L3x3))*cmath.sqrt(MS3uL3**4 - 2*MS3uL3**2*MT**2 + MT**4 - 2*MS3uL3**2*MXm**2 - 2*MT**2*MXm**2 + MXm**4))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3uR1,P.u__tilde__):'((-MS3uR1**2 + MXm**2)*(-3*gS3uR1x1*MS3uR1**2*complexconjugate(gS3uR1x1) + 3*gS3uR1x1*MXm**2*complexconjugate(gS3uR1x1)))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3uR1__tilde__,P.u):'((-MS3uR1**2 + MXm**2)*(-3*gS3uR1x1*MS3uR1**2*complexconjugate(gS3uR1x1) + 3*gS3uR1x1*MXm**2*complexconjugate(gS3uR1x1)))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3uR2,P.c__tilde__):'((-MS3uR2**2 + MXm**2)*(-3*gS3uR2x2*MS3uR2**2*complexconjugate(gS3uR2x2) + 3*gS3uR2x2*MXm**2*complexconjugate(gS3uR2x2)))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3uR2__tilde__,P.c):'((-MS3uR2**2 + MXm**2)*(-3*gS3uR2x2*MS3uR2**2*complexconjugate(gS3uR2x2) + 3*gS3uR2x2*MXm**2*complexconjugate(gS3uR2x2)))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3uR3,P.t__tilde__):'((-3*gS3uR3x3*MS3uR3**2*complexconjugate(gS3uR3x3) + 3*gS3uR3x3*MT**2*complexconjugate(gS3uR3x3) + 3*gS3uR3x3*MXm**2*complexconjugate(gS3uR3x3))*cmath.sqrt(MS3uR3**4 - 2*MS3uR3**2*MT**2 + MT**4 - 2*MS3uR3**2*MXm**2 - 2*MT**2*MXm**2 + MXm**4))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.S3uR3__tilde__,P.t):'((-3*gS3uR3x3*MS3uR3**2*complexconjugate(gS3uR3x3) + 3*gS3uR3x3*MT**2*complexconjugate(gS3uR3x3) + 3*gS3uR3x3*MXm**2*complexconjugate(gS3uR3x3))*cmath.sqrt(MS3uR3**4 - 2*MS3uR3**2*MT**2 + MT**4 - 2*MS3uR3**2*MXm**2 - 2*MT**2*MXm**2 + MXm**4))/(32.*cmath.pi*abs(MXm)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.S3dL1__tilde__,P.S3dL1):'((-2*ee**2*MS3dL1**2 + (ee**2*MZ**2)/2. - (3*cw**2*ee**2*MS3dL1**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MS3dL1**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MS3dL1**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.S3dL2__tilde__,P.S3dL2):'((-2*ee**2*MS3dL2**2 + (ee**2*MZ**2)/2. - (3*cw**2*ee**2*MS3dL2**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MS3dL2**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MS3dL2**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.S3dL3__tilde__,P.S3dL3):'((-2*ee**2*MS3dL3**2 + (ee**2*MZ**2)/2. - (3*cw**2*ee**2*MS3dL3**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MS3dL3**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MS3dL3**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.S3uL1__tilde__,P.S3uL1):'((2*ee**2*MS3uL1**2 - (ee**2*MZ**2)/2. - (3*cw**2*ee**2*MS3uL1**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MS3uL1**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MS3uL1**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.S3uL2__tilde__,P.S3uL2):'((2*ee**2*MS3uL2**2 - (ee**2*MZ**2)/2. - (3*cw**2*ee**2*MS3uL2**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MS3uL2**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MS3uL2**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.S3uL3__tilde__,P.S3uL3):'((2*ee**2*MS3uL3**2 - (ee**2*MZ**2)/2. - (3*cw**2*ee**2*MS3uL3**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MS3uL3**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MS3uL3**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

