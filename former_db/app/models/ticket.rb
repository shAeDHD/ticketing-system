class Ticket < ApplicationRecord

    # associations go here 
    # has_one :activity
    # belongs_to :user

    # also 'business logic' cusom methods
    accepts_nested_attributes_for :activity, :shipping_address, :coordinates, :note 

    permitted = params.permit( 
        
        :performed_at, :ticket_id, :performer_type, :performer_id, activity: { 
            shipping_address: { 
                :address1, :address2, :city, :state, :postalCode, coordinates: {
                    lat:, lng:
                }   #   close coordinates
            },      #   close shipping_address
            :shipment_date, :category, :contacted_customer, :issue_type, :source, :status, :priority, :group, :agent_id, :request, :product, 
            note: {
                :id, :type
            }       #   close note
        }           #   close activity 
    )               #   close permit()         

end                 #   close Ticket