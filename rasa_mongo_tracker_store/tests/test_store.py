import unittest
from unittest.mock import patch

from rasa_core.trackers import DialogueStateTracker
from mongomock import MongoClient as MockMongoClient

from rasa_mongo_tracker_store.store import MongoTrackerStore

class TestStore(unittest.TestCase):
    @patch('rasa_mongo_tracker_store.store.MongoClient')
    def test_store(self, ClientConstructor):
        ClientConstructor = MockMongoClient

        store = MongoTrackerStore(
            None, host='localhost', port=27017)
        assert store is not None

        tracker = DialogueStateTracker('some-id', [])

        store.save(tracker)
