# PlaywrightDemo

[![Python Playwright CI](https://github.com/Prajapati-umesh/PlaywrightDemo/actions/workflows/python-playwright.yml/badge.svg)](https://github.com/Prajapati-umesh/PlaywrightDemo/actions/workflows/python-playwright.yml)

A scalable Playwright test automation framework template using Python and pytest. This layout supports enterprise needs for UI automation, API validation, data-driven testing, logging, reporting, and CI/CD.

## Recommended folder structure

- `config/` - environment definitions, test settings, and framework configuration.
- `pages/` - Page Object Model classes for UI page abstractions.
- `api/` - reusable HTTP client wrappers and endpoint modules.
- `utils/` - shared helpers such as configuration loading, logging, HTTP utilities, and common utilities.
- `tests/` - pytest test modules grouped by layer, plus fixtures and sample data.
- `artifacts/` - generated runtime outputs such as logs, screenshots, and temporary files.
- `reports/` - generated test reports and results.
- `docs/` - framework onboarding, conventions, and extension guidance.

## Structure details

- `config/config.yaml` stores environment-specific values for `dev`, `qa`, and `prod`.
- `utils/config_reader.py` centralizes environment loading and retrieval.
- `utils/logger_util.py` encapsulates logging setup with file and console handlers.
- `pages/base_page.py` is the POM base class used by UI page objects.
- `api/sample_api.py` shows a reusable API client wrapper.
- `tests/conftest.py` defines shared pytest fixtures for configuration, logging, and Playwright sessions.
- `tests/base_test.py` provides a base test class for reusable setup.
- `tests/ui/` contains UI-focused test cases.
- `tests/api/` contains API-focused test cases.
- `tests/data/` is for sample test data and fixtures.

## Naming conventions

- Python modules: `snake_case.py`
- Page classes: `PascalCase` names, file names in `snake_case`
- Fixtures and helper functions: `snake_case`
- Test files: `test_*.py`
- Test classes: `Test*`
- Test methods: `test_*`
- Configuration files: `config.yaml`, `pytest.ini`, `.gitignore`

## Sample execution

Install dependencies:

```bash
python -m pip install -U pip
python -m pip install -r requirements.txt
python -m playwright install
```

Run all tests:

```bash
pytest
```

Run only UI tests:

```bash
pytest tests/ui
```

Run only API tests:

```bash
pytest tests/api
```

Run with a specific environment:

```bash
TEST_ENV=qa pytest
```

Run with GitHub Actions locally using `act`:

```bash
act -P ubuntu-latest=nektos/act-environments-ubuntu:23.10
```

## CI/CD readiness

This structure is designed for CI/CD pipelines with:

- `pytest` execution
- HTML and JUnit result generation
- centralized configuration
- reusable fixtures and page objects
- explicit separation of UI and API layers
- artifact directory support for logs and reports
- GitHub Actions workflow at `.github/workflows/python-playwright.yml`

## Documentation and maintenance notes

- `README.md` provides the high-level framework layout and execution patterns.
- Use `tests/data/` for structured test data and fixture-driven inputs.
- Add new page objects under `pages/` and group them by domain.
- Keep API wrappers in `api/` and support environment-specific base URLs through `config/config.yaml`.
- Extend `utils/` for reusable helpers like custom reporting, authentication tokens, or data generation.
- Store long-term design patterns or usage examples in a `docs/` folder if the project grows beyond the initial boilerplate.
