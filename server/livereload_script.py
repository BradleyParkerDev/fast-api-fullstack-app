from livereload import Server, shell

def live_reload():
    # Initialize the server
    server = Server()

    # Watch the Tailwind CSS files in server/static/css
    server.watch('server/static/css/*.css')

    # Watch the JavaScript files in server/dist
    server.watch('server/dist/*.js')

    # Watch the template files in server/templates
    server.watch('server/templates/**/*.html')

    # Serve the content from the server directory and enable livereload
    server.serve(root='server', open_url_delay=1)

if __name__ == "__main__":
    live_reload()
