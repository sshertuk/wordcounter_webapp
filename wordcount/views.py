from django.shortcuts import render
from wordcount.forms import *
import requests
import re #for regex matching

#Base view for first page re-direction
def base_view(request):
	return render(request, 'wordcount/input_view.html')

#Implements the logic to handle the incoming request content and return the word count as the output
def get_count(request):
	context = {} #envelope dictionary to return results/errors to the page

	wordcount_form = WordCount(request.POST) #instantiate form with request data/parameters
	
	#if data is blank throw error
	if not wordcount_form.is_valid():
		context['error'] = 'Please enter some content.'
		return render(request, 'wordcount/input_view.html', context)

	#process data if valid content is input by the user
	content = wordcount_form.cleaned_data['data']
	splitWords = content.split() #split on spaces to count number of words
	#validWords = re.findall(r'\w+',content)
	numOfWords = len(splitWords)
	context['numOfWords'] = numOfWords
	return render(request, 'wordcount/input_view.html', context)