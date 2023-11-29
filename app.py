from flask import Flask, request, jsonify
import requests
import json


app = Flask(__name__)

PLEXO_WEBHOOK_ENDPOINT = "https://core.logpot-dev.cloud/payments/plexo/webhook/"

@app.route('/payments/plexo/webhook/', methods=['POST'])
def plexo_webhook():
    if request.method == 'POST':
        try:
            # Assuming the request payload is in JSON format
            request_data = request.get_json()
            # Print the entire request payload
            print("Received Plexo Webhook Request:")
            print(request_data)

            # Forward the data to the specified endpoint
            response = requests.post(PLEXO_WEBHOOK_ENDPOINT, json=request_data)

            # Check the response from the forward request
            if response.status_code == 200:
                print("Data forwarded successfully to the Plexo Webhook endpoint.")
            else:
                print("RESPONSE:")
                print(response.text)
                print(f"Failed to forward data. Status code: {response.status_code}")

            # You can access specific fields like this:
            status = request_data.get("Status")
            link_id = request_data.get("LinkId")
            # Access other fields as needed...

            # Add your processing logic here...

            return "Webhook received successfully", 200
        except Exception as e:
            print(f"Error processing Plexo Webhook: {str(e)}")
            return "Internal Server Error", 500
    else:
        return "Method Not Allowed", 405

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    # Bind to 0.0.0.0 to allow external access
    app.run(host='0.0.0.0', port=5000, debug=True)