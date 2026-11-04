# Security Policy

Skills are instructions for an AI agent, and some include helper scripts. A
malicious or careless skill can make an agent run harmful commands or leak data.

## What to report

- A skill or script that runs destructive commands, exfiltrates data, or
  downloads and executes remote code without making that clear.
- Hidden instructions (prompt injection) inside a skill.
- Committed secrets such as API keys or tokens.

## How to report

Use GitHub's [private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability)
on this repository (Security tab, "Report a vulnerability"). Please do not open
a public issue for security problems. You should get a response within 7 days.

## Using skills safely

Read a skill's `SKILL.md` and any scripts before installing it, especially
skills that run shell commands.
