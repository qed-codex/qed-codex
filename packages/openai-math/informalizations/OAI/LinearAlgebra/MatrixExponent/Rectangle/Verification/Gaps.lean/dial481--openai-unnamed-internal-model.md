---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Verification/Gaps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Verification/Gaps.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Verification/Gaps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Restricting a public seed to finitely many outcomes

A retained set of mass greater than two thirds still strictly
separates every correct input from every incorrect one. The weights
need not be normalized again.



# Acceptance by a finite family of paths

A path is a conjunction on scalar coordinates. Both intermediate
registers and post-seed witnesses are existentially quantified.
A verifier is their finite disjunction. Its cost bounds the longest
path, even if a different path accepts each input.


### `Verifier.read`

 One accepting assignment continues to work on any change outside
the coordinates read by its path. 


# Finite arithmetic trees with equality branches

The initial auxiliary coordinates are existential witnesses. Each
arithmetic operation appends a register. Division branches on a
zero denominator and appends a register only on success.

