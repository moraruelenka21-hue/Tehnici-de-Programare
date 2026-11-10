from arsenal.privesc.enum import enumereaza, filtreaza_risc, grupeaza_risc

start = 'arsenal/privesc/start'
r = enumereaza(start)
print({k: len(v) for k, v in filtreaza_risc(r, 'mare').items()})
print({k: len(v) for k, v in grupeaza_risc(r).items()})
