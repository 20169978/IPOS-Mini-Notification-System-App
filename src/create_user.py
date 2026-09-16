from admin import Admin
from editor import Editor
from viewer import Viewer

def create_user(user_type, name):
    '''
    This function returns User class.
    Arguments:
        str user_type: Need to be one of "admin", "editor" or "viewer". Case is matter.
        str name: Name of user. Cannot be brank.
    Return:
        Admin, Editor or Viewer.
        None if user_type match.
    '''
    if name.strip() == "":
        raise Exception("Name cannot be brank.")

    if user_type == "admin":
        return Admin(name)

    if user_type == "editor":
        return Editor(name)

    if user_type == "viewer":
        return Viewer(name)

    return None