@echo off
echo Wilkommen Sie haben Maximal 20 Versuche
:regenerate
set /A COUNTER=0
set /a num=%random% %%1000
:start
set /p input=Bitte rate eine zahl zwischen 1-1000:
set /A COUNTER+=1
if %input% == answer (echo %num%) 
if %input% == %num% (set /p yn=Richtig! nochmal spielen?) ELSE goto falsch
if %input% == %num% goto richtig
goto start

:richtig
if %yn% == yes goto regenerate
if %yn% == no exit

:falsch
echo Falsch Versuche: %Counter%
if %input% LSS %num% echo zu klein
if %input% GTR %num% echo zu gross
if %Counter% == 20 (echo Zahl war %num%)
if %Counter% == 20 goto regenerate
goto start
pause