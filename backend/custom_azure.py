from storages.backends.azure_storage import AzureStorage
from django.conf import settings
import dotenv, os

# Add .env variables anywhere
dotenv_file = settings.BASE_DIR / ".env"
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

class AzureMediaStorage(AzureStorage):
    account_name = os.environ["AZURE_ACCOUNTNAME"]
    account_key = os.environ["AZURE_ACCOUNTKEY"]
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = os.environ["AZURE_ACCOUNTNAME"]
    account_key = os.environ["AZURE_ACCOUNTKEY"]
    azure_container = 'static'
    expiration_secs = None