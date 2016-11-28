# KlesanWatcher
    still in developing


## Development
    The system can be developed only font-end, use vue, vuex framework, and the backend apis are mocked.
    for example, 
    in production environment, the api /api/base/version will get the data from api.base:version (python function),
    in front-end developing environment, the api will get the data from /mock/api/base/version (a text file).
    
    run the font-end only with node dev server
    ```js
        npm run dev
    ```
    
    
    if you need to run the hold system, you will need 3g modem on /dev/ttyUSB0, a neo4j server
    run the all system with python3
    ```python
        python main.py
    ```
    
 