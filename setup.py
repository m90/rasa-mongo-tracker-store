import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rasa_mongo_tracker_store",
    version="0.1.0",
    author="Frederik Ring",
    author_email="frederik.ring@gmail.com",
    description="TrackerStore for rasa_core connecting to MongoDB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/m90/rasa-mongo-tracker-store",
    packages=["rasa_mongo_tracker_store"],
    install_requires=[
        "dialogflow==0.4",
        "pymongo==3.7",
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
