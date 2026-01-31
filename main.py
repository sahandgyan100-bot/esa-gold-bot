from flask import Flask
import requests
import os

app = Flask(__name__)

# کلیلی گووگڵ
API_KEY = "AIzaSyD3BzwGJJGy-Yfx68xyqN7_FJWmme3ZCi4"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={API_KEY}"

@app.route('/')
def home():
    try:
        p_res = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT").json()
        price = p_res['price']
        
        payload = {"contents": [{"parts": [{"text": f"Gold price is {price}. Reply only: BUY, SELL, or WAIT."}]}]}
        ai_res = requests.post(GEMINI_URL, json=payload).json()
        decision = ai_res['candidates'][0]['content']['parts'][0]['text']
    except:
        price, decision = "Loading...", "Wait"

    return f"<h1>Gold Price: ${price}</h1><h2>AI Signal: {decision}</h2>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
