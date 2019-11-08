# javascriptFileEncoder
Encodes a file into JavaScript friendly hex data, useful for adding file uploads to session riding XSS payloads

For example, if you're trying to do XHR requests to install a wordpress plugin from XSS running in a wordpress administrator context, you'd need the actual zip file of the wordpress plugin encoded and embedded in your javascript. 
