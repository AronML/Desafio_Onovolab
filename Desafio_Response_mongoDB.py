import requests
import pymongo

url = 'http://127.0.0.1:5000/get_credit'

payload = {'Gender': 'Male',
               'Married': 'No',
               'Dependents': '0',
               'Education': 'Graduate',
               'Self_Employed': 'No',
               'ApplicationIncome': '5849',
               'CoapplicationIncome': '0',
               'Loan_Amount_Term': '360',
               'Credit_History': '1',
               'Property_Area': 'Urban'}


r = requests.post(url, data = payload)
response = r.json()

myclient = pymongo.MongoClient("<inserir a StringConnexion aqui>")
mydb = myclient["onovolabDB"]
mycol = mydb["credit"]
mydict = response

x = mycol.insert_one(mydict)



