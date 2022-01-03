from django.http import HttpRequest, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import path
from wagtail.api.v2.views import BaseAPIViewSet
from wagtail.api.v2.utils import get_object_detail_url
from materials.models import Textbook, Section
from .models import HomePage


class RootViewSet(BaseAPIViewSet):
    """
    This viewset should return the link to the users enrolled course, along with
    a link to their next incomplete section.
    """

    model = HomePage

    @classmethod
    def get_urlpatterns(cls):
        return [
            path("", cls.as_view({"get": "root_view"}), name="detail"),
        ]

    def root_view(self, request):
        """
        : / Doing this so we're not returning a raw JsonResponse, but a drf one.
        Kinda a framework carcrash.
        """
        # The api_view decorator expects to wrap a simple function-based django views
        # not a wagtail APIViewset method. So wrapping an inner function. All knees
        # and elbows.
        router = self.get_serializer_context()["router"]
        course = request.user.enrollment.active_course
        next_section = course.specific.next_section(request.user)
        print(next_section)

        @api_view(["GET"])
        def inner_view(request, *args, **kwargs):
            return Response(
                {
                    "next_section": get_object_detail_url(
                        router, request, Section, next_section.pk
                    ),
                    "course_overview": get_object_detail_url(
                        router, request, Textbook, course.pk
                    ),
                }
            )

        # The view cannot be called with a drf request object, but the underlying
        # django request object accessed by the _request attribute.
        return inner_view(request._request)
