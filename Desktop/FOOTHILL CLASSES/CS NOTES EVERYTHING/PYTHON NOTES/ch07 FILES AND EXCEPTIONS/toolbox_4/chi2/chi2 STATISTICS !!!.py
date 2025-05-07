import scipy.stats

# https://www.census.gov/prod/2011pubs/12statab/vitstat.pdf

# Table 81
# 2008 births (single, twins, multiples) by race (white, black, hispanic)

data = [ 
    [ 2184914, 599536, 1017139 ],
    [ 82903, 22924, 23266 ],
    [ 4493, 569, 834 ]
]

p = scipy.stats.chi2_contingency(data)[1]
print(p)

# Table 87
# 2008 deliveries (vaginal, caesarian, not stated) by race (white, black, 
# hispanic) (in 1000s)

data = [
    [ 1527, 406, 717],
    [ 733, 214, 322],
    [ 8, 2, 3]
]

p = scipy.stats.chi2_contingency(data)[1]
print(p)
