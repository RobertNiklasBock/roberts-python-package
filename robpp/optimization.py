from properties import is_min, is_max, is_number


class OptimumFinder:
    def __init__(self, criterion_name="max"):
        self.__set_criterion(criterion_name)
        self.optimum = None
        self.optimized_parameters = None

    def __set_criterion(self, criterion_name):
        if criterion_name == "max":
            self.criterion = is_max
        elif criterion_name == "min":
            self.criterion = is_min
        else:
            raise Exception()

    def check(self, value, params=None):
        assert is_number(value), "Checked value is not a number."
        if self.optimum is None or self.criterion(self.optimum, value):
            self.optimum = value
            self.optimized_parameters = params

    def get_optimum(self):
        return self.optimum

    def get_optimized_parameters(self):
        return self.optimized_parameters
