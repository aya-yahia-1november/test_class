from survey import AnonymousSurvey
question="what language did you frist to speak?!"
my_survay=AnonymousSurvey(question)
print("prees 'q' when you want quit ")
while True:
    response= input("\n Enter your language : ")
    if response=='q':
        break
    my_survay.store_response(response)
print("\n thank you to eveyone who participated in survey")
my_survay.show_results()