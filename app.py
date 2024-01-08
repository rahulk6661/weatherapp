from flask import Flask,render_template,request
import requests
app=Flask(__name__)

@app.route('/')
def showpage():
    return render_template('index.html')


@app.route('/weatherapp',methods=['POST','GET'])
def peform_operation():
    cityid=request.form.get('city')
    apikey=request.form.get('apikey')
    url='https://api.openweathermap.org/data/2.5/weather'
    param={
        'q':cityid,
        'appid':apikey,
        'units':'metric'
    }
    response=requests.get(url,params=param)
    data=response.json()
    city=data['name']
    return f"{city} of minimum temperature is :{data['main']['temp_min']} & maximum temperature is : {data['main']['temp_max']}"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
