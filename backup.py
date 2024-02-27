# Login route otp verification code 
json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        email = python_data.get("email", None)
        otp = python_data.get("otp", None)
        
        if not email and otp:
            status_code = status.HTTP_401_UNAUTHORIZED
            response = {
            'success': False,
            'statusCode': status_code,
            'message': 'Invalid email or otp'
        }
            json_data_response = json.dumps(response)
            return HttpResponse(json_data_response, status = status_code)
        user = models.User.objects.get(email = email)
        otp_obj = models.otp.objects.get(user = user) 
        if otp_obj.otp != otp:
            status_code = status.HTTP_401_UNAUTHORIZED
            response = {
            'success': False,
            'statusCode': status_code,
            'message': 'Invalid email or otp'
        }
            json_data_response = json.dumps(response)
            return HttpResponse(json_data_response, status = status_code)