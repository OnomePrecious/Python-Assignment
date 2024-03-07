class Method:

    def __init__(self, result: str):
        self.result = result

    def get_string(self, user_input: str):
        self.result = user_input

    def print_string(self):
        return self.result.upper()


result1 = Method("ayomide")
print(result1.print_string())
