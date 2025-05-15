# API - Reference

Welcome to the Labchain API Reference! Here you will find clear and concise information about the main classes and methods that power the Labchain chemistry experiment simulator.

## Simulator
The `Simulator` class is used to create and manage experiments. You can add reagents, set the temperature, and calculate the theoretical yield of your reactions.

### Example
```python
from labchain.simulator import Simulator

sim = Simulator(temperature=40)
sim.add_reagent("Hydrogen Peroxide", 0.2)
sim.add_reagent("Potassium Iodide", 0.1)
yield_percent = sim.calculate_yield()
print(f"Yield: {yield_percent:.2f}%")
```
**Expected output:**
```
Yield: 3.00%
```

## Reagent
The `Reagent` class represents a chemical reagent, including its name and amount (in mol). Usually, you don't need to create `Reagent` objects directly; use `Simulator.add_reagent()` instead.

## Chemistry Utilities

A função `sum_reagents` permite somar as quantidades de reagentes com o mesmo nome em uma lista. Isso é útil para consolidar reagentes repetidos em experimentos.

### Exemplo de uso
```python
from labchain.simulator import Reagent
from labchain.chemistry_utils import sum_reagents

reagents = [
    Reagent("Water", 1.0),
    Reagent("Water", 2.0),
    Reagent("Ethanol", 0.5),
]
result = sum_reagents(reagents)
print(result)
```
**Saída esperada:**
```
{'Water': 3.0, 'Ethanol': 0.5}
```

Essa função facilita o controle dos reagentes totais em um experimento, tornando o processo mais simples para iniciantes.

---

Explore the automatic documentation below to understand how to use each component effectively:

::: labchain.simulator
