## Deprecation notice

Starting with `rasa_core` 0.11, a `MongoTrackerStore` is included in the core package, i.e. there is no need to use this package anymore in case you are running an up-to-date version of `rasa_core`.

---

# rasa-mongo-tracker-store
[![Build Status](https://travis-ci.org/m90/rasa-mongo-tracker-store.svg?branch=master)](https://travis-ci.org/m90/rasa-mongo-tracker-store)
> `TrackerStore` for rasa_core connecting to MongoDB

## Installation

Install the package using pip:

```sh
pip install python_mongo_tracker_store
```

## Usage

`MongoTrackerStore` can be used when loading or instantiating an Agent:

```py
from rasa_mongo_tracker_store.store import MongoTrackerStore

agent = Agent.load(
    'path/to/dialogue/models',
    tracker_store=MongoTrackerStore(
        None, # rasa's internal logic will set the domain lateron
        host='localhost', port=27017, database_name='rasa',
        collection='trackers',
    ))

```

### License
MIT © [Frederik Ring](http://www.frederikring.com)

