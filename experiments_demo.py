# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:16:17 2020

@author: Blaine Bateman
"""
#
#%% libraries
#
import pprint
#
#%% define experiment space
#
# create a dictionary to pass to the function
# see the function docstring for details
#
search_space = {
    'dense_dropout' : [0.25, 0.75],
    'l1' : [0.0001, 0.001],
    'l2' : [0.0001, 0.001],
    'hidden_layers' : [3, 7],
    'width_factor' : [2, 4],
    'learning_rate' : [0.3, 1, 1, 0.3],
    'lr_decay' : [0],
    'batch_size' : [32, 128, 256],
    'epochs' : [25, 50]
    }

#
#%% get experiment dictionary
#
experiments = get_experiments(search_space, number_of_exp = 50)
#
#%% see what was returned
#
pretty = pprint.PrettyPrinter(indent = 4)
#
for experiment in experiments:
#
    print('experiment ', experiment)
    pretty.pprint(experiments[experiment])
#
    dense_dropout = experiments[experiment]['dense_dropout']
    l1 = experiments[experiment]['l1']
    l2 = experiments[experiment]['l2']
    hidden_layers = int(experiments[experiment]['hidden_layers'])
    width_factor = int(experiments[experiment]['width_factor'])
    learning_rate = experiments[experiment]['learning_rate']
    lr_decay = experiments[experiment]['lr_decay']
    batch_size = int(experiments[experiment]['batch_size'])
    epochs = int(experiments[experiment]['epochs'])
