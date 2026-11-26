---
{
  "module": "OAI/Computability/VPVNP/RankCursorSchur.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorSchur.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorSchur.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Calling the Schur coefficient machine from the rank cursor

One request stages the six root fields and invokes the shared Schur engine.
The resulting scalar occupies the engine result port in its native
polynomial-basis representation. The cursor registers, dimension words and
scratch retain their ready values for the following zero test.


### `rootQuery`

 The instruction table stages a root from cursor registers and calls the
same engine at every matrix dimension and every bidegree. 

### `rootQueryClock`

 Step bound for loading one Schur root and evaluating its coefficient, using the arity and
recursion-depth bounds of the Schur expansion. 

### `rootQuerySpace`

 Stack-height bound for staging the root fields and executing the Schur recursion for a
single coefficient. 

### `rootQueryClock_le`

 Bounding all three numerical query dimensions by `s` bits gives a
single exponential number of engine transitions. 

### `rootQuerySpace_le`

 Only logarithms of the matrix size and outer degree enter the height of
the suspended Schur frames. 

### `routeRoot_bounded`

 Install any certified run of the same engine. The combined bound depends
on the engine's space certificate separately from its number of transitions. 

### `rootQuery_bounded`

 The returned scalar is the requested formal coefficient of the reverse
characteristic polynomial. Time and stack bounds include the initial word
copies and the engine call. The external Schur actions enter through their
individual physical execution contracts. 

### `rootQuery_runs`

 Normal-return interface for callers that need the clock and scalar. 
