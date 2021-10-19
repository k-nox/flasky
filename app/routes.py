from flask import Blueprint, json, jsonify


# syntax for instantiating a blueprint
dog_bp = Blueprint("dog", __name__, url_prefix="/dogs")
cat_bp = Blueprint("cat", __name__, url_prefix="/cats")


class Cat:
    def __init__(self, id, name, color, personality):
        self.id = id
        self.name = name
        self.color = color
        self.personality = personality


cats = [
    Cat(1, "Muna", "black", "mischeivious"),
    Cat(2, "Matthew", "spotted", "cuddly"),
    Cat(3, "George", "gray", "sassy")
]


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


# get all cats
@cat_bp.route("", methods=["GET"])
def handle_cats():
    cats_response = [vars(cat) for cat in cats]
    return jsonify(cats_response)


# get one cat
@cat_bp.route("<cat_id>", methods=["GET"])
def handle_cat(cat_id):
    try:
        cat_id = int(cat_id)
    except:
        return "Bad data", 400

    for cat in cats:
        if cat.id == cat_id:
            return vars(cat)

    return "Not found", 404


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
