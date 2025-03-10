#!/usr/bin/env python3
"""
Contains API for artisan
"""
import os
import uuid
from PIL import Image
from flask import Blueprint
from werkzeug.datastructures import MultiDict
from extensions import db
from models.user import User
from models.artisan import Artisan
from models.client import Client
from forms.artisan import ArtisanProfileForm
from flask import (flash, request, current_app, jsonify)
# from flask_login import current_user, login_required
from flask_jwt_extended import jwt_required, get_jwt_identity


# create artisans blueprint
artisans_Bp = Blueprint('artisans', __name__)


def save_picture(form_picture: any) -> str:
    """ function to save the updated profile picture"""
    # get a random hex to avoid file name collision
    random_hex = uuid.uuid4().hex[:8]
    # get the file extension
    _, file_ext = os.path.splitext(form_picture.filename)
    # create a unique file name
    pic_fname = random_hex + file_ext
    #  Select path depending on the os
    if os.name == 'nt':
        # Windows path
        file_path = 'static\\profile_pics'
    else:
        # Unix/Linux/Mac path
        file_path = 'static/profile_pics'
    # create the path to save the file
    picture_path = os.path.join(current_app.root_path, file_path, pic_fname)
    # resize the image
    output_size = (125, 125)
    open_image = Image.open(form_picture)
    open_image.thumbnail(output_size)
    # save the image
    open_image.save(picture_path)
    # return the file name
    return pic_fname


def update_user_object(form: ArtisanProfileForm, current_user: User):
    """ Update the user object details """
    if form.picture.data:
        if current_user.image_file != form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
    current_user.username = form.username.data
    current_user.email = form.email.data.lower()
    current_user.phone_number = form.phone_number.data
    current_user.location = form.location.data


def update_artisan_object(form: ArtisanProfileForm, current_user: User):
    """ Update the artisan object details """
    if not current_user.artisan:
        current_user.artisan = Artisan(user=current_user)
    current_user.artisan.name = form.username.data
    current_user.artisan.email = form.email.data.lower()
    current_user.artisan.phone_number = form.phone_number.data
    current_user.artisan.location = form.location.data
    current_user.artisan.specialization = form.specialization.data
    current_user.artisan.salary_per_hour = form.salary_per_hour.data
    current_user.artisan.skills = form.skills.data
    current_user.artisan.geocode_location()


@artisans_Bp.route("/artisan", methods=['GET', 'POST', 'OPTIONS'],
                   strict_slashes=False)
@artisans_Bp.route(
    "/artisan/<username>", methods=['GET', 'POST', 'OPTIONS'],
    strict_slashes=False)
@jwt_required()
def artisan_profile(username: str = "") -> str:
    """ artisan profile route
    GET /artisan
    GET /artisan/<username>
    POST /artisan
    POST /artisan/<username>
    Return:
        - Success: JSON with artisan object
            - JSON body:
                - name
                - email
                - phone_number
                - location
                - longitude
                - latitude
                - specialization
                - skills
                - salary_per_hour
                - image_file
                - bookings
        - Error:
            - 401 if user is not authenticated
            - 403 if user is not an artisan
            - 400 if an error occurred during update
            - 400 if form validation failed
    """
    # check OPTIONS method
    if request.method == 'OPTIONS':
        return jsonify({"message": "Preflight request"}), 200

    # check if user is authenticated
    user_id = get_jwt_identity()
    current_user = User.query.filter_by(id=user_id).first()
    if not current_user\
            or (username != current_user.username and username != ""):
        return jsonify({"error": "User not authenticated"}), 401

    # # check if user is an artisan
    if current_user.role != 'Artisan':
        return jsonify({"error": "User is not an artisan"}), 403

    # Set up Artisan profile form and disable CSRF
    form = ArtisanProfileForm(meta={'csrf': False})
    # handle GET request
    if request.method == "GET":
        # return the artisan object
        return jsonify(current_user.artisan.to_dict()), 200

    # handle POST request after validating the form
    elif form.validate_on_submit():
        try:
            # update the user and artisan profile
            update_user_object(form, current_user)
            update_artisan_object(form, current_user)
            # commit the changes
            db.session.commit()
            # flash a success message
            flash('Your profile has been updated!', 'success')
            # return the artisan object
            return jsonify(current_user.artisan.to_dict()), 200

        except Exception as e:
            # If an error occurs, rollback the session
            db.session.rollback()
            # return error if unable to complete registration
            return jsonify(
                {"error": "An error occurred during updating"}), 400
    else:
        # return error if form validation failed
        return jsonify({
            "message": "Invalid form data",
            "error": form.errors
        }), 400


@artisans_Bp.route('/all_artisans', methods=['GET', 'OPTIONS'],
                   strict_slashes=False)
@jwt_required()
def get_artisans():
    """ route to get all artisans
    GET /bookings
        Return:
        - Success: JSON with list of all artisans
        - Error:
            - 401 if user is not authenticated
            - 403 if user is not an client
    """
    # check OPTIONS method
    if request.method == 'OPTIONS':
        return jsonify({"message": "Preflight request"}), 200
    # check if user is authenticated
    user_id = get_jwt_identity()
    current_user = User.query.filter_by(id=user_id).first()
    if not current_user:
        return jsonify({"error": "User not authenticated"}), 401
    # check if user is an artisan
    if current_user.role != 'Client':
        return jsonify({"error": "User is not a client"}), 403
    # get all artisans
    artisans = Artisan.query.all()

    # check if the request is a GET request
    if 'page' not in request.args:
        data = [artisan.to_dict() for artisan in artisans]
        sorted_artisans = sorted(data, key=lambda x: x['username'])
        return jsonify(sorted_artisans), 200
    else:
        # Get query parameters for pagination
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        # Calculate start and end indices
        start = (page - 1) * per_page
        end = start + per_page
        # Paginate the data
        data = [artisan.to_dict() for artisan in artisans]
        sorted_artisans = sorted(data, key=lambda x: x['username'])
        paginated_data = sorted_artisans[start:end]
        total_pages = (len(data) + per_page - 1) // per_page
        # return the list of artisans and pagination information
        return jsonify({
            'artisans': paginated_data,
            'total_pages': total_pages,
            'current_page': page
        }), 200


@artisans_Bp.route('/location', methods=['GET', 'OPTIONS'],
                   strict_slashes=False)
@jwt_required()
def location() -> str:
    """ route to get the location of the artisan
    GET /location
        Return:
        - Success: JSON with latitude and longitude
        - Error:
            - 401 if user is not authenticated
            - 403 if user is not an artisan
    """
    # check OPTIONS method
    if request.method == 'OPTIONS':
        return jsonify({"message": "Preflight request"}), 200
    # check if user is authenticated
    user_id = get_jwt_identity()
    current_user = User.query.filter_by(user_id=user_id).first()
    if not current_user:
        return jsonify({"error": "User not authenticated"}), 401
    # check if user is an artisan
    if current_user.role != 'Artisan':
        return jsonify({"error": "User not authenticated"}), 403
    # get the location of the artisan
    map = current_user.artisan.geocode_location()
    if map:
        # return the latitude and longitude
        return jsonify(
            {
                'lat': current_user.artisan.latitude,
                'long': current_user.artisan.longitude
            }
        )
