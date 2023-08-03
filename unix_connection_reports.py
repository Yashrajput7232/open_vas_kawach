from gvm.connections import UnixSocketConnection
from gvm.protocols.latest import Gmp
from gvm.transforms import EtreeTransform
from gvm.errors import GvmError

def main():
    try:
        # Specify the path to the GVM socket file
        socket_path = '/path/to/your/gvmd.sock'  # Replace with the actual path of your gvmd.sock file

        # Create a UnixSocketConnection object using the socket file path
        connection = UnixSocketConnection.from_socket_file(socket_path)

        # Connect to the GVM server and authenticate
        with Gmp(connection, transform=EtreeTransform()) as gmp:
            # Get the list of all scan reports
            reports = gmp.get_reports()

            # Print the details of each report
            for report in reports:
                print(f"Report ID: {report['report_id']}")
                print(f"Task ID: {report['task_id']}")
                print(f"Report Format: {report['report_format']}")
                print(f"Status: {report['status']}")
                print(f"Timestamp: {report['timestamp']}")
                print(f"Report: {report['report']}\n")

    except GvmError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
