# Laptop Price Prediction Project

This project is a complete workflow for cleaning, analyzing, and predicting laptop prices using Python, Jupyter Notebooks, and Streamlit.

## Project Structure

- `dataset/`
  - `laptop_price.csv`: Raw dataset containing laptop specifications and prices.
  - `cleaned/laptops_cleaned.csv`: Cleaned dataset generated after preprocessing.
- `notebook/`
  - `data_Cleaning.ipynb`: Jupyter notebook for data cleaning and feature engineering.
  - `model_building.ipynb`: Jupyter notebook for building and evaluating the machine learning model.
- `streamlit/`
  - `app.py`: Streamlit web app for predicting laptop prices based on user input.

## Workflow

### 1. Data Cleaning (`notebook/data_Cleaning.ipynb`)
- Loaded the raw laptop dataset.
- Dropped unnecessary columns (e.g., laptop_ID, Product).
- Converted RAM and Weight columns to numeric types.
- Split CPU brand and speed into separate features.
- Extracted and converted storage features (SSD, HDD, Hybrid, Flash Storage).
- Ensured the price column is numeric and removed invalid rows.
- Performed feature engineering (e.g., price per inch).
- Visualized data distributions and correlations.
- Saved the cleaned dataset for modeling.

### 2. Model Building (`notebook/model_building.ipynb`)
- Built and trained a machine learning model to predict laptop prices.
- Saved the trained model as `models/laptop_price_model.pkl` for use in the app.

### 3. Streamlit App (`streamlit/app.py`)
- Interactive web app for predicting laptop prices.
- Users input laptop specifications (brand, type, screen size, RAM, storage, CPU, GPU, OS, etc.).
- The app loads the trained model and predicts the price based on user input.
- Displays the estimated price and handles errors gracefully.

## How to Run

1. Install required packages:
   ```bash
   pip install streamlit pandas scikit-learn joblib
   ```
2. Start the Streamlit app:
   ```bash
   streamlit run streamlit/app.py
   ```
3. Open the app in your browser and enter laptop specifications to get price predictions.

## Notes
- Ensure the trained model file (`models/laptop_price_model.pkl`) exists before running the app.
- The cleaned dataset is saved in `dataset/cleaned/laptops_cleaned.csv`.
- You can further customize the app and model as needed.

Github Repo URL - https://github.com/ekeminijoshua11-lang/new-group-laptop-prediction
## Credits
Developed by [Your Name].
