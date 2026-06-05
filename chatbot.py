from google import genai
from flask import Flask,request,jsonify
<<<<<<< HEAD
from flask_cors import CORS
app = Flask(__name__)




CORS(app,resources={r"/*": {"origins": "*"}})
#client = genai.Client(api_key="Your API Key")

@app.route("/summary",methods=["POST"])
def summary():
    data = request.get_json()
    user_input = data.get("text")
    print("Received text:", user_input)

=======
client = genai.Client(api_key="API KEY")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
>>>>>>> 14cb1f146206a3151884c9178997c15d90756fb2
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=("Give a summary of this input:", user_input)
    )
    print("AI:", response.text)
<<<<<<< HEAD

    return jsonify({"summary": response.text})
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
=======
    print('-'*100)
>>>>>>> 14cb1f146206a3151884c9178997c15d90756fb2
