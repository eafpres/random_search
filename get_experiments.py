# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:11:27 2020

@author: Blaine Bateman
"""
#
#%% get experiments
#
def get_experiments(space_dict, number_of_exp):
    """populate a dictionary of hyperparameters
       across dimensions in space_dict
       for number_of_exp trials

       for each parameter:
           if there is a single value:
               it is used and returned for every experiment
           if thre are two values:
               they are searched with random.uniform
               to generate a value for a given experiment
           if there is a list of values:
               the list is searched with random.sample
               to generate a value for a given experiment
       for example:

           search_space = {
                'hyperparameter_1' : [0, 1, 2],
                'hpyerparameter_2' : [0.5, 1.5]}
           number_of_exp = 4
           get_experiments(search_space, number_of_exp)

           returns something like:

               {'exp_0': {'hyperparameter_1': 0, 'hpyerparameter_2': 1.451704640798038},
                'exp_1': {'hyperparameter_1': 2, 'hpyerparameter_2': 0.9641265687806964},
                'exp_2': {'hyperparameter_1': 0, 'hpyerparameter_2': 0.6768719701707783},
                'exp_3': {'hyperparameter_1': 1, 'hpyerparameter_2': 0.5655527538628148}}
    """
#
    import random
    experiments = dict()
    for i in range(number_of_exp):
        experiments.update({'exp_' + str(i) : dict()})
        for key in space_dict:
            if len(space_dict[key]) > 2:
                value = random.sample(space_dict[key], 1)[0]
            elif len(space_dict[key]) == 1:
                value = space_dict[key][0]
            else:
                value = random.uniform(space_dict[key][0], space_dict[key][1])
            experiments['exp_' + str(i)].update({key : value})
    return experiments
