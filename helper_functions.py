import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

def estimate_adopters(revenue_df, asp_per_user):

    adopters_df = revenue_df.copy()
    adopters_df["Estimated Adopters"] = (adopters_df["Revenue"] * 1e9) / asp_per_user
    return adopters_df

def bass_model(t, p, q, M):

    F_t = (1 - np.exp(-(p + q) * t)) / (1 + (q / p) * np.exp(-(p + q) * t))
    return M * F_t

def estimate_bass_parameters(revenue_df, initial_guess=[0.01, 0.1, None]):

    t = np.array(revenue_df["Year"] - revenue_df["Year"].min() + 1) 
    sales = np.array(revenue_df["Estimated Adopters"])  # Adopters as proxy for sales

    params, _ = curve_fit(bass_model, t, sales, p0=initial_guess, maxfev=5000)

    return {"p": params[0], "q": abs(params[1]), "M": params[2]}  

def calculate_market_potential(market_revenue_df, market_share, asp_per_user, target_year=2024):
    
    market_revenue = market_revenue_df[market_revenue_df["Year"] == target_year]["Revenue"].values[0]
    
    M_estimated = (market_revenue * market_share * 1e9) / asp_per_user
    return M_estimated

def predict_diffusion(bass_params, start_year=2024, end_year=2035):

    years_future = np.arange(start_year, end_year + 1)

    predicted_adopters = bass_model(
        years_future - years_future.min() + 1,  
        bass_params["p"],
        bass_params["q"],
        bass_params["M"]
    )

    df_predictions = pd.DataFrame({"Year": years_future, "Predicted Adopters": predicted_adopters})
    return df_predictions

def estimate_adopters_by_period(bass_params, start_year=2024, end_year=2035):
    
    years_future = np.arange(start_year, end_year + 1)

    cumulative_adopters = bass_model(
        years_future - years_future.min() + 1,  
        bass_params["p"],
        bass_params["q"],
        bass_params["M"]
    )

    yearly_adopters = np.diff(cumulative_adopters, prepend=0)

    df_adopters = pd.DataFrame({
        "Year": years_future,
        "New Adopters": yearly_adopters,
        "Cumulative Adopters": cumulative_adopters
    })
    
    return df_adopters

