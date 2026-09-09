import os
import threading
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bot is Running Successfully!'

def start_bot():
    os.system("python3 -m Extractor")

if __name__ == "__main__":
    # Bot ko background thread me start karne ke liye
    threading.Thread(target=start_bot, daemon=True).start()
    
    # Flask web server start karne ke liye
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    
