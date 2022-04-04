from flask import Flask
from internal_igeekuplay_notion.users import user_blueprint
from internal_igeekuplay_notion.contacts import contact_blueprint
from internal_igeekuplay_notion.events import event_blueprint
from internal_igeekuplay_notion.companies import company_blueprint
from internal_igeekuplay_notion.tasks import task_blueprint
from internal_igeekuplay_notion.projects import project_blueprint
from internal_igeekuplay_notion.invoices import invoice_blueprint

app = Flask(__name__)
app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(contact_blueprint, url_prefix='/contacts')
app.register_blueprint(event_blueprint, url_prefix='/events')
app.register_blueprint(company_blueprint, url_prefix='/companies')
app.register_blueprint(task_blueprint, url_prefix='/tasks')
app.register_blueprint(project_blueprint, url_prefix='/projects')
app.register_blueprint(invoice_blueprint, url_prefix='/invoices')

if __name__ == '__main__':
    app.run()