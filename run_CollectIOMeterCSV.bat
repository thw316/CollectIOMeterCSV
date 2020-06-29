for %%i in (%*) do (
    python-embed-win32\python.exe CollectIOMeterCSV.py %%i
)
pause
