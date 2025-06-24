@echo off
echo Project Setup Script for Windows

:: Create virtual environment
echo Creating virtual environment
python -m venv myenv

:: Activate virtual environment and install packages
echo Activating virtual environment and installing requirements
call myenv\Scripts\activate.bat && pip install -r requirements.txt

echo.
echo Setup complete. The virtual environment 'myenv' is active in this terminal.
echo To deactivate it later, simply run: deactivate