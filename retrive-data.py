from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
def get_secret():
    key_vault_url = <key-vault-url>
    credential = DefaultAzureCredential()

    secret_client = SecretClient(vault_url=key_vault_url, credential=credential)
    secret_name = <name-of-secret>
    # Retrieve the secret containing your Azure credentials
    secret-value = secret_client.get_secret(secret_name)
    print(secret_name+":"+secret-value)
    return

get_secret()
