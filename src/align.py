"""A module for translating between alignments and edits sequences."""


def align(x: str, y: str, edits: str) -> tuple[str, str]:
    """Align two sequences from a sequence of edits.

    Args:
        x (str): The first sequence to align.
        y (str): The second sequence to align
        edits (str): The list of edits to apply, given as a string

    Returns:
        tuple[str, str]: The two rows in the pairwise alignment

    >>> align("ACCACAGTCATA", "ACAGAGTACAAA", "MDMMMMMMIMMMM")
    ('ACCACAGT-CATA', 'A-CAGAGTACAAA')

    """
    x, y = iter(x), iter(y)
    seq1, seq2 = list(), list()
    for i, edit in enumerate(edits):
        match edit:
            case 'M':
                seq1.append(next(x))
                seq2.append(next(y))
            case 'D':
                seq1.append(next(x))
                seq2.append('-')
            case 'I':
                seq1.append('-')
                seq2.append(next(y))
    return "".join(seq1), "".join(seq2)

def get_edit_operation(x: str, y: str) -> str:
    if x == '-':
        return 'I'
    elif y == '-':
        return 'D'
    else:
        return 'M'

def edits(x: str, y: str) -> str:
    """Extract the edit operations from a pairwise alignment.

    Args:
        x (str): The first row in the pairwise alignment.
        y (str): The second row in the pairwise alignment.

    Returns:
        str: The list of edit operations as a string.

    >>> edits('ACCACAGT-CATA', 'A-CAGAGTACAAA')
    'MDMMMMMMIMMMM'

    """
    return "".join(get_edit_operation(values[0], values[1]) for values in zip(x, y))
