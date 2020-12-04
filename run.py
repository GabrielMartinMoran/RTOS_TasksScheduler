from src.server.server import run_server
import webbrowser

FRONT_END_URL = 'http://localhost:5000'

def main():
    webbrowser.open(FRONT_END_URL)
    run_server()

if __name__ == "__main__":
    main()
