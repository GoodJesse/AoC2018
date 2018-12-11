fobj = open('Calendar_8_in.txt', 'r')

data = fobj.read().split()
data = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split()
print data
l = []
new = True
su = 0
j = 0
layer = 0
cn = []
md = []


def f(data, layer, cn, md, su):
    cn.append(int(data.pop(0)))
    md.append(int(data.pop(0)))
    print str(cn) + ' Child Nodes'
    print str(md) + ' metadata'
    print str(layer) + ' layer'
    print cn[-1]
    if cn[-1] > 0 and len(data) > 0:
        layer += 1
        data, layer, cn, md, su = f(data, layer, cn, md, su)
    else:
        print 'elif'
        if md[-1] > 0:
            for i in range(md.pop()):
                if len(data) > 0:
                    su += int(data.pop(0))
            layer -= 1
            cn.pop()
            print str(su) + ' su'
    return data, layer, cn, md, su


while len(data) > 0:
    data, layer, cn, md, su = f(data, layer, cn, md, su)

print su