@REM fix for appengine ImportError: pip install urllib3==1.26.15 requests-toolbelt==0.10.1
python setup.py sdist
python -m twine upload dist/* --config-file C:\Users\1589l\Desktop\Python\.pypirc
pause