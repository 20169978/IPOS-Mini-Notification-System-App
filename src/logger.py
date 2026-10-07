from functools import wraps

def action_logger(func):
    '''
    Defines the decorator '@action_logger'.

    When you put this decorator on your function,
    it will automatically make logs on the console.

    Example:

        @action_logger
        def upload_document(username, document_title):
            print("document uploaded")

        upload_document("Bob", "IPOS-Assessment")

    Console:

        -----Action: upload_document-----
        Arguments:
        args=('Bob', 'IPOS-Assessment')
        kwargs={}
        document uploaded
        -----Action Completed-----
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"-----Action: {func.__name__}-----")

        print(f"Arguments:\n args={args}\nkwargs={kwargs}")

        result = func(*args, **kwargs)

        print("-----Action Completed-----")

        return result
    return wrapper

def user_action_logger(action):
    '''
    Defines the decorator '@user_action_logger(action)'.

    When you put this decorator on your function,
    it will automatically make logs on the console 
    with given action and user name.
    Specificly, this decolator shold be used in class which has 'name' instance attribute.

    Argument:
        action string: action's title.

    Example:
        class User:
            def __init__(self, name):
                self.name = name

            @user_action_logger("upload document")
            def upload_document(self, document):
                print("document upload")

        user = User("Bob")
        user.upload_document("IPOS-Assessment")
    Console:

        -----Action: upload_document-----
        Bob do upload document
        document uploaded
        -----Action Completed-----
    '''
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            print(f"-----Action Starts-----")

            print(f"{self.name} do {action}")

            result = func(self, *args, **kwargs)

            print("-----Action Completed-----")

            return result
        return wrapper
    return decorator


