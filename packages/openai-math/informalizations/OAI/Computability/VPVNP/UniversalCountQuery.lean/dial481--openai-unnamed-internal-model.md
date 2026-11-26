---
{
  "module": "OAI/Computability/VPVNP/UniversalCountQuery.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/UniversalCountQuery.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/UniversalCountQuery.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable coefficient queries for the universal path-count family

The coefficient query uses one fixed finite bit-stack control for all lengths.
Its only circuit-specific input is the unary-addressed gate stream. The final
binary count includes all and only accepting canonical choices. Both its width
and the maximum height of every intermediate stack are polynomial in the
length for the concrete coefficient verifier.


### `countCircuit`

 A fixed stack routine that enumerates all witnesses of the advised Boolean circuit and
returns their accepting count in binary. 

### `perChoice`

 Instruction budget per candidate witness, including the ripple counters. 

### `stackLimit`

 Space per stack, measured at every instruction of the full count. 

### `scalarInputs`

 Install the advice and query, leaving the verifier's work ports empty. 

### `countCircuit_runs`

 One uniform machine counts satisfying witnesses of any topologically ordered
Boolean circuit supplied on its advice port. Its control and number of stacks
are independent of all circuit parameters. 

### `coefficient_query_runs`

 The §8.1 constant-term oracle for the polynomial family (1.1), including
malformed input prefixes and early accepting halts. No interpreter assumptions
are required. The exact integer output is read by `count_digits_value`. 

### `coefficient_query_space`

 The entire physical bit-stack bank uses polynomial space, since the
program has a fixed finite number of ports. 

### `coefficient_query_time`

 A single polynomial exponent bounds the entire running time over all query words. 
