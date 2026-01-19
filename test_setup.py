# test_setup.py
import fastf1

# Testar carregamento de sessão
session = fastf1.get_session(2023, 'São Paulo', 'R')
print(f"✅ Sessão carregada: {session.event['EventName']} {session.event['EventDate']}")