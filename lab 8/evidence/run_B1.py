from arsenal.privesc.diferenta import cai

start = 'arsenal/privesc/start'
baza = cai(start + '/baza_suid.txt')
acum = cai(start + '/suid.txt')
print('baza:', len(baza), ' acum:', len(acum))
