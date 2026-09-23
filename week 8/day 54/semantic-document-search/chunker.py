DEFAULT_SEPARATORS = [
    "\n\n",
    "\n",
    ". ",
    " ",
    ""
]


def recursive_split(
    text: str,
    chunk_size: int = 500,
    separators=None
):
    if separators is None:
        separators = DEFAULT_SEPARATORS

    text = text.strip()

    if not text:
        return []

    if len(text) <= chunk_size:
        return [text]

    if not separators:
        return [
            text[i:i + chunk_size].strip()
            for i in range(0, len(text), chunk_size)
            if text[i:i + chunk_size].strip()
        ]

    separator = separators[0]

    # Final fallback: character-level splitting
    if separator == "":
        return [
            text[i:i + chunk_size].strip()
            for i in range(0, len(text), chunk_size)
            if text[i:i + chunk_size].strip()
        ]

    pieces = [
        piece.strip()
        for piece in text.split(separator)
        if piece.strip()
    ]

    # This separator wasn't useful, try the next one
    if len(pieces) <= 1:
        return recursive_split(
            text,
            chunk_size,
            separators[1:]
        )

    chunks = []
    current_chunk = ""

    for piece in pieces:

        if not current_chunk:
            current_chunk = piece
            continue

        candidate = current_chunk + separator + piece

        if len(candidate) <= chunk_size:
            current_chunk = candidate

        else:
            chunks.append(current_chunk)

            # A single piece can itself be too large
            if len(piece) > chunk_size:
                smaller_chunks = recursive_split(
                    piece,
                    chunk_size,
                    separators[1:]
                )

                chunks.extend(smaller_chunks)
                current_chunk = ""

            else:
                current_chunk = piece

    if current_chunk:
        chunks.append(current_chunk)

    return chunks