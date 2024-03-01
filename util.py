

class Node():
    def __init__(self, state, parent=None, cost=0, heuristic_value=0):
        self.state = state 
        self.parent = parent
        self.cost = cost
        self.heuristic_value = heuristic_value

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
        
class PriorityQueueFrontier(StackFrontier):
    def add(self, node):
        priority = node.cost + node.heuristic_value
        if self.empty():
            self.frontier.append((node, priority))
        else:
            for i in range(len(self.frontier)):
                if priority < self.frontier[i][1]:
                    self.frontier.insert(i, (node, priority))
                    break
            else:
                self.frontier.append((node, priority))

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node[0]