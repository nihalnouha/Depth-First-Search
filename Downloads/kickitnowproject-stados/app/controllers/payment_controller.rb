class PaymentController < ApplicationController
  #skip_before_action :authenticate_user!,only: [:execute]

  #def execute
    # payment = PayPal::SDK::REST::Payment.find(params[:paymentId])

    # if payment.execute(payer_id: params[:PayerID])
    #   # Le paiement a réussi
    #   flash[:success] = 'Payment successful!'
    # else
    #   # Le paiement a échoué
    #   flash[:error] = payment.error.message
    # end

      # redirect_to root_path
  #end


  # private

  # def payment_params
  #   {
  #     intent: 'sale',
  #     payer: {
  #       payment_method: 'paypal'
  #     },
  #     redirect_urls: {
  #       return_url: 'http://localhost:3000/payments/execute',
  #       cancel_url: 'http://localhost:3000/'
  #     },
  #     transactions: [
  #       {
  #         item_list: {
  #           items: [
  #             {
  #               name: 'Your Product Name',
  #               price: '10.00',
  #               currency: 'USD',
  #               quantity: 1
  #             }
  #           ]
  #         },
  #         amount: {
  #           total: '10.00',
  #           currency: 'USD'
  #         },
  #         description: 'Description of your product'
  #       }
  #     ]
  #   }
  # end
end
