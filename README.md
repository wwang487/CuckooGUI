# CuckooGUI
## Overview
This repository contains the simulation framework for modeling host–parasite coevolution, with a focus on brood parasitism dynamics between cuckoos and reedbirds. The model is a stochastic reinforcement model, capturing both population-level dynamics and behavioral adaptation under varying ecological scenarios. It allows for long-term simulations with user-defined inputs, enabling exploration of evolutionary strategies and survival outcomes.

👉 Figure 1 (workflow diagram): 

![alt text](https://github.com/wwang487//CuckooGUI/blob/main/Figure1.jpg?raw=true)

## Reproducing Results and Running Custom Simulations
To reproduce our results or run custom simulations, follow the steps below.

### 1. Preparing Input Data
Ensure your input data follows the format of the Excel files in the Cuckoo_Inputs and Reedbird_Inputs folders. These define the initial conditions for cuckoos (parasites) and reedbirds (hosts). Sample files from our published simulations are included.

### 2. Configuring the Script (Interaction.py)
Customize the simulation by modifying:

Lines 18–23: Set paths for input and output directories.

Lines 25–28: Specify the input Excel files for cuckoo and reedbird scenarios.

Line 30:

'a' — Simulates population trends (cf. Figure 6).

'b' — Evaluates behavioral adaptation and survival strategies (cf. Figure 7).

Line 43:

'f' — Disables cuckoo "backup" behavior.

't' — Enables backup behavior.

Lines 49–50: Configure number of simulation years and repetitions (each run = one reproductive cycle).

### 3. Understanding Stochastic Variability
Due to stochastic elements in the model, outcomes will vary across runs. Running multiple simulations (e.g., 30) reveals robust average patterns.

### 4. Comparing Results
Sample outputs are available at:
👉 https://github.com/wwang487/CuckooData.git

If using Simulation_Example_Inputs:

For Line 30 = 'a' (population trends):

Line 43 = 'f' → compare with Cuckoo_12_Reedbird_1_a_fl

Line 43 = 't' → compare with Cuckoo_12_Reedbird_1_a_tr

For Line 30 = 'b' (behavioral adaptation):

Compare with Cuckoo_12_Reedbird_1_b_tr

### 5. Further Questions
For any inquiries, please contact wwang487@wisc.edu.
