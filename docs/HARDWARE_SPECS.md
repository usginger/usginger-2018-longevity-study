# 🔬 Hardware Component List: DIY Controlled Stasis Chamber

**Project:** USGinger 2018 Longevity Study  
**Document:** Bill of Materials & System Architecture  
**Version:** 1.0.0  

This document lists the hardware components and wiring layouts needed to build an automated, controlled stasis chamber. This chamber handles the precise dehydration curves and preservation climate required for 8-Year Metabolic Stasis.

---

## 📦 Bill of Materials (BOM)

### 1. Microcontroller & Automation Core
* **Core Brain:** Raspberry Pi 4 (2GB RAM) or Arduino Uno R4 Minima.
* **User Interface:** 7-inch IPS Touchscreen Panel (For live environmental readouts).
* **Power Supply:** 12V 5A DC Switching Power Adapter.

### 2. Environmental Sensors
* **Atmospheric Sensor:** DHT22 / AM2302 Sensor (Measures ambient humidity and temperature).
* **Core Moisture Sensor:** SparkFun Soil Moisture Sensor (Inserted into sample roots to track internal dehydration).

### 3. Climate Control Actuators
* **Air Circulation:** 2x Noctua NF-A12x25 12V PWM Fans (For continuous, gentle airflow).
* **Moisture Extraction:** 12V Peltier Module Thermo-electric Dehumidifier (Extracts moisture without heat spikes).
* **Chamber Casing:** Clear Polycarbonate Acrylic Chamber (300mm x 300mm x 500mm) with air-tight rubber gaskets.

### 4. Photobiomodulation (Metabolite Boosting)
* **UV-B Stress Array:** 290nm–315nm UV-B LED Strip (Programmed for brief pulses to safely stress roots, triggering antioxidant production before stasis).

---

## 💻 System Architecture Diagram

```text
┌────────────────────────────────────────────────────────┐
│               Air-Tight Acrylic Chamber                │
│                                                        │
│   ┌───────────────┐                  ┌─────────────┐   │
│   │  DHT22 Temp/  │                  │ PWM Intake  │   │
│   │  Humid Sensor │                  │     Fan     │   │
│   └───────┬───────┘                  └──────┬──────┘   │
│           │                                 │          │
│           ▼                                 ▼          │
│   ┌───────────────┐                  ┌─────────────┐   │
│   │ Raspberry Pi  │─────────────────►│ UV-B Light  │   │
│   │  Core Brain   │                  │  LED Array  │   │
│   └───────┬───────┘                  └─────────────┘   │
│           │                                            │
│           ▼                                            │
│   ┌───────────────┐                                    │
│   │ Peltier Dehum │                                    │
│   └───────────────┘                                    │
└────────────────────────────────────────────────────────┘
```

## 💻 Running the Automation Loop

To initialize the hardware environment tracking and launch the automated loop, run the controller file from the root directory:

```bash
python scripts/chamber_control.py
```

---

## 🛠️ Setup and Installation Instructions

1. Assemble the acrylic chamber chassis and mount the dual Noctua intake/exhaust fans.
2. Interface the DHT22 atmospheric sensor and moisture probes to the Raspberry Pi GPIO pins.
3. Route the 12V Peltier module through a relay switch controlled by the core microprocessor.
4. Clone this repository and execute the upcoming automation scripts to begin climate control calibration.
5. This repository is for open-source scientific research, educational, and documentation purposes only. The protocols described herein have not been evaluated by the Food and Drug Administration (FDA) [SA1]. This protocol is not intended to diagnose, treat, cure, or prevent any disease [SA1]. Consult a qualified healthcare professional before beginning any new supplement or biohacking regimen [SA1].
