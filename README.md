# Goal : To understand Vision Classification using CNN

### prerequisite to run the inference server: 
1. python setup and internet for installing dependencies
2. [create model](model/README.md)

#### Steps to start the server

#### step1:
```go to project folder (say water-prediction-api) in the machine```

#### step2:
```enter terminal```

#### step 3:
```pip install -r requirements.txt```
'or'
```poetry install```

#### step 4:
if run in poetry environment :
 ```poetry run uvicorn src.main:app --reload --port 8080```

if run in base python or python environment :
    ```uvicorn src.main:app --reload --port 8080```

#### step 5:
go to chrome and type 127.0.0.1:8080/docs/

### server request using python
```
!pip install requests
```
```
import requests
url = "htp://127.0.0.1:8080/predict"
file = requests.get("https://cdn.britannica.com/32/93932-050-B213E0FB/ocean-water-beach-The-Bahamas-Grand-Bahama.jpg").content
image_path = ""
files = {"file": (image_path, file, "image/jpeg")}
res = requests.post(url, file=files)
print(res.json())
```