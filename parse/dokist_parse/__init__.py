"""DOKIST Parse — Python facade over the Rust extension.

Usage:
    from dokist_parse import parse_pdf_bytes, normalize_text, TextBlock

    blocks = parse_pdf_bytes(pdf_bytes)
    for b in blocks:
        print(b.page, b.char_start, b.char_end, b.lang, b.text)
"""
from ._dokist_parse import parse_pdf_bytes, normalize_text, TextBlock

__all__ = ["parse_pdf_bytes", "normalize_text", "TextBlock"]
