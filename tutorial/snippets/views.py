from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from snippets.serializers import SnippetSerializer
from .models import Snippet


# 이 뷰는 api_view형태로 동작함 (request에 HttpRequest가 아닌 Request가 주어짐)
# GET, POST
@api_view(['GET', 'POST'])
def snippet_list(request):
    if request.method == 'GET':
        # snippets는 모든 Snippet의 쿼리셋
        snippets = Snippet.objects.all()
        # 쿼리셋을 serialize할 때는 many=True옵션 추가
        serializer = SnippetSerializer(snippets, many=True)
        # 데이터를 적절히 렌더링해주는 Response객체 리
        return Response(serializer.data)

    elif request.method == 'POST':
        # request로 전달된 데이터들을 JSONParser를 사용해 파이썬 데이터 형식으로 파싱
        data = JSONParser().parse(request)
        # 처리된 데이터를 사용해 SnippetSerializer인스턴스를 생성
        serializer = SnippetSerializer(data=request.data)
        # 인스턴스에 주어진 데이터가 유효할 경우
        if serializer.is_valid():
            # 인서튼서의 save()메서드를 호출해 Snippet객체를 생성
            serializer.save()
            # HTTP 상태코드(201 created)로 serializer의 내용을 보내줌
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 유효하지 않으면 인스턴스의 에러들을 HTTP 400 Bad request상태코드와 함께 보내줌
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # GET 요청시에는 snippet을 serialize한 결과를 보여줌
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # PUT 요청시에는 전달된 데이터를 이용해서 snippet 인스턴스의 내용을 변경
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        # DELETE요청시에는 해당 Snippet 인스턴스를 삭제
        snippet.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
