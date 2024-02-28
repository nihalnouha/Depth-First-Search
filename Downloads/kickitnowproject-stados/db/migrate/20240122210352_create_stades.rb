class CreateStades < ActiveRecord::Migration[7.1]
  def change
    create_table :stades do |t|
      t.string :name
      t.string :desc
      t.string :img

      t.timestamps
    end
  end
end
