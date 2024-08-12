from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from datetime import datetime

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # Importer et enregistrer les routes
    from . import routes
    app.register_blueprint(routes.bp)

    # Ajouter le filtre pour formater les dates
    @app.template_filter('format_dates')
    def format_dates(availability_str):
        dates = availability_str.split(',')
        formatted_dates = []
        for date_str in dates:
            try:
                formatted_date = datetime.strptime(date_str, '%Y-%m-%d').strftime('%d/%m/%Y')
                formatted_dates.append(formatted_date)
            except ValueError:
                formatted_dates.append("Invalid date")
        return ', '.join(formatted_dates)

    return app
