from app import app, db
from flask import request, jsonify
from models import Staff


# get all staffs
@app.route("/api/staffs", methods=["GET"])
def get_staffs():
    staffs = Staff.query.all()
    result = [staff.to_json() for staff in staffs]
    return jsonify(result)


# create staff
@app.route("/api/staff/create", methods=["POST"])
def create_staff():
    try:
        data = request.json
        
        required_fields =["name", "role", "description", "gender"]
        for field in required_fields:
            if field not in data or not data.get(field):
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        name = data.get("name")
        role = data.get("role")
        description = data.get("description")
        gender = data.get("gender")
        
        # fetch avatar image based on gender
        if gender == "male":
            img_url = f"https://avatar.iran.liara.run/public/boy?username={name}"
        elif gender == "female":
            img_url = f"https://avatar.iran.liara.run/public/girl?username={name}"    
        else:
            img_url = None
            
        new_staff = Staff(name=name, role=role, description=description, gender=gender, img_url=img_url)
        db.session.add(new_staff)
        db.session.commit()
        
        return jsonify(new_staff.to_json()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}), 500

    
# update staff
@app.route("/api/staff/<int:id>", methods=["PATCH"])
def update_staff(id):
    try:
        staff = Staff.query.get(id)
        if staff is None:
            return jsonify({"error":"Staff not found"}), 404

        data = request.json
        
        staff.name = data.get("name", staff.name)
        staff.role = data.get("role", staff.role)
        staff.description = data.get("description", staff.description)
        staff.gender = data.get("gender", staff.gender)
        
        db.session.commit()
        return jsonify(staff.to_json()),200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}),500

   
# delete staff
@app.route("/api/staff/<int:id>", methods=["DELETE"])
def delete_staff(id):
    try:
        staff = Staff.query.get(id)
        if staff is None:
            return jsonify({"error":"Staff not found"}), 404
        db.session.delete(staff)
        db.session.commit()
        return jsonify({"msg":"Staff deleted"}),200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}),500


