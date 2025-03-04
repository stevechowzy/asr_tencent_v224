Skip to content
Navigation Menu
stevechowzy
asr_tencent_v224

Type / to search
Code
Issues
Pull requests
1
Actions
Projects
Wiki
Security
1
Insights
Settings
CI Pipeline
Update GitHub Actions CI configuration #15
Jobs
Run details
Annotations
1 error
build
failed 9 minutes ago in 53s
Search logs
1s
1s
7s
27s
15s
0s
0s
0s
0s
1s
Run pip install pytest
Requirement already satisfied: pytest in /opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages (7.4.3)
Requirement already satisfied: iniconfig in /opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages (from pytest) (2.0.0)
Requirement already satisfied: packaging in /opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages (from pytest) (24.2)
Requirement already satisfied: pluggy<2.0,>=0.12 in /opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages (from pytest) (1.5.0)
Requirement already satisfied: exceptiongroup>=1.0.0rc8 in /opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages (from pytest) (1.2.2)
Requirement already satisfied: tomli>=1.0.0 in /opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages (from pytest) (2.2.1)
============================= test session starts ==============================
platform linux -- Python 3.8.18, pytest-7.4.3, pluggy-1.5.0 -- /opt/hostedtoolcache/Python/3.8.18/x64/bin/python
cachedir: .pytest_cache
rootdir: /home/runner/work/asr_tencent_v224/asr_tencent_v224
collecting ... collected 2 items / 1 error

==================================== ERRORS ====================================
______________ ERROR collecting tests/test_audio_preprocessor.py _______________
ImportError while importing test module '/home/runner/work/asr_tencent_v224/asr_tencent_v224/tests/test_audio_preprocessor.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/importlib/__init__.py:127: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tests/test_audio_preprocessor.py:3: in <module>
    from src.processing.audio_preprocessor import AudioPreprocessor
src/processing/audio_preprocessor.py:1: in <module>
    from pydub import AudioSegment
E   ModuleNotFoundError: No module named 'pydub'
=========================== short test summary info ============================
ERROR tests/test_audio_preprocessor.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.07s ===============================
Error: Process completed with exit code 2.
0s
0s
0s
