import sys

from pythonnet import set_runtime
from clr_loader import get_coreclr

set_runtime(get_coreclr())

import os
import clr

package_dir = os.path.dirname(os.path.abspath(__file__))
dll_dir = os.path.join(package_dir, "lib")
if not os.path.exists(dll_dir):
    raise Exception(f"Cannot find {dll_dir}")

for f in os.listdir(dll_dir):
    if f.endswith(".dll"):
        clr.AddReference(os.path.join(dll_dir, f))

sys.path.append(package_dir)

clr.AddReference("MapCoreLibMod")
clr.AddReference("Ra3MapBridge")

import ra3_map
