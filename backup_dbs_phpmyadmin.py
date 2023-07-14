# Libs
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Inicio de sesión
loginData = {'pma_username': os.getenv('PMA_USER'), 'pma_password': os.getenv('PMA_PASS')}