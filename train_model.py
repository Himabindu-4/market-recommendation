import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load dataset
data = pd.read_csv('modcloth.csv')

# Data preprocessing
# Handling categorical variables by encoding
data['user_attr'] = data['user_attr'].astype('category').cat.codes  # Encode categorical variables if needed
data['model_attr'] = data['model_attr'].astype('category').cat.codes
data['category'] = data['category'].astype('category').cat.codes

# Handling missing values in 'size' by filling with the median value (optional)
data['size'].fillna(data['size'].median(), inplace=True)

# Prepare feature and target variables
# Choosing 'size', 'user_attr', 'model_attr', and 'category' as predictors
X = data[['size', 'user_attr', 'model_attr', 'category']]  # Adjust features as needed
y = data['rating']  # Target variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred)}")
print(f"R^2 Score: {r2_score(y_test, y_pred)}")

# Save the model
joblib.dump(model, 'modcloth_rating_model.pkl')
