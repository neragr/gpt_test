from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import openai

# Create your views here.
openai.api_key= os.environ.get('OPENAI_API_KEY')

@csrf_exempt
def main (request):
    result=openai.Completion.create(
        prompt=request.POST.get('prompt'),
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        model="text-davinci-003",
    )
    return JsonResponse(result)