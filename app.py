from flask import Flask, request, jsonify

app = Flask(__name__)

# Verification Token for Meta Webhooks
VERIFY_TOKEN = "2qNEQt8brSBrUItoDsiDs8SaOz7_2uRAkvPcFGzeTfTHAGMn9"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Log incoming GET verification request
        verify_token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        
        print(f"Received Verify Token: {verify_token}")
        print(f"Expected Verify Token: {VERIFY_TOKEN}")
        print(f"Received Challenge: {challenge}")
        
        # Check if the verification token matches
        if verify_token == VERIFY_TOKEN:
            print("Verification successful")
            return challenge, 200
        print("Verification failed")
        return "Verification token mismatch", 403

    if request.method == 'POST':
        # Log incoming POST data
        data = request.get_json()
        print(f"Received POST Data: {data}")
        return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)