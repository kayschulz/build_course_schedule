import numpy as np
import scipy.stats as stats
import math
import pandas as pd


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
    """Calculates the sample size for a given margin of error,
    confidence level, and dictionary of variances and sizes"""
    num = sum([(vars_and_n[i][1] - 1) * vars_and_n[i][0]
               for i in vars_and_n.keys()])
    den = sum([vars_and_n[i][1] for i in vars_and_n.keys()]) - len(vars_and_n)
    pooled_std = np.sqrt(num/den)
    n = 2 * (z * pooled_std / moe)**2
    n = math.ceil(n)  # round up because we can't have a decimal
    return n


def clean_df(df):
    """Add total counts column to dataframe. Remove rows that are not
    LEC or SEM or have 0 students"""
    df['total_count'] = sum([df['a_count'], df['ab_count'], df['b_count'],
                             df['bc_count'], df['c_count'], df['d_count'],
                             df['f_count']])
    df = df[df['section_type'] != 'IND']
    df = df[df['section_type'] != 'FLD']
    df = df[df['section_type'] != 'LAB']
    df = df[df['section_type'] != 'DIS']
    df = df[df['total_count'] != 0]
    return df
