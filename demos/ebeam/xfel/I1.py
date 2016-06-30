from ocelot import *
tws_5M = Twiss()
tws_5M.beta_x = 29.171000000
tws_5M.beta_y = 29.171000000
tws_5M.alpha_x = 10.955000
tws_5M.alpha_y = 10.955000
tws_5M.E = 0.005
tws_5M.s = 0.0


tws_150M = Twiss()
tws_150M.beta_x = 13.172200000
tws_150M.beta_y = 13.172200
tws_150M.alpha_x = -1.635400
tws_150M.alpha_y = -1.635400
tws_150M.E = 0.1503
tws_150M.s = 14.2441



d0276 = Drift(l = 0.276, eid= 'd0276')
d0324 = Drift(l = 0.324, eid= 'd0324')
d0100 = Drift(l = 0.1, eid= 'd0100')
d0050 = Drift(l = 0.05, eid= 'd0050')

i1_kdc = Drift(l = 0.2, eid= 'KDC.24.I1')
d0150 = Drift(l = 0.15, eid= 'd0150')
d01988 = Drift(l = 0.198782, eid= 'd01988')
d02292 = Drift(l = 0.229218, eid= 'd02292')
d0060 = Drift(l = 0.06, eid= 'd0060')
d0225 = Drift(l = 0.225, eid= 'd0225')
i1_dccol = Drift(l = 0, eid= 'i1_dccol')
d0088 = Drift(l = 0.088, eid= 'd0088')
d0111 = Drift(l = 0.111, eid= 'd0111')
d03988 = Drift(l = 0.3864, eid= 'd03988')
start_sim = Marker(eid="start_sim")
i1_cfbi = (Drift(l = 0.5512 - 0.0996, eid= 'i1_cfbi'), start_sim, Drift(l = 0.0996, eid= 'i1_cfbi_1'))
d0080 = Drift(l = 0.08, eid= 'd0080')
d01416 = Drift(l = 0.1416, eid= 'd01416')
d02043 = Drift(l = 0.2043, eid= 'd02043')
ltwakecav = Drift(l = 0.0, eid= 'ltwakecav')
d0085 = Drift(l = 0.085, eid= 'd0085')
d00729 = Drift(l = 0.0729, eid= 'd00729')
d0300 = Drift(l = 0.3, eid= 'd0300')
d00611 = Drift(l = 0.0611, eid= 'd00611')
d0075 = Drift(l = 0.075, eid= 'd0075')
d0020 = Drift(l = 0.02, eid= 'd0020')
d0102 = Drift(l = 0.102, eid= 'd0102')
ltwakecav3 = Drift(l = 0.0, eid= 'ltwakecav3')
i1_ctbi = Drift(l = 1.04, eid= 'i1_ctbi')
d12964 = Drift(l = 1.2964, eid= 'd12964')
d02519 = Drift(l = 0.2519, eid= 'd02519')
d0105 = Drift(l = 0.105, eid= 'd0105')
d0090 = Drift(l = 0.09, eid= 'd0090')
d01275 = Drift(l = 0.1275, eid= 'd01275')
d0096 = Drift(l = 0.096, eid= 'd0096')
d00315 = Drift(l = 0.0315, eid= 'd00315')
d00862 = Drift(l = 0.0862, eid= 'd00862')
d01423 = Drift(l = 0.1423, eid= 'd01423')
d0051 = Drift(l = 0.051, eid= 'd0051')
cd0100i = Drift(l = 0.100496902224, eid= 'cd0100i')
d006075 = Drift(l = 0.06075, eid= 'd006075')
d014425 = Drift(l = 0.14425, eid= 'd014425')
d0064 = Drift(l = 0.064, eid= 'd0064')
d0030 = Drift(l = 0.03, eid= 'd0030')
d0120 = Drift(l = 0.12, eid= 'd0120')
d010849 = Drift(l = 0.10849, eid= 'd010849')
d0200 = Drift(l = 0.2, eid= 'd0200')

d0003 = Drift(l = 0.003, eid= 'd0003')

d0070 = Drift(l = 0.07, eid= 'd0070')
d0122 = Drift(l = 0.122, eid= 'd0122')
d0175 = Drift(l = 0.175, eid= 'd0175')
i1_kax = Drift(l = 0.35, eid= 'i1_kax')
d0285 = Drift(l = 0.285, eid= 'd0285')
d0035 = Drift(l = 0.035, eid= 'd0035')
d0125 = Drift(l = 0.125, eid= 'd0125')
d0220 = Drift(l = 0.22, eid= 'd0220')
d0380 = Drift(l = 0.38, eid= 'd0380')
d01817 = Drift(l = 0.1817, eid= 'd01817')
d00143 = Drift(l = 0.0143, eid= 'd00143')
d0350 = Drift(l = 0.35, eid= 'd0350')
d0054 = Drift(l = 0.054, eid= 'd0054')
d0400 = Drift(l = 0.4, eid= 'd0400')
i1_bb_0 = Drift(l = 0.5, eid= 'i1_bb_0')
d0040 = Drift(l = 0.04, eid= 'd0040')
d0500 = Drift(l = 0.5, eid= 'd0500')
i1_vcbshut = Drift(l = 0.3, eid= 'i1_vcbshut')
d2900 = Drift(l = 2.9, eid= 'd2900')
d1800 = Drift(l = 1.8, eid= 'd1800')
d0700 = Drift(l = 0.7, eid= 'd0700')
d02012268 = Drift(l = 0.201226854, eid= 'd02012268')
i1_cbl = Drift(l = 0.0, eid= 'i1_cbl')
d0135 = Drift(l = 0.135, eid= 'd0135')
d0165 = Drift(l = 0.165, eid= 'd0165')
d00804818 = Drift(l = 0.0804818046, eid= 'd00804818')
d01409819 = Drift(l = 0.140981989, eid= 'd01409819')
d01086082 = Drift(l = 0.1086082922, eid= 'd01086082')
d01325 = Drift(l = 0.1325, eid= 'd01325')
d01175 = Drift(l = 0.1175, eid= 'd01175')
d00175 = Drift(l = 0.0175, eid= 'd00175')
d000013 = Drift(l = 0.00013, eid= 'd000013')
d0900 = Drift(l = 0.9, eid= 'd0900')
d0110 = Drift(l = 0.11, eid= 'd0110')
d01725 = Drift(l = 0.1725, eid= 'd01725')
d1000i = Drift(l = 1.00887371317, eid= 'd1000i')
i1_cbb_2 = Drift(l = 0.0, eid= 'i1_cbb_2')
d03975 = Drift(l = 0.3975, eid= 'd03975')
i1_colo = Drift(l = 0, eid= 'i1_colo')
i1_colu = Drift(l = 0, eid= 'i1_colu')
d03825 = Drift(l = 0.3825, eid= 'd03825')
d0310 = Drift(l = 0.31, eid= 'd0310')
d0325 = Drift(l = 0.325, eid= 'd0325')
i1_cbb_3 = Drift(l = 0.0, eid= 'i1_cbb_3')
d0600 = Drift(l = 0.6, eid= 'd0600')
d1000im = Drift(l = 0.408873713169, eid= 'd1000im')
i1_cbb_4 = Drift(l = 0.0, eid= 'i1_cbb_4')
d01225 = Drift(l = 0.1225, eid= 'd01225')
d01125 = Drift(l = 0.1125, eid= 'd01125')
i1_vcdst = Drift(l = 1.215, eid= 'i1_vcdst')
d03643 = Drift(l = 0.3643, eid= 'd03643')
d09007 = Drift(l = 0.9007, eid= 'd09007')
d01585 = Drift(l = 0.1585, eid= 'd01585')
d109132 = Drift(l = 1.09132, eid= 'd109132')
d034903 = Drift(l = 0.34903, eid= 'd034903')
d009115 = Drift(l = 0.09115, eid= 'd009115')
d01628 = Drift(l = 0.1628, eid= 'd01628')
d03522 = Drift(l = 0.3522, eid= 'd03522')

# Correctors
i1_ckx_23_i1 = Hcor(l=0.025, eid='CKX.23.I1')
i1_cky_23_i1 = Vcor(l=0.025, eid='CKY.23.I1')

i1_ckx_24_i1 = Hcor(l=0.025, eid='CKX.24.I1')
i1_cky_24_i1 = Vcor(l=0.025, eid='CKY.24.I1')

i1_ckx_25_i1 = Hcor(l=0.025, eid='CKX.25.I1')
i1_cky_25_i1 = Vcor(l=0.025, eid='CKY.25.I1')

cx_37_i1 = Hcor(l = 0, eid= 'CX.37.I1')
cy_37_i1 = Vcor(l = 0, eid= 'CY.37.I1')
cx_39_i1 = Hcor(l = 0, eid= 'CX.39.I1')
cy_39_i1 = Vcor(l = 0, eid= 'CY.39.I1')

ciy_51_i1 = Vcor(l=0.1, eid='CIY.51.I1')
cix_51_i1 = Hcor(l=0.1, eid='CIX.51.I1')

ciy_55_i1 = Vcor(l=0.1, eid='CIY.55.I1')
cix_57_i1 = Hcor(l=0.1, eid='CIX.57.I1')

ciy_58_i1 = Vcor(l=0.1, eid='CIY.58.I1')
ciy_63_i1 = Vcor(l=0.1, eid='CIY.63.I1')

cix_65_i1 = Hcor(l=0.1, eid='CIX.65.I1')
ciy_72_i1 = Vcor(l=0.1, eid='CIY.72.I1')

cix_73i_i1 = Hcor(l=0.1, eid='CIX.73I.I1')
cix_73ii_i1 = Hcor(l=0.1, eid='CIX.73II.I1')
ciy_75_i1 = Vcor(l=0.1, eid='CIY.75.I1')

cix_76_i1 = Hcor(l=0.1, eid='CIX.76.I1')
cix_78_i1 = Hcor(l=0.1, eid='CIX.78.I1')
ciy_80_i1 = Vcor(l=0.1, eid='CIY.80.I1')

cix_81_i1 = Hcor(l=0.1, eid='CIX.81.I1')
cix_83_i1 = Hcor(l=0.1, eid='CIX.83.I1')
ciy_85_i1 = Vcor(l=0.1, eid='CIY.85.I1')

cix_86_i1 = Hcor(l=0.1, eid='CIX.86.I1')
cix_88_i1 = Hcor(l=0.1, eid='CIX.88.I1')
cix_90_i1 = Vcor(l=0.1, eid='CIX.90.I1')

ciy_92_i1 = Vcor(l=0.1, eid='CIY.92.I1')
ciy_94_i1 = Vcor(l=0.1, eid='CIY.94.I1')
cix_95_i1 = Hcor(l=0.1, eid='CIX.95.I1')

cix_102_i1 = Hcor(l=0.1, eid='CIX.102.I1')
ciy_103_i1 = Vcor(l=0.1, eid='CIY.103.I1')
cix_104_i1 = Hcor(l=0.1, eid='CIX.104.I1')
ciy_107_i1 = Vcor(l=0.1, eid='CIY.107.I1')
cix_109_i1 = Hcor(l=0.1, eid='CIX.109.I1')
ciy_112_i1 = Vcor(l=0.1, eid='CIY.112.I1')
cix_114_i1 = Hcor(l=0.1, eid='CIX.114.I1')
ciy_116_i1 = Vcor(l=0.1, eid='CIY.116.I1')
cix_118_i1 = Hcor(l=0.1, eid='CIX.118.I1')

i1_cix_drift = Drift(l=0.1, eid="i1.cix.drift")
# quadrupoles 
q_37_i1 = Quadrupole(l=0.3, k1 = -1.537886,   eid= 'Q.37.I1')
q_38_i1 = Quadrupole(l=0.3, k1 = 1.435078,    eid= 'Q.38.I1')
qi_46_i1 = Quadrupole(l=0.2, k1 = -0.0932136,  eid= 'QI.46.I1')
qi_47_i1 = Quadrupole(l=0.2, k1 = 0.8875443,   eid= 'QI.47.I1')
qi_50_i1 = Quadrupole(l=0.2, k1 = -0.7654263,  eid= 'QI.50.I1')
qi_52_i1 = Quadrupole(l=0.2, k1 = -0.07117866, eid= 'QI.52.I1')
qi_53_i1 = Quadrupole(l=0.2, k1 = 2.494601,    eid= 'QI.53.I1')
qi_54_i1 = Quadrupole(l=0.2, k1 = 0.9480791,   eid= 'QI.54.I1')
qi_55_i1 = Quadrupole(l=0.2, k1 = -4.15374,    eid= 'QI.55.I1')
qi_57_i1 = Quadrupole(l=0.2, k1 = 4.15355,     eid= 'QI.57.I1')
qi_59_i1 = Quadrupole(l=0.2, k1 = -4.15374,    eid= 'QI.59.I1')
qi_60_i1 = Quadrupole(l = 0.2, k1 = 2.128,      eid= 'QI.60.I1')
qi_61_i1 = Quadrupole(l = 0.2, k1 = 0.933,      eid= 'QI.61.I1')
qi_63_i1 = Quadrupole(l = 0.2, k1 = -2.2531364, eid= 'QI.63.I1')
qi_66_i1 = Quadrupole(l = 0.2, k1 = 2.441008,   eid= 'QI.66.I1')

i1_qi_15 = Quadrupole(l = 0.2, k1 = -2.559564,       eid= 'i1_qi_15')
i1_qi_16 = Quadrupole(l = 0.2, k1 = 3.653292,        eid= 'i1_qi_16')
i1_qi_17 = Quadrupole(l = 0.2, k1 = -4.341087,       eid= 'i1_qi_17')
i1_qih_18 = Quadrupole(l = 0.1, k1 = 5.444766974,    eid= 'i1_qih_18')
i1_qi_19 = Quadrupole(l = 0.2, k1 = -5.865493569,    eid= 'i1_qi_19')
i1_qi_20 = Quadrupole(l = 0.2, k1 = 5.906955582,     eid= 'i1_qi_20')
i1_qi_21 = Quadrupole(l = 0.2, k1 = -5.865493569,    eid= 'i1_qi_21')
i1_qih_22 = Quadrupole(l = 0.1, k1 = 5.444766974,    eid= 'i1_qih_22')
i1_qi_24 = Quadrupole(l = 0.2, k1 = 5.906955582,     eid= 'i1_qi_24')
i1_qi_23 = Quadrupole(l = 0.2, k1 = -5.865493569,    eid= 'i1_qi_23')
i1_qi_25 = Quadrupole(l = 0.2, k1 = -0.525034487046, eid= 'i1_qi_25')
i1_qi_26 = Quadrupole(l = 0.2, k1 = 3.85432911747,   eid= 'i1_qi_26')
i1_qi_27 = Quadrupole(l = 0.2, k1 = -3.56939610008,  eid= 'i1_qi_27')
i1_qi_28 = Quadrupole(l = 0.2, k1 = 0.780579004468,  eid= 'i1_qi_28')
i1_qi_29 = Quadrupole(l = 0.2, k1 = -1.63148145355,  eid= 'i1_qi_29')
i1_qi_30 = Quadrupole(l = 0.2, k1 = 1.76185265487, eid= 'i1_qi_30')
i1_qi_31 = Quadrupole(l = 0.2, k1 = -1.8, eid= 'i1_qi_31')
i1_qi_32 = Quadrupole(l = 0.2, k1 = 1.8, eid= 'i1_qi_32')
i1_qi_33 = Quadrupole(l = 0.2, k1 = 1.18485127653, eid= 'i1_qi_33')
i1_qi_34 = Quadrupole(l = 0.2, k1 = 0.638691311326, eid= 'i1_qi_34')
i1_qi_35 = Quadrupole(l = 0.2, k1 = -1.11866444531, eid= 'i1_qi_35')

# bending magnets 
i1_bl_1_1 = Bend(l = 0.200330283531, angle = -0.099484, e1 = 0.0, e2 = -0.099484, tilt = 0.0, eid= 'i1_bl_1_1')
i1_bl_1_2 = Bend(l = 0.200330283531, angle = 0.099484, e1 = 0.099484, e2 = 0.0, tilt = 0.0, eid= 'i1_bl_1_2')
i1_bl_3 = Bend(l = 0.200330283531, angle = 0.099484, e1 = 0.0, e2 = 0.099484, tilt = 0.0, eid= 'i1_bl_3')
i1_bl_4 = Bend(l = 0.200330283531, angle = -0.099484, e1 = -0.099484, e2 = 0.0, tilt = 0.0, eid= 'i1_bl_4')
i1_bseci = RBend(l = 0.4, angle = 0.0, e1 = 0.0, e2 = 0.0, tilt = 0, eid= 'i1_bseci')
i1_bl_6_1 = Bend(l = 0.200102663853, angle = -0.110974039346, e1 = -0.0554870196731, e2 = -0.0554870196731, tilt = 1.5707963268, eid= 'i1_bl_6_1')
i1_bl_7_1 = Bend(l = 0.200015161073, angle = 0.0426524581, e1 = 0.02132622905, e2 = 0.02132622905, tilt = 1.5707963268, eid= 'i1_bl_7_1')
i1_bl_8_2 = Bend(l = 0.200102663853, angle = 0.110974039346, e1 = 0.0554870196731, e2 = 0.0554870196731, tilt = 1.5707963268, eid= 'i1_bl_8_2')
i1_bl_7_2 = Bend(l = 0.200015161073, angle = -0.0426524581, e1 = -0.02132622905, e2 = -0.02132622905, tilt = 1.5707963268, eid= 'i1_bl_7_2')
i1_bb_1_1 = Bend(l = 0.501471120927, angle = 0.132729704703, e1 = 0.0, e2 = 0.132729704703, tilt = 1.5707963268, eid= 'i1_bb_1_1')
i1_bb_1_2 = Bend(l = 0.501471120927, angle = -0.132729704703, e1 = -0.132729704703, e2 = 0.0, tilt = 1.5707963268, eid= 'i1_bb_1_2')
i1_bb_1_3 = Bend(l = 0.501471120927, angle = -0.132729704703, e1 = 0.0, e2 = -0.132729704703, tilt = 1.5707963268, eid= 'i1_bb_1_3')
i1_bb_1_4 = Bend(l = 0.501471120927, angle = 0.132729704703, e1 = 0.132729704703, e2 = 0.0, tilt = 1.5707963268, eid= 'i1_bb_1_4')

# correctors 

# markers 
i1_start_i1 = Marker(eid= 'i1_start_i1')
i1_gun = Marker(eid= 'i1_gun')
i1_scrn = Marker(eid= 'i1_scrn')
i1_fcup = Marker(eid= 'i1_fcup')
i1_startdrm = Marker(eid= 'i1_startdrm')
i1_tora = Marker(eid= 'i1_tora')
i1_dcm = Marker(eid= 'i1_dcm')
i1_start_l0 = Marker(eid= 'i1_start_l0')
i1_vcst35t78 = Marker(eid= 'i1_vcst35t78')
i1_stac_a1_1 = Marker(eid= 'i1_stac_a1_1')
miac = Marker(eid= 'miac')
i1_enac_a1_1 = Marker(eid= 'i1_enac_a1_1')
i1_vcst78t30 = Marker(eid= 'i1_vcst78t30')
i1_stac_ah1_1 = Marker(eid= 'i1_stac_ah1_1')
i1_enac_ah1_1 = Marker(eid= 'i1_enac_ah1_1')
i1_vcst30t78 = Marker(eid= 'i1_vcst30t78')
i1_vcst78t40 = Marker(eid= 'i1_vcst78t40')
i1_end_l0 = Marker(eid= 'i1_end_l0')
i1_bam = Marker(eid= 'i1_bam')
i1_mpbpmf = Marker(eid= 'i1_mpbpmf')
i1_start_lh = Marker(eid= 'i1_start_lh')
i1_vcst40t35 = Marker(eid= 'i1_vcst40t35')
i1_otrl = Marker(eid= 'i1_otrl')
i1_vcst35t40 = Marker(eid= 'i1_vcst35t40')
i1_end_lh = Marker(eid= 'i1_end_lh')
i1_eod = Marker(eid= 'i1_eod')
i1_start_dia = Marker(eid= 'i1_start_dia')
i1_otrc = Marker(eid= 'i1_otrc')
i1_starti1d = Marker(eid= 'i1_starti1d')
i1_start_dog = Marker(eid= 'i1_start_dog')
i1_end_dog = Marker(eid= 'i1_end_dog')
i1_start_mid = Marker(eid= 'i1_start_mid')
i1_vcst40t400y = Marker(eid= 'i1_vcst40t400y')
i1_vcst400y = Marker(eid= 'i1_vcst400y')
i1_otrs = Marker(eid= 'i1_otrs')
i1_vcst400yt40 = Marker(eid= 'i1_vcst400yt40')
i1_vcst40y = Marker(eid= 'i1_vcst40y')
i1_end_mid = Marker(eid= 'i1_end_mid')
i1_start_ps = Marker(eid= 'i1_start_ps')
i1_otra = Marker(eid= 'i1_otra')
i1_end_i1 = Marker(eid= 'i1_end_i1')

# monitor 
i1_bpmg = Monitor(eid= 'i1_bpmg')
i1_bpmc = Monitor(eid= 'i1_bpmc')
i1_bpmr = Monitor(eid= 'i1_bpmr')
i1_bpmf = Monitor(eid= 'i1_bpmf')
i1_bpma = Monitor(eid= 'i1_bpma')
i1_bpms = Monitor(eid= 'i1_bpms')

# sextupoles 
i1_sc_1_1 = Sextupole(l=0.1, k2=-98.1752276195, tilt = 1.5707963268, eid= 'i1_sc_1_1')
i1_sc_2_1 = Sextupole(l=0.1, k2=-59.4821133431, tilt = 1.5707963268, eid= 'i1_sc_2_1')
i1_sc_1_2 = Sextupole(l=0.1, k2=98.1752276195, tilt = 1.5707963268, eid= 'i1_sc_1_2')
i1_sc_2_2 = Sextupole(l=0.1, k2=59.4821133431, tilt = 1.5707963268, eid= 'i1_sc_2_2')

# octupole 

# undulator 

# cavity 
i1_c_a1 = Cavity(l = 1.0377, v = 0.01815975, delta_e = 0.01815975, freq = 1300.0, phi = 0.0, volterr = 0.0, eid='C.A1.I1')
#i1_c3_ah1 = Cavity(l = 0.346, v = -0.0024999884, delta_e = 0.0024999884, freq = 3900.0, phi = 180., volterr = 0.0, id = 'i1_c3_ah1')
i1_c3_ah1 = Cavity(l = 0.346, v = 0.00249998841, delta_e = -0.0024999884, freq = 3900.0, phi = 180., volterr = 0.0, eid= 'C3.AH1.I1')
i1_tdsa = Cavity(l = 0.7, v = 0.0, delta_e = 0.0, freq = 2800.0, phi = 0.0, volterr = 0.0, eid= 'TDSA.52.I1')

# rfcavity 

# Matrices 
i1_undu = Matrix(l = 0.74, rm11 = 1.0, rm12 = 0.74, rm13 = 0.0, rm21 = 0.0, rm22 = 1.0, rm33 = 0.943430542565, rm34 = 0.725992855245, rm43 = -0.15143235992, rm44 = 0.943430542565, eid= 'i1_undu')

# Solenoids 
i1_sola_1 = Solenoid(l = 0.0, k = 0.0, eid= 'SOLA.23.I1')
i1_solb_1 = Solenoid(l = 0.0, k = 0.0, eid= 'SOLB.23.I1')

# lattice 

gun_5MeV = (i1_start_i1, i1_gun, i1_sola_1, d0276, i1_solb_1, d0324, d0100, 
d0050, i1_ckx_23_i1, i1_cky_23_i1, i1_kdc, d0050, i1_bpmg, d0150, i1_scrn,
i1_fcup, d01988, i1_startdrm, d02292, d0100, i1_ckx_24_i1, i1_cky_24_i1, d0060,
i1_tora, d0225, i1_scrn, i1_fcup, i1_dccol, d0088, i1_bpmg, d0111, 
i1_dcm, d0050, i1_ckx_25_i1, i1_cky_25_i1, d03988, i1_start_l0, i1_vcst35t78, i1_cfbi,
i1_stac_a1_1, d0080, d01416, i1_c_a1, d02043, ltwakecav, d01416, i1_c_a1, 
d02043, ltwakecav, d01416, i1_c_a1, d02043, ltwakecav, d01416, i1_c_a1, 
d02043, ltwakecav, miac, d01416, i1_c_a1, d02043, ltwakecav, d01416, 
i1_c_a1, d02043, ltwakecav, d01416, i1_c_a1, d02043, ltwakecav, d01416, 
i1_c_a1)



i1_150M = (d02043, ltwakecav, q_37_i1, cx_37_i1, cy_37_i1, d0085, i1_bpmc,
d0085, d00729, d0300, i1_enac_a1_1, i1_vcst78t30, i1_stac_ah1_1, d00611, d0075, 
d0085, i1_bpmr, d0085, q_38_i1, cx_39_i1, cy_39_i1, d0020, d0102,
d0080, i1_c3_ah1, d0080, ltwakecav3, d0102, d0080, i1_c3_ah1, d0080, 
ltwakecav3, d0102, miac, d0080, i1_c3_ah1, d0080, ltwakecav3, d0102, 
d0080, i1_c3_ah1, d0080, ltwakecav3, d0102, d0080, i1_c3_ah1, d0080, 
ltwakecav3, d0102, d0080, i1_c3_ah1, d0080, ltwakecav3, d0102, d0080, 
i1_c3_ah1, d0080, ltwakecav3, d0102, d0080, i1_c3_ah1, d0080, ltwakecav3, 
d0075, i1_enac_ah1_1, i1_vcst30t78, i1_ctbi, i1_vcst78t40, i1_end_l0, d12964, i1_tora, 
d02519, d0100, qi_46_i1, d0105, i1_bam, d0090, d01275, i1_bpmf,
d0096, i1_mpbpmf, d00315, d00862, i1_dcm, d01423, qi_47_i1, d0100,
i1_start_lh, i1_vcst40t35, d0051, i1_bl_1_1, cd0100i, i1_bl_1_2, d006075, d00315, 
i1_mpbpmf, d0096, i1_bpmf, d01275, d014425, i1_otrl, d0064, d0100, 
d0030, i1_undu, d0030, d0100, d0064, i1_otrl, d0120, i1_bl_3, 
cd0100i, i1_bl_4, d0051, i1_vcst35t40, i1_end_lh, d0100, qi_50_i1, d010849,
d0100, i1_eod, d0200, ciy_51_i1, d0100, d0200, d0003, cix_51_i1,
d0070, d01275, i1_bpmf, d0096, i1_mpbpmf, d00315, d0075, qi_52_i1,
d0070, i1_tdsa, d0070, qi_53_i1, d0122, d0175, i1_kax, d0105,
qi_54_i1, d0105, i1_kax, d0285, i1_start_dia, d0035, i1_otrc, d0125,
d0050, ciy_55_i1, d0150, i1_bpma, d0150, qi_55_i1, d0105, i1_kax,
d0285, d0035, i1_otrc, d0125, d0050, cix_57_i1, d0150, i1_bpma,
d0150, qi_57_i1, d0105, i1_kax, d0285, d0035, i1_otrc, d0125,
d0150, ciy_58_i1, d0050, d0150, qi_59_i1, d0220, i1_bpma, d0380,
i1_otrc, d0200, d0100, qi_60_i1, d0100, d01817, i1_tora, d00143,
d0350, i1_bpma, d0150, i1_bpma, d0054, d0200, qi_61_i1, d0150,
d0400, i1_starti1d, i1_bb_0, d0200, d0200, d0040, d0100, d0200, 
ciy_63_i1, d0100, qi_63_i1, d0150, i1_bpma, d0150, d0400, i1_bseci,
d0500, cix_65_i1, d0150, i1_vcbshut, d0200, qi_66_i1, d2900, i1_qi_15,
d1800, i1_qi_16, d0700, i1_bpma, d0200, i1_qi_17, d0200, ciy_72_i1,
d0200, cix_73i_i1, d0100, i1_start_dog, i1_qih_18, i1_qih_18, d02012268, i1_bl_6_1,
i1_cbl, d0135, cix_73ii_i1, d0165, d00804818, i1_sc_1_1, d0100, i1_qi_19,
d0100, i1_sc_2_1, d01409819, i1_bl_7_1, d01086082, d0050, i1_bpma, d01325, 
ciy_75_i1, d01175, i1_qi_20, d0135, cix_76_i1, d0165, d01086082, i1_bl_7_1,
d01409819, i1_sc_2_1, d0100, i1_qi_19, d0100, i1_sc_1_1, d00804818, d0050, 
d0100, d0100, i1_bpma, d0150, i1_bl_6_1, d02012268, i1_qih_18, i1_qih_18, 
d02012268, i1_bl_6_1, i1_cbl, d0135, cix_78_i1, d0165, d00804818, i1_sc_1_1,
d0100, i1_qi_19, d0100, i1_sc_2_1, d01409819, i1_bl_7_1, d01086082, d0050, 
i1_bpma, d01325, ciy_80_i1, d01175, i1_qi_20, d0135, cix_81_i1, d0165,
d01086082, i1_bl_7_1, d01409819, i1_sc_2_1, d0100, i1_qi_21, d0100, i1_sc_1_1, 
d00804818, d0050, d0100, d0100, i1_bpma, d0150, i1_bl_6_1, d02012268, 
i1_qih_22, i1_qih_22, d02012268, i1_bl_8_2, i1_cbl, d0135, cix_83_i1, d0165,
d00804818, i1_sc_1_2, d0100, i1_qi_21, d0100, i1_sc_2_2, d01409819, i1_bl_7_2, 
d01086082, d0050, i1_bpma, d01325, ciy_85_i1, d01175, i1_qi_24, d0135,
cix_86_i1, d0165, d01086082, i1_bl_7_2, d01409819, i1_sc_2_2, d0100, i1_qi_23,
d0100, i1_sc_1_2, d00804818, d0050, d0100, d0100, i1_bpma, d0150, 
i1_bl_8_2, d02012268, i1_qih_22, i1_qih_22, d02012268, i1_bl_8_2, i1_cbl, d0135, 
cix_88_i1, d0165, d00804818, i1_sc_1_2, d0100, i1_qi_23, d0100, i1_sc_2_2,
d01409819, i1_bl_7_2, d01086082, d0050, i1_bpma, d01325, cix_90_i1, d01175,
i1_qi_24, d0135, i1_cix_drift, d0165, d01086082, i1_bl_7_2, d01409819, i1_sc_2_2,
d0100, i1_qi_23, d0100, i1_sc_1_2, d00804818, d00175, ciy_92_i1, d01325,
i1_bpma, d0150, i1_bl_8_2, d02012268, i1_qi_25, i1_end_dog, d000013, d0900, 
i1_tora, d0200, ciy_94_i1, d0110, i1_qi_26, d01725, d01275, i1_bpmf,
d0096, i1_mpbpmf, d00315, d01725, cix_95_i1, d0110, i1_qi_27, d0200,
d0200, i1_start_mid, d0100, i1_bb_1_1, i1_vcst40t400y, d1000i, i1_vcst400y, i1_bb_1_2, 
i1_cbb_2, d03975, i1_colo, d0085, i1_colu, d03825, i1_bpms, d0310, 
i1_otrs, d0325, i1_bb_1_3, i1_cbb_3, i1_vcst400yt40, d0600, d1000im, i1_vcst40y, 
i1_bb_1_4, i1_cbb_4, d0100, i1_end_mid, d0200, d0100, d0110, i1_qi_28, 
d0110, cix_102_i1, d01225, d01275, i1_bpmf, d0096, i1_mpbpmf, d00315,
d01125, ciy_103_i1, d0110, i1_qi_29, d0200, i1_bpma, d0500, d0060,
cix_104_i1, d0110, i1_qi_30, i1_start_ps, d0200, i1_bpma, d1800, d0090,
ciy_107_i1, d0110, i1_qi_31, d0200, i1_bpma, d1800, d0090, cix_109_i1,
d0110, i1_qi_32, d0200, i1_bpma, d1800, d0090, ciy_112_i1, d0110,
i1_qi_31, d0200, i1_bpma, d0500, i1_vcdst, d0325, cix_114_i1, d0110,
i1_qi_33, d0200, i1_bpma, d03643, i1_tora, d09007, ciy_116_i1, d0110,
i1_qi_34, d01585, i1_bpma, d109132, i1_otra, d034903, i1_dcm, d009115, 
cix_118_i1, d0110, i1_qi_35, d01628, i1_bpma, d03522, i1_end_i1)

i1 = (gun_5MeV, i1_150M)