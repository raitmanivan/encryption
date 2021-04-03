# Authorization Proyect

#### Ivan Raitman
  
## Encrypt

Possibility of encrypting information.

- **URL:**
    `/encrypt`

- **Method**
    `POST`
  
* **Body**

  ```
  {
	"data": "test"
  }
  ```
  
- **Response:**
    **Code:** 200 <br />
        **Content:**
    ```   
        {
            "data": "1b8e7366;bf56a7349ad012bdbb00093b3c59c6d0;26ee5a96f3a349199bae1b2f8b40eb36"
        }
    ```
    **Code:** 500 <br />
        **Content:**   
    ```   
        {
            "Desc": "There was an error"
        }
    ```

## Decrypt

Possibility of decrypting information.

- **URL:**
    `/decrypt`

- **Method**
    `POST`
  
* **Body**

  ```
  {
	"data": "1b8e7366;bf56a7349ad012bdbb00093b3c59c6d0;26ee5a96f3a349199bae1b2f8b40eb36"
  }
  ```
  
- **Response:**
    **Code:** 200 <br />
        **Content:**
    ```   
        {
            "data": "test"
        }
    ```
    **Code:** 500 <br />
        **Content:**   
    ```   
        {
            "Desc": "There was an error"
        }
    ```

# Run this project

If you want to run this code locally, you should run the following commands:

* Being inside the project folder, build the container:

      docker build -t test_app .

* After that, you are able to run the code

      docker run -it --publish 8081:8081  test_app
 
It is important to have the local_settings file to run this code correctly.
Example:
   ```
        ENCRYPTION_KEY= "key"
   ```