# Twitter API usage
Contains 2 main modules: lab2_2.py and lab2_3.py  
lab2_2.py is a console program that walks through a .json file that created with Twitter API.
lab2_3.py and it's submodule -- mapper.py is a web-app that finds locations of a friends of a Twitter users (may work for a while, if it has a lot of them)

## Requirements
needs pip packages:
- Flask 2.0.3
- folium 0.12.1.post1
- geopy 2.2.0
- uvicorn 0.17.5


## Usage
To use the lab2_3.py locally on your computer, you need to run these commands in console
```bash
>export FLASK_APP=lab2_3.py
>flask run --host=0.0.0.0 --port=8080
```
 
## Examples
![image](![image](https://user-images.githubusercontent.com/92575534/154721094-373b292e-fbe4-4784-81f5-fd5e84beecd8.png))
![image](https://user-images.githubusercontent.com/92575534/154721565-d168b55f-4a8d-4a96-9c4b-d44d5bfc89f5.png)