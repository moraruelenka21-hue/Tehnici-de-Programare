from arsenal.privesc.enum import citeste_linii

start = 'arsenal/privesc/start'
c = citeste_linii(start + '/suid.txt')
print('linii SUID:', len(c))
