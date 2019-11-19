party_size = {}
for k, v in mp_affiliation.items():
    if not v in party_size.keys():
        party_size[v] = 1
    else:
        party_size[v] += 1
