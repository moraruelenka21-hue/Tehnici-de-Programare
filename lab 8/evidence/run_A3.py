from arsenal.privesc.enum import suid_constatari

start = 'arsenal/privesc/start'
suid = suid_constatari(start + '/suid.txt')
mari = [c for c in suid if c['risc'] == 'mare']
print(len(suid), 'SUID,', len(mari), 'cu risc mare')
print(sorted(c['nume'] for c in mari))
