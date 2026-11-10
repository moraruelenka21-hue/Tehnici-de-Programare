from arsenal.privesc.enum import enumereaza

start = 'arsenal/privesc/start'
r = enumereaza(start)
for c in r['sudo']: print(c['user'], c['risc'])
for c in r['cron']: print(c['user'], c['comanda'])
