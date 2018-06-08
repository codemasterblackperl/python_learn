
import add_module

result=add_module.add_numbers(1,2,3,4)
print("Result: ",result)

print(add_module.__version__)

print(dir(add_module))

# __init__.py will be used to tell analyzer that this folder is special because it contains Python modules.
# folder structure

#<some folder present in the sys.path>/
#    - world/
#        - __init__.py
#        - asia/
#            - __init__.py
#            - india/
#                - __init__.py
#                - foo.py
#        - africa/
#            - __init__.py
#            - madagascar/
#                - __init__.py
#                - bar.py