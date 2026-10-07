from unittest import TestCase

from src.upload_notifier import UploadNotifier


class TestUploadNotifier(TestCase):
    def setUp(self):
        self.notifier = UploadNotifier()

    def test_add_new_subscriber(self):
        def log(event):
            pass

        self.notifier.add_subscriber(log)

        expected = log
        result = self.notifier.subscribers[0]

        self.assertEqual(expected, result)

    def test_recieve_notification(self):
        expected = "upload new document"

        def notification_tester(event):
            self.assertEqual(event, expected)

        self.notifier.add_subscriber(notification_tester)

        self.notifier.notify_document_updated("upload new document")