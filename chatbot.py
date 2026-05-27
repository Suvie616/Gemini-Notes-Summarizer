from google import genai
from flask import Flask,request,jsonify
client = genai.Client(api_key="AIzaSyBKkXfm5vB11M9BRoevTOWWft83mTKYTME")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=user_input
    )
    print("AI:", response.text)
    print('-'*100)