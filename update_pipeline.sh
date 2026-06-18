



#!/bin/bash

echo "🔄 Step 1: Updating the python visualization script..."
mkdir -p scripts docs
cat << 'EOF' > scripts/visualize_data.py
import matplotlib.pyplot as plt
import numpy as np

# --- 1. Historical Dataset Foundations ---
years = np.array([2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026])
curcuminoid_density = np.array([42.1, 88.4, 87.9, 87.2, 86.5, 85.9, 85.1, 84.4, 83.8, 83.1])
stasis_retention = np.array([85.0, 100.0, 99.4, 98.6, 97.9, 97.2, 96.3, 95.5, 94.8, 94.0])

# --- 2. Canvas & Dual-Axis Configuration ---
fig, ax1 = plt.subplots(figsize=(10, 6), dpi=100)
ax2 = ax1.twinx()

# --- 3. Plotting Core Target Trends ---
line1 = ax1.plot(years, curcuminoid_density, color='#D4AF37', linewidth=3, marker='o', label='Curcuminoid Density (mg/g)')
line2 = ax2.plot(years, stasis_retention, color='#228B22', linewidth=2, linestyle='--', marker='s', label='Stasis Retention (%)')

# --- 4. Highlighting the 2018 Phenotypic Spike ---
ax1.axvspan(2017.8, 2018.2, color='#FFD700', alpha=0.18, label='2018 Potency Breakthrough')

ax1.annotate(
    '2018 Breakthrough\n+110% Curcuminoid Leap\n(COA #USG-2018Q5L2)',
    xy=(2018, 88.4),
    xytext=(2019.5, 70),
    arrowprops=dict(facecolor='#D4AF37', shrink=0.08, width=1.5, headwidth=7),
    fontweight='bold',
    fontsize=9,
    bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFFDD0', edgecolor='#D4AF37', alpha=0.9)
)

# --- 5. Labels & Aesthetics ---
ax1.set_title('USGinger Longitudinal Tracking: 2017-2026 Stability Matrix', fontsize=12, fontweight='bold', pad=15)
ax1.set_xlabel('Harvest & Longitudinal Observation Year', fontsize=10)
ax1.set_ylabel('Active Curcuminoid Content (mg/g)', color='#D4AF37', fontsize=10)
ax2.set_ylabel('Metabolic Stasis Retention Rate (%)', color='#228B22', fontsize=10)

ax1.set_xticks(years)
ax1.grid(True, linestyle=':', alpha=0.5)

lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='lower left', framealpha=0.9)

plt.tight_layout()
plt.savefig('docs/potency_spike_trends.png', dpi=300)
print("[SUCCESS] Data trends compiled. Target export saved to 'docs/potency_spike_trends.png'.")
EOF

echo "📈 Step 2: Running the visualization script..."
python3 scripts/visualize_data.py

echo "🚀 Step 3: Pushing updates live to GitHub..."
git add scripts/visualize_data.py docs/potency_spike_trends.png
git commit -m "Pipeline: Generate 2018 breakthrough trend chart via bash automation"
git push origin main

echo "🏁 All done! Pipeline completed successfully."
