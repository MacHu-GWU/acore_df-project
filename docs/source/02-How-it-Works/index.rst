How it Works
==============================================================================


Google Sheet
------------------------------------------------------------------------------
我维护着一个 `Google Sheet <https://docs.google.com/spreadsheets/d/1XevE2tFnjCSf0paizwanCJMgmBdChunCgAp7BvqqD0M/edit?gid=2078125107#gid=2078125107>`_, 它是这个项目的数据源. 这个 Google Sheet 是由我手动维护的.


Generate Code
------------------------------------------------------------------------------
当我觉得有必要发布新版本时, 我需要用 Google Sheet 中的数据重新生成代码. 我先将 Google Sheet 另存为 Xlsx (Excel) 文件. 然后运行 `debug_code_gen.py <https://github.com/MacHu-GWU/acore_df-project/blob/main/debug/debug_code_gen.py>`_ 脚本. 这个脚本中我会指定要将哪些 Tab 提取成 Dataset.

.. dropdown:: debug/debug_code_gen.py

    .. literalinclude:: ../../../debug/debug_code_gen.py
       :language: python
       :linenos:

这个脚本最终会生成一个 `acore_df/model.py <https://github.com/MacHu-GWU/acore_df-project/blob/main/acore_df/model.py>`_, 里面参考 Google Sheet 中的数据, 生成了 SqlAlchemy 的类和 DataClass 类. 然后提供了一个 :class:`~acore_df.model.Lookup` 类, 用于查询这些数据.

.. dropdown:: acore_df/model.py

    .. literalinclude:: ../../../acore_df/model.py
       :language: python
       :linenos:

生成了 Python 模块后就可以运行 `tests/test_lookup.py <https://github.com/MacHu-GWU/acore_df-project/blob/main/tests/test_lookup.py>`_ 单元测试确保我们新生成的代码能正常工作. 如果我们对 dataframe 造成了不可逆的修改, 则一定要在 ``release-history.rst`` 中记录下来.

.. dropdown:: tests/test_lookup.py

    .. literalinclude:: ../../../tests/test_lookup.py
       :language: python
       :linenos:


Release
------------------------------------------------------------------------------
当我更新完数据, 重新生成代码, 并完成单元测试后, 就可以发布了. 每次发布新版本时, 需要将位于 ``${HOME}/acore_df.sqlite`` (默认位置) 上传到 GitHub release. 这样在用户的机器上就能自动下载对应的数据了.

由于这是一个数据优先的项目, 任何对数据造成无法向后兼容的修改都需要发布新的大版本.
