class AddTeamToStades < ActiveRecord::Migration[7.1]
  def change
    add_column :stades, :team, :string
  end
end
