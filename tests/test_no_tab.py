from pathlib import Path
import subprocess, sys
def test_clean(tmp_path):
    f = tmp_path / 'a.py'
    f.write_text('x = 1\n')
    r = subprocess.run([sys.executable, 'hooks/no_tab.py', str(f)])
    assert r.returncode == 0
