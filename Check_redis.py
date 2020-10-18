import os
import sys
import subprocess


def main():
        kenntwort= "3d66a3e822d96f9025cb8a0b1e30"
        pako = subprocess.call(['./redis-cli', '-h', '10.171.139.78', '-p', '6379', '-a', kenntwort],shell=True)
        subprocess.call("set test1 test_werte", shell=True)
        result = subprocess.call("get test1", shell=True)
        print(result)
	

if __name__ == "__main__":
         main()

		 
./re
		 
		 
// testing		 
import subprocess

print subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])

10.171.139.25

subprocess.call("call your redis cli ")
+
