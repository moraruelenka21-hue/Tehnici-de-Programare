from arsenal.privesc.enum import citeste_linii, nume

start = 'arsenal/privesc/start'
c = citeste_linii(start + '/suid.txt')
u = {nume(x) for x in c}
print('SUID distincte:', len(u))
