from django.shortcuts import render
from django.http import  HttpResponse
from django.core.paginator import Page

def main(request):
    '''
    Show 'hello world' in the main Page'''
    return  HttpResponse