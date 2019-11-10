from flask import Flask, jsonify,request
import pickle

import numpy as np
     

app = Flask(__name__)


@app.route('/get_credit', methods = ['GET','POST'])

def get_credit():
    if request.method == 'POST':
        # load the model from disk
        
        filename = 'floresta_credit_model.sav'
        filename2 = 'MLPRegressor_credit_model.sav'
        amount_model = pickle.load(open(filename2, 'rb'))
        status_model = pickle.load(open(filename, 'rb'))


        #Loan_ID : Id único
        #Gender: gênero
        #Married: casado ou não casado
        #Dependents: quantidade de dependentes
        #Education: grau de escolaridade
        #Self_Employed: se a pessoa é autônoma
        #ApplicationIncome: Renda
        #CoapplicationIncome: Renda familiar
        #Loan Amount: Quantidade do empréstimo (em milhares)
        #Loan_Amount_Term: Tempo para quitação da dívida (em dias)
        #Credit_History: Se a pessoa possui empréstimos passados
        #Property_Area: Se a pessoa mora em zona rural ou urbana
        #Loan_Status: Se o empréstimo foi quitado ou não
        #previsores = []
        
        Gender = request.form.get('Gender')
        Married = request.form.get('Married')
        Dependents = request.form.get('Dependents')
        Education = request.form.get('Education')
        Self_Employed = request.form.get('Self_Employed')
        ApplicationIncome = request.form.get('ApplicationIncome')
        CoapplicationIncome = request.form.get('CoapplicationIncome')
        Loan_Amount_Term = request.form.get('Loan_Amount_Term')
        Credit_History = request.form.get('Credit_History')
        Property_Area = request.form.get('Property_Area')
           
        #######################################################################
        ##Tratamentos
        #######################################################################
        if Gender == 'Male':
            Gender = 1
        elif Gender == 'Female':
            Gender = 0
        else:
            Gender = 2
            
        if Married == 'Yes':
            Married = 2
        elif Married == 'No':
            Married = 0
        else:
           Married = 1
        
        if Dependents == '0':
            Dependents = 0
        elif Dependents == '1':
            Dependents = 1
        elif Dependents == '2':
            Dependents = 2
        elif Dependents == '3+':
            Dependents = 3
        else:
           Married = 4
           
        if Education == 'Graduate':
            Education = 0
        elif Education == 'Not Graduate':
            Education = 1
        else:
            Education = 2
        
        if Self_Employed == 'Yes':
            Self_Employed = 0
        elif Self_Employed == 'No':
            Self_Employed = 2
        else:
            Self_Employed = 1
        
        if Credit_History == '1':
            Credit_History = 2
        elif Credit_History == '0':
            Credit_History = 1
        else:
            Credit_History = 0
            
        if Property_Area == 'Urban':
            Property_Area = 2
        elif Property_Area == 'Rural':
            Property_Area = 0
        elif Property_Area == 'Semiurban':
            Property_Area = 1
        else: 
            Property_Area = 3
        
        if Loan_Amount_Term == '360':
            Loan_Amount_Term = 9
        elif Loan_Amount_Term == '120':
            Loan_Amount_Term = 5
        elif Loan_Amount_Term == '240':
            Loan_Amount_Term = 7
        elif Loan_Amount_Term == '180':
            Loan_Amount_Term = 6
        elif Loan_Amount_Term == '60':
            Loan_Amount_Term = 3
        elif Loan_Amount_Term == '480':
            Loan_Amount_Term = 10
        elif Loan_Amount_Term == '300':
            Loan_Amount_Term = 8
        elif Loan_Amount_Term == '36':
            Loan_Amount_Term = 2
        elif Loan_Amount_Term == '84':
            Loan_Amount_Term = 4
        elif Loan_Amount_Term == '12':
            Loan_Amount_Term = 1
        else:
            Loan_Amount_Term = 0
            
        #######################################################################
        
 
        x_amount = [Gender, Married, Dependents, Education, Self_Employed, int(ApplicationIncome), int(CoapplicationIncome), Loan_Amount_Term, Credit_History, Property_Area]
        x_status = [Dependents,int(ApplicationIncome), int(CoapplicationIncome), Loan_Amount_Term, Credit_History, Property_Area]
        
        x_amount = np.reshape(x_amount,-1,10)
        x_amount = x_amount.reshape(-1,10)
        x_status = np.reshape(x_status,-1,6)
        x_status = x_status.reshape(-1,6)
        
        amount = amount_model.predict(x_amount)
        status = status_model.predict(x_status)

        amount = int(amount[0])
        status = int(status[0])
        if status == 1:
            status = 'Yes'
        else:
            status = 'No'
        response = {'Amount':  amount,
                    'Status': status
        }
        
        
                     
    
        return jsonify(response), 200

app.run(host = '0.0.0.0', port = 5000)

    


 




