from locust import HttpUser, task


class QuickstartUser(HttpUser):


    def on_start(self):
        response = self.client.post('/accounts/api/v1/jwt/create/',data = {
           'email': 'farimahtizghadam@gmail.com', 
           'password':"nimrimah"
           }).json()
        
        self.client.headers = {'Authorization': f"Bearer {response.get("access", None)}"}



    @task
    def list_post(self):
        self.client.get("/blog/api/v1/post/")

    
    @task
    def list_category(self):
        self.client.get("/blog/api/v1/category/")
