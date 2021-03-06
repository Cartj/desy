from ocelot import *
tws_L3 = Twiss()
tws_L3.beta_x = 16.219300000
tws_L3.beta_y = 21.076600
tws_L3.alpha_x = 0.394600
tws_L3.alpha_y = -0.603200
tws_L3.E = 2.400300000
tws_L3.s = 450.918702


l3_cfb = Drift(l = 3.35, eid= 'l3_cfb')
d0080 = Drift(l = 0.08, eid= 'd0080')
d01416 = Drift(l = 0.1416, eid= 'd01416')
d02043 = Drift(l = 0.2043, eid= 'd02043')
ltwakecav = Drift(l = 0.0, eid= 'ltwakecav')
l3_cx = Drift(l = 0, eid= 'l3_cx')
d0085 = Drift(l = 0.085, eid= 'd0085')
d00729 = Drift(l = 0.0729, eid= 'd00729')
d0300 = Drift(l = 0.3, eid= 'd0300')
l3_cy = Drift(l = 0, eid= 'l3_cy')
l3_csc = Drift(l = 2.9978, eid= 'l3_csc')
l3_ctb = Drift(l = 3.25, eid= 'l3_ctb')
d0100 = Drift(l = 0.1, eid= 'd0100')
d002575 = Drift(l = 0.02575, eid= 'd002575')
l3_vcdst = Drift(l = 1.215, eid= 'l3_vcdst')
d042845 = Drift(l = 0.20505, eid= 'd042845')
d02308 = Drift(l = 0.4542, eid= 'd02308')
d359096c = Drift(l = 15.772275, eid= 'd359096c')
d0200 = Drift(l = 0.2, eid= 'd0200')
d0400 = Drift(l = 0.4, eid= 'd0400')
d359096b = Drift(l = 17.537275, eid= 'd359096b')
d0050 = Drift(l = 0.05, eid= 'd0050')
d0075 = Drift(l = 0.075, eid= 'd0075')
d0030 = Drift(l = 0.03, eid= 'd0030')
l3_cex = Drift(l = 0.1, eid= 'l3_cex')
d359096a = Drift(l = 17.772275, eid= 'd359096a')
l3_cey = Drift(l = 0.1, eid= 'l3_cey')
d1277325 = Drift(l = 12.77325, eid= 'd1277325')
d5780 = Drift(l = 5.78, eid= 'd5780')
d5745 = Drift(l = 5.745, eid= 'd5745')
d0040 = Drift(l = 0.04, eid= 'd0040')
l3_cfx = Drift(l = 0.1, eid= 'l3_cfx')
d8215 = Drift(l = 8.215, eid= 'd8215')
l3_cfy = Drift(l = 0.1, eid= 'l3_cfy')
d11263 = Drift(l = 1.1263, eid= 'd11263')

# quadrupoles 
l3_q_a6_1 = Quadrupole(l = 0.3, k1 = -0.2715919, eid= 'l3_q_a6_1')
l3_q_a6_2 = Quadrupole(l = 0.3, k1 = 0.2909251, eid= 'l3_q_a6_2')
l3_q_a6_3 = Quadrupole(l = 0.3, k1 = -0.1010462, eid= 'l3_q_a6_3')
l3_q_a6_4 = Quadrupole(l = 0.3, k1 = -0.1674086, eid= 'l3_q_a6_4')
l3_q_a7_1 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a7_1')
l3_q_a7_2 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a7_2')
l3_q_a7_3 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a7_3')
l3_q_a7_4 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a7_4')
l3_q_a8_1 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a8_1')
l3_q_a8_2 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a8_2')
l3_q_a8_3 = Quadrupole(l = 0.3, k1 = 0.2258091, eid= 'l3_q_a8_3')
l3_q_a8_4 = Quadrupole(l = 0.3, k1 = -0.2094214, eid= 'l3_q_a8_4')
l3_q_a9_1 = Quadrupole(l = 0.3, k1 = 0.2067368, eid= 'l3_q_a9_1')
l3_q_a9_2 = Quadrupole(l = 0.3, k1 = -0.2181746, eid= 'l3_q_a9_2')
l3_q_a9_3 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a9_3')
l3_q_a9_4 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a9_4')
l3_q_a10_1 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a10_1')
l3_q_a10_2 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a10_2')
l3_q_a10_3 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a10_3')
l3_q_a10_4 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a10_4')
l3_q_a11_1 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a11_1')
l3_q_a11_2 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a11_2')
l3_q_a11_3 = Quadrupole(l = 0.3, k1 = 0.2258091, eid= 'l3_q_a11_3')
l3_q_a11_4 = Quadrupole(l = 0.3, k1 = -0.2094214, eid= 'l3_q_a11_4')
l3_q_a12_1 = Quadrupole(l = 0.3, k1 = 0.2067368, eid= 'l3_q_a12_1')
l3_q_a12_2 = Quadrupole(l = 0.3, k1 = -0.2181746, eid= 'l3_q_a12_2')
l3_q_a12_3 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a12_3')
l3_q_a12_4 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a12_4')
l3_q_a13_1 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a13_1')
l3_q_a13_2 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a13_2')
l3_q_a13_3 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a13_3')
l3_q_a13_4 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a13_4')
l3_q_a14_1 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a14_1')
l3_q_a14_2 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a14_2')
l3_q_a14_3 = Quadrupole(l = 0.3, k1 = 0.2258091, eid= 'l3_q_a14_3')
l3_q_a14_4 = Quadrupole(l = 0.3, k1 = -0.2094214, eid= 'l3_q_a14_4')
l3_q_a15_1 = Quadrupole(l = 0.3, k1 = 0.2067368, eid= 'l3_q_a15_1')
l3_q_a15_2 = Quadrupole(l = 0.3, k1 = -0.2181746, eid= 'l3_q_a15_2')
l3_q_a15_3 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a15_3')
l3_q_a15_4 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a15_4')
l3_q_a16_1 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a16_1')
l3_q_a16_2 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a16_2')
l3_q_a16_3 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a16_3')
l3_q_a16_4 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a16_4')
l3_q_a17_1 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a17_1')
l3_q_a17_2 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a17_2')
l3_q_a17_3 = Quadrupole(l = 0.3, k1 = 0.2258091, eid= 'l3_q_a17_3')
l3_q_a17_4 = Quadrupole(l = 0.3, k1 = -0.2094214, eid= 'l3_q_a17_4')
l3_q_a18_1 = Quadrupole(l = 0.3, k1 = 0.2067368, eid= 'l3_q_a18_1')
l3_q_a18_2 = Quadrupole(l = 0.3, k1 = -0.2181746, eid= 'l3_q_a18_2')
l3_q_a18_3 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a18_3')
l3_q_a18_4 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a18_4')
l3_q_a19_1 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a19_1')
l3_q_a19_2 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a19_2')
l3_q_a19_3 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a19_3')
l3_q_a19_4 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a19_4')
l3_q_a20_1 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a20_1')
l3_q_a20_2 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a20_2')
l3_q_a20_3 = Quadrupole(l = 0.3, k1 = 0.2258091, eid= 'l3_q_a20_3')
l3_q_a20_4 = Quadrupole(l = 0.3, k1 = -0.2094214, eid= 'l3_q_a20_4')
l3_q_a21_1 = Quadrupole(l = 0.3, k1 = 0.2067368, eid= 'l3_q_a21_1')
l3_q_a21_2 = Quadrupole(l = 0.3, k1 = -0.2181746, eid= 'l3_q_a21_2')
l3_q_a21_3 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a21_3')
l3_q_a21_4 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a21_4')
l3_q_a22_1 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a22_1')
l3_q_a22_2 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a22_2')
l3_q_a22_3 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a22_3')
l3_q_a22_4 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a22_4')
l3_q_a23_1 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a23_1')
l3_q_a23_2 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a23_2')
l3_q_a23_3 = Quadrupole(l = 0.3, k1 = 0.2258091, eid= 'l3_q_a23_3')
l3_q_a23_4 = Quadrupole(l = 0.3, k1 = -0.2094214, eid= 'l3_q_a23_4')
l3_q_a24_1 = Quadrupole(l = 0.3, k1 = 0.2067368, eid= 'l3_q_a24_1')
l3_q_a24_2 = Quadrupole(l = 0.3, k1 = -0.2181746, eid= 'l3_q_a24_2')
l3_q_a24_3 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a24_3')
l3_q_a24_4 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a24_4')
l3_q_a25_1 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a25_1')
l3_q_a25_2 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a25_2')
l3_q_a25_3 = Quadrupole(l = 0.3, k1 = 0.21458, eid= 'l3_q_a25_3')
l3_q_a25_4 = Quadrupole(l = 0.3, k1 = -0.21458, eid= 'l3_q_a25_4')
l3_q_a26_1 = Quadrupole(l = 0.3, k1 = 0.1040586, eid= 'l3_q_a26_1')
l3_q_a26_2 = Quadrupole(l = 0.3, k1 = -0.02918657, eid= 'l3_q_a26_2')
l3_q_a26_3 = Quadrupole(l = 0.3, k1 = 0.155385, eid= 'l3_q_a26_3')
l3_q_a26_4 = Quadrupole(l = 0.3, k1 = -0.1772898, eid= 'l3_q_a26_4')
l3_qe_1_1 = Quadrupole(l = 0.2, k1 = 0.1537098, eid= 'l3_qe_1_1')
l3_qe_1_2 = Quadrupole(l = 0.2, k1 = -0.1537098, eid= 'l3_qe_1_2')
l3_qe_2 = Quadrupole(l = 0.2, k1 = -0.01501576, eid= 'l3_qe_2')
l3_qf_1 = Quadrupole(l = 0.5, k1 = 1e-10, eid= 'l3_qf_1')
l3_qf_2 = Quadrupole(l = 0.5, k1 = -0.1259369, eid= 'l3_qf_2')

# bending magnets 

# correctors 

# markers 
l3_start_l3 = Marker(eid= 'l3_start_l3')
l3_vcst40t78 = Marker(eid= 'l3_vcst40t78')
l3_stac_a6_1 = Marker(eid= 'l3_stac_a6_1')
miac = Marker(eid= 'miac')
l3_enac_a6_1 = Marker(eid= 'l3_enac_a6_1')
l3_stac_a6_2 = Marker(eid= 'l3_stac_a6_2')
l3_enac_a6_2 = Marker(eid= 'l3_enac_a6_2')
l3_stac_a6_3 = Marker(eid= 'l3_stac_a6_3')
l3_enac_a6_3 = Marker(eid= 'l3_enac_a6_3')
l3_stac_a6_4 = Marker(eid= 'l3_stac_a6_4')
l3_enac_a6_4 = Marker(eid= 'l3_enac_a6_4')
l3_match = Marker(eid= 'l3_match')
l3_stac_a7_1 = Marker(eid= 'l3_stac_a7_1')
l3_enac_a7_1 = Marker(eid= 'l3_enac_a7_1')
l3_stac_a7_2 = Marker(eid= 'l3_stac_a7_2')
l3_enac_a7_2 = Marker(eid= 'l3_enac_a7_2')
l3_stac_a7_3 = Marker(eid= 'l3_stac_a7_3')
l3_enac_a7_3 = Marker(eid= 'l3_enac_a7_3')
l3_stac_a7_4 = Marker(eid= 'l3_stac_a7_4')
l3_enac_a7_4 = Marker(eid= 'l3_enac_a7_4')
l3_stac_a8_1 = Marker(eid= 'l3_stac_a8_1')
l3_enac_a8_1 = Marker(eid= 'l3_enac_a8_1')
l3_stac_a8_2 = Marker(eid= 'l3_stac_a8_2')
l3_enac_a8_2 = Marker(eid= 'l3_enac_a8_2')
l3_stac_a8_3 = Marker(eid= 'l3_stac_a8_3')
l3_enac_a8_3 = Marker(eid= 'l3_enac_a8_3')
l3_stac_a8_4 = Marker(eid= 'l3_stac_a8_4')
l3_enac_a8_4 = Marker(eid= 'l3_enac_a8_4')
l3_stac_a9_1 = Marker(eid= 'l3_stac_a9_1')
l3_enac_a9_1 = Marker(eid= 'l3_enac_a9_1')
l3_stac_a9_2 = Marker(eid= 'l3_stac_a9_2')
l3_enac_a9_2 = Marker(eid= 'l3_enac_a9_2')
l3_stac_a9_3 = Marker(eid= 'l3_stac_a9_3')
l3_enac_a9_3 = Marker(eid= 'l3_enac_a9_3')
l3_stac_a9_4 = Marker(eid= 'l3_stac_a9_4')
l3_enac_a9_4 = Marker(eid= 'l3_enac_a9_4')
l3_stac_a10_1 = Marker(eid= 'l3_stac_a10_1')
l3_enac_a10_1 = Marker(eid= 'l3_enac_a10_1')
l3_stac_a10_2 = Marker(eid= 'l3_stac_a10_2')
l3_enac_a10_2 = Marker(eid= 'l3_enac_a10_2')
l3_stac_a10_3 = Marker(eid= 'l3_stac_a10_3')
l3_enac_a10_3 = Marker(eid= 'l3_enac_a10_3')
l3_stac_a10_4 = Marker(eid= 'l3_stac_a10_4')
l3_enac_a10_4 = Marker(eid= 'l3_enac_a10_4')
l3_stac_a11_1 = Marker(eid= 'l3_stac_a11_1')
l3_enac_a11_1 = Marker(eid= 'l3_enac_a11_1')
l3_stac_a11_2 = Marker(eid= 'l3_stac_a11_2')
l3_enac_a11_2 = Marker(eid= 'l3_enac_a11_2')
l3_stac_a11_3 = Marker(eid= 'l3_stac_a11_3')
l3_enac_a11_3 = Marker(eid= 'l3_enac_a11_3')
l3_stac_a11_4 = Marker(eid= 'l3_stac_a11_4')
l3_enac_a11_4 = Marker(eid= 'l3_enac_a11_4')
l3_stac_a12_1 = Marker(eid= 'l3_stac_a12_1')
l3_enac_a12_1 = Marker(eid= 'l3_enac_a12_1')
l3_stac_a12_2 = Marker(eid= 'l3_stac_a12_2')
l3_enac_a12_2 = Marker(eid= 'l3_enac_a12_2')
l3_stac_a12_3 = Marker(eid= 'l3_stac_a12_3')
l3_enac_a12_3 = Marker(eid= 'l3_enac_a12_3')
l3_stac_a12_4 = Marker(eid= 'l3_stac_a12_4')
l3_enac_a12_4 = Marker(eid= 'l3_enac_a12_4')
l3_stac_a13_1 = Marker(eid= 'l3_stac_a13_1')
l3_enac_a13_1 = Marker(eid= 'l3_enac_a13_1')
l3_stac_a13_2 = Marker(eid= 'l3_stac_a13_2')
l3_enac_a13_2 = Marker(eid= 'l3_enac_a13_2')
l3_stac_a13_3 = Marker(eid= 'l3_stac_a13_3')
l3_enac_a13_3 = Marker(eid= 'l3_enac_a13_3')
l3_stac_a13_4 = Marker(eid= 'l3_stac_a13_4')
l3_enac_a13_4 = Marker(eid= 'l3_enac_a13_4')
l3_stac_a14_1 = Marker(eid= 'l3_stac_a14_1')
l3_enac_a14_1 = Marker(eid= 'l3_enac_a14_1')
l3_stac_a14_2 = Marker(eid= 'l3_stac_a14_2')
l3_enac_a14_2 = Marker(eid= 'l3_enac_a14_2')
l3_stac_a14_3 = Marker(eid= 'l3_stac_a14_3')
l3_enac_a14_3 = Marker(eid= 'l3_enac_a14_3')
l3_stac_a14_4 = Marker(eid= 'l3_stac_a14_4')
l3_enac_a14_4 = Marker(eid= 'l3_enac_a14_4')
l3_stac_a15_1 = Marker(eid= 'l3_stac_a15_1')
l3_enac_a15_1 = Marker(eid= 'l3_enac_a15_1')
l3_stac_a15_2 = Marker(eid= 'l3_stac_a15_2')
l3_enac_a15_2 = Marker(eid= 'l3_enac_a15_2')
l3_stac_a15_3 = Marker(eid= 'l3_stac_a15_3')
l3_enac_a15_3 = Marker(eid= 'l3_enac_a15_3')
l3_stac_a15_4 = Marker(eid= 'l3_stac_a15_4')
l3_enac_a15_4 = Marker(eid= 'l3_enac_a15_4')
l3_stac_a16_1 = Marker(eid= 'l3_stac_a16_1')
l3_enac_a16_1 = Marker(eid= 'l3_enac_a16_1')
l3_stac_a16_2 = Marker(eid= 'l3_stac_a16_2')
l3_enac_a16_2 = Marker(eid= 'l3_enac_a16_2')
l3_stac_a16_3 = Marker(eid= 'l3_stac_a16_3')
l3_enac_a16_3 = Marker(eid= 'l3_enac_a16_3')
l3_stac_a16_4 = Marker(eid= 'l3_stac_a16_4')
l3_enac_a16_4 = Marker(eid= 'l3_enac_a16_4')
l3_stac_a17_1 = Marker(eid= 'l3_stac_a17_1')
l3_enac_a17_1 = Marker(eid= 'l3_enac_a17_1')
l3_stac_a17_2 = Marker(eid= 'l3_stac_a17_2')
l3_enac_a17_2 = Marker(eid= 'l3_enac_a17_2')
l3_stac_a17_3 = Marker(eid= 'l3_stac_a17_3')
l3_enac_a17_3 = Marker(eid= 'l3_enac_a17_3')
l3_stac_a17_4 = Marker(eid= 'l3_stac_a17_4')
l3_enac_a17_4 = Marker(eid= 'l3_enac_a17_4')
l3_stac_a18_1 = Marker(eid= 'l3_stac_a18_1')
l3_enac_a18_1 = Marker(eid= 'l3_enac_a18_1')
l3_stac_a18_2 = Marker(eid= 'l3_stac_a18_2')
l3_enac_a18_2 = Marker(eid= 'l3_enac_a18_2')
l3_stac_a18_3 = Marker(eid= 'l3_stac_a18_3')
l3_enac_a18_3 = Marker(eid= 'l3_enac_a18_3')
l3_stac_a18_4 = Marker(eid= 'l3_stac_a18_4')
l3_enac_a18_4 = Marker(eid= 'l3_enac_a18_4')
l3_stac_a19_1 = Marker(eid= 'l3_stac_a19_1')
l3_enac_a19_1 = Marker(eid= 'l3_enac_a19_1')
l3_stac_a19_2 = Marker(eid= 'l3_stac_a19_2')
l3_enac_a19_2 = Marker(eid= 'l3_enac_a19_2')
l3_stac_a19_3 = Marker(eid= 'l3_stac_a19_3')
l3_enac_a19_3 = Marker(eid= 'l3_enac_a19_3')
l3_stac_a19_4 = Marker(eid= 'l3_stac_a19_4')
l3_enac_a19_4 = Marker(eid= 'l3_enac_a19_4')
l3_stac_a20_1 = Marker(eid= 'l3_stac_a20_1')
l3_enac_a20_1 = Marker(eid= 'l3_enac_a20_1')
l3_stac_a20_2 = Marker(eid= 'l3_stac_a20_2')
l3_enac_a20_2 = Marker(eid= 'l3_enac_a20_2')
l3_stac_a20_3 = Marker(eid= 'l3_stac_a20_3')
l3_enac_a20_3 = Marker(eid= 'l3_enac_a20_3')
l3_stac_a20_4 = Marker(eid= 'l3_stac_a20_4')
l3_enac_a20_4 = Marker(eid= 'l3_enac_a20_4')
l3_stac_a21_1 = Marker(eid= 'l3_stac_a21_1')
l3_enac_a21_1 = Marker(eid= 'l3_enac_a21_1')
l3_stac_a21_2 = Marker(eid= 'l3_stac_a21_2')
l3_enac_a21_2 = Marker(eid= 'l3_enac_a21_2')
l3_stac_a21_3 = Marker(eid= 'l3_stac_a21_3')
l3_enac_a21_3 = Marker(eid= 'l3_enac_a21_3')
l3_stac_a21_4 = Marker(eid= 'l3_stac_a21_4')
l3_enac_a21_4 = Marker(eid= 'l3_enac_a21_4')
l3_stac_a22_1 = Marker(eid= 'l3_stac_a22_1')
l3_enac_a22_1 = Marker(eid= 'l3_enac_a22_1')
l3_stac_a22_2 = Marker(eid= 'l3_stac_a22_2')
l3_enac_a22_2 = Marker(eid= 'l3_enac_a22_2')
l3_stac_a22_3 = Marker(eid= 'l3_stac_a22_3')
l3_enac_a22_3 = Marker(eid= 'l3_enac_a22_3')
l3_stac_a22_4 = Marker(eid= 'l3_stac_a22_4')
l3_enac_a22_4 = Marker(eid= 'l3_enac_a22_4')
l3_stac_a23_1 = Marker(eid= 'l3_stac_a23_1')
l3_enac_a23_1 = Marker(eid= 'l3_enac_a23_1')
l3_stac_a23_2 = Marker(eid= 'l3_stac_a23_2')
l3_enac_a23_2 = Marker(eid= 'l3_enac_a23_2')
l3_stac_a23_3 = Marker(eid= 'l3_stac_a23_3')
l3_enac_a23_3 = Marker(eid= 'l3_enac_a23_3')
l3_stac_a23_4 = Marker(eid= 'l3_stac_a23_4')
l3_enac_a23_4 = Marker(eid= 'l3_enac_a23_4')
l3_stac_a24_1 = Marker(eid= 'l3_stac_a24_1')
l3_enac_a24_1 = Marker(eid= 'l3_enac_a24_1')
l3_stac_a24_2 = Marker(eid= 'l3_stac_a24_2')
l3_enac_a24_2 = Marker(eid= 'l3_enac_a24_2')
l3_stac_a24_3 = Marker(eid= 'l3_stac_a24_3')
l3_enac_a24_3 = Marker(eid= 'l3_enac_a24_3')
l3_stac_a24_4 = Marker(eid= 'l3_stac_a24_4')
l3_enac_a24_4 = Marker(eid= 'l3_enac_a24_4')
l3_stac_a25_1 = Marker(eid= 'l3_stac_a25_1')
l3_enac_a25_1 = Marker(eid= 'l3_enac_a25_1')
l3_stac_a25_2 = Marker(eid= 'l3_stac_a25_2')
l3_enac_a25_2 = Marker(eid= 'l3_enac_a25_2')
l3_stac_a25_3 = Marker(eid= 'l3_stac_a25_3')
l3_enac_a25_3 = Marker(eid= 'l3_enac_a25_3')
l3_stac_a25_4 = Marker(eid= 'l3_stac_a25_4')
l3_enac_a25_4 = Marker(eid= 'l3_enac_a25_4')
l3_stac_a26_1 = Marker(eid= 'l3_stac_a26_1')
l3_enac_a26_1 = Marker(eid= 'l3_enac_a26_1')
l3_stac_a26_2 = Marker(eid= 'l3_stac_a26_2')
l3_enac_a26_2 = Marker(eid= 'l3_enac_a26_2')
l3_stac_a26_3 = Marker(eid= 'l3_stac_a26_3')
l3_enac_a26_3 = Marker(eid= 'l3_enac_a26_3')
l3_stac_a26_4 = Marker(eid= 'l3_stac_a26_4')
l3_enac_a26_4 = Marker(eid= 'l3_enac_a26_4')
l3_vcst78t40 = Marker(eid= 'l3_vcst78t40')
l3_tora = Marker(eid= 'l3_tora')
l3_otrbw = Marker(eid= 'l3_otrbw')
l3_end_l3 = Marker(eid= 'l3_end_l3')

# monitor 
l3_bpmc = Monitor(eid= 'l3_bpmc')
l3_bpmr = Monitor(eid= 'l3_bpmr')
l3_bpma = Monitor(eid= 'l3_bpma')

# sextupoles 

# octupole 

# undulator 

# cavity 
l3_c_a6 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a6')
l3_c_a7 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a7')
l3_c_a8 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a8')
l3_c_a9 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a9')
l3_c_a10 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a10')
l3_c_a11 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a11')
l3_c_a12 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a12')
l3_c_a13 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a13')
l3_c_a14 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a14')
l3_c_a15 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a15')
l3_c_a16 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a16')
l3_c_a17 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a17')
l3_c_a18 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a18')
l3_c_a19 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a19')
l3_c_a20 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a20')
l3_c_a21 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a21')
l3_c_a22 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a22')
l3_c_a23 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a23')
l3_c_a24 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a24')
l3_c_a25 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a25')
l3_c_a26 = Cavity(l = 1.0377, v = 0.02265625, delta_e = 0.02265625, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l3_c_a26')

# rfcavity 

# Matrices 

# Solenoids 

# lattice 
L3 = (l3_start_l3, l3_vcst40t78, l3_cfb, l3_stac_a6_1, d0080, d01416, l3_c_a6,
d02043, ltwakecav, d01416, l3_c_a6, d02043, ltwakecav, d01416, l3_c_a6, 
d02043, ltwakecav, d01416, l3_c_a6, d02043, ltwakecav, miac, d01416, 
l3_c_a6, d02043, ltwakecav, d01416, l3_c_a6, d02043, ltwakecav, d01416, 
l3_c_a6, d02043, ltwakecav, d01416, l3_c_a6, d02043, ltwakecav, l3_q_a6_1, 
l3_cx, d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a6_1, l3_stac_a6_2, 
d0080, d01416, l3_c_a6, d02043, ltwakecav, d01416, l3_c_a6, d02043, 
ltwakecav, d01416, l3_c_a6, d02043, ltwakecav, d01416, l3_c_a6, d02043, 
ltwakecav, miac, d01416, l3_c_a6, d02043, ltwakecav, d01416, l3_c_a6, 
d02043, ltwakecav, d01416, l3_c_a6, d02043, ltwakecav, d01416, l3_c_a6, 
d02043, ltwakecav, l3_q_a6_2, l3_cy, d0085, l3_bpmc, d0085, d00729, 
d0300, l3_enac_a6_2, l3_stac_a6_3, d0080, d01416, l3_c_a6, d02043, ltwakecav, 
d01416, l3_c_a6, d02043, ltwakecav, d01416, l3_c_a6, d02043, ltwakecav, 
d01416, l3_c_a6, d02043, ltwakecav, miac, d01416, l3_c_a6, d02043, 
ltwakecav, d01416, l3_c_a6, d02043, ltwakecav, d01416, l3_c_a6, d02043, 
ltwakecav, d01416, l3_c_a6, d02043, ltwakecav, l3_q_a6_3, l3_cx, d0085, 
l3_bpmc, d0085, d00729, d0300, l3_enac_a6_3, l3_stac_a6_4, d0080, d01416, 
l3_c_a6, d02043, ltwakecav, d01416, l3_c_a6, d02043, ltwakecav, d01416, 
l3_c_a6, d02043, ltwakecav, d01416, l3_c_a6, d02043, ltwakecav, miac, 
d01416, l3_c_a6, d02043, ltwakecav, d01416, l3_c_a6, d02043, ltwakecav, 
d01416, l3_c_a6, d02043, ltwakecav, d01416, l3_c_a6, d02043, ltwakecav, 
l3_q_a6_4, l3_cy, d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a6_4, 
l3_match, l3_stac_a7_1, d0080, d01416, l3_c_a7, d02043, ltwakecav, d01416, 
l3_c_a7, d02043, ltwakecav, d01416, l3_c_a7, d02043, ltwakecav, d01416, 
l3_c_a7, d02043, ltwakecav, miac, d01416, l3_c_a7, d02043, ltwakecav, 
d01416, l3_c_a7, d02043, ltwakecav, d01416, l3_c_a7, d02043, ltwakecav, 
d01416, l3_c_a7, d02043, ltwakecav, l3_q_a7_1, l3_cx, d0085, l3_bpmc, 
d0085, d00729, d0300, l3_enac_a7_1, l3_stac_a7_2, d0080, d01416, l3_c_a7, 
d02043, ltwakecav, d01416, l3_c_a7, d02043, ltwakecav, d01416, l3_c_a7, 
d02043, ltwakecav, d01416, l3_c_a7, d02043, ltwakecav, miac, d01416, 
l3_c_a7, d02043, ltwakecav, d01416, l3_c_a7, d02043, ltwakecav, d01416, 
l3_c_a7, d02043, ltwakecav, d01416, l3_c_a7, d02043, ltwakecav, l3_q_a7_2, 
l3_cy, d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a7_2, l3_stac_a7_3, 
d0080, d01416, l3_c_a7, d02043, ltwakecav, d01416, l3_c_a7, d02043, 
ltwakecav, d01416, l3_c_a7, d02043, ltwakecav, d01416, l3_c_a7, d02043, 
ltwakecav, miac, d01416, l3_c_a7, d02043, ltwakecav, d01416, l3_c_a7, 
d02043, ltwakecav, d01416, l3_c_a7, d02043, ltwakecav, d01416, l3_c_a7, 
d02043, ltwakecav, l3_q_a7_3, l3_cx, d0085, l3_bpmc, d0085, d00729, 
d0300, l3_enac_a7_3, l3_stac_a7_4, d0080, d01416, l3_c_a7, d02043, ltwakecav, 
d01416, l3_c_a7, d02043, ltwakecav, d01416, l3_c_a7, d02043, ltwakecav, 
d01416, l3_c_a7, d02043, ltwakecav, miac, d01416, l3_c_a7, d02043, 
ltwakecav, d01416, l3_c_a7, d02043, ltwakecav, d01416, l3_c_a7, d02043, 
ltwakecav, d01416, l3_c_a7, d02043, ltwakecav, l3_q_a7_4, l3_cy, d0085, 
l3_bpmr, d0085, d00729, d0300, l3_enac_a7_4, l3_stac_a8_1, d0080, d01416, 
l3_c_a8, d02043, ltwakecav, d01416, l3_c_a8, d02043, ltwakecav, d01416, 
l3_c_a8, d02043, ltwakecav, d01416, l3_c_a8, d02043, ltwakecav, miac, 
d01416, l3_c_a8, d02043, ltwakecav, d01416, l3_c_a8, d02043, ltwakecav, 
d01416, l3_c_a8, d02043, ltwakecav, d01416, l3_c_a8, d02043, ltwakecav, 
l3_q_a8_1, l3_cx, d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a8_1, 
l3_stac_a8_2, d0080, d01416, l3_c_a8, d02043, ltwakecav, d01416, l3_c_a8, 
d02043, ltwakecav, d01416, l3_c_a8, d02043, ltwakecav, d01416, l3_c_a8, 
d02043, ltwakecav, miac, d01416, l3_c_a8, d02043, ltwakecav, d01416, 
l3_c_a8, d02043, ltwakecav, d01416, l3_c_a8, d02043, ltwakecav, d01416, 
l3_c_a8, d02043, ltwakecav, l3_q_a8_2, l3_cy, d0085, l3_bpmc, d0085, 
d00729, d0300, l3_enac_a8_2, l3_stac_a8_3, d0080, d01416, l3_c_a8, d02043, 
ltwakecav, d01416, l3_c_a8, d02043, ltwakecav, d01416, l3_c_a8, d02043, 
ltwakecav, d01416, l3_c_a8, d02043, ltwakecav, miac, d01416, l3_c_a8, 
d02043, ltwakecav, d01416, l3_c_a8, d02043, ltwakecav, d01416, l3_c_a8, 
d02043, ltwakecav, d01416, l3_c_a8, d02043, ltwakecav, l3_q_a8_3, l3_cx, 
d0085, l3_bpmr, d0085, d00729, d0300, l3_enac_a8_3, l3_stac_a8_4, d0080, 
d01416, l3_c_a8, d02043, ltwakecav, d01416, l3_c_a8, d02043, ltwakecav, 
d01416, l3_c_a8, d02043, ltwakecav, d01416, l3_c_a8, d02043, ltwakecav, 
miac, d01416, l3_c_a8, d02043, ltwakecav, d01416, l3_c_a8, d02043, 
ltwakecav, d01416, l3_c_a8, d02043, ltwakecav, d01416, l3_c_a8, d02043, 
ltwakecav, l3_q_a8_4, l3_cy, d0085, l3_bpmr, d0085, d00729, d0300, 
l3_enac_a8_4, l3_csc, l3_stac_a9_1, d0080, d01416, l3_c_a9, d02043, ltwakecav, 
d01416, l3_c_a9, d02043, ltwakecav, d01416, l3_c_a9, d02043, ltwakecav, 
d01416, l3_c_a9, d02043, ltwakecav, miac, d01416, l3_c_a9, d02043, 
ltwakecav, d01416, l3_c_a9, d02043, ltwakecav, d01416, l3_c_a9, d02043, 
ltwakecav, d01416, l3_c_a9, d02043, ltwakecav, l3_q_a9_1, l3_cx, d0085, 
l3_bpmr, d0085, d00729, d0300, l3_enac_a9_1, l3_stac_a9_2, d0080, d01416, 
l3_c_a9, d02043, ltwakecav, d01416, l3_c_a9, d02043, ltwakecav, d01416, 
l3_c_a9, d02043, ltwakecav, d01416, l3_c_a9, d02043, ltwakecav, miac, 
d01416, l3_c_a9, d02043, ltwakecav, d01416, l3_c_a9, d02043, ltwakecav, 
d01416, l3_c_a9, d02043, ltwakecav, d01416, l3_c_a9, d02043, ltwakecav, 
l3_q_a9_2, l3_cy, d0085, l3_bpmr, d0085, d00729, d0300, l3_enac_a9_2, 
l3_stac_a9_3, d0080, d01416, l3_c_a9, d02043, ltwakecav, d01416, l3_c_a9, 
d02043, ltwakecav, d01416, l3_c_a9, d02043, ltwakecav, d01416, l3_c_a9, 
d02043, ltwakecav, miac, d01416, l3_c_a9, d02043, ltwakecav, d01416, 
l3_c_a9, d02043, ltwakecav, d01416, l3_c_a9, d02043, ltwakecav, d01416, 
l3_c_a9, d02043, ltwakecav, l3_q_a9_3, l3_cx, d0085, l3_bpmc, d0085, 
d00729, d0300, l3_enac_a9_3, l3_stac_a9_4, d0080, d01416, l3_c_a9, d02043, 
ltwakecav, d01416, l3_c_a9, d02043, ltwakecav, d01416, l3_c_a9, d02043, 
ltwakecav, d01416, l3_c_a9, d02043, ltwakecav, miac, d01416, l3_c_a9, 
d02043, ltwakecav, d01416, l3_c_a9, d02043, ltwakecav, d01416, l3_c_a9, 
d02043, ltwakecav, d01416, l3_c_a9, d02043, ltwakecav, l3_q_a9_4, l3_cy, 
d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a9_4, l3_stac_a10_1, d0080, 
d01416, l3_c_a10, d02043, ltwakecav, d01416, l3_c_a10, d02043, ltwakecav, 
d01416, l3_c_a10, d02043, ltwakecav, d01416, l3_c_a10, d02043, ltwakecav, 
miac, d01416, l3_c_a10, d02043, ltwakecav, d01416, l3_c_a10, d02043, 
ltwakecav, d01416, l3_c_a10, d02043, ltwakecav, d01416, l3_c_a10, d02043, 
ltwakecav, l3_q_a10_1, l3_cx, d0085, l3_bpmc, d0085, d00729, d0300, 
l3_enac_a10_1, l3_stac_a10_2, d0080, d01416, l3_c_a10, d02043, ltwakecav, d01416, 
l3_c_a10, d02043, ltwakecav, d01416, l3_c_a10, d02043, ltwakecav, d01416, 
l3_c_a10, d02043, ltwakecav, miac, d01416, l3_c_a10, d02043, ltwakecav, 
d01416, l3_c_a10, d02043, ltwakecav, d01416, l3_c_a10, d02043, ltwakecav, 
d01416, l3_c_a10, d02043, ltwakecav, l3_q_a10_2, l3_cy, d0085, l3_bpmc, 
d0085, d00729, d0300, l3_enac_a10_2, l3_stac_a10_3, d0080, d01416, l3_c_a10, 
d02043, ltwakecav, d01416, l3_c_a10, d02043, ltwakecav, d01416, l3_c_a10, 
d02043, ltwakecav, d01416, l3_c_a10, d02043, ltwakecav, miac, d01416, 
l3_c_a10, d02043, ltwakecav, d01416, l3_c_a10, d02043, ltwakecav, d01416, 
l3_c_a10, d02043, ltwakecav, d01416, l3_c_a10, d02043, ltwakecav, l3_q_a10_3, 
l3_cx, d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a10_3, l3_stac_a10_4, 
d0080, d01416, l3_c_a10, d02043, ltwakecav, d01416, l3_c_a10, d02043, 
ltwakecav, d01416, l3_c_a10, d02043, ltwakecav, d01416, l3_c_a10, d02043, 
ltwakecav, miac, d01416, l3_c_a10, d02043, ltwakecav, d01416, l3_c_a10, 
d02043, ltwakecav, d01416, l3_c_a10, d02043, ltwakecav, d01416, l3_c_a10, 
d02043, ltwakecav, l3_q_a10_4, l3_cy, d0085, l3_bpmc, d0085, d00729, 
d0300, l3_enac_a10_4, l3_stac_a11_1, d0080, d01416, l3_c_a11, d02043, ltwakecav, 
d01416, l3_c_a11, d02043, ltwakecav, d01416, l3_c_a11, d02043, ltwakecav, 
d01416, l3_c_a11, d02043, ltwakecav, miac, d01416, l3_c_a11, d02043, 
ltwakecav, d01416, l3_c_a11, d02043, ltwakecav, d01416, l3_c_a11, d02043, 
ltwakecav, d01416, l3_c_a11, d02043, ltwakecav, l3_q_a11_1, l3_cx, d0085, 
l3_bpmc, d0085, d00729, d0300, l3_enac_a11_1, l3_stac_a11_2, d0080, d01416, 
l3_c_a11, d02043, ltwakecav, d01416, l3_c_a11, d02043, ltwakecav, d01416, 
l3_c_a11, d02043, ltwakecav, d01416, l3_c_a11, d02043, ltwakecav, miac, 
d01416, l3_c_a11, d02043, ltwakecav, d01416, l3_c_a11, d02043, ltwakecav, 
d01416, l3_c_a11, d02043, ltwakecav, d01416, l3_c_a11, d02043, ltwakecav, 
l3_q_a11_2, l3_cy, d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a11_2, 
l3_stac_a11_3, d0080, d01416, l3_c_a11, d02043, ltwakecav, d01416, l3_c_a11, 
d02043, ltwakecav, d01416, l3_c_a11, d02043, ltwakecav, d01416, l3_c_a11, 
d02043, ltwakecav, miac, d01416, l3_c_a11, d02043, ltwakecav, d01416, 
l3_c_a11, d02043, ltwakecav, d01416, l3_c_a11, d02043, ltwakecav, d01416, 
l3_c_a11, d02043, ltwakecav, l3_q_a11_3, l3_cx, d0085, l3_bpmr, d0085, 
d00729, d0300, l3_enac_a11_3, l3_stac_a11_4, d0080, d01416, l3_c_a11, d02043, 
ltwakecav, d01416, l3_c_a11, d02043, ltwakecav, d01416, l3_c_a11, d02043, 
ltwakecav, d01416, l3_c_a11, d02043, ltwakecav, miac, d01416, l3_c_a11, 
d02043, ltwakecav, d01416, l3_c_a11, d02043, ltwakecav, d01416, l3_c_a11, 
d02043, ltwakecav, d01416, l3_c_a11, d02043, ltwakecav, l3_q_a11_4, l3_cy, 
d0085, l3_bpmr, d0085, d00729, d0300, l3_enac_a11_4, l3_csc, l3_stac_a12_1, 
d0080, d01416, l3_c_a12, d02043, ltwakecav, d01416, l3_c_a12, d02043, 
ltwakecav, d01416, l3_c_a12, d02043, ltwakecav, d01416, l3_c_a12, d02043, 
ltwakecav, miac, d01416, l3_c_a12, d02043, ltwakecav, d01416, l3_c_a12, 
d02043, ltwakecav, d01416, l3_c_a12, d02043, ltwakecav, d01416, l3_c_a12, 
d02043, ltwakecav, l3_q_a12_1, l3_cx, d0085, l3_bpmr, d0085, d00729, 
d0300, l3_enac_a12_1, l3_stac_a12_2, d0080, d01416, l3_c_a12, d02043, ltwakecav, 
d01416, l3_c_a12, d02043, ltwakecav, d01416, l3_c_a12, d02043, ltwakecav, 
d01416, l3_c_a12, d02043, ltwakecav, miac, d01416, l3_c_a12, d02043, 
ltwakecav, d01416, l3_c_a12, d02043, ltwakecav, d01416, l3_c_a12, d02043, 
ltwakecav, d01416, l3_c_a12, d02043, ltwakecav, l3_q_a12_2, l3_cy, d0085, 
l3_bpmr, d0085, d00729, d0300, l3_enac_a12_2, l3_stac_a12_3, d0080, d01416, 
l3_c_a12, d02043, ltwakecav, d01416, l3_c_a12, d02043, ltwakecav, d01416, 
l3_c_a12, d02043, ltwakecav, d01416, l3_c_a12, d02043, ltwakecav, miac, 
d01416, l3_c_a12, d02043, ltwakecav, d01416, l3_c_a12, d02043, ltwakecav, 
d01416, l3_c_a12, d02043, ltwakecav, d01416, l3_c_a12, d02043, ltwakecav, 
l3_q_a12_3, l3_cx, d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a12_3, 
l3_stac_a12_4, d0080, d01416, l3_c_a12, d02043, ltwakecav, d01416, l3_c_a12, 
d02043, ltwakecav, d01416, l3_c_a12, d02043, ltwakecav, d01416, l3_c_a12, 
d02043, ltwakecav, miac, d01416, l3_c_a12, d02043, ltwakecav, d01416, 
l3_c_a12, d02043, ltwakecav, d01416, l3_c_a12, d02043, ltwakecav, d01416, 
l3_c_a12, d02043, ltwakecav, l3_q_a12_4, l3_cy, d0085, l3_bpmc, d0085, 
d00729, d0300, l3_enac_a12_4, l3_stac_a13_1, d0080, d01416, l3_c_a13, d02043, 
ltwakecav, d01416, l3_c_a13, d02043, ltwakecav, d01416, l3_c_a13, d02043, 
ltwakecav, d01416, l3_c_a13, d02043, ltwakecav, miac, d01416, l3_c_a13, 
d02043, ltwakecav, d01416, l3_c_a13, d02043, ltwakecav, d01416, l3_c_a13, 
d02043, ltwakecav, d01416, l3_c_a13, d02043, ltwakecav, l3_q_a13_1, l3_cx, 
d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a13_1, l3_stac_a13_2, d0080, 
d01416, l3_c_a13, d02043, ltwakecav, d01416, l3_c_a13, d02043, ltwakecav, 
d01416, l3_c_a13, d02043, ltwakecav, d01416, l3_c_a13, d02043, ltwakecav, 
miac, d01416, l3_c_a13, d02043, ltwakecav, d01416, l3_c_a13, d02043, 
ltwakecav, d01416, l3_c_a13, d02043, ltwakecav, d01416, l3_c_a13, d02043, 
ltwakecav, l3_q_a13_2, l3_cy, d0085, l3_bpmc, d0085, d00729, d0300, 
l3_enac_a13_2, l3_stac_a13_3, d0080, d01416, l3_c_a13, d02043, ltwakecav, d01416, 
l3_c_a13, d02043, ltwakecav, d01416, l3_c_a13, d02043, ltwakecav, d01416, 
l3_c_a13, d02043, ltwakecav, miac, d01416, l3_c_a13, d02043, ltwakecav, 
d01416, l3_c_a13, d02043, ltwakecav, d01416, l3_c_a13, d02043, ltwakecav, 
d01416, l3_c_a13, d02043, ltwakecav, l3_q_a13_3, l3_cx, d0085, l3_bpmc, 
d0085, d00729, d0300, l3_enac_a13_3, l3_stac_a13_4, d0080, d01416, l3_c_a13, 
d02043, ltwakecav, d01416, l3_c_a13, d02043, ltwakecav, d01416, l3_c_a13, 
d02043, ltwakecav, d01416, l3_c_a13, d02043, ltwakecav, miac, d01416, 
l3_c_a13, d02043, ltwakecav, d01416, l3_c_a13, d02043, ltwakecav, d01416, 
l3_c_a13, d02043, ltwakecav, d01416, l3_c_a13, d02043, ltwakecav, l3_q_a13_4, 
l3_cy, d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a13_4, l3_stac_a14_1, 
d0080, d01416, l3_c_a14, d02043, ltwakecav, d01416, l3_c_a14, d02043, 
ltwakecav, d01416, l3_c_a14, d02043, ltwakecav, d01416, l3_c_a14, d02043, 
ltwakecav, miac, d01416, l3_c_a14, d02043, ltwakecav, d01416, l3_c_a14, 
d02043, ltwakecav, d01416, l3_c_a14, d02043, ltwakecav, d01416, l3_c_a14, 
d02043, ltwakecav, l3_q_a14_1, l3_cx, d0085, l3_bpmc, d0085, d00729, 
d0300, l3_enac_a14_1, l3_stac_a14_2, d0080, d01416, l3_c_a14, d02043, ltwakecav, 
d01416, l3_c_a14, d02043, ltwakecav, d01416, l3_c_a14, d02043, ltwakecav, 
d01416, l3_c_a14, d02043, ltwakecav, miac, d01416, l3_c_a14, d02043, 
ltwakecav, d01416, l3_c_a14, d02043, ltwakecav, d01416, l3_c_a14, d02043, 
ltwakecav, d01416, l3_c_a14, d02043, ltwakecav, l3_q_a14_2, l3_cy, d0085, 
l3_bpmc, d0085, d00729, d0300, l3_enac_a14_2, l3_stac_a14_3, d0080, d01416, 
l3_c_a14, d02043, ltwakecav, d01416, l3_c_a14, d02043, ltwakecav, d01416, 
l3_c_a14, d02043, ltwakecav, d01416, l3_c_a14, d02043, ltwakecav, miac, 
d01416, l3_c_a14, d02043, ltwakecav, d01416, l3_c_a14, d02043, ltwakecav, 
d01416, l3_c_a14, d02043, ltwakecav, d01416, l3_c_a14, d02043, ltwakecav, 
l3_q_a14_3, l3_cx, d0085, l3_bpmr, d0085, d00729, d0300, l3_enac_a14_3, 
l3_stac_a14_4, d0080, d01416, l3_c_a14, d02043, ltwakecav, d01416, l3_c_a14, 
d02043, ltwakecav, d01416, l3_c_a14, d02043, ltwakecav, d01416, l3_c_a14, 
d02043, ltwakecav, miac, d01416, l3_c_a14, d02043, ltwakecav, d01416, 
l3_c_a14, d02043, ltwakecav, d01416, l3_c_a14, d02043, ltwakecav, d01416, 
l3_c_a14, d02043, ltwakecav, l3_q_a14_4, l3_cy, d0085, l3_bpmr, d0085, 
d00729, d0300, l3_enac_a14_4, l3_csc, l3_stac_a15_1, d0080, d01416, l3_c_a15, 
d02043, ltwakecav, d01416, l3_c_a15, d02043, ltwakecav, d01416, l3_c_a15, 
d02043, ltwakecav, d01416, l3_c_a15, d02043, ltwakecav, miac, d01416, 
l3_c_a15, d02043, ltwakecav, d01416, l3_c_a15, d02043, ltwakecav, d01416, 
l3_c_a15, d02043, ltwakecav, d01416, l3_c_a15, d02043, ltwakecav, l3_q_a15_1, 
l3_cx, d0085, l3_bpmr, d0085, d00729, d0300, l3_enac_a15_1, l3_stac_a15_2, 
d0080, d01416, l3_c_a15, d02043, ltwakecav, d01416, l3_c_a15, d02043, 
ltwakecav, d01416, l3_c_a15, d02043, ltwakecav, d01416, l3_c_a15, d02043, 
ltwakecav, miac, d01416, l3_c_a15, d02043, ltwakecav, d01416, l3_c_a15, 
d02043, ltwakecav, d01416, l3_c_a15, d02043, ltwakecav, d01416, l3_c_a15, 
d02043, ltwakecav, l3_q_a15_2, l3_cy, d0085, l3_bpmr, d0085, d00729, 
d0300, l3_enac_a15_2, l3_stac_a15_3, d0080, d01416, l3_c_a15, d02043, ltwakecav, 
d01416, l3_c_a15, d02043, ltwakecav, d01416, l3_c_a15, d02043, ltwakecav, 
d01416, l3_c_a15, d02043, ltwakecav, miac, d01416, l3_c_a15, d02043, 
ltwakecav, d01416, l3_c_a15, d02043, ltwakecav, d01416, l3_c_a15, d02043, 
ltwakecav, d01416, l3_c_a15, d02043, ltwakecav, l3_q_a15_3, l3_cx, d0085, 
l3_bpmc, d0085, d00729, d0300, l3_enac_a15_3, l3_stac_a15_4, d0080, d01416, 
l3_c_a15, d02043, ltwakecav, d01416, l3_c_a15, d02043, ltwakecav, d01416, 
l3_c_a15, d02043, ltwakecav, d01416, l3_c_a15, d02043, ltwakecav, miac, 
d01416, l3_c_a15, d02043, ltwakecav, d01416, l3_c_a15, d02043, ltwakecav, 
d01416, l3_c_a15, d02043, ltwakecav, d01416, l3_c_a15, d02043, ltwakecav, 
l3_q_a15_4, l3_cy, d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a15_4, 
l3_stac_a16_1, d0080, d01416, l3_c_a16, d02043, ltwakecav, d01416, l3_c_a16, 
d02043, ltwakecav, d01416, l3_c_a16, d02043, ltwakecav, d01416, l3_c_a16, 
d02043, ltwakecav, miac, d01416, l3_c_a16, d02043, ltwakecav, d01416, 
l3_c_a16, d02043, ltwakecav, d01416, l3_c_a16, d02043, ltwakecav, d01416, 
l3_c_a16, d02043, ltwakecav, l3_q_a16_1, l3_cx, d0085, l3_bpmc, d0085, 
d00729, d0300, l3_enac_a16_1, l3_stac_a16_2, d0080, d01416, l3_c_a16, d02043, 
ltwakecav, d01416, l3_c_a16, d02043, ltwakecav, d01416, l3_c_a16, d02043, 
ltwakecav, d01416, l3_c_a16, d02043, ltwakecav, miac, d01416, l3_c_a16, 
d02043, ltwakecav, d01416, l3_c_a16, d02043, ltwakecav, d01416, l3_c_a16, 
d02043, ltwakecav, d01416, l3_c_a16, d02043, ltwakecav, l3_q_a16_2, l3_cy, 
d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a16_2, l3_stac_a16_3, d0080, 
d01416, l3_c_a16, d02043, ltwakecav, d01416, l3_c_a16, d02043, ltwakecav, 
d01416, l3_c_a16, d02043, ltwakecav, d01416, l3_c_a16, d02043, ltwakecav, 
miac, d01416, l3_c_a16, d02043, ltwakecav, d01416, l3_c_a16, d02043, 
ltwakecav, d01416, l3_c_a16, d02043, ltwakecav, d01416, l3_c_a16, d02043, 
ltwakecav, l3_q_a16_3, l3_cx, d0085, l3_bpmc, d0085, d00729, d0300, 
l3_enac_a16_3, l3_stac_a16_4, d0080, d01416, l3_c_a16, d02043, ltwakecav, d01416, 
l3_c_a16, d02043, ltwakecav, d01416, l3_c_a16, d02043, ltwakecav, d01416, 
l3_c_a16, d02043, ltwakecav, miac, d01416, l3_c_a16, d02043, ltwakecav, 
d01416, l3_c_a16, d02043, ltwakecav, d01416, l3_c_a16, d02043, ltwakecav, 
d01416, l3_c_a16, d02043, ltwakecav, l3_q_a16_4, l3_cy, d0085, l3_bpmc, 
d0085, d00729, d0300, l3_enac_a16_4, l3_stac_a17_1, d0080, d01416, l3_c_a17, 
d02043, ltwakecav, d01416, l3_c_a17, d02043, ltwakecav, d01416, l3_c_a17, 
d02043, ltwakecav, d01416, l3_c_a17, d02043, ltwakecav, miac, d01416, 
l3_c_a17, d02043, ltwakecav, d01416, l3_c_a17, d02043, ltwakecav, d01416, 
l3_c_a17, d02043, ltwakecav, d01416, l3_c_a17, d02043, ltwakecav, l3_q_a17_1, 
l3_cx, d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a17_1, l3_stac_a17_2, 
d0080, d01416, l3_c_a17, d02043, ltwakecav, d01416, l3_c_a17, d02043, 
ltwakecav, d01416, l3_c_a17, d02043, ltwakecav, d01416, l3_c_a17, d02043, 
ltwakecav, miac, d01416, l3_c_a17, d02043, ltwakecav, d01416, l3_c_a17, 
d02043, ltwakecav, d01416, l3_c_a17, d02043, ltwakecav, d01416, l3_c_a17, 
d02043, ltwakecav, l3_q_a17_2, l3_cy, d0085, l3_bpmc, d0085, d00729, 
d0300, l3_enac_a17_2, l3_stac_a17_3, d0080, d01416, l3_c_a17, d02043, ltwakecav, 
d01416, l3_c_a17, d02043, ltwakecav, d01416, l3_c_a17, d02043, ltwakecav, 
d01416, l3_c_a17, d02043, ltwakecav, miac, d01416, l3_c_a17, d02043, 
ltwakecav, d01416, l3_c_a17, d02043, ltwakecav, d01416, l3_c_a17, d02043, 
ltwakecav, d01416, l3_c_a17, d02043, ltwakecav, l3_q_a17_3, l3_cx, d0085, 
l3_bpmr, d0085, d00729, d0300, l3_enac_a17_3, l3_stac_a17_4, d0080, d01416, 
l3_c_a17, d02043, ltwakecav, d01416, l3_c_a17, d02043, ltwakecav, d01416, 
l3_c_a17, d02043, ltwakecav, d01416, l3_c_a17, d02043, ltwakecav, miac, 
d01416, l3_c_a17, d02043, ltwakecav, d01416, l3_c_a17, d02043, ltwakecav, 
d01416, l3_c_a17, d02043, ltwakecav, d01416, l3_c_a17, d02043, ltwakecav, 
l3_q_a17_4, l3_cy, d0085, l3_bpmr, d0085, d00729, d0300, l3_enac_a17_4, 
l3_csc, l3_stac_a18_1, d0080, d01416, l3_c_a18, d02043, ltwakecav, d01416, 
l3_c_a18, d02043, ltwakecav, d01416, l3_c_a18, d02043, ltwakecav, d01416, 
l3_c_a18, d02043, ltwakecav, miac, d01416, l3_c_a18, d02043, ltwakecav, 
d01416, l3_c_a18, d02043, ltwakecav, d01416, l3_c_a18, d02043, ltwakecav, 
d01416, l3_c_a18, d02043, ltwakecav, l3_q_a18_1, l3_cx, d0085, l3_bpmr, 
d0085, d00729, d0300, l3_enac_a18_1, l3_stac_a18_2, d0080, d01416, l3_c_a18, 
d02043, ltwakecav, d01416, l3_c_a18, d02043, ltwakecav, d01416, l3_c_a18, 
d02043, ltwakecav, d01416, l3_c_a18, d02043, ltwakecav, miac, d01416, 
l3_c_a18, d02043, ltwakecav, d01416, l3_c_a18, d02043, ltwakecav, d01416, 
l3_c_a18, d02043, ltwakecav, d01416, l3_c_a18, d02043, ltwakecav, l3_q_a18_2, 
l3_cy, d0085, l3_bpmr, d0085, d00729, d0300, l3_enac_a18_2, l3_stac_a18_3, 
d0080, d01416, l3_c_a18, d02043, ltwakecav, d01416, l3_c_a18, d02043, 
ltwakecav, d01416, l3_c_a18, d02043, ltwakecav, d01416, l3_c_a18, d02043, 
ltwakecav, miac, d01416, l3_c_a18, d02043, ltwakecav, d01416, l3_c_a18, 
d02043, ltwakecav, d01416, l3_c_a18, d02043, ltwakecav, d01416, l3_c_a18, 
d02043, ltwakecav, l3_q_a18_3, l3_cx, d0085, l3_bpmc, d0085, d00729, 
d0300, l3_enac_a18_3, l3_stac_a18_4, d0080, d01416, l3_c_a18, d02043, ltwakecav, 
d01416, l3_c_a18, d02043, ltwakecav, d01416, l3_c_a18, d02043, ltwakecav, 
d01416, l3_c_a18, d02043, ltwakecav, miac, d01416, l3_c_a18, d02043, 
ltwakecav, d01416, l3_c_a18, d02043, ltwakecav, d01416, l3_c_a18, d02043, 
ltwakecav, d01416, l3_c_a18, d02043, ltwakecav, l3_q_a18_4, l3_cy, d0085, 
l3_bpmc, d0085, d00729, d0300, l3_enac_a18_4, l3_stac_a19_1, d0080, d01416, 
l3_c_a19, d02043, ltwakecav, d01416, l3_c_a19, d02043, ltwakecav, d01416, 
l3_c_a19, d02043, ltwakecav, d01416, l3_c_a19, d02043, ltwakecav, miac, 
d01416, l3_c_a19, d02043, ltwakecav, d01416, l3_c_a19, d02043, ltwakecav, 
d01416, l3_c_a19, d02043, ltwakecav, d01416, l3_c_a19, d02043, ltwakecav, 
l3_q_a19_1, l3_cx, d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a19_1, 
l3_stac_a19_2, d0080, d01416, l3_c_a19, d02043, ltwakecav, d01416, l3_c_a19, 
d02043, ltwakecav, d01416, l3_c_a19, d02043, ltwakecav, d01416, l3_c_a19, 
d02043, ltwakecav, miac, d01416, l3_c_a19, d02043, ltwakecav, d01416, 
l3_c_a19, d02043, ltwakecav, d01416, l3_c_a19, d02043, ltwakecav, d01416, 
l3_c_a19, d02043, ltwakecav, l3_q_a19_2, l3_cy, d0085, l3_bpmc, d0085, 
d00729, d0300, l3_enac_a19_2, l3_stac_a19_3, d0080, d01416, l3_c_a19, d02043, 
ltwakecav, d01416, l3_c_a19, d02043, ltwakecav, d01416, l3_c_a19, d02043, 
ltwakecav, d01416, l3_c_a19, d02043, ltwakecav, miac, d01416, l3_c_a19, 
d02043, ltwakecav, d01416, l3_c_a19, d02043, ltwakecav, d01416, l3_c_a19, 
d02043, ltwakecav, d01416, l3_c_a19, d02043, ltwakecav, l3_q_a19_3, l3_cx, 
d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a19_3, l3_stac_a19_4, d0080, 
d01416, l3_c_a19, d02043, ltwakecav, d01416, l3_c_a19, d02043, ltwakecav, 
d01416, l3_c_a19, d02043, ltwakecav, d01416, l3_c_a19, d02043, ltwakecav, 
miac, d01416, l3_c_a19, d02043, ltwakecav, d01416, l3_c_a19, d02043, 
ltwakecav, d01416, l3_c_a19, d02043, ltwakecav, d01416, l3_c_a19, d02043, 
ltwakecav, l3_q_a19_4, l3_cy, d0085, l3_bpmc, d0085, d00729, d0300, 
l3_enac_a19_4, l3_stac_a20_1, d0080, d01416, l3_c_a20, d02043, ltwakecav, d01416, 
l3_c_a20, d02043, ltwakecav, d01416, l3_c_a20, d02043, ltwakecav, d01416, 
l3_c_a20, d02043, ltwakecav, miac, d01416, l3_c_a20, d02043, ltwakecav, 
d01416, l3_c_a20, d02043, ltwakecav, d01416, l3_c_a20, d02043, ltwakecav, 
d01416, l3_c_a20, d02043, ltwakecav, l3_q_a20_1, l3_cx, d0085, l3_bpmc, 
d0085, d00729, d0300, l3_enac_a20_1, l3_stac_a20_2, d0080, d01416, l3_c_a20, 
d02043, ltwakecav, d01416, l3_c_a20, d02043, ltwakecav, d01416, l3_c_a20, 
d02043, ltwakecav, d01416, l3_c_a20, d02043, ltwakecav, miac, d01416, 
l3_c_a20, d02043, ltwakecav, d01416, l3_c_a20, d02043, ltwakecav, d01416, 
l3_c_a20, d02043, ltwakecav, d01416, l3_c_a20, d02043, ltwakecav, l3_q_a20_2, 
l3_cy, d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a20_2, l3_stac_a20_3, 
d0080, d01416, l3_c_a20, d02043, ltwakecav, d01416, l3_c_a20, d02043, 
ltwakecav, d01416, l3_c_a20, d02043, ltwakecav, d01416, l3_c_a20, d02043, 
ltwakecav, miac, d01416, l3_c_a20, d02043, ltwakecav, d01416, l3_c_a20, 
d02043, ltwakecav, d01416, l3_c_a20, d02043, ltwakecav, d01416, l3_c_a20, 
d02043, ltwakecav, l3_q_a20_3, l3_cx, d0085, l3_bpmr, d0085, d00729, 
d0300, l3_enac_a20_3, l3_stac_a20_4, d0080, d01416, l3_c_a20, d02043, ltwakecav, 
d01416, l3_c_a20, d02043, ltwakecav, d01416, l3_c_a20, d02043, ltwakecav, 
d01416, l3_c_a20, d02043, ltwakecav, miac, d01416, l3_c_a20, d02043, 
ltwakecav, d01416, l3_c_a20, d02043, ltwakecav, d01416, l3_c_a20, d02043, 
ltwakecav, d01416, l3_c_a20, d02043, ltwakecav, l3_q_a20_4, l3_cy, d0085, 
l3_bpmr, d0085, d00729, d0300, l3_enac_a20_4, l3_csc, l3_stac_a21_1, d0080, 
d01416, l3_c_a21, d02043, ltwakecav, d01416, l3_c_a21, d02043, ltwakecav, 
d01416, l3_c_a21, d02043, ltwakecav, d01416, l3_c_a21, d02043, ltwakecav, 
miac, d01416, l3_c_a21, d02043, ltwakecav, d01416, l3_c_a21, d02043, 
ltwakecav, d01416, l3_c_a21, d02043, ltwakecav, d01416, l3_c_a21, d02043, 
ltwakecav, l3_q_a21_1, l3_cx, d0085, l3_bpmr, d0085, d00729, d0300, 
l3_enac_a21_1, l3_stac_a21_2, d0080, d01416, l3_c_a21, d02043, ltwakecav, d01416, 
l3_c_a21, d02043, ltwakecav, d01416, l3_c_a21, d02043, ltwakecav, d01416, 
l3_c_a21, d02043, ltwakecav, miac, d01416, l3_c_a21, d02043, ltwakecav, 
d01416, l3_c_a21, d02043, ltwakecav, d01416, l3_c_a21, d02043, ltwakecav, 
d01416, l3_c_a21, d02043, ltwakecav, l3_q_a21_2, l3_cy, d0085, l3_bpmr, 
d0085, d00729, d0300, l3_enac_a21_2, l3_stac_a21_3, d0080, d01416, l3_c_a21, 
d02043, ltwakecav, d01416, l3_c_a21, d02043, ltwakecav, d01416, l3_c_a21, 
d02043, ltwakecav, d01416, l3_c_a21, d02043, ltwakecav, miac, d01416, 
l3_c_a21, d02043, ltwakecav, d01416, l3_c_a21, d02043, ltwakecav, d01416, 
l3_c_a21, d02043, ltwakecav, d01416, l3_c_a21, d02043, ltwakecav, l3_q_a21_3, 
l3_cx, d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a21_3, l3_stac_a21_4, 
d0080, d01416, l3_c_a21, d02043, ltwakecav, d01416, l3_c_a21, d02043, 
ltwakecav, d01416, l3_c_a21, d02043, ltwakecav, d01416, l3_c_a21, d02043, 
ltwakecav, miac, d01416, l3_c_a21, d02043, ltwakecav, d01416, l3_c_a21, 
d02043, ltwakecav, d01416, l3_c_a21, d02043, ltwakecav, d01416, l3_c_a21, 
d02043, ltwakecav, l3_q_a21_4, l3_cy, d0085, l3_bpmc, d0085, d00729, 
d0300, l3_enac_a21_4, l3_stac_a22_1, d0080, d01416, l3_c_a22, d02043, ltwakecav, 
d01416, l3_c_a22, d02043, ltwakecav, d01416, l3_c_a22, d02043, ltwakecav, 
d01416, l3_c_a22, d02043, ltwakecav, miac, d01416, l3_c_a22, d02043, 
ltwakecav, d01416, l3_c_a22, d02043, ltwakecav, d01416, l3_c_a22, d02043, 
ltwakecav, d01416, l3_c_a22, d02043, ltwakecav, l3_q_a22_1, l3_cx, d0085, 
l3_bpmc, d0085, d00729, d0300, l3_enac_a22_1, l3_stac_a22_2, d0080, d01416, 
l3_c_a22, d02043, ltwakecav, d01416, l3_c_a22, d02043, ltwakecav, d01416, 
l3_c_a22, d02043, ltwakecav, d01416, l3_c_a22, d02043, ltwakecav, miac, 
d01416, l3_c_a22, d02043, ltwakecav, d01416, l3_c_a22, d02043, ltwakecav, 
d01416, l3_c_a22, d02043, ltwakecav, d01416, l3_c_a22, d02043, ltwakecav, 
l3_q_a22_2, l3_cy, d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a22_2, 
l3_stac_a22_3, d0080, d01416, l3_c_a22, d02043, ltwakecav, d01416, l3_c_a22, 
d02043, ltwakecav, d01416, l3_c_a22, d02043, ltwakecav, d01416, l3_c_a22, 
d02043, ltwakecav, miac, d01416, l3_c_a22, d02043, ltwakecav, d01416, 
l3_c_a22, d02043, ltwakecav, d01416, l3_c_a22, d02043, ltwakecav, d01416, 
l3_c_a22, d02043, ltwakecav, l3_q_a22_3, l3_cx, d0085, l3_bpmc, d0085, 
d00729, d0300, l3_enac_a22_3, l3_stac_a22_4, d0080, d01416, l3_c_a22, d02043, 
ltwakecav, d01416, l3_c_a22, d02043, ltwakecav, d01416, l3_c_a22, d02043, 
ltwakecav, d01416, l3_c_a22, d02043, ltwakecav, miac, d01416, l3_c_a22, 
d02043, ltwakecav, d01416, l3_c_a22, d02043, ltwakecav, d01416, l3_c_a22, 
d02043, ltwakecav, d01416, l3_c_a22, d02043, ltwakecav, l3_q_a22_4, l3_cy, 
d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a22_4, l3_stac_a23_1, d0080, 
d01416, l3_c_a23, d02043, ltwakecav, d01416, l3_c_a23, d02043, ltwakecav, 
d01416, l3_c_a23, d02043, ltwakecav, d01416, l3_c_a23, d02043, ltwakecav, 
miac, d01416, l3_c_a23, d02043, ltwakecav, d01416, l3_c_a23, d02043, 
ltwakecav, d01416, l3_c_a23, d02043, ltwakecav, d01416, l3_c_a23, d02043, 
ltwakecav, l3_q_a23_1, l3_cx, d0085, l3_bpmc, d0085, d00729, d0300, 
l3_enac_a23_1, l3_stac_a23_2, d0080, d01416, l3_c_a23, d02043, ltwakecav, d01416, 
l3_c_a23, d02043, ltwakecav, d01416, l3_c_a23, d02043, ltwakecav, d01416, 
l3_c_a23, d02043, ltwakecav, miac, d01416, l3_c_a23, d02043, ltwakecav, 
d01416, l3_c_a23, d02043, ltwakecav, d01416, l3_c_a23, d02043, ltwakecav, 
d01416, l3_c_a23, d02043, ltwakecav, l3_q_a23_2, l3_cy, d0085, l3_bpmc, 
d0085, d00729, d0300, l3_enac_a23_2, l3_stac_a23_3, d0080, d01416, l3_c_a23, 
d02043, ltwakecav, d01416, l3_c_a23, d02043, ltwakecav, d01416, l3_c_a23, 
d02043, ltwakecav, d01416, l3_c_a23, d02043, ltwakecav, miac, d01416, 
l3_c_a23, d02043, ltwakecav, d01416, l3_c_a23, d02043, ltwakecav, d01416, 
l3_c_a23, d02043, ltwakecav, d01416, l3_c_a23, d02043, ltwakecav, l3_q_a23_3, 
l3_cx, d0085, l3_bpmr, d0085, d00729, d0300, l3_enac_a23_3, l3_stac_a23_4, 
d0080, d01416, l3_c_a23, d02043, ltwakecav, d01416, l3_c_a23, d02043, 
ltwakecav, d01416, l3_c_a23, d02043, ltwakecav, d01416, l3_c_a23, d02043, 
ltwakecav, miac, d01416, l3_c_a23, d02043, ltwakecav, d01416, l3_c_a23, 
d02043, ltwakecav, d01416, l3_c_a23, d02043, ltwakecav, d01416, l3_c_a23, 
d02043, ltwakecav, l3_q_a23_4, l3_cy, d0085, l3_bpmr, d0085, d00729, 
d0300, l3_enac_a23_4, l3_csc, l3_stac_a24_1, d0080, d01416, l3_c_a24, d02043, 
ltwakecav, d01416, l3_c_a24, d02043, ltwakecav, d01416, l3_c_a24, d02043, 
ltwakecav, d01416, l3_c_a24, d02043, ltwakecav, miac, d01416, l3_c_a24, 
d02043, ltwakecav, d01416, l3_c_a24, d02043, ltwakecav, d01416, l3_c_a24, 
d02043, ltwakecav, d01416, l3_c_a24, d02043, ltwakecav, l3_q_a24_1, l3_cx, 
d0085, l3_bpmr, d0085, d00729, d0300, l3_enac_a24_1, l3_stac_a24_2, d0080, 
d01416, l3_c_a24, d02043, ltwakecav, d01416, l3_c_a24, d02043, ltwakecav, 
d01416, l3_c_a24, d02043, ltwakecav, d01416, l3_c_a24, d02043, ltwakecav, 
miac, d01416, l3_c_a24, d02043, ltwakecav, d01416, l3_c_a24, d02043, 
ltwakecav, d01416, l3_c_a24, d02043, ltwakecav, d01416, l3_c_a24, d02043, 
ltwakecav, l3_q_a24_2, l3_cy, d0085, l3_bpmr, d0085, d00729, d0300, 
l3_enac_a24_2, l3_stac_a24_3, d0080, d01416, l3_c_a24, d02043, ltwakecav, d01416, 
l3_c_a24, d02043, ltwakecav, d01416, l3_c_a24, d02043, ltwakecav, d01416, 
l3_c_a24, d02043, ltwakecav, miac, d01416, l3_c_a24, d02043, ltwakecav, 
d01416, l3_c_a24, d02043, ltwakecav, d01416, l3_c_a24, d02043, ltwakecav, 
d01416, l3_c_a24, d02043, ltwakecav, l3_q_a24_3, l3_cx, d0085, l3_bpmc, 
d0085, d00729, d0300, l3_enac_a24_3, l3_stac_a24_4, d0080, d01416, l3_c_a24, 
d02043, ltwakecav, d01416, l3_c_a24, d02043, ltwakecav, d01416, l3_c_a24, 
d02043, ltwakecav, d01416, l3_c_a24, d02043, ltwakecav, miac, d01416, 
l3_c_a24, d02043, ltwakecav, d01416, l3_c_a24, d02043, ltwakecav, d01416, 
l3_c_a24, d02043, ltwakecav, d01416, l3_c_a24, d02043, ltwakecav, l3_q_a24_4, 
l3_cy, d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a24_4, l3_stac_a25_1, 
d0080, d01416, l3_c_a25, d02043, ltwakecav, d01416, l3_c_a25, d02043, 
ltwakecav, d01416, l3_c_a25, d02043, ltwakecav, d01416, l3_c_a25, d02043, 
ltwakecav, miac, d01416, l3_c_a25, d02043, ltwakecav, d01416, l3_c_a25, 
d02043, ltwakecav, d01416, l3_c_a25, d02043, ltwakecav, d01416, l3_c_a25, 
d02043, ltwakecav, l3_q_a25_1, l3_cx, d0085, l3_bpmc, d0085, d00729, 
d0300, l3_enac_a25_1, l3_stac_a25_2, d0080, d01416, l3_c_a25, d02043, ltwakecav, 
d01416, l3_c_a25, d02043, ltwakecav, d01416, l3_c_a25, d02043, ltwakecav, 
d01416, l3_c_a25, d02043, ltwakecav, miac, d01416, l3_c_a25, d02043, 
ltwakecav, d01416, l3_c_a25, d02043, ltwakecav, d01416, l3_c_a25, d02043, 
ltwakecav, d01416, l3_c_a25, d02043, ltwakecav, l3_q_a25_2, l3_cy, d0085, 
l3_bpmc, d0085, d00729, d0300, l3_enac_a25_2, l3_stac_a25_3, d0080, d01416, 
l3_c_a25, d02043, ltwakecav, d01416, l3_c_a25, d02043, ltwakecav, d01416, 
l3_c_a25, d02043, ltwakecav, d01416, l3_c_a25, d02043, ltwakecav, miac, 
d01416, l3_c_a25, d02043, ltwakecav, d01416, l3_c_a25, d02043, ltwakecav, 
d01416, l3_c_a25, d02043, ltwakecav, d01416, l3_c_a25, d02043, ltwakecav, 
l3_q_a25_3, l3_cx, d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a25_3, 
l3_stac_a25_4, d0080, d01416, l3_c_a25, d02043, ltwakecav, d01416, l3_c_a25, 
d02043, ltwakecav, d01416, l3_c_a25, d02043, ltwakecav, d01416, l3_c_a25, 
d02043, ltwakecav, miac, d01416, l3_c_a25, d02043, ltwakecav, d01416, 
l3_c_a25, d02043, ltwakecav, d01416, l3_c_a25, d02043, ltwakecav, d01416, 
l3_c_a25, d02043, ltwakecav, l3_q_a25_4, l3_cy, d0085, l3_bpmc, d0085, 
d00729, d0300, l3_enac_a25_4, l3_stac_a26_1, d0080, d01416, l3_c_a26, d02043, 
ltwakecav, d01416, l3_c_a26, d02043, ltwakecav, d01416, l3_c_a26, d02043, 
ltwakecav, d01416, l3_c_a26, d02043, ltwakecav, miac, d01416, l3_c_a26, 
d02043, ltwakecav, d01416, l3_c_a26, d02043, ltwakecav, d01416, l3_c_a26, 
d02043, ltwakecav, d01416, l3_c_a26, d02043, ltwakecav, l3_q_a26_1, l3_cx, 
d0085, l3_bpmc, d0085, d00729, d0300, l3_enac_a26_1, l3_stac_a26_2, d0080, 
d01416, l3_c_a26, d02043, ltwakecav, d01416, l3_c_a26, d02043, ltwakecav, 
d01416, l3_c_a26, d02043, ltwakecav, d01416, l3_c_a26, d02043, ltwakecav, 
miac, d01416, l3_c_a26, d02043, ltwakecav, d01416, l3_c_a26, d02043, 
ltwakecav, d01416, l3_c_a26, d02043, ltwakecav, d01416, l3_c_a26, d02043, 
ltwakecav, l3_q_a26_2, l3_cy, d0085, l3_bpmc, d0085, d00729, d0300, 
l3_enac_a26_2, l3_stac_a26_3, d0080, d01416, l3_c_a26, d02043, ltwakecav, d01416, 
l3_c_a26, d02043, ltwakecav, d01416, l3_c_a26, d02043, ltwakecav, d01416, 
l3_c_a26, d02043, ltwakecav, miac, d01416, l3_c_a26, d02043, ltwakecav, 
d01416, l3_c_a26, d02043, ltwakecav, d01416, l3_c_a26, d02043, ltwakecav, 
d01416, l3_c_a26, d02043, ltwakecav, l3_q_a26_3, l3_cx, d0085, l3_bpmr, 
d0085, d00729, d0300, l3_enac_a26_3, l3_stac_a26_4, d0080, d01416, l3_c_a26, 
d02043, ltwakecav, d01416, l3_c_a26, d02043, ltwakecav, d01416, l3_c_a26, 
d02043, ltwakecav, d01416, l3_c_a26, d02043, ltwakecav, miac, d01416, 
l3_c_a26, d02043, ltwakecav, d01416, l3_c_a26, d02043, ltwakecav, d01416, 
l3_c_a26, d02043, ltwakecav, d01416, l3_c_a26, d02043, ltwakecav, l3_q_a26_4, 
l3_cy, d0085, l3_bpmr, d0085, d00729, d0300, l3_enac_a26_4, l3_ctb, 
l3_vcst78t40, d0100, d002575, l3_vcdst, d042845, l3_tora, d02308, d359096c, 
d0200, l3_otrbw, d0400, d359096b, d0100, l3_bpma, d0100, d0050, 
d0075, l3_qe_1_1, d0080, d0050, d0030, l3_cex, d0030, d359096a, 
d0200, d0400, d359096b, d0100, l3_bpma, d0100, d0050, d0075, 
l3_qe_1_2, d0080, d0050, d0030, l3_cey, d0030, d359096a, d0200, 
l3_otrbw, d0400, d359096b, d0100, l3_bpma, d0100, d0050, d0075, 
l3_qe_1_1, d0080, d0050, d0030, l3_cex, d0030, d1277325, d0100, 
l3_bpma, d0100, d0050, d0075, l3_qe_2, d0080, d0050, d0030, 
l3_cey, d0030, d5780, l3_otrbw, d5745, d0100, l3_bpma, d0100, 
d0050, d0075, l3_qf_1, d0080, d0050, d0040, l3_cfx, d0040, 
d8215, d0100, l3_bpma, d0100, d0050, d0075, l3_qf_2, d0080, 
d0050, d0040, l3_cfy, d0040, d11263, l3_end_l3)