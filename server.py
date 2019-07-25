import flask
import json, io
import os
app = flask.Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def main():
  print('Hello')
  return "Server Initialized"
  if flask.request.method == "POST":
    print("12")
    print(flask.request)
    if flask.request.files["file"]:
      print("13")
      image = flask.request.files["file"].read()
      image_stream = io.BytesIO(image)
      with open("delta.bin", "wb") as f:
        f.write(image_stream.read())
      print("File Created")
      return "File Received\n"
  if flask.request.method == "GET":
    print("In GET Method")
    return flask.send_file("graph1.pb", attachment_filename = 'graph1.pb')
  return "Server Initialized"
	
if __name__ == "__main__":
  app.run(debug = True, port = int(os.environ.get("PORT", 5000)))
	

