from webapp import create_app

app = create_app()


# Only runs if this file execute the app.run
if __name__ == '__main__':
    app.run(debug=True)