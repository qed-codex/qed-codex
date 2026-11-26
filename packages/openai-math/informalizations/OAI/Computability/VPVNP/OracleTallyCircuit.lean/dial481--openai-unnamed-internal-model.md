---
{
  "module": "OAI/Computability/VPVNP/OracleTallyCircuit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/OracleTallyCircuit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/OracleTallyCircuit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Boolean circuit checking row counts

The coefficient oracle of §8.1 counts the selected terminal and production events.
Each event flag may increment the counts of any fixed set of rows. At each stage this
circuit maintains one bit for every row and every count from zero through the number
of flags. Its final layer compares those bits with the supplied one-hot target table.


### `Input`

 Flag wires followed by the row and count coordinates of the one-hot table. 

### `rowCount`

 Number of selected flags that are set in this row. 

### `RowCountsOK`

 The target marks exactly the attained count in each row. 

### `rowCountsOK_oneHot_iff`

 An all-zero target row for a count greater than `k` is rejected as well. 

### `counters`

 The completed table of attained counts, before checking the supplied target. 

### `frame`

 Finished network over both the flag bits and the queried target table. 

### `frame_eval_iff`

 The output rejects every differing entry, including extra marks in a target row. 

### `verifier`

 Deterministic transcript verifier for the row counts. 

### `frame_size_le`

 One constant-size local expression per live wire at every clock tick, followed by
one constant-size mismatch check per table entry and a disjunction. 

### `verifier_size_le`

 Size bound in the AND/NOT gate model used by the transcript verifier. 
