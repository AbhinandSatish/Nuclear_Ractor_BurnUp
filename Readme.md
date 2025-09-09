# Nuclear Reactor Burnup Simulation  

This repository contains a Python-based framework for modeling **nuclear fuel burnup and transmutation** using **Bateman equations** and neutron reaction networks. The code simulates the time evolution of isotopic concentrations in uranium-based reactor fuel under irradiation, providing insights into fuel depletion, actinide buildup, and long-term isotopic inventories.  

The project was developed as part of a training program at **Indira Gandhi Centre for Atomic Research (IGCAR)**. It validates trends against **ORIGEN2** calculations while providing an open and simplified implementation.  

---

## 📂 Repository Contents  

- `U-238_Burnup Model.py` – Main Python script implementing the ODE solver and burnup model.  
- [`Abhinand Satish Final Report.pdf`](./Abhinand%20Satish%20Final%20Report.pdf) – Full project report with theory, methodology, validation, and results.  
- [`Abhinand Saitsh - Uranium Transmutation decay chain - Presentation (2).pptx`](./Abhinand%20Saitsh%20-%20Uranium%20Transmutation%20decay%20chain%20-%20Presentation%20(2).pptx) – Presentation slides summarizing the project.  

---

## 🔬 The Process  

1. **Model Basis**  
   - Uses **Stacey’s Nuclear Reactor Physics** fuel depletion–transmutation–decay equations.  
   - Implements 19 coupled ODEs representing uranium, neptunium, plutonium, and americium isotopes.  
   - Accounts for decay, neutron capture, fission, and (n,2n) reactions.  

2. **Inputs**  
   - Initial isotopic masses (grams).  
   - Neutron flux spectrum (read from `Flux.txt`).  
   - Total flux value and interval fractions to model variable irradiation.  
   - Time intervals, step size, and units.  

3. **Solver**  
   - Uses `scipy.integrate.solve_ivp` with **BDF** method for stiff ODEs.  
   - Adaptive time-stepping ensures numerical stability.  
   - Converts atom densities → grams for interpretation.  

4. **Outputs**  
   - Time-dependent isotope concentrations.  
   - Final isotope inventory (grams).  
   - Plots showing depletion and transmutation trends.  

---

## ⚙️ Setup  

### Prerequisites  
Make sure you have Python 3.8+ and the following libraries installed:  

```bash
pip install numpy pandas scipy matplotlib
```

### Clone Repository  
```bash
git clone https://github.com/AbhinandSatish/Nuclear_Ractor_BurnUp.git
cd Nuclear_Ractor_BurnUp
```

---

## ▶️ Running the Simulation  

1. **Prepare Input Files**  
   - `Flux.txt` – multigroup neutron flux values (175 energy groups).  
   - Input file (e.g., `input1.txt`) specifying isotopes, masses, time intervals, flux, etc. Example:  

   ```
   Isotopes : U235, U238
   Isotope masses (g) : 71.0, 9929.0
   Time units : d
   Time intervals : 180, 60, 180, 60, 180, 60
   Time step : 10
   Flux fractions : 1.0E+00, 1.0E-10, 1.0E+00, 1.0E-10, 1.0E+00, 1.0E-10
   Total flux : 8.0E+15
   ```

2. **Run Model**  
   From the terminal:  

   ```bash
   python "U-238_Burnup Model.py" input1.txt
   ```

   Replace `input1.txt` with your desired input file.  

3. **Outputs**  
   - Final isotope concentrations (printed and saved).  
   - Plots of isotopic evolution over irradiation periods.  

---

## 📊 Example Cases  

- **Input 1:** Natural uranium cycle (`U235`, `U238`).  
- **Input 2:** Plutonium cycle (`Pu239–Pu242`).  
- **Input 3:** Mixed fuel composition (U + Pu).  

Results show similar **trends** compared to ORIGEN2, validating the model, though absolute values differ due to simplified reaction networks.  

---

## 📑 References  

- Abhinand Satish, *Simulation and Modelling of Uranium Burnup Using Neutron Reaction Networks and ODEs*, [Final Report (PDF)](./Abhinand%20Satish%20Final%20Report.pdf).  
- Abhinand Satish, *Modeling Nuclear Fuel Burnup Using Bateman Equations*, [Presentation (PPTX)](./Abhinand%20Saitsh%20-%20Uranium%20Transmutation%20decay%20chain%20-%20Presentation%20(2).pptx).  
- Stacey, W. M. *Nuclear Reactor Physics*.  

---

## 🔮 Future Work  

- Extend model to include additional reactions: (n,α), (n,p), spontaneous fission, delayed neutron emission.  
- Incorporate radiotoxicity indices and decay heat calculations.  
- Benchmark against SCALE/ORIGEN datasets for validation.  
