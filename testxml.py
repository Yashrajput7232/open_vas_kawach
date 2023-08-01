# Define the filter to get the scan report logs (optional but recommended)

# Get the logs
logs = gmp.get_logs()
# Print the XML content of scan reports
for log in`    if 'scan_result' in log.message:
        print(log.message)

