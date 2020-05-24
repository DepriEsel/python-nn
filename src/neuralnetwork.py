from layer import Layer

class NeuralNetwork:
    def __init__(self, inputnodes, hiddenlayers, hiddenlayernodes, outputnodes):
        super().__init__()
        self.inputlayer = Layer(inputnodes)
        self.hiddenlayers = []
        for i in range(hiddenlayers):
            self.hiddenlayers.append(Layer(hiddenlayernodes))
        self.outputlayer = Layer(outputnodes)
        pass