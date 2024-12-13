def check_auth(request):
    token = request.headers.get('Authorization')
    return token == "Bearer valid_token"
