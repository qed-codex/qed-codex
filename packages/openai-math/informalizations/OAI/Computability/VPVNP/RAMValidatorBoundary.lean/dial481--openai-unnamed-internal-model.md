---
{
  "module": "OAI/Computability/VPVNP/RAMValidatorBoundary.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMValidatorBoundary.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMValidatorBoundary.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A single pass over the local sorted RAM block

The predecessor register starts at the received last record. At each physical
slot the validator checks a possible read, latches the status, and replaces
the predecessor even if the current slot is padding. At the end it compares
this register with the outgoing field on sites that have a successor.


### `loop`

 The address argument counts the slots *after* the next slot, decreasing
from `B - 1` to zero. The physical offset is its reversal in `Fin B`. This
passes a constant-size index into a fixed buffer on each iteration. 

### `decrement`

 The loop counter is decremented by one in the machine word type. 

### `wordOffset`

 Machine-word offset of the next record in the allocated local array. 

### `wordLoop`

 An executable loop over a materialized array. The counter, the decrement,
and the subtraction that produces the next array offset use the machine word
type. Loop termination follows from the counter value. 

### `scan`

 Scan the site's sorted slots in increasing order. The second argument is
absent at the final site. A present field can itself contain padding. 

### `scan_ok_iff`

 The status for independently supplied incoming and outgoing fields. 

### `scan_spec`

 The counted local scan implements the boundary predicate of Lemma 10.1
on all message and record assignments. 

### `scan_cost`

 Every slot is visited once, including slots after a failing read check. 

### `WordTuple`

 The five fields of a physical slot occupy a fixed-size array. 

### `scanWords`

 Execute the same pass directly on a finite array of five-word tuples.
The bound on the buffer length is the representability of the initial word
counter. Every subsequent counter and offset fits by construction. 

### `scanWords_eq`

 Both decision and work agree with the parsed-slot scan. Unknown tags and
noncanonical payloads are included, with the parser's interpretation of each
tuple. Canonicality is enforced when loading shared messages. 
