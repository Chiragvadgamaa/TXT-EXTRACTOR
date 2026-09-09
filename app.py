import os
import asyncio
import threading
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bot is Running Successfully!'

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # Flask app ko alag thread me chalayein taaki port active rahe
    threading.Thread(target=run_flask, daemon=True).start()
    
    # Bot script ko run karein
    os.system("python3 -m Extractor")
    
