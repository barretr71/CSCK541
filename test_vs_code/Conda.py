import sys
import requests

def main():
    print(f"Python Executable: {sys.executable}\n")
    response = requests.get("https://httpbin.org/get")
    if response.status_code == 200:
        print("Status Code: 200 OK")
        print("Conda environment is linked and working perfectly in PyCharm!")

if __name__ == "__main__":
    main()