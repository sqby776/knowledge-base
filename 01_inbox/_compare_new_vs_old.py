#!/usr/bin/env python3
"""Compare new vs. existing Hermes Agent page captures to detect structural changes."""
import re, sys

# Read new capture
with open("/home/sqby776/workspace/knowledge/01_inbox/articles/2026-07-07_Hermes_Agent.md") as f:
    new_content = f.read()

# Read existing compiled note (stripping the changelog part)
with open("/home/sqby776/workspace/knowledge/02-笔记/概念/Hermes-Agent.md") as f:
    old_note = f.read()

# Extract just the frontmatter + body of the old note (before the changelog blocks that start with "> **")
old_body_match = re.match(r'^(.*?)(?=\n> \*\*|\n> ###)', old_note, re.DOTALL)
if old_body_match:
    old_body = old_body_match.group(1)
else:
    old_body = old_note

# Extract the key sections from both
def extract_sections(text):
    """Extract structured content, ignoring frontmatter and nav links."""
    lines = text.split('\n')
    clean = []
    for line in lines:
        # Skip frontmatter
        if line.startswith('---'):
            continue
        # Skip nav/community links
        if line.strip().startswith('* ['):
            continue
        if 'hermes-agent.nousresearch.com' in line and ('Edit this page' in line or 'Community' in line):
            continue
        clean.append(line)
    return '\n'.join(clean)

new_clean = extract_sections(new_content)
old_clean = extract_sections(old_body)

# Extract llms-full.txt hashes
new_hash = re.findall(r'llms-full-([a-f0-9]+)\.txt', new_content)
old_hash = re.findall(r'llms-full-([a-f0-9]+)\.txt', old_body)
print(f"New llms-full hash: {new_hash[0] if new_hash else 'NOT FOUND'}")
print(f"Old llms-full hash: {old_hash[0] if old_hash else 'NOT FOUND'}")
print()

new_llms = re.findall(r'llms-([a-f0-9]+)\.txt', new_content)
old_llms = re.findall(r'llms-([a-f0-9]+)\.txt', old_body)
print(f"New llms.txt hash: {new_llms[0] if new_llms else 'NOT FOUND'}")
print(f"Old llms.txt hash: {old_llms[0] if old_llms else 'NOT FOUND'}")
print()

# Check length difference
print(f"New content length (cleaned): {len(new_clean)}")
print(f"Old content length (cleaned): {len(old_clean)}")
print()

# Look for structural changes by comparing section headings
new_headings = re.findall(r'^#{1,3}\s+(.+)$', new_content, re.MULTILINE)
old_headings = re.findall(r'^#{1,3}\s+(.+)$', old_body, re.MULTILINE)
print("=== New headings ===")
for h in new_headings:
    print(f"  - {h}")
print()
print("=== Old headings ===")
for h in old_headings:
    print(f"  - {h}")
print()

# Check for added/removed content
new_set = set(new_headings)
old_set = set(old_headings)
added = new_set - old_set
removed = old_set - new_set
if added:
    print(f"** Added sections: {added}")
if removed:
    print(f"** Removed sections: {removed}")