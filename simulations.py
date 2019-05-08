import numpy as np
import scipy.stats as stats
import random

random.seed(1000)
#np.random.seed(2019)

def simulate_days_ttests_with_samples(days_pairs, one_day, two_days, 
                                      three_days, four_days, five_days, 
                                      seed, sample_size=30):
    """Takes random samples from each of the days per week dataframes. """
    
    np.random.seed(seed)

    
    one_sample = np.random.choice(one_day, size=sample_size)
    two_sample = np.random.choice(two_days, size=sample_size)
    three_sample = np.random.choice(three_days, size=sample_size)
    four_sample = np.random.choice(four_days, size=sample_size)
    five_sample = np.random.choice(five_days, size=sample_size)

    for days1, days2 in days_pairs: 
        if days1 == 1:
            first = one_sample
        elif days1 == 2:
            first = two_sample
        elif days1 == 3:
            first = three_sample
        else:
            first = four_sample
        if days2 == 2:
            second = two_sample
        elif days2 == 3:
            second = three_sample
        elif days2 == 4:
            second = four_sample
        else:
            second = five_sample
        print(days1, days2)
        print(stats.ttest_ind(first, second)) 