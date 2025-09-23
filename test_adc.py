from google.auth import default

credentials, project = default()
print("Project:", project)
print("Scopes:", credentials.scopes)
