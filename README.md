# King County House Price Prediction

This project builds a machine learning model to predict house prices in King County based on property characteristics such as size, location, and quality. The goal is to explore regression techniques, evaluate model performance, and deploy a simple interactive application for price estimation.

---

## Project Overview

Accurately estimating house prices is a common real-world regression problem. In this project, I:

- Explored and prepared housing data  
- Built multiple regression models  
- Compared their performance using cross-validation  
- Applied regularization to reduce overfitting  
- Interpreted model behavior using residuals and feature importance  
- Deployed the final model using **Streamlit**

The result is a complete end-to-end machine learning workflow, from modeling to deployment.

---

## Dataset

The dataset contains housing information from **King County**, including:
<img width="770" height="678" alt="image" src="https://github.com/user-attachments/assets/2211db6b-adae-4abe-9051-46f2cfa4fd52" /> 

**Target variable:**  
- `price`

---

## Models Explored

The following models were trained and evaluated:

1. Simple Linear Regression  
2. Multiple Linear Regression  
3. Polynomial Regression  
4. Ridge Regression (with polynomial features)

Model performance was evaluated using:
- R² score  
- Mean Absolute Error (MAE)  
- Cross-validation  
- Residual plots  
- Actual vs Predicted plots  

---

## Final Model Selection

The final selected model is:

**Polynomial Regression (degree = 2) with Ridge Regularization**

This model was chosen because it:

- Achieved the highest and most stable cross-validated R² score  
- Generalized well across folds  
- Reduced overfitting compared to higher-degree polynomials  
- Captured non-linear relationships in the data  

### Final Performance
- **R² ≈ 0.73**
- **Mean Absolute Error ≈ $120,000**

This means the model explains about 73% of the variance in house prices and predicts prices within approximately $120K on average.

---

## Model Interpretation

### Residual Analysis
Residual plots show that:
- Predictions are accurate for low- to mid-priced homes  
- Errors increase for higher-priced properties  
- High-priced homes are underrepresented, making them harder to predict  

### Feature Importance
Feature importance is derived from the magnitude of Ridge regression coefficients after standardization.

Key observations:
- **Construction grade** is the most influential feature  
- **Location (latitude)** strongly affects price  
- **Size-related features** (living area, basement, above-ground area) play a major role  
- Polynomial and interaction terms improve model performance  

These results align well with real-world housing behavior.

---

## Streamlit Web App

A Streamlit app was built to allow users to interactively estimate house prices.

### App Features
- Simple and intuitive input interface  
- Sensible default values for hidden features  
- Uses the trained Ridge regression pipeline  
- Instant price prediction  

### Note on Assumptions
Some features (e.g., nearby house size or view score) are assigned reasonable default values to simplify user input. These assumptions may slightly affect prediction accuracy.

---

## Project Structure

```

├── King_County_Professional_Valuation.ipynb
├── app.py
├── house_price_model.pkl
├── housing.csv
├── requirements.txt
├── README.md

```

---

## Limitations

- High-priced homes are underrepresented in the dataset  
- Location is only partially captured using latitude  
- Some features are fixed to default values in the app  
- Polynomial regression may not capture all complex real-world interactions  

---

## Future Improvements

Possible extensions include:
- Using tree-based models (Random Forest, Gradient Boosting, XGBoost)
- Adding longitude or neighborhood-level features
- Applying log transformation to the target variable
- Handling outliers more explicitly
- Adding prediction uncertainty intervals
- Improving UI with maps or visual analytics

---

## Conclusion

This project demonstrates a complete end-to-end machine learning workflow, from data preprocessing and model evaluation to deployment. By progressively refining model complexity and validating results using cross-validation, a reliable and interpretable pricing model was developed. While there is room for improvement, the project provides a strong foundation for more advanced modeling techniques.

---

## Author

**Ali Nazir**  
Aspiring Data Scientist | Machine Learning Enthusiast
