import os

# get emails and password from environment variables
Toolname = os.environ.get("TOOL_NAME")
print(Toolname)
if(Toolname=="terraform"):
  print("value is terraform")
else:
  print("secret is not reading correctly")
