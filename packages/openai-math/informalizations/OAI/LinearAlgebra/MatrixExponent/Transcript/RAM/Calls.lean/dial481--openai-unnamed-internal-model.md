---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Transcript/RAM/Calls.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Transcript/RAM/Calls.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Transcript/RAM/Calls.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bit-addressed memory tapes

A row specifies an address, the bit before the access and the bit
after it. Initial contents are zero. Reads can write back the same
bit, and initialization by advice can be implemented by writes.



# Deterministic bit-graph programs with random-access memory

A gate sees a limited number of ordered arguments, plus one bit
of random-access memory. It produces one wire value and specifies
the new value of that cell. Returning the old value implements
read-only access. Gates may use constants and reuse any old wire.


### `Trace`

 The columns are the memory bit before and after the access and
the value on the gate's output wire. 

 # Adjacent accesses in stable address order 

### `previous`

 Any earlier access to this address lies no later than the previous
row in sorted order, which then has the same address. 

 # Computing all the local checks in stable address order 

 # Trivalent verification of a named memory tape 

### `weight`

 One zero-one weight verifies every read against the most recent
write to the same address, with no multiplicity in any characteristic. 


# A weighted deterministic processor

Tap the output wires to check acceptance and to supply the arguments
of the installed dictionary tables. The only internal guesses are two
constant wires and the three columns of the execution. Their consistency
checks leave exactly one assignment, in every characteristic.


### `products`

 The factors only see the wires intended as their arguments. 

### `build`

 All RAM operations and bounded-arity Boolean gates are trivalent.
The table set need only contain labels already used by the output factors. 


# Dyadic dictionary seats

The active bit distinguishes an empty call from an unused seat.
Lengths are explicit and each width uses one common table label.
Uniformity is in the choice of the dictionary as well as the slot.


### `Processor`

 A processor with bounded total charge reserves the indicated
number of seats at each length. Taps can include final memory reads. 


# Packing variable-length calls

Every call costs at least one bit of charge. Within each dyadic bucket
we use an initial segment of the installed seats, in issuance order.
Unused seats contribute one.


### `Issuance`

 A slot stores the ordinal of its call, or a sentinel for an unused seat. 
