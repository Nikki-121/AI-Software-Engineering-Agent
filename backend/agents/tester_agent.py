from services.llm_service import get_llm


def test_code(requirement: str, generated_code: str):
    """
    Generate test cases and identify possible bugs or edge cases
    in the AI-generated code.
    """

    llm = get_llm()

    prompt = f"""
You are a senior software testing engineer.

USER REQUIREMENT:
{requirement}

GENERATED CODE:
{generated_code}

Analyze the generated code and create a testing report.

Check for:

1. Functional bugs
2. Missing edge cases
3. Invalid inputs
4. Error handling problems
5. Security-related test cases
6. Integration issues
7. Boundary conditions
8. Expected vs actual behavior

Create practical test cases.

Return the result using this structure:

TESTING REPORT

Test Summary:
<brief summary>

Test Cases:

1. Test Case:
   Description:
   Input:
   Expected Result:
   Priority:

2. Test Case:
   Description:
   Input:
   Expected Result:
   Priority:

Potential Bugs:
- <bug>
- <bug>

Edge Cases:
- <edge case>
- <edge case>

Security Tests:
- <test>
- <test>

Overall Testing Status:
<Passed / Passed with Warnings / Failed>

Recommended Fixes:
- <fix>
- <fix>

If there are no issues in a category, write:
"No major issues found."
"""

    response = llm.invoke(prompt)

    return response.content
