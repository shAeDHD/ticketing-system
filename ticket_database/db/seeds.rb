
# generated_tickets = File.read(~/Users/shaeriches/coding-stuff/tech-challenges/aginic/ticket_generator/json_ticket_data.json)
# JSON.parse( generated_tickets ).each do | json_ticket |
#     Ticket.create!(json_ticket)
# end

generated_tickets = File.read("C:/Users/shaeriches/coding-stuff/tech-challenges/aginic/ticket_generator/json_ticket_data.json")

JSON.parse( generated_tickets ).each do | json_ticket |
    Ticket.create!(json_ticket)
end