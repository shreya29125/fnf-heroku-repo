from functools import wraps
from django.shortcuts import redirect


# *Important decorator, use with every view other than signup/ones that do not require to be logged in. Enforces the user to fill their profile details
def validate_profile(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.user.profile.is_profile_completed == True:
            return function(request, *args, **kwargs)
        else:
            return redirect('users:edit_profile')
    return wrap