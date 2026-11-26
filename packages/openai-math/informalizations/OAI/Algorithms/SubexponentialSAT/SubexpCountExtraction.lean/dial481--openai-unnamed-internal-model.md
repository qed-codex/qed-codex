---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpCountExtraction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCountExtraction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCountExtraction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Runtime extraction of the constant coefficient word

The wire format is a framed list of polynomial coefficients, in increasing
degree order.  Each coefficient is a framed list of its four little-endian
base-ring words.  A fixed program selects the first record twice, restores the
word order, clears its work stacks, and preserves the modulus on stack five.

The input representation is an explicit boundary: this module does not assert
that an arithmetic callback returning a Lean list has already serialized it.


### `headCmd`

 Select one list record, discard the rest, and restore its original order. 

### `head_records_eval`

 A semantic description of the result is justified by an actual parser trace. 

### `program`

 This fixed 39-label table operates on arbitrarily long encoded coefficient lists. 

### `firstCode_of_denote_eq`

 The only arithmetic selection step: a dense polynomial's zeroth
  coefficient is the decoded head, with a proved encoded zero for an empty list. 

 ## Link the actual parser to the actual remainder-and-positivity program 

### `count_decision_run`

 All semantic premises concern the represented polynomial returned by CRT;
the transition from its encoded list to the answer is an actual finite program. 

### `count_primitive_decision`

 The compiled primitive tape machine reaches the correct Boolean answer
from the explicitly encoded polynomial and prepared modulus. 
