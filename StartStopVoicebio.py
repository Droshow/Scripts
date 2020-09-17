#coding: utf-8
import os
import sys
import subprocess

def main():
  print('Press "start", "stop", "status" or "restart" with uppercase to operate the script')
  stopOrStartOrStatus = raw_input("Enter whether you want to START or STOP or STATUS or RESTART Voicebiometrics services: ")
  if str.upper(stopOrStartOrStatus) != "START" and str.upper(stopOrStartOrStatus) != "STOP" and str.upper(stopOrStartOrStatus) != "STATUS" and str.upper(stopOrStartOrStatus) != "RESTART":
        print ("Invalid STOPSTARTSTATUS parameter entered")
  if stopOrStartOrStatus == "STOP":
        subprocess.call("sudo systemctl stop voicebiometrics-contract.service", shell = True)
        print("voicebiometrics-contract stopped")
        subprocess.call("sudo systemctl stop voicebiometrics-profile-check.service", shell = True)
        print("voicebiometrics-profile-check stopped")
        subprocess.call("sudo systemctl stop voicebiometrics.service", shell = True)
        print("voicebiometrics stopped")
  if stopOrStartOrStatus == "START":
        subprocess.call("sudo systemctl start voicebiometrics-contract.service", shell = True)
        print("voicebiometrics-contract started")
        subprocess.call("sudo systemctl start voicebiometrics-profile-check.service", shell = True)
        print("voicebiometrics-profile-check started")
        subprocess.call("sudo systemctl start voicebiometrics.service",shell = True)
        print("voicebiometrics started")
  if stopOrStartOrStatus == "STATUS":
        subprocess.call("sudo systemctl status voicebiometrics-profile-check.service", shell = True)
        subprocess.call("sudo systemctl status voicebiometrics-contract.service", shell = True)
        subprocess.call("sudo systemctl status voicebiometrics.service", shell = True)
  if stopOrStartOrStatus == "RESTART":
        subprocess.call("sudo systemctl restart voicebiometrics-profile-check.service", shell = True)
        subprocess.call("sudo systemctl restart voicebiometrics-contract.service", shell = True)
        subprocess.call("sudo systemctl restart voicebiometrics.service", shell = True)
        print("systems restarting")

if __name__ == "__main__":
         main()
