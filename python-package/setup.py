from pathlib import Path
from setuptools import setup, find_packages

# Define el directorio actual
cwd = Path(__file__).resolve().parent

# Lee los requisitos desde requirements.txt dentro de employee_events
requirements = (cwd / 'employee_events' / 'requirements.txt').read_text().split('\n')

# Define los argumentos para setup()
setup_args = dict(
    name='employee_events',
    version='0.0',
    description='SQL Query API',
    packages=find_packages(),
    package_data={'': ['employee_events.db', 'requirements.txt']},
    install_requires=requirements,  
)

if __name__ == "__main__":
    setup(**setup_args)
