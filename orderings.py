import random

'''
This file will contain different variable ordering heuristics to be used within
bt_search.

var_ordering == a function with the following template
    ord_type(csp)
        ==> returns Variable

    csp is a CSP object---the heuristic can use this to get access to the
    variables and constraints of the problem. The assigned variables can be
    accessed via methods, the values assigned can also be accessed.

    ord_type returns the next Variable to be assigned, as per the definition
    of the heuristic it implements.

val_ordering == a function with the following template
    val_ordering(csp,var)
        ==> returns [Value, Value, Value...]

    csp is a CSP object, var is a Variable object; the heuristic can use csp to access the constraints of the problem, and use var to access var's potential values.

    val_ordering returns a list of all var's potential values, ordered from best value choice to worst value choice according to the heuristic.

'''

def ord_expensive_first(csp):
    # higher chance that we can quickly go through combinations
    # with this variable early on
    highestCost = 0     # all items must have cost > 0
    varSelected = None

    for var in csp.get_all_unasgn_vars():
        if var.properties.price > highestCost:
            varSelected = var

    return varSelected

def val_always_select(csp, var):
    # always try to select the item until we reach a point
    # where that combination is no longer possible.
    if var.cur_domain_size() == 2:
        return [1, 0]
    return [0]
