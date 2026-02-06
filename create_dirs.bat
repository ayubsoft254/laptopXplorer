@echo off
cd src
if not exist templates mkdir templates
if not exist templates\laptops mkdir templates\laptops
if not exist templates\core mkdir templates\core
if not exist static mkdir static
if not exist static\css mkdir static\css
if not exist static\js mkdir static\js
if not exist static\images mkdir static\images
if not exist media mkdir media
echo Directory structure created successfully!
