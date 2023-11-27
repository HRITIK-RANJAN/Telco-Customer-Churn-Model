import pandas as pd
import pickle
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")


def predict(df,random_row):
    model = pickle.load(open("model.pkl", "rb"))
    print('Randomly Chosen data is :: ')
    print(random_row.to_string())

    df_1 = pd.concat([df, random_row.tail(1)], ignore_index = True)
    create_label = lambda x: "{0} - {1}".format(x, x + 11)
    df_1['tenure_group'] = df_1['tenure'].apply(lambda x: create_label((x - 1) // 12 * 12 + 1))
    df_1['Churn'] = df_1['Churn'].replace({ 'No':0, 'Yes':1})
    df_1.drop(columns= ['customerID','tenure'], axis=1, inplace=True)

    df_1_improved=pd.get_dummies(df_1)
    val=df_1_improved.tail(1)['Churn'].iloc[-1]
    df_1_improved.drop(columns= ['Churn'], axis=1, inplace=True)
    df_1_improved = df_1_improved.iloc[1:]

    single = model.predict(df_1_improved.tail(1))

    if single==1:
        o1 = "This customer is likely to be churned!!"
    else:
        o1 = "This customer is likely to continue!!"
    o3="As per given data In original the customer will {}".format('churn' if val==1 else 'not Churn' )
    print("As per prediction-> ",o1,'\n',o3)


df=pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
df['TotalCharges']=pd.to_numeric(df['TotalCharges'],errors='coerce')
df=df[df['TotalCharges'].isnull()!=True] 
random_row = df.sample(n=1)  
predict(df,random_row)