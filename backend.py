from flask import Flask

import os, platform
 
app = Flask(__name__)

@app.route("/")
def hello_world():

    host_name = ""

    if platform.system() == "Windows":
        host_name = platform.uname().node
    else:
        host_name = os.uname()[1]  # doesnt work on windows
    
    return f"<p>you are seeing the response from {host_name}</p>"

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)    