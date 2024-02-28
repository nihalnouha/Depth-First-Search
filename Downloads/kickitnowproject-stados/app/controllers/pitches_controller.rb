class PitchesController < ApplicationController
  skip_before_action :authenticate_user!,only: [:index]
  def index
    @pitches = Stade.all
  end

  def show
    @pitch = Stade.find(params[:id])
    #respond_to do |format|
      # format.html # Show the pitch
      #format.json { render json: @pitch }
    #end

    @booking = Booking.new
  end

  def book
    @pitch  = Stade.find(params[:id])
    if @pitch .reserved
      flash[:alert] = 'Le stade est déjà réservé.'
    else
      # Logique de réservation
      @pitch .update(reserved: true)
      flash[:notice] = 'Stade réservé avec succès.'
    end
    redirect_to pitches_path
  end
end
