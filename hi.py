import os

# get emails and password from environment variables
Toolname = os.environ.get("TOOL_NAME")
if Toolname == "hello":
  print("value is terraform")
else:
  print("secret is not reading correctly")
