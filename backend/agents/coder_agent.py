from services.llm_service import get_llm


def generate_code(requirement: str, plan: str):
    llm = get_llm()

    prompt = f"""
You are an expert software engineer.

User requirement:
{requirement}

Development plan:
{plan}

Generate the initial implementation for this project.

Requirements:
1. Follow the development plan.
2. Create clean, modular code.
3. Use meaningful file and function names.
4. Include error handling where appropriate.
5. Follow basic security best practices.
6. Include comments only where they improve understanding.
7. Clearly separate different files in your response.

For every file, use this format:

FILE: path/to/file.ext

```language
code
