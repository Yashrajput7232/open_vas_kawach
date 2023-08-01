from gvm.connections import UnixSocketConnection
from gvm.connections import *
from gvm.protocols.gmp import Gmp
import gvm

# Connect to the OpenVAS server
import gvm

# Connect to the OpenVAS server
client = gvm.connections.GvmConnection("localhost", 9392, "admin", "1234")

scans = client.get_scans()

# Get the ID of the first scan
scan_id = scans[0].id

# Get the scan report
report = client.get_report(scan_id)

# Print the XML content of the report
print(report.xml)

