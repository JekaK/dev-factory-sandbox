# SPDX-License-Identifier: MIT


def file_count(count: int) -> str:
    """Format the number of files shown in a status label."""
    noun = "file" if count <= 1 else "files"
    return f"{count} {noun}"
