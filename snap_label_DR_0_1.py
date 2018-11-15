from solidfire.factory import ElementFactory
import re

# Create connection to SF Cluster
sfe = ElementFactory.create("192.168.13.207", "admin", "abc")


list_snap = str(sfe.list_snapshots())

nums = re.findall('snapshot_id=(.+?),', list_snap)
for num in nums:
    sfe.modify_snapshot(num, snap_mirror_label="DR")



