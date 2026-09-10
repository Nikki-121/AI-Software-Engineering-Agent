from services.llm_service import get_llm


def create_plan(requirement: str):
    llm = get_llm()

    prompt = f"""
You are a senior software architect.

Analyze the following software requirement:

{requirement}

Create a clear development plan.

Your response must contain:

1. Project understanding
2. Required features
3. Recommended technology stack
4. Project folder structure
5. Development tasks in order
6. Potential technical challenges
7. Testing requirements

Keep the plan practical and suitable for implementation.
"""

    response = llm.invoke(prompt)

    return response.content
