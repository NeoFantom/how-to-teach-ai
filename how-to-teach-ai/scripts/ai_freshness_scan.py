#!/usr/bin/env python3
"""Extract AI-tool freshness review candidates from Markdown files."""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

KEYWORDS = {
    "model_or_vendor": r"\b(GPT|OpenAI|Claude|Anthropic|Codex|Gemini|DeepSeek|Kimi|GLM|MIMOcode|Workybody|OpenCode|OpenClaw)\b|模型|大模型",
    "install_or_cli": r"\b(npm|pip|brew|curl|bun|uv|codex|claude)\b|安装|命令|CLI|终端|命令行",
    "api_or_secret": r"API\s*key|api key|token|secret|sk-[A-Za-z0-9]|密钥|凭证",
    "price_quota": r"价格|额度|免费|付费|quota|limit|rate limit|billing|subscription",
    "permission_sandbox": r"权限|审批|sandbox|沙箱|allow|deny|approval|读写|删除",
    "email_smtp": r"SMTP|邮箱|邮件|发信|send mail|IMAP",
    "ui_behavior": r"界面|按钮|菜单|快捷键|截图|面板|默认|版本|截至",
}
COMPILED = {k: re.compile(v, re.IGNORECASE) for k, v in KEYWORDS.items()}


def iter_markdown(root: Path):
    if root.is_file() and root.suffix.lower() == ".md":
        yield root
    else:
        yield from sorted(p for p in root.rglob("*.md") if ".git" not in p.parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", type=Path)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    root = args.path.resolve()
    if not root.exists():
        print(f"Path not found: {root}", file=sys.stderr)
        return 2

    rows = []
    base = root if root.is_dir() else root.parent
    for md in iter_markdown(root):
        for no, line in enumerate(md.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            risks = [name for name, rx in COMPILED.items() if rx.search(line)]
            if risks:
                rows.append({
                    "file": str(md.relative_to(base)),
                    "line": no,
                    "risk": "+".join(risks),
                    "text": line.strip()[:300],
                })

    if args.json:
        print(json.dumps({"count": len(rows), "rows": rows}, ensure_ascii=False, indent=2))
    else:
        writer = csv.DictWriter(sys.stdout, fieldnames=["file", "line", "risk", "text"])
        writer.writeheader()
        writer.writerows(rows)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
