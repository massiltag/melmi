from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from . import db
from .models import Event, Availability
from .forms import EventForm, AvailabilityForm
from .utils import find_best_time

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(name=form.name.data)
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('main.event', slug=event.slug))
    return render_template('index.html', form=form)

@bp.route('/event/<slug>', methods=['GET', 'POST'])
def event(slug):
    event = Event.query.filter_by(slug=slug).first_or_404()
    form = AvailabilityForm()
    if form.validate_on_submit():
        existing_availability = Availability.query.filter_by(name=form.name.data, event_id=event.id).first()
        if existing_availability:
            existing_availability.available_times = form.available_times.data
        else:
            availability = Availability(name=form.name.data, available_times=form.available_times.data, event=event)
            db.session.add(availability)
        db.session.commit()
        return redirect(url_for('main.event', slug=slug))
    
    availabilities = event.availabilities
    best_time_slots, _ = find_best_time(availabilities)
    return render_template('event.html', event=event, form=form, availabilities=availabilities, best_time_slots=best_time_slots)

@bp.route('/get-names/<int:event_id>')
def get_names(event_id):
    availabilities = Availability.query.filter_by(event_id=event_id).all()
    names = [availability.name for availability in availabilities]
    return jsonify(names)
