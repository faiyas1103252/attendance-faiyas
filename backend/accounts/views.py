from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Attendance
from .serializers import UserSerializer
import math

# OFFICE LOCATION
OFFICE_LAT = 12.9716
OFFICE_LON = 77.5946
RADIUS = 100  # meters


def get_distance(lat1, lon1, lat2, lon2):
    R = 6371000
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * \
        math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1-a))


# ---------------- SIGNUP ----------------
@api_view(["POST"])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created"})
    return Response(serializer.errors)


# ---------------- LOGIN ----------------
@api_view(["POST"])
def login(request):

    username = request.data.get("username")
    password = request.data.get("password")
    lat = float(request.data.get("lat"))
    lon = float(request.data.get("lon"))

    user = User.objects.filter(
        username=username,
        password=password
    ).first()

    if not user:
        return Response({"error": "Invalid credentials"}, status=400)

    # Superadmin can login from anywhere
    if user.role != "superadmin":
        dist = get_distance(lat, lon, OFFICE_LAT, OFFICE_LON)
        if dist > RADIUS:
            return Response({"error": "Outside office location"}, status=400)

    Attendance.objects.create(user=user)

    return Response({
        "username": user.username,
        "role": user.role
    })
