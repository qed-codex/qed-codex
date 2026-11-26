---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rounds/Local.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rounds/Local.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rounds/Local.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The graph interface to local concentration

Each index in `Cell h` identifies an independent block. Host positions
name cells and each station belongs to one cell of one block. The input
has positive arities and integral packets of width `R`. The output
reserves individual host slots for the stations and is padded to units
of width `u` before the beats.


### `Input.ranks`

 Optional local station and host keys for deterministic numbering. 

### `Concentrated`

 The graph and arity estimates needed from one summand. Here `D=2^d`
in applications. All implicit constants are bounded by `C`. 

### `LocalExpansion`

 The exact expansion and control-index count. Algorithmic locality
of the chosen terms is an additional requirement for realizing the sum. 

### `LocalLaw`

 Uniform local concentration uses a fixed finite extension for
planting and polynomially many field points for the motions. 
