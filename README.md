# djangoProjectBlockchain

Ho creato un sito con caratteristiche tipiche di un social network con Django nel quale è possibile accedere con i propri dati e scrivere dei post che finiscono su una bacheca pubblica. 
Questi post vengono salvati sulla blockchain e possono essere facilmente analizzati dall'Admin del sito.
Il sito sfrutta Redis per gestire in modo ottimale la cache e, associato ad un normale database SQL, permette di avere un sito sempre efficiente anche sotto condizioni di stress.

    - Sono presenti sistemi di controllo per evitare che gli utenti inseriscano termini scorretti;
    - E' possibile visualizzare i post pubblicati nell'ultima ora comodamente tramite JSON;
    - E' possibile verificare se sono presenti eventuali mutamenti dell'indirizzo IP dell'utente;
    - Cercare quante volte un termine appare nei post pubblicati.
    - Risalire allo Username solamente indicando l'ID.
    - L'Admin può visualizzare il numero di post pubblicati da ogni utente
