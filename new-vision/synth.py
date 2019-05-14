"""This script is used to synthesize generated parts of this library."""

import synthtool as synth
import synthtool.gcp as gcp

gapic = gcp.GAPICGenerator()

library = gapic.py_library("vision", "v1")

synth.copy(library)
