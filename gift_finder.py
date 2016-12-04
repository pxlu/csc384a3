import sys
from cspbase import *
from propagators import *
import itertools
import traceback

def test_run():
    import gift_finder_csp as gfc
    import orderings as orderings
    import process_data as pd

    gift_items_data = pd.main()

    # should have a prompt that prompts user for input
    # stub the user response object for now.
    spec = lambda: None
    spec.age = 6
    spec.season = "Winter"

    # turn string into numbers
    for item in gift_items_data:
        item.rec_age = float(item.rec_age[:-1])
        item.price = float(item.price[1:])

    csp, var = gfc.gift_finder_csp_model(gift_items_data, spec)

    # print(model)
    # print(var)

    # lister = []
    #
    # for i in range(len(var)):
    #     lister.append(var[i].cur_domain())
    # print(lister)

    solver = BT(csp)
    solver.bt_search(prop_BT, orderings.ord_expensive_first, orderings.val_always_select)

    print(var)


def main():
    test_run()

if __name__=="__main__":
    main()
