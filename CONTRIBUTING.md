# Contributing to LaptopXplorer

First off, thank you for considering contributing to LaptopXplorer! It's people like you that make LaptopXplorer such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps which reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed after following the steps**
* **Explain which behavior you expected to see instead and why**
* **Include screenshots if possible**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a step-by-step description of the suggested enhancement**
* **Provide specific examples to demonstrate the steps**
* **Describe the current behavior and explain which behavior you expected to see instead**
* **Explain why this enhancement would be useful**

### Pull Requests

* Fill in the required template
* Do not include issue numbers in the PR title
* Follow the Python/Django style guides
* Include screenshots in your pull request whenever possible
* End all files with a newline
* Avoid platform-dependent code

## Development Setup

1. Fork the repo
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR-USERNAME/laptopXplorer.git
   cd laptopXplorer
   ```

3. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On Mac/Linux
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run migrations:
   ```bash
   cd src
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Populate database (optional):
   ```bash
   python manage.py populate_db
   ```

8. Run development server:
   ```bash
   python manage.py runserver
   ```

## Style Guidelines

### Python Style Guide

* Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
* Use 4 spaces for indentation (not tabs)
* Use docstrings for functions and classes
* Keep lines under 100 characters when possible

### Django Style Guide

* Use Django's built-in features when possible
* Follow Django's model, view, template naming conventions
* Use Django's forms for data validation
* Write database queries efficiently (use select_related, prefetch_related)

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

### Template Style Guide

* Use 4 spaces for indentation
* Follow Tailwind CSS utility-first approach
* Keep templates readable and well-organized
* Use meaningful class names

## Testing

* Write tests for new features
* Ensure all tests pass before submitting PR
* Run tests with: `python manage.py test`

## Documentation

* Update README.md if needed
* Add docstrings to new functions/classes
* Update inline comments for complex logic

## Recognition

Contributors will be recognized in our README.md file.

Thank you for contributing! 🎉
