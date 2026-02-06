@echo off
cd src\templates\laptops
del laptop_list.html
ren laptop_list_new.html laptop_list.html
echo Template replaced successfully!
pause
