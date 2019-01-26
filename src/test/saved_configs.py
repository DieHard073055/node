SAMPLE_CONFIG = {
	"version": "0.0.1",
	"device_endpoint": "00000000.0000.0000.0000.000000000000",
	"device_endpoint_index":0,
	"drivers":[
		{
			"name": "HealthMonitor",
			"module":"drivers.sensors.health_monitor.HealthMonitor",
			"params":[
				{
					"key":"cpu_temp_0",
					"type":"shell",
					"command":[
						"cat",
						"/sys/class/thermal/thermal_zone0/temp"
					]
				},
				{
					"key":"memory_available",
					"type":"shell",
					"command":[
						"cat",
						"/proc/meminfo",
						"|",
						"grep",
						"'MemAvailable'",
                                                "|",
                                                "awk",
                                                "'{print $2}'"
					]
				},
				{
					"key":"memory_total",
					"type":"shell",
					"command":[
						"cat",
						"/proc/meminfo",
						"|",
						"grep",
						"'MemTotal'",
                                                "|",
                                                "awk",
                                                "'{print $2}'"
					]
				},
				{
					"key":"memory_usage",
					"type":"calc",
					"calc":	{
						"operation":"sub",
						"keys":[
							"memory_total",
							"memory_free"
						]
					}
				}


			]
		}
	],
	"comms":{
		"module":"comms.mqtt.simple_mqtt_client.SimpleMQTTClient",
		"params":{
			"host":"localhost",
			"port":1883
		}
	},
	"update_interval":10
}
def get_config(value=0):
    return SAMPLE_CONFIG
