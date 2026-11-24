import os

ROAST = "My phone charger only works at exactly 37 degrees — I'm cracking a safe, not charging a phone."


def writeEntry(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)


writeEntry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
