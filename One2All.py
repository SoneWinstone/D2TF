# -*- coding: UTF-8 -*-
import os

rebuildDir = ""
contextDir = ""
context = ""

def rebuildFiles(filePath):
  global rebuildDir
  fileStart = False
  file = open(filePath, encoding="UTF-8") 
  lines = file.readlines()
  for line in lines: 
    if line.startswith("$$$"):
      if "newFile" in vars():
        # close opened file 
        newFile.close()
      fileStart = True
      oldFilePath = line[3:-1]
      newFilePath = oldFilePath.replace(contextDir, rebuildDir)
      parentDir = getParentDir(newFilePath)
      if not os.path.exists(parentDir):
        os.makedirs(parentDir)
      newFile = open(newFilePath, "w", encoding="UTF-8")
      continue
    if fileStart:
      newFile.write(line)

def getParentDir(path):
  filename = str(path)
  return filename[:filename.rindex(os.sep)]

if __name__ == '__main__':
  contextDir = input("input the backup file absolute dir path: ")
  while not os.path.exists(contextDir):
    print("dir not exists!")
    contextDir = input("input the backup file absolute dir path: ")
  rebuildDir = input("input the rebuild dir path: ")
  if (rebuildDir == ""):
    rebuildDir = contextDir
  rebuildFiles(os.path.join(contextDir, "context"))
