import sys

from pythonnet import set_runtime
from clr_loader import get_coreclr

set_runtime(get_coreclr())

import os
import clr

package_dir = os.path.dirname(os.path.abspath(__file__))
dll_path = os.path.join(package_dir, "lib", 'MapCoreLibMod.dll')
if not os.path.exists(dll_path):
    raise Exception(f"Cannot find {dll_path}")
sys.path.append(package_dir)
clr.AddReference(dll_path)

clr.AddReference("MapCoreLibMod")
from MapCoreLib.Core.Util import PathUtil

print(PathUtil.RA3MapFolder)