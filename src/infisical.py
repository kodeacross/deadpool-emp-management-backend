# from infisical_client import ClientSettings, InfisicalClient, GetSecretOptions, AuthenticationOptions, UniversalAuthMethod
# client = InfisicalClient(ClientSettings(
#     auth=AuthenticationOptions(
#         universal_auth=UniversalAuthMethod(
#             client_id="CLIENT_ID",
#             client_secret="CLIENT_SECRET",
#         )
#     )
# ))

from dotenv import load_dotenv
load_dotenv(dotenv_path=".env", override=True)
