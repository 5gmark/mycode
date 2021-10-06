#!/usr/bin/env python3
"""
   Date: 10/6/2021
   From: Mark Mollere, mmollere@alta3.com
Subject: ghbackup.py
     To: You

Creating a Python script to automate git commands to GitHub:
    cd ~/mycode
    git add *
    git commit -m "studying for logic"
    git push origin
"""

# Modules <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
import getopt        # C-style parser for command line options.
import os            # Operating system dependent functionality.
import sys           # System-specific parameters and functions.
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def scan_for_arguments(git_comment):
  argumentList = sys.argv[1:]
  options      = "c:v" 
  long_options = ["comment","version"]
  version      = '1.5'
  input(">>> Beginning command line argument parsing.")
  try:
    input(">>> Press <Enter> to set <arguments> and <values>.")
    arguments, values = getopt.getopt(argumentList, options, long_options)
    input(">>> <arguments> and <values> set.")
    print("<arguments>:",arguments)
    print("<values>:",values)
    input(">>> Press <Enter> to set <curretArgument> and <currentValue>.")
    for currentArgument, currentValue in arguments:
      print("<currentArgument>:",currentArgument)
      print("<currentValue>:",currentValue)
      if currentArgument in ("-c", "--comment"):
        return currentValue
      elif currentArgument in ("-v", "--version"):
        print (os.path.basename(sys.argv[0]), version)
  except:
    print("Error 101")
  sys.exit()
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def run_git_commands(git_comment):
  input(">>> Beginning git commands.")
  if len(sys.argv) == 1 or git_comment:
    if bool(git_comment):
      commit_message    = git_comment
    else:
      commit_message    = input('Commit Comment: ')
#  commit_message=input("Commit Comment: ")
  working_directory="/home/student/mycode"
  git_add="git add *"
  git_commit='git commit -m "'+ commit_message + '"'
  git_push="git push origin"
  os.chdir(working_directory)
  print(">>> Working directory set:",working_directory)
  os.system(git_add)
  print(">>> git command processed:",git_add)
  os.system(git_commit)
  print(">>> git command processed:",git_commit)
  os.system(git_push)
  print(">>> git command processed:",git_push)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def main():
#  scan_for_arguments()
#  if len(sys.argv) == 1:
#    run_git_commands()
#  run_git_commands(scan_for_arguments(""))
#  comment=scan_for_arguments("")
#  run_git_commands(comment)
  run_git_commands(scan_for_arguments(""))
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
if __name__ == "__main__":
    main()
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
