import numpy as np
import scipy.stats as stats
import math

np.random.seed(2019)


def simulate_days_ttests_with_samples(days_pairs, ratio_of_as,
                                      seed, sample_size=30):
    """Takes random samples from each of the days per week dataframes. """

    np.random.seed(seed)
    
    samples = {}
    for key, val in ratio_of_as.items():
        samples[key] = np.random.choice(val, size=sample_size)  

    for days1, days2 in days_pairs:
        if days1 == 1:
            first = samples['one']
        elif days1 == 2:
            first = samples['two']
        elif days1 == 3:
            first = samples['three']
        else:
            first = samples['four']

        if days2 == 2:
            second = samples['two']
        elif days2 == 3:
            second = samples['three']
        elif days2 == 4:
            second = samples['four']
        else:
            second = samples['five']
            
        print(days1, days2)
        print(stats.ttest_ind(first, second))
        

def get_sample_size(moe, z, vars_and_n):
    """Calculates the sample size for a given margin of error, confidence level, and dictionary of variances and sizes"""
    num = sum([(vars_and_n[i][1] - 1) * vars_and_n[i][0] for i in vars_and_n.keys()])
    den = sum([vars_and_n[i][1] for i in vars_and_n.keys()]) - len(vars_and_n)
    pooled_std = np.sqrt(num/den)
    n = 2 * (z * pooled_std / moe)**2
    n = math.ceil(n) # round up because we can't have a decimal
    return n
 
