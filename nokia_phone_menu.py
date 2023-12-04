print("List of menu functions")
print("1. Phonebook")
print("2. Messages")
print("3. Chat")
print("4. Call register")
print("5. Tones")
print("6. Settings")
print("7. Call divert")
print("8. Games")
print("9. Calculator")
print("10. Remiinders")
print("11. Clock")
print("12. Profiles")
print("13. SIM services")

menu = int(input("Select an option: "))

if menu == 1:
	print("1. Search")
	print("2. Service Nos")
	print("3. Add name")
	print("4. Erase")
	print("5. Edit")
	print("6. Assign tone")
	print("7. Send b'card")
	print("8. Options")
	print("9. Speed dials")
	print("10. Voice tags")

	phonebook_menu = int(input("Select an option: "))
	
	if phonebook_menu == 1:
		print("Search")
	
	if phonebook_menu == 2:
		print("Service Nos")

	if phonebook_menu == 3:
		print("Add name")

	if phonebook_menu == 4:
		print("Erase")

	if phonebook_menu == 5:
		print("Edit")

	if phonebook_menu == 6:
		print("Assign tone")
	
	if phonebook_menu == 7:
		print("Send b'card")

	if phonebook_menu == 8:
		print("1. Type of view")
		print("2. Memory status")
	
		options_menu = int(input("Select an option: "))
	
		if options_menu == 1:
			print("Type of view")

		if options_menu == 2:
			print("Memory status")

	if phonebook_menu == 9:
		print("Speed dials")

	if phonebook_menu == 10:
		print("Voice tags")

if menu == 2:
	print("1. Write messages")
	print("2. Inbox")
	print("3. Outbox")
	print("4. Picture messages")
	print("5. Templates")
	print("6. Smileys")
	print("7. Messages settings")
	print("8. Info service")
	print("9. Voice mailbox number")
	print("10. Service command editor")

	messages_menu = int(input("Select an option: "))

	if messages_menu == 1:
		print("Write messages")

	if messages_menu == 2:
		print("Inbox")

	if messages_menu == 3:
		print("Outbox")

	if messages_menu == 4:
		print("Picture messages")

	if messages_menu == 5:
		print("Templates")
	
	if messages_menu == 6:
		print("Smileys")

	if messages_menu == 7:
		print("1. Set1")
		print("2. Common")
		
		message_settings_menu = int(input("Select an option: "))

		if message_settings_menu == 1:
			print("1. Message centre number")
			print("2. Messages sent as")
			print("3. Message validity")

			set_menu = int(input("Select an option: "))
			
			if set_menu == 1:
				print("Message centre number")

			if set_menu == 2:
				print("Message sent as")

			if set_menu == 3:
				print("Message validity")

		if message_settings_menu == 2:
			print("1. Delivery reports")
			print("2. Reply via same centre")
			print("3. Character support")

			common_menu = int(input("Select an option: "))
			
			if common_menu == 1:
				print("Delivery reports")

			if common_menu == 2:
				print("Reply via same centre")
	
			if common_menu == 3:
				print("Character support")
		
	if messages_menu == 8:
		print("Info service")

	if messages_menu == 9:
		print("Voice mailbox number")

	if messages_menu == 10:
		print("Service command editor")	

if menu == 3:
	print("Chat")

if menu == 4:
	print("1. Missed calls")
	print("2. Received calls")
	print("3. Dialled numbers")
	print("4. Erase recent call lists")
	print("5. Show call duration")
	print("6. Show call costs")
	print("7. Call cost settings")
	print("8. Prepaid credit")

	call_register_menu = int(input("Select an option: "))
	
	if call_register_menu == 1:
		print("Missed calls")

	if call_register_menu == 2:
		print("Received calls")

	if call_register_menu == 3:
		print("Dialled numbers")

	if call_register_menu == 4:
		print("Erase recent call lists")	

	if call_register_menu == 5:
		print("1. Last call duration")
		print("2. All calls' duration")
		print("3. Received call's duration")
		print("4. Dialled calls's duration")
		print("5. Clear timers")
		
		show_call_duration = int(input("Select an option: "))
		
		if show_call_duration == 1:
			print("Last call cost")
		
		if show_call_duration == 2:
			print("All calls' duration")

		if show_call_duration == 3:
			print("Received calls' duration")

		if show_call_duration == 4:
			print("Dialled calls' duration")

		if show_call_duration == 5:
			print("Clear timers")
		
	if call_register_menu == 6:
		print("1. Last call cost" )
		print("2. All calls' cost")
		print("3. Clear counters")

		show_call_costs = int(input("Select an option: "))
		
		if show_call_costs == 1:
			print("Last call cost")

		if show_call_costs == 2:
			print("All calls' cost")

		if show_call_costs == 3:
			print("Clear counters")
		
	if call_register_menu == 7:
		print("1. Call cost limit")
		print("2. Show cost in")

		call_cost_settings = int(input("Select an option: "))

		if call_cost_settings == 1:
			print("Call cost limit")

		if call_cost_settings == 2:
			print("Show costs in")
	
	if call_register_menu == 8:
		print("Prepaid credit")
		
if menu == 5:
	print("1. Ringing tone")
	print("2. Ringing volume")
	print("3. Incoming call alert")
	print("4. Composer")
	print("5. Message alert tone")
	print("6. Keypad tones")
	print("7. Warning and game tones")
	print("8. Vibrating alert")
	print("9. Screen saver")

	tones_menu = int(input("Select an option: "))
	
	if tones_menu == 1:
		print("Ringing tone")
 
	if tones_menu == 2:
		print("Ringing volume")

	if tones_menu == 3:
		print("Incoming call alert")

	if tones_menu == 4:
		print("Composer")

	if tones_menu == 5:
		print("Message alert tone")

	if tones_menu == 6:
		print("Keypad tones")

	if tones_menu == 7:
		print("Warning and game tones")

	if tones_menu == 8:
		print("Vibrating alert")

	if tones_menu == 9:
		print("Screen saver")

if menu == 6:
	print("1. Call settings")
	print("2. Phone settings")
	print("3. Security settings")
	print("4. Restore factory settings")

	settings_menu = int(input("Select an option: "))
	
	if settings_menu == 1:
		print("1. Automatic redial")
		print("2. Speed dialling")
		print("3. Call waiting options")
		print("4. Own number sending")
		print("5. Phone line in use")
		print("6. Automatic answer")

		call_settings_menu = int(input("Select an option: "))
		
		if call_settings_menu == 1:
			print("Automatic redial")

		if call_settings_menu == 2:
			print("Speed dialling")

		if call_settings_menu == 3:
			print("Call waiting options")

		if call_settings_menu == 4:
			print("Own number sending")
	
		if call_settings_menu == 5:
			print("Phone line in use")

		if call_settings_menu == 6:
			print("Automatic answer")

	if settings_menu == 2:
		print("1. Language")
		print("2. Cell info display")
		print("3. Welcome note")
		print("4. Network selection")
		print("5. Lights")
		print("6. Confirm SIM service actions")

		phone_settings_menu = int(input("Select an option: "))
		
		if phone_settings_menu == 1:
			print("Language")

		if phone_settings_menu == 2:
			print("Cell info display")

		if phone_settings_menu == 3:
			print("Welcome note")

		if phone_settings_menu == 4:
			print("Network selection")
	
		if phone_settings_menu == 5:
			print("Lights")

		if phone_settings_menu == 6:
			print("Confirm SIM service actions")

	if settings_menu == 3:
		print("1. PIN code request")
		print("2. Call barrring service")
		print("3. Fixed dialling")
		print("4. Closer user group")
		print("5. Phone security")
		print("6. Change access codes")

		security_settings_menu = int(input("Select an option: "))
		
		if security_settings_menu == 1:
			print("PIN code request")

		if security_settings_menu == 2:
			print("Call barring service")

		if security_settings_menu == 3:
			print("Fixed dialling")

		if security_settings_menu == 4:
			print("Closed user group")
	
		if security_settings_menu == 5:
			print("Phone security")

		if security_settings_menu == 6:
			print("Change access codes")

	if settings_menu == 4:
		print("Restore factory settings")

if menu == 7:
	print("Call divert")

if menu == 8:
	print("Games")

if menu == 9:
	prnit("Calculator")

if menu == 10:
	print("Reminders")

if menu == 11:
	print("1. Alarm Clock")
	print("2. Clock settings")
	print("3. Date settings")
	print("4. Stopwatch")
	print("5. Countdown timer")
	print("6. Auto update of date and time")

	clock = int(input("Select an option: "))

	if clock == 1:
		print("Alarm clock")

	if clock == 2:
		print("Clock settings")

	if clock == 3:
		print("Date setting")

	if clock == 4:
		print("Stopwatch")

	if clock == 5:
		print("Countdown timer")

	if clock == 6:
		print("Auto update of date and time")
		
if menu == 12:
	print("Profiles")

if menu == 13:
	print("SIM services")













