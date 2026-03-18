FINGERPRINT_RULES = {
    "Linux": "Linux device",
    "Windows": "Windows device",
    "router": "Router / Network device",
    "printer": "Printer",
    # Dodatki dla kamer i IoT:
    "hikvision": "IP Camera (Hikvision)",
    "dahua": "IP Camera (Dahua)",
    "axis": "IP Camera (Axis)",
    "webcam": "Web Camera",
    "embedded": "Embedded IoT Device",
    "synology": "NAS Storage (Synology)",
    "qnap": "NAS Storage (QNAP)",
    "hp": "HP Device (likely printer)",
    "canon": "Canon Device (likely printer)"
}


PORT_RULES = {

    "22/tcp": "Linux / SSH device",
    "3389/tcp": "Windows device",
    "9100/tcp": "Network printer (JetDirect)",
    "631/tcp": "Printer / CUPS",
    "80/tcp": "Web device",
    "443/tcp": "Secure web device",
    "8080/tcp": "Python Web / Proxy Server",
    # Porty dla kamer i automatyki:
    "554/tcp": "IP Camera (RTSP Stream)",
    "8000/tcp": "IP Camera (Hikvision/DVR)",
    "37777/tcp": "IP Camera (Dahua)",
    "5000/tcp": "NAS / Synology Web Interface",
    "515/tcp": "Printer (LPD protocol)",
    "161/udp": "Network Device (SNMP)"
}
