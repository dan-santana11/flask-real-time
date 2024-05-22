from repository.database import db

class Payment(db.Model):
    # id, value, paid, bank_payment_id, qrcode, expiration_date
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)
    paid = db.Column(db.Boolean, default=False)
    bank_payment_id = db.Column(db.Integer)
    qr_code = db.Column(db.String(100))
    expiration_date = db.Column(db.DateTime) # 2024-01-01 00:00:00