import string

ss = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr " \
     "ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

#  k->m, o->q, e->g

# print(ord('k')-ord('m'))
# print(ord('o')-ord('q'))
# print(ord('e')-ord('g'))

# for s in ss:
#     if ord('a') <= ord(s) <= ord('z'):
#         temp = ord(s)+2
#         if temp > ord('z'):
#             temp -= 26
#         print(chr(temp), end='')
#     else:
#         print(s, end='')

trantab = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
print(ss.translate(trantab))

ss2 = 'map'
print(ss2.translate(trantab))

