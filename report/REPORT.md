# Report on COPD Risk Prediction Model

## Introduction
Chronic Obstructive Pulmonary Disease (COPD) is a critical public health concern, particularly in countries like Nepal, where environmental pollutants, biomass fuel exposure, and smoking are widespread. The prediction model aims to identify individuals at risk of COPD by analyzing various lifestyle, environmental, and genetic factors. This report discusses the development of the COPD risk prediction model using machine learning techniques, providing a comprehensive understanding of the underlying data, model performance, and key insights.

## 1. Data Overview

The dataset used for building the COPD prediction model includes features related to patient demographics, lifestyle choices, environmental exposures, and genetic factors. The most important features identified are:
- Age
- Gender
- Smoking Status
- Duration of Smoking
- Biomass Fuel Exposure
- Occupational Exposure
- Family History of COPD
- BMI
- Air Pollution Level
- Respiratory Infections in Childhood
- Location (One-Hot Encoded)

### Key Variables
The dataset includes several key variables highly relevant to COPD, such as **smoking status**,**duration of smoking**, **air pollution**, and **biomass fuel exposure**, among others. These variables contribute differently to the prediction of COPD, with smoking being the most prominent risk factor.

---

## 2. Model Development

### 2.1 Feature Engineering
Several features, such as smoking status and location, were encoded to be compatible with machine learning algorithms. Continuous variables were left unchanged, while categorical features like gender, smoking status, and location were encoded to reflect their influence on COPD.

Interactions between features, such as the interaction between smoking and pollution levels, were created to capture the combined effects of these factors.

### 2.2 Model Training
The **Random Forest Classifier** was chosen for its ability to handle imbalanced datasets and nonlinear relationships among features. Key parameters such as the number of estimators and maximum depth were fine-tuned to improve performance.

### 2.3 Model Evaluation
The model was evaluated using various classification metrics:
- **Accuracy**: 99%
- **Precision**: 99%
- **Recall**: 99%
- **F1 Score**: 99%
- **Confusion Matrix**:[[184   2]
                        [  1 213]]

The model's strong performance in terms of recall ensures that most COPD cases are correctly identified, minimizing the risk of false negatives.

---

## 3. Insights from EDA of the COPD Data

### 3.1 Age vs COPD Diagnosis
While age is a contributing factor, it does not have a strong predictive influence on COPD. This is confirmed by the correlation matrix, where age shows a weak positive correlation (0.25) with COPD. The age range for COPD patients generally falls between 45 and 75 years, suggesting that while older individuals are more prone to COPD, age alone is not a strong predictor.

### 3.2 Smoking Status vs COPD Diagnosis
Smoking status emerges as the most significant predictor of COPD. The count plot clearly shows a much higher likelihood of COPD among current and former smokers. The correlation matrix supports this, with duration of smoking having strong positive correlation (0.85) with COPD diagnosis.

### 3.3 Environmental Factors
- **Biomass fuel exposure** is common in rural areas of Nepal, contributing moderately to COPD risk. The correlation coefficient for biomass fuel exposure is 0.04, indicating a positive relationship but weaker compared to smoking.
- **air pollution levels** show only a slight difference between COPD-diagnosed and non-diagnosed individuals, with a correlation of 0.03. While pollution contributes to respiratory diseases, its impact in this dataset appears less significant than smoking or genetic predisposition.

### 3.4 Family History of COPD
Family history plays a moderate role in COPD diagnosis. The correlation between family history and COPD, suggesting that genetics, along with shared environmental exposures, can increase the risk of COPD. This factor, although not as dominant as smoking, should still be considered in risk assessments.

### 3.5 Occupational Exposure vs COPD Diagnosis
Occupational exposure, often linked to respiratory diseases, shows a weak correlation with COPD in this dataset. This may be due to the types of occupations represented or the stronger influence of other factors like smoking and environmental exposure.

### 3.6 Gender, BMI, and Childhood Infections
Other factors like **gender**, **BMI**, and **respiratory infections in childhood** were found to have minimal influence on COPD diagnosis:
- **Gender** has no significant difference in COPD risk between men and women.
- **BMI** has a negligible correlation (0.03), indicating no substantial link between body weight and COPD.
- **Respiratory infections in childhood** also show a weak correlation (0.005) COPD daignosis.

---

## 4. Conclusion

The analysis of the COPD dataset reveals that smoking status is the most significant predictor of COPD, followed by family history and biomass fuel exposure. Environmental factors such as air pollution and occupational exposure play a role but are less influential. Age and other demographic factors have a minimal impact on the prediction.

### Key Recommendations:
1. **Public Health Interventions**: Focus on reducing smoking rates, particularly in high-risk populations, to mitigate the leading risk factor for COPD.
2. **Biomass Fuel Alternatives**: Promote cleaner alternatives to biomass fuels, especially in rural areas, to lower COPD incidence.
3. **Further Research**: Investigate genetic factors more deeply to better understand their interaction with environmental triggers in COPD development.

The insights gained from this analysis should guide future public health policies in Nepal, particularly in reducing smoking and improving environmental conditions.

---

## 5. Streamlit Deployment
The COPD prediction application has been successfully deployed using Streamlit. You can access the app at the following link: [Streamlit App](https://copd-prediction-zuy3yuivcbggeh4qnecftx.streamlit.app/).

---