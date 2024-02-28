class Booking < ApplicationRecord
  belongs_to :stade
  belongs_to :user

  after_create :send_invoice_email

  private

  def send_invoice_email
    recipient_email = "elhaounouhaila@gmail.com"
    BillingMailer.invoice_email(recipient_email).deliver_now
  end

end
