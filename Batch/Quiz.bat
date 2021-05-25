@echo off

GOTO :main

:main
    echo Quiz
    echo Beantworte die Fragen mit Ja oder Nein
    set /a points=0
    set /a counter=0
    GOTO :LOOP

:LOOP
    IF "%counter%"=="0" GOTO Frage1
    IF "%counter%"=="1" GOTO Frage2
    IF "%counter%"=="2" GOTO Frage3
    IF "%points%"=="3" GOTO win
    IF /I %points% LSS 3 GOTO points

:Frage1
    set /p inp=Frage 1: Magst du INFO?
    IF "%inp%"=="Ja" set /a points+=1
    set /A counter+=1 
    GOTO :LOOP

:Frage2
    set /p inp=Frage 2: Ist Schweden die Hauptstadt von Norwegen?
    IF "%inp%"=="Nein" set /a points+=1
    set /A counter+=1 
    GOTO :LOOP

:Frage3
    set /p inp=Frage 2: Magst du Batch?
    IF "%inp%"=="Ja" set /a points+=1
    set /A counter+=1 
    GOTO :LOOP

:win
    echo Glueckwunsch, du hast alle Fragen richtig beantwortet.
    set /p play_again=Willst du nochmals spielen [y/n]?
    IF "%play_again%"=="y" GOTO main
    IF "%play_again%"=="n" exit

:points
    echo Du hast %points% Punkte und somit %points% Fragen richtig beantwortet.
    set /p play_again=Willst du nochmals spielen [y/n]?
    IF "%play_again%"=="y" GOTO main
    IF "%play_again%"=="n" exit