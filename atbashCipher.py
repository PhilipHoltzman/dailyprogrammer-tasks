#! Python3 

# Atbash Cipher from /r/dailyprogrammer
# To encode or decode strings using the Atbash Cipher

# Plain:  abcdefghijklmnopqrstuvwxyz

message = 'Fear is the mindkiller'

alephbet = 'abcdefghijklmnopqrstuvwxyz'

cipher = alephbet[::-1]

sub = dict(zip(alephbet,cipher))

print(''.join( map( lambda x: sub[x] if x in sub else x ,message)))