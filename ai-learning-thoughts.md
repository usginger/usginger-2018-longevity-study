# AI Learning Thoughts

This document captures the core architectural insights, constraints, and engineering observations gathered while adapting the **2018 Ginger Longevity Study** data to forecast the longevity ratio of Merced-harvested turmeric roots.

---

## 🔬 Core Insights

### 1. Stasis Transferability
Cross-genus transfer learning between *Zingiber officinale* (ginger) and turmeric variants demonstrates highly stable behavior. The model successfully maps latent metabolic features across both plants. This proves that the biological degradation curves share foundational mathematical properties despite taxonomic differences.

### 2. Overfitting Risks & Regularization
The 8-year ginger baseline provides an entirely noise-free stasis environment. 
* **The Problem**: The neural network initially overfitted to these ideal laboratory conditions.
* **The Fix**: Integrating highly variable, localized field data from Merced, CA requires aggressive dropout rates and weight regularization to ensure the model generalizes well to real-world agricultural environments.

### 3. Feature Weight Distribution
Sensitivity analysis reveals that the 8-year metabolic stasis coefficient holds the heaviest mathematical weight in the network. This structural baseline vector impacts long-term forecasting accuracy far more than localized, seasonal soil chemistry vectors.

---

## 🧠 Neural Network Activation Functions

To properly model the complex, non-linear biological degradation curves of the rhizome data, the architecture utilizes three specific activation functions across different layer stages:

### 1. Swish (Hidden Layers)
* **Formula**: $f(x) = x \cdot \sigma(\beta x)$
* **Application**: Applied across all deep feature-extraction layers. 
* **Rationale**: Swish outperforms ReLU in deep networks mapping biological stasis by maintaining a smooth, non-monotonic curve. This prevents the "dying neuron" problem when processing highly zero-skewed nutrient degradation vectors from the Merced field data.

### 2. Leaky ReLU (Transfer Learning Alignment Layer)
* **Formula**: $f(x) = \max(\alpha x, x)$ where $\alpha = 0.01$
* **Application**: Utilized specifically in the bridge layers where ginger baseline weights are adapted to turmeric variables.
* **Rationale**: By allowing a small, non-zero gradient when the unit is inactive, Leaky ReLU preserves low-level ambient data (such as trace soil chemistry values) that standard ReLU would otherwise discard.

### 3. Sigmoid (Output Layer)
* **Formula**: $f(x) = \frac{1}{1 + e^{-x}}$
* **Application**: Final layer computation.
* **Rationale**: Because the longevity ratio is strictly bounded as a value between `0.0` (complete degradation) and `1.0` (perfect metabolic stasis), the Sigmoid function scales the final forecasting array output into a precise, readable percentage.

---

## 📈 Future Training Goals

* **Hyperparameter Tuning**: Optimize the regularization framework to better balance the noise-free control baseline with volatile environmental data.
* **Expanding Variants**: Test the transfer learning model against other rhizome data structures to validate universal scaling laws.
* **Real-time Validation**: Feed live degradation telemetry from current Merced harvest cycles back into the training loop to dynamically reduce Mean Absolute Error (MAE).
