#!/usr/bin/env python3
"""
Generate manifest.json for the ALB platform standard libraries.

Scans the current directory for platform sub-folders (macOS, Unix, ...)
and lists their library archives (.zip / .tar.gz / .tgz / .tar).

Usage:
    cd lib && python3 generate-manifest.py

Re-run this whenever you add / remove / rename library archives, then
commit the updated manifest.json. The website (index.html) reads this
manifest instead of the GitHub API, so it is never rate-limited.
"""
import os
import json
import datetime

# Archive extensions treated as downloadable libraries
EXTS = ('.zip', '.tar.gz', '.tgz', '.tar')

# Display order for known platforms (others go last, alphabetically)
ORDER = {'macOS': 0, 'Unix': 1, 'Linux': 2, 'Windows': 3}


def main():
    platforms = []
    for name in sorted(os.listdir('.')):
        if not os.path.isdir(name) or name.startswith('.'):
            continue
        files = sorted(
            f for f in os.listdir(name)
            if f.lower().endswith(EXTS)
        )
        if files:
            platforms.append({'name': name, 'files': files})

    platforms.sort(key=lambda p: (ORDER.get(p['name'], 9), p['name']))

    manifest = {
        'generated': datetime.date.today().isoformat(),
        'note': 'Auto-generated library manifest. Regenerate after adding/removing lib files.',
        'platforms': platforms,
    }

    with open('manifest.json', 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        f.write('\n')

    total = sum(len(p['files']) for p in platforms)
    print(f"manifest.json written: {len(platforms)} platform(s), {total} librar(ies).")
    for p in platforms:
        print(f"  - {p['name']}: {', '.join(p['files'])}")


if __name__ == '__main__':
    main()
