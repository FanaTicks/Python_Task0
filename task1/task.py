s = input("Enter:")
l = len(s)
integ = []
integ2 = []
i = 0

while i < l:
    s_int = ''
    a = s[i]
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < l:
            a = s[i]
        else:
            break
    i += 1
    if s_int != '':
        integ.append(int(s_int))
print("Only numbers:",integ)

largest_number = max(integ)
print("Max=",largest_number)

for i in range(len(integ)):
    if integ[i] != largest_number:
        integ2.append(integ[i]**i)
print("The numbers are raised to the power of them index:",integ2)

for d in '1234567890':
    s=s.replace(d, '')
s.strip(' ')
while s.find('  ') != -1:
    s = s.replace('  ', ' ')
print("Characters only:",s)
def big(s):
 r=""
 z=0
 spl=str(s).split()
 for i in spl:
    for i in spl[z].split():
        a=''.join(spl[z])
        if len(a)==1:
                r=r+a[0].upper()+' '
        else:
                r=r+a[0].upper()+a[1:-1]+a[-1].upper()+' '
        z=z+1
 return r
print("Each word begins and ends with a capital letter:",big(s))
