# -*- coding: utf-8 -*-

import string
import random

from paste.fixture import TestApp, TestResponse

from root import Wiki

app = TestApp(Wiki())

def start_response_func(status, content_type):
    assert status == '200 OK'
    # print content_type
    assert ('content-type', 'text/html; charset=utf-8') in content_type

def random_string(length=5):
    return ''.join([random.choice(string.letters) for i in range(length)])

random_stub = random_string(20)
random_tags = ' '.join([random_string() for j in range(5)])

def test_wiki_save_page():
    response = app.post('/save/homepage', params={'stub':'', 'body':'This is the modified home page'})
    print response
    response = response.follow()
    print response
    response = response.follow()
    print response
    assert 'This is the modified home page' in response.normal_body
    response = app.post('/save/test', params={'body':'This is the modified test page'})
    response = response.follow()
    print response
    assert 'This is the modified test page' in response.normal_body
    

def test_list_pages():
    response = app.get('/list')
    print response
    assert '<a href="/edit/homepage">Edit this page</a>'

def test_wiki_homepage():
    response = app.get('/')
    print response.normal_body
    assert "This is the modified home page" in response.normal_body

def test_wiki_page():
    response = app.get('/test')
    print response.normal_body
    assert "This is the modified test page" in response.normal_body

def test_wiki_edit_page():
    response = app.get('/edit')
    response = response.follow()
    print response.normal_body
    assert "Edit homepage" in response.normal_body
    response = app.get('/edit/hello')
    print response.normal_body
    assert "Edit hello" in response.normal_body

def test_wiki_tagging():
    response = app.post('/save/test', params={'body':'This is the modified test page', 'tags':random_tags})
    response = response.follow()
    print response
    for tag in random_tags.split():
        assert tag in response.normal_body

def test_page_not_found():
    response = app.get('/' + random_stub)
    form = response.form
    assert "404" in response.normal_body
    form.set('body', 'This page is named ' + random_stub)
    response = form.submit()
    print response
    response = response.follow()
    assert random_stub in response.normal_body

def test_delete_pages():
    response = app.post('/delete/test')
    response = response.follow()
    response = app.get('/test')
    assert "404" in response.normal_body
    response = app.post('/delete/' + random_stub)
    response = response.follow()
    response = app.get('/' + random_stub)
    assert "404" in response.normal_body
    




