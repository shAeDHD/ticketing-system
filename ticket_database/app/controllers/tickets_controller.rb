class TicketsController < ApplicationController
    def home
        
    end
end

permitted = params.permit( 
    activities_data: { 
      :performed_at, :ticket_id, :performer_type, :performer_id, activity: { 
        shipping_address: { 
          :address1, :address2, :city, :state, :postalCode, coordinates: {
              lat:, lng:
            } #   close coordinates
        },    #   close shipping_address
        :shipment_date, :category, :contacted_customer, :issue_type, :source, :status, :priority, :group, :agent_id, :request, :product, 
        note: {
          :id, :type
        }     #   close note
      }       #   close activity 
    }         #   close activites_data 
  )           #   close .permit()
