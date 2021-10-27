from flask import Flask , render_template , request
import pandas as pd
import pickle
import numpy as np
app=Flask(__name__)
model = pickle.load(open("LinearRegressionModel.pkl","rb"))

car=pd.read_excel('SecondToLast.xlsx')

@app.route('/')
def index():
    brands = sorted(car['Brand'].unique())
    boites= sorted(car['Boite'].unique())
    Year= sorted(car['Year'].unique(), reverse=True)
    Energie=sorted(car['Energie'].unique())

    
    return render_template('index.html', brands=brands , boites = boites, years=Year, Energie=Energie)

@app.route('/predict',methods=['POST'])
def predict():
    Brand=request.form.get('Brand')
    Boite=request.form.get('Boite')
    Year=int(request.form.get('Year'))
    Energie=request.form.get('Energie')
    kilometrage=int(request.form.get('kilometrage'))
    
    
   
    prediction=model.predict(pd.DataFrame([[Brand,Boite,Year,Energie,kilometrage]],columns=['Brand','Boite','Year','Energie','Kilometrage']))
    
    

    return str(np.round(prediction[0],3))

if __name__=="__main__":
    app.run(debug=True)
