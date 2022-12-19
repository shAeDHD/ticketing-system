require 'sqlite3'
require 'pry'
require 'active_record'
require 'json'

ActiveRecord::Base.establish_connection(
    :adapter => 'sqlite3',
    :database => 'database.db'
)
class Metadata < ActiveRecord::Base
    has_one :ticket_header
    has_many :other_activities, through: :ticket_header
    has_one :note_activity, through: :ticket_header
    def create
        puts "made to metadata new" 
    end

    def start_time(  )
    end
end
class Ticket_Id < ActiveRecord::Base
    has_many :other_activities
    
    def create
    end
end
class Note_Ticket < ActiveRecord::Base
    belongs_to :ticket_header
    # belongs_to :metadata, through: :ticket_header
    def create 
    end
end
class Other_Ticket < ActiveRecord::Base
    belongs_to :ticket_header
    # belongs_to :metadata, through: :ticket_header
    def create
    end
end

parent_file = File.expand_path("..", Dir.pwd)
file = File.open(File.expand_path("#{parent_file}/ticket_generator/ticket_data.json"))
ticket_data = JSON.load file
file.close 
puts ActiveRecord::Base.connection.tables

######      MAPS JSON SEED DATA INTO DB TABLES       ######
# FIRST. delete all pre-existing to avoid doubling up & errors.
Ticket_Id.destroy_all
Note_Ticket.destroy_all
Other_Ticket.destroy_all

ticket_data.map do | ticket_iteration |
    ticket_id = Ticket_Id.new 
    ticket_id.ticket_id = ticket_iteration.dig("ticket_id")
    ticket_id.save
    puts ticket_iteration.dig("ticket_id")

    if ticket_iteration.dig("activity").has_key?("note")
        #   Put Note data into database
        note = Note_Ticket.new 
        note.performed_at = ticket_iteration.dig("performed_at")
        note.performer_type = ticket_iteration.dig("performer_type")
        note.performer_id = ticket_iteration.dig("performer_id")
        note.note_id = ticket_iteration.dig("activity", "note", "id" )
        note.note_type = ticket_iteration.dig("activity", "note", "type" )
        note.save
    else
        other = Other_Ticket.new 
        other.performed_at = ticket_iteration.dig("performed_at")
        other.performer_type = ticket_iteration.dig("performer_type")
        other.performer_id = ticket_iteration.dig("performer_id")
        other.shipping_address = ticket_iteration.dig("activity", "shipping_address" )
        other.shipment_date = ticket_iteration.dig("activity", "shipment_date" )
        other.category = ticket_iteration.dig("activity", "category" )
        other.contacted_customer = ticket_iteration.dig("activity", "contacted_customer" )
        other.issue_type = ticket_iteration.dig("activity", "issue_type" )
        other.source = ticket_iteration.dig("activity", "source" )
        other.status = ticket_iteration.dig("activity", "status" )
        other.priority = ticket_iteration.dig("activity", "priority" )
        other.group_id = ticket_iteration.dig("activity", "group_id" )
        other.agent_id = ticket_iteration.dig("activity", "agent_id" )
        other.requester = ticket_iteration.dig("activity", "requester" )
        other.product = ticket_iteration.dig("activity", "product" )
        other.save
    end #   end else/if
end     #   end JSON data mapping


pry binding
puts "Finished!"