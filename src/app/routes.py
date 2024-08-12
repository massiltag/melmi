from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from . import db
from .models import Event, Availability
from .forms import EventForm, AvailabilityForm
from .utils import find_best_time
from sqlalchemy import func

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(name=form.name.data)
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('main.event', event_id=event.id))
    return render_template('index.html', form=form)

@bp.route('/event/<int:event_id>', methods=['GET', 'POST'])
def event(event_id):
    event = Event.query.get_or_404(event_id)
    form = AvailabilityForm()
    if form.validate_on_submit():
        # Recherche d'un utilisateur existant avec le même nom (insensible à la casse)
        existing_availability = Availability.query.filter_by(event_id=event.id).filter(
            func.lower(Availability.name) == func.lower(form.name.data)).first()
        
        if existing_availability:
            # Mise à jour de la disponibilité existante
            existing_availability.available_times = form.available_times.data
            flash(f'Disponibilité mise à jour pour {form.name.data}.', 'success')
        else:
            # Ajout d'une nouvelle disponibilité
            availability = Availability(
                event_id=event.id,
                name=form.name.data,
                available_times=form.available_times.data
            )
            db.session.add(availability)
            flash('Votre disponibilité a été enregistrée.', 'success')
        
        db.session.commit()
        return redirect(url_for('main.event', event_id=event.id))

    availabilities = Availability.query.filter_by(event_id=event.id).all()
    
    # Calcul des disponibilités communes
    best_time_slots, _ = find_best_time(availabilities)

    return render_template('event.html', event=event, form=form, 
                           availabilities=availabilities, 
                           best_time_slots=best_time_slots)

@bp.route('/event/<int:event_id>/names', methods=['GET'])
def get_names(event_id):
    # Récupérer les noms des disponibilités existantes pour l'événement
    names = db.session.query(Availability.name).filter_by(event_id=event_id).all()
    # Retourner une liste de noms en JSON
    return jsonify([name[0] for name in names])
