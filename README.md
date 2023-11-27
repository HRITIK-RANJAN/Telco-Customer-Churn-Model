# Telco-Customer-Churn-Model
This is a telecommunication Customer churn prediction model project, a data science project which aims to help in solving churning of customers a major bussiness problem.

The dataset used here has been taken from kaggle(https://www.kaggle.com/datasets/blastchar/telco-customer-churn). Here it is 'WA_Fn-UseC_-Telco-Customer-Churn.csv'.\n
1.Customer-churn.ipynb is jupyter notebook in which steps like Data preprocessing, EDA are performed and processed dataset is saved as prepared.csv ,prepared_new_df.csv.
2.model-building.ipynb  invovlves model building and fine tuning the model. 
3.mainApp.py- this file is created to check the consistency and accurracy of final model.In this a random row is selected from the dataset and checked for the churn and returns the prediction as well as the actual value of churn.
model.pkl- It is the final model exported after going through the various classifier and achieves best accuracy.
Customer-churn-AnalysisUsing-PowerBi.pbix - Tried to perform EDA with the help of PowerBi and further dashboard in future.
