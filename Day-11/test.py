from numpy import loadtxt
from keras.models import model_from_json

dataset=loadtxt('diabetes.csv', delimiter=",", skiprows=1)

x=dataset[:,0:8]
y=dataset[:,8]

json_file=open('model.json','r')
loaded_model_json=json_file.read()
json_file.close()

model=model_from_json(loaded_model_json)
model.load_weights("model.weights.h5")
print("Loaded model from disk")

prediction=model.predict(x)
for i in range(10,15):
    print('%s=>%d(expected %d)' %(x[i].tolist(),prediction[i][0],y[i]))
