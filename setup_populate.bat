@echo off
echo Creating management command directories...
mkdir "C:\Users\henry\Desktop\laptopXplorer\src\laptops\management" 2>nul
mkdir "C:\Users\henry\Desktop\laptopXplorer\src\laptops\management\commands" 2>nul
echo Directories created!
echo.
echo Now creating Python files...
echo.

echo # Django management module > "C:\Users\henry\Desktop\laptopXplorer\src\laptops\management\__init__.py"
echo # Django management commands module > "C:\Users\henry\Desktop\laptopXplorer\src\laptops\management\commands\__init__.py"

echo Files created! Now run: populate.bat
pause
