import paramiko


class FileTransfer():
    """Represents a class capable of downloading files from the robot.
    """
    def __init__(self, robot):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(robot.configuration.Ip, username=robot.configuration.Username, password=robot.configuration.Password)


    def get(self, remote, local):
        """Downloads the remote file to local file.

        Args:
            remote (str): the path to the remote file
            local (str): the path to the local file to store the downloaded file to.
        """
        sftp = self.ssh.open_sftp()
        sftp.get(remote, local)
        sftp.remove(remote)
        sftp.close()

    def close(self):
        self.ssh.close()