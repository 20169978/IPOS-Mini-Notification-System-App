from src.logger import action_logger, user_action_logger
'''
Because loggers do the things on console, it shold be tested by human eyes.
By running this test file, you can see if those work properly.

Tips:
    You can run this file by this command from project root.
    python -m tests.manual_test_logger  

Here is expected result.

On Console:
    -----Action: upload_document-----
    Arguments:
    args=('Bob', 'IPOS-Assessment')
    kwargs={}
    document uploaded
    -----Action Completed-----
    -----Action Starts-----
    Bob do upload document
    document upload
    -----Action Completed-----
'''

@action_logger
def upload_document(username, document_title):
    print("document uploaded")

class User:
    def __init__(self, name):
        self.name = name

    @user_action_logger("upload document")
    def upload_document(self, document):
        print("document upload")

upload_document("Bob", "IPOS-Assessment")

user = User("Bob")
user.upload_document("IPOS-Assessment")