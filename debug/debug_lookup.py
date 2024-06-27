# -*- coding: utf-8 -*-

import sqlalchemy as sa
from acore_df.api import Lookup

lookup = Lookup.new()

print(lookup.item_template_class.get(0))
print(lookup.item_template_class.get_by_kvs(kvs=dict(name="Consumable")))
with lookup.engine.connect() as conn:
    stmt = sa.select(lookup.item_template_class.orm_table)
    for row in conn.execute(stmt):
        print(row)
