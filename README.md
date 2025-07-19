
# Software Engineering for Data Scientists 
# Proyecto actualizado

### ## Notas 
# dsnd-dashboard-project

Este proyecto es un dashboard interactivo desarrollado para el programa Data Scientist Nanodegree de Udacity, utilizando `FastHTML` y `SQLite`.

## 📦 Estructura del proyecto
```
├── README.md
├── assets
│   ├── model.pkl
│   └── report.css
├── env
├── python-package
│   ├── employee_events
│   │   ├── __init__.py
│   │   ├── employee.py
│   │   ├── employee_events.db
│   │   ├── query_base.py
│   │   ├── sql_execution.py
│   │   └── team.py
│   ├── requirements.txt
│   ├── setup.py
├── report
│   ├── base_components
│   │   ├── __init__.py
│   │   ├── base_component.py
│   │   ├── data_table.py
│   │   ├── dropdown.py
│   │   ├── matplotlib_viz.py
│   │   └── radio.py
│   ├── combined_components
│   │   ├── __init__.py
│   │   ├── combined_component.py
│   │   └── form_group.py
│   ├── dashboard.py
│   └── utils.py
├── requirements.txt
├── start
├── tests
    └── test_employee_events.py
```

### employee_events.db

```mermaid
erDiagram

  employee {
    INTEGER employee_id PK
    TEXT first_name
    TEXT last_name
    INTEGER team_id
    
  }

  employee_events {
    TEXT event_date
    INTEGER employee_id FK
    INTEGER team_id FK
    INTEGER positive_events
    INTEGER negative_events
  }

  notes {
    INTEGER employee_id PK
    INTEGER team_id PK
    TEXT note
    TEXT note_date PK
  }

  team {
    INTEGER team_id PK
    TEXT team_name
    TEXT shift
    TEXT manager_name
  }

  team ||--o{ employee_events : "team_id"
  employee ||--o{ employee_events : "employee_id"
  notes }o--o{ employee_events : ""
```


---


# 📊 Dashboard de Employee Events

## Instrucciones para ejecutar el proyecto

1️⃣ Clonar el repositorio:
```bash
git clone https://github.com/diegomejialleras99/dsnd-dashboard-project.git
cd dsnd-dashboard-project

2️⃣ Crear y activar un entorno virtual (opcional pero recomendado):

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # En Mac/Linux
venv\Scripts\activate     # En Windows

3️⃣ Instalar las dependencias:

bash
Copiar
Editar
pip install -r requirements.txt

4️⃣ Ejecutar la aplicación:

bash
Copiar
Editar
python report/dashboard.py

Al ejecutar el paso 4️⃣ aparecerá en la consola una dirección tipo http://0.0.0.0:5001/ que puedes abrir en tu navegador para ver el dashboard funcionando.
