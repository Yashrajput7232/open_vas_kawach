import paramiko
from gvm.connections import SSHConnection
from gvm.protocols.latest import Gmp
from gvm.transforms import EtreeTransform
from gvm.errors import GvmError

def main():
    try:
        # SSH connection details for the GVM server
        hostname = '13.127.68.169'
        port = 22
        username = 'gvm_user'  # Use the new user you created
        private_key_path = '/workspaces/open_vas_kawach/kali-linux.pem'

        # Create an SSH client instance
        client = paramiko.SSHClient()

        # Automatically add the remote server's host key (not recommended for production use)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Load your private key (without passphrase)
        private_key = paramiko.RSAKey.from_private_key_file(private_key_path)

        # Connect to the SSH server and authenticate with the private key
        client.connect(hostname, port, username, pkey=private_key)

        # Now you can use the 'client' object to execute commands on the server

        # Establish a GMP connection using SSH tunneling
        connection = SSHConnection.from_paramiko(client)

        # Authenticate with GVM using your credentials
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

        # Close the SSH connection
        client.close()

    except paramiko.AuthenticationException as auth_exception:
        print("Authentication failed. Check your private key and passphrase.")
        print(f"Error: {auth_exception}")
    except paramiko.SSHException as ssh_exception:
        print("SSH connection failed. Make sure the server allows public key authentication.")
        print(f"Error: {ssh_exception}")
    except GvmError as gvm_exception:
        print(f"GVM error: {gvm_exception}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
