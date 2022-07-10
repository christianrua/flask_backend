from flask import Flask, request

import os, platform
from datetime import datetime

import boto3
s3_client = boto3.client('s3')

s3 = boto3.resource('s3')
bucket = s3.Bucket('sysopsadmin-christian')
 
app = Flask(__name__)

@app.route("/")
def hello_world():

    host_name = ""

    if platform.system() == "Windows":
        host_name = platform.uname().node
    else:
        host_name = os.uname()[1]  # doesnt work on windows

    ip_addr = request.remote_addr    
    file_name = f'log_{ip_addr}_{datetime.now()}.txt'

    with open(file_name, 'w') as f:
        f.write(f'{ip_addr} 200 {datetime.now()}')

#     response = s3_client.put_object(
#     Body=file_name,
#     Bucket='sysopsadmin-christian',
#     Key='flask-logs',
# )

    bucket.upload_file(f'{file_name}', 'flask-logs/')
    
    return f"<p>you are seeing the response from {host_name}, and your IP is {ip_addr}, adding {file_name} to s3</p>"

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)    