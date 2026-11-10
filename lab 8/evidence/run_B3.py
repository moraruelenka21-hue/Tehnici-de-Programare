from arsenal.privesc.diferenta import cai, compara

start = 'arsenal/privesc/start'
r = compara(cai(start + '/baza_suid.txt'), cai(start + '/suid.txt'))
print('periculoase NOI:')
for c in r['periculoase']: print(c)
