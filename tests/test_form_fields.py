# -*- coding: utf-8 -*-

import unittest

from wiseguy import form_fields

class TestInput(unittest.TestCase):
    def test_plain(self):
        context = dict(data=None, errors=None)
        expected = '''
<label for="foo">Foo:</label>
<input type="text" id="foo" value="" name="foo">
        '''.strip()
        result = form_fields.input(context, 'foo', "Foo:")
        assert expected == result

    def test_empty(self):
        context = dict()
        expected = '''
<label for="foo">Foo:</label>
<input type="text" id="foo" value="" name="foo">
        '''.strip()
        result = form_fields.input(context, 'foo', "Foo:")
        assert expected == result

    def test_compulsory(self):
        context = dict()
        expected = '''
<label for="foo">Foo:*</label>
<input type="text" id="foo" value="" name="foo">
        '''.strip()
        result = form_fields.input(context, 'foo', "Foo:", compulsory=True)
        assert expected == result

    def test_data(self):
        context = dict(data=dict(foo='blah'), errors=None)
        expected = '''
<label for="foo">Foo:</label>
<input type="text" id="foo" value="blah" name="foo">
        '''.strip()
        result = form_fields.input(context, 'foo', "Foo:")
        assert expected == result

    def test_errors(self):
        context = dict(data=dict(), errors=dict(foo="Please enter a foo"))
        expected = '''
<label for="foo">Foo:</label>
<input type="text" id="foo" value="" name="foo">
<span class="error">Please enter a foo</span>
        '''.strip()
        result = form_fields.input(context, 'foo', "Foo:")
        assert expected == result


class TestPassword(unittest.TestCase):
    def test_plain(self):
        context = dict(data=None, errors=None)
        expected = '''
<label for="foo">Foo:</label>
<input type="password" id="foo" value="" name="foo">
        '''.strip()
        result = form_fields.password(context, 'foo', "Foo:")
        assert expected == result

    def test_empty(self):
        context = dict()
        expected = '''
<label for="foo">Foo:</label>
<input type="password" id="foo" value="" name="foo">
        '''.strip()
        result = form_fields.password(context, 'foo', "Foo:")
        assert expected == result

    def test_compulsory(self):
        context = dict()
        expected = '''
<label for="foo">Foo:*</label>
<input type="password" id="foo" value="" name="foo">
        '''.strip()
        result = form_fields.password(context, 'foo', "Foo:", compulsory=True)
        assert expected == result

    def test_data(self):
        context = dict(data=dict(foo='blah'), errors=None)
        expected = '''
<label for="foo">Foo:</label>
<input type="password" id="foo" value="" name="foo">
        '''.strip()
        result = form_fields.password(context, 'foo', "Foo:")
        assert expected == result

    def test_errors(self):
        context = dict(data=dict(), errors=dict(foo="Please enter a foo"))
        expected = '''
<label for="foo">Foo:</label>
<input type="password" id="foo" value="" name="foo">
<span class="error">Please enter a foo</span>
        '''.strip()
        result = form_fields.password(context, 'foo', "Foo:")
        assert expected == result


class TestSelect(unittest.TestCase):
    def test_plain(self):
        options = [('bar1', "Bar 1"), ('bar2', "Bar 2"), ('bar3', "Bar 3")]
        expected = '''
<label for="foo">Foo:</label>

<select id="foo" name="foo">
<option value="bar1">Bar 1</option>
<option value="bar2">Bar 2</option>
<option value="bar3">Bar 3</option></select>
        '''.strip()
        result = form_fields.select({}, 'foo', "Foo:", options)
        result = result.strip()
        assert expected == result

    def test_compulsory(self):
        options = [('bar1', "Bar 1"), ('bar2', "Bar 2"), ('bar3', "Bar 3")]
        expected = '''
<label for="foo">Foo:*</label>

<select id="foo" name="foo">
<option value="bar1">Bar 1</option>
<option value="bar2">Bar 2</option>
<option value="bar3">Bar 3</option></select>
        '''.strip()
        result = form_fields.select({}, 'foo', "Foo:", options, compulsory=True)
        result = result.strip()
        assert expected == result

    def test_data(self):
        options = [('bar1', "Bar 1"), ('bar2', "Bar 2"), ('bar3', "Bar 3")]
        context = dict(data=dict(foo='bar3'))
        expected = '''
<label for="foo">Foo:</label>

<select id="foo" name="foo">
<option value="bar1">Bar 1</option>
<option value="bar2">Bar 2</option>
<option selected value="bar3">Bar 3</option></select>
        '''.strip()
        result = form_fields.select(context, 'foo', "Foo:", options)
        result = result.strip()
        assert expected == result

    def test_errors(self):
        options = [('bar1', "Bar 1"), ('bar2', "Bar 2"), ('bar3', "Bar 3")]
        context = dict(errors=dict(foo='Please choose a foo'))
        expected = '''
<label for="foo">Foo:</label>

<select id="foo" name="foo">
<option value="bar1">Bar 1</option>
<option value="bar2">Bar 2</option>
<option value="bar3">Bar 3</option></select>

<span class="error">Please choose a foo</span>
        '''.strip()
        result = form_fields.select(context, 'foo', "Foo:", options)
        result = result.strip()
        assert expected == result


class TestSubmit(unittest.TestCase):
    def test_plain(self):
        expected = '''<input type="submit" id="submit" value="Submit">'''
        result = form_fields.submit()
        result = result.strip()
        assert expected == result

    def test_with_labels(self):
        expected = '''<input type="submit" id="foo" value="Foo!">'''
        result = form_fields.submit('foo', "Foo!")
        result = result.strip()
        assert expected == result

    def test_bad_value(self):
        expected = '''<input type="submit" id="foo" value="Foo&amp;&lt;">'''
        result = form_fields.submit('foo', "Foo&<")
        result = result.strip()
        assert expected == result

    def test_with_classes(self):
        expected = '''<input type="submit" id="submit" value="Submit" class="foo bar">'''
        result = form_fields.submit(class_="foo bar")
        result = result.strip()
        assert expected == result


class TestBootstrapFormFields(unittest.TestCase):
    def test_input(self):
        context = dict(data=None, errors=None)
        expected = '''
<fieldset class="control-group">
<label for="foo" class="control-label">Foo:</label><div class="controls"><input type="text" id="foo" value="" name="foo"></div>
</fieldset>'''.strip()
        result = form_fields.bootstrap_input(context, 'foo', "Foo:")
        result = result.strip()
        assert expected == result
