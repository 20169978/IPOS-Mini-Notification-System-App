from unittest import TestCase

from src.logger import action_logger, user_action_logger
from src.readLogs import read_logs
class TestLogger(TestCase):
    def test_user_action_logger_works(self):
        class User:
            def __init__(self):
                self.name = "test"

            @user_action_logger("test action")
            def sum(self, num1, num2):
                return num1 + num2

        user = User()

        expected = 30

        result = user.sum(13, 17)

        self.assertEqual(result, expected)
        
    def test_read_logs(self):
        logs = list(read_logs("tetsing.txt"))

        self.assertGreater(len(logs), 0)
