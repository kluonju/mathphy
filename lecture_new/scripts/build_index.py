#!/usr/bin/env python3
"""Build a makeindex-compatible .ind file from a hyperref .idx file."""
import re
import sys
from collections import OrderedDict

encap_re = re.compile(r"^\\indexentry\{(.*)\|hyperpage\}\{(.*)\}$")


def sort_key(s):
    return re.sub(r"[^A-Za-z0-9]+", "", s).lower()


def main(idx_path, ind_path):
    entries = {}
    with open(idx_path, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            m = encap_re.match(line)
            if not m:
                continue
            key, page = m.group(1), m.group(2)
            parts = key.split("!")
            head, *rest = parts
            node = entries.setdefault(head, {"pages": [], "subs": {}})
            if rest:
                sub = "!".join(rest)
                subnode = node["subs"].setdefault(sub, [])
                if page not in subnode:
                    subnode.append(page)
            else:
                if page not in node["pages"]:
                    node["pages"].append(page)

    heads = sorted(entries, key=sort_key)
    lines = ["\\begin{theindex}", ""]
    last_letter = None
    for head in heads:
        letter = sort_key(head)[:1].upper()
        if last_letter is not None and letter != last_letter:
            lines.append("  \\indexspace")
            lines.append("")
        last_letter = letter
        pages = ", ".join(f"\\hyperpage{{{p}}}" for p in entries[head]["pages"])
        if pages:
            lines.append(f"  \\item {head}, {pages}")
        else:
            lines.append(f"  \\item {head}")
        for sub in sorted(entries[head]["subs"], key=sort_key):
            spages = ", ".join(
                f"\\hyperpage{{{p}}}" for p in entries[head]["subs"][sub]
            )
            lines.append(f"    \\subitem {sub}, {spages}")
    lines.append("")
    lines.append("\\end{theindex}")
    with open(ind_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    idx = sys.argv[1] if len(sys.argv) > 1 else "main.idx"
    ind = sys.argv[2] if len(sys.argv) > 2 else "main.ind"
    main(idx, ind)
