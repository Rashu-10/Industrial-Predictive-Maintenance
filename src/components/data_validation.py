class DataValidator:
  @staticmethod
  def validate_input(air_temp,process_temp,rpm,torque,tool_wear):
    if air_temp < 0:
        return False 
    if process_temp < 0:
        return False
    if rpm < 0:
        return False
    if torque < 0:
        return False
    if tool_wear < 0:
        return False
    return True
