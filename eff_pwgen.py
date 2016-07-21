import random


r = random.SystemRandom()

with open("eff_small_wordlist_2.txt") as password_file:
    short_list = password_file.read().split()[1::2]
assert len(short_list) == 6**4, len(short_list)

with open("eff_large_wordlist.txt") as password_file:
    long_list = password_file.read().split()[1::2]
assert len(long_list) == 6**5, len(long_list)


# print short_list
# print long_list

# print len(set(x[0:3] for x in long_list))
# print len(set(x[0:3] for x in short_list))

# my_password = [r.choice(long_list) for _ in range(6)]
my_password = [r.choice(short_list) for _ in range(8)]
print " ".join(my_password)
print "".join(x[0:3] for x in my_password)