from .models import Notice
from .serializers import NoticeSerializer, NoticeCheckSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#00-12 공지 생성
class AdminNoticeList(APIView):
    def post(self, request):
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class AdminNoticeDetail(APIView):
    def get_notice(self, pk):
        try:
            return Notice.objects.get(pk=pk)
        except Notice.DoesNotExist:
            raise Http404

    #00-16 조회
    def get(self, request, pk):
        notice = self.get_notice(pk)
        serializer = NoticeSerializer(notice)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #00-13 수정
    def put(self, request, pk):
        notice = self.get_notice(pk)
        serializer = NoticeSerializer(notice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    #00-14 삭제
    def delete(self, request, pk):
        notice = self.get_notice(pk)
        notice.delete()
        return Response(status=status.HTTP_200_OK)


#00-15 important, visible 수정
class AdminNoticeCheckDetail(APIView):
    def get_object(self, pk):
        try:
            return Notice.objects.get(pk=pk)
        except Notice.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        notice = self.get_object(pk)
        data = request.data
        obj = {
            "visible" : data["visible"],
            "important" : data["important"],
        }
        serializer = NoticeCheckSerializer(notice, data=obj)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class NoticeList(APIView):
    #04-01 공지 리스트 전체 조회
    def get(self, request):
        notices = Notice.objects.all()
        serializer = NoticeSerializer(notices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





