import sys

class CustomException(Exception):
  def __init__(self,error_message,error_detail):
    super().__init__(error_message)

    self.error_message=(f"{error_message}")
    super().__init__(self.error_message)

