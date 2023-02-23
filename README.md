# Explications 
> Projet consiste à collecter les données sur une page web de manière dynamique 

Modules utilisés : selenium, request et SQLITE3 (Base de données) 

1. Vérifier si le site est fonctionnel `requests.status_code`
   ```python
   url = "votre url" #en STR
   response = requests.get(url)
   # vérification
   if response.status_code != 200:
        print(f"Attention erreur \n code : {response.status_code}") 
    ```
2. Lancer le driver et rechercher la page en question
   ```python
   driver.get("votre url")
   ```
3. Rechercher les éléments avec CSS_SELECTOR
    Exemple de code :
    ```python
    driver.find_element(By.CSS_SELECTOR, "votre CSS_selector")
    ```

... 

DM pour la suite des explications. 