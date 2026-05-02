{
    "name": "Hospital Management",
    "version": "19.0.1.0.0",
    "category": "Hospital",
    "summary": "Comprehensive hospital management system",
    "author": "Evgen Cerkun",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "demo/hr_hospital_demo.xml",
        "data/hr_hospital_disease_data.xml",
        "views/hr_hospital_doctor_views.xml",
        "views/hr_hospital_patient_views.xml",
        "views/hr_hospital_disease_views.xml",
        "views/hr_hospital_visit_views.xml",
        "views/hr_hospital_menus.xml",
    ],
    "demo": [
        #"demo/hr_hospital_demo.xml",
    ],
    "installable": True,
    "application": True,
    'images':
        ['static/description/icon.png'],
}
