@echo
env\Scripts\activate && pyinstaller main.py --onedir --windowed --noconfirm --name "Snake Game" --icon "assets\Graphics\snake-logo.ico" --add-data "assets;assets"