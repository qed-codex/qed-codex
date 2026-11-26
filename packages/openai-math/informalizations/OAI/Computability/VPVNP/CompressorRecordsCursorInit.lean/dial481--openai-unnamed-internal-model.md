---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsCursorInit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsCursorInit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsCursorInit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Installing the scheduler row for the cursor incidence scan

The initializer reads eight public words. It multiplies the degree, cursor
count and two binary radices to obtain the loop count. Successive additions
give the starts of the six incidence columns. A single burst then writes the
worker tag, first row, row count and the worker's eleven parameters.


### `inputs`

 Row address, worker tag, degree, cursor count, low radix, lane radix,
arc width and first column address, in that order. 

### `setup`

 Registers zero through seven cache the public inputs. Register eight holds
the row count, and nine through thirteen hold the remaining column starts. 

### `ops`

 Fixed instruction table for every width and every admissible cursor graph. 

### `events`

 All probes are writes in increasing row-field order. 

### `initialize_row`

 From arbitrary external memory the compiled call installs the complete row
read by the scheduler. Fields three through thirteen agree with the parameters
of the cursor scan at the same degree, address split, width and array start. 

### `stop_value`

 The scheduler reads the exact natural exclusive bound when it fits in a word. 
