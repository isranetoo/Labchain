import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from labchain.simulator import Reagent
from labchain.chemistry_utils import sum_reagents

def test_sum_reagents():
    reagents = [
        Reagent("Water", 1.0),
        Reagent("Water", 2.0),
        Reagent("Ethanol", 0.5),
    ]
    result = sum_reagents(reagents)
    assert result == {"Water": 3.0, "Ethanol": 0.5}