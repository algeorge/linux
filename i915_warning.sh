#!/bin/bash
echo "blacklist i915" | sudo bash -c 'cat > /etc/modprobe.d/blacklist-i915.conf'
