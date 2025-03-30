from abc import ABC, abstractmethod

class Controller(ABC):
  def parseInput():
    '''
      Método que obtém os parâmetros passados via body
      * Validar todas as informações recebidas
    '''
    pass

  def parseParams():
    '''
      Método que obtém os parâmetros passados via URL
      * Validar todas as informações recebidas
    '''
    pass

  def parseQuery():
    '''
      Método que obtém os parâmetros passados via query string
      * Validar todas as informações recebidas
    '''

  @abstractmethod()
  def handle(self):
    '''Executar o processo'''
    pass

  
     