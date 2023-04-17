from flask import Flask,request,jsonify
from flask_restful import Api,Resource
import joblib
app = Flask(__name__)
api = Api(app)
model = joblib.load('model.pkl')
model2 = joblib.load('model2.pkl')

@app.route('/predictHeart',methods=['post'])
def post():
        posted_data = request.get_json()
        
        age = posted_data['age']
        sex = posted_data['sex']
        cp = posted_data['cp']
        trestbps = posted_data['trestbps']
        chol = posted_data['chol']
        fbs = posted_data['fbs']
        restecg = posted_data['restecg']
        thalach = posted_data['thalach']
        exang = posted_data['exang']
        oldpeak = posted_data['oldpeak']
        slope = posted_data['slope']
        ca = posted_data['ca']
        thal = posted_data['thal']
     
        
        prediction = model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if prediction == 1 :
           prediction_class = " heart disease"
        elif prediction == 0 :
           prediction_class = " no heart disease"
        else :
           prediction_class ="not found" 
        return jsonify({
         "predicted": prediction_class
        })        
@app.route('/predictDiabetes',methods=['post'])
def yy():
        posted_data = request.get_json()
        Glucose = posted_data['Glucose']
        Insulin = posted_data['Insulin']
        BMI = posted_data['BMI']
        Age = posted_data['Age']
        prediction = model2.predict([[Glucose,Insulin,BMI,Age]])
        if prediction == 1 :
           prediction_class = " diabetes patient"
        elif prediction == 0 :
           prediction_class = " no diabetes patient"
        else :
           prediction_class ="not found" 
        return jsonify({
         "predicted": prediction_class
        })   
if __name__== '__main__':
 app.run(debug=True)
