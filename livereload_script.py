# livereload_script.py
from livereload import Server

def start_livereload():
    server = Server()
    server.watch('templates/')
    server.watch('static/css/')
    server.watch('static/js/')
    server.serve(root='.', port=5500)  # Serve on port 5500

if __name__ == "__main__":
    start_livereload()
