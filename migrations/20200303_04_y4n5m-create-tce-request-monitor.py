"""
create tce_request_monitor
"""

from yoyo import step

__depends__ = {'20200303_03_ga9Yd-create-orgaos'}

steps = [
    step(
        "create table tce_request_monitor ("
	        "id SERIAL PRIMARY KEY,"
	        "method varchar(10) UNIQUE,"
            "municipio_id integer,"
	        "year integer,"
            "month integer,"
	        "error varchar(255),"
            "success boolean,"
            "tries integer,"
            "created_at timestamp,"
            "updated_at timestamp"
        ")",
        "DROP TABLE tce_request_monitor",
    )
]
