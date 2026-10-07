class UploadNotifier:
    def __init__(self):
        '''
        This class probides notification feature of uploading new document for subscribers.
        '''
        self.subscribers = []

    def add_subscriber(self, subscriber):
        '''
        You can add new subscriber.
        Argument:
            subscriber Function: Must be callable function. The first argument of subscriber will be information of new document.
        '''
        self.subscribers.append(subscriber)

    def notify_document_updated(self, document):
        '''
        Call all subscribers. Give document information as a first argument.
        Argument:
            document string: Name of new document.
        '''
        for subscriber in self.subscribers:
            subscriber(document)