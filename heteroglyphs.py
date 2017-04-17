"""
Sample code for generating heteroglyphic codes for easy human entry.
See: https://github.com/mattpavelle/heteroglyphs/blob/master/README.md
"""

import random

# heteroglyph_upper = `347ACDEFHJKMNPQRTXY`
hgu = ['3', '4', '7', 'A', 'C', 'D', 'E', 'F', 'H', 'J', 'K', 'M', 'N', 'P', 'Q', 'R', 'T', 'X',
       'Y']
# heteroglyph_msft = `2346789BCDFGHJKMPQRTVWXY`
hgm = ['2', '3', '4', '6', '7', '8', '9', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'M', 'P', 'Q',
       'R', 'T', 'V', 'W', 'X', 'Y']

# the length (number of characters) to be in your code
cdl = 17  # change this to suit your needs

# code separator - will be inserted every spc characters in your code
cds = '-'  # change this to another characer (or delete it)
spc = 4  # change as needed

res = cds.join([''.join(random.choices(hgu, k=cdl))[i:i + spc] for i in range(0, cdl, spc)])

# print(res)
