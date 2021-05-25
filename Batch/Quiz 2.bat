@echo off
set /a points = 0
echo wilkommen zum Quiz

:start
echo Frage 1
echo 1. im Januar
echo 2. im März 
echo 3. im Mai
set /p num= wann habe ich gburtstag? 
if %num% == 1 echo falsch
if %num% == 2 echo falsch
if %num% == 3 echo richtig
if %num% == 3 set /a points=%points%+1
echo Dein Punktestand: %points%
echo .
echo 
echo .
echo Frage 2
echo 1. David
echo 2. Uwe
echo 3. René
set /p num1= wie heisse ich? 
if %num1% == 1 echo richtig
if %num1% == 2 echo falsch
if %num1% == 3 echo falsch
if %num1% == 1 set /a points=%points%+1
echo Dein Punktestand: %points%
echo . 
echo 
echo .
echo Frage 3
echo 1. Dori
echo 2. Nemo
echo 3. Blauwal
set /p num2= Welcher Fisch ist cool?
if %num2% == 1 echo falsch
if %num2% == 2 echo richtig
if %num2% == 3 echo falsch
if %num2% == 2 set /a points=%points%+1
echo Dein Punktestand: %points%
echo .
echo _
echo .
if %points% == 3 echo Glückwunsch du pilz (du Glücklpilz)
set /a points=%points%-%points%
echo .
echo 
echo .
set /p restart= willst du neu starten (j = ja, n = nein)
if %restart% == j goto start
if %restart% == n exit
sachön otomatitisirön,  w