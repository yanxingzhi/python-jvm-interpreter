class Frame:
    def __init__(self, maxStack, maxLocal, current_class):
        self.stack  = []
        self.locals = [current_class] + [0 for i in range(maxLocal)]
        self.current_class = current_class

    def set_local(self, i, value):
        self.locals[i] = value

    def get_local(self, i):
        return self.locals[i]