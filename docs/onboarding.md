# Onboarding

Welcome to the PlaywrightDemo automation framework.

## Getting started

1. Install dependencies:

```bash
python -m pip install -U pip
pip install -r requirements.txt
python -m playwright install
```

2. Run all tests:

```bash
pytest
```

3. Run UI tests only:

```bash
pytest tests/ui
```

4. Run API tests only:

```bash
pytest tests/api
```

5. Run with a specific environment:

```bash
TEST_ENV=qa pytest
```

## Folder overview

- `config/` - environment settings
- `pages/` - POM page classes
- `api/` - API service wrappers
- `utils/` - shared utilities
- `tests/` - test cases and fixtures
- `docs/` - framework documentation

## CI usage

The GitHub Actions workflow is located at `.github/workflows/python-playwright.yml`.

### Local workflow execution

If you want to run the CI workflow locally, use:

```bash
act -P ubuntu-latest=nektos/act-environments-ubuntu:23.10
```

## Contributing

- Keep test logic in `tests/`
- Keep page interaction code in `pages/`
- Keep API interaction code in `api/`
- Keep shared helpers in `utils/`
- Keep environment values in `config/config.yaml`
