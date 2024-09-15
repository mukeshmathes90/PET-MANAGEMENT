from flask import Flask, request, jsonify
from ai_recommendation_system import recommend_food
from iot_monitoring import collect_health_data

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def get_recommendation():
    data = request.json
    age = data['age']
    weight = data['weight']
    allergies = data['allergies']
    recommendation = recommend_food(age, weight, allergies)
    return jsonify({'food_recommendation': recommendation})

@app.route('/health_data', methods=['GET'])
def get_health_data():
    data = collect_health_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
