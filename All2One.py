# -*- coding: UTF-8 -*-
import os
import sys

context = ""
# suffix in filter will be backup
suffixFilter = []

def readFiles(dir):
  global context
  for root, dirs, files in os.walk(dir):
    for file in files:
      fileName = os.path.join(root, file)
      if (getSuffix(fileName) not in suffixFilter):
        continue
      controlFile = open(fileName, "r", encoding="UTF-8") 
      lines = controlFile.readlines()
      if lines.__len__() > 0:
        context = context + "$$$" + os.path.join(root, file) + "\n"
      for line in lines: 
        context = context + line
      context = context + "\n"
      controlFile.close()
    # for dir in dirs:
    #   readFiles(os.path.join(root, dir))

def getParentDir(path):
  filename = str(path)
  return filename[:filename.rfind(os.sep)]

def getSuffix(file):
  filename = str(file)
  pointIndex = filename.rfind('.')
  if pointIndex == -1:
    return ""
  return filename[pointIndex + 1:]

def init():
  global suffixFilter
  conf = open("D2TF.conf", "r", encoding="UTF-8")
  lines = conf.readlines()
  for line in lines:
    if line.startswith("filter"):
      split = line.split(",")
      for sp in split:
        suffixFilter.append(str(sp).strip())

if __name__ == '__main__':
  init()

  dir = input("input absolute dir path you want backup: ")
  while not os.path.exists(dir):
    print("dir not exists!")
    dir = input("input absolute dir path you want backup: ")
  readFiles(dir)
  f = open(os.path.join(dir, "context"), "w", encoding="UTF-8")
  f.writelines(context)
  f.close()
  print("backup success!")
