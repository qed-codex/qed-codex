---
{
  "module": "OAI/Computability/VPVNP/PairSimulationFieldRead.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationFieldRead.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationFieldRead.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading a padded motif field in private RAM

Incident bit strings occupy consecutive private cells. The reader scans a
little-endian field from its high end, doubling its accumulator before adding
the next bit. A private comparison selects a load inside the string and a
literal zero beyond it. Both paths take six instructions per bit.


### `instruction`

 Registers hold the accumulator, descending cursor, field start, data
end, one, and a temporary bit. All three addresses are absolute. 

### `Linked`

 Require the seven padded-field reader instructions at the assigned labels and registers.
The descending scan doubles the accumulator and adds either the private bit or a padding
zero before returning to its loop test. 

### `template`

 A concrete register file and instruction table. Its eighth instruction
returns the result word in register zero. 

### `readField_succ_last`

 Reading the highest bit last in the sum gives the descending Horner recursion. 

### `accumulate`

 Exact private execution with any initial accumulator. All registers
outside the accumulator, cursor and temporary, and all memory cells, are
preserved for the continuation. 

### `native_read`

 A zeroed accumulator and a field at most one word wide recover the
natural value. The prefix length agrees exactly with the abstract meter,
also for the empty field and for fields extending into padding. 
