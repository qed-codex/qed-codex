---
{
  "module": "OAI/Computability/VPVNP/ParseOracleRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseOracleRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseOracleRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Deterministic stack execution of the grammar coefficient query

One fixed bit-stack control enumerates event flags and evaluates the advised circuit
on the word and binary histogram coordinates. The output stack contains the full
integer coefficient in little-endian binary. The supplied advice depends on the
table dimensions, root and coordinate ordering, independently of the queried values.


### `Flags`

 The number of candidate event flags, one for each bounded event code on the paired
variables and grammar states. 

### `checker`

 Circuit supplied as advice. Its ordered gate stream is independent of both
the input word and the queried monomial. 

### `coefficient_query_runs`

 Space and per-candidate time hold along every intermediate machine step.
The accepting flags are counted once each, including when several have the
same histogram. 

### `coefficient_query_value`

 The result bits represent the full integer, since the number of satisfying flag
words is at most two to the width of the enumeration. 
