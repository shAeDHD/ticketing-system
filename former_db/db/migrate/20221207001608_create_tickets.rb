class CreateTickets < ActiveRecord::Migration[5.2]
  def change
    create_table :tickets, id: false do |t|

        t.string :performed_at, null: false
        t.integer :ticket_id, null: false
        t.string  :performer_type, null: false
        t.integer :performer_id, null: false
        t.string  :activity, null: false
        t.string  :note
        t.integer :id
        t.integer :type
        t.string  :shipping_address
        t.text  :address1
        t.text  :address2
        t.string  :city 
        t.string  :state
        t.integer :postalCode
        t.string  :coordinates
        t.integer  :lat
        t.integer  :lng
        t.text :shipment_date
        t.string :category
        t.boolean :contacted_customer
        t.string :issue_type
        t.integer :source
        t.string :status
        t.integer :priority
        t.string :group
        t.integer :agent_id
        t.integer :requester
        t.string :product

    end
  end
end