import numpy as np

def Problem1():

    def PV(cf, r, t, face):
        return (cf/r)*(1-pow(1+r, -t)) + face/pow(1+r, t)

    def dPV(cf, r, t, face):
        A = t/pow(1+r, t+1)
        B = -cf/pow(r, 2)
        C = -t*face/pow(1+r,t+1)
        return A*(cf/r) + (1-pow(1+r,-t))*B + C
    
    value = 1200
    er = 0.1260
    gr = 0.0190
    div = 15.76
    coup = 0.098
    face = 1000
    mat = 12

    new_value = value - div/(er - gr)
    coupon = coup*face

    r0, r1 = 0.1, 0.99
    while True:
        r1 = r0 - (PV(coupon, r0, mat, face) - new_value)/dPV(coupon, r0, mat, face)
        if abs(r1 - r0) < 0.0001:
            break
        r0 = r1

    print('Answer: ', r1)


def Problem2():

    def PV(cf, r, t, face):
        return (cf/r)*(1-pow(1+r, -t)) + face/pow(1+r, t)

    value = 1000
    ytm = 0.0840
    coup = 0.0790
    mat = 12
    div = 2.17
    er = 0.1083
    face = 1000

    coupon = face*coup
    
    bond_pv = PV(coupon, ytm, mat, face)
    value -= bond_pv

    grow = er - div/value

    print("Answer: ", grow)


def Problem3():
    
    face = 1000
    oldprice = 962
    newprice = 865
    ror = -0.0570
    # rate = (newprice + coupon - oldprice)/oldprice
    # -0.0570 = (865 + coupon - 962)/962
    coupon = ror*oldprice + oldprice - newprice

    yld = (coupon*2)/newprice

    print('Answer: ', yld)


def Problem4():

    def PV(cf, r, t, face):
        return (cf/r)*(1-pow(1+r, -t)) + face/pow(1+r, t)

    coup = 0.1120
    face = 1000
    mat = 9*2
    oldprice = 835.17
    ytm = 0.1560

    coupon = coup*face/2

    bond_pv = PV(coupon, ytm/2, mat, face)

    ror = (bond_pv + coupon - oldprice)/oldprice

    print('Answer: ', ror)


def Problem5():

    er = 0.082
    gr = 0.029
    div = 68.50

    fv1 = div*pow(1 + gr, 4)
    disc = fv1/pow(1 + er, 5)

    print('Answer: ', disc)



    
Problem5()
