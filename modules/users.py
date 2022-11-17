from aplicacion import app

from aplicacion import user_list

@app.get("/api/users")
def get_usuarios():
    return user_list