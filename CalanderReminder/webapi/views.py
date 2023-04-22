from rest_framework.decorators import api_view # decorator for api
from rest_framework.response import Response
from Notify.models import UsersFriends
# Create your views here.


@api_view(['POST'])
def addFriends(request):
    full_name = request.data.get('full_name')
    birthday = request.data.get('birthday')
    special_occasions = request.data.get('special_occasions')
    remind_before = request.data.get('remind_before')
    if not all(full_name, birthday, special_occasions, remind_before):
        return Response({'message': 'All parameters are required: full name, birthday, special_occasions, remind_before'})
    userFriend = UsersFriends(full_name=full_name, birthday=birthday, special_occasions=special_occasions, remind_before=remind_before)
    userFriend.save()
    return Response({'message' : 'Friend added successfully'})
