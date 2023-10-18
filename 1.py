from flask import Flask, request, jsonify
import random
import string
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from pytz import utc

app = Flask(__name__)

# Danh sách các keys đang quản lý
keys = []

# Hàm tạo chuỗi ngẫu nhiên
def generate_random_value(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Hàm xoá key sau khi hết hạn
def delete_expired_keys():
    current_time = datetime.now().replace(tzinfo=utc)
    keys_to_remove = [key for key in keys if (current_time - key["created_at"]).total_seconds() >= 86400]  # 86400 giây = 24 giờ
    for key in keys_to_remove:
        keys.remove(key)

scheduler = BackgroundScheduler(timezone=utc)
scheduler.add_job(delete_expired_keys, 'interval', hours=24)
scheduler.start()

@app.route('/keys', methods=['GET'])
def get_all_keys():
    return jsonify({"keys": keys})

@app.route('/keys/<key_id>', methods=['GET'])
def get_key(key_id):
    for key in keys:
        if key["id"] == key_id:
            return jsonify(key)
    return "Key not found", 404

@app.route('/keys', methods=['POST'])
def create_key():
    data = request.get_json()
    if "id" not in data:
        return "Invalid data", 400

    new_key = {
        "id": data["id"],
        "value": generate_random_value(),
        "created_at": datetime.now().replace(tzinfo=utc)
    }
    keys.append(new_key)
    return "Key created", 201

@app.route('/keys/<key_id>', methods=['PUT'])
def update_key(key_id):
    data = request.get_json()
    if "value" not in data:
        return "Invalid data", 400

    for key in keys:
        if key["id"] == key_id:
            key["value"] = data["value"]
            return "Key updated", 200

    return "Key not found", 404

@app.route('/keys/<key_id>', methods=['DELETE'])
def delete_key(key_id):
    for key in keys:
        if key["id"] == key_id:
            keys.remove(key)
            return "Key deleted", 200

    return "Key not found", 404

if __name__ == '__main__':
    app.run(debug=True)
