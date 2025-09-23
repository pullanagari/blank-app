from google.oauth2 import service_account
from googleapiclient.discovery import build

creds_dict = dict(st.secrets["gcp_service_account"])
creds = service_account.Credentials.from_service_account_info(
    creds_dict,
    scopes=["https://www.googleapis.com/auth/drive.file"]
)

service = build("drive", "v3", credentials=creds)

# Test connection
about = service.about().get(fields="user").execute()
st.write("🔑 Connected as:", about["user"]["emailAddress"])
