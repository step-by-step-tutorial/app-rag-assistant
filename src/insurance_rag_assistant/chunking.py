"""Text chunking utilities."""


def chunk_text(text: str, size: int) -> list[str]:
    """Split text into consecutive chunks of at most `size` characters."""
    if size <= 0:
        raise ValueError("size must be positive")
    return [text[i : i + size] for i in range(0, len(text), size)]
