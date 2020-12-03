# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.2.0 for Mac OS X x86 (64-bit) (September 11, 2017)
# Date: Tue 12 Mar 2019 11:12:13


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W+',
                     antitexname = 'W-',
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

W__minus__ = W__plus__.anti()

g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

ghA = Particle(pdg_code = 9000001,
               name = 'ghA',
               antiname = 'ghA~',
               spin = -1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghA',
               antitexname = 'ghA~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghA__tilde__ = ghA.anti()

ghZ = Particle(pdg_code = 9000002,
               name = 'ghZ',
               antiname = 'ghZ~',
               spin = -1,
               color = 1,
               mass = Param.MZ,
               width = Param.WZ,
               texname = 'ghZ',
               antitexname = 'ghZ~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghZ__tilde__ = ghZ.anti()

ghWp = Particle(pdg_code = 9000003,
                name = 'ghWp',
                antiname = 'ghWp~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWp',
                antitexname = 'ghWp~',
                charge = 1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWp__tilde__ = ghWp.anti()

ghWm = Particle(pdg_code = 9000004,
                name = 'ghWm',
                antiname = 'ghWm~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWm',
                antitexname = 'ghWm~',
                charge = -1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWm__tilde__ = ghWm.anti()

ghG = Particle(pdg_code = 82,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghG',
               antitexname = 'ghG~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghG__tilde__ = ghG.anti()

ve = Particle(pdg_code = 12,
              name = 've',
              antiname = 've~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 've',
              antitexname = 've~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

ve__tilde__ = ve.anti()

vm = Particle(pdg_code = 14,
              name = 'vm',
              antiname = 'vm~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vm',
              antitexname = 'vm~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vm__tilde__ = vm.anti()

vt = Particle(pdg_code = 16,
              name = 'vt',
              antiname = 'vt~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vt',
              antitexname = 'vt~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vt__tilde__ = vt.anti()

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.ZERO,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e+',
                      charge = -1,
                      GhostNumber = 0,
                      LeptonNumber = 1,
                      Y = 0)

e__plus__ = e__minus__.anti()

mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.ZERO,
                       width = Param.ZERO,
                       texname = 'mu-',
                       antitexname = 'mu+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

mu__plus__ = mu__minus__.anti()

ta__minus__ = Particle(pdg_code = 15,
                       name = 'ta-',
                       antiname = 'ta+',
                       spin = 2,
                       color = 1,
                       mass = Param.MTA,
                       width = Param.ZERO,
                       texname = 'ta-',
                       antitexname = 'ta+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

ta__plus__ = ta__minus__.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'u~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

u__tilde__ = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'c~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'c~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

c__tilde__ = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 't~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

t__tilde__ = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'd~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'd~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

d__tilde__ = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 's~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 's',
             antitexname = 's~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

s__tilde__ = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'b~',
             spin = 2,
             color = 3,
             mass = Param.MB,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'b~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

b__tilde__ = b.anti()

H = Particle(pdg_code = 25,
             name = 'H',
             antiname = 'H',
             spin = 1,
             color = 1,
             mass = Param.MH,
             width = Param.WH,
             texname = 'H',
             antitexname = 'H',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

G0 = Particle(pdg_code = 250,
              name = 'G0',
              antiname = 'G0',
              spin = 1,
              color = 1,
              mass = Param.MZ,
              width = Param.WZ,
              texname = 'G0',
              antitexname = 'G0',
              goldstone = True,
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

G__plus__ = Particle(pdg_code = 251,
                     name = 'G+',
                     antiname = 'G-',
                     spin = 1,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'G+',
                     antitexname = 'G-',
                     goldstone = True,
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

G__minus__ = G__plus__.anti()

Xr = Particle(pdg_code = 51,
              name = 'Xr',
              antiname = 'Xr',
              spin = 1,
              color = 1,
              mass = Param.MXr,
              width = Param.ZERO,
              texname = 'Xr',
              antitexname = 'Xr',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

Xv = Particle(pdg_code = 53,
              name = 'Xv',
              antiname = 'Xv',
              spin = 3,
              color = 1,
              mass = Param.MXv,
              width = Param.ZERO,
              texname = 'Xv',
              antitexname = 'Xv',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

F3uL1 = Particle(pdg_code = 3000002,
                 name = 'F3uL1',
                 antiname = 'F3uL1~',
                 spin = 2,
                 color = 3,
                 mass = Param.MF3uL1,
                 width = Param.WF3uL1,
                 texname = 'F3uL1',
                 antitexname = 'F3uL1~',
                 charge = 2/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 0)

F3uL1__tilde__ = F3uL1.anti()

F3uL2 = Particle(pdg_code = 3000004,
                 name = 'F3uL2',
                 antiname = 'F3uL2~',
                 spin = 2,
                 color = 3,
                 mass = Param.MF3uL2,
                 width = Param.WF3uL2,
                 texname = 'F3uL2',
                 antitexname = 'F3uL2~',
                 charge = 2/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 0)

F3uL2__tilde__ = F3uL2.anti()

F3uL3 = Particle(pdg_code = 3000006,
                 name = 'F3uL3',
                 antiname = 'F3uL3~',
                 spin = 2,
                 color = 3,
                 mass = Param.MF3uL3,
                 width = Param.WF3uL3,
                 texname = 'F3uL3',
                 antitexname = 'F3uL3~',
                 charge = 2/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 0)

F3uL3__tilde__ = F3uL3.anti()

F3dL1 = Particle(pdg_code = 3000001,
                 name = 'F3dL1',
                 antiname = 'F3dL1~',
                 spin = 2,
                 color = 3,
                 mass = Param.MF3dL1,
                 width = Param.WF3dL1,
                 texname = 'F3dL1',
                 antitexname = 'F3dL1~',
                 charge = -1/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 0)

F3dL1__tilde__ = F3dL1.anti()

F3dL2 = Particle(pdg_code = 3000003,
                 name = 'F3dL2',
                 antiname = 'F3dL2~',
                 spin = 2,
                 color = 3,
                 mass = Param.MF3dL2,
                 width = Param.WF3dL2,
                 texname = 'F3dL2',
                 antitexname = 'F3dL2~',
                 charge = -1/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 0)

F3dL2__tilde__ = F3dL2.anti()

F3dL3 = Particle(pdg_code = 3000005,
                 name = 'F3dL3',
                 antiname = 'F3dL3~',
                 spin = 2,
                 color = 3,
                 mass = Param.MF3dL3,
                 width = Param.WF3dL3,
                 texname = 'F3dL3',
                 antitexname = 'F3dL3~',
                 charge = -1/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 0)

F3dL3__tilde__ = F3dL3.anti()

F3uR1 = Particle(pdg_code = 4000002,
                 name = 'F3uR1',
                 antiname = 'F3uR1~',
                 spin = 2,
                 color = 3,
                 mass = Param.MF3uR1,
                 width = Param.WF3uR1,
                 texname = 'F3uR1',
                 antitexname = 'F3uR1~',
                 charge = 2/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 0)

F3uR1__tilde__ = F3uR1.anti()

F3uR2 = Particle(pdg_code = 4000004,
                 name = 'F3uR2',
                 antiname = 'F3uR2~',
                 spin = 2,
                 color = 3,
                 mass = Param.MF3uR2,
                 width = Param.WF3uR2,
                 texname = 'F3uR2',
                 antitexname = 'F3uR2~',
                 charge = 2/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 0)

F3uR2__tilde__ = F3uR2.anti()

F3uR3 = Particle(pdg_code = 4000006,
                 name = 'F3uR3',
                 antiname = 'F3uR3~',
                 spin = 2,
                 color = 3,
                 mass = Param.MF3uR3,
                 width = Param.WF3uR3,
                 texname = 'F3uR3',
                 antitexname = 'F3uR3~',
                 charge = 2/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 0)

F3uR3__tilde__ = F3uR3.anti()

F3dR1 = Particle(pdg_code = 4000001,
                 name = 'F3dR1',
                 antiname = 'F3dR1~',
                 spin = 2,
                 color = 3,
                 mass = Param.MF3dR1,
                 width = Param.WF3dR1,
                 texname = 'F3dR1',
                 antitexname = 'F3dR1~',
                 charge = -1/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 0)

F3dR1__tilde__ = F3dR1.anti()

F3dR2 = Particle(pdg_code = 4000003,
                 name = 'F3dR2',
                 antiname = 'F3dR2~',
                 spin = 2,
                 color = 3,
                 mass = Param.MF3dR2,
                 width = Param.WF3dR2,
                 texname = 'F3dR2',
                 antitexname = 'F3dR2~',
                 charge = -1/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 0)

F3dR2__tilde__ = F3dR2.anti()

F3dR3 = Particle(pdg_code = 4000005,
                 name = 'F3dR3',
                 antiname = 'F3dR3~',
                 spin = 2,
                 color = 3,
                 mass = Param.MF3dR3,
                 width = Param.WF3dR3,
                 texname = 'F3dR3',
                 antitexname = 'F3dR3~',
                 charge = -1/3,
                 GhostNumber = 0,
                 LeptonNumber = 0,
                 Y = 0)

F3dR3__tilde__ = F3dR3.anti()

