---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackCursor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackCursor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackCursor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Descending bidegree scan for rank

The scan asks for one coefficient at a time and returns the first outer degree
with a nonzero coefficient. One transition updates the two indices, or halts
with the exact rank. Its fixed bit-stack code receives the zero-test flag
from the scalar routine.


### `State`

 State of the descending coefficient search, recording a current rank and degree or the
finished rank. 

### `advance`

 Return the current rank for a nonzero coefficient. On zero, move to the previous degree or
restart at degree `Z` for the previous rank. 

### `step`

 Perform one coefficient test on a running cursor and keep a finished cursor at its recorded
rank. 

### `control`

 Six-output dispatch tree implementing one transition of the descending rank cursor. 

### `input`

 Encode the zero-test result, current rank, current degree and degree limit in the cursor's
eight input words. 

### `State.words`

 Encode a running cursor or final rank as six output words with the status tag first. 

### `peak`

 Maximum of the first `n` values of a natural-valued stream, starting from zero. 

### `row`

 Contribution of rank `u` from the first `count` degree tests, equal to `u` if any
coefficient is nonzero. 

### `below`

 Largest candidate rank strictly below `u` for which the zero test fails at some degree from
zero through `Z`, defaulting to zero. 

### `answer`

 Rank represented by the cursor, taking the maximum over the remaining search region or
returning the finished value. 

### `remaining`

 Exact number of remaining requests if all remaining coefficients vanish. 

### `run`

 Deterministic recursion asks for at most the entire rectangle of scalar
queries. Its halting value is the maximum nonzero outer degree. 

### `physical`

 All index updates and the stopping decision on one scalar zero-test flag
run on a fixed binary-stack routine. 
