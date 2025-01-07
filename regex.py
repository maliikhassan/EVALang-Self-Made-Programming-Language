import re

# Token specifications
TOKEN_SPECIFICATIONS = [
    ("KEYWORD", r"\b(if|else|while|for|int|float|bool|return|function)\b"),  # Keywords
    ("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_][a-zA-Z_0-9][a-z_A-Z0-9]*"),                             # Identifiers
    ("INTEGER", r"\b\d+\b"),                                               # Integer literals
    ("FLOAT", r"\b\d+\.\d+\b"),                                            # Floating-point literals
    ("BOOLEAN", r"\b(true|false)\b"),                                      # Boolean literals
    ("OPERATOR", r"(==|!=|<=|>=|<|>|\+|-|\*|/|&&|\|\||!)"),                # Operators
    ("DELIMITER", r"[\(\)\{\};,]"),                                        # Delimiters
    ("STRING", r'"(?:\\.|[^"\\])*"'),                                      # String literals
    ("COMMENT_SINGLE", r"##.*"),                                           # Single-line comments
    ("WHITESPACE", r"\s+"),                                                # Whitespace (ignored)
]

# Compile the regex patterns into a single master pattern
master_pattern = re.compile(
    "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPECIFICATIONS)
)

# Tokenize function
def tokenize(source_code):
    tokens = []
    for match in master_pattern.finditer(source_code):
        token_type = match.lastgroup  # The name of the matched group
        token_value = match.group(token_type)
        if token_type != "WHITESPACE" and not token_type.startswith("COMMENT"):  # Ignore whitespace and comments
            tokens.append((token_type, token_value))
    return tokens

