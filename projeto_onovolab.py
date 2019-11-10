import pandas as pd

credito = pd.read_csv('dataset.csv')

credito["Gender"].fillna("NotInformed", inplace = True)
credito["Married"].fillna("NotInformed", inplace = True)
credito["Dependents"].fillna("NotInformed", inplace = True)
credito["Education"].fillna("NotInformed", inplace = True)
credito["Education"].fillna("NotInformed", inplace = True)
credito["Self_Employed"].fillna("NotInformed", inplace = True)
credito["Property_Area"].fillna("NotInformed", inplace = True)
credito["Credit_History"].fillna(-1, inplace = True)
credito["ApplicantIncome"].fillna(-1, inplace = True)
credito["CoapplicantIncome"].fillna(-1, inplace = True)
credito["LoanAmount"].fillna(-1, inplace = True)
credito["Loan_Amount_Term"].fillna(-1, inplace = True)

#atributo zero é identificador, não é importante para a previsão
previsores = credito.iloc[:,1:12].values
classe = credito.iloc[:,12].values

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder() 

previsores[:,0] = labelencoder.fit_transform(previsores[:,0]) 
previsores[:,1] = labelencoder.fit_transform(previsores[:,1]) 
previsores[:,2] = labelencoder.fit_transform(previsores[:,2]) 
previsores[:,3] = labelencoder.fit_transform(previsores[:,3]) 
previsores[:,4] = labelencoder.fit_transform(previsores[:,4]) 
previsores[:,8] = labelencoder.fit_transform(previsores[:,8]) 
previsores[:,9] = labelencoder.fit_transform(previsores[:,9]) 
previsores[:,10] = labelencoder.fit_transform(previsores[:,10]) 

classe = labelencoder.fit_transform(classe)

from sklearn.model_selection import train_test_split

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores,
                                                                  classe, 
                                                                  test_size = 0.3,
                                                                  random_state = 0)
amount_treinamento = X_treinamento[:,[7]]
amount_teste = X_teste[:,[7]]

X_treinamento = X_treinamento[:,[0,1,2,3,4,5,6,8,9,10]]
X_teste = X_teste[:,[0,1,2,3,4,5,6,8,9,10]]

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier


###############################################################################
#                                Naive Bayes
###############################################################################
naive_bayes = GaussianNB()
naive_bayes.fit(X_treinamento, y_treinamento)

previsoes = naive_bayes.predict(X_teste)

confusao = confusion_matrix(y_teste, previsoes)

taxaacerto = accuracy_score(y_teste, previsoes)
###############################################################################
#                                SVM
###############################################################################
svm = SVC()
svm.fit(X_treinamento, y_treinamento)
previsoes2 = svm.predict(X_teste)
confusao2 = confusion_matrix(y_teste, previsoes2)
taxa_acerto2 = accuracy_score(y_teste, previsoes)

###############################################################################
#                                Random Forest
###############################################################################

floresta = RandomForestClassifier(n_estimators = 100)
floresta.fit(X_treinamento, y_treinamento)

# Previsões
previsoes4 = floresta.predict(X_teste)

matriz4 = confusion_matrix(y_teste, previsoes4)
taxa_acerto4 = accuracy_score(y_teste, previsoes4)

###############################################################################
#                                features selction
###############################################################################
from sklearn.ensemble import ExtraTreesClassifier
forest = ExtraTreesClassifier()
forest.fit(X_treinamento,y_treinamento)

importancias = forest.feature_importances_


#svm2 = SVC()
#svm2.fit(X_treinamento2, y_treinamento)
#previsoes3 = svm2.predict(X_teste2)
#confusao3 = confusion_matrix(y_teste, previsoes3)
#taxa_acerto3 = accuracy_score(y_teste, previsoes3)

###############################################################################
#floresta 2



X_treinamento2 = X_treinamento [:,[2,5,6,7,8,9]]
X_teste2 = X_teste[:,[2,5,6,7,8,9]]

floresta2 = RandomForestClassifier(n_estimators = 100)
floresta2.fit(X_treinamento2, y_treinamento)

# Previsões
previsoes5 = floresta2.predict(X_teste2)

matriz5 = confusion_matrix(y_teste, previsoes5)
taxa_acerto5 = accuracy_score(y_teste, previsoes5)
#taxa_erro2 = 1 - taxa_acerto


###############################################################################

from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt


clf = MLPRegressor(alpha=0.1, hidden_layer_sizes = (30,), max_iter = 50000, 
                 activation = 'relu', verbose = 'True', learning_rate = 'adaptive')
clf.fit(X_treinamento, amount_treinamento)

pred_y = clf.predict(X_teste)

t = len(pred_y)
for i in range(t):
    plt.plot(i,pred_y[i,],'r*-',i, amount_teste[i,],'bo-')
    


##############################################################################
import pickle
# save the model to disk
filename = 'floresta_credit_model.sav'
pickle.dump(floresta2, open(filename, 'wb'))

filename2 = 'MLPRegressor_credit_model.sav'
pickle.dump(clf, open(filename2, 'wb'))
 





