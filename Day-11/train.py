
'''Libraries ti install
pip install tensorflow
pip install keras
pip install h5py
pip install scipy
'''

from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense


dataset = loadtxt('diabetes.csv', delimiter=",", skiprows=1)

x=dataset[:,0:8]
y=dataset[:,8]
print("Input",x)
print("Output",y)

model=Sequential()

model.add(Dense(12,input_dim=8,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(x,y,epochs=10,batch_size=10)
_,accuracy=model.evaluate(x,y)
print('Accuracy: %.2f%%' % (accuracy * 100))

model_json = model.to_json()

with open("model.json", "w") as json_file:
    json_file.write(model_json)

model.save_weights("model.weights.h5")
      
