
# install poetry
install:
# pip install -Uq poetry
	poetry env activate
# poetry self update
	poetry lock
	poetry install

