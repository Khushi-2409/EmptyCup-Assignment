from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data (You can later connect this to MongoDB)
designers = [
    {
        "id": 1,
        "name": "Epic Designs",
        "shortlisted": False
    },
    {
        "id": 2,
        "name": "Studio D3",
        "shortlisted": False
    },
    {
        "id": 3,
        "name": "Creative Sparks",
        "shortlisted": False
    },
    {
        "id": 4,
        "name": "Aura Interiors",
        "shortlisted": False
    }
]

@app.route('/api/designers', methods=['GET'])
def get_designers():
    return jsonify(designers)

@app.route('/api/shortlist/<int:designer_id>', methods=['POST'])
def toggle_shortlist(designer_id):
    for designer in designers:
        if designer["id"] == designer_id:
            designer["shortlisted"] = not designer["shortlisted"]
            return jsonify({"success": True, "shortlisted": designer["shortlisted"]})
    return jsonify({"error": "Designer not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
