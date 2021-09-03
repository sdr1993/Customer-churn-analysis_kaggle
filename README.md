# Customer-churn-analysis_kaggle
This is a kaggle project of telecom customer data  
## Dataset ##
"Predict behavior to retain customers. You can analyze all relevant customer data and develop focused customer retention programs." [IBM Sample Data Sets] https://www.kaggle.com/blastchar/telco-customer-churn Each row represents a customer, each column contains customer’s attributes described on the column Metadata. The raw data contains 7043 rows (customers) and 21 columns (features). The “Churn” column is our target.


## File Explanation ##
 * The main EDA analysis file is Telco_Customer_Churn_Analysis.ipynb
 * The final classifier is build on Telecom_churn_classfier.ipynb and the models are saved.

## Limitation ##
  Limitation 1 : In this dataset, we can only see one type of each variables instead of real world situation of changing different options as time passes, e.g., in real world,     people might wanna try streaming service, but they might change their mind to leave the service next month.
  
  Limitation 2 : We cannot only see these variables as whole factors to understand the exact reasons why customers left because they might leave for better price offered by competitors or the bad economy in certian time, etc. We also cannot see the time they leaked, so it's hard to infer those external situation.
  
## Key Insights for Presentation ##

* The average LTV of 80% of those who unsubscribed is 750 dollars. On the other hand, the average LTV of top 20% of those who unsubscribed is 4750 dollars. And the ratio by the sum of total LTV by each groups is 750*4 : 4750 = 1 : 1.6, which suggests we should focus on serving those 20% customers with high LTV, which brought 60%(1.6/2.6) of our revenue from leaked customers
* 80%(low LTV) of leaked customers only stayed under 10 months.
* In 80%(low LTV) of leaked customers, only 5% of them used internet service.
* 81% of those who have and had stayed for more than 50 months tends to use multiple lines.
* 100% of those who brought 20% of extremely high LTV used and are using internet service.
* In 80% of data of current customers, all the subsets of internet services are equally used by 40% of people. Except for 80% of data of current customers, in the rest of the data, streaming movies and streaming TV are two top subsets of internet service people use, and device protection and online backup are the second place, and tech support and online security are both third place, the gaps between places are near 10% of whole data except for 80% of current customers.
* In 80% of current customers, those whose LTV are more than the average LTV of 80% of leaked customers are 10% more likely to use multiple lines and internet service than the average 80% of current customers.
* 89% of those who leaked used monthly contract, while only 42% of current customers are using monthly contract.
* Whether people use internet service is the most important factor to create high LTV, and yearly contract is second place.
* Among all the subsets of internet services, online backup is the most important factor to create high LTV

## Model Performances:

* Random Forest Classifier:
    * Accuracy_score : 0.78591
    
    * ROC_AUC_score : 0.67832
    
* Decission Tree Classifier:
    * Accuracy_score : 0.78875
    
    * ROC_AUC_score : 0.69761
    
* SVM Classifier: 
    * Accuracy_score : 0.79557
    
    * ROC_AUC_score : 0.70710

* XGBoost Classifier:
    * Accuracy_score : 0.79045
    
    * ROC_AUC_score : 0.69321

* ANN:
    * Accuracy_score : 0.78875
    
    * ROC_AUC_score : 0.71220


## Future Scope:

The accuracy of the models can be further improved if we address the 'imbalanced dataset' issue. On inspection, we find the number of records of majority class is more than twice the number of records in the minority class. This can be fixed with Under-Sampling or Over-Sampling techniques.
