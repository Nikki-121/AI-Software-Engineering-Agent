from services.llm_service import get_llm


def generate_code(requirement: str, plan: str):
    """
    Generate project code using the Coding Agent.
    """

    llm = get_llm()

    prompt = f"""
You are an expert software engineer.

Your job is to generate a clean, modular software implementation
based on the user's requirement and the development plan.

USER REQUIREMENT:
{requirement}

DEVELOPMENT PLAN:
{plan}

IMPLEMENTATION RULES:

1. Follow the development plan carefully.
2. Generate production-style, readable code.
3. Use meaningful file and function names.
4. Keep the project modular.
5. Include appropriate error handling.
6. Follow basic security best practices.
7. Avoid unnecessary dependencies.
8. Do not include fake or placeholder functionality unless necessary.
9. Include comments only where they improve understanding.
10. Make sure files work together correctly.
11. Generate all important files required for the project.
12. Include a README.md when appropriate.

OUTPUT FORMAT:

For every generated file, write:

FILE: path/to/file.ext

Then provide the complete code for that file.

Example:

FILE: backend/main.py

print("Hello")

Then continue with the next file.

IMPORTANT:

- Clearly provide the file path before every file.
- Do not combine multiple files under one file path.
- Do not skip important implementation files.
- Generate complete working code.
"""

    response = llm.invoke(prompt)

    return response.content
