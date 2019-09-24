# pgen
use the eff wordlists to create passwords

wordlists from the EFF

# new wordlist

from
https://initstring.keybase.pub/passphrase-wordlist/passphrases.txt?dl=1
https://github.com/dwyl/english-words/blob/master/words_alpha.txt

filtered down:
tr ' ' '\n'  <passphrases.txt | grep -E '^[[:alpha:]]+$' | sort | uniq > newpass.txt

