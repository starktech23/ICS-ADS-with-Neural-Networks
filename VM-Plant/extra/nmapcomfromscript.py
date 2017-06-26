import subprocess
import os
def main():


    try:
        subprocess.call(["python"])
    except ImportError:
        print 'nmap not installed'
        os.exit(1)

if __name__ == "__main__":
	main()