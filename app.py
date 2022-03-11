from flask import Flask, redirect , render_template,request,url_for,request
app = Flask(__name__)
sum = 0
first_value = 0
second_value=0
third_value=0
four_value =0 
five_value = 0
@app.route('/')
def start():
    return redirect(url_for('firstget'))
@app.route('/first',methods=['GET'])
def firstget():
    return render_template('first.html')
@app.route('/first',methods=['POST'])
def firstpost():
    first_value = request.form['yes'] 
   # print(first_value)
    return redirect(url_for('secondget'))
@app.route('/second',methods=['GET'])
def secondget():
    return render_template('second.html')
@app.route('/second',methods=['POST'])
def secondpost():
    second_value = request.form['yes'] 
    print(second_value)
    return redirect(url_for('thirdget'))
@app.route('/third',methods=['GET'])
def thirdget():
    return render_template('third.html')
@app.route('/third',methods=['POST'])
def thirdpost():
    third_value = request.form['yes'] 
    return redirect(url_for('fourget'))
@app.route('/four',methods=['GET' ])
def fourget():
    return render_template('four.html')
@app.route('/four',methods=['POST'])
def fourpost():
    four_value = request.form['yes'] 
    return redirect(url_for('fiveget'))
@app.route('/five',methods=['GET'])
def fiveget():
    return render_template('five.html')
@app.route('/five',methods=['POST'])
def fivepost():
    five_value = request.form['yes'] 
    l = [first_value,second_value, third_value,four_value,five_value]
    print(first_value)
    i = 0
    global s
    s= 0
    while(i < 5):
        if(l[i] == "1"):
            s += pow(2,i)
        i+=1
    return render_template('final.html', s =s)
if __name__== '__main__':
    app.run(debug=True)