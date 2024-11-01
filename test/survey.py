from urllib import response


class AnonymousSurvey():
    def __init__(self, question):
        self.question = question
        self.response = []
    
    def show_question(self):
        print(self.question)
    
    def store_response(self, new_res):
        self.response.append(new_res)
    
    def show_results(self):
        print("Survey results:")
        for res in self.response:
            print('- ' + res)

