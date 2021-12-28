from my_app import create_app, db
app = create_app()
db.create_all(app=app)
app.run(debug=True)
