from fastapi import APIRouter


def MappingModules(modules: list[list[APIRouter]]) -> list[APIRouter]:
  allModules: list[APIRouter] = []
  
  for listModules in modules:
    for module in listModules:
      allModules.append(module)
      
  return allModules