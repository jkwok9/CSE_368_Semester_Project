
from pathlib import Path

import pymupdf


def extract_text(filename: str, contents: bytes) -> str:
    """Return selectable text or raise ValueError with a user-facing message."""
    extension = Path(filename).suffix.lower()
    if extension not in {".pdf", ".txt"}:
        raise ValueError("Upload a PDF or TXT file.")
    if not contents:
        raise ValueError("This file is empty. Upload another file or paste the text.")

    if extension == ".pdf":
        try:
            with pymupdf.open(stream=contents, filetype="pdf") as document:
                if not document.is_pdf:
                    raise ValueError("Upload a valid PDF or paste the text.")
                if document.needs_pass:
                    raise ValueError("Upload an unlocked PDF or paste the text.")
                pages = [page.get_text(sort=True).strip() for page in document]
        except (RuntimeError, OSError) as error:
            raise ValueError("Could not read this PDF. Upload another file or paste the text.") from error

        text = "\n\n".join(page for page in pages if page)
        if not text:
            raise ValueError("This PDF has no selectable text. Paste the text or upload a text-based PDF.")
    else:
        try:
            text = contents.decode("utf-8-sig").strip()
        except UnicodeDecodeError as error:
            raise ValueError("Save this TXT file as UTF-8 or paste the text.") from error
        if "\x00" in text:
            raise ValueError("Save this TXT file as UTF-8 or paste the text.")
        if not text:
            raise ValueError("This file contains no text. Upload another file or paste the text.")

    return text
