from django.shortcuts import render
import requests

#Base view for first page re-direction
def base_view(request):
	return render(request, 'wordcount/input_view.html')

#Implements the logic to handle the incoming request content and return the word count as the output
def get_count(request):
	context = {} #envelope dictionary to return results/errors to the page
	content = request.POST.get('data')

	#if data is blank throw error
	if not content:
		context['error'] = 'Please enter some content!'
		return render(request, 'wordcount/input_view.html', context)

	#process data if valid content is input by the user
	splitWords = content.split() #split on spaces to count number of words
	numOfWords = len(splitWords)
	context['numOfWords'] = numOfWords
	return render(request, 'wordcount/input_view.html', context)