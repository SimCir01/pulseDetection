# Pulse detection from PPG signal
Progetto finale per l'esame di Sistemi di Misura Distribuiti  

## Autori
* **Simone Cirnelli** - *main contributor* - [SimCir01](https://github.com/SimCir01)
* **Benedetta Dukic** - *main contributor* - [Bennidu](https://github.com/Bennidu) 
* **Fabrizio Ravelli** - *main contributor* - [reFraw](https://github.com/reFraw)
* **Pierfrancesco Romano** - *main contributor* - [Shunsui-94](https://github.com/Shunsui-94)

## Descrizione
Il progetto, realizzato in linguaggio LabVIEW, è costituito da due applicativi, che svolgono funzione di client e server, e permette di calcolare la frequenza cardiaca a partire da un segnale ottenuto tramite sensore pulsiossimentro.  
Per informazioni sull'utilizzo degli applicativi consultare il file pdf presente nella cartella DOCUMENT.  

Il progetto può essere utilizzato in modalità DEMO utilizzando l'applicativo server fullSERVER-NotDAQ

## Requisiti software
* LabVIEW 2023 Q3 o superiore
* Driver NI-DAQmx LabVIEW
* Driver NI-488.2 LabView
* Driver NI-VISA LabView
* Python 3.9 o superiore

## Requisiti hardware
* Alimentatore stablizzato HP Agilent Keysight E3631A o equivalente
* Pulsiossimetro riflessivo PulseSensor o equivalente
* Scheda di acquisizione NI-DAQMX USB-6001
* Interfaccia USB-GPIB
* Bus GPIB/IEEE-488
