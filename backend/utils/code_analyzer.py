import ast


def analyze_python_code(code: str):
    """
    Perform basic static analysis on Python source code.

    Returns syntax status, functions, classes, imports,
    and basic code statistics.
    """

    result = {
        "syntax_valid": False,
        "functions": [],
        "classes": [],
        "imports": [],
        "lines": len(code.splitlines()),
        "issues": []
    }

    if not code.strip():
        result["issues"].append("Code is empty.")
        return result

    try:
        tree = ast.parse(code)

    except SyntaxError as error:
        result["issues"].append(
            f"Syntax error at line {error.lineno}: {error.msg}"
        )
        return result

    result["syntax_valid"] = True

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            result["functions"].append(node.name)

        elif isinstance(node, ast.AsyncFunctionDef):
            result["functions"].append(node.name)

        elif isinstance(node, ast.ClassDef):
            result["classes"].append(node.name)

        elif isinstance(node, ast.Import):
            for alias in node.names:
                result["imports"].append(alias.name)

        elif isinstance(node, ast.ImportFrom):
            if node.module:
                result["imports"].append(node.module)

    if not result["functions"] and not result["classes"]:
        result["issues"].append(
            "No functions or classes were detected."
        )

    return result
