random_search

the function get_experimetnts takes a dictionary of hyperparameters
and given a number of experiments to return, populates random
search values within the provided parameter ranges in eaach experiment

the passed-in dictionary consists of parameter names and lists of values
for each parameter:
    if there is a single value:
        it is used and returned for every experiment
    if thre are two values:
        they are searched with random.uniform
        to generate a value for a given experiment
    if there is a list of values:
        the list is searched with random.sample
        to generate a value for a given experiment

See the function docstring and the accompanying experiments_demo for full details