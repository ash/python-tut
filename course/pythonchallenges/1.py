s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

for c in s:
    n = ord(c)
    if n >= ord('a') and n <= ord('z'):
        if c == 'y':
            c = 'a'
        elif c == 'z':
            c = 'b'
        else:
            c = chr(ord(c) + 2)
    print(c, end='')
