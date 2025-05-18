

UPDATE 
	security
SET live_per_unit_cost = (SELECT (average_per_unit_cost+3) FROM securitysnapshot WHERE security_id = security.id)
where EXISTS ( SELECT average_per_unit_cost FROM securitysnapshot WHERE security_id = security.id)