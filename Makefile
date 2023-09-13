run:
	FLASK_APP=app FLASK_ENV=development flask run

log:
	export PYTHONPATH=$$PYTHONPATH:$(shell pwd) && python3 tests/generate_log.py --name $(shell echo $(name) | tr A-Z a-z) --size $(size)

.PHONY: log

clean:
	@rm -f *.log

.PHONY: clean-logs