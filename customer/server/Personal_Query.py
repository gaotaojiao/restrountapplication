#Personal_Query的后端代码
# 用于查询用户最近一次的消费记录和用户的剩余金额
from flask import Flask, request, jsonify
from db_config import get_db_connection
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/recent_meal', methods=['GET'])
def recent_meal():
    user_id = request.args.get('user_id', type=int)
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc('QueryRecentMeal', [user_id])
    results = []
    for result in cursor.stored_results():
        results.extend(result.fetchall())
    cursor.close()
    conn.close()
    return jsonify(results)


@app.route('/remaining_money', methods=['GET'])
def remaining_money():
    user_id = request.args.get('user_id', type=int)
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc('GetRemainingMoney', [user_id])
    result = []
    for res in cursor.stored_results():
        result.extend(res.fetchall())
    cursor.close()
    conn.close()
    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True)