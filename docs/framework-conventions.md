# Framework Conventions

## Folder structure

- `config/` - environment and framework configuration files
- `pages/` - Page Object Model classes for UI pages
- `api/` - API client wrappers and service modules
- `utils/` - shared helpers, utilities, and support functions
- `tests/` - pytest cases organized by layer and test type
- `tests/data/` - structured test data and fixture inputs
- `artifacts/` - logs, screenshots, and generated runtime artifacts
- `reports/` - generated test report files

## Naming conventions

- Files and modules: `snake_case.py`
- Page classes: `PascalCase`
- Test files: `test_*.py`
- Test classes: `Test*`
- Test functions: `test_*`
- Config files: `config.yaml`, `pytest.ini`

## Design principles

- Keep UI flows inside page objects and keep assertions in tests.
- Centralize environment configuration in `config/config.yaml`.
- Use helpers in `utils/` for cross-cutting concerns like logging and HTTP calls.
- Avoid hard-coded test data; use data files under `tests/data/` or factory methods.
- Separate UI, API, and AI tests into distinct directories for maintainability.

## Extension guidance

- Add new page object modules under `pages/` with a corresponding file name.
- Add new API modules under `api/` and keep endpoint methods small and reusable.
- Add common fixtures to `tests/conftest.py` and keep them well-scoped.
- Add support utilities to `utils/` only when they are reusable across layers.
