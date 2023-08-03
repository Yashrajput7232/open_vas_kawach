from gvm.connections import SSHConnection
from gvm.protocols.gmpv208 import Gmp

def main():
    # Server SSH credentials and connection details
    hostname = '15.207.247.136'
    port = 22  # Default SSH port is 22
    username = 'kali'
    password = '1234'  # GVM admin password
    
    try:
        # Create an SSHConnection object with the provided credentials
        ssh_connection = SSHConnection(hostname=hostname, port=port, username=username, password=password)

        # Connect to the SSH server and authenticate
        ssh_connection.connect()

        # Create a Gmp object using the SSH connection
        gmp = Gmp(connection=ssh_connection)

        # Authenticate with gvmd using your credentials
        response = gmp.authenticate("admin", "1234")

        # Print the response (You may choose to use the transformed response if a transform function is provided)
        print("Authentication response:")
        print(response)

        # Disconnect the SSH connection
        ssh_connection.disconnect()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
