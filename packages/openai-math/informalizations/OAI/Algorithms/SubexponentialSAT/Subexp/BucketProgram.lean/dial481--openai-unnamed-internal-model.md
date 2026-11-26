---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/BucketProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BucketProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BucketProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed bit program for one packing bucket

The input is a framed query followed by framed `(type key, vertex payload)`
records. The routine compares actual bit strings. It consumes all records,
keeps the query on port 2, and prepends matching framed payloads on port 5.
Supplying records in reverse vertex order produces the original bucket order.


### `scanLoop_eval`

 An actual structured execution of the EOF-controlled loop. 

### `command_eval`

 Parse the query once, then run the fixed record loop. 

### `program_trace`

 This is a trace of the actual fixed instruction table, including its halt. 

### `traceBudget_le`

 Polynomial bound in encoded data lengths, derived from the measured loop. 

### `ordered_bucket_trace`

 Reversing the serialized record order makes the bucket output preserve
the original vertex order. The full frame of every selected index is emitted. 

### `initial_ordered_trace`

 A raw-input trace: the query is supplied as the first frame on the input
stack, and all work stacks start empty. 

### `constructive_bucket_output`

 The encoded output agrees exactly with the executable constructive bucket. 

### `constructive_bucket_trace`

 The fixed bit program computes precisely the typed constructive bucket
when its records contain injectively encoded type keys. 

### `universalRows`

 Concrete records use the existing fixed-width universal-type encoding
and framed unary vertex indices. 

### `universal_bucket_trace`

 The actual fixed program computes a bucket of the universal-type labeling,
with a proved polynomial bound in the dimension and encoded type width. 
