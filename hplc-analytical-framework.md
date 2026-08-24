# HPLC Analytical Framework & Screening Readiness

This document outlines the standardized data schema and chromatographic targets prepared for High-Performance Liquid Chromatography (HPLC) validation of sun-dried turmeric (*Curcuma longa*) cubes. 

---

## 🧪 Target Phytochemical Markers

The analytical pipeline is optimized to cross-reference our neural network's longevity forecasting coefficients with the absolute quantification of three primary curcuminoid vectors:

1. **Curcumin (C1)**: Primary target for metabolic stability mapping.
2. **Demethoxycurcumin (C2)**: Secondary matrix stabilizer.
3. **Bisdemethoxycurcumin (C3)**: Volatility control marker under solar-dehydration stress.

---

## 📋 Prepared Chromatographic Schema

To ensure seamless integration with institutional testing facilities, our data models assume the following reference baseline conditions:

| Parameter | Specification | Purpose / Rationale |
| :--- | :--- | :--- |
| **Stationary Phase** | Reversed-Phase C18 (e.g., 250 x 4.6 mm, 5 µm) | Maximizes resolution of hydrophobic rhizome compounds. |
| **Mobile Phase** | Isocratic Acetonitrile / 2% Acetic Acid (40:60 v/v) | Prevents peak tailing from complex sun-dried matrix sugars. |
| **Flow Rate** | 1.0 mL/min | Maintains peak baseline integrity for predictive modeling. |
| **Detection** | UV/Vis Spectrophotometry @ 425 nm | Maximizes signaling efficiency for targeted curcuminoids. |

---

## 📊 Data Ingestion Layer for External Partners

When an institution or pharmaceutical partner initiates deep analytical screening, the raw peak area outputs will map directly into our existing training architecture via this standardized data array layout:

```text
[Sample_ID] -> [Moisture_Content_%] -> [Peak_Area_C1] -> [Peak_Area_C2] -> [Peak_Area_C3] -> [Predicted_Stasis_Ratio]
```

This layout allows our PyTorch `LongevityForecastingModel` to immediately accept external quantitative validation weights, closing the loop between hardware testing and AI predictive learning.
