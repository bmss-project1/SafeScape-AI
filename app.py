from flask import Flask, request, jsonify
import json
import logging
from handlers import (
    handle_comment,
    handle_message,
    handle_reaction,
    handle_live_comment,
    handle_optin,
    handle_postback,
    handle_referral,
    handle_seen,
    handle_unhandled_field,
)

app = Flask(__name__)

# Verification Token for Meta Webhooks
VERIFY_TOKEN = "2qNEQt8brSBrUItoDsiDs8SaOz7_2uRAkvPcFGzeTfTHAGMn9"

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    try:
        if request.method == 'GET':
            # Webhook verification
            verify_token = request.args.get("hub.verify_token")
            challenge = request.args.get("hub.challenge")
            logging.info(f"Verify Token Received: {verify_token}")
            if verify_token == VERIFY_TOKEN:
                logging.info("Verification successful.")
                return challenge, 200
            logging.warning("Verification failed: token mismatch.")
            return "Verification token mismatch", 403

        if request.method == 'POST':
            data = request.get_json()
            logging.info("Received POST Data:")
            logging.info(json.dumps(data, indent=4))

            # Process each entry in the payload
            for entry in data.get('entry', []):
                for change in entry.get('changes', []):
                    field = change.get('field')
                    value = change.get('value')

                    # Check field and call respective handler
                    if field == "comments":
                        handle_comment(value)
                    elif field == "message_reactions":
                        handle_reaction(value)
                    elif field == "messages":
                        handle_message(value)
                    elif field == "live_comments":
                        handle_live_comment(value)
                    elif field == "messaging_optins":
                        handle_optin(value)
                    elif field == "messaging_postbacks":
                        handle_postback(value)
                    elif field == "messaging_referral":
                        handle_referral(value)
                    elif field == "messaging_seen":
                        handle_seen(value)
                    else:
                        handle_unhandled_field(field, value)

            return jsonify({"status": "success"}), 200
    except Exception as e:
        logging.error(f"Error processing webhook: {e}", exc_info=True)
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)