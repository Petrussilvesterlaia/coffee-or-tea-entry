"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter to /output/entry.txt: "A" for coffee.
The output is a single byte, no newline, no extra text.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
LETTER = "A"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(LETTER.encode("utf-8"))

    # Verifikasi mandiri: baca kembali output dan pastikan isinya tepat
    # satu byte yang sama dengan huruf yang ditetapkan.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != LETTER.encode("utf-8"):
        raise SystemExit(
            "verifikasi gagal: isi /output/entry.txt tidak cocok "
            f"dengan huruf {LETTER!r}"
        )


if __name__ == "__main__":
    main()
