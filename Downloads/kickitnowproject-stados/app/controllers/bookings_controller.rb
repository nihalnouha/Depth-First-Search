class BookingsController < ApplicationController
  skip_before_action :authenticate_user!,only: [:new, :create]
  skip_before_action :verify_authenticity_token

  def new
    @booking = Booking.new
    @pitch = Stade.find(params[:pitch_id])
  end

  def create
    @booking = Booking.create(booking_params)

    @booking.user = current_user

    if @booking.save
      redirect_to root_path, notice: 'Woo-hoo! Your booking is a go! Please check your email for payment details.'
    else
      redirect_to root_path, alert: 'Tickets Unavailable. Please check again later.'






    end
  end

  private

  def booking_params
    params.require(:booking).permit(:stade_id, :date, :pitch_id)
  end
end
