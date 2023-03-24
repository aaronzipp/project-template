"""
Docstring for this test file.

```python
test = sum(1, 2)
```
"""
import logging

import pandas as pd

logging.basicConfig(format="%(asctime)s\n%(message)s", level=logging.INFO)

example_list = list(range(3))

example_df = pd.DataFrame(
    {
        "a": example_list,
        "b": [0, 1, 0],
        "c": [lambda x: x**2, example_list],
    },
)

logging.info(example_df)
