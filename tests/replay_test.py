import os

from replay.utils.session_handler import get_spark_session, State
from replay.splitters import LastNSplitter, TwoStageSplitter
import pandas as pd

if "HOME" not in os.environ:
    os.environ["HOME"] = os.environ.get("USERPROFILE", "")

spark = get_spark_session(1, 1)
state = State(spark)


data_frame = pd.DataFrame({"query_id": [1,1,1,2,2,2],
   "item_id": [1,2,3,1,2,3],
   "relevance": [1,2,3,4,5,6],
   "timestamp": [1,2,3,3,2,1]})


print(data_frame)


splitter = LastNSplitter(
    N=1,
    divide_column="query_id",
    query_column="query_id",
    strategy="interactions",
)

raw_test_events, raw_test_gt = splitter.split(data_frame)
raw_train_events = raw_test_events

print("\nОбучающие события:")
print(raw_train_events)
