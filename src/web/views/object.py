from flask import Blueprint, render_template, redirect, url_for, flash, \
                  request, abort
from flask_login import login_required, current_user

from bootstrap import db, application
from web.models import Schema, JsonObject
from web.forms import AddObjectForm

object_bp = Blueprint('object_bp', __name__, url_prefix='/object')
objects_bp = Blueprint('objects_bp', __name__, url_prefix='/objects')


@object_bp.route('/editor/<int:object_id>', methods=['GET'])
@login_required
def edit_json(schema_id=None, object_id=None):
    action = "Edit an object"
    head_titles = [action]

    json_object = JsonObject.query.filter(JsonObject.id == object_id).first()
    schema = json_object.schema

    return render_template('edit_json.html', action=action,
                            head_titles=head_titles,
                            schema=schema,
                            json_object=json_object)


@object_bp.route('/create', methods=['GET'])
@object_bp.route('/edit/<int:object_id>', methods=['GET'])
@login_required
def form(schema_id=None, object_id=None):
    action = "Create an object"
    head_titles = [action]

    schema_id = request.args.get('schema_id', None)
    # schema = Schema.query.filter(Schema.id == schema_id).first()

    form = AddObjectForm()
    form.schema_id.data = schema_id

    if object_id is None:
        return render_template('edit_object.html', action=action,
                               head_titles=head_titles, form=form)

    json_object = JsonObject.query.filter(JsonObject.id == object_id).first()
    form = AddObjectForm(obj=json_object)
    action = "Edit an object"
    head_titles = [action]
    head_titles.append(json_object.name)
    return render_template('edit_object.html', action=action,
                           head_titles=head_titles,
                           form=form, json_object=json_object)


@object_bp.route('/create', methods=['POST'])
@object_bp.route('/edit/<int:object_id>', methods=['POST'])
@login_required
def process_form(object_id=None):
    form = AddObjectForm()

    if not form.validate():
        return render_template('edit_object.html', form=form)

    if object_id is not None:
        pass # edit an object

    # Create a new JsonObject
    new_object = JsonObject(name=form.name.data,
                            description=form.description.data,
                            schema_id=form.schema_id.data)
    db.session.add(new_object)
    try:
        db.session.commit()
    except Exception as e:
        # TODO: display the error
        return redirect(url_for('object_bp.form', object_id=new_object.id))
    return redirect(url_for('object_bp.form', object_id=new_object.id))