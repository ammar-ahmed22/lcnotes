.PHONY: run

run:
	@if [ -z "$$VIRTUAL_ENV" ]; then  \
		echo "Error: No virtual environment activated."; \
		echo "Please activate a virtual environment first and try again (e.g 'source venv/bin/activate')"; \
		exit 1; \
	else \
		echo "✅ Virtual environment detected"; \
		python3 -m pip install -e .; \
		echo "Successfully installed 'lc'. Try with 'lc --help'"; \
	fi
