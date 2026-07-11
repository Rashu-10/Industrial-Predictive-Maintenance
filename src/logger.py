import logging
import os
LOG_FILE="project.log"
logging.basicConfig(
  filename=LOG_FILE,  
  level=logging.INFO,
  format="[%(asctime)s] %(message)s"
)