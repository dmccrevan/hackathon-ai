deps: requirements.txt
	pip install -r requirements.txt

run: build main.py
	env FLASK_APP=main.py flask run

build: cljs

static/cljs/main.js: src/todo/core.cljs
	clj -m cljs.main --optimizations advanced --output-dir static/cljs -c todo.core

cljs: static/cljs/main.js

cljs-repl:
	clj -m cljs.main --output-dir static/cljs -c todo.core -r

.PHONY: clean
clean:
	rm -rf __pycache__ **/__pycache__ **/*.pyc out/ static/cljs
