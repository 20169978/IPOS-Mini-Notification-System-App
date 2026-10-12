from unittest import TestCase
import asyncio
from src.fetch_metadata import fetch_metadata

class TestFetchMetadata(TestCase):
    def setUp(self):
        self.doc_ids = [1, 2, 3]
        self.invalid_id = 999999

    def test_fetch_metadata(self):
        metadata = asyncio.run(fetch_metadata(self.doc_ids[0]))
        self.assertIsNotNone(metadata)
        self.assertEqual(metadata.get('id'), self.doc_ids[0])

        metadata = asyncio.run(fetch_metadata(self.invalid_id))
        self.assertEqual(metadata, {})

    def test_concurrent_fetches(self):
        expected = 3
        async def run_gather():
            tasks = [fetch_metadata(i) for i in self.doc_ids]
            return await asyncio.gather(*tasks)
        
        results = asyncio.run(run_gather())
        self.assertEqual(len(results), expected)

    def test_fetch_error_handling(self):
        invalid_id = 999999
        result = asyncio.run(fetch_metadata(invalid_id))
        self.assertEqual(result, {})