---
{
  "module": "OAI/Computability/VPVNP/RAMSuccessorDecodeCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSuccessorDecodeCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSuccessorDecodeCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word work to decode a successor message

The successor field of Lemma 10.1 comprises three control words and a five-word
record. The validator scans each word into a register once. It returns the parsed
successor together with a flag for equality with the canonical eight registers.
This separates parsing from rejection, including when the input is a clamped field.


### `scanEight`

 Each scan returns its word and operation count. The eight register writes are
charged once when saving the results. 

### `scanSuccessor`

 Parse the saved control and record fields and compare with the canonical words.
Allow 24 operations for dispatch (status, cost cap and up to three record tags)
and copying the payload. Allow 24 for forming the canonical control and record
words. Comparing eight registers costs at most six operations per register
(loop test, advance, two loads, equality and branch) plus the final test.
Returning the successor and flag costs two more writes. 
