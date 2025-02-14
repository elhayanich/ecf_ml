# fucntion pour corriger le dict

 lance ton serveur avec  : uvicorn main:app --reload puis accéde au server/docs ensuite et utilise l'exemple de valeur suivant :

 ```json
 {
  "temp": 0,
  "sis": 0,
  "hygro": 0,
  "anem1": 0,
  "anem2": 0
}
```
then execute it will correct the data and predict the action ( still not accurate).

---------------------

for more info about the iqr, lower bound and upper bound check the tests files ( replacement and deletion of data en fonction de iqr).

All this and i’m not sure of the function if it’s accurate or not ( since i did not finish) 
The best global error result I had is “0,2” using first classification to predict the action => check the whole response in result_api folder : response_forest.json

I still didn’t finish, some code snippets are AI generated because I was blocked and had to move on so they’re very dark areas.

to try a whole file prediction, execute train.py file and then predict.py , then use the newly corrected file in the api to verify. ( in models.py you can choose either forest cassification or logistic regression that i don’t recommend) 



