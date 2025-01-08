'''
    Given an array a of integers and the corresponding probabilities their occurence,
    define a funtion which return one of the integers at each call with the respect
    to the probabilities.
'''
import itertools, random, bisect

def nonuniform_random_generator(probabilites, values):
    accumulated_probabilities_range = list(itertools.accumulate(probabilites))
    interval_idx = bisect.bisect(accumulated_probabilities_range, random.random())
    return values[interval_idx]