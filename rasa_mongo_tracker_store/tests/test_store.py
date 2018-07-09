import unittest
from unittest.mock import patch

from rasa_core.trackers import DialogueStateTracker
from rasa_core.domain import TemplateDomain
from mongomock import MongoClient as MockMongoClient

from rasa_mongo_tracker_store.store import MongoTrackerStore

class TestStore(unittest.TestCase):
    @patch('rasa_mongo_tracker_store.store.MongoClient', MockMongoClient)
    def test_store(self):
        domain = TemplateDomain.load("rasa_mongo_tracker_store/tests/test_domain.yml")

        store = MongoTrackerStore(
            domain, host='localhost', port=27017)
        assert store is not None

        original = DialogueStateTracker('some-id', [])
        store.save(original)

        result = store.retrieve('some-id')
        assert result == original

        unknown = store.retrieve('unknown-id')
        assert unknown is None
