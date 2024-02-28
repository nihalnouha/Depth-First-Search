class BillingMailer < ApplicationMailer

  # Subject can be set in your I18n file at config/locales/en.yml
  # with the following lookup:
  #
  #   en.billing_mailer.invoice_email.subject
  #
  def invoice_email(recipient_email)
    @user = User.find_by(email: recipient_email)
    mail(to: recipient_email, subject: "Facture pour votre achat")
  end
  
end
