random_search

the function get_experimetnts takes a dictionary of hyperparameters  
and given a number of experiments to return, populates random  
search values within the provided parameter ranges in eaach experiment  
  
the passed-in dictionary consists of parameter names and lists of values  
for each parameter:  

&nbsp;&nbsp;&nbsp;&nbsp;if there is a single value:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;it is used and returned for every experiment  
&nbsp;&nbsp;&nbsp;&nbsp;if thre are two values:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;they are searched with random.uniform  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to generate a value for a given experiment  
&nbsp;&nbsp;&nbsp;&nbsp;if there is a list of values:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the list is searched with random.sample  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to generate a value for a given experiment  
  
See the function docstring and the accompanying experiments_demo for full details  