# find max
# find min
# convert to tuple so it's order and removes duplicates
# loop through every number from min to max and check if this number is in the tuple
# if not add it to the resultc

# codechef practice c++, solved 1500 - went on 1800 problem - worked on a full stack project again and did some codechef

import hashlib
import os
random_bytes = os.urandom(24)
print(random_bytes)
username_trial = b"MORTON"

print(hashlib.sha256(username_trial).hexdigest()[4])

print("".join(hashlib.sha256(username_trial).hexdigest()[x] for x in (4, 5, 3, 6, 2, 7, 1, 8)))
