
import csv
import pypd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def write_incidents_to_csv(csvfilename):
	'''
	function that gets all incidents and writes to csv file
	param: csvfilename - file name with csv extension
	return: csv file
	'''

	pypd.api_key = 'u+WJGmsUunQkGQakRezw'

	incidents = pypd.Incident.find() # get incidents

	csvdata = open(csvfilename, 'w')
	column_names = ['incident_id','incident_summary','incident_urgency','incident_status','created_at','incident_type','service_id','service_summary','escalation_policy_id','escalation_policy_summary', 'trigger_log_entry_summary', 'incident_url', 'assigned_to']
	writer = csv.DictWriter(csvdata, fieldnames=column_names)
	writer.writeheader()
	counter = 0
	for incident in incidents:
		row = {
			'incident_id': incident._data['id'],
			'incident_summary': incident._data['summary'],
			'incident_urgency': incident._data['urgency'],
			'incident_status': incident._data['status'],
			'created_at': incident._data['created_at'],
			'incident_type': incident._data['type'],
			'service_id': incident._data['service']['id'],
			'service_summary': incident._data['service']['summary'],
			'escalation_policy_id': incident._data['escalation_policy']['id'],
			'escalation_policy_summary': incident._data['escalation_policy']['summary'],
			'trigger_log_entry_summary': incident._data['first_trigger_log_entry']['summary'],
			'incident_url': incident._data['html_url'],
			'assigned_to': incident._data['assignments'][0]['assignee']['summary']
		}
		writer.writerow(row)
		counter += 1

	csvdata.close()
	logger.info(' {} incidents saved to csv file'.format(counter))

write_incidents_to_csv('incidents.csv')



