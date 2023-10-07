import os
from dotenv import load_dotenv

load_dotenv()
if os.environ['ENVIRONMENT'] == 'PRODUCTION':
    from .prod import *
elif os.environ['ENVIRONMENT'] == 'DEVELOPMENT':
    from .dev import *
else:
    raise Exception(f'Invalid environment value: {os.environ["ENVIRONMENT"]}')