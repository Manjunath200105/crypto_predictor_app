import sys
import subprocess


def initialize():
    stop_app()
    subprocess.run(["docker", "rmi", "-f", "crypto-python-docker"])
    subprocess.run(["docker", "build", "--tag", "crypto-python-docker", "."])


def start_app():
    stop_app()
    subprocess.run(["docker", "run", "-d", "-p", "8080:8080", "--name", "crypto_predictor_app", "crypto-python-docker"])


def stop_app():
    subprocess.run(["docker", "rm", "-f", "crypto_predictor_app"])


if __name__ == '__main__':
    action = sys.argv[1].strip().lower()
    if action == 'start':
        start_app()
    elif action == 'stop':
        stop_app()
    elif action == 'init':
        initialize()
    else:
        print("please provide valid command: init/start/stop")
