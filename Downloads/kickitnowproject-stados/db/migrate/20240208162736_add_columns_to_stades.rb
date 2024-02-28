class AddColumnsToStades < ActiveRecord::Migration[7.1]
  def change
    add_column :stades, :capacity, :integer
    add_column :stades, :surface_type, :string
    add_column :stades, :availability, :string
    add_column :stades, :map_url, :string
  end
end
