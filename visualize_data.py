import os
import matplotlib.pyplot as plt
import pandas as pd

# 1. Setup mock longevity data based on the 9-year study
data = {
    "Year": [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026],
    "Gingerol_Stability_Pct": [100.0, 99.8, 99.5, 99.2, 99.0, 98.7, 98.5, 98.2, 98.0],
    "Turmeric_Curcumin_Pct": [100.0, 99.9, 99.6, 99.4, 99.1, 98.9, 98.6, 98.4, 98.1],
}

df = pd.DataFrame(data)

# 2. Create the trend visualization plot
plt.figure(figsize=(10, 5))
plt.plot(
    df["Year"],
    df["Gingerol_Stability_Pct"],
    marker="o",
    linewidth=2,
    label="Active Gingerols (%)",
    color="#e67e22",
)
plt.plot(
    df["Year"],
    df["Turmeric_Curcumin_Pct"],
    marker="s",
    linewidth=2,
    label="Curcuminoids (%)",
    color="#f1c40f",
)

# 3. Add styling and labels
plt.title("USGinger 9-Year Botanical Stasis Stability Trends", fontsize=14, pad=15)
plt.xlabel("Study Year", fontsize=12)
plt.ylabel("Retention / Compound Integrity (%)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.ylim(90, 105)
plt.legend(loc="lower left")

# 4. Save the generated chart image locally
output_image = "stasis_stability_chart.png"
plt.savefig(output_image, dpi=300, bbox_inches="tight")
print(f" Success: Visualization saved as '{output_image}'")
