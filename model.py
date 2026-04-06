def analyze_complexity(code):
    
    lines = len(code.split("\n"))
    loops = code.count("for ") + code.count("while ")
    conditions = code.count("if ")
    functions = code.count("def ")

    # Simple heuristic for time complexity
    if loops == 0:
        complexity = "O(1)"
    elif loops == 1:
        complexity = "O(n)"
    elif loops == 2:
        complexity = "O(n²)"
    elif loops >= 3:
        complexity = "O(n³) or higher"
    else:
        complexity = "Unknown"

    return {
        "lines": lines,
        "loops": loops,
        "conditions": conditions,
        "functions": functions,
        "complexity": complexity
    }