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
class Ticket < ActiveRecord::Base
    has_many :other_activities
    belongs_to :metadata
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

######      MAPS JSON DATA INTO DB TABLES       ######
ticket_data.map do | ticket_iteration |

    if ticket_iteration.has_key?("note")
        #   Put Note data into database
        note = Note.new 
        note.performed_at = ticket_iteration.dig("performed_at"),
        note.performer_type = ticket_iteration.dig("performer_type")
        note.performer_id = ticket_iteration.dig("performer_id")
        note.id = activity.dig( "note", "id" )
        note.note_type = activity.dig( "note", "type" )
        note.save
    else
        other = Other.new 
        other.performed_at = ticket_iteration.dig("performed_at"),
        other.performer_type = ticket_iteration.dig("performer_type")
        other.performer_id = ticket_iteration.dig("performer_id")
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

    end #   end else/if
end     #   end JSON data mapping


pry binding
puts "Finished!"