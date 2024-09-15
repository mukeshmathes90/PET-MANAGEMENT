import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Sample data
data = pd.DataFrame({
    'breed': ['Labrador', 'Poodle', 'Bulldog'],
    'age': [5, 3, 4],
    'weight': [30, 25, 40],
    'allergies': [0, 1, 0],
    'food_recommendation': ['Brand A', 'Brand B', 'Brand C']
})

# Prepare data
X = data[['age', 'weight', 'allergies']]
y = data['food_recommendation']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train AI model
model = RandomForestClassifier()
model.fit(X_scaled, y)

def recommend_food(age, weight, allergies):
    input_data = [[age, weight, allergies]]
    input_data_scaled = scaler.transform(input_data)
    recommendation = model.predict(input_data_scaled)
    return recommendation[0]

# Example usage
recommended_food = recommend_food(4, 35, 0)
print(f"Recommended Food: {recommended_food}")
