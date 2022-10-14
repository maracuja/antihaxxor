
class StringMasker:
    def __init__(self, input: ""=str):
        self.input = input

    def get_masked(self) -> str:
        return '*' * len(self.input)

    def __repr__(self) -> str:
        return "I'm a class holding a masked password lol."
