# USGinger 2018 Longevity Study & Bio-Aging Protocol

[![License: MIT](https://shields.io)](https://opensource.org)
[![Status: Active Phase 1 Trials](https://shields.io)](https://github.com)


This repository contains the data, protocols, and automation tools for the **8-Year Metabolic Stasis Protocol** of California-grown *Curcuma longa* (turmeric) and ginger. By achieving zero potency loss over an 8-year span, this protocol provides a stable foundation for long-term anti-aging and anti-inflammatory research.

We are currently tracking open-source community data regarding the therapeutic impact of these stasis-preserved root capsules.

---

## 🔬 Phase 1 Trial Protocol

This protocol is optimized for long-term compound absorption, cellular stability, and mitigating systemic "inflammaging."

| Parameter | Specification |
| :--- | :--- |
| **Form Factor** | 200mg Metabolic-Stasis Ginger/Turmeric Capsules |
| **Frequency** | Exactly 1 capsule every two days (48-hour intervals) |
| **Timing** | Administered immediately following a hot breakfast |
| **Cycle Duration** | 14 Days (Two-week evaluation window) |

### Why a Hot Breakfast?
Stasis-preserved gingerols and curcuminoids are highly lipophilic (fat-soluble). Taking the capsule immediately after a warm meal containing healthy lipids triggers bile release, maximizing cellular bioavailability and reducing gastric irritation.

---

## 🎯 Targeted Applications & Tracking Metrics

Contributors are actively logging the impact of this 200mg alternating-day protocol on three core age-related and systemic ailments:

### 1. Metabolic Health (Diabetes Type I & II)
* **Target:** Mitigation of insulin resistance and reduction of oxidative stress on pancreatic beta cells.
* **Key Metrics:** Fasting blood glucose (mg/dL), post-prandial spikes, and 14-day average glucose stability.

### 2. Gut Health & Motility (Indigestion)
* **Target:** Acceleration of gastric emptying and reduction of chronic gut mucosal inflammation.
* **Key Metrics:** Bloating severity scale (1–10), post-meal transit comfort, and gut microbiome regularity.

### 3. Endocrine Support (Pre-Menopause)
* **Target:** Suppression of systemic inflammatory cytokines that trigger vasomotor symptoms.
* **Key Metrics:** Daily hot flash frequency, joint pain/stiffness tracking, and systemic fatigue scores.

---

## 💻 Repository Structure

```text
├── README.md               <- This overview and study roadmap
├── scripts/
│   └── dose_tracker.py     <- Automated 14-day trial schedule generator
└── data/
    ├── template.csv        <- Standardized data schema for user logs
    └── community_results/  <- Anonymous user-submitted trial data
```

---

## 📊 How to Participate & Contribute Data

We welcome anonymous data submissions from self-experimenters and independent researchers.

1. **Generate Your Schedule:** Run the `scripts/dose_tracker.py` tool to generate your exact 14-day calendar.
2. **Log Your Metrics:** Use the schema provided in `data/template.csv` to track your daily baselines and post-dose symptoms.
3. **Submit Data:** Submit an anonymous Pull Request adding your data log to the `data/community_results/` folder.

---

## ⚠️ Medical Disclaimer

*This repository is for open-source scientific research, educational, and documentation purposes only. The   Mandatory participant exclusions for the 200mg capsule trial include pregnancy/nursing, bleeding disorders, use of blood thinners, upcoming surgery, gallstones, and low blood pressure. Contraindications and drug interactions highlight risks for individuals with diabetes, those taking GI medications, and individuals on hormone therapies, emphasizing the need for monitoring blood sugar and avoiding empty-stomach consumption.protocols described herein have not been evaluated by the Food and Drug Administration (FDA). This protocol is not intended to diagnose, treat, cure, or prevent any disease. Consult a qualified healthcare professional before beginning any new supplement or biohacking regimen.*
