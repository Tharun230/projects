# 📦 HelpDesk Lite - A Mini Ticketing System in Flask (Python)

from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory ticket store
tickets = {}

# Create Ticket
@app.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.get_json()
    ticket_id = str(uuid4())
    ticket = {
        'id': ticket_id,
        'title': data.get('title'),
        'description': data.get('description'),
        'status': 'open'
    }
    tickets[ticket_id] = ticket
    return jsonify({'message': 'Ticket created', 'ticket': ticket}), 201

# Get All Tickets
@app.route('/tickets', methods=['GET'])
def get_all_tickets():
    return jsonify(list(tickets.values())), 200

# Get Single Ticket
@app.route('/tickets/<ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    ticket = tickets.get(ticket_id)
    if not ticket:
        return jsonify({'error': 'Ticket not found'}), 404
    return jsonify(ticket), 200

# Update Ticket Status
@app.route('/tickets/<ticket_id>', methods=['PATCH'])
def update_ticket(ticket_id):
    data = request.get_json()
    ticket = tickets.get(ticket_id)
    if not ticket:
        return jsonify({'error': 'Ticket not found'}), 404
    ticket['status'] = data.get('status', ticket['status'])
    return jsonify({'message': 'Ticket updated', 'ticket': ticket}), 200

# Delete Ticket
@app.route('/tickets/<ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    if ticket_id in tickets:
        del tickets[ticket_id]
        return jsonify({'message': 'Ticket deleted'}), 200
    return jsonify({'error': 'Ticket not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
