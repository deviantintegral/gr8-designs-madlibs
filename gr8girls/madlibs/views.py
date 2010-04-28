# Create your views here.
import sys
import inspect

from django.template import Context, loader
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response

from django import forms

"""
Dynamically create a form based on the blanks variable.
"""
class MadlibForm(forms.Form):
    def __init__(self, blanks, *args, **kwargs):
        super(MadlibForm, self).__init__(*args, **kwargs)            
        for key in blanks:
            self.fields[key] = forms.CharField(label=blanks[key])

# This is the index page.
def index(request):
    return render_to_response('index.html', {'user_names': usernames()})

"""
Return a list of Madlibs for a given user
"""
def list_madlibs(request, user_name):
    import_path = '/home/guest/' + user_name + '/public_html'
    if import_path not in sys.path:
        sys.path.append(import_path)
    
    error = {}
    try:
        import MyMadLibs
        reload(MyMadLibs)
        classes = []
        for name in dir(MyMadLibs):
           obj = getattr(MyMadLibs, name)
           if inspect.isclass(obj):
               classes.append(obj.__name__)
    
        sys.path.remove(import_path)
        return render_to_response('madlib-list.html', {'user': user_name, 'classes' : classes})
    except ImportError, ie:
        error = {'type' : 'ImportError', 'message' : import_path}
    except SyntaxError, s:
        error = {'type' : 'SyntaxError', 'message': s}
    sys.path.remove(import_path)
    return render_to_response('madlib-exception.html', {'error' : error})

"""
Display a madlib
"""
def madlib(request, user_name, madlib_class):
    import_path = '/home/guest/' + user_name + '/public_html'
    if import_path not in sys.path:
        sys.path.append(import_path)
    
    error = {}
    try:
        import MyMadLibs
        reload(MyMadLibs)
        klass = getattr(MyMadLibs, madlib_class)
        m = klass()
        blanks = m.blanks()
        story = ""
        if request.method == 'POST':
            form = MadlibForm(blanks, request.POST)
            answers = {}
            # This is really bad form. Normally, we should call form.is_valid(),
            # however the dynamic form breaks that, and I don't see how to solve it.
            # This isn't in our case a security issue, as we aren't using SQL and
            # the template system protects us from XSS anyways.
            for key in request.POST:
                answers[key] = request.POST[key]

            try:
                story = m.story(answers)
            except KeyError, ke:
              error = {'type' : 'KeyError', 'message' : ke}
              sys.path.remove(import_path)
              return render_to_response('madlib-exception.html', {'error' : error})

            sys.path.remove(import_path)
            return render_to_response('madlib.html', {'story' : story, 'user' : user_name, 'madlib_name' : madlib_class, 'form' : form})
        else:
            form = MadlibForm(blanks=blanks)
            sys.path.remove(import_path)
            return render_to_response('madlib.html', {'user' : user_name, 'madlib_name' : madlib_class, 'form' : form})
        sys.path.remove(import_path)
    except ImportError, ie:
        error = {'type' : 'ImportError', 'message' : ie}
    except AttributeError, ae:
        error = {'type' : 'AttributeError', 'message' : ae}
    except SyntaxError, s:
        error = {'type' : 'SyntaxError', 'message': s}
    sys.path.remove(import_path)
    return render_to_response('madlib-exception.html', {'error' : error})

"""
Return a list of valid usernames
"""
def usernames():
    users = []
    for i in range(1, 41):
	if (i < 10):
		i = "0" + str(i)
        users.append("tmpusr" + str(i))
    return users

