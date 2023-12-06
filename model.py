import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv('preprocessed_dataset.csv')


# List of columns to include
selected_columns = [
    'Interest_Rate',
    'Credit_Mix',
    'Delay_from_due_date',
    'Num_Credit_Inquiries',
    'Num_Credit_Card',
    'Outstanding_Debt',
    'Credit_History_Age',
    'Payment_of_Min_Amount',
    'Num_Bank_Accounts',
    'Num_of_Delayed_Payment',
    'Credit_Score'
]

# Create a new DataFrame with only the selected columns
selected_df = df[selected_columns]


# Drop the 'Credit_Score' column along the columns axis
X = selected_df.drop('Credit_Score', axis=1)

y = selected_df['Credit_Score']  # Make sure to use brackets to keep y as a DataFrame or Series

# Rest of your code remains unchanged


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, shuffle=True, random_state=42)
scalar = StandardScaler()

features = X_train.columns

X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

X_train = pd.DataFrame(X_train, columns=features)
X_test = pd.DataFrame(X_test, columns=features)

model = RandomForestClassifier()

model.fit(X_train, y_train)

# Specify the file path where you want to save the model


pickle.dump(model, open("model_rfc.pkl", "wb"))

pickle.dump(scalar, open("scaling.pickle", "wb"))

y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)


scale_obj = pickle.load(open("scaling.pickle", 'rb'))

model_obj = pickle.load(open('model_rfc.pkl', 'rb'))
sample = scale_obj.transform(X_test.iloc[[0]])

output = model_obj.predict(sample)
print(output)
