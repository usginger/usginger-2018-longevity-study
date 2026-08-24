# 🌿 AI Longevity Forecasting Model: Merced Turmeric Study

This repository hosts a production-grade deep learning framework that leverages baseline data from the **2018 Ginger Longevity Study** to forecast the longevity ratio and metabolic stasis of solar-dehydrated turmeric (*Curcuma longa*) cubes harvested in Merced, CA.

---

## 🚀 Repository Architecture

The project is structured to enforce separation between analytical documentation, strict schema blueprints, and core PyTorch operational scripts:

*   **`src/model.py`**: Neural network architecture featuring non-linear Swish and Leaky ReLU activations tailored to complex agricultural matrices.
*   **`src/train.py`**: Optimization pipeline running AdamW and Huber Loss, incorporating mathematical layer-locking to safeguard historical ginger stasis controls.
*   **`ai-learning-thoughts.md`**: Core engineering notes covering transfer learning mechanics, model convergence curves, and regularization targets.
*   **`extraction-protocol.md`**: Compliance framework documenting solvent ratios and ultrasonic preparation parameters to ensure audit readiness.
*   **`hplc-analytical-framework.md`**: Standardized data ingestion schemas optimized to process raw quantitative data from external Reversed-Phase C18 chromatography equipment.

---

## 📊 Analytical Core Features

### 1. Mathematical Baseline Continuity
To preserve the 8-year noise-free stasis variables, deep model layers are structurally frozen (`requires_grad = False`). This ensures that highly volatile seasonal environmental factors from field collections cannot distort or wash away established biological parameters.

### 2. Pharmaceutical Integration Layer
The data schema is optimized to map absolute quantification vectors from target curcuminoid peaks directly into the tensor training loop:

```text
[Sample_ID] -> [Moisture_Content_%] -> [Peak_Area_C1] -> [Peak_Area_C2] -> [Peak_Area_C3] -> [Predicted_Stasis_Ratio]
```

---

## 🛠️ Local Environment Initialization

Install the required core dependencies to compile the model layout locally:

```bash
pip install -r requirements.txt
python3 src/train.py
```


