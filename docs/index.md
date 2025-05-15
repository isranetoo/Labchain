# Labchain

Labchain is a simulator for chemistry laboratory experiments. It allows you to add reagents, set the temperature, and calculate the theoretical yield of a chemical reaction in a simple and intuitive way.

## Main Features
- Add reagents with name and amount (in mol)
- Set the experiment temperature (°C)
- Automatic calculation of theoretical yield based on reagents and temperature

Ideal for students, teachers, and chemistry enthusiasts who want to simulate experiments quickly and didactically.

## Quick Example

Here's how you can use Labchain in Python:

```python
from labchain.simulator import Simulator

# Create a simulator with a specific temperature
sim = Simulator(temperature=30)

# Add reagents (name, amount in mol)
sim.add_reagent("Acetic Acid", 0.5)
sim.add_reagent("Ethanol", 0.5)

# Calculate the theoretical yield
result = sim.calculate_yield()
print(f"Theoretical yield: {result:.2f}%")
```

**Expected output:**
```
Theoretical yield: 11.25%
```

This example shows how to set up an experiment, add reagents, and calculate the yield easily.
