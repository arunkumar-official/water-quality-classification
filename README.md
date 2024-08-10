# Goal : To understand Vision Classification using CNN

### prerequisite to run the inference server: python setup and internet for installing dependencies

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