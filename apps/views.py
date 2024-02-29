import json

from django.shortcuts import render

from apps.services import run_python_code, get_actual_type


def index_view(request):
    return render(request, 'python/index.htm')


def overview(request):
    return render(request, 'python/overview.htm')


def basic_syntax(request):
    return render(request, 'python/python_basic_syntax.htm')


def variables(request):
    return render(request, 'python/python_variables.htm')


def data_types(request):
    return render(request, 'python/python_data_types.htm')


def operators(request):
    return render(request, 'python/python_operators.htm')


def arithmetic_operators(request):
    return render(request, 'python/python_arithmetic_operators.htm')


def comments(request):
    return render(request, 'python/python_comments.htm')


def boolean(request):
    return render(request, 'python/python_booleans.htm')


def if_statement(request):
    return render(request, 'python/python_if_statement.htm')


def if_else(request):
    return render(request, 'python/python_if_else.htm')


def nested_if(request):
    return render(request, 'python/nested_if.htm')


def loops(request):
    return render(request, 'python/python_loops.htm')


def for_loops(request):
    return render(request, 'python/python_for_loops.htm')

def for_else(request):
    return render(request, 'python/python_forelse_loops.htm')


def while_loops(request):
    return render(request, 'python/python_while_loops.htm')


def function(request):
    return render(request, 'python/python_functions.htm')


def strings(request):
    return render(request, 'python/python_strings.htm')


def slicing_strings(request):
    return render(request, 'python/python_slicing_strings.htm')


def string_exercise(request):
    return render(request, 'python/python_string_exercises.htm')


def lists(request):
    return render(request, 'python/python_lists.htm')


def list_comprehension(request):
    return render(request, 'python/python_list_comprehension.htm')


def list_methods(request):
    return render(request, 'python/python_list_methods.htm')


def list_exercise(request):
    return render(request, 'python/python_list_exercises.htm')


def sets(request):
    return render(request, 'python/python_sets.htm')


def set_methods(request):
    return render(request, 'python/python_set_methods.htm')


def set_exercise(request):
    return render(request, 'python/python_set_exercises.htm')


def dictionaries(request):
    return render(request, 'python/python_dictionaries.htm')


def dictionary_methods(request):
    return render(request, 'python/python_dictionary_methods.htm')


def dictionary_exercise(request):
    return render(request, 'python/python_dictionary_exercises.htm')


def tuples(request):
    return render(request, 'python/python_tuples.htm')


def tuple_methods(request):
    return render(request, 'python/python_tuple_methods.htm')


def tuple_exercise(request):
    return render(request, 'python/python_tuple_exercises.htm')

def oop_concepts(request):
    return render(request, 'python/python_oops_concepts.htm')

def object_class(request):
    return render(request, 'python/python_object_classes.htm')

def inheritance(request):
    return render(request, 'python/python_inheritance.htm')

def encapsulation(request):
    return render(request, 'python/python_encapsulation.htm')

def polymorphism(request):
    return render(request, 'python/python_polymorphism.htm')

def package(request):
    return render(request, 'python/python_packages.htm')

def discuss(request):
    return render(request, 'python/python_discussion.htm')

def class_attributes(request):
    return render(request, 'python/python_class_attributes.htm')

def class_methods(request):
    return render(request, 'python/python_class_methods.htm')

def arrays(request):
    return render(request, 'python/python_arrays.htm')


# myapp/views.py
# views.py
from django.shortcuts import render

def execute_code(request):
    result = None
    error_message = None

    if request.method == 'POST':
        python_code = request.POST.get('python_code', '')
        try:
            timeout = 5  # Set your desired timeout value
            output, error = run_python_code(python_code, timeout)

            if error:
                error_message = f"Error during execution: {error}"
            else:
                result, actual_type = get_actual_type(output)

        except TimeoutError:
            error_message = "Execution time exceeded, action stopped."
        except Exception as e:
            error_message = f"Error during execution: {e}"

    return render(request, 'execute.html', {'result': result, 'error_message': error_message})





