VENV := venv

install: venv

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

venv: $(VENV)/bin/activate

run: venv
	./$(VENV)/bin/python3 direction_finding_test_angles.py

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.png' -delete

.PHONY: all venv run clean