
from flask import Flask,render_template,request
import requests
import sklearn
import pickle

import pickle
import sklearn
from sklearn.preprocessing import StandardScaler


app=Flask(__name__)
model=pickle.load(open('the_random_forest_for_car.pkl','rb'))




@app.route('/',methods=['GET'])
def home():
    return render_template('home_practice.html')

@app.route('/predict',methods=[ 'POST'])
def predict():
    if request.method=='POST':
        Year=int(request.form['Year'])
        Present_Price=float(request.form['Selling_Price'])
        Kms_Driven=int(request.form['Kms_Driven'])
        Fuel_Type=(request.form['Fuel_Type_Petrol'])
        Owner=int(request.form['Owner'])
        Seller_Type=(request.form['Seller_Type_Individual'])
        Transmission=int(request.form['Transmission_Mannual'])

        Year=2021-Year
        if Fuel_Type == 'Petrol':
             Fuel_Type_Petrol=1
             Fuel_Type_Diesel=0

        elif  Fuel_Type == 'Diesel':
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        else:
             Fuel_Type_Petrol=0
             Fuel_Type_Diesel=0

        pre=model.predict([[Owner,Year,Kms_Driven,Present_Price,Seller_Type,Transmission,
             Fuel_Type_Diesel,Fuel_Type_Petrol]])

        return render_template('home_practice.html',prediction_text="You Can Sell The Car at",pre,'lacs')
    


if __name__ == '__main__':
    app.run(debug=True)
"""'Car_Name', 'Year', 'Selling_Price', 'Present_Price', 'Kms_Driven',
       'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner', 'current year',
       'age_car'"""
