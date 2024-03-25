"""
Docstring for this test file.

```python
from example_utils import sum

test = sum(1, 2)

assert test == 3
```
"""

import logging

import pandas as pd
from example_utils import sum

logging.basicConfig(format="%(asctime)s\n%(message)s", level=logging.INFO)

example_list = list(range(3))

example_df = pd.DataFrame(
    {
        "a": example_list,
        "b": [0, 1, sum(1, 1)],
        "c": [x**2 for x in example_list],
    },
)

logging.info(example_df)
