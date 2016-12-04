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
        constraint = Constraint('min age for item: ' + va[i].properties.name, [va[i]])
        satisfying_tuples = [(0,)]
        if (va[i].properties.rec_age <= user_specification.age):
            satisfying_tuples.append((1,))
        constraint.add_satisfying_tuples(satisfying_tuples)
        model.add_constraint(constraint)

        # Season (unary) - items must belong to season specified.
        constraint = Constraint('seasonal item: ' + va[i].properties.name, [va[i]])
        satisfying_tuples = [(0,)]
        if (va[i].properties.seasonal == "Any" or
            user_specification.season in va[i].properties.seasonal
        ):
            satisfying_tuples.append((1,))
        constraint.add_satisfying_tuples(satisfying_tuples)
        model.add_constraint(constraint)

    # binary constraints
    for i in range(len(variable_array)):
        for j in range(i+1, len(variable_array)):
            # Indoor (binary) - if we choose an indoor item, everything else
            # must also be an indoor item or both.
            constraint = Constraint('indoor item: ' + va[i].properties.name, [va[i], va[j]])
            satisfying_tuples = [(0,0), (0,1), (1,0)]
            if (va[i].properties.is_indoor == None or
                va[j].properties.is_indoor == None or
                (va[i].properties.is_indoor == va[j].properties.is_indoor)
            ):
                satisfying_tuples.append((1,1))
            constraint.add_satisfying_tuples(satisfying_tuples)
            model.add_constraint(constraint)

            # Entertainment (binary) - if we choose an entertainment item,
            # everything else must also be it or both.
            constraint = Constraint('entertainment item: ' + va[i].properties.name, [va[i], va[j]])
            satisfying_tuples = [(0,0), (0,1), (1,0)]
            if (va[i].properties.is_entertainment == None or
                va[j].properties.is_entertainment == None or
                (va[i].properties.is_entertainment == va[j].properties.is_entertainment)
            ):
                satisfying_tuples.append((1,1))
            constraint.add_satisfying_tuples(satisfying_tuples)
            model.add_constraint(constraint)

    # Brand competition within category (n-ary)

    # Price (n-ary) - combination of items must not be over price specified
    constraint = Constraint('Max price', va)
    constraint.add_satisfying_tuples(generate_satisfying_price_tuples(va, user_specification.price))
    model.add_constraint(constraint)

    return model, variable_array

def generate_satisfying_price_tuples(va, max_price):
    domain = [var.cur_domain() for var in va]
    satisfying_tuples = []
    print("creating valid permutations of price assignments, this may take a while..")

    # generate permutation of domain values to assign
    for assignment in itertools.product(*domain):
        if (is_below_price(va, assignment, max_price)):
            print(assignment)
            satisfying_tuples.append(assignment)
    return satisfying_tuples

def is_below_price(va, assignment, price):
    ls = list(assignment)

    for i in range(len(ls)):
        if (ls[i] == 1):
            price -= va[i].properties.price

    if (price < 0):
        return False
    return True
