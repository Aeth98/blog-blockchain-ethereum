# blog-blockchain-ethereum
Grazie a Django,SQlite e Redis, ho realizzato un Social con le funzionalità più comuni ed altre particolari.
Una pagina per la registrazione e accesso degli utenti.
Una pagina, accessibile soltanto dagli utenti loggati, dalla quale è possibile scrivere un post, e guardare tutti i post degli altri utenti in ordine cronologico.
Grazie alla funzione di hash SHA256, da ogni contenuto di tutti i Post si ricava l'hash, che viene mandato come messaggio di una transazione all'interno della testnet Ropsten della blockchain di Ethereum.
Una pagina, alla quale soltanto gli amministratori possono accedere, dove è possibile vedere il numero di post pubblicati da ciascun utente.
Una pagina, accessibile dall’url /utente/[id], dove [id] è un parametro che rappresenta l’id dell’utente.
Un endpoint che restituisca una risposta in JSON contenente le informazioni su tutti i post pubblicati nell’ultima ora.
Un endpoint che, fornita una stringa tramite GET, restituisca un valore intero corrispondente al numero di volte in cui questa stringa è apparsa nei post pubblicati.
Un sistema di controllo che proibisca l’inserimento di qualsiasi post che contiene la parola ‘hack’.
Un sistema di logging per memorizzare l’ultimo IP che ha avuto accesso alla piattaforma per un certo utente, per mostrare un messaggio di avvertimento quando questo è diverso dal precedente.
