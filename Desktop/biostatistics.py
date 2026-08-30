"""
Descriptive statistics for a small biological dataset.

Example data: hypothetical urinary metabolite concentrations (ug/L).
Replace the list with your own measurements.
"""

def mean(values):
    return sum(values) / len(values)

def variance(values, sample=True):
    m = mean(values)
    n = len(values)
    denom = n - 1 if sample and n > 1 else n
    return sum((x - m) ** 2 for x in values) / denom

def std_dev(values, sample=True):
    return variance(values, sample) ** 0.5

def summarise(values, label="dataset"):
    print(f"\nSummary for {label}")
    print(f"n      = {len(values)}")
    print(f"min    = {min(values):.4f}")
    print(f"max    = {max(values):.4f}")
    print(f"mean   = {mean(values):.4f}")
    print(f"var    = {variance(values):.4f}")
    print(f"sd     = {std_dev(values):.4f}")

if __name__ == "__main__":
    concentrations = [1.2, 2.8, 0.9, 3.4, 1.7, 2.1, 4.0, 1.5, 2.6, 3.1]
    summarise(concentrations, "hypothetical metabolite (ug/L)")