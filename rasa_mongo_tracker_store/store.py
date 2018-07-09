from pymongo import MongoClient
from rasa_core.tracker_store import TrackerStore


class MongoTrackerStore(TrackerStore):
    """
    MongoTrackerStore stores rasa conversation trackers using MongoDB
    """
    def __init__(self, domain, database_name='rasa', collection='tracker_store',
                 host=None, port=None, tz_aware=None, connect=None):

        m_client = MongoClient(host=host, port=port,
                               tz_aware=tz_aware, connect=connect)
        self.collection = m_client[database_name][collection]
        super(MongoTrackerStore, self).__init__(domain)

    def save(self, tracker):
        serialised_tracker = self.serialise_tracker(tracker)
        self.collection.update_one(
            {'sender_id': tracker.sender_id},
            {'$set': {'sender_id': tracker.sender_id, 'tracker': serialised_tracker}},
            upsert=True)

    def retrieve(self, sender_id):
        stored = self.collection.find_one({'sender_id': sender_id})
        if stored is not None:
            return self.deserialise_tracker(sender_id, stored.get('tracker', None))
        return None

    def keys(self):
        pass
