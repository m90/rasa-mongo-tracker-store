package: setup.py
	@python3 setup.py sdist bdist_wheel

publish: package
	@twine upload dist/*

.PHONY: publish
