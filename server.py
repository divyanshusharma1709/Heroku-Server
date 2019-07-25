import flask
import firebase_admin
from firebase_admin import credentials, firestore, storage
import json, io
import os
app = flask.Flask(__name__)


certi = firebase_admin.credentials.Certificate(cred)
firebase_admin.initialize_app(certi, {'storageBucket': 'fedserver-3766d.appspot.com'})
@app.route("/", methods = ['GET', 'POST'])
def main():
  print("Firebase Initialized")
  if flask.request.method == "POST":
    if flask.request.files["file"]:
      weights = flask.request.files["file"].read()
      weights_stream = io.BytesIO(weights)
      db = firestore.client()
      bucket = storage.bucket()
      blob = bucket.blob('Weight1')
      print("Saving at Server")
      with open("delta.bin", "wb") as f:
        f.write(weights_stream.read())
      print("Starting upload to Firebase")
      with open("delta.bin", "rb") as upload:
        blob.upload_from_file(upload)
        print("File Successfully Uploaded to Firebase")
        return "File Uploaded\n"
  if flask.request.method == "GET":
    print("In GET Method")
    return flask.send_file("graph1.pb", attachment_filename = 'graph1.pb')
  return "Server Initialized"
	
if __name__ == "__main__":
  app.run(debug = True, port = int(os.environ.get("PORT", 5000)))
	

