import os
import re
from pathlib import Path

def find_git_root():
    """Find the git repository root"""
    current = Path.cwd()
    while current != current.parent:
        if (current / '.git').exists():
            return current
        current = current.parent
    raise FileNotFoundError("Not in a git repository")

def update_head_sections():
    """Update <head> sections in all HTML files"""
    
    # Find project root and docs folder
    root = find_git_root()
    docs_dir = root / 'docs'
    
    if not docs_dir.exists():
        raise FileNotFoundError(f"docs folder not found in {root}")
    
    new_head = '''<head id="head">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">


  <script type="module" src="./js/datastar-inspector.js"></script>
  <script type="module">
    try {
      await import('./js/datastar-pro.js');
    } catch {
      await import('https://cdn.jsdelivr.net/gh/starfederation/datastar@1.0.0-RC.7/bundles/datastar.js');
    }
  </script>

  <style>@layer reset, props, theme, composition, utility, block, exception;</style>
  <link rel="stylesheet" href="./css/0_reset.css">
  <link rel="stylesheet" href="./css/1_props.css">
  <link rel="stylesheet" data-attr:href="$prst_theme" href="./css/2_theme-default.css">
  <link rel="stylesheet" href="./css/3_composition.css">
  <link rel="stylesheet" href="./css/4_utility.css">
  <link rel="stylesheet" href="./css/5_block.css">
  <link rel="stylesheet" href="./css/6_exception.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/prismjs@1/themes/prism-tomorrow.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/prismjs@1/prism.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/prismjs@1/components/prism-markup.min.js"></script>
</head>'''
    
    updated_files = []
    
    # Only process HTML files directly in docs folder
    for file in docs_dir.glob('*.html'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace everything between <head> and </head>
        new_content = re.sub(
            r'<head[^>]*>.*?</head>',
            new_head,
            content,
            flags=re.DOTALL
        )
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_files.append(file.name)
    
    return updated_files, root

# Run it
try:
    updated, root = update_head_sections()
    print(f"✅ Found git root: {root}")
    print(f"✅ Updated {len(updated)} files:\n")
    for f in updated:
        print(f"  {f}")
except FileNotFoundError as e:
    print(f"❌ Error: {e}")
