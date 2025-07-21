# Flask app routing    

from flask import Flask, render_template, request,url_for



# Create a Simple flask application
app = Flask(__name__)      # Its entry point of a program

@app.route("/",methods=["GET"])
def welcome():
    return "<h1>Welcome to first Flask App<h1>"

@app.route("/index",methods=["GET"])
def index():
    return "<h4>Welcome to Index Page in Flask App."

# Variable rule
@app.route("/success/<int:score>",)
def success(score):
    return "A person has passed and the score is : " + str(score)   #used type casting to change int to string

@app.route("/fail/<int:score>",)
def fail(score):
    return "A person has failed and the score is : " + str(score)

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:
        Math=float(request.form['Math'])
        Science=float(request.form['Science'])
        History=float(request.form['History'])

        average_marks=(Math+Science+History)/3
        # return render_template('form.html',score = average_marks)
        result="" 
        if average_marks>=50:
            result="success"
        else:
            result="fail"

        #return redirect(url_for(result,score=average_marks))


        return render_template('result.html',results=average_marks)


## Assignemnt Try for loop


if __name__ == "__main__":
    app.run(debug = True)       # It will take (URL, Port) which is defoult in this 

