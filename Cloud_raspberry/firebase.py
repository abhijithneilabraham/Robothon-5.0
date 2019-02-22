import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': '<BUCKET_NAME>.appspot.com'
})

bucket = storage.bucket()
