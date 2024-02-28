class AddPriceToStades < ActiveRecord::Migration[7.1]
  def change
    add_column :stades, :price, :decimal
  end
end
