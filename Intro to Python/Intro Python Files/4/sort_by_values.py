#!/usr/bin/env python3
def usethis(akey):
    return states[akey]

states = {'New Hampshire':'NH', 'Maryland':'MD',
          'Nevada':'NV', 'Maine':'ME'}

long_names = list(states.keys())
long_names.sort(key=usethis)
#long_names.sort(usethis(key))
for name in long_names:
    print(name, states[name])
