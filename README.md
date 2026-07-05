# how-to-teach-ai

`how-to-teach-ai` 是一个同时兼容 **Claude Code** 和 **Codex**、并依赖 [`tutorialize-skill`](https://github.com/NeoFantom/tutorialize-skill) 的 Agent Skill，用来设计、撰写和审查面向普通人的 AI / AI Agent 教程。

它不是通用教程法本身；通用部分放在 `tutorialize-skill`。本 skill 只保留 AI 教学特化内容：Agent 概念、安装上手、命令行恐惧、API key、权限、安全、隐私、工具事实新鲜度、办公和科研分线示例等。

## 致谢

本项目的 AI 教学方法受到 [stormzhang/ai-coding-guide](https://github.com/stormzhang/ai-coding-guide) 启发，并依赖通用的 [`tutorialize-skill`](https://github.com/NeoFantom/tutorialize-skill)。我们学习的是其面向新手的课程组织、章节脚手架、资产管理和 Markdown 质量维护方法；本项目未复制其正文、图片或章节内容，所有 AI 教学规则均为重新抽象与原创实现。

如果你正在学习 AI Coding，也建议直接阅读原项目；本仓库只提供 AI 教程生产 workflow，不替代原教程。

## 兼容性

同一个 skill 目录可用于：

- **Claude Code**：安装到 `~/.claude/skills/how-to-teach-ai` 或项目内 `.claude/skills/how-to-teach-ai`，在 Claude Code 中可用 `/how-to-teach-ai` 调用。
- **Codex**：安装到 Codex skills 目录，或在支持 Agent Skills 的环境中作为一个包含 `SKILL.md` 的 skill 目录使用，可用 `$how-to-teach-ai` 显式提及。

## 安装

先安装 `tutorialize-skill`，再安装本 skill：

```bash
git clone https://github.com/NeoFantom/tutorialize-skill.git
git clone https://github.com/NeoFantom/how-to-teach-ai.git
```

### Claude Code

```bash
mkdir -p "$HOME/.claude/skills"
ln -s "$PWD/tutorialize-skill/tutorialize-skill" "$HOME/.claude/skills/tutorialize-skill"
ln -s "$PWD/how-to-teach-ai/how-to-teach-ai" "$HOME/.claude/skills/how-to-teach-ai"
```

### Codex

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
ln -s "$PWD/tutorialize-skill/tutorialize-skill" "${CODEX_HOME:-$HOME/.codex}/skills/tutorialize-skill"
ln -s "$PWD/how-to-teach-ai/how-to-teach-ai" "${CODEX_HOME:-$HOME/.codex}/skills/how-to-teach-ai"
```

如果你的 Codex 环境使用 Agent Skills 标准目录，也可以安装到：

```bash
mkdir -p "$HOME/.agents/skills"
ln -s "$PWD/tutorialize-skill/tutorialize-skill" "$HOME/.agents/skills/tutorialize-skill"
ln -s "$PWD/how-to-teach-ai/how-to-teach-ai" "$HOME/.agents/skills/how-to-teach-ai"
```

## 使用

```text
Use $how-to-teach-ai with $tutorialize-skill to design an AI Agent tutorial for office staff.
```

Claude Code 中也可以用：

```text
/how-to-teach-ai Design an AI Agent tutorial for office staff, using tutorialize-skill as the general method.
```

```text
Use $how-to-teach-ai to split this AI course into shared basics, office track, research track, workflows, and safety.
```

## 设计边界

- 通用教程结构、章节模板、Markdown QA、资产规范：属于 `tutorialize-skill`。
- AI/Agent 专有顺序、安全、事实新鲜度、办公/科研案例：属于本 skill。
- 任何会发送邮件、公开发布、删除数据、消耗额度、触碰敏感信息的内容，都必须先教风险和人工确认。

## 仓库结构

```text
how-to-teach-ai/
├── README.md
├── LICENSE
└── how-to-teach-ai/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/
    │   ├── ai-curriculum-map.md
    │   └── ai-safety-and-freshness.md
    └── scripts/
        └── ai_freshness_scan.py
```

## AI 事实新鲜度扫描

```bash
python how-to-teach-ai/scripts/ai_freshness_scan.py path/to/ai-tutorial > freshness.csv
```

这个脚本只创建复核队列，不替代官方文档核验。

## License

MIT
