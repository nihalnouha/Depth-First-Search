# app/models/contact.rb
class Contact < MailForm::Base
  attribute :name,        :validate => true
  attribute :email,       :validate => /\A([\W\.%\+\-]+)+@([\W\-]+\.)+([\W]{2,})\Z/i
  attribute :file,        :attachment => true
  attribute :message
  attribute :username,    :captcha => true

  def headers(recipient_email)
    {
      subject: "Sujet de l'e-mail",
      to: recipient_email,
      from: "#{name} <#{email}>"
    }
  end
end
