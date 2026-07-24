class RecommendationEngine:
  @staticmethod
  def recommend(probability):
    if probability>80:
      return """Immediate shutdown and inspection"""
    
    elif probability>60:
      return """Maintenance within 24 hours"""
    
    elif probability>30:
      return """Schedule preventive maintenance"""
    
    return """Normal operation"""
