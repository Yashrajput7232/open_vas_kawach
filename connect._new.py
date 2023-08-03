import paramiko
from gvm.protocols.gmpv208 import Gmp
def main():
    # Server SSH credentials and connection details
    hostname = '13.127.68.169'
    port = 22  # Default SSH port is 22
    username = 'kali'
    private_key_path = "/workspaces/open_vas_kawach/kali-linux.pem"  # Replace this with the path to your .pem file

    try:
        # Create an SSH client instance
        client = paramiko.SSHClient()

        # Automatically add the remote server's host key (not recommended for production use)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Load your private key with passphrase (if applicable)
        private_key = paramiko.RSAKey.from_private_key_file(private_key_path)

        # Connect to the SSH server and authenticate with the private key
        client.connect(hostname, port, username, pkey=private_key)

        # Now you can use the 'client' object to execute commands on the server
        command=input("enter the command")
        stdin, stdout, stderr = client.exec_command(command)

        # Print the output of the command
        print(stdout.read().decode())
        gmp = Gmp(connection=client)

        # Authenticate with gvmd using your credentials
        response = gmp.authenticate("admin", "1234")

        # Print the response (You may choose to use the transformed response if a transform function is provided)
        print("Authentication response:")
        print(response)

        # Close the SSH connection
        client.close()

    except paramiko.AuthenticationException as auth_exception:
        print("Authentication failed. Check your private key and passphrase.")
        print(f"Error: {auth_exception}")
    except paramiko.SSHException as ssh_exception:
        print("SSH connection failed. Make sure the server allows public key authentication.")
        print(f"Error: {ssh_exception}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
