import  unittest
from survey import  AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question="what language did you frist learn to speak"
        self.my_survey=AnonymousSurvey(question)
        self.responeses=["python","java","c++"]

    def test_store_single_survey(self):
        self.my_survey.store_response(self.responeses[0])
        self.assertIn(self.responeses[0],self.my_survey.responses)

    def test_store_tree_survey(self):
        for response in self.responeses:
            self.my_survey.store_response(response)
        for response in self.responeses:
            self.assertIn(response, self.my_survey.responses)



""" 
   def test_store_single_survey(self):
        question="what language did you frist learn to speak?!"
        my_survey=AnonymousSurvey(question)
        my_survey.store_response("python")
        self.assertIn('python',my_survey.responses,'should be True')
    def test_store_tree_survey(self):
        question="what language did you frist learn to speak"
        my_survey=AnonymousSurvey(question)
        responses=["python","java","c++"]
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response,my_survey.responses)"""