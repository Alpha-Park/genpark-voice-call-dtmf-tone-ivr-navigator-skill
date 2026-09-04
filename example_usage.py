from client import VoiceCallDtmfToneIvrNavigatorClient

def main():
    client = VoiceCallDtmfToneIvrNavigatorClient()
    res = client.navigate_ivr_menu('Press 1 for Sales, 2 for Support', 'TECHNICAL_SUPPORT')
    print('IVR Navigator: ' + res['navigation_id'] + ' (DTMF Digit: ' + res['dtmf_tone_emitted'] + ')')
    print('Department: ' + res['target_department'] + ' | Success: ' + str(res['menu_traversal_successful']))
    print('Graph URL: ' + res['call_session_graph_url'])

if __name__ == '__main__':
    main()
