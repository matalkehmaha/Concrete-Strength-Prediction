# Predicting Concrete Compressive Strength Using Machine Learning

**Student:** Maha Matalkeh  
**Course:** Advanced Artificial Intelligence  
**University:** Virginia State University

## Project Overview

This project uses machine learning to predict concrete compressive strength based on its ingredients and curing age.

The goal is to compare Linear Regression and Random Forest to find which model gives better predictions.

## Dataset

The dataset was obtained from the UCI Machine Learning Repository.

**Source:** https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength

The original dataset contains 1,030 samples, eight input features, and one target variable (concrete compressive strength in MPa).

After removing 25 exact duplicate rows, 1,005 samples remained.

## Machine Learning Models

Two models were used:

1. Linear Regression
2. Random Forest Regression

The models were evaluated using MAE, RMSE, and R². Grouped cross-validation was used, and Random Forest was improved using hyperparameter tuning.

## Final Results

| Model | MAE (MPa) | RMSE (MPa) | R² |
|---|---:|---:|---:|
| Linear Regression | 8.035 | 10.084 | 0.590 |
| Tuned Random Forest | 4.621 | 6.081 | 0.851 |

Random Forest performed better than Linear Regression and was selected as the final model.

## Working Demonstration

The saved Random Forest model can predict concrete strength from eight input values.

For one example mixture with a curing age of 28 days, the model predicted a compressive strength of **41.94 MPa**.

## How to Run the Project

1. Download or open the project notebook in Google Colab.
2. Install the required Python libraries, including `xlrd` for reading the original Excel dataset.
3. Run the notebook cells in order.
4. The dataset is downloaded automatically from UCI.
5. Review the model training and evaluation results.
6. Run the working demonstration to enter a new concrete mixture and predict its strength.

## Project Files

- `Concrete_Strength_Prediction_Maha_Matalkeh.ipynb` - Project code, analysis, and model evaluation.
- `concrete_strength_model.joblib` - Saved trained Random Forest model.

## Conclusion

The results show that Random Forest can predict concrete compressive strength more accurately than Linear Regression.

The model may help estimate concrete strength using mixture ingredients and curing age, but it should not replace laboratory testing for construction safety.
