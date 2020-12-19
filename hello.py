from flask import Flask,json,render_template,request,send_file
from main import initialize
import datetime
app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
	if request.method == 'POST':
		f = request.files['file']
		print("inside")
		f.filename="user_img.jpg"
		print("name chngd")
		f.save("static/User_Images/"+f.filename)
		print("saved")
		ans=initialize("static/User_Images/user_img.jpg")
		print(ans)
		return send_file('actual.csv', as_attachment=True)
	return render_template("index.html")

@app.route("/api")
def hello():
	ans=initialize("C:\\Users\\win\\Documents\\project\\4.jpeg")
	d={"Date":datetime.date.today(),"Name":ans}
	response = app.response_class(response=json.dumps(d),status=200,mimetype='application/json')
	return response

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)