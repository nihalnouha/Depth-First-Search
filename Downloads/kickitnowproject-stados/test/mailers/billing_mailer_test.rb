require "test_helper"

class BillingMailerTest < ActionMailer::TestCase
  test "invoice_email" do
    mail = BillingMailer.invoice_email
    assert_equal "Invoice email", mail.subject
    assert_equal ["to@example.org"], mail.to
    assert_equal ["from@example.com"], mail.from
    assert_match "Hi", mail.body.encoded
  end

end
