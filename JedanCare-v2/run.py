from app import create_app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)


