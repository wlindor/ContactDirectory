from flask import request, jsonify
from config import app, db
from models import Contact

# Get decorator is used to tell the app which URL should trigger the function
@app.route('/contacts', methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    contacts_json = [contact.to_json() for contact in contacts]
    return jsonify({"contacts": contacts_json})


if __name__ == '__main__':
    with app.app_context():
        # create_all() will create any tables in the database that do not already exist
        db.create_all()

    app.run(debug=True)
