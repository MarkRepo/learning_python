import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_resonse(self):
        self.my_survey.store_response('English')
        self.assertIn('English', self.my_survey.response)
    
    def test_store_three_responses(self):
        for res in self.responses:
            self.my_survey.store_response(res)
        for res in self.responses:
            self.assertIn(res, self.my_survey.response)
    
unittest.main()