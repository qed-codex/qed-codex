---
{
  "module": "OAI/Computability/VPVNP/LiveVirtualPairContinuation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveVirtualPairContinuation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveVirtualPairContinuation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# First-half continuation for the fixed program's virtual pair witness

The production nominations use the physical parser order. The paths and
increments are exactly those of `VirtualPairs.pairData`, computed with the
auxiliary machine's own private fuel. This supplies the pair argument of
`assembleLocalCertificate` once its local compressed calls have been realized.


### `compressedObligation`

 Compressed calls on the physical group, expressed with the fixed
program's mathematical dimensions and its exact path family. 

### `noncomputable local instance (n C : ℕ) : DecidableEq (JointLabelSystem.Production n C)`

 Classical decidable equality for the grammar productions at length n and circuit exponent
C, used locally to index production nominations. 

### `physicalNomination`

 Reindex the dense nomination array by the production labels of the
very same virtual coefficient counter. 

### `VirtualPairs.compressedCalls`

 The native obligation for the physical inputs of `VirtualPairs.witness`.
That witness uses `d.machine d.fuel 0 d.initial` with `d := V.data ...`.
Its dense increments combine the nominated grammar counts with the
compression-label counts of that exact choice. 

### `VirtualPairs.pairObligation`

 The canonical first-half argument of `assembleLocalCertificate`.
The only remaining stage-specific premise is the native realization and
budget of the compressed subroutine. 
