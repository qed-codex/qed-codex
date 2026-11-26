---
{
  "module": "OAI/Computability/VPVNP/PairSimulationStackCalls.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationStackCalls.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationStackCalls.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact branch streams of a bounded bit-stack call

A stack call consumes one supplied bit at each binary choice. A halting
instruction returns its status, stack bank, remaining instruction fuel and
unused suffix. Section 13 can therefore run the next local test on the same
stream. The complete accepted words form a finite set of cardinality exactly
the bounded accepting path count of the stack code.


### `Exit`

 State at a genuine halt. The final halt itself has spent one unit of fuel. 

### `Exit.accept`

 Boolean status of the halt reached by the bounded stack call. 

### `Exit.state`

 Stack-code control state at which the halt instruction was executed. 

### `Exit.bank`

 Contents of each named bit stack when the call halted. 

### `Exit.rest`

 Suffix of the input choice stream left unconsumed at the halt. 

### `Exit.unused`

 Instruction fuel remaining after charging the final halt instruction. 

### `parse`

 A binary choice reads one bit, including when its two successors coincide.
Running out of fuel or choices before a halt returns `none`. 

### `haltPrefix`

 Keep the suffix of a call which halted with the required status. 

### `acceptPrefix`

 Return the unused choice suffix when bounded stack execution reaches an accepting halt, and
return `none` otherwise. 

### `haltWords`

 Complete streams halting with the selected status. A one-bit tag keeps
the two branch slots disjoint even when both continue at the same state. 

### `acceptedWords`

 Finite set of exact choice words that lead from the supplied control state and stack bank
to an accepting halt within the fuel bound. 

### `haltPrefix_iff`

 Every accepting or rejecting halt reads exactly one complete word for
its status. The suffix can begin immediately with another stack call. 

### `CompleteStreams`

 Distinct words accepted with an empty remaining suffix. 

### `parse_append`

 An extension of a halted input changes only the unused suffix. In
particular, the stack bank and fuel handed to the next subroutine are the
ones obtained by running the complete consumed word in isolation. 

### `parse_split`

 Recover the complete consumed word and the exact exit configuration
from an arbitrary halted stream. 

### `parse_runs`

 A deterministic stack segment leaves the branch stream untouched and
hands all remaining fuel to its successor. 
