from flask import request, jsonify
from config import app, db
from models import Contact

# Get decorator is used to tell the app which URL should trigger the function
@app.route('/contacts', methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    contacts_json = [contact.to_json() for contact in contacts]
    return jsonify({"contacts": contacts_json})

@app.route('/create_contact', methods=["POST"])
def create_contact():
    first_name = request.json.get('firstName')
    last_name = request.json.get('lastName')
    email = request.json.get('email')

    if not first_name or not last_name or not email:
        return(jsonify({"error": "You must include a first name, last name and email"}), 400)
    
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)

    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    finally:
        db.session.close()

    return jsonify({"message": "Contact created successfully"}), 201

@app.route('/update_contact/<int:id>', methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"error": "Contact not found"}), 404

    data = request.json
    contact.first_name = data.get('firstName', contact.first_name)
    contact.last_name = data.get('lastName', contact.last_name)
    contact.email = data.get('email', contact.email)

    db.session.commit()

    return jsonify({"message": "Contact updated successfully"}), 201

@app.route('/delete_contact/<int:id>', methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"error": "Contact not found"}), 404

    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "Contact deleted successfully"}), 201

if __name__ == '__main__':
    with app.app_context():
        # create_all() will create any tables in the database that do not already exist
        db.create_all()

    app.run(debug=True)
