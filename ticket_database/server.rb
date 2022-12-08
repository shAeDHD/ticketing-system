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
# puts ticket_data    #   check == true


ticket_data.map do | ticket_iteration |
    ticket = ticket_iteration
    # ticket_header = Ticket_Header.new 
    # puts ticket.fetch("activity")
    activity = ticket.fetch("activity")
    
    if ticket.fetch("activity") == "note"
        note = Note_Activity.new 
        note.id = ticket.dig( "activity", "note", "id" )
        note.type = ticket.dig( "activity", "note", "type" )
        note.save
    else 
        other = Other_Activity.new
        other.shipping_address = ticket.dig("activity", "shipping_address")
        other.shipment_date = ticket.dig("activity", "shipment_date")
        other.category = ticket.dig("activity", "category")
        other.contacted_customer = ticket.dig("activity", "contacted_customer")
        other.issue_type = ticket.dig("activity", "issue_type")
        other.source = ticket.dig("activity", "source")
        other.status = ticket.dig("activity", "status")
        other.priority = ticket.dig("activity", "priority")
        other.group_id = ticket.dig("activity", "group_id")
        other.agent_id = ticket.dig("activity", "agent_id")
        other.requester = ticket.dig("activity", "requester")
        other.product = ticket.dig("activity", "product")
        other.save
        # puts "no note"
    end
    # if ticket > 4
    #     puts ticket 
    # else
    #     nil
    # end
end