import re, sys

#2018-01-16 14:51:44.366
#lat:54.7751435 long:-1.5745468
pattern = r"lat:([-0-9.]+) long:([-0-9.]+)"
pattern = r"(\d\d\d\d-\d\d-\d\d) (\d\d:\d\d):\d\d" + ".*" + pattern

s = ""


for line in open(sys.argv[1]):
    mo = re.search(pattern, line)
    if mo:
        #print mo.group(1), mo.group(2),
        latitude = mo.group(3)
        longitude = mo.group(4)
        time = mo.group(2)
        s +=  '[' +  latitude + ',' + longitude + ',' + '"' + time + '"' + '],\n'

s = s[:-2]
s = '[' + s + ']'
s = "var results =" + s
s += ';'
print s
