from django.shortcuts import redirect, get_object_or_404

def create_view(Form_class):
    def inside_function(func):  
        def call_func(request, *args, **kwargs):
            if request.method == 'POST':
                form = Form_class(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('../')
                else:
                    print(form.errors)
            form = Form_class()
            context = {
                'form' : form
            }
            return func(request, context, *args, **kwargs)
        return call_func
    return inside_function

def delete_view(Model_class):
    def inside_function(func):  
        def call_func(request, id, *args, **kwargs):
            obj = get_object_or_404(Model_class, id=id)
            if request.method == 'POST':
                obj.delete()
                return redirect('../')
            context = {
                "obj" : obj
            }
            return func(request, context, *args, **kwargs)
        return call_func
    return inside_function

def detail_view(Model_class):
    def inside_function(func):  
        def call_func(request, id, *args, **kwargs):
            obj = get_object_or_404(Model_class, id=id)
            context = {
                "obj" : obj
            }
            return func(request, context, *args, **kwargs)
        return call_func
    return inside_function

def edit_view(Model_class, Form_class):
    def inside_function(func):  
        def call_func(request, id, *args, **kwargs):
            obj = get_object_or_404(Model_class, id=id)
            form = Form_class(request.POST or None, instance=obj)
            if form.is_valid():
                form.save()
                form = Form_class()
                return redirect('../')
            context = {
                "form" : form
            }
            return func(request, context, *args, **kwargs)
        return call_func
    return inside_function