"""
Martin Dohlus DESY, 2015
"""
import numpy as np

from numpy.linalg import norm

def arcline( SREin, Delta_S, dS, R_vect ):
    """
    :param SREin: in
    :param Delta_S:
    :param dS:
    :param R_vect:
    :return:
    """
    #%arcline( sre0,Delta_S,dS,R_vect )

    epsilon = 1e-8

    sre0 = SREin[:,-1]
    N = max(1, np.round(Delta_S/dS))
    #print N
    dS = Delta_S/N
    SRE2 = np.zeros((7, N))
    SRE2[0,:] = sre0[0] + np.arange(1, N+1)*dS

    R_vect_valid = False
    # if nargin==4 && isequal(size(R_vect),[3 1]):

    if True:
        #print np.all(np.equal(R_vect, np.zeros((3,1))))
        R_vect_valid = np.all(np.isfinite(R_vect)) and not np.all(np.equal(R_vect, np.zeros((3,1))))
        if R_vect_valid:
            R = norm(R_vect)
            n_vect = R_vect/R
            e1=sre0[4:7]
            if np.abs(np.dot(n_vect, e1)) > epsilon:
                R_vect_valid = False
                print('*** error in arcline: invalid R_vect --> using line')




    if not R_vect_valid:
        SRE2[2-1, :] = sre0[2-1] + sre0[5-1]*np.arange(1, N+1)*dS
        SRE2[3-1, :] = sre0[3-1] + sre0[6-1]*np.arange(1, N+1)*dS
        SRE2[4-1, :] = sre0[4-1] + sre0[7-1]*np.arange(1, N+1)*dS
        SRE2[5-1, :] = sre0[5-1]
        SRE2[6-1, :] = sre0[6-1]
        SRE2[7-1, :] = sre0[7-1]
    else:
        R = norm(R_vect)
        n_vect = R_vect/R
        e2 = np.array([[n_vect[1]*e1[2] - n_vect[2]*e1[1]],
            [n_vect[2]*e1[0] - n_vect[0]*e1[2]],
            [n_vect[0]*e1[1] - n_vect[1]*e1[0]]])
        si = np.sin(np.arange(1, N+1)*dS/R)
        co = np.cos(np.arange(1, N+1)*dS/R)
        omco = 2*np.sin(np.arange(1, N+1)*dS/R/2)**2
        SRE2[2-1, :] = sre0[1] + R*(e1[0]*si + e2[0]*omco)
        SRE2[3-1, :] = sre0[2] + R*(e1[1]*si + e2[1]*omco)
        SRE2[4-1, :] = sre0[3] + R*(e1[2]*si + e2[2]*omco)
        SRE2[5-1, :] = e1[0]*co + e2[0]*si
        SRE2[6-1, :] = e1[1]*co + e2[1]*si
        SRE2[7-1, :] = e1[2]*co + e2[2]*si

    #print np.shape(np.transpose([SREin])), np.shape(SRE2)
    SRE = np.append(SREin, SRE2, axis=1)

    return SRE

