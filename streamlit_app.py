from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload

creds = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=["https://www.googleapis.com/auth/drive"]
)
service = build("drive", "v3", credentials=creds)

folder_id = get_or_create_disease_photos_folder(service)

file_metadata = {'name': 'test_photo.jpg', 'parents': [folder_id]}
media = MediaFileUpload('uploads/test_photo.jpg', mimetype='image/jpeg')

file = service.files().create(body=file_metadata, media_body=media, fields='id, webViewLink').execute()
print("Uploaded file ID:", file.get('id'))
