from flask import Blueprint, jsonify


# syntax for instantiating a blueprint
dog_bp = Blueprint("dog", __name__, url_prefix="/dogs")


# get all dogs
@dog_bp.route("", methods=["GET"])
def handle_dogs():
    dogs_response = []
    for dog in dogs:
        dogs_response.append(dog.to_dict())

    return jsonify(dogs_response)


# get one dog
@dog_bp.route("/<dog_id>", methods=["GET"])
def handle_dog(dog_id):
    dog_id = int(dog_id)
    for dog in dogs:
        if dog.id == dog_id:
            return dog.to_dict()
    return {"error": "Dog not found"}, 404
