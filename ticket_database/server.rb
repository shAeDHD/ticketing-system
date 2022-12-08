require 'sqlite3'
require 'pry'
require 'active_record'
require 'json'
require 'active_record'

ActiveRecord::Base.establish_connection(
    :adapter => 'sqlite3',
    :database => 'database.db'
)
class Metadata < ActiveRecord::Base
    def create
    end
end
class Ticket_Header < ActiveRecord::Base
    def create
    end
end
class Note_Activity < ActiveRecord::Base
    def create 
    end
end
class Other_Activity < ActiveRecord::Base
    def create
    end
end

parent_file = File.expand_path("..", Dir.pwd)
file = File.open(File.expand_path("#{parent_file}/ticket_generator/ticket_data.json"))
ticket_data = JSON.load file
file.close 
puts ActiveRecord::Base.connection.tables

######      MAPS JSON DATA INTO DB TABLES       ######
ticket_data.map do | ticket_iteration |
    
    iteration_th = Ticket_Header.new
    iteration_th.performed_at = ticket_iteration.dig("performed_at"),
    iteration_th.ticket_id = ticket_iteration.dig("ticket_id"),
    iteration_th.performer_type = ticket_iteration.dig("performer_type")
    iteration_th.performer_id = ticket_iteration.dig("performer_id")
    iteration_th.save

    activity = ticket_iteration.fetch("activity")

    if activity.has_key?("note")
        note = Note_Activity.new 
        note.id = activity.dig( "note", "id" )
        note.note_type = activity.dig( "note", "type" )
        note.save
    else
        other = Other_Activity.new 
        other.shipping_address = activity.dig( "shipping_address" )
        other.shipment_date = activity.dig( "shipment_date" )
        other.category = activity.dig( "category" )
        other.contacted_customer = activity.dig( "contacted_customer" )
        other.issue_type = activity.dig( "issue_type" )
        other.source = activity.dig( "source" )
        other.status = activity.dig( "status" )
        other.priority = activity.dig( "priority" )
        other.group_id = activity.dig( "group_id" )
        other.agent_id = activity.dig( "agent_id" )
        other.requester = activity.dig( "requester" )
        other.product = activity.dig( "product" )
        other.save
        # puts "no note"
    end
    # if ticket > 4
    #     puts ticket 
    # else
    #     nil
    # end
end     #   end JSON data mapping

puts "Finished!"