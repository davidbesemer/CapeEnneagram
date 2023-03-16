import sys
import json

def cape_handler(arg):

    ranks = json.loads(arg)

    # Score each type
    types = []
    types.append(ranks[0] + ranks[9] + ranks[18] + ranks[27])
    types.append(ranks[1] + ranks[10] + ranks[19] + ranks[28])
    types.append(ranks[2] + ranks[11] + ranks[20] + ranks[29])
    types.append(ranks[3] + ranks[12] + ranks[21] + ranks[30])
    types.append(ranks[4] + ranks[13] + ranks[22] + ranks[31])
    types.append(ranks[5] + ranks[14] + ranks[23] + ranks[32])
    types.append(ranks[6] + ranks[15] + ranks[24] + ranks[33])
    types.append(ranks[7] + ranks[16] + ranks[25] + ranks[34])
    types.append(ranks[8] + ranks[17] + ranks[26] + ranks[35])

    print(types, file=sys.stderr)

    max_type = max(types)
    my_types = []
    for ii in range(0,len(types)):
        if types[ii] == max_type:
            my_types.append(ii+1)
    
    return str(my_types);
