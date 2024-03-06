from flask import Flask, request, jsonify
from pyngrok import ngrok
from llmodel import predo 


app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data=request.json
    
    # print(data)
    # Process the received data as needed
    # print("Received data:", data)
    salary=predo(data['year'])
    # print(type(salary))
    # print(salary)
    # Example response
    
    response = {'salary': salary}
    
    return jsonify(response), 200



@app.route("/home/<year>")
def home(year):

    price=predo(int(year))
    return f"hello {price}"


if __name__ == '__main__':
    # Authenticate ngrok (replace 'YOUR_AUTHTOKEN' with your actual ngrok authtoken)

    # Run the Flask app
    app.run()
