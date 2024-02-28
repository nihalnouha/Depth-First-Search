# Preview all emails at http://localhost:3000/rails/mailers/billing_mailer
class BillingMailerPreview < ActionMailer::Preview

  # Preview this email at http://localhost:3000/rails/mailers/billing_mailer/invoice_email
  def invoice_email
    BillingMailer.invoice_email
  end

end
