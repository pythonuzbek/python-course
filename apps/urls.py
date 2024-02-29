from array import array

from django.urls import path

from apps.views import index_view, overview, nested_if, basic_syntax, data_types, variables, operators, \
    arithmetic_operators, boolean, if_statement, if_else, loops, for_loops, while_loops, comments, function, strings, \
    slicing_strings, string_exercise, lists, list_comprehension, list_methods, sets, set_methods, set_exercise, \
    dictionaries, dictionary_methods, dictionary_exercise, oop_concepts, object_class, inheritance, polymorphism, \
    package, for_else, discuss, class_attributes, class_methods, list_exercise, tuples, tuple_methods, tuple_exercise, \
    arrays, encapsulation, execute_code

urlpatterns = [
    path('', index_view, name='index_view'),
    path('python-overview/', overview, name='python_overview'),
    path('python-nested-if/', nested_if, name='nested_if'),
    path('basic-syntax/', basic_syntax, name='basic_syntax'),
    path('data-types/', data_types, name='data_types'),
    path('variables/', variables, name='variables'),
    path('operators/', operators, name='operators'),
    path('arithmetic-operators/', arithmetic_operators, name='arithmetic_operators'),
    path('comments/', comments, name='comments'),
    path('boolean/', boolean, name='boolean'),
    path('if-statement/', if_statement, name='if_statement'),
    path('if-else/', if_else, name='if_else'),
    path('nested-if/', nested_if, name='nested_if'),
    path('loops/', loops, name='loops'),
    path('for-loops/', for_loops, name='for_loops'),
    path('for-else', for_else, name='for_else'),
    path('while-loops/', while_loops, name='while_loops'),
    path('function', function, name='function'),
    path('strings/', strings, name='strings'),
    path('slicing-strings/', slicing_strings, name='slicing_string'),
    path('strings-exercise/', string_exercise, name='string_exercise'),
    path('list/', lists, name='list'),
    path('list-comprehension/', list_comprehension, name='list-comprehension'),
    path('list-methods/', list_methods, name='list_methods'),
    path('list-exercise', list_exercise, name='list_exercise'),
    path('tuples', tuples, name='tuple'),
    path('tuple-methods', tuple_methods, name='tuple_methods'),
    path('tuple-exercise', tuple_exercise, name='tuple_exercise'),
    path('array', arrays, name='array'),
    path('set/', sets, name='set'),
    path('set-methods', set_methods, name='set_methods'),
    path('set-exercise',set_exercise, name='set_exercise'),
    path('dictionary', dictionaries, name='dictionary'),
    path('dictionary-methods', dictionary_methods, name='dictionary_methods'),
    path('dictionary-exercise', dictionary_exercise, name='dictionary_exercise'),
    path('oop-concepts', oop_concepts, name='oop_concepts'),
    path('object-classes', object_class, name='object_class'),
    path('class-attributes', class_attributes, name='class_attributes'),
    path('class-methods', class_methods, name='class_methods'),
    path('inheritance/', inheritance, name='inheritance'),
    path('polymorphism/', polymorphism, name='polymorphism'),
    path('encapsulation', encapsulation, name='encapsulation'),
    path('package', package, name='package'),
    path('discuss', discuss, name='discuss'),
    path('execute/', execute_code, name='execute_code')
]



