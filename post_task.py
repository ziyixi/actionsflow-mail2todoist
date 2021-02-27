from todoist.api import TodoistAPI
import os
from markdownify import markdownify as md

auth_key = os.getenv("AUTH")

api = TodoistAPI(auth_key)
api.sync()

# predefined ids
# project_id = 2259411554
# section_id = 39189879
project_id = int(os.getenv("PROJECT"))
section_id = int(os.getenv("SECTION"))

# get env
subject = os.getenv("SUBJECT")
due = os.getenv("DUE")

sender = md(os.getenv("SENDER"))
comment_body = md(os.getenv("CONTENT"))
comment_head = f"**FROM {sender}\n\n"
comment = comment_head+comment_body


task = api.items.add(subject, project_id=project_id,
                     section_id=section_id, due={'string': due})
api.notes.add(task['id'], comment)
api.commit()
print(task)
