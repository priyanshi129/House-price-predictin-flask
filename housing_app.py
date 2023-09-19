from flask import Flask, render_template, request
#import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
print("Loading model...")
model=pickle.load(open('linear_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    furnishingstatus_furnished=0
    if request.method == 'POST':
        bathrooms = float(request.form['bathrooms'])
        stories=float(request.form['stories'])
        parking=float(request.form['parking'])
        mainroad_yes=request.form['mainroad_yes']
        if(mainroad_yes=='Yes'):
                mainroad_yes=1
        else:
            mainroad_yes=0
            
        
        guestroom_yes=request.form['guestroom_yes']
        if(guestroom_yes=='Yes'):
                guestroom_yes=1
        else:
            guestroom_yes=0
        '''basement_yes=request.form['basement_yes']
        if(basement_yes=='Yes'):
                basement_yes=1
        else:
            basement_yes=0'''
        hotwaterheating_yes=request.form['hotwaterheating_yes']
        if(hotwaterheating_yes=='Yes'):
                hotwaterheating_yes=1
        else:
            hotwaterheating_yes=0
        airconditioning_yes=request.form['airconditioning_yes']
        if(airconditioning_yes=='Yes'):
                airconditioning_yes=1
        else:
            airconditioning_yes=0
                                  
        prefarea_yes=request.form['prefarea_yes']
        if(prefarea_yes=='Yes'):
                prefarea_yes=1
        else:
            prefarea_yes=0
        furnishingstatus_unfurnished=request.form['furnishingstatus_unfurnished']
        if(furnishingstatus_unfurnished=='unfurnished'):
                furnishingstatus_unfurnished=1
                furnishingstatus_furnished=0
            
        else:
            furnishingstatus_furnished=1
            furnishingstatus_unfurnished=0
            
        prediction=model.predict([[bathrooms, stories, parking, mainroad_yes, guestroom_yes,hotwaterheating_yes,airconditioning_yes,prefarea_yes, furnishingstatus_unfurnished]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this house")
        else:
            return render_template('index.html',prediction_text="You Can Sell The House at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
