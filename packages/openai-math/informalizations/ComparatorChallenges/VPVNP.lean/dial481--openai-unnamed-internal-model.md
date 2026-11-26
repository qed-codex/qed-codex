---
{
  "module": "ComparatorChallenges/VPVNP.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Exact VP and VNP over every field 

### `Computes`

 A table of `s` binary gates computes `p`. Variables and scalars are free, and the
output and later gates may reuse any previously available value. 

### `PolynomiallyBounded`

 A polynomial bound uniform in all sufficiently large indices. 

### `Family`

 At each index a family has its own finite type of indeterminates. 

### `PFamily`

 Arity and total degree grow at most polynomially with the index. 

### `IsVP`

 VP consists of polynomial families computed by polynomial-size exact circuits. 

### `IsVNP`

 A VNP family sums a VP verifier over all Boolean assignments to its witness variables. 

### `vp_ne_vnp`

 The two nonuniform classes differ over each field. 
