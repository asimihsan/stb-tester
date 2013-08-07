import glob
import os
import time

import stbt


# Fail if this script is run more than once from the same $scratchdir
n_runs = len(glob.glob("../????-??-??_??.??.??*"))  # includes current run
if n_runs == 2:
    raise stbt.UITestError("UITestError: not the system-under-test's fault")
elif n_runs > 2:  # UITestFailure
    stbt.wait_for_match("videotestsrc-checkers-8.png", timeout_secs=1)

stbt.press("gamut")
stbt.wait_for_match("videotestsrc-gamut.png")

time.sleep(float(os.getenv("sleep", 0)))

stbt.press("smpte")
stbt.wait_for_motion()
