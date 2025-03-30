def Serializable(id: str):
  def Serialize(func):
    def wrapper(*args, **kwargs):
      return func(*args, **kwargs)
    return wrapper
  return Serialize
    