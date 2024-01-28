import subprocess
import sys


def install_packages_from_file(file_path):
    with open(file_path, 'r') as file:
        packages = [line.strip() for line in file.readlines() if line.strip()]

    for package in packages:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])


if __name__ == "__main__":
    install_packages_from_file('requirements.txt')
