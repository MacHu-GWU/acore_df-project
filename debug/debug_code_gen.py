# -*- coding: utf-8 -*-

from pathlib_mate import Path
from acore_df.code_gen.api import Dataset, generate_code

path_xlsx = Path("/Users/sanhehu/Downloads/azerothcore-dataframe.xlsx")
dataset_list = [
    Dataset(tab="item_template_class"),
    Dataset(tab="item_template_subclass"),
    Dataset(tab="item_template_quality"),
    Dataset(tab="item_template_bonding"),
    Dataset(tab="item_template_allowable_class"),
    Dataset(tab="item_template_stat_type", mapping={"type_id": "id"}),
    Dataset(tab="item_template_damage_type"),
    Dataset(tab="factions", id_col="faction_id"),
]
generate_code(path_xlsx, dataset_list)
