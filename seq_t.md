
# 碱基序列反向互补
'''python
def revcomp(seq):
    """ 碱基序列反向互补 """
    set_all = set('ATCGatcgRYMKrymkVBHDvbhd')
    set_seq = set(seq)
    if set_seq - set_all:
        print("\033[31m* 字符%s超出碱基范围\033[0m" % ",".join(set_seq -set_all))
        return
    seq = seq[::-1]
    return seq.translate( str.maketrans( "ACGTacgtRYMKrymkVBHDvbhd",
                                         "TGCAtgcaYRKMyrkmBVDHbvdh"))
'''

