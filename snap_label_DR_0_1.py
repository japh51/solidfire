from solidfire.factory import ElementFactory
import re

# Create connection to SF Cluster
sfe = ElementFactory.create("192.168.13.207", "admin", "abc")

# store the report of all snap and convert to string
list_snap = str(sfe.list_snapshots())

# regular expression to find in the string all of the snap id and FOR to modify all snap with snapmirror_label
nums = re.findall('snapshot_id=(.+?),', list_snap)
for num in nums:
    sfe.modify_snapshot(num, snap_mirror_label="DR")



