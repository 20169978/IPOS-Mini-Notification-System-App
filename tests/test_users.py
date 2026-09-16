from unittest import TestCase

from src.create_user import create_user

class TestUsers(TestCase):
    def test_admin_creation(self):
        admin = create_user("admin", "admin_1")

        result = admin.name

        expected = "admin_1"

        self.assertEqual(result, expected)

    def test_editor_creation(self):
        editor = create_user("editor", "editor_1")

        result = editor.name

        expected = "editor_1"

        self.assertEqual(result, expected)

    def test_viewer_creation(self):
        viewer = create_user("viewer", "viewer_1")

        result = viewer.name

        expected = "viewer_1"

        self.assertEqual(result, expected)

    def test_none_returned(self):
        result = create_user("user", "user_1")

        expected = None

        self.assertEqual(result, expected)

    def test_error_rised(self):
        with self.assertRaises(Exception):
            create_user("admin", "   ")

        