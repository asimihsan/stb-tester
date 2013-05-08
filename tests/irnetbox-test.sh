#!/bin/bash

# To run this script:
#
# PYTHONPATH=/home/asim.ihsan/Programming/libs/stb-tester bash -c "seq 1 8 | parallel -u --halt-on-error 2 ./irnetbox-test.sh irnetbox-02437.dev.youview.co.uk"

set -o pipefail

python -c '
import sys
import irnetbox

rcu = irnetbox.RemoteControlConfig(
    "/home/asim.ihsan/Programming/libs/uitests/config/humax.irnetbox.conf")
irnetbox_host = sys.argv[1]
irnetbox_port = int(sys.argv[2])
limit = 50
cnt = 0
while True:
    sys.stderr.write("Port: %s. Connecting to irNetBox\n" % irnetbox_port)
    with irnetbox.IRNetBox(irnetbox_host) as ir:
        ir.irsend_raw(port=irnetbox_port, power=100, data=rcu["MENU"])
        sys.stderr.write("Port: %s. Sent irNetBox command\n" % irnetbox_port)
    cnt += 1
    if cnt >= limit:
        break
' "$@" 2>&1 |
sed "s/^/$*: /"
