# Claude Camp Week 3 — String Tools Project

## Overview

This project is a beginner Python assignment focused on:

* Python functions
* string manipulation
* pytest unit testing
* Git/GitHub workflow
* repository organization

---

# Project Structure

```text
claude-camp-w3/
│
├── .gitignore
│
├── string-tools-project/
│   ├── string_utility.py
│   └── test_string_utility.py
```

---

# Features

## reverse_word(word)

Reverses a string.

Example:

```python
reverse_word("hello")
# "olleh"
```

## count_vowels(text)

Counts vowels in a string.

Example:

```python
count_vowels("hello")
# 2
```

## is_palindrome(text)

Checks whether a string is a palindrome.

Example:

```python
is_palindrome("madam")
# True
```

---

# Running Tests

Install pytest:

```bash
python -m pip install pytest
```

Run tests:

```bash
python -m pytest
```

Expected result:

```text
10 passed
```

---

# Git Workflow

```bash
git checkout -b project-3-string-tools-project
git add .
git commit -m "Complete string tools project with pytest"
git push -u origin project-3-string-tools-project
```

---

# .gitignore

```text
__pycache__/
.pytest_cache/
*.pyc
```

---

# Key Learning Outcomes

* reusable Python functions
* string slicing and list operations
* defensive programming
* pytest testing
* debugging workflow
* Git branches and commits
* GitHub collaboration
* clean repository management

---

# Technologies Used

* Python 3.14
* pytest 9.0.3
* Git
* GitHub
* Visual Studio Code

---

# Author

Spring Shi
GitHub: springshi2011-cloud
