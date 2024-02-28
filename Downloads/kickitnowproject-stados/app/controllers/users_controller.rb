class UsersController < ApplicationController
  def history
    @user = current_user
    @bookings = @user.bookings
  end
end
