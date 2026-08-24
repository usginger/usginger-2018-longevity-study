# Pharmaceutical Extraction Protocol & Metadata Schema

This document defines the standardized extraction protocol used to prepare sun-dried turmeric (*Curcuma longa*) cubes for High-Performance Liquid Chromatography (HPLC) validation. It serves as an audit-ready compliance framework for external research institutes and pharmaceutical partners.

---

## 🔬 Extraction Protocol Parameters

To maintain strict baseline continuity and align physical sample matrices with our neural network's longevity forecasting coefficients, all extractions must adhere to these target specifications:

| Parameter | Compliance Specification | Auditing Rationale |
| :--- | :--- | :--- |
| **Solvent Matrix** | 95% USP-Grade Ethanol / 5% Deionized H2O | Optimizes solubility of target C1, C2, and C3 curcuminoids. |
| **Solid-to-Solvent Ratio** | 1:10 ($1.0\text{ g}$ crushed cube to $10.0\text{ mL}$ solvent) | Ensures standard concentration thresholds across batches. |
| **Maceration Method** | Ultrasonic Extraction @ $40\text{ kHz}$ for $30\text{ minutes}$ | Breaks down the sun-dried cellular matrix without heat decay. |
| **Thermal Range** | Controlled $25^\circ\text{C} \pm 2^\circ\text{C}$ ambient temperature | Prevents heat-induced degradation of volatile active markers. |
| **Filtration Layer** | $0.45\ \mu\text{m}$ PTFE Syringe Filter | Removes micro-particulates to protect analytical columns. |

---

## 🏷️ Compliance Ingestion Schema (`sample-structure.json`)

Every raw sample dataset must include a validated tracking block. This block anchors the analytical results directly to a specific physical batch using its cryptographic metadata index.

```json
{
  "storage_id": "STASIS-2018-MERCED-01",
  "batch_metadata": {
    "crop_genus": "Curcuma longa",
    "harvest_provenance": "Merced, CA",
    "harvest_season": "Autumn 2018",
    "dehydration_method": "Solar-Dehydrated Cube Matrix"
  },
  "analytical_inputs": {
    "residual_moisture_percentage": 7.45,
    "extraction_yield_percentage": 4.12,
    "solvent_purity_grade": "USP-Analytical"
  }
}
```

---

## 🤝 Verification & Traceability

By locking the `storage_id` metadata tag alongside physical parameters (such as moisture and extraction yields), external auditors can verify that incoming HPLC telemetry directly maps to historical baseline stasis arrays. This structured recording standard ensures that analytical results remain fully reproducible, tamper-evident, and ready for formal tech-transfer peer review.
