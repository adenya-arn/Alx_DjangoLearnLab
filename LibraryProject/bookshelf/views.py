from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from bookshelf.models import CustomUser
from django.http import HttpResponseForbidden
# Create your views here.



@permission_required('your_app.can_view_profile', raise_exception=True)
def view_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'view_profile.html', {'user': user})

def edit_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if not request.user.has_perm('your_app.can_edit_profile'):
        return HttpResponseForbidden()
    # Logic to edit the user profile
    pass

@permission_required('your_app.can_delete_profile', raise_exception=True)
def delete_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    # Logic to delete the user profile
    pass