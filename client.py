class VoiceCallDtmfToneIvrNavigatorClient:
    def navigate_ivr_menu(self, spoken_menu_prompt='For billing press 1, for technical support press 2, for customer service press 3', desired_department='TECHNICAL_SUPPORT'):
        digit = '2' if 'technical' in desired_department.lower() else '1'
        return {
            'navigation_id': 'ivr_nav_5519',
            'detected_menu_options': {'1': 'billing', '2': 'technical support', '3': 'customer service'},
            'target_department': desired_department,
            'dtmf_tone_emitted': digit,
            'tone_frequency_hz': [770, 1336],
            'menu_traversal_successful': True,
            'call_session_graph_url': 'https://twilio.ivr.genpark.ai/sessions/5519.json'
        }
