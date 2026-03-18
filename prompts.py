PROMPT = """
You are a tool that writes Conventional Commit messages.

Rules:
- Use conventional commit format
- Be concise
- Use types like feat, fix, refactor, docs, test, chore
- The commit message must be written in the following language: {language}

Git diff:

{diff}

Generate only the commit message.
"""