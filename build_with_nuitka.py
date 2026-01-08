import os
import sys
import subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))

ENTRY = os.path.join(ROOT, "lpunpack_cli.py")
OUTPUT = "lpunpack.exe"

cmd = [
    sys.executable, "-m", "nuitka",
    ENTRY,
    "--onefile",
    "--standalone",
    "--follow-imports",
    "--include-module=lpunpack",
    "--include-package=argparse",
    "--include-package=json",
    "--include-package=enum",
    "--include-package=re",
    "--include-package=pathlib",
    "--assume-yes-for-downloads",
    f"--output-filename={OUTPUT}",
]

print("[*] Running Nuitka build:")
print(" ".join(cmd))
print()

subprocess.check_call(cmd)
print("\n[+] Build finished successfully")
