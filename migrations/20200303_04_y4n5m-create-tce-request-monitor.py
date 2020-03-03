"""
create tce_request_monitor
"""

from yoyo import step

__depends__ = {'20200303_03_ga9Yd-create-orgaos'}

steps = [
    step(
        "create table tce_request_monitor ("
	        "id SERIAL PRIMARY KEY,"
	        "method varchar(10),"
	        "year integer,"
            "month integer,"
	        "error varchar(10),"
            "success boolean"
        ")",
        "DROP TABLE tce_request_monitor",
    )
]
