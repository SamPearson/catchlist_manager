

def on_starting(server):
    print("Initializing Database in master process")
    # Put your database initialization logic here
    from webapp import initialize_database
    initialize_database()
