from rest_framework.authentication import TokenAuthentication as BaseTokenAuth

# There are packages for , if the tokens are genrated for viewing data,
#  no need to change them as frequently as those used to change data in the backend.

class TokenAuthentication(BaseTokenAuth):
  keyword = 'Bearer'