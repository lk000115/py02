import re


def validate_string(s):
    """Validate common string properties."""
    return {
        'original': s,
        'is_alpha': s.isalpha(),
        'is_digit': s.isdigit(),
        'is_alnum': s.isalnum(),
        'is_ascii': s.isascii(),
        'has_whitespace': any(ch.isspace() for ch in s),
        'length': len(s),
        'contains_chinese': bool(re.search(r'[\u4e00-\u9fff]', s)),
        'contains_markdown': bool(re.search(r'(^|\n)(#{1,6}\s+)|(\[.*?\]\(.*?\))|(```)', s, re.MULTILINE)),
    }


if __name__ == '__main__':
    samples = [
        'hello',
        '12345',
        'abc123',
        '你好',
        'abc 123',
        '## Release Notes\n- Markdown preview',
    ]

    for text in samples:
        result = validate_string(text)
        print(f"Input: {text!r}")
        for key, value in result.items():
            print(f"  {key}: {value}")
        print()

