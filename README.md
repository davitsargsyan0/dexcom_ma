# **Dexcom Stelo Diffusion Analysis (Bass Model)**

## **Project Overview**
This project applies the **Bass Diffusion Model** to predict the adoption of **Dexcom Stelo**, an over-the-counter (OTC) continuous glucose monitoring (CGM) system designed for individuals with **Type 2 diabetes who are not on insulin**. The analysis leverages historical data from **Dexcom G-Series (G5, G6, G7)** and market trends to estimate future adoption in the **U.S. market**.

## **Methodology**
1. **Historical Data Analysis**
   - **Dexcom Revenue Data (2019-2023)** used to estimate past adoption trends.
   - **Global Diabetes Care Market Revenue (2016-2029)** as a reference for market potential.
   - **Dexcom Market Share (~25%)** estimated from industry reports.

2. **Market Potential Estimation (M) using Fermi’s Logic**
   - U.S. Population: ~330M
   - People with Diabetes: ~38M
   - Type 2 Diabetics (~90% of total): ~34M
   - Non-Insulin Type 2 Diabetics (~70% of Type 2): ~24M
   - Estimated adoption rate (~30%) → **Market Potential (M) ≈ 7.2M adopters**

3. **Bass Model Estimation**
   - **Innovation Rate (p):** ~0.235
   - **Imitation Rate (q):** ~0.235
   - **Market Potential (M):** ~7.2M (based on Fermi estimation)

4. **Prediction (2024-2035)**
   - Forecasting annual new adopters and cumulative adoption.
   - Analyzing early vs. late adoption trends.

## **Project Files**
- `bass_model_analysis.ipynb` → Jupyter Notebook with code and analysis.
- `bass_model_report.pdf` → Final project report.
- `README.md` → This file.
- `data/` → Folder containing:
  - `dexcom_revenue_2019_2023.csv`
  - `diabetes_market_revenue_2016_2029.csv`
  - `healthcare_growth_data.csv`

## **Installation & Requirements**
### **Dependencies**
Ensure you have the following Python libraries installed:
```bash
pip install numpy pandas scipy matplotlib
```

### **Running the Analysis**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/dexcom-stelo-bass-model.git
   ```
2. Navigate to the project folder:
   ```bash
   cd dexcom-stelo-bass-model
   ```
3. Run the Jupyter Notebook:
   ```bash
   jupyter notebook bass_model_analysis.ipynb
   ```

## **Results Summary**
- Adoption is expected to follow an **S-curve trend**.
- **2024-2026**: Slow initial adoption phase.
- **2027-2031**: Rapid growth as awareness increases.
- **2032-2035**: Market saturation with late adopters joining.

## **Future Work**
- Expand predictions for **global diffusion**.
- Incorporate **real-world sales data** post-2024 for model refinements.
- Analyze **insurance reimbursement effects** on adoption.

## **References**
- [Dexcom Stelo FDA Approval](https://investors.dexcom.com/news/news-details/2024/Stelo-by-Dexcom-First-Glucose-Biosensor-to-be-Cleared-by-FDA-as-Over-the-Counter/default.aspx)
- [TIME Best Inventions 2024](https://time.com/best-inventions-2024/)
- [Statista Diabetes Market Reports](https://www.statista.com/)

---
📌 **Author**: Your Name  
📅 **Date**: March 2025

