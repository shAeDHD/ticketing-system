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
        # attr_accessor "shipping_address", "shipment_date", "category", "contacted_customer", "issue_type", "source", "status", "priority", "group_id", "agent_id", "requester", "product", "save"
    end
end
class TicketHeader < ActiveRecord::Base
    def create

    end
end
class Note_Activity < ActiveRecord::Base
    def create
        @Note_Activity = Note_Activity.new
        # attr_accessor "id", "type"
    end
end
class Other_Activity < ActiveRecord::Base
    def create
        @Other_Activity = Other_Activity.new    
    end
end

parent_file = File.expand_path("..", Dir.pwd)
file = File.open(File.expand_path("#{parent_file}/ticket_generator/ticket_data.json"))
ticket_data = JSON.load file
file.close 
puts ActiveRecord::Base.connection.tables

ticket_data.map do | ticket_iteration |
    


    activity = ticket_iteration.fetch("activity")

    if activity.has_key?("note")
        note = Note_Activity.new 
        note.id = activity.dig( "note", "id" )
        note.type = activity.dig( "note", "type" )
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
end

binding.pry
puts "Finished!"