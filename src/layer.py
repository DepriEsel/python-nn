from node import Node

class Layer:
    def __init__(self, nodes):
        super().__init__()
        self.nodes = []
        for i in range(nodes):
            self.nodes.append(Node())
        pass

    def nodelist(self):
        return self.nodes

    def __len__(self):
        return len(self.nodes)

    def __getitem__(self, index):
        return self.nodes[index]