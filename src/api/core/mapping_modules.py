from fastapi import APIRouter
from src.api.core.controller import Controller

def MappingModules(routesCollection: list[list[type[Controller]]]) -> list[APIRouter]:
  allRoutes: list[APIRouter] = []
  
  for listOfRoutes in routesCollection:
    for router in listOfRoutes:
      allRoutes.append(router.__router__)
      
  return allRoutes