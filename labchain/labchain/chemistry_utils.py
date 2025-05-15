from typing import List, Dict

from labchain.simulator import Reagent

def sum_reagents(reagents: List[Reagent]) -> Dict[str, float]:
    """
    Sum the quantities of reagents with the same name.

    Args:
        reagents (List[Reagent]): List of reagent objects.

    Returns:
        Dict[str, float]: Dictionary with reagent names as keys and total quantities as values.
    """
    totals = {}
    for reagent in reagents:
        if reagent.name in totals:
            totals[reagent.name] += reagent.amount
        else:
            totals[reagent.name] = reagent.amount
    return totals