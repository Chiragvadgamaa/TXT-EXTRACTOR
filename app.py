import os
import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bot is active!'

if __name__ == "__main__":
    # Bot module/script ko start karne ke liye
    subprocess.Popen(["python3", "-m", "Extractor"])
    
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    
  
