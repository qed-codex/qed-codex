---
{
  "module": "OAI/Computability/VPVNP/RankQueryPlainRoot.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryPlainRoot.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryPlainRoot.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Full fixed Schur computation for Cramer minors

At a top-degree query of an ordinary square minor, each coefficient callback
reads one scalar at degree zero. The same finite register bank, power-basis
arithmetic, and bounded continuation stack implement every level.


### `machine`

 Schur stack machine for an ordinary square minor. Its entry callback reads a matrix scalar
at degree zero and supplies zero at higher degrees. 

### `descriptorClock`

 Time bound for describing one Schur node of an ordinary minor, allowing a plain scalar
callback whose matrix-entry reader has clock `B`. 

### `queryTime`

 Time bound for the bidegree `(n,0)` root query of an ordinary square minor, combining the
Schur traversal bound with the time per engine step. 

### `querySpace`

 Per-stack height bound for the bidegree `(n,0)` query, accounting for the Schur
continuation depth, initial auxiliary height `A` and peak `S` of a matrix-entry read. 

### `top_query`

 A true run of the fixed binary-stack machine, returning the top coefficient
of the minor pencil. The independent height bound of the input-entry reader
enters space, and its running time enters only the clock. 
