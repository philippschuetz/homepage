import subprocess

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f'File {event.src_path} has been modified, rebuilding...')
        run_build_script()


def run_build_script():
    try:
        subprocess.run(['python', 'build.py'], check=True)
    except FileNotFoundError:
        subprocess.run(['python3', 'build.py'], check=True)


def main():
    run_build_script()

    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path='./src', recursive=True)
    observer.start()

    try:
        while observer.is_alive():
            observer.join(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    main()
