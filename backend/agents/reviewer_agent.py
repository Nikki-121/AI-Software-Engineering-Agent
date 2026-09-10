from services.llm_service import get_llm


def review_code(requirement: str, generated_code: str):
    """
    Review AI-generated code for quality, correctness,
    security, maintainability, and potential issues.
    """

    llm = get_llm()

    prompt = f"""
You are a senior software code reviewer.

USER REQUIREMENT:
{requirement}

GENERATED CODE:
{generated_code}

Review the generated code carefully.

Check for:

1. Functional correctness
2. Logical errors
3. Missing functionality
4. Code quality
5. Project structure
6. Error handling
7. Security vulnerabilities
8. Performance issues
9. Maintainability
10. Best practices

Return the review using this structure:

CODE REVIEW

Overall Assessment:
<brief assessment>

Critical Issues:
- <issue>
- <issue>

Code Quality Issues:
- <issue>
- <issue>

Security Issues:
- <issue>
- <issue>

Performance Issues:
- <issue>
- <issue>

Recommended Improvements:
- <improvement>
- <improvement>

Final Verdict:
<Approved / Needs Improvement / Major Changes Required>

If a category has no issues, write:
"No major issues found."
"""

    response = llm.invoke(prompt)

    return response.content
