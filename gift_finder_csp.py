'''
Construct and return optimal gift finder CSP models.
'''

from cspbase import *
import itertools

def gift_finder_csp_model(gift_list, user_specification):
    '''Return a CSP object representing a gift finder CSP problem along
       with an array of variables for the problem. That is return

       gift_finder_csp, variable_array

       where variable_array is a list of gift variables

       such that variable_array[i] is the Variable (object) built
       to represent whether the gift is selected for a valid representation
       of combination of gifts

       The input gift list is specified as a list of gifts (a3_classes
       ItemProfile object).

       This routine returns a gift_finder_csp model which consists of
       a variable for each gift item, with domain equal to {0,1}, with
       0? being the initial value of the cell in the board.

       This model also contains unary, binary, and n-ary constraints
       between all relevant variables. Based on condition specified
       by user at start of the program and inheriant relationship
       between properties of gift items.
    '''

    variable_array = []

    for item in gift_list:
        variable_array.append(
            Variable(str(item.name), item, [0, 1])
        )

    model = CSP("Optimal Gift Finder", variable_array)
    va = variable_array

    # unary constraints
    for i in range(len(variable_array)):
        # Minimum Age (unary)
        constraint = Constraint('min age for item:' + va[i].properties.name, [va[i]])
        satisfying_tuples = [(0,)]
        if (va[i].properties.rec_age <= user_specification.age):
            satisfying_tuples.append((1,))
        constraint.add_satisfying_tuples(satisfying_tuples)
        model.add_constraint(constraint)

        # Season (unary) - items must belong to season specified.
        constraint = Constraint('seasonal item:' + va[i].properties.name, [va[i]])
        satisfying_tuples = [(0,)]
        if (va[i].properties.seasonal == None or
            user_specification.season in va[i].properties.seasonal
        ):
            satisfying_tuples.append((1,))
        constraint.add_satisfying_tuples(satisfying_tuples)
        model.add_constraint(constraint)

    return model, variable_array
