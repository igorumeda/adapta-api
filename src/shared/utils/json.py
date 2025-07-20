import json
import os

def ExtractJsonFrom(pathFile: str, fileName: str) -> str:
  '''Extrair pathFile de __file__'''
  base_dir = os.path.dirname(pathFile)
  json_path = os.path.join(base_dir, "", fileName)

  with open(json_path, "r", encoding="utf-8") as file:
    dados = json.load(file)

  return dados