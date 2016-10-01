from django.http import HttpResponseForbidden


class SetErrorMessageMiddleware(object):
    def process_request(self, request):
        allowed_ips = ['127.0.0.1']
        ip = request.META.get('REMOTE_ADDR')
        if ip not in allowed_ips:
            return HttpResponseForbidden()
        else:
            if request.user.is_authenticated() is False and request.META["QUERY_STRING"] is not "":
                request.session['login_error_message'] = True
            else:
                request.session['login_error_message'] = False

        return None
