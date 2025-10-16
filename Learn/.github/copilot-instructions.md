# Copilot Instructions for AI Coding Agents

## Project Overview
This workspace contains a collection of Python scripts for learning and practice, including individual problems (`Problem1.py` to `Problem45.py`) and a `Mini project` folder. Each file is self-contained and typically solves a single problem or demonstrates a specific concept. There is no central application architecture or shared module structure.

## File Organization
- **Problem Files:** Each `ProblemXX.py` file is independent. They do not import from each other and usually start with input prompts and direct logic.
- **Mini Project:** The `Mini project.py` file in the `Mini project/` folder may contain more complex or multi-step logic. Treat it as a standalone script unless you discover explicit imports or references to other files.

## Developer Workflows
- **Running Code:** Execute scripts directly using Python (e.g., `python Problem1.py`). No build system or test framework is present.
- **Debugging:** Use print statements or Python's built-in debugging tools. There are no custom logging or error handling conventions.

## Patterns and Conventions
- **Input/Output:** Most scripts use `input()` for user input and `print()` for output. Avoid adding external dependencies unless explicitly requested.
- **Variable Naming:** Variable names are short and descriptive, often matching the problem context (e.g., `sum`, `dict_rom`).
- **No External Libraries:** Unless specified, do not introduce third-party packages.
- **No Shared State:** Scripts do not share data or state. Avoid cross-file imports unless you find explicit code requiring it.

## Integration Points
- **No External APIs or Services:** All logic is local and self-contained.
- **No Database or Persistent Storage:** Data is handled in-memory within each script.

## Examples
- Roman numeral conversion in `Problem45.py` uses a dictionary for mapping and a loop for calculation.
- The `Mini project.py` may contain more advanced logic, but follows the same standalone pattern.

## How to Contribute
- Add new problem files as `ProblemXX.py`.
- For larger projects, create a new folder and keep logic self-contained.
- Follow the input/output and naming conventions observed in existing files.

---
If any section is unclear or missing details, please provide feedback so this guide can be improved for future AI agents.
