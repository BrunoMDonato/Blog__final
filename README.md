# Blog_Final

## **Blog creado con Django (Python) y SQLite**

Este proyecto es un blog funcional donde los usuarios pueden registrarse, crear publicaciones con imágenes, comentar y enviar mensajes privados a otros usuarios.


### *[Blog´s video here !](https://www.youtube.com/watch?v=4WpVwsg4sjU)*

---

## **Cómo usarlo**  

### 🔹 Clonar el repositorio  
```bash
git clone https://github.com/BrunoMDonato/django-blog.git
cd Blog_Final
```

### 🔹 Instalar dependencias  
Es recomendable usar un entorno virtual:  
```bash
python -m venv env
source env/bin/activate  # En Mac/Linux
env\Scripts\activate  # En Windows
```

Instalar los paquetes requeridos:  
```bash
pip install -r requirements.txt
```  

⚠ **IMPORTANTE:**  
Si aparece un error al instalar `psycopg2`, significa que necesitas herramientas de compilación.  

Para solucionar esto en Windows, instala **Microsoft Visual C++ Build Tools** con **"Desarrollo para escritorio con C++"** desde:  
🔗 [https://visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/)  

Una vez instaladas, intenta de nuevo:  
```bash
pip install -r requirements.txt
```

### 🔹 Ejecutar el servidor  
```bash
python manage.py runserver
```

---

## **Características del Blog**  
✔ Usuarios con perfil (nombre, email, avatar)  
✔ Publicaciones con título, imagen y contenido  
✔ Comentarios en publicaciones  
✔ Sistema de likes  
✔ Mensajería privada entre usuarios  

---

## **Notas Importantes**  
- Es recomendable usar un entorno virtual para evitar conflictos con paquetes globales.  
- Si tienes problemas con `psycopg2`, instala las herramientas de compilación como se indica arriba.  

---

## 📜 **Licencia**  
Este proyecto está bajo la licencia **MIT**.
