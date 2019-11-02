deps: requirements.txt
	pip install -r requirements.txt

run: build main.py
	env FLASK_APP=main.py flask run

build: deps
	echo "building..."

.PHONY: clean
clean:
	rm -rf **/__pycache__ **/*.pyc
