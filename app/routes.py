from flask import Blueprint, jsonify


# syntax for instantiating a blueprint
dog_bp = Blueprint("dog", __name__, url_prefix="/dogs")


class Dog:
    def __init__(self, id, name, breed, tricks=None):
        self.id = id
        self.name = name
        self.breed = breed
        self.tricks = tricks or []

    def to_dict(self):
        tricks = self.tricks or "No Tricks"
        return {
            "id": self.id,
            "name": self.name,
            "breed": self.breed,
            "tricks": tricks
        }


dogs = [
    Dog(1, "mac", "greyhound"),
    Dog(2, "sparky", "schnauzer"),
    Dog(3, "teddy", "golden retriever")
]


@dog_bp.route("", methods=["GET"])
def handle_dogs():
    dogs_response = []
    for dog in dogs:
        dogs_response.append(dog.to_dict())

    return jsonify(dogs_response)


@dog_bp.route("/<dog_id>", methods=["GET"])
def handle_dog(dog_id):
    dog_id = int(dog_id)
    for dog in dogs:
        if dog.id == dog_id:
            return dog.to_dict()
