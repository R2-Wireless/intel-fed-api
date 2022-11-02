# Intel fed graphql API

This is an example project to try the api that will be established between Intel and R2 wireless.

## Requirements
* Install pyton 3.7 or higher.
* install [Poetry](https://python-poetry.org/).
* Clone project
* Run `poetry install`
* Run `poetry run start`

## Usage
* After the start command, the graphql playground is available on [http://127.0.0.1:5000/graphql](http://127.0.0.1:5000/graphql), open it in your browser.
* To test the api, copy these lines to the graphql playground:
    ```graphql
    query {
        test(name: "Yuval")
    }
    ```
    and press the execute button, should get in return
    ```json
    {
        "data": {
            "test": "Hello, Yuval!"
        }
    }
    ```
* To use the actual api, try the mutation for detection
    ```graphql
    mutation {
        detect(file: "bin_file_path") {
            detections {
                type
            }
        }
    }
    ```
    and press the execute button, should get in return
    ```json
    {
        "data": {
            "detect": {
                "detections": [
                    {
                        "type": "MAVIC"
                    }
                ]
            }
        }
    }
    ```