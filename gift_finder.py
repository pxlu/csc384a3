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
    spec.age = 15
    spec.season = "Winter"
    spec.price = 50

    # normalize data
    for item in gift_items_data:
        item.rec_age = float(item.rec_age[:-1])
        item.price = float(item.price[1:])

        if item.is_indoor == '':
            item.is_indoor = None
        else:
            item.is_indoor = item.is_indoor != "No"

        if item.is_entertainment == '':
            item.is_entertainment = None
        else:
            item.is_entertainment = item.is_entertainment != "No"

    csp, var = gfc.gift_finder_csp_model(gift_items_data, spec)

    solver = BT(csp)
    solver.bt_search(prop_BT, orderings.ord_expensive_first, orderings.val_always_select)


def main():
    test_run()

if __name__=="__main__":
    main()
