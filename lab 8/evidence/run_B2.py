from arsenal.privesc.diferenta import cai

start = 'arsenal/privesc/start'
baza = cai(start + '/baza_suid.txt')
acum = cai(start + '/suid.txt')
noi = acum - baza
print(len(noi), 'SUID noi fata de sistemul curat')
for c in sorted(noi): print(' ', c)
