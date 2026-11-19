import pytest

from app_rag_assistant.chunking import chunk_text


def test_splits_text_into_equal_chunks() -> None:
    assert chunk_text("abcdef", 2) == ["ab", "cd", "ef"]


def test_last_chunk_can_be_shorter() -> None:
    assert chunk_text("abcde", 2) == ["ab", "cd", "e"]


def test_empty_text_returns_empty_list() -> None:
    assert chunk_text("", 3) == []


@pytest.mark.parametrize("size", [0, -1])
def test_rejects_non_positive_size(size: int) -> None:
    with pytest.raises(ValueError):
        chunk_text("abc", size)
