import pandas as pd

person = pd.Series({'First': 'FIRSTNAME', 'Last': 'LASTNAME'})

print(f'Hello from {person['Vincent']} {person['Li']}')
