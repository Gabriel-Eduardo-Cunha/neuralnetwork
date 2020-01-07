from NeuralNetworkGameBlockJump import NeuralNetworkGBJ
from NeuralNetwork import Network



nnGBJ = NeuralNetworkGBJ('lastModel', True)

# nnGBJ.setLearningRate(0.4)

# nnGBJ.randomizeKnoledge(50)

# print(nnGBJ.train(1000))

nnGBJ.printNetworkStatus()
nnGBJ.saveModel('firstPlayer')




