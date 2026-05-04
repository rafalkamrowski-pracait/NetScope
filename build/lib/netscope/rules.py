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
    # Protokoły przestarzałe (Clear-text)
    "21/tcp": "[KRYTYCZNE] FTP - Dane i hasła przesyłane tekstem jawnym.",
    "23/tcp": "[KRYTYCZNE] Telnet - Brak szyfrowania! Użyj SSH.",
    "80/tcp": "[ŚREDNIE] HTTP - Brak szyfrowania strony.",

    # Zdalny dostęp
    "22/tcp": "[INFO] SSH - Bezpieczny dostęp (sprawdź czy nie ma Brute-Force).",
    "3389/tcp": "[WYSOKIE] RDP - Pulpit zdalny. Główny wektor Ransomware!",
    "5900/tcp": "[WYSOKIE] VNC - Zdalny pulpit. Często słabe hasła.",

    # Usługi Windows i pliki
    "135/tcp": "[ŚREDNIE] RPC - Często skanowany pod kątem mapowania sieci.",
    "139/tcp": "[WYSOKIE] NetBIOS - Ryzyko wycieku nazw użytkowników.",
    "445/tcp": "[KRYTYCZNE] SMB - Ryzyko EternalBlue. Nie wystawiaj do sieci!",

    # Bazy danych
    "1433/tcp": "[WYSOKIE] MSSQL Server - Baza danych dostępna z zewnątrz.",
    "3306/tcp": "[WYSOKIE] MySQL - Ryzyko nieautoryzowanego dostępu.",
    "5432/tcp": "[WYSOKIE] PostgreSQL - Sprawdź konfigurację uwierzytelniania.",

    # Twoje kamery i IoT (zachowane z Twojego kodu)
    "554/tcp": "[INFO] RTSP Stream - Strumień wideo kamer IP.",
    "8000/tcp": "[INFO] IP Camera (Hikvision/DVR).",
    "37777/tcp": "[INFO] IP Camera (Dahua).",
    "5000/tcp": "[INFO] NAS / Synology Web Interface",
    "161/udp": "[WYSOKIE] SNMP - Ryzyko wycieku konfiguracji urządzenia."
}
